# research literature linkage exp004

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/workers/worker_research_literature-linkage-exp004_20260518T102211.log`
- **Structured JSON:** [`185c8e6c71127bd88ce6.json`](../../sessions/18/185c8e6c71127bd88ce6.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews",
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
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
  "uuid": "3665a3e3-a71f-4fe4-ab21-8e83eef654f8",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-5-projects-spectral-collapse-ews/memory/"
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
    "resetsAt": 1779110400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "36e0f7a8-e0ff-4034-96d1-4dd0f6d80fd0",
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to do a literature search about the divergence between spectral metrics and diversity metrics in model collapse scenarios. Let me break this down:

1. Search for relevant papers using WebSearch
2. Check existing literature_map.yaml
3. Write a report

Let me start by reading the literature_map.yaml and doing web searches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "25420981-6360-40f0-bb78-dc839dbdc697",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8BWwPPQ6V8Z3a39Mft8sN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13165,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13165
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

### Assistant

_source line 5_

开始文献调研。先并行读取已有 literature_map 和进行多组关键词搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "290002f9-768f-40a5-bcb1-54b96a3ac5e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8BWwPPQ6V8Z3a39Mft8sN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13165,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13165
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

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Ri8XkTFTXhLj1gh5Dk2PV8`</summary>

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
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "44665bd2-1d87-4276-8d42-1b9f716c2660",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8BWwPPQ6V8Z3a39Mft8sN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13165,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13165
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

_source line 7 · 2026-05-18T10:22:24.316Z_

<details><summary>↩ Tool result · `toolu_01Ri8XkTFTXhLj1gh5Dk2PV8`</summary>

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
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "a1adbf7f-4fc9-47d5-a89b-77c6da3323a7",
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

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0115qb2vF5r922jLzt7b3ckU`</summary>

```json
{
  "project": "spectral_collapse_ews",
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
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "262aa16c-5eff-452f-8de4-345c24af84d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrWpFQEKztUQ57uriheGHV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1060,
      "cache_read_input_tokens": 25006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1060
      },
      "output_tokens": 70,
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

_source line 9 · 2026-05-18T10:22:27.301Z_

<details><summary>↩ Tool result · `toolu_0115qb2vF5r922jLzt7b3ckU`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/literature_map.yaml\", \"content\": \"papers:\\n  # ============================================================\\n  # Cluster 1: model_collapse_core (6 papers)\\n  # ============================================================\\n  - bibtex_key: shumailov2024collapse\\n    title: \\\"AI models collapse when trained on recursively generated data\\\"\\n    authors: \\\"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin\\\"\\n    year: 2024\\n    venue: \\\"Nature\\\"\\n    arxiv_id: \\\"2305.17493\\\"\\n    doi: \\\"10.1038/s41586-024-07566-y\\\"\\n    category: model_collapse_core\\n    verified: true\\n    abstract_short: \\\"Shows that training on model-generated data causes irreversible defects where tails of the original content distribution disappear, leading to model collapse across LLMs, VAEs, and GMMs.\\\"\\n    relevance: \\\"Seminal paper defining model collapse. Our work provides spectral EWS to detect collapse onset before irreversible degradation.\\\"\\n\\n  - bibtex_key: dohmatob2024tails\\n    title: \\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\"\\n    authors: \\\"Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia\\\"\\n    year: 2024\\n    venue: \\\"ICML 2024\\\"\\n    arxiv_id: \\\"2402.07043\\\"\\n    doi: \\\"\\\"\\n    category: model_collapse_core\\n    verified: true\\n    abstract_short: \\\"Provides first theoretical framework for model collapse through scaling laws, showing how tail distributions vanish across generations with validated experiments on transformers.\\\"\\n    relevance: \\\"Theoretical foundation for understanding collapse dynamics. Our spectral metrics connect to their scaling law framework.\\\"\\n\\n  - bibtex_key: alemohammad2024mad\\n    title: \\\"Self-Consuming Generative Models Go MAD\\\"\\n    authors: \\\"Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.\\\"\\n    year: 2024\\n    venue: \\\"ICLR 2024\\\"\\n    arxiv_id: \\\"2307.01850\\\"\\n    doi: \\\"\\\"\\n    category: model_collapse_core\\n    verified: true\\n    abstract_short: \\\"Introduces Model Autophagy Disorder (MAD) showing that without fresh real data, autophagous loops cause progressive quality/diversity loss in just a few generations.\\\"\\n    relevance: \\\"Establishes MAD framework for self-consuming loops. Our EWS can detect MADness onset before quality degrades.\\\"\\n\\n  - bibtex_key: gerstgrasser2024inevitable\\n    title: \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\"\\n    authors: \\\"Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi\\\"\\n    year: 2024\\n    venue: \\\"arXiv\\\"\\n    arxiv_id: \\\"2404.01413\\\"\\n    doi: \\\"\\\"\\n    category: model_collapse_core\\n    verified: true\\n    abstract_short: \\\"Shows that accumulating synthetic data alongside real data avoids model collapse, with finite upper bound on test error independent of iteration count.\\\"\\n    relevance: \\\"Key mitigation result. Our EWS enables knowing when to inject real data vs. when accumulation suffices.\\\"\\n\\n  - bibtex_key: dohmatob2024demystified\\n    title: \\\"Model Collapse Demystified: The Case of Regression\\\"\\n    authors: \\\"Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS 2024\\\"\\n    arxiv_id: \\\"2402.07712\\\"\\n    doi: \\\"\\\"\\n    category: model_collapse_core\\n    verified: true\\n    abstract_short: \\\"Derives analytical formulas for model collapse in high-dimensional regression, revealing modified scaling laws with crossover phenomena in both under- and over-parameterized regimes.\\\"\\n    relevance: \\\"Provides analytical collapse characterization. Our spectral metrics offer empirical detection aligned with their theory.\\\"\\n\\n  - bibtex_key: dohmatob2025strong\\n    title: \\\"Strong Model Collapse\\\"\\n    authors: \\\"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\\\"\\n    year: 2025\\n    venue: \\\"ICLR 2025\\\"\\n    arxiv_id: \\\"2410.04840\\\"\\n    doi: \\\"\\\"\\n    category: model_collapse_core\\n    verified: true\\n    abstract_short: \\\"Proves that even 1% synthetic data in training corpus leads to model collapse within scaling laws paradigm, using operator-valued free probability theory.\\\"\\n    relevance: \\\"Strongest theoretical result on collapse inevitability. Motivates need for early detection even with small synthetic contamination.\\\"\\n\\n  # ============================================================\\n  # Cluster 2: spectral_analysis_collapse (5 papers)\\n  # ============================================================\\n  - bibtex_key: gu2026sigma\\n    title: \\\"SIGMA: Scalable Spectral Insights for LLM Model Collapse\\\"\\n    authors: \\\"Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    arxiv_id: \\\"2601.03385\\\"\\n    doi: \\\"\\\"\\n    category: spectral_analysis_collapse\\n    verified: true\\n    abstract_short: \\\"Proposes SIGMA framework using spectral bounds of embedding Gram matrix to quantify model collapse, benchmarking on OPT-125M across recursive training generations.\\\"\\n    relevance: \\\"Most directly related work. Uses spectral analysis for collapse detection. Our contribution extends with EWS methodology and predictive capability.\\\"\\n\\n  - bibtex_key: naderi2025mindgap\\n    title: \\\"Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers\\\"\\n    authors: \\\"Naderi, Alireza and Nait Saada, Thiziri and Tanner, Jared\\\"\\n    year: 2025\\n    venue: \\\"ICML 2025\\\"\\n    arxiv_id: \\\"2410.07799\\\"\\n    doi: \\\"\\\"\\n    category: spectral_analysis_collapse\\n    verified: true\\n    abstract_short: \\\"Uses Random Matrix Theory to uncover spectral gap between largest singular values as cause of rank collapse in attention, proposing eigenvalue removal as mitigation.\\\"\\n    relevance: \\\"Provides spectral characterization of rank collapse in transformers. Our work applies similar spectral analysis to detect data-driven collapse.\\\"\\n\\n  - bibtex_key: he2025spectral\\n    title: \\\"Spectral Collapse Drives Loss of Plasticity in Deep Continual Learning\\\"\\n    authors: \\\"He, Naicheng and Guo, Kaicheng and Prakash, Arjun and Tiwari, Saket and Tao, Ruo Yu and Serapio, Tyrone and Greenwald, Amy and Konidaris, George\\\"\\n    year: 2025\\n    venue: \\\"NeurIPS 2025\\\"\\n    arxiv_id: \\\"2509.22335\\\"\\n    doi: \\\"\\\"\\n    category: spectral_analysis_collapse\\n    verified: true\\n    abstract_short: \\\"Shows Hessian spectral collapse at new-task initialization prevents learning, proposing effective rank regularization and L2 penalties to preserve plasticity.\\\"\\n    relevance: \\\"Demonstrates spectral collapse as mechanism for plasticity loss. Parallels our finding that spectral signatures predict collapse in recursive training.\\\"\\n\\n  - bibtex_key: roy2007effectiverank\\n    title: \\\"The Effective Rank: A Measure of Effective Dimensionality\\\"\\n    authors: \\\"Roy, Olivier and Vetterli, Martin\\\"\\n    year: 2007\\n    venue: \\\"EUSIPCO 2007\\\"\\n    arxiv_id: \\\"\\\"\\n    doi: \\\"\\\"\\n    category: spectral_analysis_collapse\\n    verified: true\\n    abstract_short: \\\"Defines effective rank as exponential of Shannon entropy of normalized singular value distribution, providing continuous measure of matrix dimensionality.\\\"\\n    relevance: \\\"Foundation metric for our EWS. We track effective rank decline of representation matrices as collapse indicator.\\\"\\n\\n  - bibtex_key: martin2021implicit\\n    title: \\\"Implicit Self-Regularization in Deep Neural Networks: Evidence from Random Matrix Theory and Implications for Learning\\\"\\n    authors: \\\"Martin, Charles H. and Mahoney, Michael W.\\\"\\n    year: 2021\\n    venue: \\\"JMLR\\\"\\n    arxiv_id: \\\"1810.01075\\\"\\n    doi: \\\"\\\"\\n    category: spectral_analysis_collapse\\n    verified: true\\n    abstract_short: \\\"Applies RMT to analyze weight matrix spectra in DNNs, identifying implicit self-regularization through heavy-tailed spectral distributions correlated with model quality.\\\"\\n    relevance: \\\"Establishes spectral analysis of weight matrices as diagnostic tool. Our approach extends to representation matrices under recursive training.\\\"\\n\\n  # ============================================================\\n  # Cluster 3: data_mixing_strategies (4 papers)\\n  # ============================================================\\n  - bibtex_key: xie2023doremi\\n    title: \\\"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\\\"\\n    authors: \\\"Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao and Lu, Yifeng and Liang, Percy and Le, Quoc V. and Ma, Tengyu and Yu, Adams Wei\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023\\\"\\n    arxiv_id: \\\"2305.10429\\\"\\n    doi: \\\"\\\"\\n    category: data_mixing_strategies\\n    verified: true\\n    abstract_short: \\\"Uses group DRO on proxy model to optimize domain mixture proportions, improving downstream accuracy by 6.5% and reaching baseline performance with 2.6x fewer steps.\\\"\\n    relevance: \\\"Establishes data mixing optimization. Our EWS can inform when to adjust mixing ratios during recursive training.\\\"\\n\\n  - bibtex_key: ye2025mixinglaws\\n    title: \\\"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\\\"\\n    authors: \\\"Ye, Jiasheng and Liu, Peiju and Sun, Tianxiang and Zhan, Jun and Zhou, Yunhua and Qiu, Xipeng\\\"\\n    year: 2025\\n    venue: \\\"ICLR 2025\\\"\\n    arxiv_id: \\\"2403.16952\\\"\\n    doi: \\\"\\\"\\n    category: data_mixing_strategies\\n    verified: true\\n    abstract_short: \\\"Discovers quantitative data mixing laws predicting model performance from mixture proportions, enabling optimization of 1B model training with 48% fewer steps.\\\"\\n    relevance: \\\"Provides predictive framework for data mixing. Our spectral EWS complements by detecting when current mixture causes collapse.\\\"\\n\\n  - bibtex_key: chen2025aioli\\n    title: \\\"Aioli: A Unified Optimization Framework for Language Model Data Mixing\\\"\\n    authors: \\\"Chen, Mayee F. and Hu, Michael Y. and Lourie, Nicholas and Cho, Kyunghyun and R\\\\\\\\'{e}, Christopher\\\"\\n    year: 2025\\n    venue: \\\"ICLR 2025\\\"\\n    arxiv_id: \\\"2411.05735\\\"\\n    doi: \\\"\\\"\\n    category: data_mixing_strategies\\n    verified: true\\n    abstract_short: \\\"Unifies existing data mixing methods into common optimization framework, proposing online method that dynamically estimates mixing law parameters during training.\\\"\\n    relevance: \\\"Online mixing adjustment mechanism. Our EWS provides signal for when to trigger mixture proportion updates.\\\"\\n\\n  - bibtex_key: kazdan2024collapsethrive\\n    title: \\\"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\\\"\\n    authors: \\\"Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David L. and Koyejo, Sanmi\\\"\\n    year: 2024\\n    venue: \\\"arXiv\\\"\\n    arxiv_id: \\\"2410.16713\\\"\\n    doi: \\\"\\\"\\n    category: data_mixing_strategies\\n    verified: true\\n    abstract_short: \\\"Studies three data workflows (replace/accumulate/fixed-compute) showing collapse only under replacement, with non-trivial real-synthetic data interactions.\\\"\\n    relevance: \\\"Characterizes when synthetic data helps vs. hurts. Our EWS enables real-time workflow selection based on spectral health.\\\"\\n\\n  # ============================================================\\n  # Cluster 4: synthetic_data_quality (3 papers)\\n  # ============================================================\\n  - bibtex_key: gudibande2024falsepromise\\n    title: \\\"The False Promise of Imitating Proprietary LLMs\\\"\\n    authors: \\\"Gudibande, Arnav and Wallace, Eric and Snell, Charlie and Geng, Xinyang and Liu, Hao and Abbeel, Pieter and Levine, Sergey and Song, Dawn\\\"\\n    year: 2024\\n    venue: \\\"ICLR 2024\\\"\\n    arxiv_id: \\\"2305.15717\\\"\\n    doi: \\\"\\\"\\n    category: synthetic_data_quality\\n    verified: true\\n    abstract_short: \\\"Shows imitation models trained on proprietary LLM outputs appear fluent but close little capability gap, revealing fundamental quality limitations of synthetic training data.\\\"\\n    relevance: \\\"Demonstrates quality degradation from synthetic imitation. Our spectral metrics can quantify this capability gap during training.\\\"\\n\\n  - bibtex_key: feng2024verification\\n    title: \\\"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification\\\"\\n    authors: \\\"Feng, Yunzhen and Dohmatob, Elvis and Yang, Pu and Charton, Francois and Kempe, Julia\\\"\\n    year: 2024\\n    venue: \\\"arXiv\\\"\\n    arxiv_id: \\\"2406.07515\\\"\\n    doi: \\\"\\\"\\n    category: synthetic_data_quality\\n    verified: true\\n    abstract_short: \\\"Shows that even imperfect verifiers can prevent model collapse when scaling with synthetic data, providing theoretical conditions for effective verification.\\\"\\n    relevance: \\\"Verification as collapse prevention. Our EWS serves as a verification signal indicating when synthetic data quality degrades.\\\"\\n\\n  - bibtex_key: keisha2025knowledge\\n    title: \\\"Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training\\\"\\n    authors: \\\"Keisha, Figarri and Wu, Zekun and Wang, Ze and Koshiyama, Adriano and Treleaven, Philip\\\"\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    arxiv_id: \\\"2509.04796\\\"\\n    doi: \\\"\\\"\\n    category: synthetic_data_quality\\n    verified: true\\n    abstract_short: \\\"Defines three-stage knowledge collapse where factual accuracy erodes while fluency persists, creating confidently wrong outputs under recursive synthetic training.\\\"\\n    relevance: \\\"Identifies knowledge collapse as distinct from perplexity collapse. Our spectral EWS may detect this before factual degradation manifests.\\\"\\n\\n  # ============================================================\\n  # Cluster 5: early_warning_signals (3 papers)\\n  # ============================================================\\n  - bibtex_key: scheffer2009ews\\n    title: \\\"Early-warning signals for critical transitions\\\"\\n    authors: \\\"Scheffer, Marten and Bascompte, Jordi and Brock, William A. and Brovkin, Victor and Carpenter, Stephen R. and Dakos, Vasilis and Held, Hermann and van Nes, Egbert H. and Rietkerk, Max and Sugihara, George\\\"\\n    year: 2009\\n    venue: \\\"Nature\\\"\\n    arxiv_id: \\\"\\\"\\n    doi: \\\"10.1038/nature08227\\\"\\n    category: early_warning_signals\\n    verified: true\\n    abstract_short: \\\"Proposes generic early warning signals (rising variance, autocorrelation, spectral reddening) indicating proximity to critical tipping points in complex systems.\\\"\\n    relevance: \\\"Foundational EWS theory. We adapt critical slowing down indicators to neural network representation space for collapse detection.\\\"\\n\\n  - bibtex_key: bury2021deeplearning\\n    title: \\\"Deep learning for early warning signals of tipping points\\\"\\n    authors: \\\"Bury, Thomas M. and Sujith, R. I. and Pavithran, Induja and Scheffer, Marten and Lenton, Timothy M. and Anand, Madhur and Bauch, Chris T.\\\"\\n    year: 2021\\n    venue: \\\"PNAS\\\"\\n    arxiv_id: \\\"\\\"\\n    doi: \\\"10.1073/pnas.2106140118\\\"\\n    category: early_warning_signals\\n    verified: true\\n    abstract_short: \\\"Develops deep learning algorithm for EWS that generalizes across systems, providing higher sensitivity and fewer false positives than generic statistical indicators.\\\"\\n    relevance: \\\"Demonstrates ML-based EWS for tipping points. Inspires our approach of learning spectral EWS patterns for model collapse detection.\\\"\\n\\n  - bibtex_key: dakos2012methods\\n    title: \\\"Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data\\\"\\n    authors: \\\"Dakos, Vasilis and Carpenter, Stephen R. and Brock, William A. and Ellison, Aaron M. and Guttal, Vishwesha and Ives, Anthony R. and Kefi, Saran and Livina, Vasilis and Seekell, David A. and van Nes, Egbert H. and Scheffer, Marten\\\"\\n    year: 2012\\n    venue: \\\"PLOS ONE\\\"\\n    arxiv_id: \\\"\\\"\\n    doi: \\\"10.1371/journal.pone.0041010\\\"\\n    category: early_warning_signals\\n    verified: true\\n    abstract_short: \\\"Comprehensive comparison of metric-based and model-based EWS methods for time series, providing practical toolbox for detecting approaching critical transitions.\\\"\\n    relevance: \\\"Methodological reference for EWS detection. We adapt their time-series indicators to spectral metric trajectories during training.\\\"\\n\\n  # ============================================================\\n  # Cluster 4 supplement: synthetic_data_quality (+1)\\n  # ============================================================\\n  - bibtex_key: briesch2023entropy\\n    title: \\\"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\\\"\\n    authors: \\\"Briesch, Martin and Sobania, Dominik and Rothlauf, Franz\\\"\\n    year: 2023\\n    venue: \\\"arXiv\\\"\\n    arxiv_id: \\\"2311.16822\\\"\\n    doi: \\\"\\\"\\n    category: synthetic_data_quality\\n    verified: true\\n    abstract_short: \\\"Analyzes self-consuming training loops in LLMs showing progressive quality degradation with reduced output diversity and increased repetition across generations.\\\"\\n    relevance: \\\"Provides complementary characterization of quality degradation in self-consuming loops. Our spectral metrics can quantify the diversity loss they observe.\\\"\\n\\n  # ============================================================\\n  # Infrastructure / Methodology\\n  # ============================================================\\n  - bibtex_key: biderman2023pythia\\n    title: \\\"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\\\"\\n    authors: \\\"Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and van der Wal, Oskar\\\"\\n    year: 2023\\n    venue: \\\"ICML 2023\\\"\\n    arxiv_id: \\\"2304.01373\\\"\\n    doi: \\\"\\\"\\n    category: methodology\\n    verified: true\\n    abstract_short: \\\"Introduces Pythia suite of 16 LLMs (70M-12B) trained on public data with consistent hyperparameters, enabling controlled scientific study of LLM training dynamics.\\\"\\n    relevance: \\\"Experimental platform. We use Pythia-410M and Pythia-1B for all recursive training experiments.\\\"\\n\", \"total_chars\": 17963, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "1a9d8255-476f-427c-8e4a-38d4a01b0c6c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/literature_map.yaml\\\", \\\"content\\\": \\\"papers:\\\\n  # ============================================================\\\\n  # Cluster 1: model_collapse_core (6 papers)\\\\n  # ============================================================\\\\n  - bibtex_key: shumailov2024collapse\\\\n    title: \\\\\\\"AI models collapse when trained on recursively generated data\\\\\\\"\\\\n    authors: \\\\\\\"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"Nature\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2305.17493\\\\\\\"\\\\n    doi: \\\\\\\"10.1038/s41586-024-07566-y\\\\\\\"\\\\n    category: model_collapse_core\\\\n    verified: true\\\\n    abstract_short: \\\\\\\"Shows that training on model-generated data causes irreversible defects where tails of the original content distribution disappear, leading to model collapse across LLMs, VAEs, and GMMs.\\\\\\\"\\\\n    relevance: \\\\\\\"Seminal paper defining model collapse. Our work provides spectral EWS to detect collapse onset before irreversible degradation.\\\\\\\"\\\\n\\\\n  - bibtex_key: dohmatob2024tails\\\\n    title: \\\\\\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\\\\\"\\\\n    authors: \\\\\\\"Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"ICML 2024\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2402.07043\\\\\\\"\\\\n    doi: \\\\\\\"\\\\\\\"\\\\n    category: model_collapse_core\\\\n    verified: true\\\\n    abstract_short: \\\\\\\"Provides first theoretical framework for model collapse through scaling laws, showing how tail distributions vanish across generations with validated experiments on transformers.\\\\\\\"\\\\n    relevance: \\\\\\\"Theoretical foundation for understanding collapse dynamics. Our spectral metrics connect to their scaling law framework.\\\\\\\"\\\\n\\\\n  - bibtex_key: alemohammad2024mad\\\\n    title: \\\\\\\"Self-Consuming Generative Models Go MAD\\\\\\\"\\\\n    authors: \\\\\\\"Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"ICLR 2024\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2307.01850\\\\\\\"\\\\n    doi: \\\\\\\"\\\\\\\"\\\\n    category: model_collapse_core\\\\n    verified: true\\\\n    abstract_short: \\\\\\\"Introduces Model Autophagy Disorder (MAD) showing that without fresh real data, autophagous loops cause progressive quality/diversity loss in just a few generations.\\\\\\\"\\\\n    relevance: \\\\\\\"Establishes MAD framework for self-consuming loops. Our EWS can detect MADness onset before quality degrades.\\\\\\\"\\\\n\\\\n  - bibtex_key: gerstgrasser2024inevitable\\\\n    title: \\\\\\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\\\\\"\\\\n    authors: \\\\\\\"Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2404.01413\\\\\\\"\\\\n    doi: \\\\\\\"\\\\\\\"\\\\n    category: model_collapse_core\\\\n    verified: true\\\\n    abstract_short: \\\\\\\"Shows that accumulating synthetic data alongside real data avoids model collapse, with finite upper bound on test error independent of iteration count.\\\\\\\"\\\\n    relevance: \\\\\\\"Key mitigation result. Our EWS enables knowing when to inject real data vs. when accumulation suffices.\\\\\\\"\\\\n\\\\n  - bibtex_key: dohmatob2024demystified\\\\n    title: \\\\\\\"Model Collapse Demystified: The Case of Regression\\\\\\\"\\\\n    authors: \\\\\\\"Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"NeurIPS 2024\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2402.07712\\\\\\\"\\\\n    doi: \\\\\\\"\\\\\\\"\\\\n    category: model_collapse_core\\\\n    verified: true\\\\n    abstract_short: \\\\\\\"Derives analytical formulas for model collapse in high-dimensional regression, revealing modified scaling laws with crossover phenomena in both under- and over-parameterized regimes.\\\\\\\"\\\\n    relevance: \\\\\\\"Provides analytical collapse characterization. Our spectral metrics offer empirical detection aligned with their theory.\\\\\\\"\\\\n\\\\n  - bibtex_key: dohmatob2025strong\\\\n    title: \\\\\\\"Strong Model Collapse\\\\\\\"\\\\n    authors: \\\\\\\"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"ICLR 2025\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2410.04840\\\\\\\"\\\\n    doi: \\\\\\\"\\\\\\\"\\\\n    category: model_collapse_core\\\\n    verified: true\\\\n    abstract_short: \\\\\\\"Proves that even 1% synthetic data in training corpus leads to model collapse within scaling laws paradigm, using operator-valued free probability theory.\\\\\\\"\\\\n    relevance: \\\\\\\"Strongest theoretical result on collapse inevitability. Motivates need for early detection even with small synthetic contamination.\\\\\\\"\\\\n\\\\n  # ============================================================\\\\n  # Cluster 2: spectral_analysis_collapse (5 papers)\\\\n  # ============================================================\\\\n  - bibtex_key: gu2026sigma\\\\n    title: \\\\\\\"SIGMA: Scalable Spectral Insights for LLM Model Collapse\\\\\\\"\\\\n    authors: \\\\\\\"Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2601.03385\\\\\\\"\\\\n    doi: \\\\\\\"\\\\\\\"\\\\n    category: spectral_analysis_collapse\\\\n    verified: true\\\\n    abstract_short: \\\\\\\"Proposes SIGMA framework using spectral bounds of embedding Gram matrix to quantify model collapse, benchmarking on OPT-125M across recursive training generations.\\\\\\\"\\\\n    relevance: \\\\\\\"Most directly related work. Uses spectral analysis for collapse detection. Our contribution extends with EWS methodology and predictive capability.\\\\\\\"\\\\n\\\\n  - bibtex_key: naderi2025mindgap\\\\n    title: \\\\\\\"Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers\\\\\\\"\\\\n    authors: \\\\\\\"Naderi, Alireza and Nait Saada, Thiziri and Tanner, Jared\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"ICML 2025\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2410.07799\\\\\\\"\\\\n    doi: \\\\\\\"\\\\\\\"\\\\n    category: spectral_analysis_collapse\\\\n    verified: true\\\\n    abstract_short: \\\\\\\"Uses Random Matrix Theory to uncover spectral gap between largest singular values as cause of rank collapse in attention, proposing eigenvalue removal as mitigation.\\\\\\\"\\\\n    relevance: \\\\\\\"Provides spectral characterization of rank collapse in transformers. Our work applies similar spectral analysis to detect data-driven collapse.\\\\\\\"\\\\n\\\\n  - bibtex_key: he2025spectral\\\\n    title: \\\\\\\"Spectral Collapse Drives Loss of Plasticity in Deep Continual Learning\\\\\\\"\\\\n    authors: \\\\\\\"He, Naicheng and Guo, Kaicheng and Prakash, Arjun and Tiwari, Saket and Tao, Ruo Yu and Serapio, Tyrone and Greenwald, Amy and Konidaris, George\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"NeurIPS 2025\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2509.22335\\\\\\\"\\\\n    doi: \\\\\\\"\\\\\\\"\\\\n    category: spectral_analysis_collapse\\\\n    verified: true\\\\n    abstract_short: \\\\\\\"Shows Hessian spectral collapse at new-task initialization prevents learning, proposing effective rank regularization and L2 penalties to preserve plasticity.\\\\\\\"\\\\n    relevance: \\\\\\\"Demonstrates spectral collapse as mechanism for plasticity loss. Parallels our finding that spectral signatures predict collapse in recursive training.\\\\\\\"\\\\n\\\\n  - bibtex_key: roy2007effectiverank\\\\n    title: \\\\\\\"The Effective Rank: A Measure of Effective Dimensionality\\\\\\\"\\\\n    authors: \\\\\\\"Roy, Olivier and Vetterli, Martin\\\\\\\"\\\\n    year: 2007\\\\n    venue: \\\\\\\"EUSIPCO 2007\\\\\\\"\\\\n    arxiv_id: \\\\\\\"\\\\\\\"\\\\n    doi: \\\\\\\"\\\\\\\"\\\\n    category: spectral_analysis_collapse\\\\n    verified: true\\\\n    abstract_short: \\\\\\\"Defines effective rank as exponential of Shannon entropy of normalized singular value distribution, providing continuous measure of matrix dimensionality.\\\\\\\"\\\\n    relevance: \\\\\\\"Foundation metric for our EWS. We track effective rank decline of representation matrices as collapse indicator.\\\\\\\"\\\\n\\\\n  - bibtex_key: martin2021implicit\\\\n    title: \\\\\\\"Implicit Self-Regularization in Deep Neural Networks: Evidence from Random Matrix Theory and Implications for Learning\\\\\\\"\\\\n    authors: \\\\\\\"Martin, Charles H. and Mahoney, Michael W.\\\\\\\"\\\\n    year: 2021\\\\n    venue: \\\\\\\"JMLR\\\\\\\"\\\\n    arxiv_id: \\\\\\\"1810.01075\\\\\\\"\\\\n    doi: \\\\\\\"\\\\\\\"\\\\n    category: spectral_analysis_collapse\\\\n    verified: true\\\\n    abstract_short: \\\\\\\"Applies RMT to analyze weight matrix spectra in DNNs, identifying implicit self-regularization through heavy-tailed spectral distributions correlated with model quality.\\\\\\\"\\\\n    relevance: \\\\\\\"Establishes spectral analysis of weight matrices as diagnostic tool. Our approach extends to representation matrices under recursive training.\\\\\\\"\\\\n\\\\n  # ============================================================\\\\n  # Cluster 3: data_mixing_strategies (4 papers)\\\\n  # ============================================================\\\\n  - bibtex_key: xie2023doremi\\\\n    title: \\\\\\\"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\\\\\\\"\\\\n    authors: \\\\\\\"Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao and Lu, Yifeng and Liang, Percy and Le, Quoc V. and Ma, Tengyu and Yu, Adams Wei\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"NeurIPS 2023\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2305.10429\\\\\\\"\\\\n    doi: \\\\\\\"\\\\\\\"\\\\n    category: data_mixing_strategies\\\\n    verified: true\\\\n    abstract_short: \\\\\\\"Uses group DRO on proxy model to optimize domain mixture proportions, improving downstream accuracy by 6.5% and reaching baseline performance with 2.6x fewer steps.\\\\\\\"\\\\n    relevance: \\\\\\\"Establishes data mixing optimization. Our EWS can inform when to adjust mixing ratios during recursive training.\\\\\\\"\\\\n\\\\n  - bibtex_key: ye2025mixinglaws\\\\n    title: \\\\\\\"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\\\\\\\"\\\\n    authors: \\\\\\\"Ye, Jiasheng and Liu, Peiju and Sun, Tianxiang and Zhan, Jun and Zhou, Yunhua and Qiu, Xipeng\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"ICLR 2025\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2403.16952\\\\\\\"\\\\n    doi: \\\\\\\"\\\\\\\"\\\\n    category: data_mixing_strategies\\\\n    verified: true\\\\n    abstract_short: \\\\\\\"Discovers quantitative data mixing laws predicting model performance from mixture proportions, enabling optimization of 1B model training with 48% fewer steps.\\\\\\\"\\\\n    relevance: \\\\\\\"Provides predictive framework for data mixing. Our spectral EWS complements by detecting when current mixture causes collapse.\\\\\\\"\\\\n\\\\n  - bibtex_key: chen2025aioli\\\\n    title: \\\\\\\"Aioli: A Unified Optimization Framework for Language Model Data Mixing\\\\\\\"\\\\n    authors: \\\\\\\"Chen, Mayee F. and Hu, Michael Y. and Lourie, Nicholas and Cho, Kyunghyun and R\\\\\\\\\\\\\\\\'{e}, Christopher\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"ICLR 2025\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2411.05735\\\\\\\"\\\\n    doi: \\\\\\\"\\\\\\\"\\\\n    category: data_mixing_strategies\\\\n    verified: true\\\\n    abstract_short: \\\\\\\"Unifies existing data mixing methods into common optimization framework, proposing online method that dynamically estimates mixing law parameters during training.\\\\\\\"\\\\n    relevance: \\\\\\\"Online mixing adjustment mechanism. Our EWS provides signal for when to trigger mixture proportion updates.\\\\\\\"\\\\n\\\\n  - bibtex_key: kazdan2024collapsethrive\\\\n    title: \\\\\\\"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\\\\\\\"\\\\n    authors: \\\\\\\"Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David L. and Koyejo, Sanmi\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2410.16713\\\\\\\"\\\\n    doi: \\\\\\\"\\\\\\\"\\\\n    category: data_mixing_strategies\\\\n    verified: true\\\\n    abstract_short: \\\\\\\"Studies three data workflows (replace/accumulate/fixed-compute) showing collapse only under replacement, with non-trivial real-synthetic data interactions.\\\\\\\"\\\\n    relevance: \\\\\\\"Characterizes when synthetic data helps vs. hurts. Our EWS enables real-time workflow selection based on spectral health.\\\\\\\"\\\\n\\\\n  # ============================================================\\\\n  # Cluster 4: synthetic_data_quality (3 papers)\\\\n  # ============================================================\\\\n  - bibtex_key: gudibande2024falsepromise\\\\n    title: \\\\\\\"The False Promise of Imitating Proprietary LLMs\\\\\\\"\\\\n    authors: \\\\\\\"Gudibande, Arnav and Wallace, Eric and Snell, Charlie and Geng, Xinyang and Liu, Hao and Abbeel, Pieter and Levine, Sergey and Song, Dawn\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"ICLR 2024\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2305.15717\\\\\\\"\\\\n    doi: \\\\\\\"\\\\\\\"\\\\n    category: synthetic_data_quality\\\\n    verified: true\\\\n    abstract_short: \\\\\\\"Shows imitation models trained on proprietary LLM outputs appear fluent but close little capability gap, revealing fundamental quality limitations of synthetic training data.\\\\\\\"\\\\n    relevance: \\\\\\\"Demonstrates quality degradation from synthetic imitation. Our spectral metrics can quantify this capability gap during training.\\\\\\\"\\\\n\\\\n  - bibtex_key: feng2024verification\\\\n    title: \\\\\\\"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification\\\\\\\"\\\\n    authors: \\\\\\\"Feng, Yunzhen and Dohmatob, Elvis and Yang, Pu and Charton, Francois and Kempe, Julia\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2406.07515\\\\\\\"\\\\n    doi: \\\\\\\"\\\\\\\"\\\\n    category: synthetic_data_quality\\\\n    verified: true\\\\n    abstract_short: \\\\\\\"Shows that even imperfect verifiers can prevent model collapse when scaling with synthetic data, providing theoretical conditions for effective verification.\\\\\\\"\\\\n    relevance: \\\\\\\"Verification as collapse prevention. Our EWS serves as a verification signal indicating when synthetic data quality degrades.\\\\\\\"\\\\n\\\\n  - bibtex_key: keisha2025knowledge\\\\n    title: \\\\\\\"Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training\\\\\\\"\\\\n    authors: \\\\\\\"Keisha, Figarri and Wu, Zekun and Wang, Ze and Koshiyama, Adriano and Treleaven, Philip\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2509.04796\\\\\\\"\\\\n    doi: \\\\\\\"\\\\\\\"\\\\n    category: synthetic_data_quality\\\\n    verified: true\\\\n    abstract_short: \\\\\\\"Defines three-stage knowledge collapse where factual accuracy erodes while fluency persists, creating confidently wrong outputs under recursive synthetic training.\\\\\\\"\\\\n    relevance: \\\\\\\"Identifies knowledge collapse as distinct from perplexity collapse. Our spectral EWS may detect this before factual degradation manifests.\\\\\\\"\\\\n\\\\n  # ============================================================\\\\n  # Cluster 5: early_warning_signals (3 papers)\\\\n  # ============================================================\\\\n  - bibtex_key: scheffer2009ews\\\\n    title: \\\\\\\"Early-warning signals for critical transitions\\\\\\\"\\\\n    authors: \\\\\\\"Scheffer, Marten and Bascompte, Jordi and Brock, William A. and Brovkin, Victor and Carpenter, Stephen R. and Dakos, Vasilis and Held, Hermann and van Nes, Egbert H. and Rietkerk, Max and Sugihara, George\\\\\\\"\\\\n    year: 2009\\\\n    venue: \\\\\\\"Nature\\\\\\\"\\\\n    arxiv_id: \\\\\\\"\\\\\\\"\\\\n    doi: \\\\\\\"10.1038/nature08227\\\\\\\"\\\\n    category: early_warning_signals\\\\n    verified: true\\\\n    abstract_short: \\\\\\\"Proposes generic early warning signals (rising variance, autocorrelation, spectral reddening) indicating proximity to critical tipping points in complex systems.\\\\\\\"\\\\n    relevance: \\\\\\\"Foundational EWS theory. We adapt critical slowing down indicators to neural network representation space for collapse detection.\\\\\\\"\\\\n\\\\n  - bibtex_key: bury2021deeplearning\\\\n    title: \\\\\\\"Deep learning for early warning signals of tipping points\\\\\\\"\\\\n    authors: \\\\\\\"Bury, Thomas M. and Sujith, R. I. and Pavithran, Induja and Scheffer, Marten and Lenton, Timothy M. and Anand, Madhur and Bauch, Chris T.\\\\\\\"\\\\n    year: 2021\\\\n    venue: \\\\\\\"PNAS\\\\\\\"\\\\n    arxiv_id: \\\\\\\"\\\\\\\"\\\\n    doi: \\\\\\\"10.1073/pnas.2106140118\\\\\\\"\\\\n    category: early_warning_signals\\\\n    verified: true\\\\n    abstract_short: \\\\\\\"Develops deep learning algorithm for EWS that generalizes across systems, providing higher sensitivity and fewer false positives than generic statistical indicators.\\\\\\\"\\\\n    relevance: \\\\\\\"Demonstrates ML-based EWS for tipping points. Inspires our approach of learning spectral EWS patterns for model collapse detection.\\\\\\\"\\\\n\\\\n  - bibtex_key: dakos2012methods\\\\n    title: \\\\\\\"Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data\\\\\\\"\\\\n    authors: \\\\\\\"Dakos, Vasilis and Carpenter, Stephen R. and Brock, William A. and Ellison, Aaron M. and Guttal, Vishwesha and Ives, Anthony R. and Kefi, Saran and Livina, Vasilis and Seekell, David A. and van Nes, Egbert H. and Scheffer, Marten\\\\\\\"\\\\n    year: 2012\\\\n    venue: \\\\\\\"PLOS ONE\\\\\\\"\\\\n    arxiv_id: \\\\\\\"\\\\\\\"\\\\n    doi: \\\\\\\"10.1371/journal.pone.0041010\\\\\\\"\\\\n    category: early_warning_signals\\\\n    verified: true\\\\n    abstract_short: \\\\\\\"Comprehensive comparison of metric-based and model-based EWS methods for time series, providing practical toolbox for detecting approaching critical transitions.\\\\\\\"\\\\n    relevance: \\\\\\\"Methodological reference for EWS detection. We adapt their time-series indicators to spectral metric trajectories during training.\\\\\\\"\\\\n\\\\n  # ============================================================\\\\n  # Cluster 4 supplement: synthetic_data_quality (+1)\\\\n  # ============================================================\\\\n  - bibtex_key: briesch2023entropy\\\\n    title: \\\\\\\"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\\\\\\\"\\\\n    authors: \\\\\\\"Briesch, Martin and Sobania, Dominik and Rothlauf, Franz\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2311.16822\\\\\\\"\\\\n    doi: \\\\\\\"\\\\\\\"\\\\n    category: synthetic_data_quality\\\\n    verified: true\\\\n    abstract_short: \\\\\\\"Analyzes self-consuming training loops in LLMs showing progressive quality degradation with reduced output diversity and increased repetition across generations.\\\\\\\"\\\\n    relevance: \\\\\\\"Provides complementary characterization of quality degradation in self-consuming loops. Our spectral metrics can quantify the diversity loss they observe.\\\\\\\"\\\\n\\\\n  # ============================================================\\\\n  # Infrastructure / Methodology\\\\n  # ============================================================\\\\n  - bibtex_key: biderman2023pythia\\\\n    title: \\\\\\\"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\\\\\\\"\\\\n    authors: \\\\\\\"Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and van der Wal, Oskar\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"ICML 2023\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2304.01373\\\\\\\"\\\\n    doi: \\\\\\\"\\\\\\\"\\\\n    category: methodology\\\\n    verified: true\\\\n    abstract_short: \\\\\\\"Introduces Pythia suite of 16 LLMs (70M-12B) trained on public data with consistent hyperparameters, enabling controlled scientific study of LLM training dynamics.\\\\\\\"\\\\n    relevance: \\\\\\\"Experimental platform. We use Pythia-410M and Pythia-1B for all recursive training experiments.\\\\\\\"\\\\n\\\", \\\"total_chars\\\": 17963, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/literature_map.yaml\", \"content\": \"papers:\\n  # ============================================================\\n  # Cluster 1: model_collapse_core (6 papers)\\n  # ============================================================\\n  - bibtex_key: shumailov2024collapse\\n    title: \\\"AI models collapse when trained on recursively generated data\\\"\\n    authors: \\\"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin\\\"\\n    year: 2024\\n    venue: \\\"Nature\\\"\\n    arxiv_id: \\\"2305.17493\\\"\\n    doi: \\\"10.1038/s41586-024-07566-y\\\"\\n    category: model_collapse_core\\n    verified: true\\n    abstract_short: \\\"Shows that training on model-generated data causes irreversible defects where tails of the original content distribution disappear, leading to model collapse across LLMs, VAEs, and GMMs.\\\"\\n    relevance: \\\"Seminal paper defining model collapse. Our work provides spectral EWS to detect collapse onset before irreversible degradation.\\\"\\n\\n  - bibtex_key: dohmatob2024tails\\n    title: \\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\"\\n    authors: \\\"Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia\\\"\\n    year: 2024\\n    venue: \\\"ICML 2024\\\"\\n    arxiv_id: \\\"2402.07043\\\"\\n    doi: \\\"\\\"\\n    category: model_collapse_core\\n    verified: true\\n    abstract_short: \\\"Provides first theoretical framework for model collapse through scaling laws, showing how tail distributions vanish across generations with validated experiments on transformers.\\\"\\n    relevance: \\\"Theoretical foundation for understanding collapse dynamics. Our spectral metrics connect to their scaling law framework.\\\"\\n\\n  - bibtex_key: alemohammad2024mad\\n    title: \\\"Self-Consuming Generative Models Go MAD\\\"\\n    authors: \\\"Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.\\\"\\n    year: 2024\\n    venue: \\\"ICLR 2024\\\"\\n    arxiv_id: \\\"2307.01850\\\"\\n    doi: \\\"\\\"\\n    category: model_collapse_core\\n    verified: true\\n    abstract_short: \\\"Introduces Model Autophagy Disorder (MAD) showing that without fresh real data, autophagous loops cause progressive quality/diversity loss in just a few generations.\\\"\\n    relevance: \\\"Establishes MAD framework for self-consuming loops. Our EWS can detect MADness onset before quality degrades.\\\"\\n\\n  - bibtex_key: gerstgrasser2024inevitable\\n    title: \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\"\\n    authors: \\\"Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi\\\"\\n    year: 2024\\n    venue: \\\"arXiv\\\"\\n    arxiv_id: \\\"2404.01413\\\"\\n    doi: \\\"\\\"\\n    category: model_collapse_core\\n    verified: true\\n    abstract_short: \\\"Shows that accumulating synthetic data alongside real data avoids model collapse, with finite upper bound on test error independent of iteration count.\\\"\\n    relevance: \\\"Key mitigation result. Our EWS enables knowing when to inject real data vs. when accumulation suffices.\\\"\\n\\n  - bibtex_key: dohmatob2024demystified\\n    title: \\\"Model Collapse Demystified: The Case of Regression\\\"\\n    authors: \\\"Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS 2024\\\"\\n    arxiv_id: \\\"2402.07712\\\"\\n    doi: \\\"\\\"\\n    category: model_collapse_core\\n    verified: true\\n    abstract_short: \\\"Derives analytical formulas for model collapse in high-dimensional regression, revealing modified scaling laws with crossover phenomena in both under- and over-parameterized regimes.\\\"\\n    relevance: \\\"Provides analytical collapse characterization. Our spectral metrics offer empirical detection aligned with their theory.\\\"\\n\\n  - bibtex_key: dohmatob2025strong\\n    title: \\\"Strong Model Collapse\\\"\\n    authors: \\\"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\\\"\\n    year: 2025\\n    venue: \\\"ICLR 2025\\\"\\n    arxiv_id: \\\"2410.04840\\\"\\n    doi: \\\"\\\"\\n    category: model_collapse_core\\n    verified: true\\n    abstract_short: \\\"Proves that even 1% synthetic data in training corpus leads to model collapse within scaling laws paradigm, using operator-valued free probability theory.\\\"\\n    relevance: \\\"Strongest theoretical result on collapse inevitability. Motivates need for early detection even with small synthetic contamination.\\\"\\n\\n  # ============================================================\\n  # Cluster 2: spectral_analysis_collapse (5 papers)\\n  # ============================================================\\n  - bibtex_key: gu2026sigma\\n    title: \\\"SIGMA: Scalable Spectral Insights for LLM Model Collapse\\\"\\n    authors: \\\"Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    arxiv_id: \\\"2601.03385\\\"\\n    doi: \\\"\\\"\\n    category: spectral_analysis_collapse\\n    verified: true\\n    abstract_short: \\\"Proposes SIGMA framework using spectral bounds of embedding Gram matrix to quantify model collapse, benchmarking on OPT-125M across recursive training generations.\\\"\\n    relevance: \\\"Most directly related work. Uses spectral analysis for collapse detection. Our contribution extends with EWS methodology and predictive capability.\\\"\\n\\n  - bibtex_key: naderi2025mindgap\\n    title: \\\"Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers\\\"\\n    authors: \\\"Naderi, Alireza and Nait Saada, Thiziri and Tanner, Jared\\\"\\n    year: 2025\\n    venue: \\\"ICML 2025\\\"\\n    arxiv_id: \\\"2410.07799\\\"\\n    doi: \\\"\\\"\\n    category: spectral_analysis_collapse\\n    verified: true\\n    abstract_short: \\\"Uses Random Matrix Theory to uncover spectral gap between largest singular values as cause of rank collapse in attention, proposing eigenvalue removal as mitigation.\\\"\\n    relevance: \\\"Provides spectral characterization of rank collapse in transformers. Our work applies similar spectral analysis to detect data-driven collapse.\\\"\\n\\n  - bibtex_key: he2025spectral\\n    title: \\\"Spectral Collapse Drives Loss of Plasticity in Deep Continual Learning\\\"\\n    authors: \\\"He, Naicheng and Guo, Kaicheng and Prakash, Arjun and Tiwari, Saket and Tao, Ruo Yu and Serapio, Tyrone and Greenwald, Amy and Konidaris, George\\\"\\n    year: 2025\\n    venue: \\\"NeurIPS 2025\\\"\\n    arxiv_id: \\\"2509.22335\\\"\\n    doi: \\\"\\\"\\n    category: spectral_analysis_collapse\\n    verified: true\\n    abstract_short: \\\"Shows Hessian spectral collapse at new-task initialization prevents learning, proposing effective rank regularization and L2 penalties to preserve plasticity.\\\"\\n    relevance: \\\"Demonstrates spectral collapse as mechanism for plasticity loss. Parallels our finding that spectral signatures predict collapse in recursive training.\\\"\\n\\n  - bibtex_key: roy2007effectiverank\\n    title: \\\"The Effective Rank: A Measure of Effective Dimensionality\\\"\\n    authors: \\\"Roy, Olivier and Vetterli, Martin\\\"\\n    year: 2007\\n    venue: \\\"EUSIPCO 2007\\\"\\n    arxiv_id: \\\"\\\"\\n    doi: \\\"\\\"\\n    category: spectral_analysis_collapse\\n    verified: true\\n    abstract_short: \\\"Defines effective rank as exponential of Shannon entropy of normalized singular value distribution, providing continuous measure of matrix dimensionality.\\\"\\n    relevance: \\\"Foundation metric for our EWS. We track effective rank decline of representation matrices as collapse indicator.\\\"\\n\\n  - bibtex_key: martin2021implicit\\n    title: \\\"Implicit Self-Regularization in Deep Neural Networks: Evidence from Random Matrix Theory and Implications for Learning\\\"\\n    authors: \\\"Martin, Charles H. and Mahoney, Michael W.\\\"\\n    year: 2021\\n    venue: \\\"JMLR\\\"\\n    arxiv_id: \\\"1810.01075\\\"\\n    doi: \\\"\\\"\\n    category: spectral_analysis_collapse\\n    verified: true\\n    abstract_short: \\\"Applies RMT to analyze weight matrix spectra in DNNs, identifying implicit self-regularization through heavy-tailed spectral distributions correlated with model quality.\\\"\\n    relevance: \\\"Establishes spectral analysis of weight matrices as diagnostic tool. Our approach extends to representation matrices under recursive training.\\\"\\n\\n  # ============================================================\\n  # Cluster 3: data_mixing_strategies (4 papers)\\n  # ============================================================\\n  - bibtex_key: xie2023doremi\\n    title: \\\"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\\\"\\n    authors: \\\"Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao and Lu, Yifeng and Liang, Percy and Le, Quoc V. and Ma, Tengyu and Yu, Adams Wei\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023\\\"\\n    arxiv_id: \\\"2305.10429\\\"\\n    doi: \\\"\\\"\\n    category: data_mixing_strategies\\n    verified: true\\n    abstract_short: \\\"Uses group DRO on proxy model to optimize domain mixture proportions, improving downstream accuracy by 6.5% and reaching baseline performance with 2.6x fewer steps.\\\"\\n    relevance: \\\"Establishes data mixing optimization. Our EWS can inform when to adjust mixing ratios during recursive training.\\\"\\n\\n  - bibtex_key: ye2025mixinglaws\\n    title: \\\"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\\\"\\n    authors: \\\"Ye, Jiasheng and Liu, Peiju and Sun, Tianxiang and Zhan, Jun and Zhou, Yunhua and Qiu, Xipeng\\\"\\n    year: 2025\\n    venue: \\\"ICLR 2025\\\"\\n    arxiv_id: \\\"2403.16952\\\"\\n    doi: \\\"\\\"\\n    category: data_mixing_strategies\\n    verified: true\\n    abstract_short: \\\"Discovers quantitative data mixing laws predicting model performance from mixture proportions, enabling optimization of 1B model training with 48% fewer steps.\\\"\\n    relevance: \\\"Provides predictive framework for data mixing. Our spectral EWS complements by detecting when current mixture causes collapse.\\\"\\n\\n  - bibtex_key: chen2025aioli\\n    title: \\\"Aioli: A Unified Optimization Framework for Language Model Data Mixing\\\"\\n    authors: \\\"Chen, Mayee F. and Hu, Michael Y. and Lourie, Nicholas and Cho, Kyunghyun and R\\\\\\\\'{e}, Christopher\\\"\\n    year: 2025\\n    venue: \\\"ICLR 2025\\\"\\n    arxiv_id: \\\"2411.05735\\\"\\n    doi: \\\"\\\"\\n    category: data_mixing_strategies\\n    verified: true\\n    abstract_short: \\\"Unifies existing data mixing methods into common optimization framework, proposing online method that dynamically estimates mixing law parameters during training.\\\"\\n    relevance: \\\"Online mixing adjustment mechanism. Our EWS provides signal for when to trigger mixture proportion updates.\\\"\\n\\n  - bibtex_key: kazdan2024collapsethrive\\n    title: \\\"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\\\"\\n    authors: \\\"Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David L. and Koyejo, Sanmi\\\"\\n    year: 2024\\n    venue: \\\"arXiv\\\"\\n    arxiv_id: \\\"2410.16713\\\"\\n    doi: \\\"\\\"\\n    category: data_mixing_strategies\\n    verified: true\\n    abstract_short: \\\"Studies three data workflows (replace/accumulate/fixed-compute) showing collapse only under replacement, with non-trivial real-synthetic data interactions.\\\"\\n    relevance: \\\"Characterizes when synthetic data helps vs. hurts. Our EWS enables real-time workflow selection based on spectral health.\\\"\\n\\n  # ============================================================\\n  # Cluster 4: synthetic_data_quality (3 papers)\\n  # ============================================================\\n  - bibtex_key: gudibande2024falsepromise\\n    title: \\\"The False Promise of Imitating Proprietary LLMs\\\"\\n    authors: \\\"Gudibande, Arnav and Wallace, Eric and Snell, Charlie and Geng, Xinyang and Liu, Hao and Abbeel, Pieter and Levine, Sergey and Song, Dawn\\\"\\n    year: 2024\\n    venue: \\\"ICLR 2024\\\"\\n    arxiv_id: \\\"2305.15717\\\"\\n    doi: \\\"\\\"\\n    category: synthetic_data_quality\\n    verified: true\\n    abstract_short: \\\"Shows imitation models trained on proprietary LLM outputs appear fluent but close little capability gap, revealing fundamental quality limitations of synthetic training data.\\\"\\n    relevance: \\\"Demonstrates quality degradation from synthetic imitation. Our spectral metrics can quantify this capability gap during training.\\\"\\n\\n  - bibtex_key: feng2024verification\\n    title: \\\"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification\\\"\\n    authors: \\\"Feng, Yunzhen and Dohmatob, Elvis and Yang, Pu and Charton, Francois and Kempe, Julia\\\"\\n    year: 2024\\n    venue: \\\"arXiv\\\"\\n    arxiv_id: \\\"2406.07515\\\"\\n    doi: \\\"\\\"\\n    category: synthetic_data_quality\\n    verified: true\\n    abstract_short: \\\"Shows that even imperfect verifiers can prevent model collapse when scaling with synthetic data, providing theoretical conditions for effective verification.\\\"\\n    relevance: \\\"Verification as collapse prevention. Our EWS serves as a verification signal indicating when synthetic data quality degrades.\\\"\\n\\n  - bibtex_key: keisha2025knowledge\\n    title: \\\"Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training\\\"\\n    authors: \\\"Keisha, Figarri and Wu, Zekun and Wang, Ze and Koshiyama, Adriano and Treleaven, Philip\\\"\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    arxiv_id: \\\"2509.04796\\\"\\n    doi: \\\"\\\"\\n    category: synthetic_data_quality\\n    verified: true\\n    abstract_short: \\\"Defines three-stage knowledge collapse where factual accuracy erodes while fluency persists, creating confidently wrong outputs under recursive synthetic training.\\\"\\n    relevance: \\\"Identifies knowledge collapse as distinct from perplexity collapse. Our spectral EWS may detect this before factual degradation manifests.\\\"\\n\\n  # ============================================================\\n  # Cluster 5: early_warning_signals (3 papers)\\n  # ============================================================\\n  - bibtex_key: scheffer2009ews\\n    title: \\\"Early-warning signals for critical transitions\\\"\\n    authors: \\\"Scheffer, Marten and Bascompte, Jordi and Brock, William A. and Brovkin, Victor and Carpenter, Stephen R. and Dakos, Vasilis and Held, Hermann and van Nes, Egbert H. and Rietkerk, Max and Sugihara, George\\\"\\n    year: 2009\\n    venue: \\\"Nature\\\"\\n    arxiv_id: \\\"\\\"\\n    doi: \\\"10.1038/nature08227\\\"\\n    category: early_warning_signals\\n    verified: true\\n    abstract_short: \\\"Proposes generic early warning signals (rising variance, autocorrelation, spectral reddening) indicating proximity to critical tipping points in complex systems.\\\"\\n    relevance: \\\"Foundational EWS theory. We adapt critical slowing down indicators to neural network representation space for collapse detection.\\\"\\n\\n  - bibtex_key: bury2021deeplearning\\n    title: \\\"Deep learning for early warning signals of tipping points\\\"\\n    authors: \\\"Bury, Thomas M. and Sujith, R. I. and Pavithran, Induja and Scheffer, Marten and Lenton, Timothy M. and Anand, Madhur and Bauch, Chris T.\\\"\\n    year: 2021\\n    venue: \\\"PNAS\\\"\\n    arxiv_id: \\\"\\\"\\n    doi: \\\"10.1073/pnas.2106140118\\\"\\n    category: early_warning_signals\\n    verified: true\\n    abstract_short: \\\"Develops deep learning algorithm for EWS that generalizes across systems, providing higher sensitivity and fewer false positives than generic statistical indicators.\\\"\\n    relevance: \\\"Demonstrates ML-based EWS for tipping points. Inspires our approach of learning spectral EWS patterns for model collapse detection.\\\"\\n\\n  - bibtex_key: dakos2012methods\\n    title: \\\"Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data\\\"\\n    authors: \\\"Dakos, Vasilis and Carpenter, Stephen R. and Brock, William A. and Ellison, Aaron M. and Guttal, Vishwesha and Ives, Anthony R. and Kefi, Saran and Livina, Vasilis and Seekell, David A. and van Nes, Egbert H. and Scheffer, Marten\\\"\\n    year: 2012\\n    venue: \\\"PLOS ONE\\\"\\n    arxiv_id: \\\"\\\"\\n    doi: \\\"10.1371/journal.pone.0041010\\\"\\n    category: early_warning_signals\\n    verified: true\\n    abstract_short: \\\"Comprehensive comparison of metric-based and model-based EWS methods for time series, providing practical toolbox for detecting approaching critical transitions.\\\"\\n    relevance: \\\"Methodological reference for EWS detection. We adapt their time-series indicators to spectral metric trajectories during training.\\\"\\n\\n  # ============================================================\\n  # Cluster 4 supplement: synthetic_data_quality (+1)\\n  # ============================================================\\n  - bibtex_key: briesch2023entropy\\n    title: \\\"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\\\"\\n    authors: \\\"Briesch, Martin and Sobania, Dominik and Rothlauf, Franz\\\"\\n    year: 2023\\n    venue: \\\"arXiv\\\"\\n    arxiv_id: \\\"2311.16822\\\"\\n    doi: \\\"\\\"\\n    category: synthetic_data_quality\\n    verified: true\\n    abstract_short: \\\"Analyzes self-consuming training loops in LLMs showing progressive quality degradation with reduced output diversity and increased repetition across generations.\\\"\\n    relevance: \\\"Provides complementary characterization of quality degradation in self-consuming loops. Our spectral metrics can quantify the diversity loss they observe.\\\"\\n\\n  # ============================================================\\n  # Infrastructure / Methodology\\n  # ============================================================\\n  - bibtex_key: biderman2023pythia\\n    title: \\\"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\\\"\\n    authors: \\\"Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and van der Wal, Oskar\\\"\\n    year: 2023\\n    venue: \\\"ICML 2023\\\"\\n    arxiv_id: \\\"2304.01373\\\"\\n    doi: \\\"\\\"\\n    category: methodology\\n    verified: true\\n    abstract_short: \\\"Introduces Pythia suite of 16 LLMs (70M-12B) trained on public data with consistent hyperparameters, enabling controlled scientific study of LLM training dynamics.\\\"\\n    relevance: \\\"Experimental platform. We use Pythia-410M and Pythia-1B for all recursive training experiments.\\\"\\n\", \"total_chars\": 17963, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FmKM6GmWum8df47PvxiaFU`</summary>

```json
{
  "query": "model collapse diversity loss spectral metrics divergence synthetic data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "e34615e3-bed9-4e23-8017-136c0a7fd5e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrWpFQEKztUQ57uriheGHV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1060,
      "cache_read_input_tokens": 25006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1060
      },
      "output_tokens": 70,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_016nbdXLgd8bhcSku9jfrYma`</summary>

```json
{
  "query": "effective rank diversity metrics divergence language model collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "0ad3c2b3-40f3-49cb-87e2-bee84e13bb01",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrWpFQEKztUQ57uriheGHV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1060,
      "cache_read_input_tokens": 25006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1060
      },
      "output_tokens": 70,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M3iir8C9tTMpCmAB1QyvcJ`</summary>

```json
{
  "query": "n-gram diversity model collapse recursive training synthetic data generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "72ffe5b5-dceb-4c34-ad41-8295a0aa7297",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrWpFQEKztUQ57uriheGHV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1060,
      "cache_read_input_tokens": 25006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1060
      },
      "output_tokens": 70,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U9ByiPRyLQ3rni8JhDRwAj`</summary>

```json
{
  "query": "spectral metrics limitations language model quality diversity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "95bdbd95-71f1-4401-9ade-a74f3430f49e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrWpFQEKztUQ57uriheGHV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1060,
      "cache_read_input_tokens": 25006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1060
      },
      "output_tokens": 70,
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

_source line 14 · 2026-05-18T10:22:35.649Z_

<details><summary>↩ Tool result · `toolu_01U9ByiPRyLQ3rni8JhDRwAj`</summary>

```text
Web search results for query: "spectral metrics limitations language model quality diversity"

Links: [{"title":"Benchmarking Linguistic Diversity of Large Language Models | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.47/134150/Benchmarking-Linguistic-Diversity-of-Large"},{"title":"An overview of model uncertainty and variability in LLM-based sentiment analysis: challenges, mitigation strategies, and the role of explainability - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12375657/"},{"title":"Surveying the Effects of Quality, Diversity, and Complexity in Synthetic Data From Large Language Models","url":"https://arxiv.org/html/2412.02980v2"},{"title":"Large Language Models as Spectrographic Assistants: Opportunities and Challenges in Laboratory Data Analysis","url":"https://www.sciopen.com/article/10.26599/ECS.2025.9600002"},{"title":"Evaluating the Diversity and Quality of LLM Generated Content","url":"https://arxiv.org/html/2504.12522v1"},{"title":"What are some of the current challenges and limitations of language modeling benchmarks?","url":"https://www.linkedin.com/advice/1/what-some-current-challenges-limitations-language"},{"title":"Evaluating the Evaluation of Diversity in Natural Language ...","url":"https://aclanthology.org/2021.eacl-main.25.pdf"},{"title":"Large Language Model Evaluation in '26: 10+ Metrics & Methods","url":"https://research.aimultiple.com/large-language-model-evaluation/"},{"title":"Benchmarking Linguistic Diversity of Large Language Models","url":"https://arxiv.org/html/2412.10271v1"},{"title":"LLM Evaluation: 15 Metrics You Need to Know","url":"https://arya.ai/blog/llm-evaluation-metrics"}]

Based on the search results, here are the key findings about spectral metrics limitations, language model quality, and diversity:

## Key Limitations of Diversity Metrics for Language Models

Quality metrics may have limitations in recognizing the value of syntactic variation, particularly in summarization, automatic story generation, and next utterance generation tasks.

Models used for evaluating diversity like Sentence-BERT are generally trained and evaluated on human text; however, for diversity they're expected to generalize to the most diverse sets of LLM-generated text which may be off-distribution.

## Inconsistent Relationships Between Quality and Diversity

The research reveals complex relationships between quality and diversity metrics:

Results show a positive correlation between quality and lexical as well as semantic diversity in model outputs, while syntactic diversity often exhibits negative correlations, where higher syntactic diversity is associated with lower quality scores.

## General Evaluation Limitations

The evaluation techniques used for LLMs today frequently do not capture the whole range of output diversity and innovation, as traditional metrics emphasizing accuracy and relevance sometimes overlook the crucial significance of producing diverse and creative replies.

While measures of diversity using latent space embeddings do not require domain knowledge, for more domain-specific or complex tasks embeddings may fail to capture certain attribute-based features essential to comparing samples, which may result in weaker correlation with downstream metrics.

These findings highlight the importance of using multiple complementary metrics rather than relying on single diversity or quality measures when evaluating language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "a736cb08-858a-404a-83bf-857425a22cbb",
  "tool_use_result": {
    "query": "spectral metrics limitations language model quality diversity",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FuwjyLeHQKiprUBbX22e38",
        "content": [
          {
            "title": "Benchmarking Linguistic Diversity of Large Language Models | Transactions of the Association for Computational Linguistics | MIT Press",
            "url": "https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.47/134150/Benchmarking-Linguistic-Diversity-of-Large"
          },
          {
            "title": "An overview of model uncertainty and variability in LLM-based sentiment analysis: challenges, mitigation strategies, and the role of explainability - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12375657/"
          },
          {
            "title": "Surveying the Effects of Quality, Diversity, and Complexity in Synthetic Data From Large Language Models",
            "url": "https://arxiv.org/html/2412.02980v2"
          },
          {
            "title": "Large Language Models as Spectrographic Assistants: Opportunities and Challenges in Laboratory Data Analysis",
            "url": "https://www.sciopen.com/article/10.26599/ECS.2025.9600002"
          },
          {
            "title": "Evaluating the Diversity and Quality of LLM Generated Content",
            "url": "https://arxiv.org/html/2504.12522v1"
          },
          {
            "title": "What are some of the current challenges and limitations of language modeling benchmarks?",
            "url": "https://www.linkedin.com/advice/1/what-some-current-challenges-limitations-language"
          },
          {
            "title": "Evaluating the Evaluation of Diversity in Natural Language ...",
            "url": "https://aclanthology.org/2021.eacl-main.25.pdf"
          },
          {
            "title": "Large Language Model Evaluation in '26: 10+ Metrics & Methods",
            "url": "https://research.aimultiple.com/large-language-model-evaluation/"
          },
          {
            "title": "Benchmarking Linguistic Diversity of Large Language Models",
            "url": "https://arxiv.org/html/2412.10271v1"
          },
          {
            "title": "LLM Evaluation: 15 Metrics You Need to Know",
            "url": "https://arya.ai/blog/llm-evaluation-metrics"
          }
        ]
      },
      "Based on the search results, here are the key findings about spectral metrics limitations, language model quality, and diversity:\n\n## Key Limitations of Diversity Metrics for Language Models\n\nQuality metrics may have limitations in recognizing the value of syntactic variation, particularly in summarization, automatic story generation, and next utterance generation tasks.\n\nModels used for evaluating diversity like Sentence-BERT are generally trained and evaluated on human text; however, for diversity they're expected to generalize to the most diverse sets of LLM-generated text which may be off-distribution.\n\n## Inconsistent Relationships Between Quality and Diversity\n\nThe research reveals complex relationships between quality and diversity metrics:\n\nResults show a positive correlation between quality and lexical as well as semantic diversity in model outputs, while syntactic diversity often exhibits negative correlations, where higher syntactic diversity is associated with lower quality scores.\n\n## General Evaluation Limitations\n\nThe evaluation techniques used for LLMs today frequently do not capture the whole range of output diversity and innovation, as traditional metrics emphasizing accuracy and relevance sometimes overlook the crucial significance of producing diverse and creative replies.\n\nWhile measures of diversity using latent space embeddings do not require domain knowledge, for more domain-specific or complex tasks embeddings may fail to capture certain attribute-based features essential to comparing samples, which may result in weaker correlation with downstream metrics.\n\nThese findings highlight the importance of using multiple complementary metrics rather than relying on single diversity or quality measures when evaluating language models."
    ],
    "durationSeconds": 6.867142177000002
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-18T10:22:35.660Z_

<details><summary>↩ Tool result · `toolu_01M3iir8C9tTMpCmAB1QyvcJ`</summary>

```text
Web search results for query: "n-gram diversity model collapse recursive training synthetic data generation"

Links: [{"title":"AI-generated data contamination erodes pathological ...","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344383v1.full.pdf"},{"title":"Multi-modal Synthetic Data Training and Model Collapse: Insights from VLMs and Diffusion Models","url":"https://arxiv.org/html/2505.08803v1"},{"title":"Synthetic Data Generation Using Large Language Models","url":"https://arxiv.org/pdf/2503.14023"},{"title":"AI models collapse when trained on recursively generated data | Nature","url":"https://www.nature.com/articles/s41586-024-07566-y"},{"title":"The AI Model Collapse Risk is Not Solved in 2025","url":"https://www.winssolutions.org/ai-model-collapse-2025-recursive-training/"},{"title":"Addressing Concerns of Model Collapse from Synthetic Data in AI","url":"https://www.gretel.ai/blog/addressing-concerns-of-model-collapse-from-synthetic-data-in-ai"},{"title":"Fit, simulate, fit: How models can collapse after generations of recursive fitting - The DO Loop","url":"https://blogs.sas.com/content/iml/2024/07/31/synthetic-data-model-collapse.html"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse","url":"https://arxiv.org/html/2404.05090v1"},{"title":"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops","url":"https://arxiv.org/html/2502.18865"},{"title":"Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training","url":"https://arxiv.org/html/2509.04796v1"}]

Based on the search results, here's a comprehensive overview of the topics you're asking about:

## Model Collapse in Recursive Training

Model collapse is a phenomenon in which models recursively trained on self-generated data experience performance degradation. It is hypothesized that model collapse happens because synthetic data lacks the diversity and nuances of real-world data.

## N-gram Diversity and Linguistic Collapse

Linguistic collapse is characterized by converging impression word counts, shrinking vocabulary size, increased n-gram repetition, and rising perplexity across generations. Distinct-n (n-gram diversity) is used as a diversity and realism metric for evaluating synthetic data quality.

## Key Mechanisms

Model collapse refers to the model's tendency to produce limited or repetitive outputs making recursive training on such outputs forget about the tails of the original underlying distribution of real data. A language model tends to over-predict events that have high probability and under-predict rare events, and if this process repeats itself over several generations of AI models, the models of the future will increasingly generate high-probability events and rarely generate low-probability events.

## Mitigation Strategies

There is a consensus that recursive training on model-made data without real-data anchoring drives collapse. Model collapse cannot be avoided when training solely on synthetic data; however, when mixing both real and synthetic data, model collapse can eventually be avoided when the amount of synthetic data is below a certain threshold.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "542b0a49-04b3-4ab5-aee6-8be58243e017",
  "tool_use_result": {
    "query": "n-gram diversity model collapse recursive training synthetic data generation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CNUSABS8fWnmWA7hzUs3q8",
        "content": [
          {
            "title": "AI-generated data contamination erodes pathological ...",
            "url": "https://www.medrxiv.org/content/10.64898/2026.01.19.26344383v1.full.pdf"
          },
          {
            "title": "Multi-modal Synthetic Data Training and Model Collapse: Insights from VLMs and Diffusion Models",
            "url": "https://arxiv.org/html/2505.08803v1"
          },
          {
            "title": "Synthetic Data Generation Using Large Language Models",
            "url": "https://arxiv.org/pdf/2503.14023"
          },
          {
            "title": "AI models collapse when trained on recursively generated data | Nature",
            "url": "https://www.nature.com/articles/s41586-024-07566-y"
          },
          {
            "title": "The AI Model Collapse Risk is Not Solved in 2025",
            "url": "https://www.winssolutions.org/ai-model-collapse-2025-recursive-training/"
          },
          {
            "title": "Addressing Concerns of Model Collapse from Synthetic Data in AI",
            "url": "https://www.gretel.ai/blog/addressing-concerns-of-model-collapse-from-synthetic-data-in-ai"
          },
          {
            "title": "Fit, simulate, fit: How models can collapse after generations of recursive fitting - The DO Loop",
            "url": "https://blogs.sas.com/content/iml/2024/07/31/synthetic-data-model-collapse.html"
          },
          {
            "title": "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse",
            "url": "https://arxiv.org/html/2404.05090v1"
          },
          {
            "title": "A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops",
            "url": "https://arxiv.org/html/2502.18865"
          },
          {
            "title": "Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training",
            "url": "https://arxiv.org/html/2509.04796v1"
          }
        ]
      },
      "Based on the search results, here's a comprehensive overview of the topics you're asking about:\n\n## Model Collapse in Recursive Training\n\nModel collapse is a phenomenon in which models recursively trained on self-generated data experience performance degradation. It is hypothesized that model collapse happens because synthetic data lacks the diversity and nuances of real-world data.\n\n## N-gram Diversity and Linguistic Collapse\n\nLinguistic collapse is characterized by converging impression word counts, shrinking vocabulary size, increased n-gram repetition, and rising perplexity across generations. Distinct-n (n-gram diversity) is used as a diversity and realism metric for evaluating synthetic data quality.\n\n## Key Mechanisms\n\nModel collapse refers to the model's tendency to produce limited or repetitive outputs making recursive training on such outputs forget about the tails of the original underlying distribution of real data. A language model tends to over-predict events that have high probability and under-predict rare events, and if this process repeats itself over several generations of AI models, the models of the future will increasingly generate high-probability events and rarely generate low-probability events.\n\n## Mitigation Strategies\n\nThere is a consensus that recursive training on model-made data without real-data anchoring drives collapse. Model collapse cannot be avoided when training solely on synthetic data; however, when mixing both real and synthetic data, model collapse can eventually be avoided when the amount of synthetic data is below a certain threshold."
    ],
    "durationSeconds": 6.8914066909999985
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T10:22:36.030Z_

<details><summary>↩ Tool result · `toolu_016nbdXLgd8bhcSku9jfrYma`</summary>

```text
Web search results for query: "effective rank diversity metrics divergence language model collapse"

Links: [{"title":"The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward","url":"https://arxiv.org/html/2509.07430v1"},{"title":"The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward | OpenReview","url":"https://openreview.net/forum?id=xPEsxcO7F7"},{"title":"Evaluating the Diversity and Quality of LLM Generated ...","url":"https://openreview.net/pdf?id=O7bF6nlSOD"},{"title":"Knowledge Collapse in LLMs","url":"https://www.emergentmind.com/topics/knowledge-collapse-in-llms"},{"title":"Evaluating the Diversity and Quality of LLM Generated Content","url":"https://arxiv.org/html/2504.12522v1"},{"title":"Epistemic Diversity and Knowledge Collapse in Large Language Models","url":"https://arxiv.org/pdf/2510.04226"},{"title":"Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity","url":"https://arxiv.org/html/2510.01171v1"},{"title":"Diverse, not Short: A Length-Controlled Data Selection Strategy for Improving Response Diversity of Language Models","url":"https://arxiv.org/html/2505.16245"},{"title":"preserving diversity in supervised fine-tuning","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf"},{"title":"THE CHOICE OF DIVERGENCE: A NEGLECTED KEY TO MITIGATING DIVERSITY COLLAPSE","url":"https://arxiv.org/pdf/2509.07430"}]

Based on the web search results, here's what I found about effective rank, diversity metrics, divergence, and language model collapse:

## Key Research Findings

### Language Model Diversity Collapse

Recent research addresses the limitations of reverse KL divergence in current large language model reinforcement learning methods through f-divergence, which effectively solves the issue of diversity collapse. A central paradox in fine-tuning Large Language Models (LLMs) with Reinforcement Learning with Verifiable Reward (RLVR) is the frequent degradation of multi-attempt performance (Pass@k) despite improvements in single-attempt accuracy (Pass@1), often accompanied by catastrophic forgetting.

### Measuring Diversity

Researchers have introduced a framework for measuring effective semantic diversity—diversity among outputs that meet quality thresholds—which better reflects the practical utility of large language models. Knowledge collapse in LLMs is modeled with metrics like cosine similarity, Hill-Shannon diversity, and Hellinger distance to quantify the reduction in epistemic diversity.

### Alternative Solutions Using Divergence

The Diversity-Preserving Hybrid RL (DPH-RL) framework leverages mass-covering f-divergences (like forward-KL and JS-divergence) to function as a 'rehearsal mechanism', continuously referencing the initial policy to force the model to maintain broad solution coverage.

### Mode Collapse in Post-Training

Post-training alignment often reduces LLM diversity, leading to mode collapse, with typicality bias in preference data being a fundamental, pervasive data-level driver whereby annotators systematically favor familiar text.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "88f942b3-4b7e-4799-9cdc-49fa0f965ecb",
  "tool_use_result": {
    "query": "effective rank diversity metrics divergence language model collapse",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LCFVTuwnEqZwMQ5Pd9wx9W",
        "content": [
          {
            "title": "The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward",
            "url": "https://arxiv.org/html/2509.07430v1"
          },
          {
            "title": "The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward | OpenReview",
            "url": "https://openreview.net/forum?id=xPEsxcO7F7"
          },
          {
            "title": "Evaluating the Diversity and Quality of LLM Generated ...",
            "url": "https://openreview.net/pdf?id=O7bF6nlSOD"
          },
          {
            "title": "Knowledge Collapse in LLMs",
            "url": "https://www.emergentmind.com/topics/knowledge-collapse-in-llms"
          },
          {
            "title": "Evaluating the Diversity and Quality of LLM Generated Content",
            "url": "https://arxiv.org/html/2504.12522v1"
          },
          {
            "title": "Epistemic Diversity and Knowledge Collapse in Large Language Models",
            "url": "https://arxiv.org/pdf/2510.04226"
          },
          {
            "title": "Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity",
            "url": "https://arxiv.org/html/2510.01171v1"
          },
          {
            "title": "Diverse, not Short: A Length-Controlled Data Selection Strategy for Improving Response Diversity of Language Models",
            "url": "https://arxiv.org/html/2505.16245"
          },
          {
            "title": "preserving diversity in supervised fine-tuning",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf"
          },
          {
            "title": "THE CHOICE OF DIVERGENCE: A NEGLECTED KEY TO MITIGATING DIVERSITY COLLAPSE",
            "url": "https://arxiv.org/pdf/2509.07430"
          }
        ]
      },
      "Based on the web search results, here's what I found about effective rank, diversity metrics, divergence, and language model collapse:\n\n## Key Research Findings\n\n### Language Model Diversity Collapse\n\nRecent research addresses the limitations of reverse KL divergence in current large language model reinforcement learning methods through f-divergence, which effectively solves the issue of diversity collapse. A central paradox in fine-tuning Large Language Models (LLMs) with Reinforcement Learning with Verifiable Reward (RLVR) is the frequent degradation of multi-attempt performance (Pass@k) despite improvements in single-attempt accuracy (Pass@1), often accompanied by catastrophic forgetting.\n\n### Measuring Diversity\n\nResearchers have introduced a framework for measuring effective semantic diversity—diversity among outputs that meet quality thresholds—which better reflects the practical utility of large language models. Knowledge collapse in LLMs is modeled with metrics like cosine similarity, Hill-Shannon diversity, and Hellinger distance to quantify the reduction in epistemic diversity.\n\n### Alternative Solutions Using Divergence\n\nThe Diversity-Preserving Hybrid RL (DPH-RL) framework leverages mass-covering f-divergences (like forward-KL and JS-divergence) to function as a 'rehearsal mechanism', continuously referencing the initial policy to force the model to maintain broad solution coverage.\n\n### Mode Collapse in Post-Training\n\nPost-training alignment often reduces LLM diversity, leading to mode collapse, with typicality bias in preference data being a fundamental, pervasive data-level driver whereby annotators systematically favor familiar text."
    ],
    "durationSeconds": 7.822145703999999
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-18T10:22:36.447Z_

<details><summary>↩ Tool result · `toolu_01FmKM6GmWum8df47PvxiaFU`</summary>

```text
Web search results for query: "model collapse diversity loss spectral metrics divergence synthetic data"

Links: [{"title":"Mode Collapse in Generative Models","url":"https://www.emergentmind.com/topics/mode-collapse"},{"title":"1 Introduction","url":"https://arxiv.org/html/2510.04202v1"},{"title":"What Is Model Collapse? Causes, Examples, and Fixes | DataCamp","url":"https://www.datacamp.com/blog/what-is-model-collapse"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of","url":"https://arxiv.org/pdf/2404.01413"},{"title":"Early Detection of Mode Collapse in GANs Through Loss Monitoring | Request PDF","url":"https://www.researchgate.net/publication/391897296_Early_Detection_of_Mode_Collapse_in_GANs_Through_Loss_Monitoring"},{"title":"AI Model Collapse: Causes and Prevention - WitnessAI","url":"https://witness.ai/blog/ai-model-collapse/"},{"title":"How training data properties modulate distribution shift in ...","url":"https://aclanthology.org/2025.emnlp-main.1643.pdf"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v1"},{"title":"Model collapse - Wikipedia","url":"https://en.wikipedia.org/wiki/Model_collapse"},{"title":"Understanding Model Collapse: A Hidden Threat in Generative AI | Generative AI Lab","url":"https://generativeailab.org/l/trends/understanding-model-collapse/1080/"}]

I've found comprehensive information on your search query. Here are the key findings:

## Model Collapse and Diversity Loss

Model collapse refers to the failure of a generative model to capture the full diversity of a target distribution, manifesting as concentration of generated mass onto a strict subset of ground-truth modes or regions. Model collapse induces a loss of data diversity because synthetic data overemphasizes common patterns while erasing rare or minority ones (outliers), leading to biased models that ignore edge cases.

## Spectral Metrics and Divergence

Spectral Alignment (SA) is a novel, theoretically-grounded metric that monitors distributional alignment between layer inputs and principal singular vectors of weight matrices, where a collapse in sign diversity of this alignment is a powerful early predictor of representational collapse and training divergence.

Spectral collapse describes a phenomenon where a large number of singular values of weight matrices drop dramatically when mode collapse occurs, and there is strong evidence linking mode collapse to spectral collapse.

## Diversity Loss with Synthetic Data

Training language models on predecessor-generated text causes a consistent decrease in the lexical, syntactic, and semantic diversity of model outputs through successive iterations. However, if synthetic data accumulates alongside human-generated data, model collapse is avoided.

## Detection Metrics

Diversity metrics for detecting mode collapse include the number of unique clusters, KL divergence between class frequencies, Inception Score (IS), and techniques such as optimal transport are used to identify and quantify mode collapse.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "370b5ba8-bc4f-43ec-9bf6-c86e9e367535",
  "tool_use_result": {
    "query": "model collapse diversity loss spectral metrics divergence synthetic data",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LwX1sAGe43LMjKjDfWr8BP",
        "content": [
          {
            "title": "Mode Collapse in Generative Models",
            "url": "https://www.emergentmind.com/topics/mode-collapse"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2510.04202v1"
          },
          {
            "title": "What Is Model Collapse? Causes, Examples, and Fixes | DataCamp",
            "url": "https://www.datacamp.com/blog/what-is-model-collapse"
          },
          {
            "title": "Is Model Collapse Inevitable? Breaking the Curse of",
            "url": "https://arxiv.org/pdf/2404.01413"
          },
          {
            "title": "Early Detection of Mode Collapse in GANs Through Loss Monitoring | Request PDF",
            "url": "https://www.researchgate.net/publication/391897296_Early_Detection_of_Mode_Collapse_in_GANs_Through_Loss_Monitoring"
          },
          {
            "title": "AI Model Collapse: Causes and Prevention - WitnessAI",
            "url": "https://witness.ai/blog/ai-model-collapse/"
          },
          {
            "title": "How training data properties modulate distribution shift in ...",
            "url": "https://aclanthology.org/2025.emnlp-main.1643.pdf"
          },
          {
            "title": "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective",
            "url": "https://arxiv.org/html/2509.16499v1"
          },
          {
            "title": "Model collapse - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Model_collapse"
          },
          {
            "title": "Understanding Model Collapse: A Hidden Threat in Generative AI | Generative AI Lab",
            "url": "https://generativeailab.org/l/trends/understanding-model-collapse/1080/"
          }
        ]
      },
      "I've found comprehensive information on your search query. Here are the key findings:\n\n## Model Collapse and Diversity Loss\n\nModel collapse refers to the failure of a generative model to capture the full diversity of a target distribution, manifesting as concentration of generated mass onto a strict subset of ground-truth modes or regions. Model collapse induces a loss of data diversity because synthetic data overemphasizes common patterns while erasing rare or minority ones (outliers), leading to biased models that ignore edge cases.\n\n## Spectral Metrics and Divergence\n\nSpectral Alignment (SA) is a novel, theoretically-grounded metric that monitors distributional alignment between layer inputs and principal singular vectors of weight matrices, where a collapse in sign diversity of this alignment is a powerful early predictor of representational collapse and training divergence.\n\nSpectral collapse describes a phenomenon where a large number of singular values of weight matrices drop dramatically when mode collapse occurs, and there is strong evidence linking mode collapse to spectral collapse.\n\n## Diversity Loss with Synthetic Data\n\nTraining language models on predecessor-generated text causes a consistent decrease in the lexical, syntactic, and semantic diversity of model outputs through successive iterations. However, if synthetic data accumulates alongside human-generated data, model collapse is avoided.\n\n## Detection Metrics\n\nDiversity metrics for detecting mode collapse include the number of unique clusters, KL divergence between class frequencies, Inception Score (IS), and techniques such as optimal transport are used to identify and quantify mode collapse."
    ],
    "durationSeconds": 8.687408879000003
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Now let me do more targeted searches for the specific papers mentioned in the task, and for the specific phenomenon of spectral vs diversity divergence.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "b816c659-13e8-4b1a-b7cd-a04803a89620",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LjsFuNJBEubW9AhneDsNju",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2578,
      "cache_creation_input_tokens": 7255,
      "cache_read_input_tokens": 26066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7255
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

_source line 19_

继续针对性搜索 gerstgrasser2024inevitable 和 dohmatob2025strong 的 diversity 数据，以及 SIGMA 的 diversity 报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "1b089964-250e-4b39-ad1a-91c5f3447427",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LjsFuNJBEubW9AhneDsNju",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2578,
      "cache_creation_input_tokens": 7255,
      "cache_read_input_tokens": 26066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7255
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_016jBCAV4KqgTu6f4ixVeFKm`</summary>

```json
{
  "query": "gerstgrasser 2024 \"model collapse inevitable\" accumulating data diversity distinct-n metrics arXiv 2404.01413"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "bf9d862b-91b7-4229-a2c0-7121c0f1b6e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LjsFuNJBEubW9AhneDsNju",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2578,
      "cache_creation_input_tokens": 7255,
      "cache_read_input_tokens": 26066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7255
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

_source line 21_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RwzSMPjK3vXzPQ84Mkf7Mx`</summary>

```json
{
  "query": "dohmatob \"strong model collapse\" spectral diversity singular value 2410.04840"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "940d216b-91e9-483e-bbfa-95552b7a20f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LjsFuNJBEubW9AhneDsNju",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2578,
      "cache_creation_input_tokens": 7255,
      "cache_read_input_tokens": 26066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7255
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

_source line 22_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S4pF59p14iKNd8TqvEejRr`</summary>

```json
{
  "query": "SIGMA spectral insights model collapse diversity metrics Gu Pang 2601.03385"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "1560d906-47f3-4226-959a-48c17f3058fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LjsFuNJBEubW9AhneDsNju",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2578,
      "cache_creation_input_tokens": 7255,
      "cache_read_input_tokens": 26066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7255
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

_source line 23_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011ucQBYVcjyUsDzBPxgzpJP`</summary>

```json
{
  "query": "\"effective rank\" \"distinct-n\" OR \"self-BLEU\" divergence model collapse synthetic training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "a72bfe46-dd51-4e9a-9f37-5d809a65049f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LjsFuNJBEubW9AhneDsNju",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2578,
      "cache_creation_input_tokens": 7255,
      "cache_read_input_tokens": 26066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7255
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

_source line 24 · 2026-05-18T10:22:49.525Z_

<details><summary>↩ Tool result · `toolu_016jBCAV4KqgTu6f4ixVeFKm`</summary>

```text
Web search results for query: "gerstgrasser 2024 "model collapse inevitable" accumulating data diversity distinct-n metrics arXiv 2404.01413"

Links: [{"title":"[2404.01413] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of","url":"https://arxiv.org/pdf/2404.01413"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Rylan Schaeffer","url":"https://rylanschaeffer.github.io/content/research/2024_arxiv_is_model_collapse_inevitable/main.html"},{"title":"[2404.01413v1] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413v1"},{"title":"[PDF] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Is-Model-Collapse-Inevitable-Breaking-the-Curse-of-Gerstgrasser-Schaeffer/e8815da26d4e6cac8b23b7e6aa75cec028cb66d2"},{"title":"Accumulating Data Prevents Model Collapse","url":"https://www.emergentmind.com/papers/2404.01413"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v2"},{"title":"AI-Powered Paper Summarization about the arXiv paper 2404.01413v1","url":"https://www.summarizepaper.com/en/arxiv-id/2404.01413v1/"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/html/2404.01413v1"},{"title":"Addressing Concerns of Model Collapse from Synthetic Data in AI","url":"https://www.gretel.ai/blog/addressing-concerns-of-model-collapse-from-synthetic-data-in-ai"}]

I found the paper you were searching for. Here's what the search results reveal:

## Paper Summary

The paper "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data" is by Matthias Gerstgrasser and 13 other authors, published on arXiv as 2404.01413.

### Main Research Question

The paper addresses what happens when generative models are trained on their own generated outputs, examining whether model-data feedback loops lead to model collapse, where performance progressively degrades with each model-data feedback iteration until fitted models become useless.

### Key Findings

The research notes that prior studies largely assumed new data replace old data over time, whereas a more realistic assumption is that data accumulate over time. 

The paper's core contribution is that accumulating data prevents model collapse. More specifically, if data are replaced, test error increases with the number of model-fitting iterations, but if data instead accumulate, test error has a finite upper bound independent of the number of iterations, meaning model collapse no longer occurs.

### Methodology

The researchers empirically study the question by pretraining sequences of language models on text corpora, and use three diverse experimental setups of causal transformers, diffusion models, and variational autoencoders trained on real text, molecular conformation, and image datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "e8dc2f39-24f2-4af2-9669-6513f2d7053b",
  "tool_use_result": {
    "query": "gerstgrasser 2024 \"model collapse inevitable\" accumulating data diversity distinct-n metrics arXiv 2404.01413",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TdbxVdfDFNi78rv4PgsPCP",
        "content": [
          {
            "title": "[2404.01413] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data",
            "url": "https://arxiv.org/abs/2404.01413"
          },
          {
            "title": "Is Model Collapse Inevitable? Breaking the Curse of",
            "url": "https://arxiv.org/pdf/2404.01413"
          },
          {
            "title": "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Rylan Schaeffer",
            "url": "https://rylanschaeffer.github.io/content/research/2024_arxiv_is_model_collapse_inevitable/main.html"
          },
          {
            "title": "[2404.01413v1] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data",
            "url": "https://arxiv.org/abs/2404.01413v1"
          },
          {
            "title": "[PDF] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Is-Model-Collapse-Inevitable-Breaking-the-Curse-of-Gerstgrasser-Schaeffer/e8815da26d4e6cac8b23b7e6aa75cec028cb66d2"
          },
          {
            "title": "Accumulating Data Prevents Model Collapse",
            "url": "https://www.emergentmind.com/papers/2404.01413"
          },
          {
            "title": "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective",
            "url": "https://arxiv.org/html/2509.16499v2"
          },
          {
            "title": "AI-Powered Paper Summarization about the arXiv paper 2404.01413v1",
            "url": "https://www.summarizepaper.com/en/arxiv-id/2404.01413v1/"
          },
          {
            "title": "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data",
            "url": "https://arxiv.org/html/2404.01413v1"
          },
          {
            "title": "Addressing Concerns of Model Collapse from Synthetic Data in AI",
            "url": "https://www.gretel.ai/blog/addressing-concerns-of-model-collapse-from-synthetic-data-in-ai"
          }
        ]
      },
      "I found the paper you were searching for. Here's what the search results reveal:\n\n## Paper Summary\n\nThe paper \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\" is by Matthias Gerstgrasser and 13 other authors, published on arXiv as 2404.01413.\n\n### Main Research Question\n\nThe paper addresses what happens when generative models are trained on their own generated outputs, examining whether model-data feedback loops lead to model collapse, where performance progressively degrades with each model-data feedback iteration until fitted models become useless.\n\n### Key Findings\n\nThe research notes that prior studies largely assumed new data replace old data over time, whereas a more realistic assumption is that data accumulate over time. \n\nThe paper's core contribution is that accumulating data prevents model collapse. More specifically, if data are replaced, test error increases with the number of model-fitting iterations, but if data instead accumulate, test error has a finite upper bound independent of the number of iterations, meaning model collapse no longer occurs.\n\n### Methodology\n\nThe researchers empirically study the question by pretraining sequences of language models on text corpora, and use three diverse experimental setups of causal transformers, diffusion models, and variational autoencoders trained on real text, molecular conformation, and image datasets."
    ],
    "durationSeconds": 6.874126198999998
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-18T10:22:50.189Z_

<details><summary>↩ Tool result · `toolu_01RwzSMPjK3vXzPQ84Mkf7Mx`</summary>

```text
Web search results for query: "dohmatob "strong model collapse" spectral diversity singular value 2410.04840"

Links: [{"title":"[2410.04840] Strong Model Collapse","url":"https://arxiv.org/abs/2410.04840"},{"title":"Strong Model Collapse Elvis Dohmatob1 e.dohmatob@meta.com Yunzhen Feng1,2,∗","url":"https://arxiv.org/pdf/2410.04840"},{"title":"Strong Model Collapse - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241004840D/abstract"},{"title":"Strong Model Collapse","url":"https://arxiv.org/html/2410.04840"},{"title":"Elvis Dohmatob on X: \"1/n Introducing our new preprint: Strong Model Collapse https://t.co/spdA6sGtDT, wherein we show that within the \"scaling laws\" paradigm, even 1% bad / synthetic data in the training corpus might lead to model collapse, an eventual critical flattening or even degradation of model https://t.co/ydRtUVe0BT\" / X","url":"https://x.com/dohmatobelvis/status/1844300320811241477"},{"title":"Strong Model Collapse | Request PDF","url":"https://www.researchgate.net/publication/384700001_Strong_Model_Collapse"},{"title":"Strong Model Collapse | alphaXiv","url":"https://www.alphaxiv.org/abs/2410.04840"},{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"},{"title":"Strong Model Collapse","url":"https://www.emergentmind.com/papers/2410.04840"},{"title":"Strong Model Collapse Dohmatob et al.: https://arxiv.org/ ...","url":"https://www.facebook.com/MontrealAI/posts/strong-model-collapsedohmatob-et-al-httpsarxivorgabs241004840artificialintellige/991389606504758/"}]

I found relevant results for your search query. Here's what the search revealed:

"Strong Model Collapse" is an arXiv paper (2410.04840) by Elvis Dohmatob and collaborators.

## Key Findings:

**Main Result:**
The research shows that even the smallest fraction of synthetic data (e.g., as little as 1% of the total training dataset) can still lead to model collapse: larger and larger training sets do not enhance performance.

**Technical Approach:**
The authors employ the tools of operator-valued free probability theory (OVFPT) to obtain a new bias-variance decomposition of the test error evaluated on the real/true data distribution, of a model trained on a mixture of real and synthetic data. This decomposition is expressed as Etest ≃ B + V + ζ, where the extra term ζ induces model collapse.

**Scope:**
The theoretical analysis focuses on regression problems in the classical linear setting and also the setting of neural networks in a simplified regime which can be approximated by random projections.

**Significance:**
The issue is especially concerning in large-scale AI systems like ChatGPT and Llama, which rely heavily on vast amounts of training data to maintain their performance. If synthetic data is used in training these models, even in small quantities, the model can start producing "gibberish" or nonsensical outputs.

The paper was published in October 2024 and has since been published as a conference paper at ICLR 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "18eb5b3b-9a73-476d-ad2b-d0c5dfa6fd2c",
  "tool_use_result": {
    "query": "dohmatob \"strong model collapse\" spectral diversity singular value 2410.04840",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BGuD4rSzqFRJkE53UQBmUQ",
        "content": [
          {
            "title": "[2410.04840] Strong Model Collapse",
            "url": "https://arxiv.org/abs/2410.04840"
          },
          {
            "title": "Strong Model Collapse Elvis Dohmatob1 e.dohmatob@meta.com Yunzhen Feng1,2,∗",
            "url": "https://arxiv.org/pdf/2410.04840"
          },
          {
            "title": "Strong Model Collapse - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv241004840D/abstract"
          },
          {
            "title": "Strong Model Collapse",
            "url": "https://arxiv.org/html/2410.04840"
          },
          {
            "title": "Elvis Dohmatob on X: \"1/n Introducing our new preprint: Strong Model Collapse https://t.co/spdA6sGtDT, wherein we show that within the \"scaling laws\" paradigm, even 1% bad / synthetic data in the training corpus might lead to model collapse, an eventual critical flattening or even degradation of model https://t.co/ydRtUVe0BT\" / X",
            "url": "https://x.com/dohmatobelvis/status/1844300320811241477"
          },
          {
            "title": "Strong Model Collapse | Request PDF",
            "url": "https://www.researchgate.net/publication/384700001_Strong_Model_Collapse"
          },
          {
            "title": "Strong Model Collapse | alphaXiv",
            "url": "https://www.alphaxiv.org/abs/2410.04840"
          },
          {
            "title": "Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"
          },
          {
            "title": "Strong Model Collapse",
            "url": "https://www.emergentmind.com/papers/2410.04840"
          },
          {
            "title": "Strong Model Collapse Dohmatob et al.: https://arxiv.org/ ...",
            "url": "https://www.facebook.com/MontrealAI/posts/strong-model-collapsedohmatob-et-al-httpsarxivorgabs241004840artificialintellige/991389606504758/"
          }
        ]
      },
      "I found relevant results for your search query. Here's what the search revealed:\n\n\"Strong Model Collapse\" is an arXiv paper (2410.04840) by Elvis Dohmatob and collaborators.\n\n## Key Findings:\n\n**Main Result:**\nThe research shows that even the smallest fraction of synthetic data (e.g., as little as 1% of the total training dataset) can still lead to model collapse: larger and larger training sets do not enhance performance.\n\n**Technical Approach:**\nThe authors employ the tools of operator-valued free probability theory (OVFPT) to obtain a new bias-variance decomposition of the test error evaluated on the real/true data distribution, of a model trained on a mixture of real and synthetic data. This decomposition is expressed as Etest ≃ B + V + ζ, where the extra term ζ induces model collapse.\n\n**Scope:**\nThe theoretical analysis focuses on regression problems in the classical linear setting and also the setting of neural networks in a simplified regime which can be approximated by random projections.\n\n**Significance:**\nThe issue is especially concerning in large-scale AI systems like ChatGPT and Llama, which rely heavily on vast amounts of training data to maintain their performance. If synthetic data is used in training these models, even in small quantities, the model can start producing \"gibberish\" or nonsensical outputs.\n\nThe paper was published in October 2024 and has since been published as a conference paper at ICLR 2025."
    ],
    "durationSeconds": 6.989874111000001
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T10:22:51.417Z_

<details><summary>↩ Tool result · `toolu_011ucQBYVcjyUsDzBPxgzpJP`</summary>

```text
Web search results for query: ""effective rank" "distinct-n" OR "self-BLEU" divergence model collapse synthetic training"

Links: [{"title":"Evaluating the Diversity and Quality of LLM Generated Content","url":"https://arxiv.org/html/2504.12522"},{"title":"Evaluating the Diversity and Quality of LLM Generated ...","url":"https://arxiv.org/pdf/2504.12522"}]

I found search results related to your query. The results come from a research paper on evaluating the diversity and quality of LLM-generated content:

Lexical metrics for measuring diversity include Distinct-N and Self-BLEU, which involve calculating summary statistics over n-grams. 

An optimization strategy that places all probability on the highest-reward outcome is optimal for certain loss functions but will inevitably lead to distribution collapse, which KL-divergence regularization has been instrumental in mitigating in preference-tuned LLMs.

In scenarios such as generating synthetic training data, the utility of the model depends not only on producing coherent responses but also on generating outputs that span a meaningful range of ideas or examples.

The paper also discusses how semantic uniqueness of generations should be determined based on their meaning rather than superficial textual differences, since two outputs may differ significantly in lexical form yet convey identical semantic content.

Would you like me to search for more specific information about any of these topics, such as "effective rank" measurements or additional details about model collapse in synthetic training?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "87a9da49-4b56-4bd7-aed4-851681681949",
  "tool_use_result": {
    "query": "\"effective rank\" \"distinct-n\" OR \"self-BLEU\" divergence model collapse synthetic training",
    "results": [
      {
        "tool_use_id": "srvtoolu_01B5McqPCoZFHDW2z1T78Huv",
        "content": [
          {
            "title": "Evaluating the Diversity and Quality of LLM Generated Content",
            "url": "https://arxiv.org/html/2504.12522"
          },
          {
            "title": "Evaluating the Diversity and Quality of LLM Generated ...",
            "url": "https://arxiv.org/pdf/2504.12522"
          }
        ]
      },
      "I found search results related to your query. The results come from a research paper on evaluating the diversity and quality of LLM-generated content:\n\nLexical metrics for measuring diversity include Distinct-N and Self-BLEU, which involve calculating summary statistics over n-grams. \n\nAn optimization strategy that places all probability on the highest-reward outcome is optimal for certain loss functions but will inevitably lead to distribution collapse, which KL-divergence regularization has been instrumental in mitigating in preference-tuned LLMs.\n\nIn scenarios such as generating synthetic training data, the utility of the model depends not only on producing coherent responses but also on generating outputs that span a meaningful range of ideas or examples.\n\nThe paper also discusses how semantic uniqueness of generations should be determined based on their meaning rather than superficial textual differences, since two outputs may differ significantly in lexical form yet convey identical semantic content.\n\nWould you like me to search for more specific information about any of these topics, such as \"effective rank\" measurements or additional details about model collapse in synthetic training?"
    ],
    "durationSeconds": 6.579771055999998
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-18T10:22:53.198Z_

<details><summary>↩ Tool result · `toolu_01S4pF59p14iKNd8TqvEejRr`</summary>

```text
Web search results for query: "SIGMA spectral insights model collapse diversity metrics Gu Pang 2601.03385"

Links: [{"title":"[2601.03385] SIGMA: Scalable Spectral Insights for LLM Model Collapse","url":"https://arxiv.org/abs/2601.03385"},{"title":"SIGMA: Scalable Spectral Insights for LLM Model Collapse","url":"https://www.arxiv.org/pdf/2601.03385"},{"title":"Sigma: Scalable Spectral Insights for LLM Model Collapse","url":"https://arxiv.org/html/2601.03385"},{"title":"Sigma: Scalable Spectral Insights for LLM Collapse","url":"https://arxiv.org/html/2601.03385v1"},{"title":"HyperSIGMA: Hyperspectral Intelligence Comprehension Foundation Model","url":"https://arxiv.org/html/2406.11519v1"},{"title":"SIGMA: Spectral Interpretation Using Gaussian Mixtures and Autoencoder - Tung - 2023 - Geochemistry, Geophysics, Geosystems - Wiley Online Library","url":"https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2022GC010530"},{"title":"(PDF) SIGMA: Spectral Interpretation Using Gaussian Mixtures and Autoencoder","url":"https://www.researchgate.net/publication/367093978_SIGMA_Spectral_Interpretation_using_Gaussian_Mixtures_and_Autoencoder"},{"title":"Spectral shape metrics and structural collapse potential - Eads - 2016 - Earthquake Engineering & Structural Dynamics - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1002/eqe.2739"},{"title":"Machine Learning Jun 2025","url":"https://arxiv.org/list/cs.LG/2025-06?skip=3350&show=2000"},{"title":"[2601.02080] The Homogeneity Trap: Spectral Collapse in Doubly-Stochastic Deep Networks","url":"https://arxiv.org/abs/2601.02080"}]

Based on the search results, I found detailed information about the paper you're looking for:

## SIGMA: Scalable Spectral Insights for LLM Model Collapse

The paper is authored by Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, and Alexander Aue.

SIGMA (Spectral Inequalities for Gram Matrix Analysis) is a unified framework that benchmarks model collapse through the spectral lens of the embedding Gram matrix. 

The paper addresses the technical challenge of "model collapse"–a degenerative process where recursive training on model-generated content leads to a contraction of distributional variance and representational quality. While the phenomenology of collapse is increasingly evident, rigorous methods to quantify and predict its onset in high-dimensional spaces remain elusive.

By deriving and utilizing deterministic and stochastic bounds on the matrix's spectrum, SIGMA provides a mathematically grounded metric to track the contraction of the representation space. The framework focuses on representation geometry by tracking collapse via the eigenspectrum of embedding Gram matrices and develops deterministic and stochastic spectral inequalities that enable scalable, one-sided monitoring when only partial Gram information is available.

The paper was first submitted on January 6, 2026, with the most recent version from March 23, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "331139d4-6c85-4071-9937-0272db63c44c",
  "tool_use_result": {
    "query": "SIGMA spectral insights model collapse diversity metrics Gu Pang 2601.03385",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WZqNdXvR18Y9z9VRrYR466",
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
            "title": "HyperSIGMA: Hyperspectral Intelligence Comprehension Foundation Model",
            "url": "https://arxiv.org/html/2406.11519v1"
          },
          {
            "title": "SIGMA: Spectral Interpretation Using Gaussian Mixtures and Autoencoder - Tung - 2023 - Geochemistry, Geophysics, Geosystems - Wiley Online Library",
            "url": "https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2022GC010530"
          },
          {
            "title": "(PDF) SIGMA: Spectral Interpretation Using Gaussian Mixtures and Autoencoder",
            "url": "https://www.researchgate.net/publication/367093978_SIGMA_Spectral_Interpretation_using_Gaussian_Mixtures_and_Autoencoder"
          },
          {
            "title": "Spectral shape metrics and structural collapse potential - Eads - 2016 - Earthquake Engineering & Structural Dynamics - Wiley Online Library",
            "url": "https://onlinelibrary.wiley.com/doi/10.1002/eqe.2739"
          },
          {
            "title": "Machine Learning Jun 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-06?skip=3350&show=2000"
          },
          {
            "title": "[2601.02080] The Homogeneity Trap: Spectral Collapse in Doubly-Stochastic Deep Networks",
            "url": "https://arxiv.org/abs/2601.02080"
          }
        ]
      },
      "Based on the search results, I found detailed information about the paper you're looking for:\n\n## SIGMA: Scalable Spectral Insights for LLM Model Collapse\n\nThe paper is authored by Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, and Alexander Aue.\n\nSIGMA (Spectral Inequalities for Gram Matrix Analysis) is a unified framework that benchmarks model collapse through the spectral lens of the embedding Gram matrix. \n\nThe paper addresses the technical challenge of \"model collapse\"–a degenerative process where recursive training on model-generated content leads to a contraction of distributional variance and representational quality. While the phenomenology of collapse is increasingly evident, rigorous methods to quantify and predict its onset in high-dimensional spaces remain elusive.\n\nBy deriving and utilizing deterministic and stochastic bounds on the matrix's spectrum, SIGMA provides a mathematically grounded metric to track the contraction of the representation space. The framework focuses on representation geometry by tracking collapse via the eigenspectrum of embedding Gram matrices and develops deterministic and stochastic spectral inequalities that enable scalable, one-sided monitoring when only partial Gram information is available.\n\nThe paper was first submitted on January 6, 2026, with the most recent version from March 23, 2026."
    ],
    "durationSeconds": 9.000272737
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
Now let me look more specifically at the SIGMA paper and Gerstgrasser paper to check if they report diversity metrics. Let me also search for the specific phenomenon we're observing - where spectral health recovers but diversity still collapses.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "cbd68d81-414c-402d-9f35-d04b96b91891",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HmBy66UyUkdt1qUjPGe6yv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 389,
      "cache_creation_input_tokens": 5833,
      "cache_read_input_tokens": 33321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5833
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

_source line 29_

进一步查看 SIGMA 论文全文是否报告了 diversity metrics，以及搜索 "spectral health" 与 diversity collapse 的 divergence 现象。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "950f040d-0ac2-49cf-b490-4f3b702cc015",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HmBy66UyUkdt1qUjPGe6yv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 389,
      "cache_creation_input_tokens": 5833,
      "cache_read_input_tokens": 33321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5833
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_0132dhBsi3MDPtau3qXAZ1vU`</summary>

```json
{
  "query": "site:arxiv.org \"2601.03385\" SIGMA model collapse distinct-n perplexity diversity evaluation metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "c3e688ec-8806-49f7-9373-e707d21a476b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HmBy66UyUkdt1qUjPGe6yv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 389,
      "cache_creation_input_tokens": 5833,
      "cache_read_input_tokens": 33321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5833
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HCatbJS8f9zVksQrG8FYEr`</summary>

```json
{
  "query": "\"real data mixing\" \"diversity collapse\" spectral health synthetic training generations language model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "c4f2942d-3735-420d-bd44-41074f64139a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HmBy66UyUkdt1qUjPGe6yv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 389,
      "cache_creation_input_tokens": 5833,
      "cache_read_input_tokens": 33321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5833
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_011msZFAqTuoHHq88KsEcM9E`</summary>

```json
{
  "query": "briesch 2023 \"self-consuming\" LLM diversity distinct repetition spectral 2311.16822"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "4cfb03af-f6dd-4199-b28a-e692fcdaae7d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HmBy66UyUkdt1qUjPGe6yv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 389,
      "cache_creation_input_tokens": 5833,
      "cache_read_input_tokens": 33321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5833
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

_source line 33 · 2026-05-18T10:23:05.571Z_

<details><summary>↩ Tool result · `toolu_0132dhBsi3MDPtau3qXAZ1vU`</summary>

```text
Web search results for query: "site:arxiv.org "2601.03385" SIGMA model collapse distinct-n perplexity diversity evaluation metrics"

Links: [{"title":"[2601.03385] SIGMA: Scalable Spectral Insights for LLM Model Collapse","url":"https://arxiv.org/abs/2601.03385"},{"title":"Sigma: Scalable Spectral Insights for LLM Model Collapse","url":"https://arxiv.org/html/2601.03385"},{"title":"Perplexity for LLM Evaluation - Comet","url":"https://www.comet.com/site/blog/perplexity-for-llm-evaluation/"},{"title":"Perplexity - Wikipedia","url":"https://en.wikipedia.org/wiki/Perplexity"},{"title":"Perplexity for LLM Evaluation - GeeksforGeeks","url":"https://www.geeksforgeeks.org/nlp/perplexity-for-llm-evaluation/"},{"title":"Perplexity as an evaluation metric for ML models | Statistical Odds & Ends","url":"https://statisticaloddsandends.wordpress.com/2023/10/24/perplexity-as-an-evaluation-metric-for-ml-models/"},{"title":"Evaluating Language Models Using Perplexity | Baeldung on Computer Science","url":"https://www.baeldung.com/cs/language-models-perplexity"},{"title":"Understanding Perplexity as a Statistical Measure of Language Model Performance","url":"https://www.statology.org/understanding-perplexity-statistical-measure-language-model-performance/"},{"title":"Perplexity: The Standard Language Model Metric - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/perplexity-language-model-evaluation-metric"},{"title":"Perplexity in LLMs: Formula, GPT Benchmarks & Interactive Guide | TensorTonic","url":"https://www.tensortonic.com/ml-math/information-theory/perplexity"}]

Based on the web search results, here's what I found about the SIGMA paper (arXiv:2601.03385) and its use of evaluation metrics:

## SIGMA Framework Overview

SIGMA (Spectral Inequalities for Gram Matrix Analysis) is a unified framework that benchmarks model collapse through the spectral lens of the embedding Gram matrix. The paper addresses "model collapse"—a degenerative process where recursive training on model-generated content leads to a contraction of distributional variance and representational quality.

## Evaluation Metrics Used

Regarding the evaluation metrics you asked about specifically, the paper computes two lightweight proxies: (i) distinct-2 (unique/total bigrams; higher is more diverse), and (ii) hashed n-gram HHI (higher is more concentrated/repetitive). These proxies are not collapse definitions and can be noisy, but they provide an operational sanity check.

Sigma-UB is specifically constructed to follow the geometry of the gram matrix instead of merely capturing surface-level repetition. Nevertheless, it is useful to ask whether geometry contraction coincides with familiar surface-form baseline metrics.

The paper uses these diversity and surface-form metrics alongside the main SIGMA metric to validate that the spectral approach to detecting model collapse aligns with more traditional diversity-based evaluation approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "59257ea8-4b6b-4df3-91f1-9f556a3acfdd",
  "tool_use_result": {
    "query": "site:arxiv.org \"2601.03385\" SIGMA model collapse distinct-n perplexity diversity evaluation metrics",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Xzpg531fH4ovFqPtBbPvGY",
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
            "title": "Perplexity for LLM Evaluation - Comet",
            "url": "https://www.comet.com/site/blog/perplexity-for-llm-evaluation/"
          },
          {
            "title": "Perplexity - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Perplexity"
          },
          {
            "title": "Perplexity for LLM Evaluation - GeeksforGeeks",
            "url": "https://www.geeksforgeeks.org/nlp/perplexity-for-llm-evaluation/"
          },
          {
            "title": "Perplexity as an evaluation metric for ML models | Statistical Odds & Ends",
            "url": "https://statisticaloddsandends.wordpress.com/2023/10/24/perplexity-as-an-evaluation-metric-for-ml-models/"
          },
          {
            "title": "Evaluating Language Models Using Perplexity | Baeldung on Computer Science",
            "url": "https://www.baeldung.com/cs/language-models-perplexity"
          },
          {
            "title": "Understanding Perplexity as a Statistical Measure of Language Model Performance",
            "url": "https://www.statology.org/understanding-perplexity-statistical-measure-language-model-performance/"
          },
          {
            "title": "Perplexity: The Standard Language Model Metric - Interactive | Michael Brenndoerfer | Michael Brenndoerfer",
            "url": "https://mbrenndoerfer.com/writing/perplexity-language-model-evaluation-metric"
          },
          {
            "title": "Perplexity in LLMs: Formula, GPT Benchmarks & Interactive Guide | TensorTonic",
            "url": "https://www.tensortonic.com/ml-math/information-theory/perplexity"
          }
        ]
      },
      "Based on the web search results, here's what I found about the SIGMA paper (arXiv:2601.03385) and its use of evaluation metrics:\n\n## SIGMA Framework Overview\n\nSIGMA (Spectral Inequalities for Gram Matrix Analysis) is a unified framework that benchmarks model collapse through the spectral lens of the embedding Gram matrix. The paper addresses \"model collapse\"—a degenerative process where recursive training on model-generated content leads to a contraction of distributional variance and representational quality.\n\n## Evaluation Metrics Used\n\nRegarding the evaluation metrics you asked about specifically, the paper computes two lightweight proxies: (i) distinct-2 (unique/total bigrams; higher is more diverse), and (ii) hashed n-gram HHI (higher is more concentrated/repetitive). These proxies are not collapse definitions and can be noisy, but they provide an operational sanity check.\n\nSigma-UB is specifically constructed to follow the geometry of the gram matrix instead of merely capturing surface-level repetition. Nevertheless, it is useful to ask whether geometry contraction coincides with familiar surface-form baseline metrics.\n\nThe paper uses these diversity and surface-form metrics alongside the main SIGMA metric to validate that the spectral approach to detecting model collapse aligns with more traditional diversity-based evaluation approaches."
    ],
    "durationSeconds": 7.031924853999997
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-18T10:23:06.965Z_

<details><summary>↩ Tool result · `toolu_011msZFAqTuoHHq88KsEcM9E`</summary>

```text
Web search results for query: "briesch 2023 "self-consuming" LLM diversity distinct repetition spectral 2311.16822"

Links: [{"title":"[2311.16822] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://arxiv.org/abs/2311.16822"},{"title":"[2311.16822v2] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://arxiv.org/abs/2311.16822v2"},{"title":"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://arxiv.org/html/2311.16822"},{"title":"[Submitted on 28 Nov 2023 (v1), last revised 17 Jun 2024 (this version, v2)]","url":"https://arxiv.org/pdf/2311.16822"},{"title":"LLM Self-Consuming Training Loop Analysis","url":"https://www.emergentmind.com/papers/2311.16822"},{"title":"[2311.16822] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://ar5iv.labs.arxiv.org/html/2311.16822"},{"title":"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2311.16822"},{"title":"What Matters in LLM-generated Data: Diversity and Its Effect on Model Fine-Tuning","url":"https://arxiv.org/html/2506.19262"},{"title":"Understanding the Repeat Curse in Large Language ...","url":"https://aclanthology.org/2025.findings-acl.406.pdf"},{"title":"How Far Can We Extract Diverse Perspectives from Large Language Models?","url":"https://arxiv.org/html/2311.09799v3"}]

Based on the search results, here's what I found about the paper with arXiv ID 2311.16822:

## Paper Overview

The paper is titled "Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop" by Martin Briesch and 2 other authors (the co-authors are Dominik Sobania and Franz Rothlauf).

## Key Findings

The self-consuming training loop produces correct outputs, however, the output declines in its diversity depending on the proportion of the used generated data. Fresh data can slow down this decline, but not stop it.

## Research Focus

The paper presents the first study investigating the self-consuming training loop for LLMs. As LLM-generated content cannot be safely distinguished from human-produced content, LLM-generated content is used to train the next generation of LLMs, giving rise to a self-consuming training loop.

## Methodology

The authors propose a novel method based on logic expressions that allows them to unambiguously verify the correctness of LLM-generated content, which is difficult for natural language text.

The paper was submitted on November 28, 2023, with subsequent revisions released on June 17, 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "7c941921-bcc6-4fb1-a76b-8cc2209b87d8",
  "tool_use_result": {
    "query": "briesch 2023 \"self-consuming\" LLM diversity distinct repetition spectral 2311.16822",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Kf9EoZh1YiRcoWBwupqNFP",
        "content": [
          {
            "title": "[2311.16822] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop",
            "url": "https://arxiv.org/abs/2311.16822"
          },
          {
            "title": "[2311.16822v2] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop",
            "url": "https://arxiv.org/abs/2311.16822v2"
          },
          {
            "title": "Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop",
            "url": "https://arxiv.org/html/2311.16822"
          },
          {
            "title": "[Submitted on 28 Nov 2023 (v1), last revised 17 Jun 2024 (this version, v2)]",
            "url": "https://arxiv.org/pdf/2311.16822"
          },
          {
            "title": "LLM Self-Consuming Training Loop Analysis",
            "url": "https://www.emergentmind.com/papers/2311.16822"
          },
          {
            "title": "[2311.16822] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop",
            "url": "https://ar5iv.labs.arxiv.org/html/2311.16822"
          },
          {
            "title": "Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/arXiv:2311.16822"
          },
          {
            "title": "What Matters in LLM-generated Data: Diversity and Its Effect on Model Fine-Tuning",
            "url": "https://arxiv.org/html/2506.19262"
          },
          {
            "title": "Understanding the Repeat Curse in Large Language ...",
            "url": "https://aclanthology.org/2025.findings-acl.406.pdf"
          },
          {
            "title": "How Far Can We Extract Diverse Perspectives from Large Language Models?",
            "url": "https://arxiv.org/html/2311.09799v3"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper with arXiv ID 2311.16822:\n\n## Paper Overview\n\nThe paper is titled \"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\" by Martin Briesch and 2 other authors (the co-authors are Dominik Sobania and Franz Rothlauf).\n\n## Key Findings\n\nThe self-consuming training loop produces correct outputs, however, the output declines in its diversity depending on the proportion of the used generated data. Fresh data can slow down this decline, but not stop it.\n\n## Research Focus\n\nThe paper presents the first study investigating the self-consuming training loop for LLMs. As LLM-generated content cannot be safely distinguished from human-produced content, LLM-generated content is used to train the next generation of LLMs, giving rise to a self-consuming training loop.\n\n## Methodology\n\nThe authors propose a novel method based on logic expressions that allows them to unambiguously verify the correctness of LLM-generated content, which is difficult for natural language text.\n\nThe paper was submitted on November 28, 2023, with subsequent revisions released on June 17, 2024."
    ],
    "durationSeconds": 6.639409303000001
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-18T10:23:18.591Z_

<details><summary>↩ Tool result · `toolu_01HCatbJS8f9zVksQrG8FYEr`</summary>

```text
Web search results for query: ""real data mixing" "diversity collapse" spectral health synthetic training generations language model"

Links: [{"title":"Synthetic Data Generation Using Large Language Models","url":"https://arxiv.org/pdf/2503.14023"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse","url":"https://arxiv.org/html/2404.05090v1"},{"title":"On the Diversity of Synthetic Data and its Impact on Training Large Language Models","url":"https://arxiv.org/html/2410.15226v2"},{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"},{"title":"Synthetic Data Generation Using Large Language Models: Advances in Text and Code","url":"https://arxiv.org/html/2503.14023v2"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text","url":"https://arxiv.org/html/2311.09807v2"},{"title":"Characterizing Model Collapse in Large Language Models Using Semantic Networks and Next-Token Probability","url":"https://arxiv.org/html/2410.12341v2"},{"title":"[2404.05090] How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse","url":"https://arxiv.org/abs/2404.05090"},{"title":"Language-Informed Hyperspectral Image Synthesis for Imbalanced-Small Sample Classification via Semi-Supervised Conditional Diffusion Model","url":"https://arxiv.org/html/2502.19700"},{"title":"What Matters in LLM-generated Data: Diversity and Its Effect on Model Fine-Tuning","url":"https://arxiv.org/html/2506.19262"}]

Based on the search results, I found several highly relevant papers on real data mixing, diversity collapse, and synthetic data training in language models. Here are the key findings:

## Real Data Mixing as a Mitigation Strategy

Mixing synthetic data with real data is a common practice to alleviate model collapse, with maintaining a core of real examples anchoring the model in reality while the synthetic portion provides augmentation. Importantly, the importance of maximizing diversity decreases when synthetic data is mixed with even modest amounts of real data, since the real samples anchor the data distribution and provide natural variety.

## Diversity Collapse Phenomena

Model collapse refers to the deterioration in performance that occurs when new models are trained on synthetic data generated from previously trained models. Model collapse refers to the model's tendency to produce limited or repetitive outputs, and recursive training on synthetic data leads to a "self-consuming" loop that affects linguistic diversity.

## Spectral Health and Synthetic Mixtures

Recent theoretical work analyzes what happens when synthetic and real data are mixed. One ICLR 2025 paper examines "what happens when the synthetic data and real data are strategically mixed during training," using spectral analysis methods to understand the dynamics of model collapse in this mixed setting.

## Diversity in Synthetic Data Generation

Mixing up the synthetic data generated by different base LLMs can also slightly improve diversity, leading to better performance, and results suggest that the use of synthetic data from more advanced models and mixed models can be potentially beneficial in practice.

The research consistently shows that maintaining real data in training mixtures is critical for preventing diversity collapse across successive generations of language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "c8c221be-90f8-46a9-9c47-55f6473f4d3b",
  "tool_use_result": {
    "query": "\"real data mixing\" \"diversity collapse\" spectral health synthetic training generations language model",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FAXGVy1S7vvG2m8ZsSggCV",
        "content": [
          {
            "title": "Synthetic Data Generation Using Large Language Models",
            "url": "https://arxiv.org/pdf/2503.14023"
          },
          {
            "title": "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse",
            "url": "https://arxiv.org/html/2404.05090v1"
          },
          {
            "title": "On the Diversity of Synthetic Data and its Impact on Training Large Language Models",
            "url": "https://arxiv.org/html/2410.15226v2"
          },
          {
            "title": "Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"
          },
          {
            "title": "Synthetic Data Generation Using Large Language Models: Advances in Text and Code",
            "url": "https://arxiv.org/html/2503.14023v2"
          },
          {
            "title": "The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text",
            "url": "https://arxiv.org/html/2311.09807v2"
          },
          {
            "title": "Characterizing Model Collapse in Large Language Models Using Semantic Networks and Next-Token Probability",
            "url": "https://arxiv.org/html/2410.12341v2"
          },
          {
            "title": "[2404.05090] How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse",
            "url": "https://arxiv.org/abs/2404.05090"
          },
          {
            "title": "Language-Informed Hyperspectral Image Synthesis for Imbalanced-Small Sample Classification via Semi-Supervised Conditional Diffusion Model",
            "url": "https://arxiv.org/html/2502.19700"
          },
          {
            "title": "What Matters in LLM-generated Data: Diversity and Its Effect on Model Fine-Tuning",
            "url": "https://arxiv.org/html/2506.19262"
          }
        ]
      },
      "Based on the search results, I found several highly relevant papers on real data mixing, diversity collapse, and synthetic data training in language models. Here are the key findings:\n\n## Real Data Mixing as a Mitigation Strategy\n\nMixing synthetic data with real data is a common practice to alleviate model collapse, with maintaining a core of real examples anchoring the model in reality while the synthetic portion provides augmentation. Importantly, the importance of maximizing diversity decreases when synthetic data is mixed with even modest amounts of real data, since the real samples anchor the data distribution and provide natural variety.\n\n## Diversity Collapse Phenomena\n\nModel collapse refers to the deterioration in performance that occurs when new models are trained on synthetic data generated from previously trained models. Model collapse refers to the model's tendency to produce limited or repetitive outputs, and recursive training on synthetic data leads to a \"self-consuming\" loop that affects linguistic diversity.\n\n## Spectral Health and Synthetic Mixtures\n\nRecent theoretical work analyzes what happens when synthetic and real data are mixed. One ICLR 2025 paper examines \"what happens when the synthetic data and real data are strategically mixed during training,\" using spectral analysis methods to understand the dynamics of model collapse in this mixed setting.\n\n## Diversity in Synthetic Data Generation\n\nMixing up the synthetic data generated by different base LLMs can also slightly improve diversity, leading to better performance, and results suggest that the use of synthetic data from more advanced models and mixed models can be potentially beneficial in practice.\n\nThe research consistently shows that maintaining real data in training mixtures is critical for preventing diversity collapse across successive generations of language models."
    ],
    "durationSeconds": 19.180484778000004
  }
}
```

</details>

---

### Assistant

_source line 36_

<details><summary>Logged reasoning block</summary>

```text
Key findings so far:

1. **SIGMA (gu2026sigma)**: The paper DOES report distinct-2 and hashed n-gram HHI as "operational sanity checks" alongside their spectral bounds. However, the search results suggest they use these as validation that spectral metrics align with diversity metrics, not to investigate divergence between them. They position these diversity metrics as "noisy" surface-level proxies. This is a critical finding - they seem to assume alignment, not divergence.

2. **gerstgrasser2024inevitable**: Focuses on accumulation strategy, uses test error (perplexity/loss) as primary metric. 

3. **dohmatob2025strong**: Uses operator-valued free probability theory and focuses on test error scaling laws without mentioning diversity metrics like distinct-n or self-BLEU—purely theoretical and spectral in approach.

4. **briesch2023entropy**: Documents diversity decline in self-consuming loops but doesn't perform spectral analysis, staying focused on diversity alone.

5. **No paper found** that explicitly reports a divergence between spectral metrics (effective rank, SLV) and diversity metrics (distinct-n) in model collapse scenarios with data mixing.

Let me dig deeper into the SIGMA HTML paper to see what else they're measuring.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "b03d2b4a-c4aa-49d0-a8da-3725ae01dd48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017DcDAT9sFjD3asaeVyAn4i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 823,
      "cache_creation_input_tokens": 2431,
      "cache_read_input_tokens": 39154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2431
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

_source line 37_

最后一组搜索确认是否有论文讨论 representation-level vs output-level metrics 的 divergence。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "256d5726-58ea-4d63-89d4-808c10edcaa9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017DcDAT9sFjD3asaeVyAn4i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 823,
      "cache_creation_input_tokens": 2431,
      "cache_read_input_tokens": 39154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2431
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_014xyxGrPoGNMRSgfSybQjjm`</summary>

```json
{
  "query": "SIGMA arxiv 2601.03385 \"distinct-2\" OR \"distinct-n\" spectral divergence diversity collapse generations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "687c1d40-d6ee-43b2-8a04-c36a37d4b713",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017DcDAT9sFjD3asaeVyAn4i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 823,
      "cache_creation_input_tokens": 2431,
      "cache_read_input_tokens": 39154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2431
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D4ZqRETME26AXA9XpDoZT4`</summary>

```json
{
  "query": "\"representation collapse\" vs \"output diversity\" language model training metrics diverge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "4b36134d-6b72-45ff-a029-1a44f4e8baca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017DcDAT9sFjD3asaeVyAn4i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 823,
      "cache_creation_input_tokens": 2431,
      "cache_read_input_tokens": 39154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2431
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

_source line 40 · 2026-05-18T10:23:39.022Z_

<details><summary>↩ Tool result · `toolu_014xyxGrPoGNMRSgfSybQjjm`</summary>

```text
Web search results for query: "SIGMA arxiv 2601.03385 "distinct-2" OR "distinct-n" spectral divergence diversity collapse generations"

Links: [{"title":"[2601.03385] SIGMA: Scalable Spectral Insights for LLM Model Collapse","url":"https://arxiv.org/abs/2601.03385"},{"title":"Sigma: Scalable Spectral Insights for LLM Model Collapse","url":"https://arxiv.org/html/2601.03385"},{"title":"Sigma: Scalable Spectral Insights for LLM Collapse","url":"https://arxiv.org/html/2601.03385v1"},{"title":"SIGMA: Scalable Spectral Insights for LLM Model Collapse","url":"https://www.arxiv.org/pdf/2601.03385"},{"title":"The Homogeneity Trap: Spectral Collapse in Doubly-Stochastic Deep Networks","url":"https://arxiv.org/html/2601.02080v1"},{"title":"The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward","url":"https://arxiv.org/html/2509.07430v2"},{"title":"[2601.02080] The Homogeneity Trap: Spectral Collapse in Doubly-Stochastic Deep Networks","url":"https://arxiv.org/abs/2601.02080"},{"title":"[2601.12401] Beyond the Dirac Delta: Mitigating Diversity Collapse in Reinforcement Fine-Tuning for Versatile Image Generation","url":"https://arxiv.org/abs/2601.12401"},{"title":"Beyond the Dirac Delta: Mitigating Diversity Collapse in Reinforcement Fine-Tuning for Versatile Image Generation","url":"https://arxiv.org/html/2601.12401v1"},{"title":"It’s Never Too Late: Noise Optimization for Collapse Recovery in Trained Diffusion Models","url":"https://arxiv.org/html/2601.00090"}]

Based on the search results, I found the paper you're looking for. SIGMA (Spectral Inequalities for Gram Matrix Analysis) is a unified framework that benchmarks model collapse through the spectral lens of the embedding Gram matrix.

The paper examines model collapse in large language models across multiple generations. The empirical analysis reveals a critical distinction between data-only recursion and true recursion with weight carryover, where while data recursion induces gradual drift, the compounding effect of weight updates accelerates geometric contraction by orders of magnitude.

Regarding the evaluation methodology, the evaluation prompt bank is categorized by prompt type (creative, divergent, analogy/ELI5, what-if, neutral), allowing researchers to attribute model collapse to particular regimes while holding the evaluation framework constant over time, helping answer whether collapse is uniformly distributed across prompt types or concentrated where the model is pushed into higher-entropy regimes.

The paper also employs a spectral monitoring approach: The divergence between a conservative deterministic envelope (Track I) and a sensitive stochastic scaling metric (Track II) serves as a diagnostic signature for early-stage collapse, often preceding surface-level repetition artifacts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "94499534-ea51-4e0d-81e5-0170ac3f4d05",
  "tool_use_result": {
    "query": "SIGMA arxiv 2601.03385 \"distinct-2\" OR \"distinct-n\" spectral divergence diversity collapse generations",
    "results": [
      {
        "tool_use_id": "srvtoolu_017X2NSdcqTnqztQViBQdaxd",
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
            "url": "https://www.arxiv.org/pdf/2601.03385"
          },
          {
            "title": "The Homogeneity Trap: Spectral Collapse in Doubly-Stochastic Deep Networks",
            "url": "https://arxiv.org/html/2601.02080v1"
          },
          {
            "title": "The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward",
            "url": "https://arxiv.org/html/2509.07430v2"
          },
          {
            "title": "[2601.02080] The Homogeneity Trap: Spectral Collapse in Doubly-Stochastic Deep Networks",
            "url": "https://arxiv.org/abs/2601.02080"
          },
          {
            "title": "[2601.12401] Beyond the Dirac Delta: Mitigating Diversity Collapse in Reinforcement Fine-Tuning for Versatile Image Generation",
            "url": "https://arxiv.org/abs/2601.12401"
          },
          {
            "title": "Beyond the Dirac Delta: Mitigating Diversity Collapse in Reinforcement Fine-Tuning for Versatile Image Generation",
            "url": "https://arxiv.org/html/2601.12401v1"
          },
          {
            "title": "It’s Never Too Late: Noise Optimization for Collapse Recovery in Trained Diffusion Models",
            "url": "https://arxiv.org/html/2601.00090"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. SIGMA (Spectral Inequalities for Gram Matrix Analysis) is a unified framework that benchmarks model collapse through the spectral lens of the embedding Gram matrix.\n\nThe paper examines model collapse in large language models across multiple generations. The empirical analysis reveals a critical distinction between data-only recursion and true recursion with weight carryover, where while data recursion induces gradual drift, the compounding effect of weight updates accelerates geometric contraction by orders of magnitude.\n\nRegarding the evaluation methodology, the evaluation prompt bank is categorized by prompt type (creative, divergent, analogy/ELI5, what-if, neutral), allowing researchers to attribute model collapse to particular regimes while holding the evaluation framework constant over time, helping answer whether collapse is uniformly distributed across prompt types or concentrated where the model is pushed into higher-entropy regimes.\n\nThe paper also employs a spectral monitoring approach: The divergence between a conservative deterministic envelope (Track I) and a sensitive stochastic scaling metric (Track II) serves as a diagnostic signature for early-stage collapse, often preceding surface-level repetition artifacts."
    ],
    "durationSeconds": 7.135988010000001
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-18T10:23:39.552Z_

<details><summary>↩ Tool result · `toolu_01D4ZqRETME26AXA9XpDoZT4`</summary>

```text
Web search results for query: ""representation collapse" vs "output diversity" language model training metrics diverge"

Links: [{"title":"[2604.16027] Where does output diversity collapse in post-training?","url":"https://arxiv.org/abs/2604.16027"},{"title":"AI models collapse when trained on recursively generated data | Nature","url":"https://www.nature.com/articles/s41586-024-07566-y"},{"title":"Preprint. Under review. Where does output diversity collapse in post-training?","url":"https://arxiv.org/pdf/2604.16027"},{"title":"Paper page - Where does output diversity collapse in post-training?","url":"https://huggingface.co/papers/2604.16027"},{"title":"Where does output diversity collapse in post-training?","url":"https://arxiv.org/html/2604.16027v1"},{"title":"The Price of Format: Diversity Collapse in LLMs","url":"https://arxiv.org/html/2505.18949v1"},{"title":"LLM Collapse Explained - Igor Oseledko","url":"https://www.igoroseledko.com/llm-model-collapse-explained/"},{"title":"Epistemic diversity across language models mitigates knowledge collapse","url":"https://arxiv.org/html/2512.15011v2"},{"title":"Model collapse - Wikipedia","url":"https://en.wikipedia.org/wiki/Model_collapse"},{"title":"ATTRIBUTING MODE COLLAPSE IN THE FINE-TUNING","url":"https://openreview.net/pdf?id=3pDMYjpOxk"}]

Based on the web search results, here's what I found about representation collapse versus output diversity in language model training metrics:

## Key Findings

Post-trained language models produce less varied outputs than their base counterparts, with this output diversity collapse undermining inference-time scaling methods that rely on varied samples and risking homogenization of model outputs on creative and value-laden tasks.

### How These Metrics Diverge

The research reveals an important distinction between different types of diversity metrics:

Distributional diversity captures statistical spread along lexical, semantic, and logical axes, but this is not a sufficient condition for representational diversity, which is the presence of outputs reflecting different perspectives or stances.

Aligned models can maintain varied vocabulary and phrasing while experiencing semantic diversity drops—for example, in one study, semantic diversity fell from 0.54 to 0.20, while external appearance diversity rose from 0.23 to 0.80.

### Root Causes

Research traces output diversity collapse through parallel post-training lineages across 15 tasks and four text diversity metrics, finding that the location of collapse co-varies with data composition, with the chain-of-thought lineage losing most semantic diversity at supervised fine-tuning.

### Critical Finding

Diversity collapse is determined during training by data composition and cannot be addressed at inference time alone. This suggests that the divergence between representation and output diversity metrics reflects fundamental training dynamics rather than generation-time factors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "3f7e7bff-faad-4619-bfc8-214b60f3b025",
  "tool_use_result": {
    "query": "\"representation collapse\" vs \"output diversity\" language model training metrics diverge",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TgygBVG6curUzdH8L2b8aD",
        "content": [
          {
            "title": "[2604.16027] Where does output diversity collapse in post-training?",
            "url": "https://arxiv.org/abs/2604.16027"
          },
          {
            "title": "AI models collapse when trained on recursively generated data | Nature",
            "url": "https://www.nature.com/articles/s41586-024-07566-y"
          },
          {
            "title": "Preprint. Under review. Where does output diversity collapse in post-training?",
            "url": "https://arxiv.org/pdf/2604.16027"
          },
          {
            "title": "Paper page - Where does output diversity collapse in post-training?",
            "url": "https://huggingface.co/papers/2604.16027"
          },
          {
            "title": "Where does output diversity collapse in post-training?",
            "url": "https://arxiv.org/html/2604.16027v1"
          },
          {
            "title": "The Price of Format: Diversity Collapse in LLMs",
            "url": "https://arxiv.org/html/2505.18949v1"
          },
          {
            "title": "LLM Collapse Explained - Igor Oseledko",
            "url": "https://www.igoroseledko.com/llm-model-collapse-explained/"
          },
          {
            "title": "Epistemic diversity across language models mitigates knowledge collapse",
            "url": "https://arxiv.org/html/2512.15011v2"
          },
          {
            "title": "Model collapse - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Model_collapse"
          },
          {
            "title": "ATTRIBUTING MODE COLLAPSE IN THE FINE-TUNING",
            "url": "https://openreview.net/pdf?id=3pDMYjpOxk"
          }
        ]
      },
      "Based on the web search results, here's what I found about representation collapse versus output diversity in language model training metrics:\n\n## Key Findings\n\nPost-trained language models produce less varied outputs than their base counterparts, with this output diversity collapse undermining inference-time scaling methods that rely on varied samples and risking homogenization of model outputs on creative and value-laden tasks.\n\n### How These Metrics Diverge\n\nThe research reveals an important distinction between different types of diversity metrics:\n\nDistributional diversity captures statistical spread along lexical, semantic, and logical axes, but this is not a sufficient condition for representational diversity, which is the presence of outputs reflecting different perspectives or stances.\n\nAligned models can maintain varied vocabulary and phrasing while experiencing semantic diversity drops—for example, in one study, semantic diversity fell from 0.54 to 0.20, while external appearance diversity rose from 0.23 to 0.80.\n\n### Root Causes\n\nResearch traces output diversity collapse through parallel post-training lineages across 15 tasks and four text diversity metrics, finding that the location of collapse co-varies with data composition, with the chain-of-thought lineage losing most semantic diversity at supervised fine-tuning.\n\n### Critical Finding\n\nDiversity collapse is determined during training by data composition and cannot be addressed at inference time alone. This suggests that the divergence between representation and output diversity metrics reflects fundamental training dynamics rather than generation-time factors."
    ],
    "durationSeconds": 7.190588866000006
  }
}
```

</details>

---

### Assistant

_source line 42_

<details><summary>Logged reasoning block</summary>

```text
Excellent! I now have enough information to write the report. Let me synthesize the findings:

**Key findings:**

1. **SIGMA (gu2026sigma)**: They DO report distinct-2 and hashed n-gram HHI as "operational sanity checks" alongside their spectral Gram matrix bounds. They describe the divergence between deterministic and stochastic spectral bounds as a diagnostic. But critically, they treat diversity metrics as "noisy" surface-level proxies and focus on spectral geometry. They don't explicitly investigate the scenario where spectral metrics show health while diversity metrics collapse (our exp_004 finding). 

They seem to assume spectral contraction and diversity loss move together, which our findings challenge.

2. **gerstgrasser2024inevitable**: Focuses on test error (perplexity/cross-entropy loss). No distinct-n or diversity metrics reported. They show accumulation prevents test error increase but don't track diversity.

3. **dohmatob2025strong**: Purely theoretical, uses operator-valued free probability. Focuses on test error scaling laws. No diversity metrics.

4. **briesch2023entropy**: Reports diversity decline but no spectral analysis. Diversity-only paper.

5. **No paper explicitly reports** the divergence between spectral metrics (eff_rank, log_det staying healthy) and diversity metrics (distinct-n collapsing).

6. Found a related paper on diversity collapse in post-training that shows different diversity metrics can diverge, though it's in a different context (RLHF rather than recursive synthetic training).

7. **alemohammad2024mad** uses FID and diversity metrics for images, not language models.

The specific observation that spectral metrics remain healthy while output diversity crashes under fixed real-synthetic mixing appears to be novel and unreported in the literature. SIGMA comes closest but assumes these metrics correlate, whereas our results directly contradict that assumption. Now I'm ready to write up the report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "86b42323-6dfe-4dd7-b74e-aaf5d050baca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JjtKWQhTnJLLV4VXcoGZ2Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2918,
      "cache_read_input_tokens": 41585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2918
      },
      "output_tokens": 31,
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

_source line 43_

调研完成，写报告。

---

## 文献调研报告：Spectral vs Diversity Metrics Divergence

### A) 文献中是否已有关于 spectral vs diversity divergence 的讨论

**No — 没有论文直接报告过 spectral metrics（effective rank, SLV）在 real-data mixing 下保持健康而 diversity metrics（distinct-n）同时崩溃的现象。**

最接近的是：

- **SIGMA (gu2026sigma, 2601.03385)**：报告了 distinct-2 和 hashed n-gram HHI 作为"operational sanity check"，但将其定位为 spectral bounds 的**验证手段**，暗含假设两者相关。论文未研究 data mixing 场景，也未报告两类指标的 divergence。
- **"Where does output diversity collapse in post-training?" (arXiv 2604.16027, Apr 2026)**：发现 post-training 中 semantic diversity 与 lexical diversity 可以反向运动（semantic diversity 从 0.54 降到 0.20，而 lexical diversity 从 0.23 升到 0.80）。概念上相关，但场景完全不同（RLHF post-training，非 recursive synthetic training）。

### B) 与我们发现的对比

- **Gerstgrasser et al. (2404.01413)**：证明 data accumulation 能稳定 test error，但**未报告 diversity metrics**。我们的 exp_004 补充了关键一环：固定 r=0.5 mixing 虽然保住了 spectral health，但 distinct-4 暴跌 86%，说明 test error 稳定 ≠ output diversity 稳定。
- **Dohmatob et al. (2410.04840)**：纯理论分析，用 operator-valued free probability 推导 test error scaling，**无 diversity 讨论**。
- **Briesch et al. (2311.16822)**：报告了 self-consuming loop 中 diversity 下降，但**无 spectral 分析**。正好是我们发现的反面视角。

### C) 是否可作为额外 contribution

**是的。** 这是一个有价值的 novel observation：

> Spectral metrics (effective rank, log determinant) can be "blind" to diversity collapse when real data mixing stabilizes the representation geometry but fails to prevent mode narrowing in output space.

这直接挑战了 SIGMA 等工作中 spectral metrics 作为 collapse 充分检测器的隐含假设。可以作为论文 Discussion 中的重要 finding，论证 spectral EWS 需要与 output-level diversity metrics 配合使用。

### D) 建议补充到 literature_map.yaml 的论文

1. **"Where does output diversity collapse in post-training?"** — arXiv 2604.16027 (Apr 2026), 研究 diversity metrics 之间的 divergence，概念上与我们的 spectral-diversity divergence 发现互补。建议加入 `synthetic_data_quality` cluster。

其余搜索未发现需要新增的直接相关论文。现有 literature_map 覆盖已较完整。

---

需要我将这个发现更新到 `literature_map.yaml` 或 `report.md` 中吗？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "uuid": "0cc8c727-44e7-4479-8478-8f3bd9f83e70",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JjtKWQhTnJLLV4VXcoGZ2Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2918,
      "cache_read_input_tokens": 41585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2918
      },
      "output_tokens": 31,
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

调研完成，写报告。

---

## 文献调研报告：Spectral vs Diversity Metrics Divergence

### A) 文献中是否已有关于 spectral vs diversity divergence 的讨论

**No — 没有论文直接报告过 spectral metrics（effective rank, SLV）在 real-data mixing 下保持健康而 diversity metrics（distinct-n）同时崩溃的现象。**

最接近的是：

- **SIGMA (gu2026sigma, 2601.03385)**：报告了 distinct-2 和 hashed n-gram HHI 作为"operational sanity check"，但将其定位为 spectral bounds 的**验证手段**，暗含假设两者相关。论文未研究 data mixing 场景，也未报告两类指标的 divergence。
- **"Where does output diversity collapse in post-training?" (arXiv 2604.16027, Apr 2026)**：发现 post-training 中 semantic diversity 与 lexical diversity 可以反向运动（semantic diversity 从 0.54 降到 0.20，而 lexical diversity 从 0.23 升到 0.80）。概念上相关，但场景完全不同（RLHF post-training，非 recursive synthetic training）。

### B) 与我们发现的对比

- **Gerstgrasser et al. (2404.01413)**：证明 data accumulation 能稳定 test error，但**未报告 diversity metrics**。我们的 exp_004 补充了关键一环：固定 r=0.5 mixing 虽然保住了 spectral health，但 distinct-4 暴跌 86%，说明 test error 稳定 ≠ output diversity 稳定。
- **Dohmatob et al. (2410.04840)**：纯理论分析，用 operator-valued free probability 推导 test error scaling，**无 diversity 讨论**。
- **Briesch et al. (2311.16822)**：报告了 self-consuming loop 中 diversity 下降，但**无 spectral 分析**。正好是我们发现的反面视角。

### C) 是否可作为额外 contribution

**是的。** 这是一个有价值的 novel observation：

> Spectral metrics (effective rank, log determinant) can be "blind" to diversity collapse when real data mixing stabilizes the representation geometry but fails to prevent mode narrowing in output space.

这直接挑战了 SIGMA 等工作中 spectral metrics 作为 collapse 充分检测器的隐含假设。可以作为论文 Discussion 中的重要 finding，论证 spectral EWS 需要与 output-level diversity metrics 配合使用。

### D) 建议补充到 literature_map.yaml 的论文

1. **"Where does output diversity collapse in post-training?"** — arXiv 2604.16027 (Apr 2026), 研究 diversity metrics 之间的 divergence，概念上与我们的 spectral-diversity divergence 发现互补。建议加入 `synthetic_data_quality` cluster。

其余搜索未发现需要新增的直接相关论文。现有 literature_map 覆盖已较完整。

---

需要我将这个发现更新到 `literature_map.yaml` 或 `report.md` 中吗？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 113436,
  "duration_api_ms": 179847,
  "num_turns": 16,
  "stop_reason": "end_turn",
  "session_id": "ee5a3915-7a38-48ba-ad5e-2370933f59b6",
  "total_cost_usd": 0.7667839999999999,
  "usage": {
    "input_tokens": 3796,
    "cache_creation_input_tokens": 32662,
    "cache_read_input_tokens": 176973,
    "output_tokens": 3107,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 32662,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1447,
        "cache_read_input_tokens": 41585,
        "cache_creation_input_tokens": 2918,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2918
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 217340,
      "outputTokens": 6033,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 13,
      "costUSD": 0.37750500000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 3796,
      "outputTokens": 3107,
      "cacheReadInputTokens": 176973,
      "cacheCreationInputTokens": 32662,
      "webSearchRequests": 0,
      "costUSD": 0.38927900000000004,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "f9a5230e-6671-4176-a6fb-d484e81a0a63"
}
```

</details>

---
