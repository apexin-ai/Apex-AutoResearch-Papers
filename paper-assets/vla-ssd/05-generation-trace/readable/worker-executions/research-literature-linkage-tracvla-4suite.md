# research literature linkage tracvla 4suite

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/workers/worker_research_literature-linkage-tracvla-4suite_20260521T204054.log`
- **Structured JSON:** [`3a73ff036cb4d35493cc.json`](../../sessions/3a/3a73ff036cb4d35493cc.json)

## Before a recorded user message

53 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd",
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
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
  "uuid": "29dd60a4-4839-4a86-ac7a-2f7bf2449507",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/memory/"
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
    "resetsAt": 1779412800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "2735cd64-c694-43f9-b989-5909e3aa203e",
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c"
}
```

---

### Assistant

_source line 4_

I'll start by reading the literature map and searching for relevant papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "4949a7e1-faaf-4711-84b3-0b80ad5298bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VcdBRkqgDZFnNA8bKqLuVd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11546,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11546
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HPJ98GZDJMwLn6uXibBXBR`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__append_idea,WebSearch,WebFetch",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "073f7c91-53d0-4c25-bc68-d2d55337fd0b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VcdBRkqgDZFnNA8bKqLuVd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11546,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11546
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

_source line 6 · 2026-05-21T20:41:03.492Z_

<details><summary>↩ Tool result · `toolu_01HPJ98GZDJMwLn6uXibBXBR`</summary>

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

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__append_idea"
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
  "tool_name": "WebFetch"
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
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "375e1ade-ab4d-42dc-9f1d-cfe469687734",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__append_idea",
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__append_idea,WebSearch,WebFetch",
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
Now let me read the literature map and do web searches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "f58f8ab4-7d7c-443b-ad8d-59a2ecfc5131",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01McKeCc2fkZymQASyz2s8v8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 23387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1909
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

### Assistant

_source line 8_

Reading literature map and launching web searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "a03f1743-7f56-4ae5-8dd6-a74ebbc82dde",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01McKeCc2fkZymQASyz2s8v8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 23387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1909
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

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01ErLL2aedhoKDtdsdfhFnVo`</summary>

```json
{
  "project": "vla-ssd",
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
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "13aee37c-def1-48aa-a4d0-18e065004c6c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01McKeCc2fkZymQASyz2s8v8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 23387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1909
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

_source line 10 · 2026-05-21T20:41:08.269Z_

<details><summary>↩ Tool result · `toolu_01ErLL2aedhoKDtdsdfhFnVo`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/literature_map.yaml\", \"content\": \"papers:\\n  # ============================================================\\n  # DIRECT COMPETITORS — VLA Representation Analysis / Interpretability\\n  # ============================================================\\n  - id: grant2026\\n    title: \\\"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models\\\"\\n    authors: \\\"Bryce Grant, Xijia Zhao, Peng Wang\\\"\\n    year: 2026\\n    venue: \\\"arXiv preprint (under review)\\\"\\n    arxiv_id: \\\"2603.19233\\\"\\n    category: direct-competitor\\n    role: competitor\\n    key_findings: >\\n      Visual pathway dominates action generation across all 6 tested VLA architectures (80M–7B params, 394K+ rollout episodes, 4 benchmarks).\\n      Language sensitivity depends on task structure: when visual context uniquely specifies the task, language is IGNORED;\\n      when multiple goals share a scene, language becomes essential (\\\"encoded but not used\\\").\\n      Cross-task activation injection steers robots toward source-task positions (99.8% trajectory alignment with source in X-VLA).\\n      Multi-pathway architectures (pi0.5, SmolVLA, GR00T) separate motor programs (expert pathway) from goal semantics (VLM pathway).\\n    relevance_to_us: >\\n      Most direct competitor. Behavioral intervention (activation injection, SAE, probing) reveals vision dominance + language encoded but not used.\\n      Uses OpenVLA-OFT checkpoint; we use standard fine-tuning — must qualify this difference in Related Work.\\n    novelty_gap: >\\n      No trained vs untrained representation analysis. They compare different model architectures,\\n      we compare trained vs untrained representation structure within the same architecture.\\n      Their \\\"encoded but not used\\\" is a behavioral-level conclusion; we demonstrate at the representation level\\n      that instruction conditioning comes from the input pathway, not training. Complementary work.\\n    notes: >\\n      Action Atlas interactive exploration tool released. 6 models: OpenVLA, X-VLA, pi0.5, SmolVLA, GR00T, Octo.\\n      OFT checkpoint difference may affect direct comparability.\\n\\n  - id: swann2026\\n    title: \\\"Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models\\\"\\n    authors: \\\"Aiden Swann, Lachlain McGranahan, Hugo Buurmeijer, Monroe Kennedy III, Mac Schwager\\\"\\n    year: 2026\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2603.19183\\\"\\n    category: direct-competitor\\n    role: competitor\\n    key_findings: >\\n      SAE features on OpenVLA: majority of extracted features correspond to memorized training sequences,\\n      but some correspond to interpretable, general, and steerable motion primitives and semantic properties.\\n    relevance_to_us: >\\n      Also OpenVLA interpretability work. They use SAE for feature-level decomposition,\\n      we use probing + RSA for representation-level analysis. Methodologically complementary.\\n    novelty_gap: >\\n      No language features analysis. No trained vs untrained comparison.\\n      Does not investigate source of instruction conditioning (input pathway vs training).\\n    notes: \\\"Stanford team. Published on arXiv same day as Grant 2026 (2026-03-19).\\\"\\n\\n  - id: rizzardo2026\\n    title: \\\"Observing and Controlling Features in Vision-Language-Action Models\\\"\\n    authors: \\\"Rizzardo et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2603.05487\\\"\\n    category: direct-competitor\\n    role: competitor\\n    key_findings: >\\n      Introduces feature-observability and feature-controllability concepts bridging LLM mechanistic\\n      interpretability and VLAs. Linear classifier observation + optimal-control-based minimal intervention steering.\\n      Validated on pi0.5 and OpenVLA — targeted interventions steer robot behavior while preserving closed-loop capabilities.\\n    relevance_to_us: >\\n      Also VLA internal representation analysis. They focus on how to steer,\\n      we focus on where conditioning comes from (input pathway vs training).\\n    novelty_gap: >\\n      No trained vs untrained comparison. No instruction pathway vs training separation analysis.\\n      Focuses on controllability rather than representation structure origin.\\n    notes: \\\"Submitted 2026-03-05.\\\"\\n\\n  - id: haon2025\\n    title: \\\"Mechanistic Interpretability for Steering Vision-Language-Action Models\\\"\\n    authors: \\\"Bear Haon, Kaylene Stocking, Ian Chuang, Claire Tomlin\\\"\\n    year: 2025\\n    venue: \\\"CoRL 2025\\\"\\n    arxiv_id: \\\"2509.00328\\\"\\n    category: direct-competitor\\n    role: methodology\\n    key_findings: >\\n      First VLA mechanistic interpretability framework. Projects feedforward activations onto token embedding basis,\\n      identifies sparse semantic directions (speed, direction) causally linked to action selection.\\n      Activation steering modulates behavior in real time without fine-tuning.\\n      Validated on Pi0 and OpenVLA in LIBERO (simulation) and UR5 (real robot).\\n    relevance_to_us: >\\n      Methodological reference: their activation steering proves VLAs have interpretable semantic directions.\\n      Our RSA/probing results can dialogue with their mechanistic findings.\\n    novelty_gap: >\\n      No trained vs untrained comparison. No systematic representation structure analysis (RSA/CKA).\\n      Focuses on individual semantic direction causal intervention, not overall structure comparison.\\n    notes: \\\"CoRL 2025 accepted. Pioneering work in VLA interpretability.\\\"\\n\\n  - id: molinari2025\\n    title: \\\"Emergent World Representations in OpenVLA\\\"\\n    authors: \\\"Marco Molinari, Leonardo Nevali, Saharsha Navani, Omar G. Younis\\\"\\n    year: 2025\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2509.24559\\\"\\n    category: direct-competitor\\n    role: context\\n    key_findings: >\\n      OpenVLA implicitly learns a world model. Embedding arithmetic tests state transition knowledge;\\n      linear/non-linear probes show statistically significant state transition prediction ability across layers.\\n      SAE pipeline analyzes fine-grained world model structure.\\n    relevance_to_us: >\\n      Also OpenVLA probing work. They study world model, we study instruction conditioning.\\n      Their layer-wise probe results can be compared with our layer-wise RSA.\\n    novelty_gap: >\\n      No language/instruction analysis. No trained vs untrained comparison.\\n      Only focuses on state transitions, not goal/instruction representation.\\n    notes: \\\"Submitted 2025-09-29. Has OpenReview discussion.\\\"\\n\\n  - id: lu2025\\n    title: \\\"Probing a Vision-Language-Action Model for Symbolic States and Integration into a Cognitive Architecture\\\"\\n    authors: \\\"Hong Lu, Hengxu Li, Prithviraj Singh Shahani, Stephanie Herbers, Matthias Scheutz\\\"\\n    year: 2025\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2502.04558\\\"\\n    category: direct-competitor\\n    role: methodology\\n    key_findings: >\\n      Probes OpenVLA hidden layers to extract symbolic representations (object properties, relations, action states).\\n      LIBERO-spatial pick-and-place probing accuracy > 0.90 across most layers.\\n      Integration with cognitive architecture improves interpretability and robustness.\\n    relevance_to_us: >\\n      Directly related methodology: both use linear probes on OpenVLA layers on LIBERO.\\n      Their finding that symbolic states are decodable (>0.90) is consistent with our goal classification at 100%.\\n    novelty_gap: >\\n      Only trained model probing, no untrained control.\\n      Only LIBERO-spatial single task, no cross-task/cross-condition analysis.\\n      No instruction conditioning source analysis.\\n    notes: \\\"Submitted 2025-02-06. Tufts University.\\\"\\n\\n  - id: fang_intention2025\\n    title: \\\"From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models\\\"\\n    authors: \\\"Irving Fang, Juexiao Zhang, Shengbang Tong, Chen Feng\\\"\\n    year: 2025\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2506.09930\\\"\\n    category: direct-competitor\\n    role: context\\n    key_findings: >\\n      Unified probing suite (50 simulation tasks, 10 subcategories) evaluating VLA generalization boundaries.\\n      VLM backbone provides robust perceptual understanding + high-level planning (good intentions),\\n      but cannot reliably translate to precise motor execution (perception-to-action gap).\\n      Action data fine-tuning erodes original VLM generalist reasoning abilities.\\n    relevance_to_us: >\\n      \\\"Fine-tuning erodes VLM reasoning\\\" echoes our \\\"training doesn't improve representation\\\" finding.\\n      They discover intention != execution at behavioral level; we discover\\n      training ~= untrained in representation structure.\\n    novelty_gap: >\\n      Behavioral-level probing (success rates), not representation-level analysis.\\n      No trained vs untrained representation structure comparison.\\n    notes: \\\"Submitted 2025-06-11. INT-ACT benchmark open-sourced. NYU/ai4ce team.\\\"\\n\\n  # ============================================================\\n  # DIRECT COMPETITORS — Language Grounding / Counterfactual\\n  # ============================================================\\n  - id: fang_cf2026\\n    title: \\\"When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs\\\"\\n    authors: \\\"Yu Fang, Yuchun Feng, Dong Jing, Jiaqi Liu, Yue Yang, Zhenyu Wei, Daniel Szafir, Mingyu Ding\\\"\\n    year: 2026\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2602.17659\\\"\\n    category: direct-competitor\\n    role: competitor\\n    key_findings: >\\n      Introduces LIBERO-CF counterfactual benchmark. VLAs exhibit severe counterfactual failures:\\n      vision shortcuts + dataset biases cause models to ignore language intent.\\n      OpenVLA-OFT: 4.7% grounding rate, 0.4% success rate.\\n      Best model: 30.8% grounding rate, 13.2% success rate.\\n      Proposes Counterfactual Action Guidance (CAG) dual-branch inference scheme.\\n    relevance_to_us: >\\n      Directly validates \\\"language encoded but not used\\\" severity under counterfactual settings.\\n      Their behavioral findings complement our representation-level findings.\\n      They test OpenVLA-OFT — same checkpoint issue as Grant 2026.\\n    novelty_gap: >\\n      Pure behavioral benchmark, no representation analysis.\\n      No trained vs untrained comparison. No instruction pathway causal analysis.\\n    notes: \\\"Submitted 2026-02-19. LIBERO-CF has 4 sub-suites (CF-Spatial, CF-Object, CF-Long, CF-OOD).\\\"\\n\\n  - id: hou2026\\n    title: \\\"LangGap: Diagnosing and Closing the Language Gap in Vision-Language-Action Models\\\"\\n    authors: \\\"Yuchen Hou, Lin Zhao\\\"\\n    year: 2026\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2603.00592\\\"\\n    category: direct-competitor\\n    role: context\\n    key_findings: >\\n      SOTA VLAs achieve >95% on standard benchmarks but largely ignore language instructions.\\n      Four-dimensional semantic perturbation method exposes language understanding deficits.\\n      LIBERO assigns only 1 task per layout, so models dont need to understand language.\\n      LangGap benchmark forces multi-task shared layouts; data augmentation improves from 0% to 90%.\\n    relevance_to_us: >\\n      Systematic diagnosis of \\\"VLAs ignore language\\\" supports our story:\\n      instruction conditioning comes from input pathway, not training — even trained VLAs dont truly leverage language.\\n    novelty_gap: >\\n      Behavioral-level diagnosis + data augmentation solution. No representation analysis.\\n      No trained vs untrained comparison. No input pathway causal analysis.\\n    notes: \\\"Submitted 2026-02-28. GitHub open-sourced.\\\"\\n\\n  # ============================================================\\n  # METHOD COMPONENT — RSA, CKA, Linear Probing\\n  # ============================================================\\n  - id: kriegeskorte2008\\n    title: \\\"Representational Similarity Analysis - Connecting the Branches of Systems Neuroscience\\\"\\n    authors: \\\"Nikolaus Kriegeskorte, Marieke Mur, Peter Bandettini\\\"\\n    year: 2008\\n    venue: \\\"Frontiers in Systems Neuroscience\\\"\\n    arxiv_id: null\\n    doi: \\\"10.3389/neuro.06.004.2008\\\"\\n    category: method-component\\n    role: methodology\\n    key_findings: >\\n      Introduces Representational Dissimilarity Matrix (RDM) framework for comparing multi-channel\\n      neural activity measurements with computational models and behavior.\\n      Validated on fMRI visual cortex data.\\n    relevance_to_us: \\\"RSA is one of our core analysis methods for comparing trained/untrained/DINO representation structures.\\\"\\n    novelty_gap: null\\n    notes: \\\"Original RSA paper. 5000+ citations.\\\"\\n\\n  - id: kornblith2019\\n    title: \\\"Similarity of Neural Network Representations Revisited\\\"\\n    authors: \\\"Simon Kornblith, Mohammad Norouzi, Honglak Lee, Geoffrey Hinton\\\"\\n    year: 2019\\n    venue: \\\"ICML 2019\\\"\\n    arxiv_id: \\\"1905.00414\\\"\\n    category: method-component\\n    role: methodology\\n    key_findings: >\\n      Introduces Centered Kernel Alignment (CKA) as representation similarity metric.\\n      CKA reliably identifies representation correspondences across differently initialized networks,\\n      outperforming CCA-based methods.\\n    relevance_to_us: >\\n      CKA is one of our core tools for comparing trained vs untrained representations.\\n      Deep-layer CKA reaching 0.86 demonstrates high representation similarity.\\n    novelty_gap: null\\n    notes: \\\"Google Brain. CKA is now standard for representation comparison.\\\"\\n\\n  - id: alain2017\\n    title: \\\"Understanding Intermediate Layers Using Linear Classifier Probes\\\"\\n    authors: \\\"Guillaume Alain, Yoshua Bengio\\\"\\n    year: 2017\\n    venue: \\\"ICLR 2017 Workshop\\\"\\n    arxiv_id: \\\"1610.01644\\\"\\n    category: method-component\\n    role: methodology\\n    key_findings: >\\n      Proposes linear classifier probes to monitor feature suitability for classification at every layer.\\n      Linear separability increases monotonically along network depth.\\n      Validated on Inception v3 and ResNet-50.\\n    relevance_to_us: \\\"Linear probing is the methodological foundation for our goal classification and action prediction experiments.\\\"\\n    novelty_gap: null\\n    notes: \\\"Foundational probing methodology work.\\\"\\n\\n  # ============================================================\\n  # VISION ENCODERS — SigLIP, DINOv2, CLIP\\n  # ============================================================\\n  - id: zhai2023_siglip\\n    title: \\\"Sigmoid Loss for Language Image Pre-Training\\\"\\n    authors: \\\"Xiaohua Zhai, Basil Mustafa, Alexander Kolesnikov, Lucas Beyer\\\"\\n    year: 2023\\n    venue: \\\"ICCV 2023\\\"\\n    arxiv_id: \\\"2303.15343\\\"\\n    category: vision-encoder\\n    role: baseline\\n    verified: true\\n    key_findings: >\\n      Replaces softmax contrastive loss with pairwise sigmoid loss for VL pretraining.\\n      Eliminates global batch normalization, enabling smaller batch training.\\n      SigLIP-SO400M achieves competitive zero-shot performance with simpler training.\\n    relevance_to_us: >\\n      SigLIP-SO400M is OpenVLA's frozen vision encoder. Our RSA=0.615 for SigLIP+Projector\\n      shows this encoder provides dominant action-relevant geometric structure.\\n    novelty_gap: null\\n    notes: \\\"Google. OpenVLA uses SigLIP-SO400M/14 variant.\\\"\\n\\n  - id: oquab2024_dinov2\\n    title: \\\"DINOv2: Learning Robust Visual Features without Supervision\\\"\\n    authors: \\\"Maxime Oquab, Timothée Darcet, Théo Moutakanni, et al.\\\"\\n    year: 2024\\n    venue: \\\"TMLR 2024\\\"\\n    arxiv_id: \\\"2304.07193\\\"\\n    category: vision-encoder\\n    role: baseline\\n    verified: true\\n    key_findings: >\\n      Self-supervised ViT trained on curated 142M image dataset (LVD-142M).\\n      Produces general-purpose features competitive with task-specific models.\\n      No language supervision — purely vision self-supervised.\\n    relevance_to_us: >\\n      Vision-only baseline in our analysis. DINO RSA=0.388 << SigLIP 0.615,\\n      but DINO R²=0.712 ≈ Projector R²=0.706 — key geometric-functional dissociation.\\n    novelty_gap: null\\n    notes: \\\"Meta AI. DINOv2 ViT-L/14 used as vision-only control.\\\"\\n\\n  - id: radford2021_clip\\n    title: \\\"Learning Transferable Visual Models From Natural Language Supervision\\\"\\n    authors: \\\"Alec Radford, Jong Wook Kim, Chris Hallacy, et al.\\\"\\n    year: 2021\\n    venue: \\\"ICML 2021\\\"\\n    arxiv_id: \\\"2103.00020\\\"\\n    category: vision-encoder\\n    role: baseline\\n    verified: true\\n    key_findings: >\\n      Contrastive language-image pretraining on 400M image-text pairs.\\n      Zero-shot transfer competitive with supervised baselines.\\n      Pioneering VL pretraining approach.\\n    relevance_to_us: >\\n      CLIP ViT-L/14 RSA=0.557 confirms VL pretraining universality:\\n      both CLIP (0.557) and SigLIP+Proj (0.615) >> DINO (0.388).\\n      Action-relevant geometric structure is a universal product of VL pretraining.\\n    novelty_gap: null\\n    notes: \\\"OpenAI. CLIP ViT-L/14 used as VL pretraining generalization control (plan_012).\\\"\\n\\n  # ============================================================\\n  # BACKGROUND — VLM Design, Frozen Encoders, Multi-modal Fusion\\n  # ============================================================\\n  - id: karamcheti2024\\n    title: \\\"Prismatic VLMs: Investigating the Design Space of Visually-Conditioned Language Models\\\"\\n    authors: \\\"Siddharth Karamcheti, Suraj Nair, Ashwin Balakrishna, Percy Liang, Thomas Kollar, Dorsa Sadigh\\\"\\n    year: 2024\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2402.07865\\\"\\n    category: background\\n    role: baseline\\n    key_findings: >\\n      Systematic investigation of VLM design space: pretrained visual representations, base vs instruct-tuned LM, etc.\\n      Different vision encoder ensembles (SigLIP, DINOv2) improve performance.\\n      OpenVLA is directly built on the Prismatic architecture.\\n    relevance_to_us: >\\n      OpenVLA's VLM backbone origin. The SigLIP+DINOv2 fusion design choice\\n      is the architectural basis for our analysis of \\\"frozen vision encoder carries instruction conditioning.\\\"\\n    novelty_gap: >\\n      VLM design space exploration, no VLA-specific representation analysis.\\n      No trained vs untrained comparison.\\n    notes: \\\"Significant author overlap with OpenVLA team.\\\"\\n\\n  - id: vla_survey2025\\n    title: \\\"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges\\\"\\n    authors: \\\"Multiple authors\\\"\\n    year: 2025\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2505.04769\\\"\\n    category: background\\n    role: context\\n    key_findings: >\\n      Comprehensive survey of 100+ VLA architectures, 26 major VLA datasets.\\n      Large-scale quantitative analysis linking model design choices to normalized performance.\\n      Covers fusion strategy, action representation, encoder selection.\\n    relevance_to_us: \\\"Provides VLA landscape for positioning our work in the representation analysis sub-direction.\\\"\\n    novelty_gap: \\\"Survey, no original experimental analysis.\\\"\\n    notes: \\\"Most comprehensive VLA survey as of 2025-05.\\\"\\n\\n  # ============================================================\\n  # EVALUATION — LIBERO Benchmark Ecosystem\\n  # ============================================================\\n  - id: liu2023_libero\\n    title: \\\"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\\\"\\n    authors: \\\"Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023\\\"\\n    arxiv_id: \\\"2306.03310\\\"\\n    category: evaluation\\n    role: baseline\\n    key_findings: >\\n      130 tasks across 4 suites (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long).\\n      Procedural generation + skill blending + human teleoperation demonstrations.\\n      Lifelong learning benchmark with knowledge transfer evaluation.\\n    relevance_to_us: \\\"Our primary experimental platform. LIBERO-10 (fine-tuning) + LIBERO-Goal (OOD test).\\\"\\n    novelty_gap: null\\n    notes: \\\"NeurIPS 2023 Datasets and Benchmarks track.\\\"\\n\\n  - id: fei2025_libero_plus\\n    title: \\\"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\\\"\\n    authors: \\\"Senyu Fei, Siyin Wang, Junhao Shi, et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2510.13626\\\"\\n    category: evaluation\\n    role: context\\n    key_findings: >\\n      7-dimension controlled perturbations expose VLA fragility.\\n      Performance drops from 95% to <30% (camera viewpoint, robot initial state most sensitive).\\n      Models are insensitive to language variations — largely ignore language instructions.\\n      Positional bias over genuine semantic understanding.\\n    relevance_to_us: >\\n      \\\"Models ignore language instructions\\\" is consistent with our finding that\\n      training doesnt improve representation structure — VLAs have not truly learned language grounding.\\n    novelty_gap: \\\"Behavioral robustness analysis, no representation-level analysis.\\\"\\n    notes: \\\"Submitted 2025-10. OpenMOSS team.\\\"\\n\\n  - id: zhou2025_libero_pro\\n    title: \\\"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization\\\"\\n    authors: \\\"Xueyang Zhou, Yangming Xu, Guiyao Tie, et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2510.03827\\\"\\n    category: evaluation\\n    role: context\\n    key_findings: >\\n      Standard LIBERO >90% accuracy, but generalized setting collapses to 0.0%.\\n      Exposes reliance on rote memorization (action sequences + environment layouts)\\n      rather than genuine task understanding or environmental perception.\\n    relevance_to_us: >\\n      \\\"Memorization not understanding\\\" supports our story:\\n      VLA training improves action sequence memorization, not representation structure.\\n    novelty_gap: \\\"Behavioral evaluation, no representation analysis.\\\"\\n    notes: \\\"Submitted 2025-10.\\\"\\n\\n  - id: libero_para2026\\n    title: \\\"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models\\\"\\n    authors: \\\"Multiple authors\\\"\\n    year: 2026\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2603.28301\\\"\\n    category: evaluation\\n    role: context\\n    key_findings: >\\n      7 VLA configurations (0.6B-7.5B) show 22-52pp performance degradation under paraphrasing.\\n      80-96% of failures from planning-level trajectory divergence (not execution errors),\\n      indicating paraphrasing disrupts task identification.\\n      Synonym substitution alone causes large drops — relies on surface-level matching, not semantic grounding.\\n    relevance_to_us: >\\n      Further confirms VLAs lack true language grounding.\\n      Complements our \\\"instruction conditioning comes from input pathway structure, not semantic training.\\\"\\n    novelty_gap: \\\"Paraphrase robustness diagnosis, no representation analysis.\\\"\\n    notes: \\\"Submitted 2026-03-30.\\\"\\n\\n  # ============================================================\\n  # RELATED ARCHITECTURE — VLA Models\\n  # ============================================================\\n  - id: kim2024_openvla\\n    title: \\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\"\\n    authors: \\\"Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2406.09246\\\"\\n    category: related-architecture\\n    role: baseline\\n    key_findings: >\\n      7B-param VLA trained on 970k real-world robot demonstrations (Open X-Embodiment).\\n      Llama 2 7B backbone + DINOv2+SigLIP fused vision encoder.\\n      Outperforms RT-2-X (55B) by 16.5% absolute with 7x fewer parameters.\\n    relevance_to_us: >\\n      Our analysis target. All probing/RSA/CKA experiments use OpenVLA-7B.\\n      Architecture details (frozen SigLIP, Llama 2 backbone) directly affect our interpretation\\n      of \\\"input pathway vs training.\\\"\\n    novelty_gap: null\\n    notes: \\\"Stanford/Toyota/Google. Open-source checkpoints + training code.\\\"\\n\\n  - id: brohan2023_rt2\\n    title: \\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\"\\n    authors: \\\"Anthony Brohan et al.\\\"\\n    year: 2023\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2307.15818\\\"\\n    category: related-architecture\\n    role: context\\n    key_findings: >\\n      Co-fine-tunes VLM (PaLM-E 55B) on robotic trajectory data + internet-scale VL tasks.\\n      Robot actions represented as text tokens.\\n      Demonstrates emergent capabilities: novel object generalization, chain-of-thought reasoning.\\n    relevance_to_us: >\\n      Pioneering VLA architecture. RT-2 uses PaLM-E, OpenVLA uses Llama 2,\\n      but shares the \\\"LLM backbone + frozen vision encoder\\\" core design.\\n      Our findings may generalize to similar architectures.\\n    novelty_gap: \\\"No representation analysis. No trained vs untrained comparison.\\\"\\n    notes: \\\"Google DeepMind. 55B params, not open-source.\\\"\\n\\n  - id: ghosh2024_octo\\n    title: \\\"Octo: An Open-Source Generalist Robot Policy\\\"\\n    authors: \\\"Octo Model Team, Dibya Ghosh, Homer Walke, Karl Pertsch, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2405.12213\\\"\\n    category: related-architecture\\n    role: context\\n    key_findings: >\\n      Transformer-based diffusion policy pretrained on 800k robot episodes (Open X-Embodiment).\\n      Lightweight CNN vision encoder + language model for text instructions.\\n      27M (Small) / 93M (Base) params, consumer GPU fine-tuning.\\n    relevance_to_us: >\\n      Alternative VLA architecture (not LLM-based). Grant 2026 tests include Octo.\\n      If our findings generalize to Octo, the input pathway effect is cross-architectural.\\n    novelty_gap: \\\"No representation analysis. No frozen encoder analysis.\\\"\\n    notes: \\\"Berkeley. Author overlap with OpenVLA.\\\"\\n\\n  - id: black2024_pi0\\n    title: \\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\"\\n    authors: \\\"Kevin Black et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2410.24164\\\"\\n    category: related-architecture\\n    role: context\\n    key_findings: >\\n      Flow matching action head (not autoregressive tokens), 50Hz continuous trajectories.\\n      Pre-trained VLM backbone + flow matching combination.\\n      7 robotic platforms, 68 tasks. Real-world dexterous manipulation.\\n    relevance_to_us: >\\n      pi0 uses continuous flow matching vs discrete tokens — different action representation.\\n      Grant 2026 and Haon 2025 both tested Pi0/pi0.5, enabling cross-reference with our OpenVLA results.\\n    novelty_gap: \\\"No representation structure analysis.\\\"\\n    notes: \\\"Physical Intelligence. Commercial frontier VLA.\\\"\\n\\n# ============================================================\\n# CATEGORY INDEX\\n# ============================================================\\ncategories:\\n  direct-competitor:\\n    description: \\\"VLA representation / interpretability / language grounding analysis\\\"\\n    papers:\\n      - grant2026\\n      - swann2026\\n      - rizzardo2026\\n      - haon2025\\n      - molinari2025\\n      - lu2025\\n      - fang_intention2025\\n      - fang_cf2026\\n      - hou2026\\n\\n  method-component:\\n    description: \\\"RSA, CKA, linear probing methodological references\\\"\\n    papers:\\n      - kriegeskorte2008\\n      - kornblith2019\\n      - alain2017\\n\\n  vision-encoder:\\n    description: \\\"Vision encoder architectures used in our analysis (SigLIP, DINOv2, CLIP)\\\"\\n    papers:\\n      - zhai2023_siglip\\n      - oquab2024_dinov2\\n      - radford2021_clip\\n\\n  background:\\n    description: \\\"VLM design space, frozen encoder effects, multi-modal fusion\\\"\\n    papers:\\n      - karamcheti2024\\n      - vla_survey2025\\n\\n  evaluation:\\n    description: \\\"LIBERO benchmark ecosystem and VLA robustness evaluation\\\"\\n    papers:\\n      - liu2023_libero\\n      - fei2025_libero_plus\\n      - zhou2025_libero_pro\\n      - libero_para2026\\n\\n  related-architecture:\\n    description: \\\"VLA model architectures (OpenVLA, RT-2, Octo, pi0)\\\"\\n    papers:\\n      - kim2024_openvla\\n      - brohan2023_rt2\\n      - ghosh2024_octo\\n      - black2024_pi0\\n\\n# ============================================================\\n# SYNTHESIS: OUR NOVELTY POSITION\\n# ============================================================\\nsynthesis:\\n  our_core_claim: \\\"Instruction Input Pathway Drives Conditioning, Not Training\\\"\\n\\n  what_others_have_done:\\n    behavioral_level:\\n      - \\\"Grant 2026: vision pathway dominates, language 'encoded but not used' (activation injection)\\\"\\n      - \\\"LIBERO-CF/LangGap/LIBERO-Plus: VLAs ignore language instructions (counterfactual/robustness tests)\\\"\\n      - \\\"LIBERO-PRO: models rely on memorization not understanding\\\"\\n      - \\\"Fang 2025: fine-tuning erodes VLM reasoning (intention != execution)\\\"\\n    representation_level:\\n      - \\\"Swann 2026: SAE features mostly memorized sequences, some interpretable (OpenVLA)\\\"\\n      - \\\"Molinari 2025: world model emerges in middle layers (OpenVLA)\\\"\\n      - \\\"Lu 2025: symbolic states decodable with >0.90 accuracy (OpenVLA + LIBERO)\\\"\\n      - \\\"Haon 2025: sparse semantic directions causally linked to actions (Pi0 + OpenVLA)\\\"\\n      - \\\"Rizzardo 2026: feature-observability and controllability (pi0.5 + OpenVLA)\\\"\\n\\n  what_nobody_has_done:\\n    - \\\"Trained vs untrained VLA representation comparison (we find trained ~= untrained >> DINO)\\\"\\n    - \\\"Instruction input pathway vs LLM training separation analysis (6 probing rounds + RSA all consistent)\\\"\\n    - \\\"Systematic layer-wise RSA/CKA comparison of trained/untrained/DINO representation structures\\\"\\n    - \\\"Instruction ablation causal verification: removing instruction drops RSA to DINO level\\\"\\n\\n  key_differentiation_from_grant2026: >\\n    Grant 2026 compares different VLA models (architectural differences);\\n    we compare trained vs untrained within the same model (training effect isolation).\\n    Grant finds \\\"language encoded but not used\\\" (behavioral level);\\n    we find \\\"conditioning comes from input pathway, not training\\\" (representation level).\\n    Complementary, not competing. Related Work must qualify OFT vs standard fine-tuning difference.\\n\", \"total_chars\": 29243, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "79cc8576-74dd-46a1-84bb-78b594b57448",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/literature_map.yaml\\\", \\\"content\\\": \\\"papers:\\\\n  # ============================================================\\\\n  # DIRECT COMPETITORS — VLA Representation Analysis / Interpretability\\\\n  # ============================================================\\\\n  - id: grant2026\\\\n    title: \\\\\\\"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Bryce Grant, Xijia Zhao, Peng Wang\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv preprint (under review)\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2603.19233\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    key_findings: >\\\\n      Visual pathway dominates action generation across all 6 tested VLA architectures (80M–7B params, 394K+ rollout episodes, 4 benchmarks).\\\\n      Language sensitivity depends on task structure: when visual context uniquely specifies the task, language is IGNORED;\\\\n      when multiple goals share a scene, language becomes essential (\\\\\\\"encoded but not used\\\\\\\").\\\\n      Cross-task activation injection steers robots toward source-task positions (99.8% trajectory alignment with source in X-VLA).\\\\n      Multi-pathway architectures (pi0.5, SmolVLA, GR00T) separate motor programs (expert pathway) from goal semantics (VLM pathway).\\\\n    relevance_to_us: >\\\\n      Most direct competitor. Behavioral intervention (activation injection, SAE, probing) reveals vision dominance + language encoded but not used.\\\\n      Uses OpenVLA-OFT checkpoint; we use standard fine-tuning — must qualify this difference in Related Work.\\\\n    novelty_gap: >\\\\n      No trained vs untrained representation analysis. They compare different model architectures,\\\\n      we compare trained vs untrained representation structure within the same architecture.\\\\n      Their \\\\\\\"encoded but not used\\\\\\\" is a behavioral-level conclusion; we demonstrate at the representation level\\\\n      that instruction conditioning comes from the input pathway, not training. Complementary work.\\\\n    notes: >\\\\n      Action Atlas interactive exploration tool released. 6 models: OpenVLA, X-VLA, pi0.5, SmolVLA, GR00T, Octo.\\\\n      OFT checkpoint difference may affect direct comparability.\\\\n\\\\n  - id: swann2026\\\\n    title: \\\\\\\"Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models\\\\\\\"\\\\n    authors: \\\\\\\"Aiden Swann, Lachlain McGranahan, Hugo Buurmeijer, Monroe Kennedy III, Mac Schwager\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2603.19183\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    key_findings: >\\\\n      SAE features on OpenVLA: majority of extracted features correspond to memorized training sequences,\\\\n      but some correspond to interpretable, general, and steerable motion primitives and semantic properties.\\\\n    relevance_to_us: >\\\\n      Also OpenVLA interpretability work. They use SAE for feature-level decomposition,\\\\n      we use probing + RSA for representation-level analysis. Methodologically complementary.\\\\n    novelty_gap: >\\\\n      No language features analysis. No trained vs untrained comparison.\\\\n      Does not investigate source of instruction conditioning (input pathway vs training).\\\\n    notes: \\\\\\\"Stanford team. Published on arXiv same day as Grant 2026 (2026-03-19).\\\\\\\"\\\\n\\\\n  - id: rizzardo2026\\\\n    title: \\\\\\\"Observing and Controlling Features in Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Rizzardo et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2603.05487\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    key_findings: >\\\\n      Introduces feature-observability and feature-controllability concepts bridging LLM mechanistic\\\\n      interpretability and VLAs. Linear classifier observation + optimal-control-based minimal intervention steering.\\\\n      Validated on pi0.5 and OpenVLA — targeted interventions steer robot behavior while preserving closed-loop capabilities.\\\\n    relevance_to_us: >\\\\n      Also VLA internal representation analysis. They focus on how to steer,\\\\n      we focus on where conditioning comes from (input pathway vs training).\\\\n    novelty_gap: >\\\\n      No trained vs untrained comparison. No instruction pathway vs training separation analysis.\\\\n      Focuses on controllability rather than representation structure origin.\\\\n    notes: \\\\\\\"Submitted 2026-03-05.\\\\\\\"\\\\n\\\\n  - id: haon2025\\\\n    title: \\\\\\\"Mechanistic Interpretability for Steering Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Bear Haon, Kaylene Stocking, Ian Chuang, Claire Tomlin\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"CoRL 2025\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2509.00328\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: methodology\\\\n    key_findings: >\\\\n      First VLA mechanistic interpretability framework. Projects feedforward activations onto token embedding basis,\\\\n      identifies sparse semantic directions (speed, direction) causally linked to action selection.\\\\n      Activation steering modulates behavior in real time without fine-tuning.\\\\n      Validated on Pi0 and OpenVLA in LIBERO (simulation) and UR5 (real robot).\\\\n    relevance_to_us: >\\\\n      Methodological reference: their activation steering proves VLAs have interpretable semantic directions.\\\\n      Our RSA/probing results can dialogue with their mechanistic findings.\\\\n    novelty_gap: >\\\\n      No trained vs untrained comparison. No systematic representation structure analysis (RSA/CKA).\\\\n      Focuses on individual semantic direction causal intervention, not overall structure comparison.\\\\n    notes: \\\\\\\"CoRL 2025 accepted. Pioneering work in VLA interpretability.\\\\\\\"\\\\n\\\\n  - id: molinari2025\\\\n    title: \\\\\\\"Emergent World Representations in OpenVLA\\\\\\\"\\\\n    authors: \\\\\\\"Marco Molinari, Leonardo Nevali, Saharsha Navani, Omar G. Younis\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2509.24559\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: context\\\\n    key_findings: >\\\\n      OpenVLA implicitly learns a world model. Embedding arithmetic tests state transition knowledge;\\\\n      linear/non-linear probes show statistically significant state transition prediction ability across layers.\\\\n      SAE pipeline analyzes fine-grained world model structure.\\\\n    relevance_to_us: >\\\\n      Also OpenVLA probing work. They study world model, we study instruction conditioning.\\\\n      Their layer-wise probe results can be compared with our layer-wise RSA.\\\\n    novelty_gap: >\\\\n      No language/instruction analysis. No trained vs untrained comparison.\\\\n      Only focuses on state transitions, not goal/instruction representation.\\\\n    notes: \\\\\\\"Submitted 2025-09-29. Has OpenReview discussion.\\\\\\\"\\\\n\\\\n  - id: lu2025\\\\n    title: \\\\\\\"Probing a Vision-Language-Action Model for Symbolic States and Integration into a Cognitive Architecture\\\\\\\"\\\\n    authors: \\\\\\\"Hong Lu, Hengxu Li, Prithviraj Singh Shahani, Stephanie Herbers, Matthias Scheutz\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2502.04558\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: methodology\\\\n    key_findings: >\\\\n      Probes OpenVLA hidden layers to extract symbolic representations (object properties, relations, action states).\\\\n      LIBERO-spatial pick-and-place probing accuracy > 0.90 across most layers.\\\\n      Integration with cognitive architecture improves interpretability and robustness.\\\\n    relevance_to_us: >\\\\n      Directly related methodology: both use linear probes on OpenVLA layers on LIBERO.\\\\n      Their finding that symbolic states are decodable (>0.90) is consistent with our goal classification at 100%.\\\\n    novelty_gap: >\\\\n      Only trained model probing, no untrained control.\\\\n      Only LIBERO-spatial single task, no cross-task/cross-condition analysis.\\\\n      No instruction conditioning source analysis.\\\\n    notes: \\\\\\\"Submitted 2025-02-06. Tufts University.\\\\\\\"\\\\n\\\\n  - id: fang_intention2025\\\\n    title: \\\\\\\"From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Irving Fang, Juexiao Zhang, Shengbang Tong, Chen Feng\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2506.09930\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: context\\\\n    key_findings: >\\\\n      Unified probing suite (50 simulation tasks, 10 subcategories) evaluating VLA generalization boundaries.\\\\n      VLM backbone provides robust perceptual understanding + high-level planning (good intentions),\\\\n      but cannot reliably translate to precise motor execution (perception-to-action gap).\\\\n      Action data fine-tuning erodes original VLM generalist reasoning abilities.\\\\n    relevance_to_us: >\\\\n      \\\\\\\"Fine-tuning erodes VLM reasoning\\\\\\\" echoes our \\\\\\\"training doesn't improve representation\\\\\\\" finding.\\\\n      They discover intention != execution at behavioral level; we discover\\\\n      training ~= untrained in representation structure.\\\\n    novelty_gap: >\\\\n      Behavioral-level probing (success rates), not representation-level analysis.\\\\n      No trained vs untrained representation structure comparison.\\\\n    notes: \\\\\\\"Submitted 2025-06-11. INT-ACT benchmark open-sourced. NYU/ai4ce team.\\\\\\\"\\\\n\\\\n  # ============================================================\\\\n  # DIRECT COMPETITORS — Language Grounding / Counterfactual\\\\n  # ============================================================\\\\n  - id: fang_cf2026\\\\n    title: \\\\\\\"When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs\\\\\\\"\\\\n    authors: \\\\\\\"Yu Fang, Yuchun Feng, Dong Jing, Jiaqi Liu, Yue Yang, Zhenyu Wei, Daniel Szafir, Mingyu Ding\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2602.17659\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    key_findings: >\\\\n      Introduces LIBERO-CF counterfactual benchmark. VLAs exhibit severe counterfactual failures:\\\\n      vision shortcuts + dataset biases cause models to ignore language intent.\\\\n      OpenVLA-OFT: 4.7% grounding rate, 0.4% success rate.\\\\n      Best model: 30.8% grounding rate, 13.2% success rate.\\\\n      Proposes Counterfactual Action Guidance (CAG) dual-branch inference scheme.\\\\n    relevance_to_us: >\\\\n      Directly validates \\\\\\\"language encoded but not used\\\\\\\" severity under counterfactual settings.\\\\n      Their behavioral findings complement our representation-level findings.\\\\n      They test OpenVLA-OFT — same checkpoint issue as Grant 2026.\\\\n    novelty_gap: >\\\\n      Pure behavioral benchmark, no representation analysis.\\\\n      No trained vs untrained comparison. No instruction pathway causal analysis.\\\\n    notes: \\\\\\\"Submitted 2026-02-19. LIBERO-CF has 4 sub-suites (CF-Spatial, CF-Object, CF-Long, CF-OOD).\\\\\\\"\\\\n\\\\n  - id: hou2026\\\\n    title: \\\\\\\"LangGap: Diagnosing and Closing the Language Gap in Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Yuchen Hou, Lin Zhao\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2603.00592\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: context\\\\n    key_findings: >\\\\n      SOTA VLAs achieve >95% on standard benchmarks but largely ignore language instructions.\\\\n      Four-dimensional semantic perturbation method exposes language understanding deficits.\\\\n      LIBERO assigns only 1 task per layout, so models dont need to understand language.\\\\n      LangGap benchmark forces multi-task shared layouts; data augmentation improves from 0% to 90%.\\\\n    relevance_to_us: >\\\\n      Systematic diagnosis of \\\\\\\"VLAs ignore language\\\\\\\" supports our story:\\\\n      instruction conditioning comes from input pathway, not training — even trained VLAs dont truly leverage language.\\\\n    novelty_gap: >\\\\n      Behavioral-level diagnosis + data augmentation solution. No representation analysis.\\\\n      No trained vs untrained comparison. No input pathway causal analysis.\\\\n    notes: \\\\\\\"Submitted 2026-02-28. GitHub open-sourced.\\\\\\\"\\\\n\\\\n  # ============================================================\\\\n  # METHOD COMPONENT — RSA, CKA, Linear Probing\\\\n  # ============================================================\\\\n  - id: kriegeskorte2008\\\\n    title: \\\\\\\"Representational Similarity Analysis - Connecting the Branches of Systems Neuroscience\\\\\\\"\\\\n    authors: \\\\\\\"Nikolaus Kriegeskorte, Marieke Mur, Peter Bandettini\\\\\\\"\\\\n    year: 2008\\\\n    venue: \\\\\\\"Frontiers in Systems Neuroscience\\\\\\\"\\\\n    arxiv_id: null\\\\n    doi: \\\\\\\"10.3389/neuro.06.004.2008\\\\\\\"\\\\n    category: method-component\\\\n    role: methodology\\\\n    key_findings: >\\\\n      Introduces Representational Dissimilarity Matrix (RDM) framework for comparing multi-channel\\\\n      neural activity measurements with computational models and behavior.\\\\n      Validated on fMRI visual cortex data.\\\\n    relevance_to_us: \\\\\\\"RSA is one of our core analysis methods for comparing trained/untrained/DINO representation structures.\\\\\\\"\\\\n    novelty_gap: null\\\\n    notes: \\\\\\\"Original RSA paper. 5000+ citations.\\\\\\\"\\\\n\\\\n  - id: kornblith2019\\\\n    title: \\\\\\\"Similarity of Neural Network Representations Revisited\\\\\\\"\\\\n    authors: \\\\\\\"Simon Kornblith, Mohammad Norouzi, Honglak Lee, Geoffrey Hinton\\\\\\\"\\\\n    year: 2019\\\\n    venue: \\\\\\\"ICML 2019\\\\\\\"\\\\n    arxiv_id: \\\\\\\"1905.00414\\\\\\\"\\\\n    category: method-component\\\\n    role: methodology\\\\n    key_findings: >\\\\n      Introduces Centered Kernel Alignment (CKA) as representation similarity metric.\\\\n      CKA reliably identifies representation correspondences across differently initialized networks,\\\\n      outperforming CCA-based methods.\\\\n    relevance_to_us: >\\\\n      CKA is one of our core tools for comparing trained vs untrained representations.\\\\n      Deep-layer CKA reaching 0.86 demonstrates high representation similarity.\\\\n    novelty_gap: null\\\\n    notes: \\\\\\\"Google Brain. CKA is now standard for representation comparison.\\\\\\\"\\\\n\\\\n  - id: alain2017\\\\n    title: \\\\\\\"Understanding Intermediate Layers Using Linear Classifier Probes\\\\\\\"\\\\n    authors: \\\\\\\"Guillaume Alain, Yoshua Bengio\\\\\\\"\\\\n    year: 2017\\\\n    venue: \\\\\\\"ICLR 2017 Workshop\\\\\\\"\\\\n    arxiv_id: \\\\\\\"1610.01644\\\\\\\"\\\\n    category: method-component\\\\n    role: methodology\\\\n    key_findings: >\\\\n      Proposes linear classifier probes to monitor feature suitability for classification at every layer.\\\\n      Linear separability increases monotonically along network depth.\\\\n      Validated on Inception v3 and ResNet-50.\\\\n    relevance_to_us: \\\\\\\"Linear probing is the methodological foundation for our goal classification and action prediction experiments.\\\\\\\"\\\\n    novelty_gap: null\\\\n    notes: \\\\\\\"Foundational probing methodology work.\\\\\\\"\\\\n\\\\n  # ============================================================\\\\n  # VISION ENCODERS — SigLIP, DINOv2, CLIP\\\\n  # ============================================================\\\\n  - id: zhai2023_siglip\\\\n    title: \\\\\\\"Sigmoid Loss for Language Image Pre-Training\\\\\\\"\\\\n    authors: \\\\\\\"Xiaohua Zhai, Basil Mustafa, Alexander Kolesnikov, Lucas Beyer\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"ICCV 2023\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2303.15343\\\\\\\"\\\\n    category: vision-encoder\\\\n    role: baseline\\\\n    verified: true\\\\n    key_findings: >\\\\n      Replaces softmax contrastive loss with pairwise sigmoid loss for VL pretraining.\\\\n      Eliminates global batch normalization, enabling smaller batch training.\\\\n      SigLIP-SO400M achieves competitive zero-shot performance with simpler training.\\\\n    relevance_to_us: >\\\\n      SigLIP-SO400M is OpenVLA's frozen vision encoder. Our RSA=0.615 for SigLIP+Projector\\\\n      shows this encoder provides dominant action-relevant geometric structure.\\\\n    novelty_gap: null\\\\n    notes: \\\\\\\"Google. OpenVLA uses SigLIP-SO400M/14 variant.\\\\\\\"\\\\n\\\\n  - id: oquab2024_dinov2\\\\n    title: \\\\\\\"DINOv2: Learning Robust Visual Features without Supervision\\\\\\\"\\\\n    authors: \\\\\\\"Maxime Oquab, Timothée Darcet, Théo Moutakanni, et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"TMLR 2024\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2304.07193\\\\\\\"\\\\n    category: vision-encoder\\\\n    role: baseline\\\\n    verified: true\\\\n    key_findings: >\\\\n      Self-supervised ViT trained on curated 142M image dataset (LVD-142M).\\\\n      Produces general-purpose features competitive with task-specific models.\\\\n      No language supervision — purely vision self-supervised.\\\\n    relevance_to_us: >\\\\n      Vision-only baseline in our analysis. DINO RSA=0.388 << SigLIP 0.615,\\\\n      but DINO R²=0.712 ≈ Projector R²=0.706 — key geometric-functional dissociation.\\\\n    novelty_gap: null\\\\n    notes: \\\\\\\"Meta AI. DINOv2 ViT-L/14 used as vision-only control.\\\\\\\"\\\\n\\\\n  - id: radford2021_clip\\\\n    title: \\\\\\\"Learning Transferable Visual Models From Natural Language Supervision\\\\\\\"\\\\n    authors: \\\\\\\"Alec Radford, Jong Wook Kim, Chris Hallacy, et al.\\\\\\\"\\\\n    year: 2021\\\\n    venue: \\\\\\\"ICML 2021\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2103.00020\\\\\\\"\\\\n    category: vision-encoder\\\\n    role: baseline\\\\n    verified: true\\\\n    key_findings: >\\\\n      Contrastive language-image pretraining on 400M image-text pairs.\\\\n      Zero-shot transfer competitive with supervised baselines.\\\\n      Pioneering VL pretraining approach.\\\\n    relevance_to_us: >\\\\n      CLIP ViT-L/14 RSA=0.557 confirms VL pretraining universality:\\\\n      both CLIP (0.557) and SigLIP+Proj (0.615) >> DINO (0.388).\\\\n      Action-relevant geometric structure is a universal product of VL pretraining.\\\\n    novelty_gap: null\\\\n    notes: \\\\\\\"OpenAI. CLIP ViT-L/14 used as VL pretraining generalization control (plan_012).\\\\\\\"\\\\n\\\\n  # ============================================================\\\\n  # BACKGROUND — VLM Design, Frozen Encoders, Multi-modal Fusion\\\\n  # ============================================================\\\\n  - id: karamcheti2024\\\\n    title: \\\\\\\"Prismatic VLMs: Investigating the Design Space of Visually-Conditioned Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Siddharth Karamcheti, Suraj Nair, Ashwin Balakrishna, Percy Liang, Thomas Kollar, Dorsa Sadigh\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2402.07865\\\\\\\"\\\\n    category: background\\\\n    role: baseline\\\\n    key_findings: >\\\\n      Systematic investigation of VLM design space: pretrained visual representations, base vs instruct-tuned LM, etc.\\\\n      Different vision encoder ensembles (SigLIP, DINOv2) improve performance.\\\\n      OpenVLA is directly built on the Prismatic architecture.\\\\n    relevance_to_us: >\\\\n      OpenVLA's VLM backbone origin. The SigLIP+DINOv2 fusion design choice\\\\n      is the architectural basis for our analysis of \\\\\\\"frozen vision encoder carries instruction conditioning.\\\\\\\"\\\\n    novelty_gap: >\\\\n      VLM design space exploration, no VLA-specific representation analysis.\\\\n      No trained vs untrained comparison.\\\\n    notes: \\\\\\\"Significant author overlap with OpenVLA team.\\\\\\\"\\\\n\\\\n  - id: vla_survey2025\\\\n    title: \\\\\\\"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges\\\\\\\"\\\\n    authors: \\\\\\\"Multiple authors\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2505.04769\\\\\\\"\\\\n    category: background\\\\n    role: context\\\\n    key_findings: >\\\\n      Comprehensive survey of 100+ VLA architectures, 26 major VLA datasets.\\\\n      Large-scale quantitative analysis linking model design choices to normalized performance.\\\\n      Covers fusion strategy, action representation, encoder selection.\\\\n    relevance_to_us: \\\\\\\"Provides VLA landscape for positioning our work in the representation analysis sub-direction.\\\\\\\"\\\\n    novelty_gap: \\\\\\\"Survey, no original experimental analysis.\\\\\\\"\\\\n    notes: \\\\\\\"Most comprehensive VLA survey as of 2025-05.\\\\\\\"\\\\n\\\\n  # ============================================================\\\\n  # EVALUATION — LIBERO Benchmark Ecosystem\\\\n  # ============================================================\\\\n  - id: liu2023_libero\\\\n    title: \\\\\\\"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\\\\\\\"\\\\n    authors: \\\\\\\"Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"NeurIPS 2023\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2306.03310\\\\\\\"\\\\n    category: evaluation\\\\n    role: baseline\\\\n    key_findings: >\\\\n      130 tasks across 4 suites (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long).\\\\n      Procedural generation + skill blending + human teleoperation demonstrations.\\\\n      Lifelong learning benchmark with knowledge transfer evaluation.\\\\n    relevance_to_us: \\\\\\\"Our primary experimental platform. LIBERO-10 (fine-tuning) + LIBERO-Goal (OOD test).\\\\\\\"\\\\n    novelty_gap: null\\\\n    notes: \\\\\\\"NeurIPS 2023 Datasets and Benchmarks track.\\\\\\\"\\\\n\\\\n  - id: fei2025_libero_plus\\\\n    title: \\\\\\\"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Senyu Fei, Siyin Wang, Junhao Shi, et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2510.13626\\\\\\\"\\\\n    category: evaluation\\\\n    role: context\\\\n    key_findings: >\\\\n      7-dimension controlled perturbations expose VLA fragility.\\\\n      Performance drops from 95% to <30% (camera viewpoint, robot initial state most sensitive).\\\\n      Models are insensitive to language variations — largely ignore language instructions.\\\\n      Positional bias over genuine semantic understanding.\\\\n    relevance_to_us: >\\\\n      \\\\\\\"Models ignore language instructions\\\\\\\" is consistent with our finding that\\\\n      training doesnt improve representation structure — VLAs have not truly learned language grounding.\\\\n    novelty_gap: \\\\\\\"Behavioral robustness analysis, no representation-level analysis.\\\\\\\"\\\\n    notes: \\\\\\\"Submitted 2025-10. OpenMOSS team.\\\\\\\"\\\\n\\\\n  - id: zhou2025_libero_pro\\\\n    title: \\\\\\\"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization\\\\\\\"\\\\n    authors: \\\\\\\"Xueyang Zhou, Yangming Xu, Guiyao Tie, et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2510.03827\\\\\\\"\\\\n    category: evaluation\\\\n    role: context\\\\n    key_findings: >\\\\n      Standard LIBERO >90% accuracy, but generalized setting collapses to 0.0%.\\\\n      Exposes reliance on rote memorization (action sequences + environment layouts)\\\\n      rather than genuine task understanding or environmental perception.\\\\n    relevance_to_us: >\\\\n      \\\\\\\"Memorization not understanding\\\\\\\" supports our story:\\\\n      VLA training improves action sequence memorization, not representation structure.\\\\n    novelty_gap: \\\\\\\"Behavioral evaluation, no representation analysis.\\\\\\\"\\\\n    notes: \\\\\\\"Submitted 2025-10.\\\\\\\"\\\\n\\\\n  - id: libero_para2026\\\\n    title: \\\\\\\"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models\\\\\\\"\\\\n    authors: \\\\\\\"Multiple authors\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2603.28301\\\\\\\"\\\\n    category: evaluation\\\\n    role: context\\\\n    key_findings: >\\\\n      7 VLA configurations (0.6B-7.5B) show 22-52pp performance degradation under paraphrasing.\\\\n      80-96% of failures from planning-level trajectory divergence (not execution errors),\\\\n      indicating paraphrasing disrupts task identification.\\\\n      Synonym substitution alone causes large drops — relies on surface-level matching, not semantic grounding.\\\\n    relevance_to_us: >\\\\n      Further confirms VLAs lack true language grounding.\\\\n      Complements our \\\\\\\"instruction conditioning comes from input pathway structure, not semantic training.\\\\\\\"\\\\n    novelty_gap: \\\\\\\"Paraphrase robustness diagnosis, no representation analysis.\\\\\\\"\\\\n    notes: \\\\\\\"Submitted 2026-03-30.\\\\\\\"\\\\n\\\\n  # ============================================================\\\\n  # RELATED ARCHITECTURE — VLA Models\\\\n  # ============================================================\\\\n  - id: kim2024_openvla\\\\n    title: \\\\\\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\\\\\"\\\\n    authors: \\\\\\\"Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2406.09246\\\\\\\"\\\\n    category: related-architecture\\\\n    role: baseline\\\\n    key_findings: >\\\\n      7B-param VLA trained on 970k real-world robot demonstrations (Open X-Embodiment).\\\\n      Llama 2 7B backbone + DINOv2+SigLIP fused vision encoder.\\\\n      Outperforms RT-2-X (55B) by 16.5% absolute with 7x fewer parameters.\\\\n    relevance_to_us: >\\\\n      Our analysis target. All probing/RSA/CKA experiments use OpenVLA-7B.\\\\n      Architecture details (frozen SigLIP, Llama 2 backbone) directly affect our interpretation\\\\n      of \\\\\\\"input pathway vs training.\\\\\\\"\\\\n    novelty_gap: null\\\\n    notes: \\\\\\\"Stanford/Toyota/Google. Open-source checkpoints + training code.\\\\\\\"\\\\n\\\\n  - id: brohan2023_rt2\\\\n    title: \\\\\\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\\\\\"\\\\n    authors: \\\\\\\"Anthony Brohan et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2307.15818\\\\\\\"\\\\n    category: related-architecture\\\\n    role: context\\\\n    key_findings: >\\\\n      Co-fine-tunes VLM (PaLM-E 55B) on robotic trajectory data + internet-scale VL tasks.\\\\n      Robot actions represented as text tokens.\\\\n      Demonstrates emergent capabilities: novel object generalization, chain-of-thought reasoning.\\\\n    relevance_to_us: >\\\\n      Pioneering VLA architecture. RT-2 uses PaLM-E, OpenVLA uses Llama 2,\\\\n      but shares the \\\\\\\"LLM backbone + frozen vision encoder\\\\\\\" core design.\\\\n      Our findings may generalize to similar architectures.\\\\n    novelty_gap: \\\\\\\"No representation analysis. No trained vs untrained comparison.\\\\\\\"\\\\n    notes: \\\\\\\"Google DeepMind. 55B params, not open-source.\\\\\\\"\\\\n\\\\n  - id: ghosh2024_octo\\\\n    title: \\\\\\\"Octo: An Open-Source Generalist Robot Policy\\\\\\\"\\\\n    authors: \\\\\\\"Octo Model Team, Dibya Ghosh, Homer Walke, Karl Pertsch, et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2405.12213\\\\\\\"\\\\n    category: related-architecture\\\\n    role: context\\\\n    key_findings: >\\\\n      Transformer-based diffusion policy pretrained on 800k robot episodes (Open X-Embodiment).\\\\n      Lightweight CNN vision encoder + language model for text instructions.\\\\n      27M (Small) / 93M (Base) params, consumer GPU fine-tuning.\\\\n    relevance_to_us: >\\\\n      Alternative VLA architecture (not LLM-based). Grant 2026 tests include Octo.\\\\n      If our findings generalize to Octo, the input pathway effect is cross-architectural.\\\\n    novelty_gap: \\\\\\\"No representation analysis. No frozen encoder analysis.\\\\\\\"\\\\n    notes: \\\\\\\"Berkeley. Author overlap with OpenVLA.\\\\\\\"\\\\n\\\\n  - id: black2024_pi0\\\\n    title: \\\\\\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\\\\\"\\\\n    authors: \\\\\\\"Kevin Black et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2410.24164\\\\\\\"\\\\n    category: related-architecture\\\\n    role: context\\\\n    key_findings: >\\\\n      Flow matching action head (not autoregressive tokens), 50Hz continuous trajectories.\\\\n      Pre-trained VLM backbone + flow matching combination.\\\\n      7 robotic platforms, 68 tasks. Real-world dexterous manipulation.\\\\n    relevance_to_us: >\\\\n      pi0 uses continuous flow matching vs discrete tokens — different action representation.\\\\n      Grant 2026 and Haon 2025 both tested Pi0/pi0.5, enabling cross-reference with our OpenVLA results.\\\\n    novelty_gap: \\\\\\\"No representation structure analysis.\\\\\\\"\\\\n    notes: \\\\\\\"Physical Intelligence. Commercial frontier VLA.\\\\\\\"\\\\n\\\\n# ============================================================\\\\n# CATEGORY INDEX\\\\n# ============================================================\\\\ncategories:\\\\n  direct-competitor:\\\\n    description: \\\\\\\"VLA representation / interpretability / language grounding analysis\\\\\\\"\\\\n    papers:\\\\n      - grant2026\\\\n      - swann2026\\\\n      - rizzardo2026\\\\n      - haon2025\\\\n      - molinari2025\\\\n      - lu2025\\\\n      - fang_intention2025\\\\n      - fang_cf2026\\\\n      - hou2026\\\\n\\\\n  method-component:\\\\n    description: \\\\\\\"RSA, CKA, linear probing methodological references\\\\\\\"\\\\n    papers:\\\\n      - kriegeskorte2008\\\\n      - kornblith2019\\\\n      - alain2017\\\\n\\\\n  vision-encoder:\\\\n    description: \\\\\\\"Vision encoder architectures used in our analysis (SigLIP, DINOv2, CLIP)\\\\\\\"\\\\n    papers:\\\\n      - zhai2023_siglip\\\\n      - oquab2024_dinov2\\\\n      - radford2021_clip\\\\n\\\\n  background:\\\\n    description: \\\\\\\"VLM design space, frozen encoder effects, multi-modal fusion\\\\\\\"\\\\n    papers:\\\\n      - karamcheti2024\\\\n      - vla_survey2025\\\\n\\\\n  evaluation:\\\\n    description: \\\\\\\"LIBERO benchmark ecosystem and VLA robustness evaluation\\\\\\\"\\\\n    papers:\\\\n      - liu2023_libero\\\\n      - fei2025_libero_plus\\\\n      - zhou2025_libero_pro\\\\n      - libero_para2026\\\\n\\\\n  related-architecture:\\\\n    description: \\\\\\\"VLA model architectures (OpenVLA, RT-2, Octo, pi0)\\\\\\\"\\\\n    papers:\\\\n      - kim2024_openvla\\\\n      - brohan2023_rt2\\\\n      - ghosh2024_octo\\\\n      - black2024_pi0\\\\n\\\\n# ============================================================\\\\n# SYNTHESIS: OUR NOVELTY POSITION\\\\n# ============================================================\\\\nsynthesis:\\\\n  our_core_claim: \\\\\\\"Instruction Input Pathway Drives Conditioning, Not Training\\\\\\\"\\\\n\\\\n  what_others_have_done:\\\\n    behavioral_level:\\\\n      - \\\\\\\"Grant 2026: vision pathway dominates, language 'encoded but not used' (activation injection)\\\\\\\"\\\\n      - \\\\\\\"LIBERO-CF/LangGap/LIBERO-Plus: VLAs ignore language instructions (counterfactual/robustness tests)\\\\\\\"\\\\n      - \\\\\\\"LIBERO-PRO: models rely on memorization not understanding\\\\\\\"\\\\n      - \\\\\\\"Fang 2025: fine-tuning erodes VLM reasoning (intention != execution)\\\\\\\"\\\\n    representation_level:\\\\n      - \\\\\\\"Swann 2026: SAE features mostly memorized sequences, some interpretable (OpenVLA)\\\\\\\"\\\\n      - \\\\\\\"Molinari 2025: world model emerges in middle layers (OpenVLA)\\\\\\\"\\\\n      - \\\\\\\"Lu 2025: symbolic states decodable with >0.90 accuracy (OpenVLA + LIBERO)\\\\\\\"\\\\n      - \\\\\\\"Haon 2025: sparse semantic directions causally linked to actions (Pi0 + OpenVLA)\\\\\\\"\\\\n      - \\\\\\\"Rizzardo 2026: feature-observability and controllability (pi0.5 + OpenVLA)\\\\\\\"\\\\n\\\\n  what_nobody_has_done:\\\\n    - \\\\\\\"Trained vs untrained VLA representation comparison (we find trained ~= untrained >> DINO)\\\\\\\"\\\\n    - \\\\\\\"Instruction input pathway vs LLM training separation analysis (6 probing rounds + RSA all consistent)\\\\\\\"\\\\n    - \\\\\\\"Systematic layer-wise RSA/CKA comparison of trained/untrained/DINO representation structures\\\\\\\"\\\\n    - \\\\\\\"Instruction ablation causal verification: removing instruction drops RSA to DINO level\\\\\\\"\\\\n\\\\n  key_differentiation_from_grant2026: >\\\\n    Grant 2026 compares different VLA models (architectural differences);\\\\n    we compare trained vs untrained within the same model (training effect isolation).\\\\n    Grant finds \\\\\\\"language encoded but not used\\\\\\\" (behavioral level);\\\\n    we find \\\\\\\"conditioning comes from input pathway, not training\\\\\\\" (representation level).\\\\n    Complementary, not competing. Related Work must qualify OFT vs standard fine-tuning difference.\\\\n\\\", \\\"total_chars\\\": 29243, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/literature_map.yaml\", \"content\": \"papers:\\n  # ============================================================\\n  # DIRECT COMPETITORS — VLA Representation Analysis / Interpretability\\n  # ============================================================\\n  - id: grant2026\\n    title: \\\"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models\\\"\\n    authors: \\\"Bryce Grant, Xijia Zhao, Peng Wang\\\"\\n    year: 2026\\n    venue: \\\"arXiv preprint (under review)\\\"\\n    arxiv_id: \\\"2603.19233\\\"\\n    category: direct-competitor\\n    role: competitor\\n    key_findings: >\\n      Visual pathway dominates action generation across all 6 tested VLA architectures (80M–7B params, 394K+ rollout episodes, 4 benchmarks).\\n      Language sensitivity depends on task structure: when visual context uniquely specifies the task, language is IGNORED;\\n      when multiple goals share a scene, language becomes essential (\\\"encoded but not used\\\").\\n      Cross-task activation injection steers robots toward source-task positions (99.8% trajectory alignment with source in X-VLA).\\n      Multi-pathway architectures (pi0.5, SmolVLA, GR00T) separate motor programs (expert pathway) from goal semantics (VLM pathway).\\n    relevance_to_us: >\\n      Most direct competitor. Behavioral intervention (activation injection, SAE, probing) reveals vision dominance + language encoded but not used.\\n      Uses OpenVLA-OFT checkpoint; we use standard fine-tuning — must qualify this difference in Related Work.\\n    novelty_gap: >\\n      No trained vs untrained representation analysis. They compare different model architectures,\\n      we compare trained vs untrained representation structure within the same architecture.\\n      Their \\\"encoded but not used\\\" is a behavioral-level conclusion; we demonstrate at the representation level\\n      that instruction conditioning comes from the input pathway, not training. Complementary work.\\n    notes: >\\n      Action Atlas interactive exploration tool released. 6 models: OpenVLA, X-VLA, pi0.5, SmolVLA, GR00T, Octo.\\n      OFT checkpoint difference may affect direct comparability.\\n\\n  - id: swann2026\\n    title: \\\"Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models\\\"\\n    authors: \\\"Aiden Swann, Lachlain McGranahan, Hugo Buurmeijer, Monroe Kennedy III, Mac Schwager\\\"\\n    year: 2026\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2603.19183\\\"\\n    category: direct-competitor\\n    role: competitor\\n    key_findings: >\\n      SAE features on OpenVLA: majority of extracted features correspond to memorized training sequences,\\n      but some correspond to interpretable, general, and steerable motion primitives and semantic properties.\\n    relevance_to_us: >\\n      Also OpenVLA interpretability work. They use SAE for feature-level decomposition,\\n      we use probing + RSA for representation-level analysis. Methodologically complementary.\\n    novelty_gap: >\\n      No language features analysis. No trained vs untrained comparison.\\n      Does not investigate source of instruction conditioning (input pathway vs training).\\n    notes: \\\"Stanford team. Published on arXiv same day as Grant 2026 (2026-03-19).\\\"\\n\\n  - id: rizzardo2026\\n    title: \\\"Observing and Controlling Features in Vision-Language-Action Models\\\"\\n    authors: \\\"Rizzardo et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2603.05487\\\"\\n    category: direct-competitor\\n    role: competitor\\n    key_findings: >\\n      Introduces feature-observability and feature-controllability concepts bridging LLM mechanistic\\n      interpretability and VLAs. Linear classifier observation + optimal-control-based minimal intervention steering.\\n      Validated on pi0.5 and OpenVLA — targeted interventions steer robot behavior while preserving closed-loop capabilities.\\n    relevance_to_us: >\\n      Also VLA internal representation analysis. They focus on how to steer,\\n      we focus on where conditioning comes from (input pathway vs training).\\n    novelty_gap: >\\n      No trained vs untrained comparison. No instruction pathway vs training separation analysis.\\n      Focuses on controllability rather than representation structure origin.\\n    notes: \\\"Submitted 2026-03-05.\\\"\\n\\n  - id: haon2025\\n    title: \\\"Mechanistic Interpretability for Steering Vision-Language-Action Models\\\"\\n    authors: \\\"Bear Haon, Kaylene Stocking, Ian Chuang, Claire Tomlin\\\"\\n    year: 2025\\n    venue: \\\"CoRL 2025\\\"\\n    arxiv_id: \\\"2509.00328\\\"\\n    category: direct-competitor\\n    role: methodology\\n    key_findings: >\\n      First VLA mechanistic interpretability framework. Projects feedforward activations onto token embedding basis,\\n      identifies sparse semantic directions (speed, direction) causally linked to action selection.\\n      Activation steering modulates behavior in real time without fine-tuning.\\n      Validated on Pi0 and OpenVLA in LIBERO (simulation) and UR5 (real robot).\\n    relevance_to_us: >\\n      Methodological reference: their activation steering proves VLAs have interpretable semantic directions.\\n      Our RSA/probing results can dialogue with their mechanistic findings.\\n    novelty_gap: >\\n      No trained vs untrained comparison. No systematic representation structure analysis (RSA/CKA).\\n      Focuses on individual semantic direction causal intervention, not overall structure comparison.\\n    notes: \\\"CoRL 2025 accepted. Pioneering work in VLA interpretability.\\\"\\n\\n  - id: molinari2025\\n    title: \\\"Emergent World Representations in OpenVLA\\\"\\n    authors: \\\"Marco Molinari, Leonardo Nevali, Saharsha Navani, Omar G. Younis\\\"\\n    year: 2025\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2509.24559\\\"\\n    category: direct-competitor\\n    role: context\\n    key_findings: >\\n      OpenVLA implicitly learns a world model. Embedding arithmetic tests state transition knowledge;\\n      linear/non-linear probes show statistically significant state transition prediction ability across layers.\\n      SAE pipeline analyzes fine-grained world model structure.\\n    relevance_to_us: >\\n      Also OpenVLA probing work. They study world model, we study instruction conditioning.\\n      Their layer-wise probe results can be compared with our layer-wise RSA.\\n    novelty_gap: >\\n      No language/instruction analysis. No trained vs untrained comparison.\\n      Only focuses on state transitions, not goal/instruction representation.\\n    notes: \\\"Submitted 2025-09-29. Has OpenReview discussion.\\\"\\n\\n  - id: lu2025\\n    title: \\\"Probing a Vision-Language-Action Model for Symbolic States and Integration into a Cognitive Architecture\\\"\\n    authors: \\\"Hong Lu, Hengxu Li, Prithviraj Singh Shahani, Stephanie Herbers, Matthias Scheutz\\\"\\n    year: 2025\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2502.04558\\\"\\n    category: direct-competitor\\n    role: methodology\\n    key_findings: >\\n      Probes OpenVLA hidden layers to extract symbolic representations (object properties, relations, action states).\\n      LIBERO-spatial pick-and-place probing accuracy > 0.90 across most layers.\\n      Integration with cognitive architecture improves interpretability and robustness.\\n    relevance_to_us: >\\n      Directly related methodology: both use linear probes on OpenVLA layers on LIBERO.\\n      Their finding that symbolic states are decodable (>0.90) is consistent with our goal classification at 100%.\\n    novelty_gap: >\\n      Only trained model probing, no untrained control.\\n      Only LIBERO-spatial single task, no cross-task/cross-condition analysis.\\n      No instruction conditioning source analysis.\\n    notes: \\\"Submitted 2025-02-06. Tufts University.\\\"\\n\\n  - id: fang_intention2025\\n    title: \\\"From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models\\\"\\n    authors: \\\"Irving Fang, Juexiao Zhang, Shengbang Tong, Chen Feng\\\"\\n    year: 2025\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2506.09930\\\"\\n    category: direct-competitor\\n    role: context\\n    key_findings: >\\n      Unified probing suite (50 simulation tasks, 10 subcategories) evaluating VLA generalization boundaries.\\n      VLM backbone provides robust perceptual understanding + high-level planning (good intentions),\\n      but cannot reliably translate to precise motor execution (perception-to-action gap).\\n      Action data fine-tuning erodes original VLM generalist reasoning abilities.\\n    relevance_to_us: >\\n      \\\"Fine-tuning erodes VLM reasoning\\\" echoes our \\\"training doesn't improve representation\\\" finding.\\n      They discover intention != execution at behavioral level; we discover\\n      training ~= untrained in representation structure.\\n    novelty_gap: >\\n      Behavioral-level probing (success rates), not representation-level analysis.\\n      No trained vs untrained representation structure comparison.\\n    notes: \\\"Submitted 2025-06-11. INT-ACT benchmark open-sourced. NYU/ai4ce team.\\\"\\n\\n  # ============================================================\\n  # DIRECT COMPETITORS — Language Grounding / Counterfactual\\n  # ============================================================\\n  - id: fang_cf2026\\n    title: \\\"When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs\\\"\\n    authors: \\\"Yu Fang, Yuchun Feng, Dong Jing, Jiaqi Liu, Yue Yang, Zhenyu Wei, Daniel Szafir, Mingyu Ding\\\"\\n    year: 2026\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2602.17659\\\"\\n    category: direct-competitor\\n    role: competitor\\n    key_findings: >\\n      Introduces LIBERO-CF counterfactual benchmark. VLAs exhibit severe counterfactual failures:\\n      vision shortcuts + dataset biases cause models to ignore language intent.\\n      OpenVLA-OFT: 4.7% grounding rate, 0.4% success rate.\\n      Best model: 30.8% grounding rate, 13.2% success rate.\\n      Proposes Counterfactual Action Guidance (CAG) dual-branch inference scheme.\\n    relevance_to_us: >\\n      Directly validates \\\"language encoded but not used\\\" severity under counterfactual settings.\\n      Their behavioral findings complement our representation-level findings.\\n      They test OpenVLA-OFT — same checkpoint issue as Grant 2026.\\n    novelty_gap: >\\n      Pure behavioral benchmark, no representation analysis.\\n      No trained vs untrained comparison. No instruction pathway causal analysis.\\n    notes: \\\"Submitted 2026-02-19. LIBERO-CF has 4 sub-suites (CF-Spatial, CF-Object, CF-Long, CF-OOD).\\\"\\n\\n  - id: hou2026\\n    title: \\\"LangGap: Diagnosing and Closing the Language Gap in Vision-Language-Action Models\\\"\\n    authors: \\\"Yuchen Hou, Lin Zhao\\\"\\n    year: 2026\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2603.00592\\\"\\n    category: direct-competitor\\n    role: context\\n    key_findings: >\\n      SOTA VLAs achieve >95% on standard benchmarks but largely ignore language instructions.\\n      Four-dimensional semantic perturbation method exposes language understanding deficits.\\n      LIBERO assigns only 1 task per layout, so models dont need to understand language.\\n      LangGap benchmark forces multi-task shared layouts; data augmentation improves from 0% to 90%.\\n    relevance_to_us: >\\n      Systematic diagnosis of \\\"VLAs ignore language\\\" supports our story:\\n      instruction conditioning comes from input pathway, not training — even trained VLAs dont truly leverage language.\\n    novelty_gap: >\\n      Behavioral-level diagnosis + data augmentation solution. No representation analysis.\\n      No trained vs untrained comparison. No input pathway causal analysis.\\n    notes: \\\"Submitted 2026-02-28. GitHub open-sourced.\\\"\\n\\n  # ============================================================\\n  # METHOD COMPONENT — RSA, CKA, Linear Probing\\n  # ============================================================\\n  - id: kriegeskorte2008\\n    title: \\\"Representational Similarity Analysis - Connecting the Branches of Systems Neuroscience\\\"\\n    authors: \\\"Nikolaus Kriegeskorte, Marieke Mur, Peter Bandettini\\\"\\n    year: 2008\\n    venue: \\\"Frontiers in Systems Neuroscience\\\"\\n    arxiv_id: null\\n    doi: \\\"10.3389/neuro.06.004.2008\\\"\\n    category: method-component\\n    role: methodology\\n    key_findings: >\\n      Introduces Representational Dissimilarity Matrix (RDM) framework for comparing multi-channel\\n      neural activity measurements with computational models and behavior.\\n      Validated on fMRI visual cortex data.\\n    relevance_to_us: \\\"RSA is one of our core analysis methods for comparing trained/untrained/DINO representation structures.\\\"\\n    novelty_gap: null\\n    notes: \\\"Original RSA paper. 5000+ citations.\\\"\\n\\n  - id: kornblith2019\\n    title: \\\"Similarity of Neural Network Representations Revisited\\\"\\n    authors: \\\"Simon Kornblith, Mohammad Norouzi, Honglak Lee, Geoffrey Hinton\\\"\\n    year: 2019\\n    venue: \\\"ICML 2019\\\"\\n    arxiv_id: \\\"1905.00414\\\"\\n    category: method-component\\n    role: methodology\\n    key_findings: >\\n      Introduces Centered Kernel Alignment (CKA) as representation similarity metric.\\n      CKA reliably identifies representation correspondences across differently initialized networks,\\n      outperforming CCA-based methods.\\n    relevance_to_us: >\\n      CKA is one of our core tools for comparing trained vs untrained representations.\\n      Deep-layer CKA reaching 0.86 demonstrates high representation similarity.\\n    novelty_gap: null\\n    notes: \\\"Google Brain. CKA is now standard for representation comparison.\\\"\\n\\n  - id: alain2017\\n    title: \\\"Understanding Intermediate Layers Using Linear Classifier Probes\\\"\\n    authors: \\\"Guillaume Alain, Yoshua Bengio\\\"\\n    year: 2017\\n    venue: \\\"ICLR 2017 Workshop\\\"\\n    arxiv_id: \\\"1610.01644\\\"\\n    category: method-component\\n    role: methodology\\n    key_findings: >\\n      Proposes linear classifier probes to monitor feature suitability for classification at every layer.\\n      Linear separability increases monotonically along network depth.\\n      Validated on Inception v3 and ResNet-50.\\n    relevance_to_us: \\\"Linear probing is the methodological foundation for our goal classification and action prediction experiments.\\\"\\n    novelty_gap: null\\n    notes: \\\"Foundational probing methodology work.\\\"\\n\\n  # ============================================================\\n  # VISION ENCODERS — SigLIP, DINOv2, CLIP\\n  # ============================================================\\n  - id: zhai2023_siglip\\n    title: \\\"Sigmoid Loss for Language Image Pre-Training\\\"\\n    authors: \\\"Xiaohua Zhai, Basil Mustafa, Alexander Kolesnikov, Lucas Beyer\\\"\\n    year: 2023\\n    venue: \\\"ICCV 2023\\\"\\n    arxiv_id: \\\"2303.15343\\\"\\n    category: vision-encoder\\n    role: baseline\\n    verified: true\\n    key_findings: >\\n      Replaces softmax contrastive loss with pairwise sigmoid loss for VL pretraining.\\n      Eliminates global batch normalization, enabling smaller batch training.\\n      SigLIP-SO400M achieves competitive zero-shot performance with simpler training.\\n    relevance_to_us: >\\n      SigLIP-SO400M is OpenVLA's frozen vision encoder. Our RSA=0.615 for SigLIP+Projector\\n      shows this encoder provides dominant action-relevant geometric structure.\\n    novelty_gap: null\\n    notes: \\\"Google. OpenVLA uses SigLIP-SO400M/14 variant.\\\"\\n\\n  - id: oquab2024_dinov2\\n    title: \\\"DINOv2: Learning Robust Visual Features without Supervision\\\"\\n    authors: \\\"Maxime Oquab, Timothée Darcet, Théo Moutakanni, et al.\\\"\\n    year: 2024\\n    venue: \\\"TMLR 2024\\\"\\n    arxiv_id: \\\"2304.07193\\\"\\n    category: vision-encoder\\n    role: baseline\\n    verified: true\\n    key_findings: >\\n      Self-supervised ViT trained on curated 142M image dataset (LVD-142M).\\n      Produces general-purpose features competitive with task-specific models.\\n      No language supervision — purely vision self-supervised.\\n    relevance_to_us: >\\n      Vision-only baseline in our analysis. DINO RSA=0.388 << SigLIP 0.615,\\n      but DINO R²=0.712 ≈ Projector R²=0.706 — key geometric-functional dissociation.\\n    novelty_gap: null\\n    notes: \\\"Meta AI. DINOv2 ViT-L/14 used as vision-only control.\\\"\\n\\n  - id: radford2021_clip\\n    title: \\\"Learning Transferable Visual Models From Natural Language Supervision\\\"\\n    authors: \\\"Alec Radford, Jong Wook Kim, Chris Hallacy, et al.\\\"\\n    year: 2021\\n    venue: \\\"ICML 2021\\\"\\n    arxiv_id: \\\"2103.00020\\\"\\n    category: vision-encoder\\n    role: baseline\\n    verified: true\\n    key_findings: >\\n      Contrastive language-image pretraining on 400M image-text pairs.\\n      Zero-shot transfer competitive with supervised baselines.\\n      Pioneering VL pretraining approach.\\n    relevance_to_us: >\\n      CLIP ViT-L/14 RSA=0.557 confirms VL pretraining universality:\\n      both CLIP (0.557) and SigLIP+Proj (0.615) >> DINO (0.388).\\n      Action-relevant geometric structure is a universal product of VL pretraining.\\n    novelty_gap: null\\n    notes: \\\"OpenAI. CLIP ViT-L/14 used as VL pretraining generalization control (plan_012).\\\"\\n\\n  # ============================================================\\n  # BACKGROUND — VLM Design, Frozen Encoders, Multi-modal Fusion\\n  # ============================================================\\n  - id: karamcheti2024\\n    title: \\\"Prismatic VLMs: Investigating the Design Space of Visually-Conditioned Language Models\\\"\\n    authors: \\\"Siddharth Karamcheti, Suraj Nair, Ashwin Balakrishna, Percy Liang, Thomas Kollar, Dorsa Sadigh\\\"\\n    year: 2024\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2402.07865\\\"\\n    category: background\\n    role: baseline\\n    key_findings: >\\n      Systematic investigation of VLM design space: pretrained visual representations, base vs instruct-tuned LM, etc.\\n      Different vision encoder ensembles (SigLIP, DINOv2) improve performance.\\n      OpenVLA is directly built on the Prismatic architecture.\\n    relevance_to_us: >\\n      OpenVLA's VLM backbone origin. The SigLIP+DINOv2 fusion design choice\\n      is the architectural basis for our analysis of \\\"frozen vision encoder carries instruction conditioning.\\\"\\n    novelty_gap: >\\n      VLM design space exploration, no VLA-specific representation analysis.\\n      No trained vs untrained comparison.\\n    notes: \\\"Significant author overlap with OpenVLA team.\\\"\\n\\n  - id: vla_survey2025\\n    title: \\\"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges\\\"\\n    authors: \\\"Multiple authors\\\"\\n    year: 2025\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2505.04769\\\"\\n    category: background\\n    role: context\\n    key_findings: >\\n      Comprehensive survey of 100+ VLA architectures, 26 major VLA datasets.\\n      Large-scale quantitative analysis linking model design choices to normalized performance.\\n      Covers fusion strategy, action representation, encoder selection.\\n    relevance_to_us: \\\"Provides VLA landscape for positioning our work in the representation analysis sub-direction.\\\"\\n    novelty_gap: \\\"Survey, no original experimental analysis.\\\"\\n    notes: \\\"Most comprehensive VLA survey as of 2025-05.\\\"\\n\\n  # ============================================================\\n  # EVALUATION — LIBERO Benchmark Ecosystem\\n  # ============================================================\\n  - id: liu2023_libero\\n    title: \\\"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\\\"\\n    authors: \\\"Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023\\\"\\n    arxiv_id: \\\"2306.03310\\\"\\n    category: evaluation\\n    role: baseline\\n    key_findings: >\\n      130 tasks across 4 suites (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long).\\n      Procedural generation + skill blending + human teleoperation demonstrations.\\n      Lifelong learning benchmark with knowledge transfer evaluation.\\n    relevance_to_us: \\\"Our primary experimental platform. LIBERO-10 (fine-tuning) + LIBERO-Goal (OOD test).\\\"\\n    novelty_gap: null\\n    notes: \\\"NeurIPS 2023 Datasets and Benchmarks track.\\\"\\n\\n  - id: fei2025_libero_plus\\n    title: \\\"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\\\"\\n    authors: \\\"Senyu Fei, Siyin Wang, Junhao Shi, et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2510.13626\\\"\\n    category: evaluation\\n    role: context\\n    key_findings: >\\n      7-dimension controlled perturbations expose VLA fragility.\\n      Performance drops from 95% to <30% (camera viewpoint, robot initial state most sensitive).\\n      Models are insensitive to language variations — largely ignore language instructions.\\n      Positional bias over genuine semantic understanding.\\n    relevance_to_us: >\\n      \\\"Models ignore language instructions\\\" is consistent with our finding that\\n      training doesnt improve representation structure — VLAs have not truly learned language grounding.\\n    novelty_gap: \\\"Behavioral robustness analysis, no representation-level analysis.\\\"\\n    notes: \\\"Submitted 2025-10. OpenMOSS team.\\\"\\n\\n  - id: zhou2025_libero_pro\\n    title: \\\"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization\\\"\\n    authors: \\\"Xueyang Zhou, Yangming Xu, Guiyao Tie, et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2510.03827\\\"\\n    category: evaluation\\n    role: context\\n    key_findings: >\\n      Standard LIBERO >90% accuracy, but generalized setting collapses to 0.0%.\\n      Exposes reliance on rote memorization (action sequences + environment layouts)\\n      rather than genuine task understanding or environmental perception.\\n    relevance_to_us: >\\n      \\\"Memorization not understanding\\\" supports our story:\\n      VLA training improves action sequence memorization, not representation structure.\\n    novelty_gap: \\\"Behavioral evaluation, no representation analysis.\\\"\\n    notes: \\\"Submitted 2025-10.\\\"\\n\\n  - id: libero_para2026\\n    title: \\\"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models\\\"\\n    authors: \\\"Multiple authors\\\"\\n    year: 2026\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2603.28301\\\"\\n    category: evaluation\\n    role: context\\n    key_findings: >\\n      7 VLA configurations (0.6B-7.5B) show 22-52pp performance degradation under paraphrasing.\\n      80-96% of failures from planning-level trajectory divergence (not execution errors),\\n      indicating paraphrasing disrupts task identification.\\n      Synonym substitution alone causes large drops — relies on surface-level matching, not semantic grounding.\\n    relevance_to_us: >\\n      Further confirms VLAs lack true language grounding.\\n      Complements our \\\"instruction conditioning comes from input pathway structure, not semantic training.\\\"\\n    novelty_gap: \\\"Paraphrase robustness diagnosis, no representation analysis.\\\"\\n    notes: \\\"Submitted 2026-03-30.\\\"\\n\\n  # ============================================================\\n  # RELATED ARCHITECTURE — VLA Models\\n  # ============================================================\\n  - id: kim2024_openvla\\n    title: \\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\"\\n    authors: \\\"Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2406.09246\\\"\\n    category: related-architecture\\n    role: baseline\\n    key_findings: >\\n      7B-param VLA trained on 970k real-world robot demonstrations (Open X-Embodiment).\\n      Llama 2 7B backbone + DINOv2+SigLIP fused vision encoder.\\n      Outperforms RT-2-X (55B) by 16.5% absolute with 7x fewer parameters.\\n    relevance_to_us: >\\n      Our analysis target. All probing/RSA/CKA experiments use OpenVLA-7B.\\n      Architecture details (frozen SigLIP, Llama 2 backbone) directly affect our interpretation\\n      of \\\"input pathway vs training.\\\"\\n    novelty_gap: null\\n    notes: \\\"Stanford/Toyota/Google. Open-source checkpoints + training code.\\\"\\n\\n  - id: brohan2023_rt2\\n    title: \\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\"\\n    authors: \\\"Anthony Brohan et al.\\\"\\n    year: 2023\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2307.15818\\\"\\n    category: related-architecture\\n    role: context\\n    key_findings: >\\n      Co-fine-tunes VLM (PaLM-E 55B) on robotic trajectory data + internet-scale VL tasks.\\n      Robot actions represented as text tokens.\\n      Demonstrates emergent capabilities: novel object generalization, chain-of-thought reasoning.\\n    relevance_to_us: >\\n      Pioneering VLA architecture. RT-2 uses PaLM-E, OpenVLA uses Llama 2,\\n      but shares the \\\"LLM backbone + frozen vision encoder\\\" core design.\\n      Our findings may generalize to similar architectures.\\n    novelty_gap: \\\"No representation analysis. No trained vs untrained comparison.\\\"\\n    notes: \\\"Google DeepMind. 55B params, not open-source.\\\"\\n\\n  - id: ghosh2024_octo\\n    title: \\\"Octo: An Open-Source Generalist Robot Policy\\\"\\n    authors: \\\"Octo Model Team, Dibya Ghosh, Homer Walke, Karl Pertsch, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2405.12213\\\"\\n    category: related-architecture\\n    role: context\\n    key_findings: >\\n      Transformer-based diffusion policy pretrained on 800k robot episodes (Open X-Embodiment).\\n      Lightweight CNN vision encoder + language model for text instructions.\\n      27M (Small) / 93M (Base) params, consumer GPU fine-tuning.\\n    relevance_to_us: >\\n      Alternative VLA architecture (not LLM-based). Grant 2026 tests include Octo.\\n      If our findings generalize to Octo, the input pathway effect is cross-architectural.\\n    novelty_gap: \\\"No representation analysis. No frozen encoder analysis.\\\"\\n    notes: \\\"Berkeley. Author overlap with OpenVLA.\\\"\\n\\n  - id: black2024_pi0\\n    title: \\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\"\\n    authors: \\\"Kevin Black et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv preprint\\\"\\n    arxiv_id: \\\"2410.24164\\\"\\n    category: related-architecture\\n    role: context\\n    key_findings: >\\n      Flow matching action head (not autoregressive tokens), 50Hz continuous trajectories.\\n      Pre-trained VLM backbone + flow matching combination.\\n      7 robotic platforms, 68 tasks. Real-world dexterous manipulation.\\n    relevance_to_us: >\\n      pi0 uses continuous flow matching vs discrete tokens — different action representation.\\n      Grant 2026 and Haon 2025 both tested Pi0/pi0.5, enabling cross-reference with our OpenVLA results.\\n    novelty_gap: \\\"No representation structure analysis.\\\"\\n    notes: \\\"Physical Intelligence. Commercial frontier VLA.\\\"\\n\\n# ============================================================\\n# CATEGORY INDEX\\n# ============================================================\\ncategories:\\n  direct-competitor:\\n    description: \\\"VLA representation / interpretability / language grounding analysis\\\"\\n    papers:\\n      - grant2026\\n      - swann2026\\n      - rizzardo2026\\n      - haon2025\\n      - molinari2025\\n      - lu2025\\n      - fang_intention2025\\n      - fang_cf2026\\n      - hou2026\\n\\n  method-component:\\n    description: \\\"RSA, CKA, linear probing methodological references\\\"\\n    papers:\\n      - kriegeskorte2008\\n      - kornblith2019\\n      - alain2017\\n\\n  vision-encoder:\\n    description: \\\"Vision encoder architectures used in our analysis (SigLIP, DINOv2, CLIP)\\\"\\n    papers:\\n      - zhai2023_siglip\\n      - oquab2024_dinov2\\n      - radford2021_clip\\n\\n  background:\\n    description: \\\"VLM design space, frozen encoder effects, multi-modal fusion\\\"\\n    papers:\\n      - karamcheti2024\\n      - vla_survey2025\\n\\n  evaluation:\\n    description: \\\"LIBERO benchmark ecosystem and VLA robustness evaluation\\\"\\n    papers:\\n      - liu2023_libero\\n      - fei2025_libero_plus\\n      - zhou2025_libero_pro\\n      - libero_para2026\\n\\n  related-architecture:\\n    description: \\\"VLA model architectures (OpenVLA, RT-2, Octo, pi0)\\\"\\n    papers:\\n      - kim2024_openvla\\n      - brohan2023_rt2\\n      - ghosh2024_octo\\n      - black2024_pi0\\n\\n# ============================================================\\n# SYNTHESIS: OUR NOVELTY POSITION\\n# ============================================================\\nsynthesis:\\n  our_core_claim: \\\"Instruction Input Pathway Drives Conditioning, Not Training\\\"\\n\\n  what_others_have_done:\\n    behavioral_level:\\n      - \\\"Grant 2026: vision pathway dominates, language 'encoded but not used' (activation injection)\\\"\\n      - \\\"LIBERO-CF/LangGap/LIBERO-Plus: VLAs ignore language instructions (counterfactual/robustness tests)\\\"\\n      - \\\"LIBERO-PRO: models rely on memorization not understanding\\\"\\n      - \\\"Fang 2025: fine-tuning erodes VLM reasoning (intention != execution)\\\"\\n    representation_level:\\n      - \\\"Swann 2026: SAE features mostly memorized sequences, some interpretable (OpenVLA)\\\"\\n      - \\\"Molinari 2025: world model emerges in middle layers (OpenVLA)\\\"\\n      - \\\"Lu 2025: symbolic states decodable with >0.90 accuracy (OpenVLA + LIBERO)\\\"\\n      - \\\"Haon 2025: sparse semantic directions causally linked to actions (Pi0 + OpenVLA)\\\"\\n      - \\\"Rizzardo 2026: feature-observability and controllability (pi0.5 + OpenVLA)\\\"\\n\\n  what_nobody_has_done:\\n    - \\\"Trained vs untrained VLA representation comparison (we find trained ~= untrained >> DINO)\\\"\\n    - \\\"Instruction input pathway vs LLM training separation analysis (6 probing rounds + RSA all consistent)\\\"\\n    - \\\"Systematic layer-wise RSA/CKA comparison of trained/untrained/DINO representation structures\\\"\\n    - \\\"Instruction ablation causal verification: removing instruction drops RSA to DINO level\\\"\\n\\n  key_differentiation_from_grant2026: >\\n    Grant 2026 compares different VLA models (architectural differences);\\n    we compare trained vs untrained within the same model (training effect isolation).\\n    Grant finds \\\"language encoded but not used\\\" (behavioral level);\\n    we find \\\"conditioning comes from input pathway, not training\\\" (representation level).\\n    Complementary, not competing. Related Work must qualify OFT vs standard fine-tuning difference.\\n\", \"total_chars\": 29243, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AVSpgnjgNnKUUWSLeWFNMZ`</summary>

```json
{
  "query": "attention head consistency across tasks universal attention patterns fine-tuning transformer 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "69825333-4d5b-41f0-b5d1-79c4ea8043d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01McKeCc2fkZymQASyz2s8v8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 23387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1909
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

_source line 12_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BzJMWsDZSvumkFpvb4Q9ED`</summary>

```json
{
  "query": "task-independent attention specialization VLA vision-language-action model attention routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "f8b76cc7-9d1a-43cf-ac70-9e16b24324d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01McKeCc2fkZymQASyz2s8v8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 23387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1909
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

_source line 13_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y3U6jz7dqUpC1ZQFpaBd5X`</summary>

```json
{
  "query": "specific attention head indices consistent across tasks transformer interpretability \"head identity\" preservation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "00ece03f-36a3-4740-984a-829e2f2a910f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01McKeCc2fkZymQASyz2s8v8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 23387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1909
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

_source line 14 · 2026-05-21T20:41:16.307Z_

<details><summary>↩ Tool result · `toolu_01AVSpgnjgNnKUUWSLeWFNMZ`</summary>

```text
Web search results for query: "attention head consistency across tasks universal attention patterns fine-tuning transformer 2025 2026"

Links: [{"title":"[2510.21518] Head Pursuit: Probing Attention Specialization in Multimodal Transformers","url":"https://arxiv.org/abs/2510.21518"},{"title":"Published as a conference paper at ICLR 2026 WHY ATTENTION PATTERNS EXIST:","url":"https://arxiv.org/pdf/2601.21709"},{"title":"Quantifying LLM Attention-Head Stability: Implications for Circuit Universality","url":"https://arxiv.org/pdf/2602.16740"},{"title":"2026-01-13 Interpreting Transformers Through Attention Head Intervention","url":"https://www.arxiv.org/pdf/2601.04398v3"},{"title":"2026-01-12 Interpreting Transformers Through Attention Head Intervention","url":"https://www.arxiv.org/pdf/2601.04398v2"},{"title":"2026-01-09 Interpreting Transformers Through Attention Head Intervention","url":"https://www.arxiv.org/pdf/2601.04398"}]

Based on the web search results, here are the key findings related to attention head consistency across tasks and universal attention patterns in transformers:

## Attention Head Specialization and Consistency

Research shows consistent patterns of specialization at the head level across both unimodal and multimodal transformers. Editing as few as 1% of the heads, selected using specialized methods, can reliably suppress or enhance targeted concepts in model output.

## Universal Patterns Framework

Computing attention from queries, keys, and RoPE is a common design in transformer-based models, and TAPPA (a recently developed framework) both unifies diverse attention patterns and is broadly applicable across LLMs. Attention patterns are closely linked to a model's representational capacity and can guide compression.

## The Universality Hypothesis

A key research question in 2025-2026 involves the "universality hypothesis," which asserts that models learn the same or similar representational features and circuits across different models when trained on similar tasks. However, the strength of the similarities between these learned model components has yet to be systematically quantified, leaving the critical distinction between strong and weak universality unresolved.

## Mechanistic Interpretability Through Attention Head Intervention

Recent work in 2026 has focused on understanding how attention head intervention can reveal causal relationships in transformer behavior and potentially control model outputs across different tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "b6f5a052-8eee-4de8-865b-36b1a3e7e4f7",
  "tool_use_result": {
    "query": "attention head consistency across tasks universal attention patterns fine-tuning transformer 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HgQ7dWBz6a8xD7xkECk62K",
        "content": [
          {
            "title": "[2510.21518] Head Pursuit: Probing Attention Specialization in Multimodal Transformers",
            "url": "https://arxiv.org/abs/2510.21518"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 WHY ATTENTION PATTERNS EXIST:",
            "url": "https://arxiv.org/pdf/2601.21709"
          },
          {
            "title": "Quantifying LLM Attention-Head Stability: Implications for Circuit Universality",
            "url": "https://arxiv.org/pdf/2602.16740"
          },
          {
            "title": "2026-01-13 Interpreting Transformers Through Attention Head Intervention",
            "url": "https://www.arxiv.org/pdf/2601.04398v3"
          },
          {
            "title": "2026-01-12 Interpreting Transformers Through Attention Head Intervention",
            "url": "https://www.arxiv.org/pdf/2601.04398v2"
          },
          {
            "title": "2026-01-09 Interpreting Transformers Through Attention Head Intervention",
            "url": "https://www.arxiv.org/pdf/2601.04398"
          }
        ]
      },
      "Based on the web search results, here are the key findings related to attention head consistency across tasks and universal attention patterns in transformers:\n\n## Attention Head Specialization and Consistency\n\nResearch shows consistent patterns of specialization at the head level across both unimodal and multimodal transformers. Editing as few as 1% of the heads, selected using specialized methods, can reliably suppress or enhance targeted concepts in model output.\n\n## Universal Patterns Framework\n\nComputing attention from queries, keys, and RoPE is a common design in transformer-based models, and TAPPA (a recently developed framework) both unifies diverse attention patterns and is broadly applicable across LLMs. Attention patterns are closely linked to a model's representational capacity and can guide compression.\n\n## The Universality Hypothesis\n\nA key research question in 2025-2026 involves the \"universality hypothesis,\" which asserts that models learn the same or similar representational features and circuits across different models when trained on similar tasks. However, the strength of the similarities between these learned model components has yet to be systematically quantified, leaving the critical distinction between strong and weak universality unresolved.\n\n## Mechanistic Interpretability Through Attention Head Intervention\n\nRecent work in 2026 has focused on understanding how attention head intervention can reveal causal relationships in transformer behavior and potentially control model outputs across different tasks."
    ],
    "durationSeconds": 7.138553003999998
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T20:41:17.105Z_

<details><summary>↩ Tool result · `toolu_01BzJMWsDZSvumkFpvb4Q9ED`</summary>

```text
Web search results for query: "task-independent attention specialization VLA vision-language-action model attention routing"

Links: [{"title":"GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization","url":"https://arxiv.org/html/2605.12369v1"},{"title":"[2605.12369v1] GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization","url":"https://arxiv.org/abs/2605.12369v1"},{"title":"FocusVLA: Focused Visual Utilization for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.28740"},{"title":"AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention","url":"https://arxiv.org/pdf/2511.18960"},{"title":"CogVLA: Cognition-Aligned Vision-Language-Action Model via Instruction-Driven Routing & Sparsification","url":"https://arxiv.org/pdf/2508.21046"},{"title":"AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention","url":"https://arxiv.org/html/2511.18960v1"},{"title":"Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge","url":"https://arxiv.org/html/2512.06951v1"}]

I found several relevant results about attention mechanisms in Vision-Language-Action (VLA) models. Here are the key findings:

## GuidedVLA: Task-Relevant Attention Specialization

GuidedVLA is a framework designed to guide action generation to focus on task-relevant factors by supervising individual attention heads with manually defined auxiliary signals to capture distinct factors, instantiating this with three specialized heads: object grounding, spatial geometry, and temporal skill logic. Across simulation and real-robot experiments, GuidedVLA improves success rates in both in-domain and out-of-domain settings compared to strong VLA baselines.

## FocusVLA: Task-Aligned Attention

FocusVLA uses Modality Cascaded Attention to enforce sequential modality interaction and proposes Focus Attention to suppress task-irrelevant information, leading to precise and robust manipulation.

## CogVLA: Instruction-Driven Attention Routing

CogVLA introduces Encoder-FiLM based Aggregation Routing that injects instruction information into the vision encoder to selectively aggregate visual tokens, and LLM-FiLM based Pruning Routing that introduces action intent into the language model by pruning instruction-irrelevant tokens.

## AVA-VLA: Active Visual Attention

AVA-VLA introduces an Active Visual Attention module that leverages recurrent state to dynamically modulate visual processing, enabling the model to actively filter irrelevant information and focus on task-critical features based on historical context.

These approaches represent different strategies for improving attention specialization in VLA models through various routing and gating mechanisms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "ec2cee05-4915-4d57-9a7d-2f86436953bb",
  "tool_use_result": {
    "query": "task-independent attention specialization VLA vision-language-action model attention routing",
    "results": [
      {
        "tool_use_id": "srvtoolu_012Us5u6cY25GMyhyUe8MjK1",
        "content": [
          {
            "title": "GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization",
            "url": "https://arxiv.org/html/2605.12369v1"
          },
          {
            "title": "[2605.12369v1] GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization",
            "url": "https://arxiv.org/abs/2605.12369v1"
          },
          {
            "title": "FocusVLA: Focused Visual Utilization for Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2603.28740"
          },
          {
            "title": "AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention",
            "url": "https://arxiv.org/pdf/2511.18960"
          },
          {
            "title": "CogVLA: Cognition-Aligned Vision-Language-Action Model via Instruction-Driven Routing & Sparsification",
            "url": "https://arxiv.org/pdf/2508.21046"
          },
          {
            "title": "AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention",
            "url": "https://arxiv.org/html/2511.18960v1"
          },
          {
            "title": "Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge",
            "url": "https://arxiv.org/html/2512.06951v1"
          }
        ]
      },
      "I found several relevant results about attention mechanisms in Vision-Language-Action (VLA) models. Here are the key findings:\n\n## GuidedVLA: Task-Relevant Attention Specialization\n\nGuidedVLA is a framework designed to guide action generation to focus on task-relevant factors by supervising individual attention heads with manually defined auxiliary signals to capture distinct factors, instantiating this with three specialized heads: object grounding, spatial geometry, and temporal skill logic. Across simulation and real-robot experiments, GuidedVLA improves success rates in both in-domain and out-of-domain settings compared to strong VLA baselines.\n\n## FocusVLA: Task-Aligned Attention\n\nFocusVLA uses Modality Cascaded Attention to enforce sequential modality interaction and proposes Focus Attention to suppress task-irrelevant information, leading to precise and robust manipulation.\n\n## CogVLA: Instruction-Driven Attention Routing\n\nCogVLA introduces Encoder-FiLM based Aggregation Routing that injects instruction information into the vision encoder to selectively aggregate visual tokens, and LLM-FiLM based Pruning Routing that introduces action intent into the language model by pruning instruction-irrelevant tokens.\n\n## AVA-VLA: Active Visual Attention\n\nAVA-VLA introduces an Active Visual Attention module that leverages recurrent state to dynamically modulate visual processing, enabling the model to actively filter irrelevant information and focus on task-critical features based on historical context.\n\nThese approaches represent different strategies for improving attention specialization in VLA models through various routing and gating mechanisms."
    ],
    "durationSeconds": 7.478971824
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T20:41:17.659Z_

<details><summary>↩ Tool result · `toolu_01Y3U6jz7dqUpC1ZQFpaBd5X`</summary>

```text
Web search results for query: "specific attention head indices consistent across tasks transformer interpretability "head identity" preservation"

Links: [{"title":"2026-01-09 Interpreting Transformers Through Attention Head Intervention","url":"https://www.arxiv.org/pdf/2601.04398"},{"title":"Interpreting Transformers Through Attention Head Intervention","url":"https://arxiv.org/html/2601.04398v3"},{"title":"Mechanistic Interpretability of Fine-Tuned Vision Transformers on   Distorted Images: Decoding Attention Head Behavior for Transparent and   Trustworthy AI","url":"https://arxiv.org/pdf/2503.18762"},{"title":"Head Pursuit: Probing Attention Specialization in Multimodal Transformers","url":"https://arxiv.org/pdf/2510.21518"},{"title":"GMAR: Gradient-Driven Multi-Head Attention Rollout for Vision Transformer Interpretability","url":"https://arxiv.org/html/2504.19414v1"},{"title":"Head Pursuit: Probing Attention Specialization in Multimodal Transformers","url":"https://arxiv.org/html/2510.21518"},{"title":"GitHub - IAAR-Shanghai/Awesome-Attention-Heads: An awesome repository & A comprehensive survey on interpretability of LLM attention heads. · GitHub","url":"https://github.com/IAAR-Shanghai/Awesome-Attention-Heads"},{"title":"Interpreting Context Look-ups in Transformers: Investigating Attention-MLP Interactions","url":"https://arxiv.org/html/2402.15055v1"},{"title":"Quantifying LLM Attention-Head Stability: Implications for Circuit Universality","url":"https://arxiv.org/pdf/2602.16740"}]

I found relevant research on attention head consistency and interpretability in transformers. Here are the key findings from my search:

## Head Specialization Across Tasks

Consistent patterns of specialization exist at the head level across both unimodal and multimodal transformers. Individual attention heads specialize in specific semantic or visual attributes, and research has uncovered specialized model components with consistent roles for attention heads, such as handling tokens of the same part of speech.

## Practical Head Preservation and Editing

Editing as few as 1% of the heads, selected using interpretability methods, can reliably suppress or enhance targeted concepts in model output. On question-answering tasks, ablating heads identified for "country"-related content selectively degrades performance on geography questions while preserving accuracy on other categories, demonstrating faithful mechanistic explanation.

## Stability and Identity Concerns

However, there are important nuances regarding head identity preservation across different training instances. Network circuits are rarely acid-tested for stability across different instances of the same deep learning architecture, and without this, it remains unclear whether reported circuits emerge universally or turn out to be idiosyncratic to a particular estimation instance. Attention heads in middle transformer layers are the least stable across refits and the most representationally distinct.

This research suggests that while attention heads demonstrate functional specialization within a given model, their specific indices may not necessarily preserve their identity across different training runs or instances.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "0f0a8c65-db19-4cc5-9026-2ace212f0249",
  "tool_use_result": {
    "query": "specific attention head indices consistent across tasks transformer interpretability \"head identity\" preservation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01L2g1oXSGxkV3uDYiLnDUAZ",
        "content": [
          {
            "title": "2026-01-09 Interpreting Transformers Through Attention Head Intervention",
            "url": "https://www.arxiv.org/pdf/2601.04398"
          },
          {
            "title": "Interpreting Transformers Through Attention Head Intervention",
            "url": "https://arxiv.org/html/2601.04398v3"
          },
          {
            "title": "Mechanistic Interpretability of Fine-Tuned Vision Transformers on   Distorted Images: Decoding Attention Head Behavior for Transparent and   Trustworthy AI",
            "url": "https://arxiv.org/pdf/2503.18762"
          },
          {
            "title": "Head Pursuit: Probing Attention Specialization in Multimodal Transformers",
            "url": "https://arxiv.org/pdf/2510.21518"
          },
          {
            "title": "GMAR: Gradient-Driven Multi-Head Attention Rollout for Vision Transformer Interpretability",
            "url": "https://arxiv.org/html/2504.19414v1"
          },
          {
            "title": "Head Pursuit: Probing Attention Specialization in Multimodal Transformers",
            "url": "https://arxiv.org/html/2510.21518"
          },
          {
            "title": "GitHub - IAAR-Shanghai/Awesome-Attention-Heads: An awesome repository & A comprehensive survey on interpretability of LLM attention heads. · GitHub",
            "url": "https://github.com/IAAR-Shanghai/Awesome-Attention-Heads"
          },
          {
            "title": "Interpreting Context Look-ups in Transformers: Investigating Attention-MLP Interactions",
            "url": "https://arxiv.org/html/2402.15055v1"
          },
          {
            "title": "Quantifying LLM Attention-Head Stability: Implications for Circuit Universality",
            "url": "https://arxiv.org/pdf/2602.16740"
          }
        ]
      },
      "I found relevant research on attention head consistency and interpretability in transformers. Here are the key findings from my search:\n\n## Head Specialization Across Tasks\n\nConsistent patterns of specialization exist at the head level across both unimodal and multimodal transformers. Individual attention heads specialize in specific semantic or visual attributes, and research has uncovered specialized model components with consistent roles for attention heads, such as handling tokens of the same part of speech.\n\n## Practical Head Preservation and Editing\n\nEditing as few as 1% of the heads, selected using interpretability methods, can reliably suppress or enhance targeted concepts in model output. On question-answering tasks, ablating heads identified for \"country\"-related content selectively degrades performance on geography questions while preserving accuracy on other categories, demonstrating faithful mechanistic explanation.\n\n## Stability and Identity Concerns\n\nHowever, there are important nuances regarding head identity preservation across different training instances. Network circuits are rarely acid-tested for stability across different instances of the same deep learning architecture, and without this, it remains unclear whether reported circuits emerge universally or turn out to be idiosyncratic to a particular estimation instance. Attention heads in middle transformer layers are the least stable across refits and the most representationally distinct.\n\nThis research suggests that while attention heads demonstrate functional specialization within a given model, their specific indices may not necessarily preserve their identity across different training runs or instances."
    ],
    "durationSeconds": 7.679451941000001
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the literature map and search results. Let me now fetch the most relevant papers for deeper analysis. The key papers to look at more closely are:

1. **"Quantifying LLM Attention-Head Stability: Implications for Circuit Universality"** (arxiv 2602.16740) - This is directly about head stability across training runs, very relevant to our h13/h22 finding
2. **"Head Pursuit: Probing Attention Specialization in Multimodal Transformers"** (arxiv 2510.21518) - About attention specialization in multimodal transformers


3. **"Why Attention Patterns Exist"** (ICLR 2026, arxiv 2601.21709) - Explores the underlying mechanisms driving attention pattern formation
4. **GuidedVLA** (2605.12369) and **CogVLA** (2508.21046) - Recent work on attention routing and specialization in vision-language models

Let me pull the full details on these most promising papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "d12c8f1e-4bc0-4532-bd9c-88efb04f9b79",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017FcW5aassWF9538nLDmSkq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12062,
      "cache_read_input_tokens": 25296,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12062
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

_source line 18_

Found several highly relevant papers. Let me fetch details on the most critical ones.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "f615c583-0885-4a6d-a26d-fc4393acd247",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017FcW5aassWF9538nLDmSkq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12062,
      "cache_read_input_tokens": 25296,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12062
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

_source line 19_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MY1QnS2nJKtWxFQNnvCFUF`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.16740",
  "prompt": "Extract: title, authors, year, venue, key findings about attention head stability across training runs, whether specific head indices are consistent, and any findings about \"universal\" vs \"idiosyncratic\" circuits. Also extract whether they study fine-tuned models or just pre-trained ones."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "f83cbd59-28a6-423f-8edb-b8e143e1a968",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017FcW5aassWF9538nLDmSkq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12062,
      "cache_read_input_tokens": 25296,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12062
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

_source line 20_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01E5GaN6aP7sJQ2LT6bS7her`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.21518",
  "prompt": "Extract: title, authors, year, venue, key findings about attention head specialization in multimodal transformers, whether specific heads are found to have consistent roles across tasks/inputs, and any findings about head identity preservation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "8acf1cc5-7351-4fe6-ada1-1d88472f139b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017FcW5aassWF9538nLDmSkq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12062,
      "cache_read_input_tokens": 25296,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12062
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UaQMJmJH5VuoXJuLasuqBE`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.21709",
  "prompt": "Extract: title, authors, year, venue, key findings about why attention patterns exist and their relationship to representational capacity and task consistency."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "10ad3d90-ff55-4438-9b98-5181c28e1503",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017FcW5aassWF9538nLDmSkq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12062,
      "cache_read_input_tokens": 25296,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12062
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JCxytLMCy9xs2zRY9Wxfqx`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.12369",
  "prompt": "Extract: title, authors, year, key findings about attention specialization in VLA models, whether they find natural attention head specialization patterns, and whether specific heads are assigned specific roles across tasks."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "8cd7c3fd-52f1-4274-8f31-4200f1042221",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017FcW5aassWF9538nLDmSkq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12062,
      "cache_read_input_tokens": 25296,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12062
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

_source line 23 · 2026-05-21T20:41:32.404Z_

<details><summary>↩ Tool result · `toolu_01MY1QnS2nJKtWxFQNnvCFUF`</summary>

```text
# Paper Summary

**Title:** Quantifying LLM Attention-Head Stability: Implications for Circuit Universality

**Authors:** Karan Bali, Jack Stanley, Praneet Suresh, Danilo Bzdok

**Year:** 2026 (submitted February 17, 2026)

**Venue:** arXiv (cs.LG - Computer Science/Machine Learning)

## Key Findings on Attention Head Stability

The researchers systematically examined whether transformer circuits remain consistent across independent training runs:

**Stability Patterns:**
- "Middle-layer heads are the least stable yet the most representationally distinct"
- Deeper models show stronger mid-depth divergence in attention head learning
- The residual stream exhibits comparative stability across refits
- Weight decay optimization substantially improves stability across random initializations

**Universal vs. Idiosyncratic Circuits:**
The paper directly addresses this distinction, noting that circuits are "rarely acid-tested for their stability across different instances," raising questions about whether circuits "emerge universally across labs or turn out to be idiosyncratic to a particular estimation instance."

**Head Indices:**
The research does not specifically address whether particular attention head indices remain consistent across runs.

**Model Types:**
The study focuses on "independently initialized training runs" of transformer language models, examining pre-trained instances rather than fine-tuned variants.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "391e973d-9d6f-4219-8baa-4a121e821753",
  "tool_use_result": {
    "bytes": 48241,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary\n\n**Title:** Quantifying LLM Attention-Head Stability: Implications for Circuit Universality\n\n**Authors:** Karan Bali, Jack Stanley, Praneet Suresh, Danilo Bzdok\n\n**Year:** 2026 (submitted February 17, 2026)\n\n**Venue:** arXiv (cs.LG - Computer Science/Machine Learning)\n\n## Key Findings on Attention Head Stability\n\nThe researchers systematically examined whether transformer circuits remain consistent across independent training runs:\n\n**Stability Patterns:**\n- \"Middle-layer heads are the least stable yet the most representationally distinct\"\n- Deeper models show stronger mid-depth divergence in attention head learning\n- The residual stream exhibits comparative stability across refits\n- Weight decay optimization substantially improves stability across random initializations\n\n**Universal vs. Idiosyncratic Circuits:**\nThe paper directly addresses this distinction, noting that circuits are \"rarely acid-tested for their stability across different instances,\" raising questions about whether circuits \"emerge universally across labs or turn out to be idiosyncratic to a particular estimation instance.\"\n\n**Head Indices:**\nThe research does not specifically address whether particular attention head indices remain consistent across runs.\n\n**Model Types:**\nThe study focuses on \"independently initialized training runs\" of transformer language models, examining pre-trained instances rather than fine-tuned variants.",
    "durationMs": 5657,
    "url": "https://arxiv.org/abs/2602.16740"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T20:41:32.943Z_

<details><summary>↩ Tool result · `toolu_01E5GaN6aP7sJQ2LT6bS7her`</summary>

```text
# Paper Summary: Head Pursuit

**Title:** Head Pursuit: Probing Attention Specialization in Multimodal Transformers

**Authors:** Lorenzo Basile, Valentino Maiorca, Diego Doimo, Francesco Locatello, Alberto Cazzaniga

**Year:** 2025

**Venue:** NeurIPS 2025 (spotlight presentation)

## Key Findings on Attention Head Specialization

The research demonstrates that individual attention heads exhibit specialized behavior across both unimodal and multimodal transformers. The authors developed a signal processing-based interpretability method to analyze how heads focus on particular semantic or visual attributes.

**Primary Discovery:** The study found "consistent patterns of specialization at the head level across both unimodal and multimodal transformers." This indicates that heads develop consistent functional roles within the network architecture.

**Practical Impact:** Remarkably, the researchers discovered that "editing as few as 1% of the heads...can reliably suppress or enhance targeted concepts in the model output." This demonstrates both the importance and manipulability of specialized heads.

## Head Identity and Task Consistency

The research validated its approach across diverse tasks—language-based (question answering, toxicity mitigation) and vision-language (image classification, captioning)—suggesting that head specialization patterns show stability across different task domains. The findings indicate an "interpretable and controllable structure within attention layers," suggesting heads maintain identifiable functional roles across contexts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "46eaba7c-c813-41a7-96e2-73f65bef5786",
  "tool_use_result": {
    "bytes": 46852,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary: Head Pursuit\n\n**Title:** Head Pursuit: Probing Attention Specialization in Multimodal Transformers\n\n**Authors:** Lorenzo Basile, Valentino Maiorca, Diego Doimo, Francesco Locatello, Alberto Cazzaniga\n\n**Year:** 2025\n\n**Venue:** NeurIPS 2025 (spotlight presentation)\n\n## Key Findings on Attention Head Specialization\n\nThe research demonstrates that individual attention heads exhibit specialized behavior across both unimodal and multimodal transformers. The authors developed a signal processing-based interpretability method to analyze how heads focus on particular semantic or visual attributes.\n\n**Primary Discovery:** The study found \"consistent patterns of specialization at the head level across both unimodal and multimodal transformers.\" This indicates that heads develop consistent functional roles within the network architecture.\n\n**Practical Impact:** Remarkably, the researchers discovered that \"editing as few as 1% of the heads...can reliably suppress or enhance targeted concepts in the model output.\" This demonstrates both the importance and manipulability of specialized heads.\n\n## Head Identity and Task Consistency\n\nThe research validated its approach across diverse tasks—language-based (question answering, toxicity mitigation) and vision-language (image classification, captioning)—suggesting that head specialization patterns show stability across different task domains. The findings indicate an \"interpretable and controllable structure within attention layers,\" suggesting heads maintain identifiable functional roles across contexts.",
    "durationMs": 5260,
    "url": "https://arxiv.org/abs/2510.21518"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-21T20:41:34.109Z_

<details><summary>↩ Tool result · `toolu_01UaQMJmJH5VuoXJuLasuqBE`</summary>

```text
# Paper Summary

**Title:** Why Attention Patterns Exist: A Unifying Temporal Perspective Analysis

**Authors:** Qingyue Yang, Jie Wang, Xing Li, Yinqi Bai, Xialiang Tong, Huiling Zhen, Jianye Hao, Mingxuan Yuan, Bin Li

**Year:** 2026

**Venue:** ICLR 2026

## Key Findings

The research introduces TAPPA (Temporal Attention Pattern Predictability Analysis), a framework that unifies understanding of diverse attention mechanisms in large language models. The authors categorize attention patterns into two groups: "predictable patterns with clear regularities and unpredictable patterns that appear effectively random."

A central discovery is that this distinction correlates with "the degree of query self-similarity along the temporal dimension." The framework explains previously fragmented observations—such as retrieval heads, sink heads, and diagonal traces—through a mathematically coherent lens examining how queries, keys, and Rotary Positional Embeddings interact.

The research validates these theoretical insights by applying them to practical tasks including KV cache compression and LLM pruning, demonstrating that metrics derived from TAPPA consistently outperform baseline approaches in these optimization contexts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "75178996-54ee-4549-ab1b-1ad484802e16",
  "tool_use_result": {
    "bytes": 47565,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary\n\n**Title:** Why Attention Patterns Exist: A Unifying Temporal Perspective Analysis\n\n**Authors:** Qingyue Yang, Jie Wang, Xing Li, Yinqi Bai, Xialiang Tong, Huiling Zhen, Jianye Hao, Mingxuan Yuan, Bin Li\n\n**Year:** 2026\n\n**Venue:** ICLR 2026\n\n## Key Findings\n\nThe research introduces TAPPA (Temporal Attention Pattern Predictability Analysis), a framework that unifies understanding of diverse attention mechanisms in large language models. The authors categorize attention patterns into two groups: \"predictable patterns with clear regularities and unpredictable patterns that appear effectively random.\"\n\nA central discovery is that this distinction correlates with \"the degree of query self-similarity along the temporal dimension.\" The framework explains previously fragmented observations—such as retrieval heads, sink heads, and diagonal traces—through a mathematically coherent lens examining how queries, keys, and Rotary Positional Embeddings interact.\n\nThe research validates these theoretical insights by applying them to practical tasks including KV cache compression and LLM pruning, demonstrating that metrics derived from TAPPA consistently outperform baseline approaches in these optimization contexts.",
    "durationMs": 5480,
    "url": "https://arxiv.org/abs/2601.21709"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T20:41:35.584Z_

<details><summary>↩ Tool result · `toolu_01JCxytLMCy9xs2zRY9Wxfqx`</summary>

```text
# GuidedVLA Paper Summary

**Title:** GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization

**Authors:** Xiaosong Jia, Bowen Yang, Zuhao Ge, Xian Nie, Yuchen Zhou, Cunxin Fan, Yufeng Li, Yilin Chai, Chao Jing, Zijian Liang, Qingwen Bu, Haidong Cao, Chao Wu, Qifeng Li, Zhenjie Yang, Chenhe Zhang, Hongyang Li, Zuxuan Wu, Junchi Yan, Yu-Gang Jiang

**Year:** 2026 (submitted May 12, 2026)

## Key Findings on Attention Specialization

**Core Approach:** Rather than relying on end-to-end learning, the framework treats "the action decoder not as a monolithic learner, but as an assembly of functional components." Individual attention heads receive supervision through manually defined auxiliary signals.

**Assigned Head Roles:** The paper instantiates three specialized heads with explicit functions:
- Object grounding
- Spatial geometry  
- Temporal skill logic

**Results:** The framework demonstrates improved success rates across both in-domain and out-of-domain settings compared to baseline VLA models. The authors establish that "the quality of these specialized factors correlates positively with task performance" and produce "decoupled, high-quality features."

The research treats attention head specialization as a deliberate design choice requiring external guidance rather than an emergent natural property.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "9834f786-49b2-47f8-be95-ac0ef206a580",
  "tool_use_result": {
    "bytes": 49437,
    "code": 200,
    "codeText": "OK",
    "result": "# GuidedVLA Paper Summary\n\n**Title:** GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization\n\n**Authors:** Xiaosong Jia, Bowen Yang, Zuhao Ge, Xian Nie, Yuchen Zhou, Cunxin Fan, Yufeng Li, Yilin Chai, Chao Jing, Zijian Liang, Qingwen Bu, Haidong Cao, Chao Wu, Qifeng Li, Zhenjie Yang, Chenhe Zhang, Hongyang Li, Zuxuan Wu, Junchi Yan, Yu-Gang Jiang\n\n**Year:** 2026 (submitted May 12, 2026)\n\n## Key Findings on Attention Specialization\n\n**Core Approach:** Rather than relying on end-to-end learning, the framework treats \"the action decoder not as a monolithic learner, but as an assembly of functional components.\" Individual attention heads receive supervision through manually defined auxiliary signals.\n\n**Assigned Head Roles:** The paper instantiates three specialized heads with explicit functions:\n- Object grounding\n- Spatial geometry  \n- Temporal skill logic\n\n**Results:** The framework demonstrates improved success rates across both in-domain and out-of-domain settings compared to baseline VLA models. The authors establish that \"the quality of these specialized factors correlates positively with task performance\" and produce \"decoupled, high-quality features.\"\n\nThe research treats attention head specialization as a deliberate design choice requiring external guidance rather than an emergent natural property.",
    "durationMs": 5678,
    "url": "https://arxiv.org/abs/2605.12369"
  }
}
```

</details>

---

### Assistant

_source line 27_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for more specific papers about head identity preservation across fine-tuning and "universal heads" in the transformer interpretability literature.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "1b82601d-78c0-422a-aef7-b8f82fcbd0f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNvuf7b22eShxHfp3i513E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2218,
      "cache_read_input_tokens": 37358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2218
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

_source line 28_

Let me search more specifically for the "universal heads" concept and head persistence through fine-tuning.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "3774021c-bf16-4262-923a-f5233177d0c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNvuf7b22eShxHfp3i513E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2218,
      "cache_read_input_tokens": 37358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2218
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

_source line 29_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AeRwx2EcBM3iXr8589qkwJ`</summary>

```json
{
  "query": "\"universal attention heads\" transformer fine-tuning same head indices persistent specialization 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "2db64d2d-ee43-4b0f-a110-1dd2acbb1ce2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNvuf7b22eShxHfp3i513E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2218,
      "cache_read_input_tokens": 37358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2218
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

_source line 30_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014nqUYtLfNqZLpcjAV1p7bt`</summary>

```json
{
  "query": "attention head function preserved after fine-tuning transformer \"same heads\" across models architectures 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "cd8a4743-aedd-4970-94db-9ae7dfe8ed22",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNvuf7b22eShxHfp3i513E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2218,
      "cache_read_input_tokens": 37358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2218
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

_source line 31 · 2026-05-21T20:41:48.063Z_

<details><summary>↩ Tool result · `toolu_01AeRwx2EcBM3iXr8589qkwJ`</summary>

```text
Web search results for query: ""universal attention heads" transformer fine-tuning same head indices persistent specialization 2024 2025 2026"

Links: [{"title":"Attention Head Specialization","url":"https://www.emergentmind.com/topics/attention-head-specialization"},{"title":"Reasoning-Focus Heads (RFHs) in Transformers","url":"https://www.emergentmind.com/topics/reasoning-focus-heads-rfhs"},{"title":"Mechanistic Interpretability of Fine-Tuned Vision Transformers on   Distorted Images: Decoding Attention Head Behavior for Transparent and   Trustworthy AI","url":"https://arxiv.org/pdf/2503.18762"},{"title":"Head Pursuit: Probing Attention Specialization in Multimodal Transformers","url":"https://arxiv.org/pdf/2510.21518"},{"title":"ResiDual Transformer Alignment with Spectral Decomposition","url":"https://arxiv.org/pdf/2411.00246"},{"title":"Multi-Head Softmax Attention Transformer","url":"https://www.emergentmind.com/topics/multi-head-softmax-attention-transformer"},{"title":"Augmenting Self-attention with Persistent Memory","url":"https://arxiv.org/pdf/1907.01470"}]

I found several relevant results about attention head specialization in transformers. Here's what the search revealed:

## Key Findings

Specialization has been observed to emerge in attention heads in both large language models and visual branches of CLIP models. Specialization appears to be a by-product related to large-scale training, though it's unclear exactly why it emerges and whether this is a systematic property.

### Recent Research (2024-2025)

Recent work includes "Differentiation and Specialization of Attention Heads via the Refined Local Learning Coefficient (2024)" and "Mechanistic Interpretability of Fine-Tuned Vision Transformers on Distorted Images: Decoding Attention Head Behavior for Transparent and Trustworthy AI (2025)".

A 2025 study examined individual attention heads in vision transformers fine-tuned on distorted images and revealed functional specialization in ViTs, showing how heads processed relevant vs. extraneous information.

### Universal Mechanisms

Reasoning-Focus Heads (RFHs) represent a modular and universal mechanism by which transformer models implement high-fidelity reasoning.

### Task-Specific Fine-tuning

Specialized heads can be fine-tuned or isolated per task for improved performance, and editing as few as 1% of the heads, selected using appropriate methods, can reliably suppress or enhance targeted concepts in model output.

The search results suggest that head specialization is a consistent phenomenon across different architectures and domains, with implications for efficient fine-tuning and model interpretability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "303801cf-5e47-4dda-95af-097d5417cbcc",
  "tool_use_result": {
    "query": "\"universal attention heads\" transformer fine-tuning same head indices persistent specialization 2024 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016N5dY5tJkdFGbmA8Taj8XD",
        "content": [
          {
            "title": "Attention Head Specialization",
            "url": "https://www.emergentmind.com/topics/attention-head-specialization"
          },
          {
            "title": "Reasoning-Focus Heads (RFHs) in Transformers",
            "url": "https://www.emergentmind.com/topics/reasoning-focus-heads-rfhs"
          },
          {
            "title": "Mechanistic Interpretability of Fine-Tuned Vision Transformers on   Distorted Images: Decoding Attention Head Behavior for Transparent and   Trustworthy AI",
            "url": "https://arxiv.org/pdf/2503.18762"
          },
          {
            "title": "Head Pursuit: Probing Attention Specialization in Multimodal Transformers",
            "url": "https://arxiv.org/pdf/2510.21518"
          },
          {
            "title": "ResiDual Transformer Alignment with Spectral Decomposition",
            "url": "https://arxiv.org/pdf/2411.00246"
          },
          {
            "title": "Multi-Head Softmax Attention Transformer",
            "url": "https://www.emergentmind.com/topics/multi-head-softmax-attention-transformer"
          },
          {
            "title": "Augmenting Self-attention with Persistent Memory",
            "url": "https://arxiv.org/pdf/1907.01470"
          }
        ]
      },
      "I found several relevant results about attention head specialization in transformers. Here's what the search revealed:\n\n## Key Findings\n\nSpecialization has been observed to emerge in attention heads in both large language models and visual branches of CLIP models. Specialization appears to be a by-product related to large-scale training, though it's unclear exactly why it emerges and whether this is a systematic property.\n\n### Recent Research (2024-2025)\n\nRecent work includes \"Differentiation and Specialization of Attention Heads via the Refined Local Learning Coefficient (2024)\" and \"Mechanistic Interpretability of Fine-Tuned Vision Transformers on Distorted Images: Decoding Attention Head Behavior for Transparent and Trustworthy AI (2025)\".\n\nA 2025 study examined individual attention heads in vision transformers fine-tuned on distorted images and revealed functional specialization in ViTs, showing how heads processed relevant vs. extraneous information.\n\n### Universal Mechanisms\n\nReasoning-Focus Heads (RFHs) represent a modular and universal mechanism by which transformer models implement high-fidelity reasoning.\n\n### Task-Specific Fine-tuning\n\nSpecialized heads can be fine-tuned or isolated per task for improved performance, and editing as few as 1% of the heads, selected using appropriate methods, can reliably suppress or enhance targeted concepts in model output.\n\nThe search results suggest that head specialization is a consistent phenomenon across different architectures and domains, with implications for efficient fine-tuning and model interpretability."
    ],
    "durationSeconds": 7.8390006439999995
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T20:41:48.084Z_

<details><summary>↩ Tool result · `toolu_014nqUYtLfNqZLpcjAV1p7bt`</summary>

```text
Web search results for query: "attention head function preserved after fine-tuning transformer "same heads" across models architectures 2025 2026"

Links: [{"title":"Frontiers | Adaptive noise-augmented attention for enhancing Transformer fine-tuning on longitudinal medical data","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1663484/full"},{"title":"2026-01-13 Interpreting Transformers Through Attention Head Intervention","url":"https://www.arxiv.org/pdf/2601.04398v3"},{"title":"Self-Attention Heads in Transformers","url":"https://www.emergentmind.com/topics/self-attention-heads"},{"title":"Inside Transformers: Attention, Scaling Tricks & Emerging Alternatives in 2025","url":"https://www.gocodeo.com/post/inside-transformers-attention-scaling-tricks-emerging-alternatives-in-2025"},{"title":"2026-01-12 Interpreting Transformers Through Attention Head Intervention","url":"https://www.arxiv.org/pdf/2601.04398v2"},{"title":"2026-01-09 Interpreting Transformers Through Attention Head Intervention","url":"https://www.arxiv.org/pdf/2601.04398"},{"title":"All-or-Here Attention in Transformers","url":"https://www.emergentmind.com/papers/2512.22562"},{"title":"The Effect of Attention Head Count on Transformer Approximation","url":"https://arxiv.org/pdf/2510.06662"}]

Based on the web search results, I found relevant information about attention head functions and their properties in transformer models:

## Key Findings on Attention Head Specialization and Function

Recent work by Basile et al. (2025) introduced a method for identifying and manipulating attention heads specialized for semantic properties in both language and vision-language models using Simultaneous Orthogonal Matching Pursuit (SOMP) to discover which vocabulary directions best explain each head's outputs.

Individual heads in Mistral-7B specialize for different semantic categories, with each head's top-attended tokens clustering coherently around its semantic category, including politics, nationality, temporal concepts, and numerical reasoning.

Regarding head specialization across models, studies on many-to-one multilingual models have found that even the core set of most important heads is largely language-agnostic and stable across diverse source languages.

## Function Preservation During Fine-tuning

For fine-tuning specifically, research shows that noise parameters are computed independently for each attention head to preserve head-specific attention dynamics during training, indicating that preserving individual head functions is an important consideration during fine-tuning procedures.

The search results also show broader interest in understanding which heads perform critical functions—the principle that the "heavy lifting" is performed by a residue of well-specialized heads, while the remainder can be pruned or reassigned for auxiliary functions—suggesting that certain heads maintain stable, specialized roles across different contexts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "9e5b1e9e-4cef-4ee1-bb16-32859dfb9ee7",
  "tool_use_result": {
    "query": "attention head function preserved after fine-tuning transformer \"same heads\" across models architectures 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RyzHdg4MX6FmDwm83JJfUt",
        "content": [
          {
            "title": "Frontiers | Adaptive noise-augmented attention for enhancing Transformer fine-tuning on longitudinal medical data",
            "url": "https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1663484/full"
          },
          {
            "title": "2026-01-13 Interpreting Transformers Through Attention Head Intervention",
            "url": "https://www.arxiv.org/pdf/2601.04398v3"
          },
          {
            "title": "Self-Attention Heads in Transformers",
            "url": "https://www.emergentmind.com/topics/self-attention-heads"
          },
          {
            "title": "Inside Transformers: Attention, Scaling Tricks & Emerging Alternatives in 2025",
            "url": "https://www.gocodeo.com/post/inside-transformers-attention-scaling-tricks-emerging-alternatives-in-2025"
          },
          {
            "title": "2026-01-12 Interpreting Transformers Through Attention Head Intervention",
            "url": "https://www.arxiv.org/pdf/2601.04398v2"
          },
          {
            "title": "2026-01-09 Interpreting Transformers Through Attention Head Intervention",
            "url": "https://www.arxiv.org/pdf/2601.04398"
          },
          {
            "title": "All-or-Here Attention in Transformers",
            "url": "https://www.emergentmind.com/papers/2512.22562"
          },
          {
            "title": "The Effect of Attention Head Count on Transformer Approximation",
            "url": "https://arxiv.org/pdf/2510.06662"
          }
        ]
      },
      "Based on the web search results, I found relevant information about attention head functions and their properties in transformer models:\n\n## Key Findings on Attention Head Specialization and Function\n\nRecent work by Basile et al. (2025) introduced a method for identifying and manipulating attention heads specialized for semantic properties in both language and vision-language models using Simultaneous Orthogonal Matching Pursuit (SOMP) to discover which vocabulary directions best explain each head's outputs.\n\nIndividual heads in Mistral-7B specialize for different semantic categories, with each head's top-attended tokens clustering coherently around its semantic category, including politics, nationality, temporal concepts, and numerical reasoning.\n\nRegarding head specialization across models, studies on many-to-one multilingual models have found that even the core set of most important heads is largely language-agnostic and stable across diverse source languages.\n\n## Function Preservation During Fine-tuning\n\nFor fine-tuning specifically, research shows that noise parameters are computed independently for each attention head to preserve head-specific attention dynamics during training, indicating that preserving individual head functions is an important consideration during fine-tuning procedures.\n\nThe search results also show broader interest in understanding which heads perform critical functions—the principle that the \"heavy lifting\" is performed by a residue of well-specialized heads, while the remainder can be pruned or reassigned for auxiliary functions—suggesting that certain heads maintain stable, specialized roles across different contexts."
    ],
    "durationSeconds": 7.226554217999998
  }
}
```

</details>

---

### Assistant

_source line 33_

<details><summary>Logged reasoning block</summary>

```text
Let me also check the "Reasoning-Focus Heads" paper and the ViT fine-tuning head specialization paper more closely, plus search for the Olsson et al. "induction heads" work which is a classic reference for universal head patterns.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "c46686d3-1e66-4d49-9d0d-2ceb6bb3a240",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YFhjrJEmdkuaxUahFqsBXd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1680,
      "cache_read_input_tokens": 39576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1680
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

_source line 34_

Let me fetch a few more key papers and search for the classic "induction heads" universality work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "e1931591-26fa-4a68-b229-e04702630722",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YFhjrJEmdkuaxUahFqsBXd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1680,
      "cache_read_input_tokens": 39576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1680
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

_source line 35_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019UvTkVzmcffe4xXB7zxs2K`</summary>

```json
{
  "query": "Olsson \"induction heads\" universal across models transformer mechanistic interpretability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "474ea7f2-6153-41b8-b35c-5261f3b2a0d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YFhjrJEmdkuaxUahFqsBXd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1680,
      "cache_read_input_tokens": 39576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1680
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DtujKe9tA8vt3yuYgV358c`</summary>

```json
{
  "url": "https://arxiv.org/abs/2503.18762",
  "prompt": "Extract: title, authors, year, key findings about attention head specialization in fine-tuned Vision Transformers. Do specific head indices maintain their function after fine-tuning? Is there cross-task head consistency?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "7d077a8b-5956-4910-a218-8cc7873b8a62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YFhjrJEmdkuaxUahFqsBXd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1680,
      "cache_read_input_tokens": 39576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1680
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VZNxp18z3SEF9SVxtcMVGh`</summary>

```json
{
  "query": "\"convergent\" attention heads across architectures \"same layer\" \"same head\" transformer universality circuit 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "495611c0-4811-4fac-b56d-6771addff643",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YFhjrJEmdkuaxUahFqsBXd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1680,
      "cache_read_input_tokens": 39576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1680
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

_source line 38 · 2026-05-21T20:41:58.615Z_

<details><summary>↩ Tool result · `toolu_01DtujKe9tA8vt3yuYgV358c`</summary>

```text
# Paper Summary

**Title:** Mechanistic Interpretability of Fine-Tuned Vision Transformers on Distorted Images: Decoding Attention Head Behavior for Transparent and Trustworthy AI

**Author:** Nooshin Bahador

**Year:** 2025 (submitted March 24, 2025)

## Key Findings on Attention Head Specialization

The research reveals functional stratification across transformer layers:

- **Early layers (1-3):** Minimal task relevance with "ablation increased MSE loss slightly" (approximately 0.11% mean increase)
- **Deeper layers (6+):** Substantially greater importance, causing "threefold higher loss increase" (~0.34% mean)
- **Intermediate layers (6-11):** Demonstrated "monosemantic behavior, attending exclusively to chirp regions"
- **Mixed early heads:** Some heads in layers 1-4 were monosemantic but task-irrelevant, functioning as "text detectors, edge or corner detectors"

## Regarding Cross-Task Consistency

The paper does not address whether specific head indices maintain function across different tasks or whether there is cross-task consistency. The study focuses exclusively on Vision Transformers fine-tuned on distorted spectrogram images, examining behavior within a single task context rather than comparing head functionality across multiple tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "34fd0fe5-4f17-4698-af3f-0ddc168edcdd",
  "tool_use_result": {
    "bytes": 46963,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary\n\n**Title:** Mechanistic Interpretability of Fine-Tuned Vision Transformers on Distorted Images: Decoding Attention Head Behavior for Transparent and Trustworthy AI\n\n**Author:** Nooshin Bahador\n\n**Year:** 2025 (submitted March 24, 2025)\n\n## Key Findings on Attention Head Specialization\n\nThe research reveals functional stratification across transformer layers:\n\n- **Early layers (1-3):** Minimal task relevance with \"ablation increased MSE loss slightly\" (approximately 0.11% mean increase)\n- **Deeper layers (6+):** Substantially greater importance, causing \"threefold higher loss increase\" (~0.34% mean)\n- **Intermediate layers (6-11):** Demonstrated \"monosemantic behavior, attending exclusively to chirp regions\"\n- **Mixed early heads:** Some heads in layers 1-4 were monosemantic but task-irrelevant, functioning as \"text detectors, edge or corner detectors\"\n\n## Regarding Cross-Task Consistency\n\nThe paper does not address whether specific head indices maintain function across different tasks or whether there is cross-task consistency. The study focuses exclusively on Vision Transformers fine-tuned on distorted spectrogram images, examining behavior within a single task context rather than comparing head functionality across multiple tasks.",
    "durationMs": 4571,
    "url": "https://arxiv.org/abs/2503.18762"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-21T20:41:59.886Z_

<details><summary>↩ Tool result · `toolu_019UvTkVzmcffe4xXB7zxs2K`</summary>

```text
Web search results for query: "Olsson "induction heads" universal across models transformer mechanistic interpretability"

Links: [{"title":"Induction Heads & In-Context Learning","url":"https://www.emergentmind.com/papers/2209.11895"},{"title":"Induction Head in Transformers","url":"https://www.emergentmind.com/topics/induction-head-ih"},{"title":"Mechanistic Interpretability: Part 7 - Induction Heads: The Mechanics of In-Context Learning | To Chin Yu","url":"https://ytcs.github.io/machine-learning/2025/05/25/mechanistic-interpretability-part-7.html"},{"title":"Induction Heads in Transformers","url":"https://www.emergentmind.com/topics/induction-heads-ihs"},{"title":"[2209.11895] In-context Learning and Induction Heads","url":"https://arxiv.org/abs/2209.11895"},{"title":"SELECTIVE INDUCTION HEADS: HOW TRANSFORM","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/d7ed243b13831bdd468f35039936bcef-Paper-Conference.pdf"},{"title":"(PDF) Mechanistic Interpretability of Induction Heads in Transformer Architectures","url":"https://www.researchgate.net/publication/392552787_Mechanistic_Interpretability_of_Induction_Heads_in_Transformer_Architectures"},{"title":"Induction Heads as an Essential Mechanism for Pattern ...","url":"https://aclanthology.org/2025.findings-naacl.283.pdf"}]

Based on the search results, here's what I found about Olsson's work on induction heads:

## Key Findings

Olsson and colleagues present evidence that induction heads may be the mechanistic source of general in-context learning in transformer models of any size. 

Induction heads are attention heads that implement a simple algorithm to complete token sequences like [A][B] ... [A] -> [B]. They are specialized attention heads in transformer architectures that implement a match-and-copy mechanism, enabling transformers to perform in-context learning by identifying token or sequence patterns in a prompt.

## Universality Across Models

The research confirms that mechanisms identified in small models reliably scale to larger systems, offering actionable insights for AI interpretability and safety. Induction heads develop at precisely the same point as a sudden sharp increase in in-context learning ability, visible as a bump in the training loss.

## Broader Implications

This circuit underlies a significant fraction of in-context learning in modern LLMs, governs early critical transitions in training dynamics, and is subject to distinct formation, redundancy, and generalization phenomena across architectures and data distributions. This research has uncovered the formation of induction heads, i.e., interpretable circuits embedded within the transformer's weights, capable of simple operations such as copying tokens.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "3d529f7d-8cfd-4fd9-b62a-36e380d385de",
  "tool_use_result": {
    "query": "Olsson \"induction heads\" universal across models transformer mechanistic interpretability",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CTNEv7wQwbZSAo7zaYhHmg",
        "content": [
          {
            "title": "Induction Heads & In-Context Learning",
            "url": "https://www.emergentmind.com/papers/2209.11895"
          },
          {
            "title": "Induction Head in Transformers",
            "url": "https://www.emergentmind.com/topics/induction-head-ih"
          },
          {
            "title": "Mechanistic Interpretability: Part 7 - Induction Heads: The Mechanics of In-Context Learning | To Chin Yu",
            "url": "https://ytcs.github.io/machine-learning/2025/05/25/mechanistic-interpretability-part-7.html"
          },
          {
            "title": "Induction Heads in Transformers",
            "url": "https://www.emergentmind.com/topics/induction-heads-ihs"
          },
          {
            "title": "[2209.11895] In-context Learning and Induction Heads",
            "url": "https://arxiv.org/abs/2209.11895"
          },
          {
            "title": "SELECTIVE INDUCTION HEADS: HOW TRANSFORM",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/d7ed243b13831bdd468f35039936bcef-Paper-Conference.pdf"
          },
          {
            "title": "(PDF) Mechanistic Interpretability of Induction Heads in Transformer Architectures",
            "url": "https://www.researchgate.net/publication/392552787_Mechanistic_Interpretability_of_Induction_Heads_in_Transformer_Architectures"
          },
          {
            "title": "Induction Heads as an Essential Mechanism for Pattern ...",
            "url": "https://aclanthology.org/2025.findings-naacl.283.pdf"
          }
        ]
      },
      "Based on the search results, here's what I found about Olsson's work on induction heads:\n\n## Key Findings\n\nOlsson and colleagues present evidence that induction heads may be the mechanistic source of general in-context learning in transformer models of any size. \n\nInduction heads are attention heads that implement a simple algorithm to complete token sequences like [A][B] ... [A] -> [B]. They are specialized attention heads in transformer architectures that implement a match-and-copy mechanism, enabling transformers to perform in-context learning by identifying token or sequence patterns in a prompt.\n\n## Universality Across Models\n\nThe research confirms that mechanisms identified in small models reliably scale to larger systems, offering actionable insights for AI interpretability and safety. Induction heads develop at precisely the same point as a sudden sharp increase in in-context learning ability, visible as a bump in the training loss.\n\n## Broader Implications\n\nThis circuit underlies a significant fraction of in-context learning in modern LLMs, governs early critical transitions in training dynamics, and is subject to distinct formation, redundancy, and generalization phenomena across architectures and data distributions. This research has uncovered the formation of induction heads, i.e., interpretable circuits embedded within the transformer's weights, capable of simple operations such as copying tokens."
    ],
    "durationSeconds": 7.263577312000002
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-21T20:42:00.535Z_

<details><summary>↩ Tool result · `toolu_01VZNxp18z3SEF9SVxtcMVGh`</summary>

```text
Web search results for query: ""convergent" attention heads across architectures "same layer" "same head" transformer universality circuit 2025 2026"

Links: [{"title":"Quantifying LLM Attention-Head Stability: Implications for Circuit Universality","url":"https://arxiv.org/html/2602.16740"},{"title":"[2602.16740] Quantifying LLM Attention-Head Stability: Implications for Circuit Universality","url":"https://arxiv.org/abs/2602.16740"},{"title":"Quantifying LLM Attention-Head Stability: Implications for Circuit Universality","url":"https://arxiv.org/pdf/2602.16740"},{"title":"Multi-Head Attention Layer in Transformers","url":"https://www.facebook.com/groups/DeepNetGroup/posts/2397145477344987/"},{"title":"On the Universality of Transformer Architectures; How Much Attention Is Enough?","url":"https://arxiv.org/pdf/2512.18445"}]

I found a highly relevant paper from February 2026 that directly addresses your query. Here are the key findings:

Recent mechanistic interpretability work scrutinizes transformer "circuits"—sparse, mono or multi-layer sub-computations that may reflect human-understandable functions. However, these network circuits are rarely tested for their stability across different instances of the same deep learning architecture.

The research investigates whether models converge to the requisite representational space—alignment of the attention head's induced representation, that is, the subspace it attends to and writes into—and therefore to the same functional behavior.

The study quantifies, layer by layer, how similarly attention heads learn representations across independently initialized training runs. The rigorous experiments show that: (1) middle-layer heads are the least stable yet the most representationally distinct; (2) deeper models exhibit stronger mid-depth divergence; (3) unstable heads in deeper layers become more functionally important than their peers from the same layer; (4) applying weight decay optimization substantially improves attention-head stability across random model initializations; and (5) the residual stream is comparatively stable.

The paper titled "Quantifying LLM Attention-Head Stability: Implications for Circuit Universality" (Bali et al., February 2026) directly examines convergence and universality of attention head circuits across different model instances.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "ea8dc92b-3ffe-4df4-8bb5-08d1c52b9e5e",
  "tool_use_result": {
    "query": "\"convergent\" attention heads across architectures \"same layer\" \"same head\" transformer universality circuit 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KkBWC92LUtTw4NdNXfzBFr",
        "content": [
          {
            "title": "Quantifying LLM Attention-Head Stability: Implications for Circuit Universality",
            "url": "https://arxiv.org/html/2602.16740"
          },
          {
            "title": "[2602.16740] Quantifying LLM Attention-Head Stability: Implications for Circuit Universality",
            "url": "https://arxiv.org/abs/2602.16740"
          },
          {
            "title": "Quantifying LLM Attention-Head Stability: Implications for Circuit Universality",
            "url": "https://arxiv.org/pdf/2602.16740"
          },
          {
            "title": "Multi-Head Attention Layer in Transformers",
            "url": "https://www.facebook.com/groups/DeepNetGroup/posts/2397145477344987/"
          },
          {
            "title": "On the Universality of Transformer Architectures; How Much Attention Is Enough?",
            "url": "https://arxiv.org/pdf/2512.18445"
          }
        ]
      },
      "I found a highly relevant paper from February 2026 that directly addresses your query. Here are the key findings:\n\nRecent mechanistic interpretability work scrutinizes transformer \"circuits\"—sparse, mono or multi-layer sub-computations that may reflect human-understandable functions. However, these network circuits are rarely tested for their stability across different instances of the same deep learning architecture.\n\nThe research investigates whether models converge to the requisite representational space—alignment of the attention head's induced representation, that is, the subspace it attends to and writes into—and therefore to the same functional behavior.\n\nThe study quantifies, layer by layer, how similarly attention heads learn representations across independently initialized training runs. The rigorous experiments show that: (1) middle-layer heads are the least stable yet the most representationally distinct; (2) deeper models exhibit stronger mid-depth divergence; (3) unstable heads in deeper layers become more functionally important than their peers from the same layer; (4) applying weight decay optimization substantially improves attention-head stability across random model initializations; and (5) the residual stream is comparatively stable.\n\nThe paper titled \"Quantifying LLM Attention-Head Stability: Implications for Circuit Universality\" (Bali et al., February 2026) directly examines convergence and universality of attention head circuits across different model instances."
    ],
    "durationSeconds": 5.713860535
  }
}
```

</details>

---

### Assistant

_source line 41_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me synthesize the findings:

## Summary of literature search

### Direct competitors with cross-task/cross-suite attention pattern consistency?
**None found.** The existing literature map already has the main VLA interpretability competitors (Grant 2026, Swann 2026, Rizzardo 2026, Haon 2025, etc.) and none of them report cross-task/cross-suite attention head consistency patterns. The new VLA attention papers (GuidedVLA, FocusVLA, CogVLA, AVA-VLA) are about *engineering* attention specialization, not *discovering* emergent consistent patterns.
 
I did find a couple of papers that touch on related territory. Bali et al. 2026 examines how stable attention heads are across different training runs, finding that middle-layer heads are actually the least stable but most representationally distinct—which is interesting because it contrasts with what I'm seeing: specific heads like h13 and h22 show consistency across different tasks within the same model, whereas their work shows instability across training runs. Basile et al. 2025 demonstrates consistent head specialization in multimodal transformers where editing just 1% of heads can reliably control behavior, which aligns more closely with the kind of targeted patterns I'm investigating.

Yang et al. 2026 provides theoretical grounding for why certain heads develop predictable patterns through temporal analysis, and Olsson et al. 2022 remains the foundational reference for head-level universality across models. GuidedVLA is an interesting counterpoint—they engineer head specialization deliberately, whereas I'm finding it emerges naturally in the fine-tuned models.

What's striking is that there's no direct precedent for discovering the same head indices consistently performing the same function across different task suites within a single fine-tuned model. Bali et al. actually suggests heads should be unstable across training runs, which makes this finding even more noteworthy.

Now I'm identifying the key papers to add to the literature map: Bali's work on attention-head stability directly supports the universality claim, Basile et al.'s Head Pursuit demonstrates that head specialization is real and manipulable in multimodal transformers, and Yang's ICLR paper provides the theoretical framework for why these patterns exist.

I should note that GuidedVLA is too recent and focused on engineering rather than discovery, so it's probably better to leave it out of the core map.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "7e41e241-ce6b-425b-82c5-93ecaabadee3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XjKwTomd4XBfjcM6w6cEjM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2015,
      "cache_read_input_tokens": 41256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2015
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

_source line 42_

Now I have enough to synthesize. Let me write the results to an artifact file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "e8a2ea04-ab15-4b40-9353-a7425a43de9c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XjKwTomd4XBfjcM6w6cEjM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2015,
      "cache_read_input_tokens": 41256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2015
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

_source line 43_

<details open><summary>🔧 Tool call — Bash · `toolu_01SLA8SEdLpxqcvLvFn8wZ7w`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "9c8c489d-147f-4bdc-aa45-bc20d3bc5c44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XjKwTomd4XBfjcM6w6cEjM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2015,
      "cache_read_input_tokens": 41256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2015
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

_source line 44 · 2026-05-21T20:42:30.071Z_

<details><summary>↩ Tool result · `toolu_01SLA8SEdLpxqcvLvFn8wZ7w`</summary>

```text
_project
ablation_narrative_playbook.md
action_metrics_extended
action_probe_design.md
analyze_ablation_50demos.py
attention
attention_decomposition
attention_decomposition_and_r2.py
attention_normalization_entropy
attention_normalization_entropy.py
behavioral_pilot_w4_diagnosis.md
bootstrap_task_ratio.json
branch_split_rsa_results.md
citation_verification_2026.md
closedloop_diagnosis.md
controlb_analysis
counterfactual_10tasks
counterfactual_instruction.py
counterfactual_spatial
counterfactual_spatial.py
counterfactual_token_overlap
cross_inst_extract_phase2
cross_instruction
definitive_rsa_results.md
demo_sensitivity.py
demo_standardized_rsa.md
dinov2_baseline
dream_reports
extract_fused_backbone.py
fig2_cross_instruction_heatmap.pdf
fig_cross_architecture_attention.pdf
fig_cross_architecture_attention.png
fig_cross_architecture_attention.py
fig_ood_diagnostics.png
fig_rsa_perlayer_curve.pdf
fig_rsa_perlayer_curve.png
fig_specificity_bootstrap_30seeds.pdf
fig_specificity_bootstrap_30seeds.png
figures
fix_dryrun.py
fulllayer_action_probe.py
groundtruth_action_error
kendall_w_cross_task.json
l1_ablation_action_probe_50demos.py
layer_stability_analysis.md
libero_finetuned_attention
libero_finetuned_probe_profile.json
libero_goal_feasibility.md
libero_object_full_pipeline.py
literature_map.yaml
literature_map_probing.md
literature_survey_instruction_probing.md
llama2base_action_probe.py
manifest.yaml
matched_ablation_controls.py
matched_ablation_controls_diagnosis.md
mvp_controlb_trained
mvp_probe_trained
nora_analysis_report.md
openvla_libero_goal_compat.md
paper_consistency_report.md
patch_probes.py
patch_rsa.py
pca_linear_probe_gc.py
pca_linear_probe_perlayer.py
permutation_10k
permutation_test_I2.py
phi3v_attention_profile
phi3v_attention_trained_10tasks
phi3v_attention_untrained
phi3v_probe_untrained
phi3v_r2_action_probe
phi3v_r2_seed_expansion
phi3v_r2_untrained_probe
phi3v_untrained_cross_inst_probe.py
phi3v_untrained_seed_expansion
pipeline_audit_libero_goal.md
plan_010_libero_spatial
plan_011_fulllayer_r2
plan_012_clip_vit_control
plot_dose_response.py
probe_design_plan.md
qa_probe_classification.py
random_subset_ablation.py
rebuttal_drafts.md
rebuttal_material_2026_05_20.md
redream_evidence_v2.md
review_issues.yaml
review_issues_updated.yaml
review_reports
rsa_analysis.py
rsa_branch_split.py
rsa_definitive.py
rsa_method_audit_report.md
rsa_unified_vla.py
second_vla_survey.md
specificity_random_seed_expansion
statistical_supplements
task_complexity_routing
task_routing_loo_sensitivity
tracvla_spatial
tracvla_spatial_full_pipeline.py
tracvla_spatial_trained
unified_action_probe.py
unified_rsa_summary.md
untrained_last_preaction_probe.json
vla-ssd_final_2026-05-19.pdf
vla-ssd_round12_2026-05-19.pdf
vla_rsa_method_audit.md
worker_output_diagnose_object_pipeline_ridge.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "31cc6a2a-95c4-49d0-bd94-7501c8bc2164",
  "tool_use_result": {
    "stdout": "_project\nablation_narrative_playbook.md\naction_metrics_extended\naction_probe_design.md\nanalyze_ablation_50demos.py\nattention\nattention_decomposition\nattention_decomposition_and_r2.py\nattention_normalization_entropy\nattention_normalization_entropy.py\nbehavioral_pilot_w4_diagnosis.md\nbootstrap_task_ratio.json\nbranch_split_rsa_results.md\ncitation_verification_2026.md\nclosedloop_diagnosis.md\ncontrolb_analysis\ncounterfactual_10tasks\ncounterfactual_instruction.py\ncounterfactual_spatial\ncounterfactual_spatial.py\ncounterfactual_token_overlap\ncross_inst_extract_phase2\ncross_instruction\ndefinitive_rsa_results.md\ndemo_sensitivity.py\ndemo_standardized_rsa.md\ndinov2_baseline\ndream_reports\nextract_fused_backbone.py\nfig2_cross_instruction_heatmap.pdf\nfig_cross_architecture_attention.pdf\nfig_cross_architecture_attention.png\nfig_cross_architecture_attention.py\nfig_ood_diagnostics.png\nfig_rsa_perlayer_curve.pdf\nfig_rsa_perlayer_curve.png\nfig_specificity_bootstrap_30seeds.pdf\nfig_specificity_bootstrap_30seeds.png\nfigures\nfix_dryrun.py\nfulllayer_action_probe.py\ngroundtruth_action_error\nkendall_w_cross_task.json\nl1_ablation_action_probe_50demos.py\nlayer_stability_analysis.md\nlibero_finetuned_attention\nlibero_finetuned_probe_profile.json\nlibero_goal_feasibility.md\nlibero_object_full_pipeline.py\nliterature_map.yaml\nliterature_map_probing.md\nliterature_survey_instruction_probing.md\nllama2base_action_probe.py\nmanifest.yaml\nmatched_ablation_controls.py\nmatched_ablation_controls_diagnosis.md\nmvp_controlb_trained\nmvp_probe_trained\nnora_analysis_report.md\nopenvla_libero_goal_compat.md\npaper_consistency_report.md\npatch_probes.py\npatch_rsa.py\npca_linear_probe_gc.py\npca_linear_probe_perlayer.py\npermutation_10k\npermutation_test_I2.py\nphi3v_attention_profile\nphi3v_attention_trained_10tasks\nphi3v_attention_untrained\nphi3v_probe_untrained\nphi3v_r2_action_probe\nphi3v_r2_seed_expansion\nphi3v_r2_untrained_probe\nphi3v_untrained_cross_inst_probe.py\nphi3v_untrained_seed_expansion\npipeline_audit_libero_goal.md\nplan_010_libero_spatial\nplan_011_fulllayer_r2\nplan_012_clip_vit_control\nplot_dose_response.py\nprobe_design_plan.md\nqa_probe_classification.py\nrandom_subset_ablation.py\nrebuttal_drafts.md\nrebuttal_material_2026_05_20.md\nredream_evidence_v2.md\nreview_issues.yaml\nreview_issues_updated.yaml\nreview_reports\nrsa_analysis.py\nrsa_branch_split.py\nrsa_definitive.py\nrsa_method_audit_report.md\nrsa_unified_vla.py\nsecond_vla_survey.md\nspecificity_random_seed_expansion\nstatistical_supplements\ntask_complexity_routing\ntask_routing_loo_sensitivity\ntracvla_spatial\ntracvla_spatial_full_pipeline.py\ntracvla_spatial_trained\nunified_action_probe.py\nunified_rsa_summary.md\nuntrained_last_preaction_probe.json\nvla-ssd_final_2026-05-19.pdf\nvla-ssd_round12_2026-05-19.pdf\nvla_rsa_method_audit.md\nworker_output_diagnose_object_pipeline_ridge.md",
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

_source line 45_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BaZagSgeXErMBBgf2h4det`</summary>

```json
{
  "query": "select:TodoWrite",
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
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "dc36d4c7-1e59-4508-99b7-41b2e0cfe518",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FbPSrSWQs1M8KCb6m5cVdh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2081,
      "cache_read_input_tokens": 43271,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2081
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

_source line 46 · 2026-05-21T20:42:32.503Z_

<details><summary>↩ Tool result · `toolu_01BaZagSgeXErMBBgf2h4det`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
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
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "282f7743-0ee8-4b33-b071-d727b7cffe95",
  "tool_use_result": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 47_

<details><summary>Logged reasoning block</summary>

```text
Let me now write the artifact file with the summary and suggested literature_map entries. Let me also check if there's a register_artifact tool I need to use.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "f0645f28-7664-4dce-af64-fb05c75cbccc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XufyrWDurKycdXBwudFmVf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2568,
      "cache_read_input_tokens": 45352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2568
      },
      "output_tokens": 29,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011Cwyjcprj95qVn53s4yyNA`</summary>

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
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "9d906914-a656-4def-98ce-6c44425010c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XufyrWDurKycdXBwudFmVf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2568,
      "cache_read_input_tokens": 45352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2568
      },
      "output_tokens": 29,
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

_source line 49 · 2026-05-21T20:42:36.377Z_

<details><summary>↩ Tool result · `toolu_011Cwyjcprj95qVn53s4yyNA`</summary>

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
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "d27de5e9-ed79-426a-a8aa-fc7a27b36086",
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

_source line 50_

<details open><summary>🔧 Tool call — Write · `toolu_01HMovqLgSGVtjduWxuzPAyg`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/literature_linkage_4suite_consistency.md",
  "content": "# TracVLA 4-Suite Consistency: Literature Linkage Report\n\n**Date**: 2026-05-21\n\n---\n\n## Summary (< 200 words)\n\n**No direct competitor** reports cross-task/cross-suite attention head consistency in VLA models. The existing literature map (Grant 2026, Swann 2026, Haon 2025 等) focuses on behavioral intervention, SAE features, or activation steering — none tracks specific head indices across task suites.\n\n**h13/h22 universal mixed heads** lack direct precedent. The closest references are: (1) **Olsson et al. 2022** — induction heads as universal circuits across model scales, but these are algorithmic (pattern-matching), not routing-functional; (2) **Basile et al. 2025** (Head Pursuit, NeurIPS 2025 spotlight) — shows consistent head specialization in multimodal transformers, editing 1% of heads controls output, but does not track same-index heads across tasks; (3) **Bali et al. 2026** — finds middle-layer heads are *least* stable across independent training runs, which actually *strengthens* our claim: h13/h22 consistency is a training-induced convergent property within a model, not a trivial artifact of initialization.\n\n**3 papers recommended for literature_map.yaml** (see below). No paper discovers convergent routing with head identity preservation across task suites — this remains our unique contribution.\n\n---\n\n## Detailed Analysis\n\n### 1. Direct Competitor Check\n\nScanned all 9 direct-competitor entries in literature_map.yaml. None reports:\n- Cross-suite attention pattern consistency\n- Specific head indices with consistent function across tasks\n- Convergent routing (CF ordering, R² inverted-U, exit collapse) across suites\n\n**GuidedVLA (Jia et al., May 2026)** is the only VLA paper explicitly about attention head specialization, but they *engineer* it (supervised auxiliary signals for object/spatial/temporal heads), not *discover* it emergently. This is a useful contrast: we show VLA training naturally produces convergent routing without explicit supervision.\n\n### 2. h13/h22 Head Identity Preservation — Literature Support\n\n| Reference | Finding | Relation to h13/h22 |\n|-----------|---------|---------------------|\n| Olsson et al. 2022 | Induction heads are universal circuits across model scales | Precedent for functional universality at head level, but algorithmic (copy mechanism), not routing |\n| Basile et al. 2025 (Head Pursuit) | Consistent head specialization in multimodal transformers; 1% head editing controls output | Supports head-level functional specialization as real phenomenon; no same-index tracking across tasks |\n| Bali et al. 2026 | Middle-layer heads least stable across training runs, most representationally distinct | **Key contrast**: instability across runs ≠ instability across tasks within a run. Our h13/h22 consistency is *within-model cross-task*, a distinct (stronger) claim |\n| Bahador 2025 | ViT fine-tuning: deeper heads more important, intermediate heads monosemantic | Layer-level stratification consistent with our L1 instruction-dominant finding |\n| Yang et al. 2026 (TAPPA, ICLR 2026) | Unifies attention patterns via temporal predictability; predictable vs unpredictable patterns | Theoretical framework for *why* certain heads develop consistent patterns |\n\n**Bottom line**: Head specialization is well-established. Head identity preservation *across task suites within a fine-tuned VLA* is not. Our h13/h22 finding sits in a gap between \"heads specialize\" (known) and \"the same heads specialize the same way across diverse tasks\" (novel).\n\n### 3. Convergent Routing Pattern — Novelty Position\n\nThe full convergent routing pattern (CF ordering + R² inverted-U + exit collapse + L1 instruction dominance) across 3 architectures × 4 suites has no precedent. The closest work:\n- **Grant 2026**: Cross-architecture comparison but of *different* properties (vision dominance, language ignoring), not routing convergence\n- **Bali 2026**: Cross-run stability, not cross-task consistency\n- **Head Pursuit**: Cross-task head specialization in VLMs, not VLAs, and no routing pattern analysis\n\n---\n\n## Suggested literature_map.yaml Entries\n\n### Entry 1: bali2026\n\n```yaml\n- id: bali2026\n  title: \"Quantifying LLM Attention-Head Stability: Implications for Circuit Universality\"\n  authors: \"Karan Bali, Jack Stanley, Praneet Suresh, Danilo Bzdok\"\n  year: 2026\n  venue: \"arXiv preprint\"\n  arxiv_id: \"2602.16740\"\n  category: method-component\n  role: context\n  key_findings: >\n    Systematically quantifies attention head stability across independently initialized training runs.\n    Middle-layer heads are least stable yet most representationally distinct. Deeper models show\n    stronger mid-depth divergence. Weight decay improves stability. Residual stream comparatively stable.\n  relevance_to_us: >\n    Key contrast paper for h13/h22 universality claim. Their finding that heads are unstable across\n    training runs strengthens our claim: h13/h22 cross-task consistency is a training-induced convergent\n    property, not a trivial initialization artifact. Cross-run instability ≠ cross-task instability.\n  novelty_gap: >\n    Studies pre-trained LLMs across random seeds, not fine-tuned VLAs across task suites.\n    No cross-task consistency analysis within a single trained model.\n```\n\n### Entry 2: basile2025_headpursuit\n\n```yaml\n- id: basile2025_headpursuit\n  title: \"Head Pursuit: Probing Attention Specialization in Multimodal Transformers\"\n  authors: \"Lorenzo Basile, Valentino Maiorca, Diego Doimo, Francesco Locatello, Alberto Cazzaniga\"\n  year: 2025\n  venue: \"NeurIPS 2025 (Spotlight)\"\n  arxiv_id: \"2510.21518\"\n  category: method-component\n  role: methodology\n  key_findings: >\n    Consistent head specialization patterns in unimodal and multimodal transformers.\n    Signal processing-based method (SOMP) identifies semantic specialization per head.\n    Editing 1% of heads reliably suppresses/enhances targeted concepts.\n    Validated across QA, toxicity, image classification, captioning.\n  relevance_to_us: >\n    Strongest methodological support for head-level specialization as real phenomenon.\n    Their cross-task validation (QA + toxicity + vision tasks) parallels our cross-suite validation.\n    However they do not track same-index heads across tasks — our h13/h22 identity preservation goes further.\n  novelty_gap: >\n    VLM focus, not VLA. No routing pattern analysis. No trained vs untrained comparison.\n    Does not track whether same head indices serve same function across tasks.\n```\n\n### Entry 3: olsson2022_induction\n\n```yaml\n- id: olsson2022_induction\n  title: \"In-context Learning and Induction Heads\"\n  authors: \"Catherine Olsson, Nelson Elhage, Neel Nanda, et al.\"\n  year: 2022\n  venue: \"arXiv preprint (Anthropic)\"\n  arxiv_id: \"2209.11895\"\n  category: method-component\n  role: context\n  key_findings: >\n    Induction heads implement match-and-copy ([A][B]...[A]→[B]) and are mechanistic source of\n    in-context learning. Emerge at same training point as ICL ability phase transition.\n    Universal across model scales — canonical example of circuit-level universality.\n  relevance_to_us: >\n    Classic precedent for \"specific heads with universal function across contexts.\"\n    Our h13/h22 mixed heads are analogous: specific heads with consistent routing function across\n    task suites. Induction heads = algorithmic universality; our finding = routing universality in VLAs.\n  novelty_gap: >\n    Purely LLM, not VLA. Induction is a copying mechanism, not multimodal routing.\n    No cross-task consistency analysis in the fine-tuning setting.\n```\n\n---\n\n## Action Items\n\n1. **Add 3 entries above to literature_map.yaml** under appropriate categories (bali2026 + basile2025 → method-component; olsson2022 → method-component)\n2. **Update categories index** to include new papers\n3. **Paper framing**: The h13/h22 finding can be positioned as \"convergent routing heads\" — extending the induction head universality concept (Olsson 2022) from algorithmic circuits to multimodal routing in VLAs, with the Bali 2026 cross-run instability result as a foil that highlights the within-model cross-task nature of our claim\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "6b6311a0-50f6-43c3-bfbd-c7a97454220d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013GePXq89V4u7NW3Kt1pBdU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 143,
      "cache_read_input_tokens": 47920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 143
      },
      "output_tokens": 61,
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

_source line 51 · 2026-05-21T20:43:31.135Z_

<details><summary>↩ Tool result · `toolu_01HMovqLgSGVtjduWxuzPAyg`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/literature_linkage_4suite_consistency.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "9cb8f54e-f928-465d-8aba-0c533a4e91d0",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/literature_linkage_4suite_consistency.md",
    "content": "# TracVLA 4-Suite Consistency: Literature Linkage Report\n\n**Date**: 2026-05-21\n\n---\n\n## Summary (< 200 words)\n\n**No direct competitor** reports cross-task/cross-suite attention head consistency in VLA models. The existing literature map (Grant 2026, Swann 2026, Haon 2025 等) focuses on behavioral intervention, SAE features, or activation steering — none tracks specific head indices across task suites.\n\n**h13/h22 universal mixed heads** lack direct precedent. The closest references are: (1) **Olsson et al. 2022** — induction heads as universal circuits across model scales, but these are algorithmic (pattern-matching), not routing-functional; (2) **Basile et al. 2025** (Head Pursuit, NeurIPS 2025 spotlight) — shows consistent head specialization in multimodal transformers, editing 1% of heads controls output, but does not track same-index heads across tasks; (3) **Bali et al. 2026** — finds middle-layer heads are *least* stable across independent training runs, which actually *strengthens* our claim: h13/h22 consistency is a training-induced convergent property within a model, not a trivial artifact of initialization.\n\n**3 papers recommended for literature_map.yaml** (see below). No paper discovers convergent routing with head identity preservation across task suites — this remains our unique contribution.\n\n---\n\n## Detailed Analysis\n\n### 1. Direct Competitor Check\n\nScanned all 9 direct-competitor entries in literature_map.yaml. None reports:\n- Cross-suite attention pattern consistency\n- Specific head indices with consistent function across tasks\n- Convergent routing (CF ordering, R² inverted-U, exit collapse) across suites\n\n**GuidedVLA (Jia et al., May 2026)** is the only VLA paper explicitly about attention head specialization, but they *engineer* it (supervised auxiliary signals for object/spatial/temporal heads), not *discover* it emergently. This is a useful contrast: we show VLA training naturally produces convergent routing without explicit supervision.\n\n### 2. h13/h22 Head Identity Preservation — Literature Support\n\n| Reference | Finding | Relation to h13/h22 |\n|-----------|---------|---------------------|\n| Olsson et al. 2022 | Induction heads are universal circuits across model scales | Precedent for functional universality at head level, but algorithmic (copy mechanism), not routing |\n| Basile et al. 2025 (Head Pursuit) | Consistent head specialization in multimodal transformers; 1% head editing controls output | Supports head-level functional specialization as real phenomenon; no same-index tracking across tasks |\n| Bali et al. 2026 | Middle-layer heads least stable across training runs, most representationally distinct | **Key contrast**: instability across runs ≠ instability across tasks within a run. Our h13/h22 consistency is *within-model cross-task*, a distinct (stronger) claim |\n| Bahador 2025 | ViT fine-tuning: deeper heads more important, intermediate heads monosemantic | Layer-level stratification consistent with our L1 instruction-dominant finding |\n| Yang et al. 2026 (TAPPA, ICLR 2026) | Unifies attention patterns via temporal predictability; predictable vs unpredictable patterns | Theoretical framework for *why* certain heads develop consistent patterns |\n\n**Bottom line**: Head specialization is well-established. Head identity preservation *across task suites within a fine-tuned VLA* is not. Our h13/h22 finding sits in a gap between \"heads specialize\" (known) and \"the same heads specialize the same way across diverse tasks\" (novel).\n\n### 3. Convergent Routing Pattern — Novelty Position\n\nThe full convergent routing pattern (CF ordering + R² inverted-U + exit collapse + L1 instruction dominance) across 3 architectures × 4 suites has no precedent. The closest work:\n- **Grant 2026**: Cross-architecture comparison but of *different* properties (vision dominance, language ignoring), not routing convergence\n- **Bali 2026**: Cross-run stability, not cross-task consistency\n- **Head Pursuit**: Cross-task head specialization in VLMs, not VLAs, and no routing pattern analysis\n\n---\n\n## Suggested literature_map.yaml Entries\n\n### Entry 1: bali2026\n\n```yaml\n- id: bali2026\n  title: \"Quantifying LLM Attention-Head Stability: Implications for Circuit Universality\"\n  authors: \"Karan Bali, Jack Stanley, Praneet Suresh, Danilo Bzdok\"\n  year: 2026\n  venue: \"arXiv preprint\"\n  arxiv_id: \"2602.16740\"\n  category: method-component\n  role: context\n  key_findings: >\n    Systematically quantifies attention head stability across independently initialized training runs.\n    Middle-layer heads are least stable yet most representationally distinct. Deeper models show\n    stronger mid-depth divergence. Weight decay improves stability. Residual stream comparatively stable.\n  relevance_to_us: >\n    Key contrast paper for h13/h22 universality claim. Their finding that heads are unstable across\n    training runs strengthens our claim: h13/h22 cross-task consistency is a training-induced convergent\n    property, not a trivial initialization artifact. Cross-run instability ≠ cross-task instability.\n  novelty_gap: >\n    Studies pre-trained LLMs across random seeds, not fine-tuned VLAs across task suites.\n    No cross-task consistency analysis within a single trained model.\n```\n\n### Entry 2: basile2025_headpursuit\n\n```yaml\n- id: basile2025_headpursuit\n  title: \"Head Pursuit: Probing Attention Specialization in Multimodal Transformers\"\n  authors: \"Lorenzo Basile, Valentino Maiorca, Diego Doimo, Francesco Locatello, Alberto Cazzaniga\"\n  year: 2025\n  venue: \"NeurIPS 2025 (Spotlight)\"\n  arxiv_id: \"2510.21518\"\n  category: method-component\n  role: methodology\n  key_findings: >\n    Consistent head specialization patterns in unimodal and multimodal transformers.\n    Signal processing-based method (SOMP) identifies semantic specialization per head.\n    Editing 1% of heads reliably suppresses/enhances targeted concepts.\n    Validated across QA, toxicity, image classification, captioning.\n  relevance_to_us: >\n    Strongest methodological support for head-level specialization as real phenomenon.\n    Their cross-task validation (QA + toxicity + vision tasks) parallels our cross-suite validation.\n    However they do not track same-index heads across tasks — our h13/h22 identity preservation goes further.\n  novelty_gap: >\n    VLM focus, not VLA. No routing pattern analysis. No trained vs untrained comparison.\n    Does not track whether same head indices serve same function across tasks.\n```\n\n### Entry 3: olsson2022_induction\n\n```yaml\n- id: olsson2022_induction\n  title: \"In-context Learning and Induction Heads\"\n  authors: \"Catherine Olsson, Nelson Elhage, Neel Nanda, et al.\"\n  year: 2022\n  venue: \"arXiv preprint (Anthropic)\"\n  arxiv_id: \"2209.11895\"\n  category: method-component\n  role: context\n  key_findings: >\n    Induction heads implement match-and-copy ([A][B]...[A]→[B]) and are mechanistic source of\n    in-context learning. Emerge at same training point as ICL ability phase transition.\n    Universal across model scales — canonical example of circuit-level universality.\n  relevance_to_us: >\n    Classic precedent for \"specific heads with universal function across contexts.\"\n    Our h13/h22 mixed heads are analogous: specific heads with consistent routing function across\n    task suites. Induction heads = algorithmic universality; our finding = routing universality in VLAs.\n  novelty_gap: >\n    Purely LLM, not VLA. Induction is a copying mechanism, not multimodal routing.\n    No cross-task consistency analysis in the fine-tuning setting.\n```\n\n---\n\n## Action Items\n\n1. **Add 3 entries above to literature_map.yaml** under appropriate categories (bali2026 + basile2025 → method-component; olsson2022 → method-component)\n2. **Update categories index** to include new papers\n3. **Paper framing**: The h13/h22 finding can be positioned as \"convergent routing heads\" — extending the induction head universality concept (Olsson 2022) from algorithmic circuits to multimodal routing in VLAs, with the Bali 2026 cross-run instability result as a foil that highlights the within-model cross-task nature of our claim\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
````

</details>

---

### Assistant

_source line 52_

产出文件已写入 `artifacts/literature_linkage_4suite_consistency.md`。核心结论：

**无直接竞品论文**报告过跨 task suite 的 attention head consistency pattern。现有 VLA 解释性文献（Grant/Swann/Haon/Rizzardo）全部聚焦行为干预或 SAE 特征，无人追踪 specific head indices 的跨任务一致性。

**h13/h22 head identity preservation 无直接先例**，但有三层文献支撑：
- **Olsson et al. 2022**（induction heads）：head 级功能普遍性的经典范例，但机制是 algorithmic copy，非 routing
- **Basile et al. 2025**（Head Pursuit, NeurIPS spotlight）：多模态 transformer 中 head 专化一致且可操控，但未追踪 same-index cross-task
- **Bali et al. 2026**：中间层 head 跨训练 run 最不稳定——这反而加强我们的 claim：h13/h22 的 cross-task 一致性是 training-induced convergent property，非初始化 artifact

**建议添加 3 条文献到 literature_map.yaml**（bali2026, basile2025_headpursuit, olsson2022_induction），详细条目见产出文件。

**GuidedVLA（Jia et al., 2026.05）**是唯一涉及 VLA attention head specialization 的论文，但它是人工监督强制的，非 emergent——可作为对照引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "uuid": "82b98255-3ea9-4c06-abf1-a5b113bd7f50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FX1KGU8g6ywHh52AQqDeZe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2358,
      "cache_read_input_tokens": 48063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2358
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

_source line 53_

产出文件已写入 `artifacts/literature_linkage_4suite_consistency.md`。核心结论：

**无直接竞品论文**报告过跨 task suite 的 attention head consistency pattern。现有 VLA 解释性文献（Grant/Swann/Haon/Rizzardo）全部聚焦行为干预或 SAE 特征，无人追踪 specific head indices 的跨任务一致性。

**h13/h22 head identity preservation 无直接先例**，但有三层文献支撑：
- **Olsson et al. 2022**（induction heads）：head 级功能普遍性的经典范例，但机制是 algorithmic copy，非 routing
- **Basile et al. 2025**（Head Pursuit, NeurIPS spotlight）：多模态 transformer 中 head 专化一致且可操控，但未追踪 same-index cross-task
- **Bali et al. 2026**：中间层 head 跨训练 run 最不稳定——这反而加强我们的 claim：h13/h22 的 cross-task 一致性是 training-induced convergent property，非初始化 artifact

**建议添加 3 条文献到 literature_map.yaml**（bali2026, basile2025_headpursuit, olsson2022_induction），详细条目见产出文件。

**GuidedVLA（Jia et al., 2026.05）**是唯一涉及 VLA attention head specialization 的论文，但它是人工监督强制的，非 emergent——可作为对照引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 162516,
  "duration_api_ms": 214428,
  "num_turns": 19,
  "stop_reason": "end_turn",
  "session_id": "4f814758-d1b9-4a98-a712-2b05734e8d9c",
  "total_cost_usd": 0.7438990000000001,
  "usage": {
    "input_tokens": 16,
    "cache_creation_input_tokens": 38580,
    "cache_read_input_tokens": 363320,
    "output_tokens": 5693,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 38580,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 446,
        "cache_read_input_tokens": 48063,
        "cache_creation_input_tokens": 2358,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2358
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 84374,
      "outputTokens": 4867,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 7,
      "costUSD": 0.178709,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 16,
      "outputTokens": 5693,
      "cacheReadInputTokens": 363320,
      "cacheCreationInputTokens": 38580,
      "webSearchRequests": 0,
      "costUSD": 0.56519,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "6a2543a0-c41b-45e9-8e6e-030fa2a3b9d9"
}
```

</details>

---
