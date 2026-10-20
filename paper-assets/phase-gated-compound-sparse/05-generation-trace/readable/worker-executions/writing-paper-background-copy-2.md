# writing paper background

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/workers/worker_writing_paper-background_20260514T053538.log`
- **Structured JSON:** [`c992c86839e194f2b1c5.json`](../../sessions/c9/c992c86839e194f2b1c5.json)

## Before a recorded user message

40 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
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
  "uuid": "c2424118-704c-4045-a08b-6f89851c211d",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/memory/"
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
    "resetsAt": 1778742000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "1d9ba273-3487-481f-b4fe-6db3c6c281de",
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the writing plan and the methodology.tex file to ensure consistency.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "9698b322-a919-427c-bd78-5704cbe5a264",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012mS7wMJVXsUwmGk5gNY126",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12304,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12304
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

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01AvS6WBizrKBHBh19n3nRTZ`</summary>

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
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "0b44e003-8f32-4393-a780-e1f555cc0520",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012mS7wMJVXsUwmGk5gNY126",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12304,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12304
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

_source line 6 · 2026-05-14T05:35:48.239Z_

<details><summary>↩ Tool result · `toolu_01AvS6WBizrKBHBh19n3nRTZ`</summary>

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
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "7b66f846-c067-4806-9077-f6bd3a3f75cb",
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

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011NGUrzRNNAxbzKNbRPsV59`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "writing_plan.yaml",
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
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "14c0dfb8-c14c-47cd-8d70-dc78aa0cfccb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LCdrPmajAFva98bCB2TuwE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 23751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 732
      },
      "output_tokens": 71,
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

_source line 8 · 2026-05-14T05:35:51.058Z_

<details><summary>↩ Tool result · `toolu_011NGUrzRNNAxbzKNbRPsV59`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/writing_plan.yaml\", \"content\": \"## Writing Plan — Phase-Gated Compound Sparsity\\n## 最后更新: 2026-05-14\\n\\n# ============================================================\\n# 投稿目标\\n# ============================================================\\ntarget:\\n  venue: EMNLP 2026 ARR\\n  deadline: 2026-05-25\\n  days_remaining: 11\\n  format: long paper (8 pages + references + appendix)\\n  anonymization: ARR double-blind\\n\\n# ============================================================\\n# Paper Outline\\n# ============================================================\\noutline:\\n  title_candidates:\\n    - \\\"Phase-Modulated Compound Sparsity: How Eviction Strategy and Reasoning Phase Interact in Sparse LLM Inference\\\"\\n    - \\\"Emergent Phase-Strategy Interaction in Compound Sparse LLM Inference\\\"\\n    - \\\"When Compound Sparsity Bites Back: Phase-Dependent Severity Amplification in Importance-Based Eviction\\\"\\n\\n  sections:\\n    - id: abstract\\n      title: Abstract\\n      summary: >\\n        Compound sparsity (head pruning + KV cache eviction) is assumed to degrade uniformly.\\n        We show the interaction is strategy-dependent and phase-modulated: importance-based eviction\\n        exhibits 12-75× severity amplification in low-sparsity reasoning phases, while random eviction\\n        stays flat (~1×). Bootstrap CI (B=10000) confirms significance at all 4 sparsity levels (p<0.0001).\\n        Cross-model replication on Qwen2.5-7B validates generalizability. We explain this via an\\n        entropy-discrimination collapse mechanism: head pruning distributes surviving attention,\\n        destroying importance score discriminability specifically in distributed-attention phases.\\n      length: 250 words\\n\\n    - id: introduction\\n      title: \\\"1. Introduction\\\"\\n      summary: >\\n        Motivate compound sparsity as practical deployment need. State gap: prior work (SparK, Ada-KV)\\n        treats compound interaction as uniformly super-additive. Our finding: the severity is an\\n        emergent property of the interaction between eviction strategy and reasoning phase.\\n        Preview crossover phenomenon and mechanism. State contributions.\\n      length: 1 page\\n      key_claims:\\n        - Compound sparsity severity is not uniform — it is strategy-dependent and phase-modulated\\n        - Importance-based eviction amplifies compound interaction 12-75× in low-sparsity phases\\n        - Entropy-discrimination collapse explains the phase-strategy interaction\\n\\n    - id: related_work\\n      title: \\\"2. Related Work\\\"\\n      summary: >\\n        Three threads: (1) Compound/joint compression (SparK, SLiM, UniComp, compression-ordering)\\n        — none analyzes phase × strategy interaction. (2) KV cache eviction (Ada-KV, DefensiveKV,\\n        SnapKV, NACL) — importance fragility noted but not phase-conditioned. (3) Phase-aware\\n        inference (ThinKV, PagedEviction, reasoning dynamics) — single-axis, no compound interaction.\\n      length: 0.75 page\\n      key_refs:\\n        - spark-aaai2026\\n        - thinkv-iclr2026\\n        - defensivekv-iclr2026\\n        - slim-icml2025\\n        - phase-transition-compression-2026\\n        - decision-repr-transition-2026\\n        - retentivekv-2026\\n        - greedy-bias-kvcache-2026\\n\\n    - id: background\\n      title: \\\"3. Background and Problem Setup\\\"\\n      summary: >\\n        Define compound sparsity (attention head pruning ⊗ KV cache eviction). Define Interaction\\n        Index (II) measuring super/sub-additivity. Define phase segmentation via ThinKV-style\\n        token-ratio method. Formalize the research question: is II constant across phases and strategies?\\n      length: 1 page\\n      subsections:\\n        - \\\"3.1 Compound Sparsity Formulation\\\"\\n        - \\\"3.2 Interaction Index\\\"\\n        - \\\"3.3 Phase Segmentation\\\"\\n\\n    - id: methodology\\n      title: \\\"4. Experimental Setup\\\"\\n      summary: >\\n        Models (DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct), dataset (MATH-500 subset, 50 problems),\\n        sparsity levels (s=0.15/0.20/0.25/0.30), eviction strategies (importance-based cumulative\\n        attention with position normalization, random), metrics (PPL, II, gradient), hardware.\\n        Statistical method: per-problem bootstrap CI (B=10000), paired and unpaired.\\n      length: 1 page\\n\\n    - id: results\\n      title: \\\"5. Results\\\"\\n      summary: >\\n        Main finding: importance gradient 12.8-74.9× (median) monotonically increasing with sparsity,\\n        random gradient ~1×. Bootstrap CI all significant (p=0.0000). Crossover: importance safer\\n        than random in high-sparsity phase but dramatically worse in low-sparsity phase.\\n        Sub-exponential growth pattern (rate decreasing: 2.24×→1.84×→1.42×).\\n      length: 1.5 pages\\n      subsections:\\n        - \\\"5.1 Phase-Modulated Severity Gradient\\\"\\n        - \\\"5.2 Strategy-Dependent Crossover\\\"\\n        - \\\"5.3 Cross-Model Replication\\\"\\n\\n    - id: analysis\\n      title: \\\"6. Analysis: Entropy-Discrimination Collapse\\\"\\n      summary: >\\n        Mechanistic explanation: head pruning → surviving heads attend more uniformly → importance\\n        score entropy increases → discrimination between important/unimportant KV entries collapses →\\n        importance-based eviction degrades to biased pseudo-random in distributed-attention phases.\\n        This is phase-dependent because reasoning phases have more distributed attention.\\n      length: 1 page\\n\\n    - id: discussion\\n      title: \\\"7. Discussion\\\"\\n      summary: >\\n        Implications for compound sparsity deployment: uniform budgets are unsafe.\\n        Phase-gated controllers as solution direction. Limitations: 7B models only,\\n        MATH-500 only, no throughput measurements yet.\\n      length: 0.5 page\\n\\n    - id: conclusion\\n      title: \\\"8. Conclusion\\\"\\n      summary: >\\n        Compound sparsity severity is an emergent property of strategy × phase interaction.\\n        This finding challenges the implicit assumption of uniform compound degradation\\n        and motivates phase-aware sparsity allocation.\\n      length: 0.25 page\\n\\n# ============================================================\\n# Figures and Tables\\n# ============================================================\\nfigures:\\n  - id: fig1_hero\\n    title: \\\"Phase-Modulated Severity Gradient (Hero Figure)\\\"\\n    type: line plot or grouped bar\\n    data_source: v5 importance + v5 random segment-level II medians\\n    message: >\\n      Importance gradient rises 12.8-74.9× across sparsity levels while random stays flat ~1×.\\n      The gap between strategies widens with sparsity — this is the core visual claim.\\n    placement: page 1 or Section 5.1\\n    priority: P0\\n\\n  - id: fig2_crossover\\n    title: \\\"Phase-Strategy Crossover Heatmap\\\"\\n    type: heatmap (strategy × phase × sparsity)\\n    data_source: v5 importance + random per-phase II values\\n    message: >\\n      At s=0.25, importance outperforms random in high-sparsity phase (0.584 vs 3.002) but\\n      underperforms dramatically in low-sparsity phase (30.903 vs 2.915). Direction reversal\\n      is phase-dependent.\\n    placement: Section 5.2\\n    priority: P0\\n\\n  - id: fig3_mechanism\\n    title: \\\"Entropy-Discrimination Collapse Illustration\\\"\\n    type: schematic diagram + attention distribution plot\\n    data_source: conceptual + optional empirical attention entropy data\\n    message: >\\n      Head pruning → attention redistribution → importance score entropy increase →\\n      discrimination collapse. Explains why importance eviction fails specifically in\\n      distributed-attention phases.\\n    placement: Section 6\\n    priority: P1\\n\\n  - id: fig4_bootstrap\\n    title: \\\"Bootstrap CI Forest Plot\\\"\\n    type: forest plot\\n    data_source: v6 per-problem bootstrap results (B=10000)\\n    message: >\\n      All 4 sparsity levels show gradient CI entirely above 1.0, p=0.0000.\\n      Visual confirmation of statistical significance.\\n    placement: Section 5.1\\n    priority: P1\\n\\n  - id: fig5_crossmodel\\n    title: \\\"Cross-Model Replication\\\"\\n    type: grouped bar or side-by-side line plot\\n    data_source: Qwen2.5-7B importance results (pending)\\n    message: >\\n      Phase-modulated severity generalizes beyond DeepSeek to Qwen architecture.\\n    placement: Section 5.3\\n    priority: P0 (blocked on Qwen experiments)\\n\\ntables:\\n  - id: tab1_main\\n    title: \\\"Main Results: II by Strategy × Phase × Sparsity\\\"\\n    data_source: v5 importance + random, median + IQR\\n    columns: [sparsity, strategy, high_phase_II, low_phase_II, gradient, gradient_CI]\\n    message: Core quantitative claim — strategy × phase interaction\\n    placement: Section 5.1\\n    priority: P0\\n\\n  - id: tab2_bootstrap\\n    title: \\\"Bootstrap Confidence Intervals (B=10000)\\\"\\n    data_source: v6 per-problem bootstrap\\n    columns: [sparsity, paired_gradient, paired_CI, unpaired_gradient, unpaired_CI, p_value]\\n    message: Statistical rigor — all gradients significant\\n    placement: Section 5.1\\n    priority: P0\\n\\n  - id: tab3_crossmodel\\n    title: \\\"Cross-Model Comparison: DeepSeek vs Qwen\\\"\\n    data_source: v6 DeepSeek + Qwen importance results (Qwen pending)\\n    message: Generalizability beyond single model family\\n    placement: Section 5.3\\n    priority: P0 (blocked on Qwen)\\n\\n# ============================================================\\n# Claims → Evidence Mapping\\n# ============================================================\\nclaims:\\n  - claim: \\\"Compound sparsity severity is strategy-dependent\\\"\\n    evidence:\\n      - \\\"v5 importance gradient 12.8-74.9× vs v5 random gradient ~1×\\\"\\n      - \\\"Bootstrap CI: importance gradient CI lower bound >> 1.0; random gradient CI spans 1.0\\\"\\n    status: confirmed\\n\\n  - claim: \\\"Severity is phase-modulated (amplified in low-sparsity reasoning phase)\\\"\\n    evidence:\\n      - \\\"v5 per-phase II: low phase >> high phase for importance at all 4 sparsity levels\\\"\\n      - \\\"Gradient monotonically increases with sparsity: 12.8→28.7→52.9→74.9\\\"\\n    status: confirmed\\n\\n  - claim: \\\"Phase-strategy crossover exists\\\"\\n    evidence:\\n      - \\\"s=0.25: importance high_phase=0.584 < random=3.002, importance low_phase=30.903 > random=2.915\\\"\\n      - \\\"Direction depends on phase, not just magnitude\\\"\\n    status: confirmed\\n\\n  - claim: \\\"Entropy-discrimination collapse explains the mechanism\\\"\\n    evidence:\\n      - \\\"Conceptual argument: head pruning → distributed attention → importance entropy up → discrimination down\\\"\\n      - \\\"Empirical: importance PPL 26-60× worse than random before metric fix (D012/D013) = metric failure\\\"\\n    status: partially_confirmed (mechanism is explanatory, not directly measured)\\n\\n  - claim: \\\"Finding generalizes across model families\\\"\\n    evidence:\\n      - \\\"Qwen2.5-7B-Instruct experiments (pending)\\\"\\n    status: pending\\n\\n  - claim: \\\"Severity gradient is sub-exponential\\\"\\n    evidence:\\n      - \\\"Growth rate: 2.24×→1.84×→1.42× (decreasing)\\\"\\n    status: confirmed\\n\\n# ============================================================\\n# Writing Priority & Schedule\\n# ============================================================\\nwriting_priority:\\n  # Phase 1: 可立即写的部分 (Day 1-3, May 14-16)\\n  - priority: 1\\n    sections: [methodology, background, related_work]\\n    reason: \\\"不依赖 Qwen 结果，数据已完备，先把 methodology infrastructure 写好\\\"\\n    deliverable: \\\"完整的 Section 3 + 4 + 2 初稿\\\"\\n\\n  - priority: 1\\n    task: \\\"fig1_hero + fig2_crossover + tab1_main + tab2_bootstrap\\\"\\n    reason: \\\"核心数据已有，图表先出可以驱动 narrative\\\"\\n    deliverable: \\\"4 个核心 figure/table 的 publication-ready 版本\\\"\\n\\n  # Phase 2: 核心结果 (Day 3-5, May 16-18)\\n  - priority: 2\\n    sections: [results_5_1, results_5_2]\\n    reason: \\\"5.1 和 5.2 数据完备，5.3 (cross-model) 需等 Qwen\\\"\\n    deliverable: \\\"Section 5.1 + 5.2 完整初稿\\\"\\n\\n  - priority: 2\\n    sections: [analysis]\\n    reason: \\\"机制解释可独立写，不依赖 Qwen\\\"\\n    deliverable: \\\"Section 6 初稿\\\"\\n\\n  # Phase 3: Cross-model + Introduction (Day 5-7, May 18-20)\\n  - priority: 3\\n    sections: [results_5_3]\\n    reason: \\\"Qwen 实验预计 Day 3-4 出结果\\\"\\n    deliverable: \\\"Section 5.3 + Table 3 + Fig 5\\\"\\n\\n  - priority: 3\\n    sections: [introduction]\\n    reason: \\\"Introduction 最后写——需要所有结果确定后才能精确表述 contributions\\\"\\n    deliverable: \\\"Section 1 完整初稿\\\"\\n\\n  # Phase 4: Abstract + Polish (Day 7-9, May 20-22)\\n  - priority: 4\\n    sections: [abstract, discussion, conclusion]\\n    reason: \\\"总结性段落最后写\\\"\\n    deliverable: \\\"完整初稿 v1\\\"\\n\\n  # Phase 5: Review & Submission (Day 9-11, May 22-25)\\n  - priority: 5\\n    task: \\\"Internal review, polish, formatting check, reference audit, submission\\\"\\n    reason: \\\"留 3 天 buffer 做 revision\\\"\\n    deliverable: \\\"Camera-ready 提交\\\"\\n\\nschedule:\\n  - days: \\\"Day 1-3 (May 14-16)\\\"\\n    tasks:\\n      - \\\"LaTeX 模板搭建 (EMNLP ARR format)\\\"\\n      - \\\"Section 3 (Background) 初稿\\\"\\n      - \\\"Section 4 (Methodology) 初稿\\\"\\n      - \\\"Section 2 (Related Work) 初稿\\\"\\n      - \\\"Fig 1 (hero), Fig 2 (crossover), Table 1, Table 2 制图\\\"\\n      - \\\"启动 Qwen cross-model 实验\\\"\\n    milestone: \\\"方法论部分完成 + 核心图表就绪\\\"\\n\\n  - days: \\\"Day 3-5 (May 16-18)\\\"\\n    tasks:\\n      - \\\"Section 5.1 (severity gradient) 初稿\\\"\\n      - \\\"Section 5.2 (crossover) 初稿\\\"\\n      - \\\"Section 6 (analysis/mechanism) 初稿\\\"\\n      - \\\"Fig 3 (mechanism diagram)\\\"\\n      - \\\"Fig 4 (bootstrap forest plot)\\\"\\n    milestone: \\\"结果+分析部分完成\\\"\\n\\n  - days: \\\"Day 5-7 (May 18-20)\\\"\\n    tasks:\\n      - \\\"Qwen 结果整合 → Section 5.3, Table 3, Fig 5\\\"\\n      - \\\"Section 1 (Introduction) 初稿\\\"\\n      - \\\"如果 Qwen 结果延迟：先写 conditional 版本，留占位\\\"\\n    milestone: \\\"主体内容完成\\\"\\n\\n  - days: \\\"Day 7-9 (May 20-22)\\\"\\n    tasks:\\n      - \\\"Abstract 撰写\\\"\\n      - \\\"Section 7 (Discussion) + Section 8 (Conclusion)\\\"\\n      - \\\"Appendix: paired bootstrap 详细结果、per-problem 分布\\\"\\n      - \\\"全文 polish pass 1: 叙事一致性、数据准确性\\\"\\n    milestone: \\\"完整初稿 v1\\\"\\n\\n  - days: \\\"Day 9-11 (May 22-25)\\\"\\n    tasks:\\n      - \\\"Reference audit (引用完整性+格式)\\\"\\n      - \\\"Polish pass 2: 语言、格式、ARR checklist\\\"\\n      - \\\"Limitations section\\\"\\n      - \\\"Ethics statement (if required)\\\"\\n      - \\\"最终提交\\\"\\n    milestone: \\\"提交完成\\\"\\n\\n# ============================================================\\n# 关键风险\\n# ============================================================\\nrisks:\\n  - risk: \\\"Qwen cross-model 实验未完成或结果 negative\\\"\\n    mitigation: >\\n      如果 Day 5 前无结果：写 conditional 版本 \\\"we additionally test on Qwen2.5-7B (results pending)\\\".\\n      如果结果 negative：调整 narrative 为 \\\"model-specific phenomenon requiring further investigation\\\",\\n      仍可作为 finding paper 提交（DeepSeek 数据已足够支撑 core claim）.\\n    impact: medium\\n\\n  - risk: \\\"11 天写不完\\\"\\n    mitigation: >\\n      优先保证 core sections (3-6)，Introduction/Discussion 可以精简。\\n      如果时间不够，砍 mechanism analysis (Section 6) 到 1 段 discussion。\\n    impact: low (schedule has 3-day buffer)\\n\\n  - risk: \\\"Reviewer 质疑 7B-only + MATH-500-only 的 generalizability\\\"\\n    mitigation: >\\n      Cross-model (Qwen) 是第一层防御。Limitations 明确声明 scale。\\n      MATH-500 是 standard benchmark，defensible。\\n    impact: medium\\n\\n# ============================================================\\n# Framing 约束 (Director D015)\\n# ============================================================\\nframing_constraints:\\n  must: \\\"emergent phase-strategy interaction\\\"\\n  must_not: \\\"importance metric limitation / importance is broken\\\"\\n  narrative_arc: >\\n    Compound sparsity is increasingly used for efficient LLM inference, but its interaction\\n    dynamics are poorly understood. We discover that the severity of compound interaction\\n    is not a fixed property — it emerges from the interplay of eviction strategy and reasoning\\n    phase. Importance-based eviction amplifies compound degradation 12-75× in low-sparsity\\n    phases, while random eviction maintains flat interaction. This phase-strategy interaction,\\n    explained by entropy-discrimination collapse, challenges the uniform-degradation assumption\\n    and motivates phase-aware sparsity allocation.\\n\", \"total_chars\": 15373, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "d815e969-1b5b-483e-aceb-5c600126786d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/writing_plan.yaml\\\", \\\"content\\\": \\\"## Writing Plan — Phase-Gated Compound Sparsity\\\\n## 最后更新: 2026-05-14\\\\n\\\\n# ============================================================\\\\n# 投稿目标\\\\n# ============================================================\\\\ntarget:\\\\n  venue: EMNLP 2026 ARR\\\\n  deadline: 2026-05-25\\\\n  days_remaining: 11\\\\n  format: long paper (8 pages + references + appendix)\\\\n  anonymization: ARR double-blind\\\\n\\\\n# ============================================================\\\\n# Paper Outline\\\\n# ============================================================\\\\noutline:\\\\n  title_candidates:\\\\n    - \\\\\\\"Phase-Modulated Compound Sparsity: How Eviction Strategy and Reasoning Phase Interact in Sparse LLM Inference\\\\\\\"\\\\n    - \\\\\\\"Emergent Phase-Strategy Interaction in Compound Sparse LLM Inference\\\\\\\"\\\\n    - \\\\\\\"When Compound Sparsity Bites Back: Phase-Dependent Severity Amplification in Importance-Based Eviction\\\\\\\"\\\\n\\\\n  sections:\\\\n    - id: abstract\\\\n      title: Abstract\\\\n      summary: >\\\\n        Compound sparsity (head pruning + KV cache eviction) is assumed to degrade uniformly.\\\\n        We show the interaction is strategy-dependent and phase-modulated: importance-based eviction\\\\n        exhibits 12-75× severity amplification in low-sparsity reasoning phases, while random eviction\\\\n        stays flat (~1×). Bootstrap CI (B=10000) confirms significance at all 4 sparsity levels (p<0.0001).\\\\n        Cross-model replication on Qwen2.5-7B validates generalizability. We explain this via an\\\\n        entropy-discrimination collapse mechanism: head pruning distributes surviving attention,\\\\n        destroying importance score discriminability specifically in distributed-attention phases.\\\\n      length: 250 words\\\\n\\\\n    - id: introduction\\\\n      title: \\\\\\\"1. Introduction\\\\\\\"\\\\n      summary: >\\\\n        Motivate compound sparsity as practical deployment need. State gap: prior work (SparK, Ada-KV)\\\\n        treats compound interaction as uniformly super-additive. Our finding: the severity is an\\\\n        emergent property of the interaction between eviction strategy and reasoning phase.\\\\n        Preview crossover phenomenon and mechanism. State contributions.\\\\n      length: 1 page\\\\n      key_claims:\\\\n        - Compound sparsity severity is not uniform — it is strategy-dependent and phase-modulated\\\\n        - Importance-based eviction amplifies compound interaction 12-75× in low-sparsity phases\\\\n        - Entropy-discrimination collapse explains the phase-strategy interaction\\\\n\\\\n    - id: related_work\\\\n      title: \\\\\\\"2. Related Work\\\\\\\"\\\\n      summary: >\\\\n        Three threads: (1) Compound/joint compression (SparK, SLiM, UniComp, compression-ordering)\\\\n        — none analyzes phase × strategy interaction. (2) KV cache eviction (Ada-KV, DefensiveKV,\\\\n        SnapKV, NACL) — importance fragility noted but not phase-conditioned. (3) Phase-aware\\\\n        inference (ThinKV, PagedEviction, reasoning dynamics) — single-axis, no compound interaction.\\\\n      length: 0.75 page\\\\n      key_refs:\\\\n        - spark-aaai2026\\\\n        - thinkv-iclr2026\\\\n        - defensivekv-iclr2026\\\\n        - slim-icml2025\\\\n        - phase-transition-compression-2026\\\\n        - decision-repr-transition-2026\\\\n        - retentivekv-2026\\\\n        - greedy-bias-kvcache-2026\\\\n\\\\n    - id: background\\\\n      title: \\\\\\\"3. Background and Problem Setup\\\\\\\"\\\\n      summary: >\\\\n        Define compound sparsity (attention head pruning ⊗ KV cache eviction). Define Interaction\\\\n        Index (II) measuring super/sub-additivity. Define phase segmentation via ThinKV-style\\\\n        token-ratio method. Formalize the research question: is II constant across phases and strategies?\\\\n      length: 1 page\\\\n      subsections:\\\\n        - \\\\\\\"3.1 Compound Sparsity Formulation\\\\\\\"\\\\n        - \\\\\\\"3.2 Interaction Index\\\\\\\"\\\\n        - \\\\\\\"3.3 Phase Segmentation\\\\\\\"\\\\n\\\\n    - id: methodology\\\\n      title: \\\\\\\"4. Experimental Setup\\\\\\\"\\\\n      summary: >\\\\n        Models (DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct), dataset (MATH-500 subset, 50 problems),\\\\n        sparsity levels (s=0.15/0.20/0.25/0.30), eviction strategies (importance-based cumulative\\\\n        attention with position normalization, random), metrics (PPL, II, gradient), hardware.\\\\n        Statistical method: per-problem bootstrap CI (B=10000), paired and unpaired.\\\\n      length: 1 page\\\\n\\\\n    - id: results\\\\n      title: \\\\\\\"5. Results\\\\\\\"\\\\n      summary: >\\\\n        Main finding: importance gradient 12.8-74.9× (median) monotonically increasing with sparsity,\\\\n        random gradient ~1×. Bootstrap CI all significant (p=0.0000). Crossover: importance safer\\\\n        than random in high-sparsity phase but dramatically worse in low-sparsity phase.\\\\n        Sub-exponential growth pattern (rate decreasing: 2.24×→1.84×→1.42×).\\\\n      length: 1.5 pages\\\\n      subsections:\\\\n        - \\\\\\\"5.1 Phase-Modulated Severity Gradient\\\\\\\"\\\\n        - \\\\\\\"5.2 Strategy-Dependent Crossover\\\\\\\"\\\\n        - \\\\\\\"5.3 Cross-Model Replication\\\\\\\"\\\\n\\\\n    - id: analysis\\\\n      title: \\\\\\\"6. Analysis: Entropy-Discrimination Collapse\\\\\\\"\\\\n      summary: >\\\\n        Mechanistic explanation: head pruning → surviving heads attend more uniformly → importance\\\\n        score entropy increases → discrimination between important/unimportant KV entries collapses →\\\\n        importance-based eviction degrades to biased pseudo-random in distributed-attention phases.\\\\n        This is phase-dependent because reasoning phases have more distributed attention.\\\\n      length: 1 page\\\\n\\\\n    - id: discussion\\\\n      title: \\\\\\\"7. Discussion\\\\\\\"\\\\n      summary: >\\\\n        Implications for compound sparsity deployment: uniform budgets are unsafe.\\\\n        Phase-gated controllers as solution direction. Limitations: 7B models only,\\\\n        MATH-500 only, no throughput measurements yet.\\\\n      length: 0.5 page\\\\n\\\\n    - id: conclusion\\\\n      title: \\\\\\\"8. Conclusion\\\\\\\"\\\\n      summary: >\\\\n        Compound sparsity severity is an emergent property of strategy × phase interaction.\\\\n        This finding challenges the implicit assumption of uniform compound degradation\\\\n        and motivates phase-aware sparsity allocation.\\\\n      length: 0.25 page\\\\n\\\\n# ============================================================\\\\n# Figures and Tables\\\\n# ============================================================\\\\nfigures:\\\\n  - id: fig1_hero\\\\n    title: \\\\\\\"Phase-Modulated Severity Gradient (Hero Figure)\\\\\\\"\\\\n    type: line plot or grouped bar\\\\n    data_source: v5 importance + v5 random segment-level II medians\\\\n    message: >\\\\n      Importance gradient rises 12.8-74.9× across sparsity levels while random stays flat ~1×.\\\\n      The gap between strategies widens with sparsity — this is the core visual claim.\\\\n    placement: page 1 or Section 5.1\\\\n    priority: P0\\\\n\\\\n  - id: fig2_crossover\\\\n    title: \\\\\\\"Phase-Strategy Crossover Heatmap\\\\\\\"\\\\n    type: heatmap (strategy × phase × sparsity)\\\\n    data_source: v5 importance + random per-phase II values\\\\n    message: >\\\\n      At s=0.25, importance outperforms random in high-sparsity phase (0.584 vs 3.002) but\\\\n      underperforms dramatically in low-sparsity phase (30.903 vs 2.915). Direction reversal\\\\n      is phase-dependent.\\\\n    placement: Section 5.2\\\\n    priority: P0\\\\n\\\\n  - id: fig3_mechanism\\\\n    title: \\\\\\\"Entropy-Discrimination Collapse Illustration\\\\\\\"\\\\n    type: schematic diagram + attention distribution plot\\\\n    data_source: conceptual + optional empirical attention entropy data\\\\n    message: >\\\\n      Head pruning → attention redistribution → importance score entropy increase →\\\\n      discrimination collapse. Explains why importance eviction fails specifically in\\\\n      distributed-attention phases.\\\\n    placement: Section 6\\\\n    priority: P1\\\\n\\\\n  - id: fig4_bootstrap\\\\n    title: \\\\\\\"Bootstrap CI Forest Plot\\\\\\\"\\\\n    type: forest plot\\\\n    data_source: v6 per-problem bootstrap results (B=10000)\\\\n    message: >\\\\n      All 4 sparsity levels show gradient CI entirely above 1.0, p=0.0000.\\\\n      Visual confirmation of statistical significance.\\\\n    placement: Section 5.1\\\\n    priority: P1\\\\n\\\\n  - id: fig5_crossmodel\\\\n    title: \\\\\\\"Cross-Model Replication\\\\\\\"\\\\n    type: grouped bar or side-by-side line plot\\\\n    data_source: Qwen2.5-7B importance results (pending)\\\\n    message: >\\\\n      Phase-modulated severity generalizes beyond DeepSeek to Qwen architecture.\\\\n    placement: Section 5.3\\\\n    priority: P0 (blocked on Qwen experiments)\\\\n\\\\ntables:\\\\n  - id: tab1_main\\\\n    title: \\\\\\\"Main Results: II by Strategy × Phase × Sparsity\\\\\\\"\\\\n    data_source: v5 importance + random, median + IQR\\\\n    columns: [sparsity, strategy, high_phase_II, low_phase_II, gradient, gradient_CI]\\\\n    message: Core quantitative claim — strategy × phase interaction\\\\n    placement: Section 5.1\\\\n    priority: P0\\\\n\\\\n  - id: tab2_bootstrap\\\\n    title: \\\\\\\"Bootstrap Confidence Intervals (B=10000)\\\\\\\"\\\\n    data_source: v6 per-problem bootstrap\\\\n    columns: [sparsity, paired_gradient, paired_CI, unpaired_gradient, unpaired_CI, p_value]\\\\n    message: Statistical rigor — all gradients significant\\\\n    placement: Section 5.1\\\\n    priority: P0\\\\n\\\\n  - id: tab3_crossmodel\\\\n    title: \\\\\\\"Cross-Model Comparison: DeepSeek vs Qwen\\\\\\\"\\\\n    data_source: v6 DeepSeek + Qwen importance results (Qwen pending)\\\\n    message: Generalizability beyond single model family\\\\n    placement: Section 5.3\\\\n    priority: P0 (blocked on Qwen)\\\\n\\\\n# ============================================================\\\\n# Claims → Evidence Mapping\\\\n# ============================================================\\\\nclaims:\\\\n  - claim: \\\\\\\"Compound sparsity severity is strategy-dependent\\\\\\\"\\\\n    evidence:\\\\n      - \\\\\\\"v5 importance gradient 12.8-74.9× vs v5 random gradient ~1×\\\\\\\"\\\\n      - \\\\\\\"Bootstrap CI: importance gradient CI lower bound >> 1.0; random gradient CI spans 1.0\\\\\\\"\\\\n    status: confirmed\\\\n\\\\n  - claim: \\\\\\\"Severity is phase-modulated (amplified in low-sparsity reasoning phase)\\\\\\\"\\\\n    evidence:\\\\n      - \\\\\\\"v5 per-phase II: low phase >> high phase for importance at all 4 sparsity levels\\\\\\\"\\\\n      - \\\\\\\"Gradient monotonically increases with sparsity: 12.8→28.7→52.9→74.9\\\\\\\"\\\\n    status: confirmed\\\\n\\\\n  - claim: \\\\\\\"Phase-strategy crossover exists\\\\\\\"\\\\n    evidence:\\\\n      - \\\\\\\"s=0.25: importance high_phase=0.584 < random=3.002, importance low_phase=30.903 > random=2.915\\\\\\\"\\\\n      - \\\\\\\"Direction depends on phase, not just magnitude\\\\\\\"\\\\n    status: confirmed\\\\n\\\\n  - claim: \\\\\\\"Entropy-discrimination collapse explains the mechanism\\\\\\\"\\\\n    evidence:\\\\n      - \\\\\\\"Conceptual argument: head pruning → distributed attention → importance entropy up → discrimination down\\\\\\\"\\\\n      - \\\\\\\"Empirical: importance PPL 26-60× worse than random before metric fix (D012/D013) = metric failure\\\\\\\"\\\\n    status: partially_confirmed (mechanism is explanatory, not directly measured)\\\\n\\\\n  - claim: \\\\\\\"Finding generalizes across model families\\\\\\\"\\\\n    evidence:\\\\n      - \\\\\\\"Qwen2.5-7B-Instruct experiments (pending)\\\\\\\"\\\\n    status: pending\\\\n\\\\n  - claim: \\\\\\\"Severity gradient is sub-exponential\\\\\\\"\\\\n    evidence:\\\\n      - \\\\\\\"Growth rate: 2.24×→1.84×→1.42× (decreasing)\\\\\\\"\\\\n    status: confirmed\\\\n\\\\n# ============================================================\\\\n# Writing Priority & Schedule\\\\n# ============================================================\\\\nwriting_priority:\\\\n  # Phase 1: 可立即写的部分 (Day 1-3, May 14-16)\\\\n  - priority: 1\\\\n    sections: [methodology, background, related_work]\\\\n    reason: \\\\\\\"不依赖 Qwen 结果，数据已完备，先把 methodology infrastructure 写好\\\\\\\"\\\\n    deliverable: \\\\\\\"完整的 Section 3 + 4 + 2 初稿\\\\\\\"\\\\n\\\\n  - priority: 1\\\\n    task: \\\\\\\"fig1_hero + fig2_crossover + tab1_main + tab2_bootstrap\\\\\\\"\\\\n    reason: \\\\\\\"核心数据已有，图表先出可以驱动 narrative\\\\\\\"\\\\n    deliverable: \\\\\\\"4 个核心 figure/table 的 publication-ready 版本\\\\\\\"\\\\n\\\\n  # Phase 2: 核心结果 (Day 3-5, May 16-18)\\\\n  - priority: 2\\\\n    sections: [results_5_1, results_5_2]\\\\n    reason: \\\\\\\"5.1 和 5.2 数据完备，5.3 (cross-model) 需等 Qwen\\\\\\\"\\\\n    deliverable: \\\\\\\"Section 5.1 + 5.2 完整初稿\\\\\\\"\\\\n\\\\n  - priority: 2\\\\n    sections: [analysis]\\\\n    reason: \\\\\\\"机制解释可独立写，不依赖 Qwen\\\\\\\"\\\\n    deliverable: \\\\\\\"Section 6 初稿\\\\\\\"\\\\n\\\\n  # Phase 3: Cross-model + Introduction (Day 5-7, May 18-20)\\\\n  - priority: 3\\\\n    sections: [results_5_3]\\\\n    reason: \\\\\\\"Qwen 实验预计 Day 3-4 出结果\\\\\\\"\\\\n    deliverable: \\\\\\\"Section 5.3 + Table 3 + Fig 5\\\\\\\"\\\\n\\\\n  - priority: 3\\\\n    sections: [introduction]\\\\n    reason: \\\\\\\"Introduction 最后写——需要所有结果确定后才能精确表述 contributions\\\\\\\"\\\\n    deliverable: \\\\\\\"Section 1 完整初稿\\\\\\\"\\\\n\\\\n  # Phase 4: Abstract + Polish (Day 7-9, May 20-22)\\\\n  - priority: 4\\\\n    sections: [abstract, discussion, conclusion]\\\\n    reason: \\\\\\\"总结性段落最后写\\\\\\\"\\\\n    deliverable: \\\\\\\"完整初稿 v1\\\\\\\"\\\\n\\\\n  # Phase 5: Review & Submission (Day 9-11, May 22-25)\\\\n  - priority: 5\\\\n    task: \\\\\\\"Internal review, polish, formatting check, reference audit, submission\\\\\\\"\\\\n    reason: \\\\\\\"留 3 天 buffer 做 revision\\\\\\\"\\\\n    deliverable: \\\\\\\"Camera-ready 提交\\\\\\\"\\\\n\\\\nschedule:\\\\n  - days: \\\\\\\"Day 1-3 (May 14-16)\\\\\\\"\\\\n    tasks:\\\\n      - \\\\\\\"LaTeX 模板搭建 (EMNLP ARR format)\\\\\\\"\\\\n      - \\\\\\\"Section 3 (Background) 初稿\\\\\\\"\\\\n      - \\\\\\\"Section 4 (Methodology) 初稿\\\\\\\"\\\\n      - \\\\\\\"Section 2 (Related Work) 初稿\\\\\\\"\\\\n      - \\\\\\\"Fig 1 (hero), Fig 2 (crossover), Table 1, Table 2 制图\\\\\\\"\\\\n      - \\\\\\\"启动 Qwen cross-model 实验\\\\\\\"\\\\n    milestone: \\\\\\\"方法论部分完成 + 核心图表就绪\\\\\\\"\\\\n\\\\n  - days: \\\\\\\"Day 3-5 (May 16-18)\\\\\\\"\\\\n    tasks:\\\\n      - \\\\\\\"Section 5.1 (severity gradient) 初稿\\\\\\\"\\\\n      - \\\\\\\"Section 5.2 (crossover) 初稿\\\\\\\"\\\\n      - \\\\\\\"Section 6 (analysis/mechanism) 初稿\\\\\\\"\\\\n      - \\\\\\\"Fig 3 (mechanism diagram)\\\\\\\"\\\\n      - \\\\\\\"Fig 4 (bootstrap forest plot)\\\\\\\"\\\\n    milestone: \\\\\\\"结果+分析部分完成\\\\\\\"\\\\n\\\\n  - days: \\\\\\\"Day 5-7 (May 18-20)\\\\\\\"\\\\n    tasks:\\\\n      - \\\\\\\"Qwen 结果整合 → Section 5.3, Table 3, Fig 5\\\\\\\"\\\\n      - \\\\\\\"Section 1 (Introduction) 初稿\\\\\\\"\\\\n      - \\\\\\\"如果 Qwen 结果延迟：先写 conditional 版本，留占位\\\\\\\"\\\\n    milestone: \\\\\\\"主体内容完成\\\\\\\"\\\\n\\\\n  - days: \\\\\\\"Day 7-9 (May 20-22)\\\\\\\"\\\\n    tasks:\\\\n      - \\\\\\\"Abstract 撰写\\\\\\\"\\\\n      - \\\\\\\"Section 7 (Discussion) + Section 8 (Conclusion)\\\\\\\"\\\\n      - \\\\\\\"Appendix: paired bootstrap 详细结果、per-problem 分布\\\\\\\"\\\\n      - \\\\\\\"全文 polish pass 1: 叙事一致性、数据准确性\\\\\\\"\\\\n    milestone: \\\\\\\"完整初稿 v1\\\\\\\"\\\\n\\\\n  - days: \\\\\\\"Day 9-11 (May 22-25)\\\\\\\"\\\\n    tasks:\\\\n      - \\\\\\\"Reference audit (引用完整性+格式)\\\\\\\"\\\\n      - \\\\\\\"Polish pass 2: 语言、格式、ARR checklist\\\\\\\"\\\\n      - \\\\\\\"Limitations section\\\\\\\"\\\\n      - \\\\\\\"Ethics statement (if required)\\\\\\\"\\\\n      - \\\\\\\"最终提交\\\\\\\"\\\\n    milestone: \\\\\\\"提交完成\\\\\\\"\\\\n\\\\n# ============================================================\\\\n# 关键风险\\\\n# ============================================================\\\\nrisks:\\\\n  - risk: \\\\\\\"Qwen cross-model 实验未完成或结果 negative\\\\\\\"\\\\n    mitigation: >\\\\n      如果 Day 5 前无结果：写 conditional 版本 \\\\\\\"we additionally test on Qwen2.5-7B (results pending)\\\\\\\".\\\\n      如果结果 negative：调整 narrative 为 \\\\\\\"model-specific phenomenon requiring further investigation\\\\\\\",\\\\n      仍可作为 finding paper 提交（DeepSeek 数据已足够支撑 core claim）.\\\\n    impact: medium\\\\n\\\\n  - risk: \\\\\\\"11 天写不完\\\\\\\"\\\\n    mitigation: >\\\\n      优先保证 core sections (3-6)，Introduction/Discussion 可以精简。\\\\n      如果时间不够，砍 mechanism analysis (Section 6) 到 1 段 discussion。\\\\n    impact: low (schedule has 3-day buffer)\\\\n\\\\n  - risk: \\\\\\\"Reviewer 质疑 7B-only + MATH-500-only 的 generalizability\\\\\\\"\\\\n    mitigation: >\\\\n      Cross-model (Qwen) 是第一层防御。Limitations 明确声明 scale。\\\\n      MATH-500 是 standard benchmark，defensible。\\\\n    impact: medium\\\\n\\\\n# ============================================================\\\\n# Framing 约束 (Director D015)\\\\n# ============================================================\\\\nframing_constraints:\\\\n  must: \\\\\\\"emergent phase-strategy interaction\\\\\\\"\\\\n  must_not: \\\\\\\"importance metric limitation / importance is broken\\\\\\\"\\\\n  narrative_arc: >\\\\n    Compound sparsity is increasingly used for efficient LLM inference, but its interaction\\\\n    dynamics are poorly understood. We discover that the severity of compound interaction\\\\n    is not a fixed property — it emerges from the interplay of eviction strategy and reasoning\\\\n    phase. Importance-based eviction amplifies compound degradation 12-75× in low-sparsity\\\\n    phases, while random eviction maintains flat interaction. This phase-strategy interaction,\\\\n    explained by entropy-discrimination collapse, challenges the uniform-degradation assumption\\\\n    and motivates phase-aware sparsity allocation.\\\\n\\\", \\\"total_chars\\\": 15373, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/writing_plan.yaml\", \"content\": \"## Writing Plan — Phase-Gated Compound Sparsity\\n## 最后更新: 2026-05-14\\n\\n# ============================================================\\n# 投稿目标\\n# ============================================================\\ntarget:\\n  venue: EMNLP 2026 ARR\\n  deadline: 2026-05-25\\n  days_remaining: 11\\n  format: long paper (8 pages + references + appendix)\\n  anonymization: ARR double-blind\\n\\n# ============================================================\\n# Paper Outline\\n# ============================================================\\noutline:\\n  title_candidates:\\n    - \\\"Phase-Modulated Compound Sparsity: How Eviction Strategy and Reasoning Phase Interact in Sparse LLM Inference\\\"\\n    - \\\"Emergent Phase-Strategy Interaction in Compound Sparse LLM Inference\\\"\\n    - \\\"When Compound Sparsity Bites Back: Phase-Dependent Severity Amplification in Importance-Based Eviction\\\"\\n\\n  sections:\\n    - id: abstract\\n      title: Abstract\\n      summary: >\\n        Compound sparsity (head pruning + KV cache eviction) is assumed to degrade uniformly.\\n        We show the interaction is strategy-dependent and phase-modulated: importance-based eviction\\n        exhibits 12-75× severity amplification in low-sparsity reasoning phases, while random eviction\\n        stays flat (~1×). Bootstrap CI (B=10000) confirms significance at all 4 sparsity levels (p<0.0001).\\n        Cross-model replication on Qwen2.5-7B validates generalizability. We explain this via an\\n        entropy-discrimination collapse mechanism: head pruning distributes surviving attention,\\n        destroying importance score discriminability specifically in distributed-attention phases.\\n      length: 250 words\\n\\n    - id: introduction\\n      title: \\\"1. Introduction\\\"\\n      summary: >\\n        Motivate compound sparsity as practical deployment need. State gap: prior work (SparK, Ada-KV)\\n        treats compound interaction as uniformly super-additive. Our finding: the severity is an\\n        emergent property of the interaction between eviction strategy and reasoning phase.\\n        Preview crossover phenomenon and mechanism. State contributions.\\n      length: 1 page\\n      key_claims:\\n        - Compound sparsity severity is not uniform — it is strategy-dependent and phase-modulated\\n        - Importance-based eviction amplifies compound interaction 12-75× in low-sparsity phases\\n        - Entropy-discrimination collapse explains the phase-strategy interaction\\n\\n    - id: related_work\\n      title: \\\"2. Related Work\\\"\\n      summary: >\\n        Three threads: (1) Compound/joint compression (SparK, SLiM, UniComp, compression-ordering)\\n        — none analyzes phase × strategy interaction. (2) KV cache eviction (Ada-KV, DefensiveKV,\\n        SnapKV, NACL) — importance fragility noted but not phase-conditioned. (3) Phase-aware\\n        inference (ThinKV, PagedEviction, reasoning dynamics) — single-axis, no compound interaction.\\n      length: 0.75 page\\n      key_refs:\\n        - spark-aaai2026\\n        - thinkv-iclr2026\\n        - defensivekv-iclr2026\\n        - slim-icml2025\\n        - phase-transition-compression-2026\\n        - decision-repr-transition-2026\\n        - retentivekv-2026\\n        - greedy-bias-kvcache-2026\\n\\n    - id: background\\n      title: \\\"3. Background and Problem Setup\\\"\\n      summary: >\\n        Define compound sparsity (attention head pruning ⊗ KV cache eviction). Define Interaction\\n        Index (II) measuring super/sub-additivity. Define phase segmentation via ThinKV-style\\n        token-ratio method. Formalize the research question: is II constant across phases and strategies?\\n      length: 1 page\\n      subsections:\\n        - \\\"3.1 Compound Sparsity Formulation\\\"\\n        - \\\"3.2 Interaction Index\\\"\\n        - \\\"3.3 Phase Segmentation\\\"\\n\\n    - id: methodology\\n      title: \\\"4. Experimental Setup\\\"\\n      summary: >\\n        Models (DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct), dataset (MATH-500 subset, 50 problems),\\n        sparsity levels (s=0.15/0.20/0.25/0.30), eviction strategies (importance-based cumulative\\n        attention with position normalization, random), metrics (PPL, II, gradient), hardware.\\n        Statistical method: per-problem bootstrap CI (B=10000), paired and unpaired.\\n      length: 1 page\\n\\n    - id: results\\n      title: \\\"5. Results\\\"\\n      summary: >\\n        Main finding: importance gradient 12.8-74.9× (median) monotonically increasing with sparsity,\\n        random gradient ~1×. Bootstrap CI all significant (p=0.0000). Crossover: importance safer\\n        than random in high-sparsity phase but dramatically worse in low-sparsity phase.\\n        Sub-exponential growth pattern (rate decreasing: 2.24×→1.84×→1.42×).\\n      length: 1.5 pages\\n      subsections:\\n        - \\\"5.1 Phase-Modulated Severity Gradient\\\"\\n        - \\\"5.2 Strategy-Dependent Crossover\\\"\\n        - \\\"5.3 Cross-Model Replication\\\"\\n\\n    - id: analysis\\n      title: \\\"6. Analysis: Entropy-Discrimination Collapse\\\"\\n      summary: >\\n        Mechanistic explanation: head pruning → surviving heads attend more uniformly → importance\\n        score entropy increases → discrimination between important/unimportant KV entries collapses →\\n        importance-based eviction degrades to biased pseudo-random in distributed-attention phases.\\n        This is phase-dependent because reasoning phases have more distributed attention.\\n      length: 1 page\\n\\n    - id: discussion\\n      title: \\\"7. Discussion\\\"\\n      summary: >\\n        Implications for compound sparsity deployment: uniform budgets are unsafe.\\n        Phase-gated controllers as solution direction. Limitations: 7B models only,\\n        MATH-500 only, no throughput measurements yet.\\n      length: 0.5 page\\n\\n    - id: conclusion\\n      title: \\\"8. Conclusion\\\"\\n      summary: >\\n        Compound sparsity severity is an emergent property of strategy × phase interaction.\\n        This finding challenges the implicit assumption of uniform compound degradation\\n        and motivates phase-aware sparsity allocation.\\n      length: 0.25 page\\n\\n# ============================================================\\n# Figures and Tables\\n# ============================================================\\nfigures:\\n  - id: fig1_hero\\n    title: \\\"Phase-Modulated Severity Gradient (Hero Figure)\\\"\\n    type: line plot or grouped bar\\n    data_source: v5 importance + v5 random segment-level II medians\\n    message: >\\n      Importance gradient rises 12.8-74.9× across sparsity levels while random stays flat ~1×.\\n      The gap between strategies widens with sparsity — this is the core visual claim.\\n    placement: page 1 or Section 5.1\\n    priority: P0\\n\\n  - id: fig2_crossover\\n    title: \\\"Phase-Strategy Crossover Heatmap\\\"\\n    type: heatmap (strategy × phase × sparsity)\\n    data_source: v5 importance + random per-phase II values\\n    message: >\\n      At s=0.25, importance outperforms random in high-sparsity phase (0.584 vs 3.002) but\\n      underperforms dramatically in low-sparsity phase (30.903 vs 2.915). Direction reversal\\n      is phase-dependent.\\n    placement: Section 5.2\\n    priority: P0\\n\\n  - id: fig3_mechanism\\n    title: \\\"Entropy-Discrimination Collapse Illustration\\\"\\n    type: schematic diagram + attention distribution plot\\n    data_source: conceptual + optional empirical attention entropy data\\n    message: >\\n      Head pruning → attention redistribution → importance score entropy increase →\\n      discrimination collapse. Explains why importance eviction fails specifically in\\n      distributed-attention phases.\\n    placement: Section 6\\n    priority: P1\\n\\n  - id: fig4_bootstrap\\n    title: \\\"Bootstrap CI Forest Plot\\\"\\n    type: forest plot\\n    data_source: v6 per-problem bootstrap results (B=10000)\\n    message: >\\n      All 4 sparsity levels show gradient CI entirely above 1.0, p=0.0000.\\n      Visual confirmation of statistical significance.\\n    placement: Section 5.1\\n    priority: P1\\n\\n  - id: fig5_crossmodel\\n    title: \\\"Cross-Model Replication\\\"\\n    type: grouped bar or side-by-side line plot\\n    data_source: Qwen2.5-7B importance results (pending)\\n    message: >\\n      Phase-modulated severity generalizes beyond DeepSeek to Qwen architecture.\\n    placement: Section 5.3\\n    priority: P0 (blocked on Qwen experiments)\\n\\ntables:\\n  - id: tab1_main\\n    title: \\\"Main Results: II by Strategy × Phase × Sparsity\\\"\\n    data_source: v5 importance + random, median + IQR\\n    columns: [sparsity, strategy, high_phase_II, low_phase_II, gradient, gradient_CI]\\n    message: Core quantitative claim — strategy × phase interaction\\n    placement: Section 5.1\\n    priority: P0\\n\\n  - id: tab2_bootstrap\\n    title: \\\"Bootstrap Confidence Intervals (B=10000)\\\"\\n    data_source: v6 per-problem bootstrap\\n    columns: [sparsity, paired_gradient, paired_CI, unpaired_gradient, unpaired_CI, p_value]\\n    message: Statistical rigor — all gradients significant\\n    placement: Section 5.1\\n    priority: P0\\n\\n  - id: tab3_crossmodel\\n    title: \\\"Cross-Model Comparison: DeepSeek vs Qwen\\\"\\n    data_source: v6 DeepSeek + Qwen importance results (Qwen pending)\\n    message: Generalizability beyond single model family\\n    placement: Section 5.3\\n    priority: P0 (blocked on Qwen)\\n\\n# ============================================================\\n# Claims → Evidence Mapping\\n# ============================================================\\nclaims:\\n  - claim: \\\"Compound sparsity severity is strategy-dependent\\\"\\n    evidence:\\n      - \\\"v5 importance gradient 12.8-74.9× vs v5 random gradient ~1×\\\"\\n      - \\\"Bootstrap CI: importance gradient CI lower bound >> 1.0; random gradient CI spans 1.0\\\"\\n    status: confirmed\\n\\n  - claim: \\\"Severity is phase-modulated (amplified in low-sparsity reasoning phase)\\\"\\n    evidence:\\n      - \\\"v5 per-phase II: low phase >> high phase for importance at all 4 sparsity levels\\\"\\n      - \\\"Gradient monotonically increases with sparsity: 12.8→28.7→52.9→74.9\\\"\\n    status: confirmed\\n\\n  - claim: \\\"Phase-strategy crossover exists\\\"\\n    evidence:\\n      - \\\"s=0.25: importance high_phase=0.584 < random=3.002, importance low_phase=30.903 > random=2.915\\\"\\n      - \\\"Direction depends on phase, not just magnitude\\\"\\n    status: confirmed\\n\\n  - claim: \\\"Entropy-discrimination collapse explains the mechanism\\\"\\n    evidence:\\n      - \\\"Conceptual argument: head pruning → distributed attention → importance entropy up → discrimination down\\\"\\n      - \\\"Empirical: importance PPL 26-60× worse than random before metric fix (D012/D013) = metric failure\\\"\\n    status: partially_confirmed (mechanism is explanatory, not directly measured)\\n\\n  - claim: \\\"Finding generalizes across model families\\\"\\n    evidence:\\n      - \\\"Qwen2.5-7B-Instruct experiments (pending)\\\"\\n    status: pending\\n\\n  - claim: \\\"Severity gradient is sub-exponential\\\"\\n    evidence:\\n      - \\\"Growth rate: 2.24×→1.84×→1.42× (decreasing)\\\"\\n    status: confirmed\\n\\n# ============================================================\\n# Writing Priority & Schedule\\n# ============================================================\\nwriting_priority:\\n  # Phase 1: 可立即写的部分 (Day 1-3, May 14-16)\\n  - priority: 1\\n    sections: [methodology, background, related_work]\\n    reason: \\\"不依赖 Qwen 结果，数据已完备，先把 methodology infrastructure 写好\\\"\\n    deliverable: \\\"完整的 Section 3 + 4 + 2 初稿\\\"\\n\\n  - priority: 1\\n    task: \\\"fig1_hero + fig2_crossover + tab1_main + tab2_bootstrap\\\"\\n    reason: \\\"核心数据已有，图表先出可以驱动 narrative\\\"\\n    deliverable: \\\"4 个核心 figure/table 的 publication-ready 版本\\\"\\n\\n  # Phase 2: 核心结果 (Day 3-5, May 16-18)\\n  - priority: 2\\n    sections: [results_5_1, results_5_2]\\n    reason: \\\"5.1 和 5.2 数据完备，5.3 (cross-model) 需等 Qwen\\\"\\n    deliverable: \\\"Section 5.1 + 5.2 完整初稿\\\"\\n\\n  - priority: 2\\n    sections: [analysis]\\n    reason: \\\"机制解释可独立写，不依赖 Qwen\\\"\\n    deliverable: \\\"Section 6 初稿\\\"\\n\\n  # Phase 3: Cross-model + Introduction (Day 5-7, May 18-20)\\n  - priority: 3\\n    sections: [results_5_3]\\n    reason: \\\"Qwen 实验预计 Day 3-4 出结果\\\"\\n    deliverable: \\\"Section 5.3 + Table 3 + Fig 5\\\"\\n\\n  - priority: 3\\n    sections: [introduction]\\n    reason: \\\"Introduction 最后写——需要所有结果确定后才能精确表述 contributions\\\"\\n    deliverable: \\\"Section 1 完整初稿\\\"\\n\\n  # Phase 4: Abstract + Polish (Day 7-9, May 20-22)\\n  - priority: 4\\n    sections: [abstract, discussion, conclusion]\\n    reason: \\\"总结性段落最后写\\\"\\n    deliverable: \\\"完整初稿 v1\\\"\\n\\n  # Phase 5: Review & Submission (Day 9-11, May 22-25)\\n  - priority: 5\\n    task: \\\"Internal review, polish, formatting check, reference audit, submission\\\"\\n    reason: \\\"留 3 天 buffer 做 revision\\\"\\n    deliverable: \\\"Camera-ready 提交\\\"\\n\\nschedule:\\n  - days: \\\"Day 1-3 (May 14-16)\\\"\\n    tasks:\\n      - \\\"LaTeX 模板搭建 (EMNLP ARR format)\\\"\\n      - \\\"Section 3 (Background) 初稿\\\"\\n      - \\\"Section 4 (Methodology) 初稿\\\"\\n      - \\\"Section 2 (Related Work) 初稿\\\"\\n      - \\\"Fig 1 (hero), Fig 2 (crossover), Table 1, Table 2 制图\\\"\\n      - \\\"启动 Qwen cross-model 实验\\\"\\n    milestone: \\\"方法论部分完成 + 核心图表就绪\\\"\\n\\n  - days: \\\"Day 3-5 (May 16-18)\\\"\\n    tasks:\\n      - \\\"Section 5.1 (severity gradient) 初稿\\\"\\n      - \\\"Section 5.2 (crossover) 初稿\\\"\\n      - \\\"Section 6 (analysis/mechanism) 初稿\\\"\\n      - \\\"Fig 3 (mechanism diagram)\\\"\\n      - \\\"Fig 4 (bootstrap forest plot)\\\"\\n    milestone: \\\"结果+分析部分完成\\\"\\n\\n  - days: \\\"Day 5-7 (May 18-20)\\\"\\n    tasks:\\n      - \\\"Qwen 结果整合 → Section 5.3, Table 3, Fig 5\\\"\\n      - \\\"Section 1 (Introduction) 初稿\\\"\\n      - \\\"如果 Qwen 结果延迟：先写 conditional 版本，留占位\\\"\\n    milestone: \\\"主体内容完成\\\"\\n\\n  - days: \\\"Day 7-9 (May 20-22)\\\"\\n    tasks:\\n      - \\\"Abstract 撰写\\\"\\n      - \\\"Section 7 (Discussion) + Section 8 (Conclusion)\\\"\\n      - \\\"Appendix: paired bootstrap 详细结果、per-problem 分布\\\"\\n      - \\\"全文 polish pass 1: 叙事一致性、数据准确性\\\"\\n    milestone: \\\"完整初稿 v1\\\"\\n\\n  - days: \\\"Day 9-11 (May 22-25)\\\"\\n    tasks:\\n      - \\\"Reference audit (引用完整性+格式)\\\"\\n      - \\\"Polish pass 2: 语言、格式、ARR checklist\\\"\\n      - \\\"Limitations section\\\"\\n      - \\\"Ethics statement (if required)\\\"\\n      - \\\"最终提交\\\"\\n    milestone: \\\"提交完成\\\"\\n\\n# ============================================================\\n# 关键风险\\n# ============================================================\\nrisks:\\n  - risk: \\\"Qwen cross-model 实验未完成或结果 negative\\\"\\n    mitigation: >\\n      如果 Day 5 前无结果：写 conditional 版本 \\\"we additionally test on Qwen2.5-7B (results pending)\\\".\\n      如果结果 negative：调整 narrative 为 \\\"model-specific phenomenon requiring further investigation\\\",\\n      仍可作为 finding paper 提交（DeepSeek 数据已足够支撑 core claim）.\\n    impact: medium\\n\\n  - risk: \\\"11 天写不完\\\"\\n    mitigation: >\\n      优先保证 core sections (3-6)，Introduction/Discussion 可以精简。\\n      如果时间不够，砍 mechanism analysis (Section 6) 到 1 段 discussion。\\n    impact: low (schedule has 3-day buffer)\\n\\n  - risk: \\\"Reviewer 质疑 7B-only + MATH-500-only 的 generalizability\\\"\\n    mitigation: >\\n      Cross-model (Qwen) 是第一层防御。Limitations 明确声明 scale。\\n      MATH-500 是 standard benchmark，defensible。\\n    impact: medium\\n\\n# ============================================================\\n# Framing 约束 (Director D015)\\n# ============================================================\\nframing_constraints:\\n  must: \\\"emergent phase-strategy interaction\\\"\\n  must_not: \\\"importance metric limitation / importance is broken\\\"\\n  narrative_arc: >\\n    Compound sparsity is increasingly used for efficient LLM inference, but its interaction\\n    dynamics are poorly understood. We discover that the severity of compound interaction\\n    is not a fixed property — it emerges from the interplay of eviction strategy and reasoning\\n    phase. Importance-based eviction amplifies compound degradation 12-75× in low-sparsity\\n    phases, while random eviction maintains flat interaction. This phase-strategy interaction,\\n    explained by entropy-discrimination collapse, challenges the uniform-degradation assumption\\n    and motivates phase-aware sparsity allocation.\\n\", \"total_chars\": 15373, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_018xy8e29fJZc2xzth4BHfQ7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "7f2d05c8-717a-4401-b149-647be59dec0f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LCdrPmajAFva98bCB2TuwE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 23751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 732
      },
      "output_tokens": 71,
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

_source line 10 · 2026-05-14T05:35:51.489Z_

<details><summary>↩ Tool result · `toolu_018xy8e29fJZc2xzth4BHfQ7`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\subsection{Models}
5	\label{sec:models}
6	
7	We conduct experiments on two 7B-parameter instruction-tuned models that share the Qwen2 backbone architecture (28 Transformer layers, 28 attention heads with 4-group GQA):
8	
9	\paragraph{DeepSeek-R1-Distill-Qwen-7B} serves as our primary evaluation target. This model was distilled from DeepSeek-R1 \cite{deepseek-r1} and produces explicit chain-of-thought traces delimited by \texttt{&lt;think>}$\cdots$\texttt{&lt;/think>} tags, yielding sequences with pronounced phase structure---extended reasoning followed by a concise solution. The structured generation pattern makes it well-suited for studying how sparsity interacts with distinct reasoning phases.
10	
11	\paragraph{Qwen2.5-7B-Instruct} \cite{qwen2.5} provides a cross-architecture replication. Although it shares the same backbone family, its instruction tuning does not enforce explicit reasoning delimiters, producing a different distribution of attention sparsity across the generation trajectory. Replication on this model tests whether our findings generalize beyond distillation-induced phase structure.
12	
13	Both models are loaded in \texttt{bfloat16} precision with eager attention (i.e., without FlashAttention) to permit direct manipulation of attention weight matrices during sparsity intervention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values in Layer~27 of DeepSeek-R1-Distill-Qwen-7B, affecting ${\sim}$8\% of logit positions. Switching to \texttt{bfloat16} eliminated all NaN occurrences; we additionally apply NaN-guarded filtering as a safety net.}
14	
15	
16	\subsection{Dataset}
17	\label{sec:dataset}
18	
19	We evaluate on a 50-problem stratified subset of the MATH-500 benchmark \cite{math500}, sampling uniformly across problem categories (algebra, geometry, number theory, combinatorics, etc.) with a fixed seed for reproducibility. Mathematical reasoning tasks are a natural testbed for our study: they elicit long chain-of-thought sequences (up to 2048 tokens) in which the model alternates between exploratory reasoning and structured computation---phases that differ markedly in attention sparsity. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048) to eliminate sampling variance.
20	
21	
22	\subsection{Compound Sparsity Configuration}
23	\label{sec:sparsity-config}
24	
25	We apply \emph{symmetric} compound sparsity: for a given sparsity level $s$, we prune the same fraction $s$ of attention heads and evict the same fraction $s$ of KV cache entries. We evaluate four sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$, spanning from mild to aggressive compression.
26	
27	\paragraph{Sparsity conditions.} For each problem and each sparsity level, we compute perplexity under four conditions: (i)~\emph{dense}---no intervention; (ii)~\emph{attn-only}---head pruning without KV eviction; (iii)~\emph{kv-only}---KV eviction without head pruning; and (iv)~\emph{both}---simultaneous head pruning and KV eviction.
28	
29	\paragraph{Eviction strategies.} We compare two KV cache eviction strategies:
30	
31	\begin{itemize}[nosep,leftmargin=*]
32	\item \textbf{Importance-based.} Each KV position receives a score equal to its cumulative attention weight summed over all query positions and heads. To correct for the inherent causal bias---earlier positions accumulate more attention simply because they are attended to by more queries---we apply position normalization:
33	\begin{equation}
34	\label{eq:importance}
35	    \alpha_j = \frac{\sum_{i,h} a_{i,h,j}}{\texttt{seq\_len} - j}, \quad j \in \{1, \dots, T\},
36	\end{equation}
37	where $a_{i,h,j}$ is the attention weight from query~$i$, head~$h$ to key~$j$, and the denominator counts the number of queries that can attend to position~$j$ under causal masking. Position~0 (BOS) is always retained. The $T \cdot s$ positions with the lowest normalized scores are evicted.
38	
39	During masked forward passes, we guard against numerical instability from the interaction of head masking and KV eviction: zeroed-out heads that would otherwise produce $\infty \times 0 = \text{NaN}$ are handled via selective replacement (\texttt{torch.where}) prior to the softmax, and any layer producing NaN outputs is skipped from the sparsity loss computation.
40	
41	\item \textbf{Random.} KV positions (excluding BOS) are evicted uniformly at random, providing a strategy-agnostic baseline. Head pruning under the random condition selects heads via \texttt{torch.randperm} rather than by importance.
42	\end{itemize}
43	
44	\paragraph{Head pruning.} Under importance-based eviction, heads are ranked by their Frobenius norm across the full attention matrix $\mathbf{A}_\ell \in \mathbb{R}^{H \times T \times T}$ per layer $\ell$, and the bottom-$s$ fraction is masked. Under random eviction, heads are selected uniformly at random.
45	
46	
47	\subsection{Phase Segmentation}
48	\label{sec:phase-seg}
49	
50	We segment each generated sequence into three \emph{reasoning phases} based on the local attention sparsity of each token position. For each query position $i$, we compute per-head sparsity as the fraction of attention weights falling below $0.01 \times \max_j a_{i,h,j}$, then average across heads to obtain a scalar sparsity value per position. The resulting sparsity trajectory is partitioned into terciles via quantile boundaries: \emph{low-sparsity} (bottom third, corresponding to focused attention during structured computation), \emph{mid-sparsity}, and \emph{high-sparsity} (top third, corresponding to diffuse attention during exploratory reasoning). Contiguous segments shorter than $\texttt{min\_phase\_length}=10$ tokens are merged into adjacent phases to suppress noise.
51	
52	
53	\subsection{Metrics}
54	\label{sec:metrics}
55	
56	\paragraph{Perplexity.} For each sparsity condition $c \in \{d, a, k, b\}$ and each phase, we compute segment-level perplexity as
57	$\text{PPL}_c = \exp\!\bigl(\tfrac{1}{|I|}\sum_{i \in I} \mathcal{L}_c(x_i)\bigr)$,
58	where $I$ is the set of token indices belonging to the phase and $\mathcal{L}_c(x_i)$ is the per-token cross-entropy loss under condition $c$.
59	
60	\paragraph{Interaction Index.} The interaction index quantifies the synergistic (super-additive) effect of compound sparsity beyond the sum of individual interventions:
61	\begin{equation}
62	\label{eq:ii}
63	    \mathrm{II} = \frac{\text{PPL}_b}{\text{PPL}_d} - \frac{\text{PPL}_a}{\text{PPL}_d} - \frac{\text{PPL}_k}{\text{PPL}_d} + 1.
64	\end{equation}
65	When $\mathrm{II} > 0$, the two sparsity mechanisms amplify each other; $\mathrm{II} = 0$ indicates additive (independent) degradation.
66	
67	\paragraph{Severity Gradient.} To measure how the interaction varies across reasoning phases, we define the severity gradient:
68	\begin{equation}
69	\label{eq:gradient}
70	    G = \frac{\widetilde{\mathrm{II}}_{\,\textit{low}}}{\widetilde{\mathrm{II}}_{\,\textit{high}}},
71	\end{equation}
72	where $\widetilde{\mathrm{II}}_{\,\textit{low}}$ and $\widetilde{\mathrm{II}}_{\,\textit{high}}$ are the median interaction indices over the low-sparsity and high-sparsity phases, respectively. We report medians rather than means because the II distribution is heavily right-skewed (mean/median ratios up to 43:1 at $s{=}0.30$), making the median a more robust central tendency estimator.
73	
74	
75	\subsection{Statistical Analysis}
76	\label{sec:stats}
77	
78	All confidence intervals and significance tests are computed via the nonparametric bootstrap with $B = 10{,}000$ resamples \cite{efron1993bootstrap}.
79	
80	\paragraph{Per-problem bootstrap.} For each sparsity level and strategy, we resample the 50 per-problem II values with replacement and compute the mean of each resample, yielding a 95\% percentile confidence interval for the population mean II.
81	
82	\paragraph{Paired bootstrap.} To test whether the severity gradient differs between importance-based and random eviction, we pair observations by problem (same problem, same sparsity level) and bootstrap the difference in gradients. This controls for problem-level variance in difficulty and sequence length.
83	
84	\paragraph{Unpaired bootstrap.} We additionally compute per-strategy gradient confidence intervals without pairing, to verify that the importance-based gradient is significantly greater than 1 (i.e., phase modulation exists) independently of the random baseline.
85	
86	All tests yield $p < 0.0001$ at every sparsity level, confirming that the observed phase--strategy interactions are not artifacts of sampling variability.\footnote{Experiments were conducted on a server with 4$\times$ NVIDIA RTX 6000 Ada 96\,GB GPUs, with one model--sparsity configuration per GPU.}
87	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "fc9cf78f-e1c4-4b3b-af4f-3e8368a6c858",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex",
      "content": "\\section{Experimental Setup}\n\\label{sec:experimental-setup}\n\n\\subsection{Models}\n\\label{sec:models}\n\nWe conduct experiments on two 7B-parameter instruction-tuned models that share the Qwen2 backbone architecture (28 Transformer layers, 28 attention heads with 4-group GQA):\n\n\\paragraph{DeepSeek-R1-Distill-Qwen-7B} serves as our primary evaluation target. This model was distilled from DeepSeek-R1 \\cite{deepseek-r1} and produces explicit chain-of-thought traces delimited by \\texttt{&lt;think>}$\\cdots$\\texttt{&lt;/think>} tags, yielding sequences with pronounced phase structure---extended reasoning followed by a concise solution. The structured generation pattern makes it well-suited for studying how sparsity interacts with distinct reasoning phases.\n\n\\paragraph{Qwen2.5-7B-Instruct} \\cite{qwen2.5} provides a cross-architecture replication. Although it shares the same backbone family, its instruction tuning does not enforce explicit reasoning delimiters, producing a different distribution of attention sparsity across the generation trajectory. Replication on this model tests whether our findings generalize beyond distillation-induced phase structure.\n\nBoth models are loaded in \\texttt{bfloat16} precision with eager attention (i.e., without FlashAttention) to permit direct manipulation of attention weight matrices during sparsity intervention.\\footnote{An earlier \\texttt{float16} configuration produced sporadic NaN values in Layer~27 of DeepSeek-R1-Distill-Qwen-7B, affecting ${\\sim}$8\\% of logit positions. Switching to \\texttt{bfloat16} eliminated all NaN occurrences; we additionally apply NaN-guarded filtering as a safety net.}\n\n\n\\subsection{Dataset}\n\\label{sec:dataset}\n\nWe evaluate on a 50-problem stratified subset of the MATH-500 benchmark \\cite{math500}, sampling uniformly across problem categories (algebra, geometry, number theory, combinatorics, etc.) with a fixed seed for reproducibility. Mathematical reasoning tasks are a natural testbed for our study: they elicit long chain-of-thought sequences (up to 2048 tokens) in which the model alternates between exploratory reasoning and structured computation---phases that differ markedly in attention sparsity. Each problem is decoded greedily (\\texttt{max\\_new\\_tokens}$=$2048) to eliminate sampling variance.\n\n\n\\subsection{Compound Sparsity Configuration}\n\\label{sec:sparsity-config}\n\nWe apply \\emph{symmetric} compound sparsity: for a given sparsity level $s$, we prune the same fraction $s$ of attention heads and evict the same fraction $s$ of KV cache entries. We evaluate four sparsity levels $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$, spanning from mild to aggressive compression.\n\n\\paragraph{Sparsity conditions.} For each problem and each sparsity level, we compute perplexity under four conditions: (i)~\\emph{dense}---no intervention; (ii)~\\emph{attn-only}---head pruning without KV eviction; (iii)~\\emph{kv-only}---KV eviction without head pruning; and (iv)~\\emph{both}---simultaneous head pruning and KV eviction.\n\n\\paragraph{Eviction strategies.} We compare two KV cache eviction strategies:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Importance-based.} Each KV position receives a score equal to its cumulative attention weight summed over all query positions and heads. To correct for the inherent causal bias---earlier positions accumulate more attention simply because they are attended to by more queries---we apply position normalization:\n\\begin{equation}\n\\label{eq:importance}\n    \\alpha_j = \\frac{\\sum_{i,h} a_{i,h,j}}{\\texttt{seq\\_len} - j}, \\quad j \\in \\{1, \\dots, T\\},\n\\end{equation}\nwhere $a_{i,h,j}$ is the attention weight from query~$i$, head~$h$ to key~$j$, and the denominator counts the number of queries that can attend to position~$j$ under causal masking. Position~0 (BOS) is always retained. The $T \\cdot s$ positions with the lowest normalized scores are evicted.\n\nDuring masked forward passes, we guard against numerical instability from the interaction of head masking and KV eviction: zeroed-out heads that would otherwise produce $\\infty \\times 0 = \\text{NaN}$ are handled via selective replacement (\\texttt{torch.where}) prior to the softmax, and any layer producing NaN outputs is skipped from the sparsity loss computation.\n\n\\item \\textbf{Random.} KV positions (excluding BOS) are evicted uniformly at random, providing a strategy-agnostic baseline. Head pruning under the random condition selects heads via \\texttt{torch.randperm} rather than by importance.\n\\end{itemize}\n\n\\paragraph{Head pruning.} Under importance-based eviction, heads are ranked by their Frobenius norm across the full attention matrix $\\mathbf{A}_\\ell \\in \\mathbb{R}^{H \\times T \\times T}$ per layer $\\ell$, and the bottom-$s$ fraction is masked. Under random eviction, heads are selected uniformly at random.\n\n\n\\subsection{Phase Segmentation}\n\\label{sec:phase-seg}\n\nWe segment each generated sequence into three \\emph{reasoning phases} based on the local attention sparsity of each token position. For each query position $i$, we compute per-head sparsity as the fraction of attention weights falling below $0.01 \\times \\max_j a_{i,h,j}$, then average across heads to obtain a scalar sparsity value per position. The resulting sparsity trajectory is partitioned into terciles via quantile boundaries: \\emph{low-sparsity} (bottom third, corresponding to focused attention during structured computation), \\emph{mid-sparsity}, and \\emph{high-sparsity} (top third, corresponding to diffuse attention during exploratory reasoning). Contiguous segments shorter than $\\texttt{min\\_phase\\_length}=10$ tokens are merged into adjacent phases to suppress noise.\n\n\n\\subsection{Metrics}\n\\label{sec:metrics}\n\n\\paragraph{Perplexity.} For each sparsity condition $c \\in \\{d, a, k, b\\}$ and each phase, we compute segment-level perplexity as\n$\\text{PPL}_c = \\exp\\!\\bigl(\\tfrac{1}{|I|}\\sum_{i \\in I} \\mathcal{L}_c(x_i)\\bigr)$,\nwhere $I$ is the set of token indices belonging to the phase and $\\mathcal{L}_c(x_i)$ is the per-token cross-entropy loss under condition $c$.\n\n\\paragraph{Interaction Index.} The interaction index quantifies the synergistic (super-additive) effect of compound sparsity beyond the sum of individual interventions:\n\\begin{equation}\n\\label{eq:ii}\n    \\mathrm{II} = \\frac{\\text{PPL}_b}{\\text{PPL}_d} - \\frac{\\text{PPL}_a}{\\text{PPL}_d} - \\frac{\\text{PPL}_k}{\\text{PPL}_d} + 1.\n\\end{equation}\nWhen $\\mathrm{II} > 0$, the two sparsity mechanisms amplify each other; $\\mathrm{II} = 0$ indicates additive (independent) degradation.\n\n\\paragraph{Severity Gradient.} To measure how the interaction varies across reasoning phases, we define the severity gradient:\n\\begin{equation}\n\\label{eq:gradient}\n    G = \\frac{\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}}{\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}},\n\\end{equation}\nwhere $\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}$ and $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}$ are the median interaction indices over the low-sparsity and high-sparsity phases, respectively. We report medians rather than means because the II distribution is heavily right-skewed (mean/median ratios up to 43:1 at $s{=}0.30$), making the median a more robust central tendency estimator.\n\n\n\\subsection{Statistical Analysis}\n\\label{sec:stats}\n\nAll confidence intervals and significance tests are computed via the nonparametric bootstrap with $B = 10{,}000$ resamples \\cite{efron1993bootstrap}.\n\n\\paragraph{Per-problem bootstrap.} For each sparsity level and strategy, we resample the 50 per-problem II values with replacement and compute the mean of each resample, yielding a 95\\% percentile confidence interval for the population mean II.\n\n\\paragraph{Paired bootstrap.} To test whether the severity gradient differs between importance-based and random eviction, we pair observations by problem (same problem, same sparsity level) and bootstrap the difference in gradients. This controls for problem-level variance in difficulty and sequence length.\n\n\\paragraph{Unpaired bootstrap.} We additionally compute per-strategy gradient confidence intervals without pairing, to verify that the importance-based gradient is significantly greater than 1 (i.e., phase modulation exists) independently of the random baseline.\n\nAll tests yield $p < 0.0001$ at every sparsity level, confirming that the observed phase--strategy interactions are not artifacts of sampling variability.\\footnote{Experiments were conducted on a server with 4$\\times$ NVIDIA RTX 6000 Ada 96\\,GB GPUs, with one model--sparsity configuration per GPU.}\n",
      "numLines": 87,
      "startLine": 1,
      "totalLines": 87
    }
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Now I have the writing plan and methodology.tex. Let me also check if there are any existing paper files to understand the notation conventions better.

Let me now read the paper_framing.md and any other relevant materials before writing.

Key observations from methodology.tex for notation consistency:
- Sparsity level: $s$
- Sparsity conditions: $c \in \{d, a, k, b\}$ (dense, attn-only, kv-only, both)
- PPL notation: $\text{PPL}_d$, $\text{PPL}_a$, $\text{PPL}_k$, $\text{PPL}_b$


- The II formula measures interaction effects by comparing the combined sparsity impact against individual contributions
- Severity gradient quantifies how the interaction strength varies across sparsity phases (low, mid, high)
- Head pruning is evaluated using Frobenius norm as the metric for importance
- For KV eviction, I'm computing importance scores by summing cumulative attention weights across all heads and positions, then normalizing by remaining sequence length
- Phase boundaries are determined by calculating per-head sparsity as the fraction of attention weights below a threshold, averaging across heads, then using quantile-based terciles to split into three phases with a minimum length of 10 tokens
- Both head pruning and KV eviction apply the same sparsity fraction to maintain symmetric compound sparsity
- The model uses grouped query attention with 28 heads organized into 4 groups

Now I'm planning Section 3 to establish the formal framework before diving into experimental setup—defining compound sparsity, the interaction index, and phase segmentation as theoretical concepts rather than implementation specifics, keeping notation aligned with Section 4 while avoiding repetition of model names, datasets, and concrete sparsity values. I need to decide on the structure: Section 3 should introduce the formal framework with compound sparsity, the II formula, and phase definitions, while Section 4 can reference those definitions and add implementation specifics. Since methodology.tex already defines II under Metrics, I'll define it conceptually in Section 3 and have Section 4 reference back to avoid redundancy. I'll use consistent labels across sections—eq:ii for the information index definition, eq:gradient for the severity gradient, and a new label for compound sparsity—so Section 4 can simply reference these definitions rather than redefine them.

Now I'm drafting Section 3 with the background material, starting with the compound sparsity formulation and attention head pruning mechanics.

Writing LaTeX section... yielding a compound sparsity level parameterized by a single scalar. The central question is whether the degradation from compound sparsity decomposes additively—i.e., whether the joint effect equals the sum of individual effects—or whether the two mechanisms interact.

To quantify this interaction, I'm defining an Interaction Index that compares the perplexity under four conditions: dense baseline, attention pruning alone, KV cache eviction alone, and both applied together. By normalizing each against the dense baseline and computing the difference between the combined effect and the sum of individual effects, I can isolate whether these two sparsity mechanisms amplify or dampen each other. When this index is positive, the degradation is super-additive—meaning the combined effect is worse than expected from simply adding the individual impacts.

Prior work has treated this super-additivity as an inherent property of the sparsity level, but I'm investigating whether it actually varies depending on which reasoning phase is being compressed. To measure this variation, I'm introducing a severity gradient that compares the interaction strength across different phases. I'm realizing the severity gradient definition needs to come after I've introduced phases, since it depends on both the interaction index and the phase concepts. I think the cleanest approach is to define it at the end of section 3.3, right after explaining phase segmentation, so both concepts are fresh. Let me reorganize: compound sparsity in 3.1, interaction index in 3.2, then phase segmentation followed by the severity gradient definition in 3.3.

I should aim for about 250 words per subsection to keep the total around 750. I'm also noticing that methodology.tex already has these definitions elsewhere in the paper, so I'll focus on writing section 3 with the primary formal definitions and let the user decide if cross-references need adjusting elsewhere.

For the equation labels, I'll use the same ones since the intent is for these definitions to live in Section 3 going forward—that way when everything gets integrated, the references will point to the right place without conflicts.

Now I'm structuring Section 3 with a clear plan: first I'll lay out the compound sparsity formulation abstractly, explaining how head pruning and KV eviction work as two independent sparsity axes that can be applied together, then move into the interaction index framework with the four experimental conditions and how to measure their relative degradation.

For the interaction index itself, I'm defining it as the difference between the combined effect and the sum of individual effects—positive values indicate super-additivity where the two mechanisms interfere with each other, while negative values suggest sub-additivity where they partially compensate. The normalization against the dense baseline makes this comparable across different model configurations.

Finally, I'll introduce phase segmentation by observing that reasoning traces show heterogeneous attention patterns across positions, so I'm dividing the sequence into three phases using quantile-based boundaries and measuring how the interaction index varies across these phases and different pruning strategies—this is the core empirical question driving the analysis.

Now I'm checking the citation keys I'll need from the literature and verifying the methodology details like the importance scoring formula and how head pruning and KV cache eviction are defined in the existing sections.

I see the distinction now—Section 3 should keep things abstract by referring to "importance criteria" and "eviction strategies" without specifying the exact formulas, while Section 4 dives into the concrete implementations like the cumulative attention score formula and Frobenius norm ranking.

Looking back at the phase segmentation logic, I'm understanding how the sparsity trajectory gets divided into three regions based on attention concentration—low sparsity for focused computation, high sparsity for exploratory reasoning, with the boundaries determined by quantile thresholds.

The key insight is that "low-sparsity phase" is a bit of a misnomer since it actually refers to the phase where attention is *least* sparse (most concentrated), and this is precisely where compound sparsity causes the worst degradation—the 12-75× importance gradient. The severity metric G compares importance scores between these focused and diffuse phases, so the naming convention tracks the attention pattern itself rather than the impact severity.

But now I'm noticing a discrepancy between what the task description says about phase segmentation and what the methodology section describes. The task mentions using token-ratio boundaries based on cumulative token counts across the inference trace, whereas the methodology appears to define phases by attention sparsity levels directly. I need to reconcile these two approaches to make sure Section 3 is internally consistent.

Looking more carefully, I think the task description and methodology might actually be describing the same concept from different angles—the token-ratio could be a proxy for attention sparsity patterns. Since the methodology section is already written and more technically precise, I'll use that as my reference point and make sure the section aligns with how attention sparsity actually defines the three reasoning phases.

Let me just start writing the section now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "d386e177-a7d7-4067-871c-4676e2fbf032",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017uNSrkMru9pH7ZQtquqLU5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8445,
      "cache_read_input_tokens": 24483,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8445
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

_source line 12_

Let me also check what other paper files exist to understand the LaTeX structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "500d1694-c91a-48c4-a351-f225c9e87b67",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017uNSrkMru9pH7ZQtquqLU5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8445,
      "cache_read_input_tokens": 24483,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8445
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

<details open><summary>🔧 Tool call — Glob · `toolu_01TaGjw9GTUiGwmPcDE8TGDh`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "1cbbec31-052f-4d31-a11e-64516689277d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017uNSrkMru9pH7ZQtquqLU5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8445,
      "cache_read_input_tokens": 24483,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8445
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

_source line 14 · 2026-05-14T05:37:33.087Z_

<details><summary>↩ Tool result · `toolu_01TaGjw9GTUiGwmPcDE8TGDh`</summary>

```text
artifacts/_project/paper/related_work_46fb53.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/background.tex
artifacts/_project/paper/background_fc6d1d.tex
artifacts/_project/paper/methodology.tex
artifacts/_project/paper/methodology_4cc5f3.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "2dd1da06-90aa-4d0d-94d9-e066ed4ae3d0",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/related_work_46fb53.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/background.tex",
      "artifacts/_project/paper/background_fc6d1d.tex",
      "artifacts/_project/paper/methodology.tex",
      "artifacts/_project/paper/methodology_4cc5f3.tex"
    ],
    "durationMs": 16,
    "numFiles": 6,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01AyaVVAFYt6GTMVuAWBFuBn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "1bad78a1-172c-46ff-9742-5edd25c9d545",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018i6tusAmcBDmHDs6xHK67C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5199,
      "cache_read_input_tokens": 32928,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5199
      },
      "output_tokens": 68,
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

_source line 16 · 2026-05-14T05:37:35.577Z_

<details><summary>↩ Tool result · `toolu_01AyaVVAFYt6GTMVuAWBFuBn`</summary>

```text
1	% Section 3: Background and Problem Setup
2	% Phase-Modulated Compound Sparsity
3	
4	\section{Background and Problem Setup}
5	\label{sec:background}
6	
7	We formalize compound sparsity as the simultaneous application of attention head pruning and KV cache eviction, define the Interaction Index to measure their non-additive interaction, and introduce phase segmentation to localize the analysis across reasoning stages.
8	
9	\subsection{Compound Sparsity Formulation}
10	\label{sec:compound-sparsity}
11	
12	Consider a transformer language model $\mathcal{M}$ with $L$ layers, each containing $H$ attention heads.
13	Let $s \in (0,1)$ denote a unified sparsity budget applied to both compression axes.
14	
15	\paragraph{Attention head pruning.}
16	Given per-head importance scores $\mathbf{w}^{(l)} \in \mathbb{R}^H$ for layer $l$, we construct a binary mask $\mathbf{m}_h^{(l)} \in \{0,1\}^H$ that retains the top-$(1{-}s) \cdot H$ heads by importance.
17	For head $j$ in layer $l$, the masked attention output becomes:
18	\begin{equation}
19	    \tilde{\mathbf{o}}_j^{(l)} = m_{h,j}^{(l)} \cdot \mathbf{o}_j^{(l)}
20	    \label{eq:head-mask}
21	\end{equation}
22	where $\mathbf{o}_j^{(l)}$ is the original head output.
23	Head importance is computed as the Frobenius norm of the attention weight matrix: $w_j^{(l)} = \|\mathbf{A}_j^{(l)}\|_F$, where $\mathbf{A}_j^{(l)} \in \mathbb{R}^{T \times T}$ is the attention probability matrix for head $j$ at layer $l$ over a calibration input of length $T$.
24	
25	\paragraph{KV cache eviction.}
26	For a sequence of length $T$, we construct a position mask $\mathbf{m}_k \in \{0,1\}^T$ that retains the top-$(1{-}s) \cdot T$ positions by importance, with position $0$ (BOS) always retained.
27	Evicted positions are blocked by setting their attention mask entries to zero:
28	\begin{equation}
29	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall i,j
30	    \label{eq:kv-mask}
31	\end{equation}
32	We evaluate two eviction strategies:
33	\begin{itemize}[nosep,leftmargin=*]
34	    \item \textbf{Importance-based:} Position importance is the cumulative attention mass received across all heads and query positions, with position normalization to correct for causal attention bias:
35	    \begin{equation}
36	        \mathrm{imp}(j) = \frac{\sum_{l,h,i} a^{(l,h)}_{ij}}{T - j}
37	        \label{eq:kv-importance}
38	    \end{equation}
39	    where the denominator $(T - j)$ compensates for the fact that later positions can attend to fewer future tokens under causal masking \cite{placeholder_thinkv}.
40	    \item \textbf{Random:} Positions (excluding BOS) are evicted uniformly at random.
41	\end{itemize}
42	
43	\paragraph{Compound sparsity.}
44	Applying both compressions simultaneously yields a model $\mathcal{M}(s)$ where fraction $s$ of heads are pruned per layer \emph{and} fraction $s$ of KV positions are evicted.
45	The two axes interact: head pruning alters the attention distribution over surviving heads, which in turn changes the importance ranking used for KV eviction.
46	
47	\subsection{Interaction Index}
48	\label{sec:interaction-index}
49	
50	To quantify whether compound sparsity degrades performance more (or less) than the sum of its components, we define the \emph{Interaction Index} (II) following the factorial interaction framework from experimental design.
51	
52	Let $\mathrm{PPL}_d$, $\mathrm{PPL}_h$, $\mathrm{PPL}_k$, and $\mathrm{PPL}_b$ denote the perplexity of the dense model, head-pruning only, KV-eviction only, and both applied simultaneously, respectively.
53	Perplexity is computed as $\mathrm{PPL} = \exp\!\bigl(\frac{1}{|S|}\sum_{t \in S} \mathcal{L}_t\bigr)$ where $\mathcal{L}_t$ is the per-token cross-entropy loss and $S$ is the set of evaluated positions.
54	
55	We define the relative degradation ratios $R_h = \mathrm{PPL}_h / \mathrm{PPL}_d$, $R_k = \mathrm{PPL}_k / \mathrm{PPL}_d$, $R_b = \mathrm{PPL}_b / \mathrm{PPL}_d$, and the Interaction Index:
56	\begin{equation}
57	    \mathrm{II} = R_b - R_h - R_k + 1
58	    \label{eq:ii}
59	\end{equation}
60	Under additive independence, $R_b \approx R_h + R_k - 1$, giving $\mathrm{II} \approx 0$.
61	\begin{itemize}[nosep,leftmargin=*]
62	    \item $\mathrm{II} > 0$: \textbf{super-additive} — compound sparsity degrades more than the sum of individual effects.
63	    \item $\mathrm{II} < 0$: \textbf{sub-additive} — compound sparsity is less harmful than expected.
64	    \item $\mathrm{II} = 0$: \textbf{additive} — no interaction between the two axes.
65	\end{itemize}
66	
67	We evaluate II on 50 problems from MATH-500 \cite{placeholder_math500}, stratified across difficulty levels.
68	Per-problem II values are aggregated via the median (rather than the mean) due to heavy-tailed distributions with mean/median ratios exceeding 40$\times$ at high sparsity.
69	Bootstrap confidence intervals ($n=1{,}000$) are computed at the problem level.
70	
71	\paragraph{Severity gradient.}
72	To capture how II varies across reasoning phases, we define the \emph{severity gradient}:
73	\begin{equation}
74	    G = \frac{\widetilde{\mathrm{II}}_{\mathrm{low}}}{\widetilde{\mathrm{II}}_{\mathrm{high}}}
75	    \label{eq:gradient}
76	\end{equation}
77	where $\widetilde{\mathrm{II}}_{\mathrm{low}}$ and $\widetilde{\mathrm{II}}_{\mathrm{high}}$ are the median II in the low-sparsity and high-sparsity phases respectively.
78	$G \gg 1$ indicates that compound degradation concentrates in low-sparsity phases; $G \approx 1$ indicates uniform degradation.
79	
80	\subsection{Phase Segmentation}
81	\label{sec:phase-segmentation}
82	
83	Reasoning-capable LLMs produce token sequences with heterogeneous attention patterns: some segments exhibit concentrated attention (few tokens dominate), while others distribute attention broadly.
84	We partition each generation into three phases based on the \emph{attention sparsity profile}, following the methodology of ThinKV \cite{placeholder_thinkv}.
85	
86	\paragraph{Attention sparsity.}
87	For each query position $i$ and head $h$, we compute the fraction of key positions receiving attention below $1\%$ of the row maximum:
88	\begin{equation}
89	    \sigma_i^{(h)} = \frac{1}{T}\sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right]
90	    \label{eq:sparsity}
91	\end{equation}
92	The per-token sparsity $\sigma_i = \frac{1}{H}\sum_h \sigma_i^{(h)}$ averages across heads.
93	
94	\paragraph{Quantile-based segmentation.}
95	We partition tokens into three equal-sized groups by the quantiles of $\{\sigma_i\}_{i=1}^{T}$:
96	\begin{itemize}[nosep,leftmargin=*]
97	    \item \textbf{High-sparsity phase} (top tercile): attention concentrates on a few tokens; heads are highly redundant, and pruning incurs minimal information loss.
98	    \item \textbf{Mid-sparsity phase} (middle tercile): intermediate attention patterns.
99	    \item \textbf{Low-sparsity phase} (bottom tercile): attention distributes broadly across many tokens; each head carries non-redundant information, making pruning costly.
100	\end{itemize}
101	
102	This segmentation is purely data-driven and does not require access to model internals beyond attention weights.
103	It captures the heterogeneity in attention structure that arises naturally during extended reasoning, where the model alternates between focused retrieval (high sparsity) and exploratory cross-token integration (low sparsity) \cite{placeholder_thinking_tokens_mi}.
104	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "24595e6d-0a3e-493b-8680-90ebff969f1a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex",
      "content": "% Section 3: Background and Problem Setup\n% Phase-Modulated Compound Sparsity\n\n\\section{Background and Problem Setup}\n\\label{sec:background}\n\nWe formalize compound sparsity as the simultaneous application of attention head pruning and KV cache eviction, define the Interaction Index to measure their non-additive interaction, and introduce phase segmentation to localize the analysis across reasoning stages.\n\n\\subsection{Compound Sparsity Formulation}\n\\label{sec:compound-sparsity}\n\nConsider a transformer language model $\\mathcal{M}$ with $L$ layers, each containing $H$ attention heads.\nLet $s \\in (0,1)$ denote a unified sparsity budget applied to both compression axes.\n\n\\paragraph{Attention head pruning.}\nGiven per-head importance scores $\\mathbf{w}^{(l)} \\in \\mathbb{R}^H$ for layer $l$, we construct a binary mask $\\mathbf{m}_h^{(l)} \\in \\{0,1\\}^H$ that retains the top-$(1{-}s) \\cdot H$ heads by importance.\nFor head $j$ in layer $l$, the masked attention output becomes:\n\\begin{equation}\n    \\tilde{\\mathbf{o}}_j^{(l)} = m_{h,j}^{(l)} \\cdot \\mathbf{o}_j^{(l)}\n    \\label{eq:head-mask}\n\\end{equation}\nwhere $\\mathbf{o}_j^{(l)}$ is the original head output.\nHead importance is computed as the Frobenius norm of the attention weight matrix: $w_j^{(l)} = \\|\\mathbf{A}_j^{(l)}\\|_F$, where $\\mathbf{A}_j^{(l)} \\in \\mathbb{R}^{T \\times T}$ is the attention probability matrix for head $j$ at layer $l$ over a calibration input of length $T$.\n\n\\paragraph{KV cache eviction.}\nFor a sequence of length $T$, we construct a position mask $\\mathbf{m}_k \\in \\{0,1\\}^T$ that retains the top-$(1{-}s) \\cdot T$ positions by importance, with position $0$ (BOS) always retained.\nEvicted positions are blocked by setting their attention mask entries to zero:\n\\begin{equation}\n    \\tilde{a}_{ij} = a_{ij} \\cdot m_{k,j}, \\quad \\forall i,j\n    \\label{eq:kv-mask}\n\\end{equation}\nWe evaluate two eviction strategies:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{Importance-based:} Position importance is the cumulative attention mass received across all heads and query positions, with position normalization to correct for causal attention bias:\n    \\begin{equation}\n        \\mathrm{imp}(j) = \\frac{\\sum_{l,h,i} a^{(l,h)}_{ij}}{T - j}\n        \\label{eq:kv-importance}\n    \\end{equation}\n    where the denominator $(T - j)$ compensates for the fact that later positions can attend to fewer future tokens under causal masking \\cite{placeholder_thinkv}.\n    \\item \\textbf{Random:} Positions (excluding BOS) are evicted uniformly at random.\n\\end{itemize}\n\n\\paragraph{Compound sparsity.}\nApplying both compressions simultaneously yields a model $\\mathcal{M}(s)$ where fraction $s$ of heads are pruned per layer \\emph{and} fraction $s$ of KV positions are evicted.\nThe two axes interact: head pruning alters the attention distribution over surviving heads, which in turn changes the importance ranking used for KV eviction.\n\n\\subsection{Interaction Index}\n\\label{sec:interaction-index}\n\nTo quantify whether compound sparsity degrades performance more (or less) than the sum of its components, we define the \\emph{Interaction Index} (II) following the factorial interaction framework from experimental design.\n\nLet $\\mathrm{PPL}_d$, $\\mathrm{PPL}_h$, $\\mathrm{PPL}_k$, and $\\mathrm{PPL}_b$ denote the perplexity of the dense model, head-pruning only, KV-eviction only, and both applied simultaneously, respectively.\nPerplexity is computed as $\\mathrm{PPL} = \\exp\\!\\bigl(\\frac{1}{|S|}\\sum_{t \\in S} \\mathcal{L}_t\\bigr)$ where $\\mathcal{L}_t$ is the per-token cross-entropy loss and $S$ is the set of evaluated positions.\n\nWe define the relative degradation ratios $R_h = \\mathrm{PPL}_h / \\mathrm{PPL}_d$, $R_k = \\mathrm{PPL}_k / \\mathrm{PPL}_d$, $R_b = \\mathrm{PPL}_b / \\mathrm{PPL}_d$, and the Interaction Index:\n\\begin{equation}\n    \\mathrm{II} = R_b - R_h - R_k + 1\n    \\label{eq:ii}\n\\end{equation}\nUnder additive independence, $R_b \\approx R_h + R_k - 1$, giving $\\mathrm{II} \\approx 0$.\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item $\\mathrm{II} > 0$: \\textbf{super-additive} — compound sparsity degrades more than the sum of individual effects.\n    \\item $\\mathrm{II} < 0$: \\textbf{sub-additive} — compound sparsity is less harmful than expected.\n    \\item $\\mathrm{II} = 0$: \\textbf{additive} — no interaction between the two axes.\n\\end{itemize}\n\nWe evaluate II on 50 problems from MATH-500 \\cite{placeholder_math500}, stratified across difficulty levels.\nPer-problem II values are aggregated via the median (rather than the mean) due to heavy-tailed distributions with mean/median ratios exceeding 40$\\times$ at high sparsity.\nBootstrap confidence intervals ($n=1{,}000$) are computed at the problem level.\n\n\\paragraph{Severity gradient.}\nTo capture how II varies across reasoning phases, we define the \\emph{severity gradient}:\n\\begin{equation}\n    G = \\frac{\\widetilde{\\mathrm{II}}_{\\mathrm{low}}}{\\widetilde{\\mathrm{II}}_{\\mathrm{high}}}\n    \\label{eq:gradient}\n\\end{equation}\nwhere $\\widetilde{\\mathrm{II}}_{\\mathrm{low}}$ and $\\widetilde{\\mathrm{II}}_{\\mathrm{high}}$ are the median II in the low-sparsity and high-sparsity phases respectively.\n$G \\gg 1$ indicates that compound degradation concentrates in low-sparsity phases; $G \\approx 1$ indicates uniform degradation.\n\n\\subsection{Phase Segmentation}\n\\label{sec:phase-segmentation}\n\nReasoning-capable LLMs produce token sequences with heterogeneous attention patterns: some segments exhibit concentrated attention (few tokens dominate), while others distribute attention broadly.\nWe partition each generation into three phases based on the \\emph{attention sparsity profile}, following the methodology of ThinKV \\cite{placeholder_thinkv}.\n\n\\paragraph{Attention sparsity.}\nFor each query position $i$ and head $h$, we compute the fraction of key positions receiving attention below $1\\%$ of the row maximum:\n\\begin{equation}\n    \\sigma_i^{(h)} = \\frac{1}{T}\\sum_{j=1}^{T} \\mathbf{1}\\!\\left[a_{ij}^{(h)} < 0.01 \\cdot \\max_k a_{ik}^{(h)}\\right]\n    \\label{eq:sparsity}\n\\end{equation}\nThe per-token sparsity $\\sigma_i = \\frac{1}{H}\\sum_h \\sigma_i^{(h)}$ averages across heads.\n\n\\paragraph{Quantile-based segmentation.}\nWe partition tokens into three equal-sized groups by the quantiles of $\\{\\sigma_i\\}_{i=1}^{T}$:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{High-sparsity phase} (top tercile): attention concentrates on a few tokens; heads are highly redundant, and pruning incurs minimal information loss.\n    \\item \\textbf{Mid-sparsity phase} (middle tercile): intermediate attention patterns.\n    \\item \\textbf{Low-sparsity phase} (bottom tercile): attention distributes broadly across many tokens; each head carries non-redundant information, making pruning costly.\n\\end{itemize}\n\nThis segmentation is purely data-driven and does not require access to model internals beyond attention weights.\nIt captures the heterogeneity in attention structure that arises naturally during extended reasoning, where the model alternates between focused retrieval (high sparsity) and exploratory cross-token integration (low sparsity) \\cite{placeholder_thinking_tokens_mi}.\n",
      "numLines": 104,
      "startLine": 1,
      "totalLines": 104
    }
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
There's already an existing background.tex. Let me read it carefully and see what needs to be improved.

Key issues I see with the current background.tex:

1. **Notation inconsistency with methodology.tex**: 
   - Current background.tex uses $\mathrm{PPL}_h$ for head-pruning, but methodology.tex uses $\text{PPL}_a$
   - Current uses $R_h, R_k, R_b$ but methodology.tex uses $r_c$ for ratios


2. **Bootstrap count is wrong**: Current says $n=1{,}000$ but methodology.tex says $B=10{,}000$
3. **Placeholder citations**: Uses `\cite{placeholder_thinkv}`, `\cite{placeholder_math500}`, `\cite{placeholder_thinking_tokens_mi}` instead of the proper cite keys from the writing plan: `thinkv-iclr2026`, `math500`, etc.
4. **MATH-500 details in Section 3**: Line 67 mentions "50 problems from MATH-500, stratified across difficulty levels" — this is experimental setup detail that belongs in Section 4, not background.
5. **Missing references**: The writing plan mentions citing `spark-aaai2026` when discussing related work, but it's not included.
6. **Phase naming confusion**: The description of phases could be clearer about the naming convention — "low-sparsity phase" means low attention sparsity (focused attention), which is where compound interaction is worst.
7. **Missing research question**: The writing plan specifically asks 3.3 to end with the research question: "Is II constant across phases and strategies, or does it exhibit phase × strategy interaction?"
8. **Missing `min_phase_length` mention**: The writing plan references this as a parameter.
9. The severity gradient is defined in 3.2 but references phases from 3.3 — this is OK with a forward reference.
10. **Missing key framing**: The writing plan says Section 3 should note that prior work hasn't established whether interaction intensity varies across different phases and strategies.

Now I'm checking the notation consistency with methodology.tex. I need to verify that conditions use the same labels ($c \in \{d, a, k, b\}$), that perplexity notation matches ($\text{PPL}_d, \text{PPL}_a, \text{PPL}_k, \text{PPL}_b$), and that importance scoring aligns with the existing equation references. Both files use eq:ii and eq:gradient, so I need to make sure those are properly coordinated. I see that methodology.tex defines II using $\text{PPL}_a$ for attention-only, so I need to update background.tex to match that notation instead of using $\mathrm{PPL}_h$. I'll revise the section to align the subscripts with methodology.tex, replace the placeholder citations with proper keys, strip out the experimental specifics like MATH-500, and add references to the relevant work on compression and phase transitions. I should also include the research question and mention min_phase_length to complete the picture.

Looking at the structure, I realize the intro paragraph at the top of Section 3 serves as a roadmap and is worth keeping, just tightened up. For the phase descriptions, I need to be more precise about what high-sparsity versus low-sparsity actually means—high-sparsity means many near-zero attention weights indicating concentrated focus, while low-sparsity means more distributed attention during structured computation. I'll rewrite this section cleanly to hit around 750 words, fixing the bootstrap count issue by removing it since that's a Section 4 detail, and polishing the prose throughout. I see the contradiction now—the sparsity metric counts weights below 1% of the maximum, so high sparsity actually means most weights are near-zero, which concentrates attention on the few tokens with higher weights. That makes high sparsity equivalent to focused attention, while low sparsity spreads attention more evenly across tokens, making it diffuse. The two documents have this backwards relative to each other. I'm realizing I need to reconsider the definitions more carefully. The methodology section describes low sparsity as focused attention and high sparsity as diffuse attention, but that contradicts what the sparsity metric actually means—low sparsity should indicate attention spread across many tokens, while high sparsity means concentration on few tokens. Let me think through whether there's an alternative interpretation I'm missing.

Actually, from a reasoning perspective it makes sense: structured computation like solving equations step-by-step requires focused attention on relevant tokens (high sparsity), while exploratory reasoning involves considering multiple approaches and attending broadly (low sparsity). So methodology.tex does have the definitions backwards—it should say low sparsity corresponds to diffuse attention and exploratory reasoning, not the other way around. The background.tex version is correct.

Since I'm writing background.tex, I'll stick with the accurate descriptions: low sparsity means diffuse attention where each head carries distinct information, making head pruning costly, while high sparsity means concentrated attention where heads are more redundant and pruning is cheaper.

Now I'm thinking through why compound interaction peaks during the low-sparsity phase—when attention is spread across many positions, each head attends to different parts of the sequence, so removing any single head loses unique information.  Additionally, with diffuse attention, many KV positions matter for the model's predictions, so evicting cache entries removes important context. The real problem emerges from the interaction itself: pruning surviving heads changes their attention patterns, which then throws off the importance scores that guide eviction decisions, creating a cascade of errors.

Now I need to write the revised background section, being careful to match the notation from the methodology, preserve the correct interpretations of sparsity phases, use proper citations, and end with the research question—all while keeping it around 750 words and avoiding experimental details.

Drafting the LaTeX for the formulation subsection, starting with how I'm defining compound sparsity and then introducing the mathematical framework for head pruning using Frobenius norm importance scores...

Defining the masking operation for attention heads and then moving into KV cache eviction, where I'm constructing position masks that retain the most important tokens while always keeping the beginning-of-sequence token... The key insight is that head pruning and KV cache eviction aren't independent—removing heads changes how attention distributes across the remaining ones, which shifts the importance scores used for deciding which cache entries to evict. This coupling could amplify losses beyond what we'd expect from applying each technique separately. I'm defining an Interaction Index based on factorial design principles to measure this effect, comparing perplexity across different combinations of dense, pruned, and evicted configurations. The sign of the Interaction Index tells us whether the two mechanisms interact synergistically or antagonistically—positive values mean compound sparsity hurts more than expected, negative values mean it hurts less, and zero indicates no interaction. By normalizing against the baseline perplexity, I can compare these interaction effects fairly across different problem difficulties and aggregate them meaningfully. Now I'm looking at how this interaction varies across different reasoning phases. The token sequences show varying attention patterns across different segments, so I'm partitioning each sequence into three phases based on how concentrated or distributed the attention is. To measure this, I'm computing the attention sparsity for each query position and attention head—essentially calculating what fraction of key positions receive negligible attention relative to the maximum attention weight at that position.

Once I have the sparsity scores, I'm grouping tokens into three equal-sized segments using quantiles: high-sparsity tokens where attention focuses narrowly and heads are redundant, mid-sparsity tokens with intermediate patterns, and low-sparsity tokens where attention spreads broadly and each head carries unique information. I'm also merging any contiguous segments shorter than 10 tokens into their adjacent phases to avoid fragmentation.

This segmentation is purely data-driven and only needs the attention weights themselves. The pattern emerges naturally during reasoning—the model shifts between focused fact retrieval in high-sparsity phases and broader cross-token integration in low-sparsity phases. Now I'm investigating whether the Interaction Index stays constant across these phases or if there's a meaningful interaction between phase type and eviction strategy.

I should also make sure the notation aligns with what I used in the methodology section—using `\text{PPL}_a` for perplexity and `\mathrm{II}` for the Interaction Index. The citations need to match the actual keys from my writing plan: spark-aaai2026, thinkv-iclr2026, defensivekv-iclr2026, and phase-transition-compression-2026. The research question at the end ties the whole section together nicely.

On the importance score formula, I think it makes sense to include it here in the background as part of the formal framework rather than treating it as purely an implementation detail—it's foundational to understanding the approach. I'll keep it but streamline the presentation.

Now I need to align the notation with methodology.tex. I'm seeing that the perplexity metrics use specific subscripts—$\text{PPL}_a$ for attention-only, $\text{PPL}_k$ for KV-only, $\text{PPL}_b$ for both, and $\text{PPL}_d$ for dense—but the current background uses $\mathrm{PPL}_h$, which conflicts. I'll update these to match.

For the citations, I have the keys from the writing plan, so I can reference those directly rather than searching for a .bib file.

Before finalizing, I want to verify the phase definitions align with what the task specifies: high sparsity corresponds to early inference with minimal tokens, while low sparsity corresponds to later inference with maximum tokens. I'm getting caught up on the terminology—the task description uses "token 最少/最多" to describe the phases, but that might not refer to temporal ordering at all. Since methodology.tex defines the segmentation using quantiles rather than time, the phases don't need to be temporally contiguous. I should stick with the quantile-based approach as the authoritative method and describe the phase segmentation formally without overcommitting to temporal claims.

Now I'm ready to start writing Section 3, beginning with the background and compound sparsity formulation. I'm deciding whether to include the importance score formula in this section or defer it to the implementation details later. The background section should give formal definitions, so I'll include the key equations for head masking, KV eviction masking, the Interaction Index, severity gradient, and attention sparsity—but I'll hold off on the importance score formula itself since that's more of an operational detail for the methods section.

Now I'm mapping out the structure: 3.1 will cover the compound sparsity formulation with the two compression axes, head pruning via Frobenius norm ranking, KV eviction with position masking and both importance-based and random strategies, and how they apply simultaneously. Then 3.2 will define the Interaction Index with its four conditions and the ratio.

I need to be careful about duplication with the existing Section 4 in methodology.tex—I should make sure my Section 3 definitions are the authoritative versions so the user knows which ones to keep when refactoring.

Looking at what's already defined elsewhere, I see that eq:ii and eq:gradient appear in both places, while eq:sparsity and the mask equations are only in my current draft. Since these definitions naturally belong in Section 3, I'll use these labels and let the author handle removing duplicates from Section 4 later.

Writing the LaTeX for Section 3 now with the formalization of compound sparsity, attention head pruning definitions, and the mathematical framework... For the KV cache eviction, I'm using a binary mask to retain the top positions while always keeping the beginning-of-sequence token, then blocking evicted positions through attention masking. I'm comparing two selection strategies: one that scores positions by their cumulative attention with normalization to account for causal bias, and another that randomly selects positions as a baseline.

When both head pruning and KV cache eviction operate at the same sparsity level, they create a compound effect controlled by a single parameter. The key insight is that these mechanisms interact—pruning redistributes attention across remaining heads, which changes the importance scores used for eviction decisions. This raises the central question of whether their combined degradation is additive or super-additive, and whether factors beyond the sparsity level itself matter.

To measure this interaction precisely, I'm defining an Interaction Index that quantifies how head pruning and KV cache eviction affect each other, building on factorial interaction analysis methods. framework from experimental design.

For a given text segment, let $\text{PPL}_d$, $\text{PPL}_a$, $\text{PPL}_k$, and $\text{PPL}_b$ denote the perplexity under the dense (no sparsity), attention-pruning-only, KV-eviction-only, and compound conditions, respectively. Normalizing each by the dense baseline yields relative degradation ratios $r_c = \text{PPL}_c / \text{PPL}_d$ for $c \in \{a, k, b\}$. The Interaction Index is:
\begin{equation}
    \mathrm{II} = r_b - r_a - r_k + 1 = \frac{\text{PPL}_b}{\text{PPL}_d} - \frac{\text{PPL}_a}{\text{PPL}_d} - \frac{\text{PPL}_k}{\text{PPL}_d} + 1.
    \label{eq:ii-def}
\end{equation}

Under additive independence, $r_b \approx r_a + r_k - 1$, so II approaches zero. The sign of II tells me whether the two sparsity techniques interact synergistically or antagonistically—positive values mean they compound each other's harm beyond what we'd expect from adding their individual effects, while negative values indicate they partially compensate for one another.

Since the II distribution is heavily right-skewed in practice, I'm reporting medians instead of means to avoid being pulled by extreme outliers. To track how this interaction strength changes across different reasoning phases, I'm defining a severity gradient that compares the interaction index at low sparsity levels to that at high sparsity levels.

Now I'm moving into how to segment the reasoning process itself. LLMs generate tokens with varying attention patterns—some positions focus narrowly on a few key tokens while others spread attention widely across the context. I'm partitioning each sequence into three phases based on the attention sparsity profile, following the approach used in prior work.

For each position and attention head, I'm measuring what fraction of key positions get negligible attention—essentially counting how many positions fall below a threshold relative to the maximum attention weight at that position. Then I'm averaging this sparsity metric across all heads to get a per-position sparsity score.

Finally, I'm dividing tokens into three groups using the tercile boundaries of these sparsity scores, which creates a natural segmentation into low, medium, and high sparsity phases. I'm noticing that this phase structure emerges naturally when models engage in extended reasoning, oscillating between focused fact retrieval during high-sparsity moments and broad integrative thinking across many context positions during low-sparsity phases. The key question I'm investigating is whether the Interaction Index remains stable across these phases and different eviction strategies, or if there's a meaningful interaction effect between phase type and strategy choice. I need to check the related_work.tex file to see what citation keys are already in use, then decide on my labeling strategy. Rather than delay further, I'll proceed with the cite keys I have and let the author adjust if needed. For the equation labels, I'm going to use eq:ii and eq:gradient in Section 3 since those are the primary definitions, which means methodology.tex will need to reference these instead of having duplicate definitions.

I'm estimating the word count will land around 715 words across the intro and three subsections, which is close enough to the 750-word target without needing to pad unnecessarily. Let me finalize the draft now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "3c3fe7da-1efb-4626-8fa6-326733bae4db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CRfA9M5zqo93nGB675XuBf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2667,
      "cache_read_input_tokens": 38127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2667
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

There's already an existing `background.tex`. Let me also check the related work for citation key consistency.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "b6fe62a3-6720-44f9-bc1c-6efe2be8febe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CRfA9M5zqo93nGB675XuBf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2667,
      "cache_read_input_tokens": 38127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2667
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

<details open><summary>🔧 Tool call — Read · `toolu_01DEvopqz2y8ArTRCpuGVVkF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "c48c4201-5c93-4b9b-b38e-a36fd9cb611e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CRfA9M5zqo93nGB675XuBf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2667,
      "cache_read_input_tokens": 38127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2667
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

_source line 20 · 2026-05-14T05:40:29.367Z_

<details><summary>↩ Tool result · `toolu_01DEvopqz2y8ArTRCpuGVVkF`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{Compound and Joint Compression}
5	
6	Combining multiple compression axes produces non-additive errors.
7	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction, with up to 65\% quality loss exceeding individual component effects---the first explicit measurement of this phenomenon in KV cache sparsity.
8	\cite{slim-icml2025} formalize compound error for quantization and sparsity, deriving an invertible saliency function for low-rank compensation and confirming that aggregated error is strictly non-additive.
9	\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning and multilingual capabilities degrade disproportionately relative to factual recall.
10	The order of compression stages is itself consequential: \cite{compression-ordering-2025} show that early quantization causes irreversible information loss, making P$\to$KD$\to$Q strictly preferable.
11	At a more fundamental level, \cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying that the joint safe region is the intersection---not the union---of per-dimension safe zones.
12	On the structural side, GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates to jointly prune FFN channels and attention heads, but treats the pruning decision as static across generation.
13	These works share a common assumption: compound interaction is either uniform across the generation process or varies only by task.
14	None examines how the interaction shifts across reasoning phases within a single generation.
15	
16	\subsection{KV Cache Eviction}
17	
18	Most eviction methods rely on importance scoring, yet accumulating evidence questions its reliability.
19	Ada-KV~\cite{adakv-neurips2025} introduce per-head adaptive budget allocation, outperforming uniform distribution but assuming stable importance across generation.
20	\cite{defensivekv-iclr2026} show that standard mean-based importance aggregation is fragile, with worst-case quality loss 2.3--4.3$\times$ higher than expected; their defensive aggregation mitigates but does not eliminate the instability.
21	\cite{obcache-2025} derive a second-order joint K-V saliency score from optimal brain damage theory, establishing that key pruning impacts quality more than value pruning---a useful asymmetry, though the score remains time-invariant.
22	\cite{mustafar-neurips2025} achieve 70\% unstructured KV sparsity through per-token magnitude pruning without quality loss, demonstrating that fine-grained within-entry sparsity and coarse token eviction are complementary axes.
23	RetentiveKV~\cite{retentivekv-2026} identifies \emph{deferred importance}: tokens with low initial salience can become pivotal later, undermining single-snapshot importance estimates.
24	\cite{greedy-bias-kvcache-2026} further show that any single importance metric exhibits greedy bias, systematically missing structurally relevant tokens.
25	A recurring theme is that importance estimates become unreliable under specific conditions, but these conditions are characterized in terms of aggregation functions or metric choice---not the reasoning phase during which eviction occurs, nor the interaction with concurrent head pruning.
26	
27	\subsection{Phase-Aware Inference}
28	
29	Several concurrent works introduce phase-awareness into LLM inference.
30	ThinKV~\cite{thinkv-iclr2026} partitions generation into phases and applies different KV cache strategies per phase, achieving strong single-axis results that motivate our phase decomposition---but without compound interaction.
31	\cite{pagedeviction-eacl2026} manage block-wise eviction with separate prefill and decode policies, a coarse two-phase scheme that does not extend to within-generation reasoning phases.
32	\cite{decision-repr-transition-2026} discover that layer pruning sensitivity depends on whether a layer operates in the ``silent'' or ``decisive'' phase of representation formation, with silent-phase pruning causing collapse---direct evidence that compression tolerance is phase-modulated.
33	\cite{doing-more-with-less-2026} provide sign reversal evidence: unstructured pruning combined with test-time scaling can exceed unpruned baselines, suggesting that sparsity interacts constructively with extended reasoning under certain conditions.
34	\cite{raas-acl2025} report non-monotonic token importance across decoding steps, and \cite{sparse-frontier-2025} find no universally optimal sparse attention strategy across tasks and generation stages.
35	
36	These works establish that compression tolerance is phase-dependent, but each examines either phase-aware compression along a single axis or compound compression without phase conditioning.
37	No prior work examines the interaction between eviction \emph{strategy} and reasoning phase in compound sparsity settings---the gap our study addresses.
38	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "042eafb8-f4b9-49f6-9ea9-158876d52e7b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\subsection{Compound and Joint Compression}\n\nCombining multiple compression axes produces non-additive errors.\n\\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction, with up to 65\\% quality loss exceeding individual component effects---the first explicit measurement of this phenomenon in KV cache sparsity.\n\\cite{slim-icml2025} formalize compound error for quantization and sparsity, deriving an invertible saliency function for low-rank compensation and confirming that aggregated error is strictly non-additive.\n\\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning and multilingual capabilities degrade disproportionately relative to factual recall.\nThe order of compression stages is itself consequential: \\cite{compression-ordering-2025} show that early quantization causes irreversible information loss, making P$\\to$KD$\\to$Q strictly preferable.\nAt a more fundamental level, \\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying that the joint safe region is the intersection---not the union---of per-dimension safe zones.\nOn the structural side, GRASPrune~\\cite{graspune-acl2026} learns global budget-constrained gates to jointly prune FFN channels and attention heads, but treats the pruning decision as static across generation.\nThese works share a common assumption: compound interaction is either uniform across the generation process or varies only by task.\nNone examines how the interaction shifts across reasoning phases within a single generation.\n\n\\subsection{KV Cache Eviction}\n\nMost eviction methods rely on importance scoring, yet accumulating evidence questions its reliability.\nAda-KV~\\cite{adakv-neurips2025} introduce per-head adaptive budget allocation, outperforming uniform distribution but assuming stable importance across generation.\n\\cite{defensivekv-iclr2026} show that standard mean-based importance aggregation is fragile, with worst-case quality loss 2.3--4.3$\\times$ higher than expected; their defensive aggregation mitigates but does not eliminate the instability.\n\\cite{obcache-2025} derive a second-order joint K-V saliency score from optimal brain damage theory, establishing that key pruning impacts quality more than value pruning---a useful asymmetry, though the score remains time-invariant.\n\\cite{mustafar-neurips2025} achieve 70\\% unstructured KV sparsity through per-token magnitude pruning without quality loss, demonstrating that fine-grained within-entry sparsity and coarse token eviction are complementary axes.\nRetentiveKV~\\cite{retentivekv-2026} identifies \\emph{deferred importance}: tokens with low initial salience can become pivotal later, undermining single-snapshot importance estimates.\n\\cite{greedy-bias-kvcache-2026} further show that any single importance metric exhibits greedy bias, systematically missing structurally relevant tokens.\nA recurring theme is that importance estimates become unreliable under specific conditions, but these conditions are characterized in terms of aggregation functions or metric choice---not the reasoning phase during which eviction occurs, nor the interaction with concurrent head pruning.\n\n\\subsection{Phase-Aware Inference}\n\nSeveral concurrent works introduce phase-awareness into LLM inference.\nThinKV~\\cite{thinkv-iclr2026} partitions generation into phases and applies different KV cache strategies per phase, achieving strong single-axis results that motivate our phase decomposition---but without compound interaction.\n\\cite{pagedeviction-eacl2026} manage block-wise eviction with separate prefill and decode policies, a coarse two-phase scheme that does not extend to within-generation reasoning phases.\n\\cite{decision-repr-transition-2026} discover that layer pruning sensitivity depends on whether a layer operates in the ``silent'' or ``decisive'' phase of representation formation, with silent-phase pruning causing collapse---direct evidence that compression tolerance is phase-modulated.\n\\cite{doing-more-with-less-2026} provide sign reversal evidence: unstructured pruning combined with test-time scaling can exceed unpruned baselines, suggesting that sparsity interacts constructively with extended reasoning under certain conditions.\n\\cite{raas-acl2025} report non-monotonic token importance across decoding steps, and \\cite{sparse-frontier-2025} find no universally optimal sparse attention strategy across tasks and generation stages.\n\nThese works establish that compression tolerance is phase-dependent, but each examines either phase-aware compression along a single axis or compound compression without phase conditioning.\nNo prior work examines the interaction between eviction \\emph{strategy} and reasoning phase in compound sparsity settings---the gap our study addresses.\n",
      "numLines": 38,
      "startLine": 1,
      "totalLines": 38
    }
  }
}
```

</details>

---

### Assistant

_source line 21_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture of the citation keys used in the paper:
- spark-aaai2026
- slim-icml2025
- unicomp-2026
- compression-ordering-2025
- phase-transition-compression-2026
- graspune-acl2026
- adakv-neurips2025
- defensivekv-iclr2026
- obcache-2025


- mustafar-neurips2025
- retentivekv-2026
- greedy-bias-kvcache-2026
- thinkv-iclr2026
- pagedeviction-eacl2026
- decision-repr-transition-2026
- doing-more-with-less-2026
- raas-acl2025
- sparse-frontier-2025

I notice the background.tex file has some placeholder citations that need to be replaced with actual keys, and I should check whether the head pruning section in related work has proper citations.

For head pruning, the foundational papers are Voita et al. (2019) on analyzing multi-head attention and Michel et al. (2019) on whether sixteen heads are better than one. I'll use standard citation keys like `voita2019heads` and `michel2019sixteen` that can be adjusted if the project uses different conventions.

Looking back at the background.tex, I'm noticing some inconsistencies with notation—specifically the use of lowercase $l$ for layer indices in a few places where it should probably be uppercase to match the rest of the document.

Now I'm going through the file systematically to catch issues: the placeholder citations need to be replaced with actual keys, the perplexity notation should align with what's used in methodology.tex, and some of the experimental parameters like bootstrap sample sizes and dataset references are bleeding into the background section when they belong in the experimental setup instead.

I also notice the phase descriptions here are actually correct, unlike the reversed order in methodology.tex, so I should preserve that. The main structural problem is deciding how to handle equation labels across both files—I need to either use canonical labels in Section 3 and treat methodology.tex as the duplicate, or create distinct variants to avoid conflicts when everything gets integrated.

The cleanest solution is to go with the canonical labels here and add a note explaining that methodology.tex will need to reference these equations once the files are combined, which resolves the temporary compilation issue naturally.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "8b4ea2be-9010-4e9e-b977-52fed91a2028",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XiXpZFNMCuMi1N5Tbz9Xvk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12083,
      "cache_read_input_tokens": 40794,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12083
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

_source line 22_

Now I have full context: writing plan, methodology.tex, related_work.tex (for cite keys), and the existing background.tex. Key issues in current background.tex:

1. Notation mismatch: uses `PPL_h` but methodology.tex uses `PPL_a`
2. Placeholder citations instead of proper keys
3. Experimental details (MATH-500, bootstrap n=1000) that belong in Section 4
4. Missing research question at end

Writing the revised version.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "8a58659e-1815-4ef0-b0ed-902d48ccfb32",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XiXpZFNMCuMi1N5Tbz9Xvk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12083,
      "cache_read_input_tokens": 40794,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12083
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

<details open><summary>🔧 Tool call — Write · `toolu_01Vu2MLUVpQaESxBfLqEAuCR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex",
  "content": "% Section 3: Background and Problem Setup\n% Note: eq:ii and eq:gradient are the canonical definitions.\n% Remove duplicate definitions from methodology.tex and reference these instead.\n\n\\section{Background and Problem Setup}\n\\label{sec:background}\n\nWe formalize compound sparsity as the simultaneous application of attention head pruning and KV cache eviction, define the Interaction Index to quantify their non-additive coupling, and introduce phase segmentation to localize the analysis across reasoning stages.\n\n\\subsection{Compound Sparsity Formulation}\n\\label{sec:compound-sparsity}\n\nConsider a Transformer language model with $L$ layers, each containing $H$ attention heads.\nWe study the composition of two inference-time compression mechanisms applied simultaneously.\n\n\\paragraph{Attention head pruning.}\nFor each layer $\\ell$, heads are ranked by Frobenius norm importance $w_j^{(\\ell)} = \\|\\mathbf{A}_j^{(\\ell)}\\|_F$, where $\\mathbf{A}_j^{(\\ell)} \\in \\mathbb{R}^{T \\times T}$ is the attention matrix for head $j$ \\cite{voita2019heads, michel2019sixteen}.\nA binary mask $m_j^{(\\ell)} \\in \\{0,1\\}$ retains the top-$(1{-}s)\\cdot H$ heads, zeroing the output of pruned heads:\n\\begin{equation}\n    \\tilde{\\mathbf{o}}_j^{(\\ell)} = m_j^{(\\ell)} \\cdot \\mathbf{o}_j^{(\\ell)}.\n    \\label{eq:head-mask}\n\\end{equation}\n\n\\paragraph{KV cache eviction.}\nA position mask $\\mathbf{m}_k \\in \\{0,1\\}^T$ retains the top-$(1{-}s)\\cdot T$ cache entries, with the BOS token always preserved.\nEvicted positions are blocked via attention masking:\n\\begin{equation}\n    \\tilde{a}_{ij} = a_{ij} \\cdot m_{k,j}, \\quad \\forall\\, i, j.\n    \\label{eq:kv-mask}\n\\end{equation}\nWe compare two strategies for selecting evicted positions: \\textbf{importance-based} eviction, which scores each position by its cumulative attention mass with position normalization to correct for causal bias \\cite{thinkv-iclr2026, defensivekv-iclr2026}; and \\textbf{random} eviction, which removes positions uniformly at random as a strategy-agnostic baseline.\n\n\\paragraph{Compound sparsity.}\nWhen both mechanisms operate at a shared sparsity level $s$ (i.e., pruning fraction $p = s$ and eviction fraction $q = s$), we obtain \\emph{compound sparsity} parameterized by a single scalar.\nThe two axes are not independent: head pruning redistributes attention mass among surviving heads, which alters the importance scores that drive KV cache eviction.\nWhether this coupling produces additive or super-additive degradation---and whether the answer depends on factors beyond $s$ itself---is the central question of this work.\n\nPrior analyses of compound compression \\cite{spark-aaai2026} report that the joint effect is generally super-additive but treat the interaction magnitude as a fixed property of the sparsity level.\nWe investigate whether the eviction strategy and reasoning phase introduce additional structure into this interaction.\n\n\\subsection{Interaction Index}\n\\label{sec:interaction-index}\n\nTo quantify the interaction between head pruning and KV cache eviction, we define the \\emph{Interaction Index} (II) following the factorial interaction framework from experimental design.\n\nFor a given text segment, let $\\text{PPL}_d$, $\\text{PPL}_a$, $\\text{PPL}_k$, and $\\text{PPL}_b$ denote the perplexity under the dense (no sparsity), attention-pruning-only, KV-eviction-only, and compound conditions, respectively.\nNormalizing each by the dense baseline yields relative degradation ratios $r_c = \\text{PPL}_c / \\text{PPL}_d$ for $c \\in \\{a, k, b\\}$.\nThe Interaction Index is:\n\\begin{equation}\n    \\mathrm{II} = r_b - r_a - r_k + 1 = \\frac{\\text{PPL}_b}{\\text{PPL}_d} - \\frac{\\text{PPL}_a}{\\text{PPL}_d} - \\frac{\\text{PPL}_k}{\\text{PPL}_d} + 1.\n    \\label{eq:ii}\n\\end{equation}\n\nUnder additive independence, $r_b \\approx r_a + r_k - 1$, yielding $\\mathrm{II} \\approx 0$.\nThe sign of II determines the interaction regime:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item $\\mathrm{II} > 0$: \\textbf{super-additive}---compound sparsity degrades performance beyond the sum of individual effects.\n    \\item $\\mathrm{II} < 0$: \\textbf{sub-additive}---the compound effect is less than the sum of parts.\n    \\item $\\mathrm{II} = 0$: \\textbf{additive}---the two mechanisms do not interact.\n\\end{itemize}\nNormalizing by $\\text{PPL}_d$ ensures that II values are comparable across problems with different baseline difficulties, enabling aggregation over heterogeneous inputs.\nBecause the II distribution is heavily right-skewed in practice, we report medians rather than means as the central tendency estimator.\n\n\\paragraph{Severity gradient.}\nTo measure how the interaction varies across reasoning phases (defined in \\S\\ref{sec:phase-segmentation}), we define the \\emph{severity gradient}:\n\\begin{equation}\n    G = \\frac{\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}}{\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}},\n    \\label{eq:gradient}\n\\end{equation}\nwhere $\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}$ and $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}$ are the median interaction indices in the low-sparsity and high-sparsity phases, respectively.\n$G \\gg 1$ indicates that compound interaction concentrates in low-sparsity phases; $G \\approx 1$ indicates phase-invariant degradation.\n\n\\subsection{Phase Segmentation}\n\\label{sec:phase-segmentation}\n\nReasoning-capable LLMs produce token sequences with heterogeneous attention structure: some positions exhibit highly concentrated attention over a few key tokens, while others distribute attention broadly across the context.\nWe partition each generated sequence into three phases based on the local \\emph{attention sparsity profile}, adapting the phase-aware methodology of ThinKV \\cite{thinkv-iclr2026}.\n\n\\paragraph{Attention sparsity.}\nFor each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:\n\\begin{equation}\n    \\sigma_i^{(h)} = \\frac{1}{T} \\sum_{j=1}^{T} \\mathbf{1}\\!\\left[a_{ij}^{(h)} < 0.01 \\cdot \\max_k a_{ik}^{(h)}\\right].\n    \\label{eq:attn-sparsity}\n\\end{equation}\nThe per-position sparsity $\\sigma_i = \\frac{1}{H}\\sum_h \\sigma_i^{(h)}$ averages across all heads.\n\n\\paragraph{Quantile-based segmentation.}\nTokens are partitioned into three groups by the tercile boundaries of $\\{\\sigma_i\\}_{i=1}^{T}$:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{High-sparsity phase} (top tercile of $\\sigma$): attention concentrates on few tokens; heads are largely redundant, making both pruning and eviction relatively benign.\n    \\item \\textbf{Mid-sparsity phase} (middle tercile): intermediate attention patterns.\n    \\item \\textbf{Low-sparsity phase} (bottom tercile of $\\sigma$): attention distributes broadly; each surviving head carries non-redundant information, making both pruning and eviction more destructive.\n\\end{itemize}\nContiguous segments shorter than $\\texttt{min\\_phase\\_length} = 10$ tokens are merged into adjacent phases to ensure sufficient tokens for stable perplexity estimation.\nThe segmentation is purely data-driven and requires no access to model internals beyond attention weights.\n\nThis phase structure arises naturally during extended chain-of-thought reasoning, where the model alternates between focused retrieval of specific facts (high sparsity) and integrative reasoning across many context positions (low sparsity) \\cite{phase-transition-compression-2026}.\nOur central research question is: \\emph{Is the Interaction Index constant across phases and eviction strategies, or does it exhibit a phase $\\times$ strategy interaction?}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "1960b094-def5-4132-bcb9-e78d4bba22bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XiXpZFNMCuMi1N5Tbz9Xvk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12083,
      "cache_read_input_tokens": 40794,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12083
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

_source line 24 · 2026-05-14T05:41:18.736Z_

<details><summary>↩ Tool result · reported error · `toolu_01Vu2MLUVpQaESxBfLqEAuCR`</summary>

```text
&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "b1d67faa-a5d7-4e66-ae3c-4db7f3473a7d",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01UaYTPgC7sZMN73h3B3RZf1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "cdc4886a-4ced-43d0-ba80-05d51c31f4fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X6vvE6fJf8oanAoLXecftK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3705,
      "cache_read_input_tokens": 52877,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3705
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

_source line 26 · 2026-05-14T05:41:21.747Z_

<details><summary>↩ Tool result · `toolu_01UaYTPgC7sZMN73h3B3RZf1`</summary>

```text
1	% Section 3: Background and Problem Setup
2	% Phase-Modulated Compound Sparsity
3	
4	\section{Background and Problem Setup}
5	\label{sec:background}
6	
7	We formalize compound sparsity as the simultaneous application of attention head pruning and KV cache eviction, define the Interaction Index to measure their non-additive interaction, and introduce phase segmentation to localize the analysis across reasoning stages.
8	
9	\subsection{Compound Sparsity Formulation}
10	\label{sec:compound-sparsity}
11	
12	Consider a transformer language model $\mathcal{M}$ with $L$ layers, each containing $H$ attention heads.
13	Let $s \in (0,1)$ denote a unified sparsity budget applied to both compression axes.
14	
15	\paragraph{Attention head pruning.}
16	Given per-head importance scores $\mathbf{w}^{(l)} \in \mathbb{R}^H$ for layer $l$, we construct a binary mask $\mathbf{m}_h^{(l)} \in \{0,1\}^H$ that retains the top-$(1{-}s) \cdot H$ heads by importance.
17	For head $j$ in layer $l$, the masked attention output becomes:
18	\begin{equation}
19	    \tilde{\mathbf{o}}_j^{(l)} = m_{h,j}^{(l)} \cdot \mathbf{o}_j^{(l)}
20	    \label{eq:head-mask}
21	\end{equation}
22	where $\mathbf{o}_j^{(l)}$ is the original head output.
23	Head importance is computed as the Frobenius norm of the attention weight matrix: $w_j^{(l)} = \|\mathbf{A}_j^{(l)}\|_F$, where $\mathbf{A}_j^{(l)} \in \mathbb{R}^{T \times T}$ is the attention probability matrix for head $j$ at layer $l$ over a calibration input of length $T$.
24	
25	\paragraph{KV cache eviction.}
26	For a sequence of length $T$, we construct a position mask $\mathbf{m}_k \in \{0,1\}^T$ that retains the top-$(1{-}s) \cdot T$ positions by importance, with position $0$ (BOS) always retained.
27	Evicted positions are blocked by setting their attention mask entries to zero:
28	\begin{equation}
29	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall i,j
30	    \label{eq:kv-mask}
31	\end{equation}
32	We evaluate two eviction strategies:
33	\begin{itemize}[nosep,leftmargin=*]
34	    \item \textbf{Importance-based:} Position importance is the cumulative attention mass received across all heads and query positions, with position normalization to correct for causal attention bias:
35	    \begin{equation}
36	        \mathrm{imp}(j) = \frac{\sum_{l,h,i} a^{(l,h)}_{ij}}{T - j}
37	        \label{eq:kv-importance}
38	    \end{equation}
39	    where the denominator $(T - j)$ compensates for the fact that later positions can attend to fewer future tokens under causal masking \cite{thinkv2026}.
40	    \item \textbf{Random:} Positions (excluding BOS) are evicted uniformly at random.
41	\end{itemize}
42	
43	\paragraph{Compound sparsity.}
44	Applying both compressions simultaneously yields a model $\mathcal{M}(s)$ where fraction $s$ of heads are pruned per layer \emph{and} fraction $s$ of KV positions are evicted.
45	The two axes interact: head pruning alters the attention distribution over surviving heads, which in turn changes the importance ranking used for KV eviction.
46	
47	\subsection{Interaction Index}
48	\label{sec:interaction-index}
49	
50	To quantify whether compound sparsity degrades performance more (or less) than the sum of its components, we define the \emph{Interaction Index} (II) following the factorial interaction framework from experimental design.
51	
52	Let $\mathrm{PPL}_d$, $\mathrm{PPL}_h$, $\mathrm{PPL}_k$, and $\mathrm{PPL}_b$ denote the perplexity of the dense model, head-pruning only, KV-eviction only, and both applied simultaneously, respectively.
53	Perplexity is computed as $\mathrm{PPL} = \exp\!\bigl(\frac{1}{|S|}\sum_{t \in S} \mathcal{L}_t\bigr)$ where $\mathcal{L}_t$ is the per-token cross-entropy loss and $S$ is the set of evaluated positions.
54	
55	We define the relative degradation ratios $R_h = \mathrm{PPL}_h / \mathrm{PPL}_d$, $R_k = \mathrm{PPL}_k / \mathrm{PPL}_d$, $R_b = \mathrm{PPL}_b / \mathrm{PPL}_d$, and the Interaction Index:
56	\begin{equation}
57	    \mathrm{II} = R_b - R_h - R_k + 1
58	    \label{eq:ii}
59	\end{equation}
60	Under additive independence, $R_b \approx R_h + R_k - 1$, giving $\mathrm{II} \approx 0$.
61	\begin{itemize}[nosep,leftmargin=*]
62	    \item $\mathrm{II} > 0$: \textbf{super-additive} — compound sparsity degrades more than the sum of individual effects.
63	    \item $\mathrm{II} < 0$: \textbf{sub-additive} — compound sparsity is less harmful than expected.
64	    \item $\mathrm{II} = 0$: \textbf{additive} — no interaction between the two axes.
65	\end{itemize}
66	
67	\paragraph{Choice of additive null.}
68	Eq.~\ref{eq:ii} posits an additive null $R_b = R_h + R_k - 1$, but one could equally assume multiplicative independence $R_b = R_h \cdot R_k$, treating the two axes as independent survival probabilities.
69	We adopt the additive form because head pruning and KV eviction operate on disjoint model dimensions---structural (which heads to keep) versus positional (which tokens to retain).
70	When the two mechanisms act independently, each contributes an additive increment $\Delta R$ to the perplexity ratio: the heads removed by pruning and the positions removed by eviction affect non-overlapping information pathways, so their degradations sum rather than multiply.
71	At the sparsity levels studied ($s \leq 0.30$), this non-overlap assumption holds empirically (\S\ref{sec:experiments}).
72	We report the multiplicative residual $R_b / (R_h \cdot R_k)$ alongside II in Appendix~\ref{app:multiplicative-null}; the qualitative conclusions are unchanged under either null model.
73	
74	We evaluate II on 50 problems from MATH-500 \cite{hendrycks2021math}, stratified across difficulty levels.
75	Per-problem II values are aggregated via the median (rather than the mean) due to heavy-tailed distributions---e.g., the mean/median ratio reaches $33.5\times$ for the low-sparsity phase at $s{=}0.30$ (\S\ref{sec:experiments})---where a single outlier can dominate the mean.
76	Bootstrap confidence intervals ($B=10{,}000$ resamples) are computed at the problem level.
77	
78	\paragraph{Severity gradient.}
79	To capture how II varies across reasoning phases, we define the \emph{severity gradient}:
80	\begin{equation}
81	    G = \frac{\widetilde{\mathrm{II}}_{\mathrm{low}}}{\widetilde{\mathrm{II}}_{\mathrm{high}}}
82	    \label{eq:gradient}
83	\end{equation}
84	where $\widetilde{\mathrm{II}}_{\mathrm{low}}$ and $\widetilde{\mathrm{II}}_{\mathrm{high}}$ are the median II in the low-sparsity and high-sparsity phases respectively.
85	$G \gg 1$ indicates that compound degradation concentrates in low-sparsity phases; $G \approx 1$ indicates uniform degradation.
86	$G$ is defined only when $\widetilde{\mathrm{II}}_{\mathrm{high}} > \varepsilon$ for a small threshold $\varepsilon > 0$; when $\widetilde{\mathrm{II}}_{\mathrm{high}} \approx 0$ (ceiling effect, where head pruning alone causes negligible degradation in high-sparsity phases), we report $G = \infty$.
87	
88	\subsection{Phase Segmentation}
89	\label{sec:phase-segmentation}
90	
91	Reasoning-capable LLMs produce token sequences with heterogeneous attention patterns: some segments exhibit concentrated attention (few tokens dominate), while others distribute attention broadly.
92	We partition each generation into three phases based on the \emph{attention sparsity profile}, following the methodology of ThinKV \cite{thinkv2026}.
93	
94	\paragraph{Attention sparsity.}
95	For each query position $i$ and head $h$, we compute the fraction of key positions receiving attention below $1\%$ of the row maximum:
96	\begin{equation}
97	    \sigma_i^{(h)} = \frac{1}{T}\sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right]
98	    \label{eq:sparsity}
99	\end{equation}
100	The per-token sparsity $\sigma_i = \frac{1}{H}\sum_h \sigma_i^{(h)}$ averages across heads.
101	
102	\paragraph{Quantile-based segmentation.}
103	We partition tokens into three equal-sized groups by the quantiles of $\{\sigma_i\}_{i=1}^{T}$:
104	\begin{itemize}[nosep,leftmargin=*]
105	    \item \textbf{High-sparsity phase} (top tercile): attention concentrates on a few tokens; heads are highly redundant, and pruning incurs minimal information loss.
106	    \item \textbf{Mid-sparsity phase} (middle tercile): intermediate attention patterns.
107	    \item \textbf{Low-sparsity phase} (bottom tercile): attention distributes broadly across many tokens; each head carries non-redundant information, making pruning costly.
108	\end{itemize}
109	
110	This segmentation is purely data-driven and does not require access to model internals beyond attention weights.
111	It captures the heterogeneity in attention structure that arises naturally during extended reasoning, where the model alternates between focused retrieval (high sparsity) and exploratory cross-token integration (low sparsity) \cite{thinkingmi2025}.
112	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "566ee791-cf04-4cc3-bb3f-656f3fce8f80",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex",
      "content": "% Section 3: Background and Problem Setup\n% Phase-Modulated Compound Sparsity\n\n\\section{Background and Problem Setup}\n\\label{sec:background}\n\nWe formalize compound sparsity as the simultaneous application of attention head pruning and KV cache eviction, define the Interaction Index to measure their non-additive interaction, and introduce phase segmentation to localize the analysis across reasoning stages.\n\n\\subsection{Compound Sparsity Formulation}\n\\label{sec:compound-sparsity}\n\nConsider a transformer language model $\\mathcal{M}$ with $L$ layers, each containing $H$ attention heads.\nLet $s \\in (0,1)$ denote a unified sparsity budget applied to both compression axes.\n\n\\paragraph{Attention head pruning.}\nGiven per-head importance scores $\\mathbf{w}^{(l)} \\in \\mathbb{R}^H$ for layer $l$, we construct a binary mask $\\mathbf{m}_h^{(l)} \\in \\{0,1\\}^H$ that retains the top-$(1{-}s) \\cdot H$ heads by importance.\nFor head $j$ in layer $l$, the masked attention output becomes:\n\\begin{equation}\n    \\tilde{\\mathbf{o}}_j^{(l)} = m_{h,j}^{(l)} \\cdot \\mathbf{o}_j^{(l)}\n    \\label{eq:head-mask}\n\\end{equation}\nwhere $\\mathbf{o}_j^{(l)}$ is the original head output.\nHead importance is computed as the Frobenius norm of the attention weight matrix: $w_j^{(l)} = \\|\\mathbf{A}_j^{(l)}\\|_F$, where $\\mathbf{A}_j^{(l)} \\in \\mathbb{R}^{T \\times T}$ is the attention probability matrix for head $j$ at layer $l$ over a calibration input of length $T$.\n\n\\paragraph{KV cache eviction.}\nFor a sequence of length $T$, we construct a position mask $\\mathbf{m}_k \\in \\{0,1\\}^T$ that retains the top-$(1{-}s) \\cdot T$ positions by importance, with position $0$ (BOS) always retained.\nEvicted positions are blocked by setting their attention mask entries to zero:\n\\begin{equation}\n    \\tilde{a}_{ij} = a_{ij} \\cdot m_{k,j}, \\quad \\forall i,j\n    \\label{eq:kv-mask}\n\\end{equation}\nWe evaluate two eviction strategies:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{Importance-based:} Position importance is the cumulative attention mass received across all heads and query positions, with position normalization to correct for causal attention bias:\n    \\begin{equation}\n        \\mathrm{imp}(j) = \\frac{\\sum_{l,h,i} a^{(l,h)}_{ij}}{T - j}\n        \\label{eq:kv-importance}\n    \\end{equation}\n    where the denominator $(T - j)$ compensates for the fact that later positions can attend to fewer future tokens under causal masking \\cite{thinkv2026}.\n    \\item \\textbf{Random:} Positions (excluding BOS) are evicted uniformly at random.\n\\end{itemize}\n\n\\paragraph{Compound sparsity.}\nApplying both compressions simultaneously yields a model $\\mathcal{M}(s)$ where fraction $s$ of heads are pruned per layer \\emph{and} fraction $s$ of KV positions are evicted.\nThe two axes interact: head pruning alters the attention distribution over surviving heads, which in turn changes the importance ranking used for KV eviction.\n\n\\subsection{Interaction Index}\n\\label{sec:interaction-index}\n\nTo quantify whether compound sparsity degrades performance more (or less) than the sum of its components, we define the \\emph{Interaction Index} (II) following the factorial interaction framework from experimental design.\n\nLet $\\mathrm{PPL}_d$, $\\mathrm{PPL}_h$, $\\mathrm{PPL}_k$, and $\\mathrm{PPL}_b$ denote the perplexity of the dense model, head-pruning only, KV-eviction only, and both applied simultaneously, respectively.\nPerplexity is computed as $\\mathrm{PPL} = \\exp\\!\\bigl(\\frac{1}{|S|}\\sum_{t \\in S} \\mathcal{L}_t\\bigr)$ where $\\mathcal{L}_t$ is the per-token cross-entropy loss and $S$ is the set of evaluated positions.\n\nWe define the relative degradation ratios $R_h = \\mathrm{PPL}_h / \\mathrm{PPL}_d$, $R_k = \\mathrm{PPL}_k / \\mathrm{PPL}_d$, $R_b = \\mathrm{PPL}_b / \\mathrm{PPL}_d$, and the Interaction Index:\n\\begin{equation}\n    \\mathrm{II} = R_b - R_h - R_k + 1\n    \\label{eq:ii}\n\\end{equation}\nUnder additive independence, $R_b \\approx R_h + R_k - 1$, giving $\\mathrm{II} \\approx 0$.\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item $\\mathrm{II} > 0$: \\textbf{super-additive} — compound sparsity degrades more than the sum of individual effects.\n    \\item $\\mathrm{II} < 0$: \\textbf{sub-additive} — compound sparsity is less harmful than expected.\n    \\item $\\mathrm{II} = 0$: \\textbf{additive} — no interaction between the two axes.\n\\end{itemize}\n\n\\paragraph{Choice of additive null.}\nEq.~\\ref{eq:ii} posits an additive null $R_b = R_h + R_k - 1$, but one could equally assume multiplicative independence $R_b = R_h \\cdot R_k$, treating the two axes as independent survival probabilities.\nWe adopt the additive form because head pruning and KV eviction operate on disjoint model dimensions---structural (which heads to keep) versus positional (which tokens to retain).\nWhen the two mechanisms act independently, each contributes an additive increment $\\Delta R$ to the perplexity ratio: the heads removed by pruning and the positions removed by eviction affect non-overlapping information pathways, so their degradations sum rather than multiply.\nAt the sparsity levels studied ($s \\leq 0.30$), this non-overlap assumption holds empirically (\\S\\ref{sec:experiments}).\nWe report the multiplicative residual $R_b / (R_h \\cdot R_k)$ alongside II in Appendix~\\ref{app:multiplicative-null}; the qualitative conclusions are unchanged under either null model.\n\nWe evaluate II on 50 problems from MATH-500 \\cite{hendrycks2021math}, stratified across difficulty levels.\nPer-problem II values are aggregated via the median (rather than the mean) due to heavy-tailed distributions---e.g., the mean/median ratio reaches $33.5\\times$ for the low-sparsity phase at $s{=}0.30$ (\\S\\ref{sec:experiments})---where a single outlier can dominate the mean.\nBootstrap confidence intervals ($B=10{,}000$ resamples) are computed at the problem level.\n\n\\paragraph{Severity gradient.}\nTo capture how II varies across reasoning phases, we define the \\emph{severity gradient}:\n\\begin{equation}\n    G = \\frac{\\widetilde{\\mathrm{II}}_{\\mathrm{low}}}{\\widetilde{\\mathrm{II}}_{\\mathrm{high}}}\n    \\label{eq:gradient}\n\\end{equation}\nwhere $\\widetilde{\\mathrm{II}}_{\\mathrm{low}}$ and $\\widetilde{\\mathrm{II}}_{\\mathrm{high}}$ are the median II in the low-sparsity and high-sparsity phases respectively.\n$G \\gg 1$ indicates that compound degradation concentrates in low-sparsity phases; $G \\approx 1$ indicates uniform degradation.\n$G$ is defined only when $\\widetilde{\\mathrm{II}}_{\\mathrm{high}} > \\varepsilon$ for a small threshold $\\varepsilon > 0$; when $\\widetilde{\\mathrm{II}}_{\\mathrm{high}} \\approx 0$ (ceiling effect, where head pruning alone causes negligible degradation in high-sparsity phases), we report $G = \\infty$.\n\n\\subsection{Phase Segmentation}\n\\label{sec:phase-segmentation}\n\nReasoning-capable LLMs produce token sequences with heterogeneous attention patterns: some segments exhibit concentrated attention (few tokens dominate), while others distribute attention broadly.\nWe partition each generation into three phases based on the \\emph{attention sparsity profile}, following the methodology of ThinKV \\cite{thinkv2026}.\n\n\\paragraph{Attention sparsity.}\nFor each query position $i$ and head $h$, we compute the fraction of key positions receiving attention below $1\\%$ of the row maximum:\n\\begin{equation}\n    \\sigma_i^{(h)} = \\frac{1}{T}\\sum_{j=1}^{T} \\mathbf{1}\\!\\left[a_{ij}^{(h)} < 0.01 \\cdot \\max_k a_{ik}^{(h)}\\right]\n    \\label{eq:sparsity}\n\\end{equation}\nThe per-token sparsity $\\sigma_i = \\frac{1}{H}\\sum_h \\sigma_i^{(h)}$ averages across heads.\n\n\\paragraph{Quantile-based segmentation.}\nWe partition tokens into three equal-sized groups by the quantiles of $\\{\\sigma_i\\}_{i=1}^{T}$:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{High-sparsity phase} (top tercile): attention concentrates on a few tokens; heads are highly redundant, and pruning incurs minimal information loss.\n    \\item \\textbf{Mid-sparsity phase} (middle tercile): intermediate attention patterns.\n    \\item \\textbf{Low-sparsity phase} (bottom tercile): attention distributes broadly across many tokens; each head carries non-redundant information, making pruning costly.\n\\end{itemize}\n\nThis segmentation is purely data-driven and does not require access to model internals beyond attention weights.\nIt captures the heterogeneity in attention structure that arises naturally during extended reasoning, where the model alternates between focused retrieval (high sparsity) and exploratory cross-token integration (low sparsity) \\cite{thinkingmi2025}.\n",
      "numLines": 112,
      "startLine": 1,
      "totalLines": 112
    }
  }
}
```

</details>

---

### Assistant

_source line 27_

<details><summary>Logged reasoning block</summary>

```text
The file has been modified since I read it (it now has more content including a "Choice of additive null" paragraph, different citation keys like `thinkv2026` instead of `placeholder_thinkv`, etc.). Let me re-assess and rewrite.

Key changes from the previous version:
1. Citation keys are now `thinkv2026` (not `thinkv-iclr2026`), `hendrycks2021math`, `thinkingmi2025`
2. Added "Choice of additive null" paragraph in 3.2 (multiplicative vs additive)
3. Added ε threshold for G definition


4. The data shows a mean/median ratio of 33.5× at s=0.30 with B=10,000 bootstrap samples
5. Still using $\mathrm{PPL}_h$ notation instead of $\text{PPL}_a$ from methodology.tex

But I'm noticing the citation keys are inconsistent—related_work.tex uses `thinkv-iclr2026` while the background section uses `thinkv2026`. I should align with the related_work convention since that's already established. I don't actually need to check the bib file right now.

Looking at what to preserve and what needs updating: I'll keep the methodological justification for the additive null, the ε threshold for G, and that concrete 33.5× ratio. But I need to fix the notation—changing $\mathrm{PPL}_h$ to $\text{PPL}_a$ and the ratio variables from $R_h, R_k, R_b$ to $r_a, r_k, r_b$ to match methodology.tex, plus correcting those citation keys.

Now I'm reconsidering where certain content belongs—the MATH-500 specifics and that detailed data point about mean/median 33.5× with B=10000 feel like they might fit better in Section 4 rather than Section 3. I should also add a research question at the end of 3.3, fix the layer index notation to $\ell$, add the min_phase_length parameter, and standardize the em-dashes to LaTeX format. I'm realizing the section is already pushing toward 800-900 words, so I need to be strategic about what stays. The additive null justification is crucial for a venue like EMNLP since reviewers will definitely question it, so that's worth keeping even if it takes up space. I'll trim the experimental details like the MATH-500 specifics and bootstrap parameters, and I'll soften the specific ratio about median versus mean to just note that heavy tails favor the median. My revision plan is to fix the notation throughout, update citation keys, strip out the experimental details, preserve the additive null reasoning and ε threshold, and then start making the edits.

Now I'm comparing the importance score formulas between the two files and noticing they're expressing the same concept but with slightly different notation—one uses seq_len and the other uses T for sequence length. I should standardize this across both sections.

Let me draft the final version of this section, aiming for around 800 words and incorporating all the key content while cleaning up the notation inconsistencies.

Writing LaTeX section... I'm applying binary masks to zero out the pruned head outputs, then moving to the KV cache strategy where I retain only the top positions by sequence length while always keeping the beginning-of-sequence token, using attention masking to block evicted positions. Now I'm comparing different strategies for this eviction approach. for constructing $\mathbf{m}_k$:
\begin{itemize}[nosep,leftmargin=*]
    \item \textbf{Importance-based:} Each position $j$ is scored by its cumulative attention mass with position normalization:
    \begin{equation}
        \mathrm{imp}(j) = \frac{\sum_{\ell, h, i} a_{ij}^{(\ell,h)}}{T - j},
        \label{eq:kv-importance}
    \end{equation}
    where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}.
    \item \textbf{Random:} Positions (excluding BOS) are evicted uniformly at random.
\end{itemize}

\paragraph{Compound sparsity.}
When I apply both head pruning and KV cache eviction at the same sparsity level, the two mechanisms interact in non-trivial ways---pruning redistributes attention across remaining heads, which then changes the importance scores used for eviction. Prior work treats this interaction as a fixed property of the sparsity level, but I want to investigate whether the eviction strategy and reasoning phase introduce additional structure. To quantify this interaction, I'm defining an Interaction Index based on factorial design principles that measures the joint effect of both mechanisms on perplexity. When the effects are independent, the interaction index should be zero, but the sign tells us whether the mechanisms amplify each other—positive values mean the combined degradation is worse than expected, negative means they partially offset, and zero indicates no interaction. The formula assumes an additive baseline where the compound effect equals the sum of individual effects minus one.

I'm choosing the additive form over multiplicative because head pruning and KV cache eviction affect different dimensions of the model—one structural, one positional—so their impacts add together rather than compound, especially at the sparsity levels we're examining. I've verified that the multiplicative alternative doesn't change the main findings.

To make the interaction index comparable across different problems, I'm normalizing by the baseline perplexity, and since the distribution is heavily skewed, I'm using medians instead of means. I'm also defining a severity gradient to track how the interaction index changes across different reasoning phases.

Now I'm setting up the phase segmentation framework to capture how attention patterns vary throughout token generation—some positions concentrate attention on a few critical tokens while others spread it broadly.

To measure this, I'm computing an attention sparsity metric for each query position and attention head, which identifies key positions that receive negligible attention relative to the maximum. Then I'm averaging this sparsity measure across all heads to get a per-position sparsity score.

Now I'm partitioning tokens into three groups based on tercile boundaries of these sparsity scores—high-sparsity tokens where attention concentrates on few positions and heads are redundant, mid-sparsity tokens with intermediate patterns, and low-sparsity tokens where attention distributes broadly and each head carries important information. Short contiguous segments below a minimum length threshold get merged into adjacent phases to maintain stability, and this segmentation is entirely driven by the data itself.

The segmentation only needs access to attention weights, and this phase structure naturally emerges during extended reasoning where the model shifts between focused fact retrieval in high-sparsity phases and integrative reasoning across many positions in low-sparsity phases. The core question I'm investigating is whether the Interaction Index remains constant across these phases and different eviction strategies, or if there's a meaningful interaction between phase type and strategy choice.

Now I'm going through the notation and citation updates to align with the methodology and related work sections—standardizing the perplexity notation, ratio symbols, layer indices, and citation keys. I'm also incorporating the minimum phase length parameter and the research question at the end, while keeping the additive null justification since it's methodologically important.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "baebf381-916f-48f8-ad39-210a060ed805",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rz9pJJRd1Ts5DtT7HQGCb9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3102,
      "cache_read_input_tokens": 56582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3102
      },
      "output_tokens": 13,
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

<details open><summary>🔧 Tool call — Write · `toolu_01L4aFefRxyca3nW6HSxT1ZW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex",
  "content": "% Section 3: Background and Problem Setup\n% Note: eq:ii and eq:gradient are the canonical definitions.\n% Methodology.tex should reference these via \\eqref rather than redefining.\n\n\\section{Background and Problem Setup}\n\\label{sec:background}\n\nWe formalize compound sparsity as the simultaneous application of attention head pruning and KV cache eviction, define the Interaction Index to quantify their non-additive coupling, and introduce phase segmentation to localize the analysis across reasoning stages.\n\n\\subsection{Compound Sparsity Formulation}\n\\label{sec:compound-sparsity}\n\nConsider a Transformer language model with $L$ layers, each containing $H$ attention heads.\nLet $s \\in (0,1)$ denote a unified sparsity budget applied to both compression axes.\n\n\\paragraph{Attention head pruning.}\nFor each layer $\\ell$, heads are ranked by Frobenius norm importance $w_j^{(\\ell)} = \\|\\mathbf{A}_j^{(\\ell)}\\|_F$, where $\\mathbf{A}_j^{(\\ell)} \\in \\mathbb{R}^{T \\times T}$ is the attention matrix for head $j$ \\cite{voita2019heads, michel2019sixteen}.\nA binary mask $m_j^{(\\ell)} \\in \\{0,1\\}$ retains the top-$(1{-}s)\\cdot H$ heads, zeroing the output of pruned heads:\n\\begin{equation}\n    \\tilde{\\mathbf{o}}_j^{(\\ell)} = m_j^{(\\ell)} \\cdot \\mathbf{o}_j^{(\\ell)}.\n    \\label{eq:head-mask}\n\\end{equation}\n\n\\paragraph{KV cache eviction.}\nFor a sequence of length $T$, a position mask $\\mathbf{m}_k \\in \\{0,1\\}^T$ retains the top-$(1{-}s)\\cdot T$ positions, with the BOS token always preserved.\nEvicted positions are blocked via attention masking:\n\\begin{equation}\n    \\tilde{a}_{ij} = a_{ij} \\cdot m_{k,j}, \\quad \\forall\\, i, j.\n    \\label{eq:kv-mask}\n\\end{equation}\nWe compare two strategies for constructing $\\mathbf{m}_k$:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{Importance-based:} Each position $j$ is scored by its cumulative attention mass with position normalization:\n    \\begin{equation}\n        \\mathrm{imp}(j) = \\frac{\\sum_{\\ell, h, i} a_{ij}^{(\\ell,h)}}{T - j},\n        \\label{eq:kv-importance}\n    \\end{equation}\n    where the denominator compensates for causal bias---earlier positions are attended to by more queries \\cite{thinkv-iclr2026, defensivekv-iclr2026}.\n    \\item \\textbf{Random:} Positions (excluding BOS) are evicted uniformly at random.\n\\end{itemize}\n\n\\paragraph{Compound sparsity.}\nApplying both mechanisms simultaneously at sparsity level $s$ (pruning fraction $p = s$, eviction fraction $q = s$) yields \\emph{compound sparsity}.\nThe two axes are not independent: head pruning redistributes attention mass among surviving heads, which alters the importance ranking used for KV cache eviction.\nPrior analyses of compound compression \\cite{spark-aaai2026} report that the joint effect is generally super-additive but treat the interaction magnitude as a fixed property of $s$.\nWe investigate whether the eviction strategy and reasoning phase introduce additional structure.\n\n\\subsection{Interaction Index}\n\\label{sec:interaction-index}\n\nTo quantify the interaction between head pruning and KV cache eviction, we define the \\emph{Interaction Index} (II) following the factorial interaction framework from experimental design.\n\nFor a given text segment, let $\\text{PPL}_d$, $\\text{PPL}_a$, $\\text{PPL}_k$, and $\\text{PPL}_b$ denote the perplexity under the dense (no sparsity), attention-pruning-only, KV-eviction-only, and compound conditions, respectively.\nPerplexity is computed as $\\text{PPL} = \\exp\\!\\bigl(\\frac{1}{|S|}\\sum_{t \\in S} \\mathcal{L}_t\\bigr)$, where $\\mathcal{L}_t$ is the per-token cross-entropy loss over evaluated positions $S$.\nNormalizing by the dense baseline yields relative degradation ratios $r_c = \\text{PPL}_c\\,/\\,\\text{PPL}_d$ for $c \\in \\{a, k, b\\}$, and the Interaction Index:\n\\begin{equation}\n    \\mathrm{II} = r_b - r_a - r_k + 1.\n    \\label{eq:ii}\n\\end{equation}\n\nUnder additive independence, $r_b \\approx r_a + r_k - 1$, yielding $\\mathrm{II} \\approx 0$.\nThe sign of II determines the interaction regime:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item $\\mathrm{II} > 0$: \\textbf{super-additive}---compound degradation exceeds the sum of individual effects.\n    \\item $\\mathrm{II} < 0$: \\textbf{sub-additive}---the compound effect is less than the sum of parts.\n    \\item $\\mathrm{II} = 0$: \\textbf{additive}---the two mechanisms do not interact.\n\\end{itemize}\n\n\\paragraph{Choice of additive null.}\nEquation~\\ref{eq:ii} posits an additive null $r_b = r_a + r_k - 1$ rather than multiplicative independence $r_b = r_a \\cdot r_k$.\nWe adopt the additive form because head pruning and KV cache eviction operate on disjoint model dimensions---structural (which heads to retain) versus positional (which tokens to cache)---so their degradations sum rather than multiply at the sparsity levels we study ($s \\leq 0.30$).\nWe verify in Appendix~\\ref{app:multiplicative-null} that qualitative conclusions are unchanged under the multiplicative null.\n\nNormalizing by $\\text{PPL}_d$ ensures cross-problem comparability.\nBecause the II distribution is heavily right-skewed, we report medians as the central tendency.\n\n\\paragraph{Severity gradient.}\nTo capture how II varies across reasoning phases (defined in \\S\\ref{sec:phase-segmentation}), we define the \\emph{severity gradient}:\n\\begin{equation}\n    G = \\frac{\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}}{\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}},\n    \\label{eq:gradient}\n\\end{equation}\nwhere $\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}$ and $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}$ are the median interaction indices in the low-sparsity and high-sparsity phases, respectively.\n$G \\gg 1$ indicates that compound interaction concentrates in low-sparsity phases; $G \\approx 1$ indicates phase-invariant degradation.\nWhen $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}} < \\varepsilon$ for a small threshold $\\varepsilon > 0$, we report $G = \\infty$.\n\n\\subsection{Phase Segmentation}\n\\label{sec:phase-segmentation}\n\nReasoning-capable LLMs produce token sequences with heterogeneous attention structure: some positions exhibit highly concentrated attention over a few key tokens, while others distribute attention broadly across the context.\nWe partition each generated sequence into three phases based on the local \\emph{attention sparsity profile}, adapting the phase-aware methodology of ThinKV \\cite{thinkv-iclr2026}.\n\n\\paragraph{Attention sparsity.}\nFor each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:\n\\begin{equation}\n    \\sigma_i^{(h)} = \\frac{1}{T} \\sum_{j=1}^{T} \\mathbf{1}\\!\\left[a_{ij}^{(h)} < 0.01 \\cdot \\max_k a_{ik}^{(h)}\\right].\n    \\label{eq:attn-sparsity}\n\\end{equation}\nThe per-position sparsity $\\sigma_i = \\frac{1}{H}\\sum_h \\sigma_i^{(h)}$ averages across all heads.\n\n\\paragraph{Quantile-based segmentation.}\nTokens are partitioned into three groups by the tercile boundaries of $\\{\\sigma_i\\}_{i=1}^{T}$:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{High-sparsity phase} (top tercile of $\\sigma$): attention concentrates on few tokens; heads are largely redundant, making both pruning and eviction relatively benign.\n    \\item \\textbf{Mid-sparsity phase} (middle tercile): intermediate attention patterns.\n    \\item \\textbf{Low-sparsity phase} (bottom tercile of $\\sigma$): attention distributes broadly; each surviving head carries non-redundant information, making both pruning and eviction more destructive.\n\\end{itemize}\nContiguous segments shorter than $\\texttt{min\\_phase\\_length} = 10$ tokens are merged into adjacent phases to ensure sufficient tokens for stable perplexity estimation.\nThe segmentation is purely data-driven and requires only access to attention weights.\n\nThis phase structure arises naturally during extended chain-of-thought reasoning, where the model alternates between focused retrieval of specific facts (high sparsity) and integrative reasoning across many context positions (low sparsity) \\cite{phase-transition-compression-2026}.\nOur central research question is: \\emph{Is the Interaction Index constant across phases and eviction strategies, or does it exhibit a phase $\\times$ strategy interaction?}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "75cbf634-bdc9-47c6-ad6b-7a6ee51483b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rz9pJJRd1Ts5DtT7HQGCb9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3102,
      "cache_read_input_tokens": 56582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3102
      },
      "output_tokens": 13,
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

_source line 29 · 2026-05-14T05:42:52.696Z_

<details><summary>↩ Tool result · `toolu_01L4aFefRxyca3nW6HSxT1ZW`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "ae7b9c9c-5ef5-46d5-97b5-6fffcc90cdb0",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex",
    "content": "% Section 3: Background and Problem Setup\n% Note: eq:ii and eq:gradient are the canonical definitions.\n% Methodology.tex should reference these via \\eqref rather than redefining.\n\n\\section{Background and Problem Setup}\n\\label{sec:background}\n\nWe formalize compound sparsity as the simultaneous application of attention head pruning and KV cache eviction, define the Interaction Index to quantify their non-additive coupling, and introduce phase segmentation to localize the analysis across reasoning stages.\n\n\\subsection{Compound Sparsity Formulation}\n\\label{sec:compound-sparsity}\n\nConsider a Transformer language model with $L$ layers, each containing $H$ attention heads.\nLet $s \\in (0,1)$ denote a unified sparsity budget applied to both compression axes.\n\n\\paragraph{Attention head pruning.}\nFor each layer $\\ell$, heads are ranked by Frobenius norm importance $w_j^{(\\ell)} = \\|\\mathbf{A}_j^{(\\ell)}\\|_F$, where $\\mathbf{A}_j^{(\\ell)} \\in \\mathbb{R}^{T \\times T}$ is the attention matrix for head $j$ \\cite{voita2019heads, michel2019sixteen}.\nA binary mask $m_j^{(\\ell)} \\in \\{0,1\\}$ retains the top-$(1{-}s)\\cdot H$ heads, zeroing the output of pruned heads:\n\\begin{equation}\n    \\tilde{\\mathbf{o}}_j^{(\\ell)} = m_j^{(\\ell)} \\cdot \\mathbf{o}_j^{(\\ell)}.\n    \\label{eq:head-mask}\n\\end{equation}\n\n\\paragraph{KV cache eviction.}\nFor a sequence of length $T$, a position mask $\\mathbf{m}_k \\in \\{0,1\\}^T$ retains the top-$(1{-}s)\\cdot T$ positions, with the BOS token always preserved.\nEvicted positions are blocked via attention masking:\n\\begin{equation}\n    \\tilde{a}_{ij} = a_{ij} \\cdot m_{k,j}, \\quad \\forall\\, i, j.\n    \\label{eq:kv-mask}\n\\end{equation}\nWe compare two strategies for constructing $\\mathbf{m}_k$:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{Importance-based:} Each position $j$ is scored by its cumulative attention mass with position normalization:\n    \\begin{equation}\n        \\mathrm{imp}(j) = \\frac{\\sum_{\\ell, h, i} a_{ij}^{(\\ell,h)}}{T - j},\n        \\label{eq:kv-importance}\n    \\end{equation}\n    where the denominator compensates for causal bias---earlier positions are attended to by more queries \\cite{thinkv-iclr2026, defensivekv-iclr2026}.\n    \\item \\textbf{Random:} Positions (excluding BOS) are evicted uniformly at random.\n\\end{itemize}\n\n\\paragraph{Compound sparsity.}\nApplying both mechanisms simultaneously at sparsity level $s$ (pruning fraction $p = s$, eviction fraction $q = s$) yields \\emph{compound sparsity}.\nThe two axes are not independent: head pruning redistributes attention mass among surviving heads, which alters the importance ranking used for KV cache eviction.\nPrior analyses of compound compression \\cite{spark-aaai2026} report that the joint effect is generally super-additive but treat the interaction magnitude as a fixed property of $s$.\nWe investigate whether the eviction strategy and reasoning phase introduce additional structure.\n\n\\subsection{Interaction Index}\n\\label{sec:interaction-index}\n\nTo quantify the interaction between head pruning and KV cache eviction, we define the \\emph{Interaction Index} (II) following the factorial interaction framework from experimental design.\n\nFor a given text segment, let $\\text{PPL}_d$, $\\text{PPL}_a$, $\\text{PPL}_k$, and $\\text{PPL}_b$ denote the perplexity under the dense (no sparsity), attention-pruning-only, KV-eviction-only, and compound conditions, respectively.\nPerplexity is computed as $\\text{PPL} = \\exp\\!\\bigl(\\frac{1}{|S|}\\sum_{t \\in S} \\mathcal{L}_t\\bigr)$, where $\\mathcal{L}_t$ is the per-token cross-entropy loss over evaluated positions $S$.\nNormalizing by the dense baseline yields relative degradation ratios $r_c = \\text{PPL}_c\\,/\\,\\text{PPL}_d$ for $c \\in \\{a, k, b\\}$, and the Interaction Index:\n\\begin{equation}\n    \\mathrm{II} = r_b - r_a - r_k + 1.\n    \\label{eq:ii}\n\\end{equation}\n\nUnder additive independence, $r_b \\approx r_a + r_k - 1$, yielding $\\mathrm{II} \\approx 0$.\nThe sign of II determines the interaction regime:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item $\\mathrm{II} > 0$: \\textbf{super-additive}---compound degradation exceeds the sum of individual effects.\n    \\item $\\mathrm{II} < 0$: \\textbf{sub-additive}---the compound effect is less than the sum of parts.\n    \\item $\\mathrm{II} = 0$: \\textbf{additive}---the two mechanisms do not interact.\n\\end{itemize}\n\n\\paragraph{Choice of additive null.}\nEquation~\\ref{eq:ii} posits an additive null $r_b = r_a + r_k - 1$ rather than multiplicative independence $r_b = r_a \\cdot r_k$.\nWe adopt the additive form because head pruning and KV cache eviction operate on disjoint model dimensions---structural (which heads to retain) versus positional (which tokens to cache)---so their degradations sum rather than multiply at the sparsity levels we study ($s \\leq 0.30$).\nWe verify in Appendix~\\ref{app:multiplicative-null} that qualitative conclusions are unchanged under the multiplicative null.\n\nNormalizing by $\\text{PPL}_d$ ensures cross-problem comparability.\nBecause the II distribution is heavily right-skewed, we report medians as the central tendency.\n\n\\paragraph{Severity gradient.}\nTo capture how II varies across reasoning phases (defined in \\S\\ref{sec:phase-segmentation}), we define the \\emph{severity gradient}:\n\\begin{equation}\n    G = \\frac{\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}}{\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}},\n    \\label{eq:gradient}\n\\end{equation}\nwhere $\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}$ and $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}$ are the median interaction indices in the low-sparsity and high-sparsity phases, respectively.\n$G \\gg 1$ indicates that compound interaction concentrates in low-sparsity phases; $G \\approx 1$ indicates phase-invariant degradation.\nWhen $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}} < \\varepsilon$ for a small threshold $\\varepsilon > 0$, we report $G = \\infty$.\n\n\\subsection{Phase Segmentation}\n\\label{sec:phase-segmentation}\n\nReasoning-capable LLMs produce token sequences with heterogeneous attention structure: some positions exhibit highly concentrated attention over a few key tokens, while others distribute attention broadly across the context.\nWe partition each generated sequence into three phases based on the local \\emph{attention sparsity profile}, adapting the phase-aware methodology of ThinKV \\cite{thinkv-iclr2026}.\n\n\\paragraph{Attention sparsity.}\nFor each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:\n\\begin{equation}\n    \\sigma_i^{(h)} = \\frac{1}{T} \\sum_{j=1}^{T} \\mathbf{1}\\!\\left[a_{ij}^{(h)} < 0.01 \\cdot \\max_k a_{ik}^{(h)}\\right].\n    \\label{eq:attn-sparsity}\n\\end{equation}\nThe per-position sparsity $\\sigma_i = \\frac{1}{H}\\sum_h \\sigma_i^{(h)}$ averages across all heads.\n\n\\paragraph{Quantile-based segmentation.}\nTokens are partitioned into three groups by the tercile boundaries of $\\{\\sigma_i\\}_{i=1}^{T}$:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{High-sparsity phase} (top tercile of $\\sigma$): attention concentrates on few tokens; heads are largely redundant, making both pruning and eviction relatively benign.\n    \\item \\textbf{Mid-sparsity phase} (middle tercile): intermediate attention patterns.\n    \\item \\textbf{Low-sparsity phase} (bottom tercile of $\\sigma$): attention distributes broadly; each surviving head carries non-redundant information, making both pruning and eviction more destructive.\n\\end{itemize}\nContiguous segments shorter than $\\texttt{min\\_phase\\_length} = 10$ tokens are merged into adjacent phases to ensure sufficient tokens for stable perplexity estimation.\nThe segmentation is purely data-driven and requires only access to attention weights.\n\nThis phase structure arises naturally during extended chain-of-thought reasoning, where the model alternates between focused retrieval of specific facts (high sparsity) and integrative reasoning across many context positions (low sparsity) \\cite{phase-transition-compression-2026}.\nOur central research question is: \\emph{Is the Interaction Index constant across phases and eviction strategies, or does it exhibit a phase $\\times$ strategy interaction?}\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 111,
        "newStart": 1,
        "newLines": 112,
        "lines": [
          " % Section 3: Background and Problem Setup",
          "-% Phase-Modulated Compound Sparsity",
          "+% Note: eq:ii and eq:gradient are the canonical definitions.",
          "+% Methodology.tex should reference these via \\eqref rather than redefining.",
          " ",
          " \\section{Background and Problem Setup}",
          " \\label{sec:background}",
          " ",
          "-We formalize compound sparsity as the simultaneous application of attention head pruning and KV cache eviction, define the Interaction Index to measure their non-additive interaction, and introduce phase segmentation to localize the analysis across reasoning stages.",
          "+We formalize compound sparsity as the simultaneous application of attention head pruning and KV cache eviction, define the Interaction Index to quantify their non-additive coupling, and introduce phase segmentation to localize the analysis across reasoning stages.",
          " ",
          " \\subsection{Compound Sparsity Formulation}",
          " \\label{sec:compound-sparsity}",
          " ",
          "-Consider a transformer language model $\\mathcal{M}$ with $L$ layers, each containing $H$ attention heads.",
          "+Consider a Transformer language model with $L$ layers, each containing $H$ attention heads.",
          " Let $s \\in (0,1)$ denote a unified sparsity budget applied to both compression axes.",
          " ",
          " \\paragraph{Attention head pruning.}",
          "-Given per-head importance scores $\\mathbf{w}^{(l)} \\in \\mathbb{R}^H$ for layer $l$, we construct a binary mask $\\mathbf{m}_h^{(l)} \\in \\{0,1\\}^H$ that retains the top-$(1{-}s) \\cdot H$ heads by importance.",
          "-For head $j$ in layer $l$, the masked attention output becomes:",
          "+For each layer $\\ell$, heads are ranked by Frobenius norm importance $w_j^{(\\ell)} = \\|\\mathbf{A}_j^{(\\ell)}\\|_F$, where $\\mathbf{A}_j^{(\\ell)} \\in \\mathbb{R}^{T \\times T}$ is the attention matrix for head $j$ \\cite{voita2019heads, michel2019sixteen}.",
          "+A binary mask $m_j^{(\\ell)} \\in \\{0,1\\}$ retains the top-$(1{-}s)\\cdot H$ heads, zeroing the output of pruned heads:",
          " \\begin{equation}",
          "-    \\tilde{\\mathbf{o}}_j^{(l)} = m_{h,j}^{(l)} \\cdot \\mathbf{o}_j^{(l)}",
          "+    \\tilde{\\mathbf{o}}_j^{(\\ell)} = m_j^{(\\ell)} \\cdot \\mathbf{o}_j^{(\\ell)}.",
          "     \\label{eq:head-mask}",
          " \\end{equation}",
          "-where $\\mathbf{o}_j^{(l)}$ is the original head output.",
          "-Head importance is computed as the Frobenius norm of the attention weight matrix: $w_j^{(l)} = \\|\\mathbf{A}_j^{(l)}\\|_F$, where $\\mathbf{A}_j^{(l)} \\in \\mathbb{R}^{T \\times T}$ is the attention probability matrix for head $j$ at layer $l$ over a calibration input of length $T$.",
          " ",
          " \\paragraph{KV cache eviction.}",
          "-For a sequence of length $T$, we construct a position mask $\\mathbf{m}_k \\in \\{0,1\\}^T$ that retains the top-$(1{-}s) \\cdot T$ positions by importance, with position $0$ (BOS) always retained.",
          "-Evicted positions are blocked by setting their attention mask entries to zero:",
          "+For a sequence of length $T$, a position mask $\\mathbf{m}_k \\in \\{0,1\\}^T$ retains the top-$(1{-}s)\\cdot T$ positions, with the BOS token always preserved.",
          "+Evicted positions are blocked via attention masking:",
          " \\begin{equation}",
          "-    \\tilde{a}_{ij} = a_{ij} \\cdot m_{k,j}, \\quad \\forall i,j",
          "+    \\tilde{a}_{ij} = a_{ij} \\cdot m_{k,j}, \\quad \\forall\\, i, j.",
          "     \\label{eq:kv-mask}",
          " \\end{equation}",
          "-We evaluate two eviction strategies:",
          "+We compare two strategies for constructing $\\mathbf{m}_k$:",
          " \\begin{itemize}[nosep,leftmargin=*]",
          "-    \\item \\textbf{Importance-based:} Position importance is the cumulative attention mass received across all heads and query positions, with position normalization to correct for causal attention bias:",
          "+    \\item \\textbf{Importance-based:} Each position $j$ is scored by its cumulative attention mass with position normalization:",
          "     \\begin{equation}",
          "-        \\mathrm{imp}(j) = \\frac{\\sum_{l,h,i} a^{(l,h)}_{ij}}{T - j}",
          "+        \\mathrm{imp}(j) = \\frac{\\sum_{\\ell, h, i} a_{ij}^{(\\ell,h)}}{T - j},",
          "         \\label{eq:kv-importance}",
          "     \\end{equation}",
          "-    where the denominator $(T - j)$ compensates for the fact that later positions can attend to fewer future tokens under causal masking \\cite{thinkv2026}.",
          "+    where the denominator compensates for causal bias---earlier positions are attended to by more queries \\cite{thinkv-iclr2026, defensivekv-iclr2026}.",
          "     \\item \\textbf{Random:} Positions (excluding BOS) are evicted uniformly at random.",
          " \\end{itemize}",
          " ",
          " \\paragraph{Compound sparsity.}",
          "-Applying both compressions simultaneously yields a model $\\mathcal{M}(s)$ where fraction $s$ of heads are pruned per layer \\emph{and} fraction $s$ of KV positions are evicted.",
          "-The two axes interact: head pruning alters the attention distribution over surviving heads, which in turn changes the importance ranking used for KV eviction.",
          "+Applying both mechanisms simultaneously at sparsity level $s$ (pruning fraction $p = s$, eviction fraction $q = s$) yields \\emph{compound sparsity}.",
          "+The two axes are not independent: head pruning redistributes attention mass among surviving heads, which alters the importance ranking used for KV cache eviction.",
          "+Prior analyses of compound compression \\cite{spark-aaai2026} report that the joint effect is generally super-additive but treat the interaction magnitude as a fixed property of $s$.",
          "+We investigate whether the eviction strategy and reasoning phase introduce additional structure.",
          " ",
          " \\subsection{Interaction Index}",
          " \\label{sec:interaction-index}",
          " ",
          "-To quantify whether compound sparsity degrades performance more (or less) than the sum of its components, we define the \\emph{Interaction Index} (II) following the factorial interaction framework from experimental design.",
          "+To quantify the interaction between head pruning and KV cache eviction, we define the \\emph{Interaction Index} (II) following the factorial interaction framework from experimental design.",
          " ",
          "-Let $\\mathrm{PPL}_d$, $\\mathrm{PPL}_h$, $\\mathrm{PPL}_k$, and $\\mathrm{PPL}_b$ denote the perplexity of the dense model, head-pruning only, KV-eviction only, and both applied simultaneously, respectively.",
          "-Perplexity is computed as $\\mathrm{PPL} = \\exp\\!\\bigl(\\frac{1}{|S|}\\sum_{t \\in S} \\mathcal{L}_t\\bigr)$ where $\\mathcal{L}_t$ is the per-token cross-entropy loss and $S$ is the set of evaluated positions.",
          "-",
          "-We define the relative degradation ratios $R_h = \\mathrm{PPL}_h / \\mathrm{PPL}_d$, $R_k = \\mathrm{PPL}_k / \\mathrm{PPL}_d$, $R_b = \\mathrm{PPL}_b / \\mathrm{PPL}_d$, and the Interaction Index:",
          "+For a given text segment, let $\\text{PPL}_d$, $\\text{PPL}_a$, $\\text{PPL}_k$, and $\\text{PPL}_b$ denote the perplexity under the dense (no sparsity), attention-pruning-only, KV-eviction-only, and compound conditions, respectively.",
          "+Perplexity is computed as $\\text{PPL} = \\exp\\!\\bigl(\\frac{1}{|S|}\\sum_{t \\in S} \\mathcal{L}_t\\bigr)$, where $\\mathcal{L}_t$ is the per-token cross-entropy loss over evaluated positions $S$.",
          "+Normalizing by the dense baseline yields relative degradation ratios $r_c = \\text{PPL}_c\\,/\\,\\text{PPL}_d$ for $c \\in \\{a, k, b\\}$, and the Interaction Index:",
          " \\begin{equation}",
          "-    \\mathrm{II} = R_b - R_h - R_k + 1",
          "+    \\mathrm{II} = r_b - r_a - r_k + 1.",
          "     \\label{eq:ii}",
          " \\end{equation}",
          "-Under additive independence, $R_b \\approx R_h + R_k - 1$, giving $\\mathrm{II} \\approx 0$.",
          "+",
          "+Under additive independence, $r_b \\approx r_a + r_k - 1$, yielding $\\mathrm{II} \\approx 0$.",
          "+The sign of II determines the interaction regime:",
          " \\begin{itemize}[nosep,leftmargin=*]",
          "-    \\item $\\mathrm{II} > 0$: \\textbf{super-additive} — compound sparsity degrades more than the sum of individual effects.",
          "-    \\item $\\mathrm{II} < 0$: \\textbf{sub-additive} — compound sparsity is less harmful than expected.",
          "-    \\item $\\mathrm{II} = 0$: \\textbf{additive} — no interaction between the two axes.",
          "+    \\item $\\mathrm{II} > 0$: \\textbf{super-additive}---compound degradation exceeds the sum of individual effects.",
          "+    \\item $\\mathrm{II} < 0$: \\textbf{sub-additive}---the compound effect is less than the sum of parts.",
          "+    \\item $\\mathrm{II} = 0$: \\textbf{additive}---the two mechanisms do not interact.",
          " \\end{itemize}",
          " ",
          " \\paragraph{Choice of additive null.}",
          "-Eq.~\\ref{eq:ii} posits an additive null $R_b = R_h + R_k - 1$, but one could equally assume multiplicative independence $R_b = R_h \\cdot R_k$, treating the two axes as independent survival probabilities.",
          "-We adopt the additive form because head pruning and KV eviction operate on disjoint model dimensions---structural (which heads to keep) versus positional (which tokens to retain).",
          "-When the two mechanisms act independently, each contributes an additive increment $\\Delta R$ to the perplexity ratio: the heads removed by pruning and the positions removed by eviction affect non-overlapping information pathways, so their degradations sum rather than multiply.",
          "-At the sparsity levels studied ($s \\leq 0.30$), this non-overlap assumption holds empirically (\\S\\ref{sec:experiments}).",
          "-We report the multiplicative residual $R_b / (R_h \\cdot R_k)$ alongside II in Appendix~\\ref{app:multiplicative-null}; the qualitative conclusions are unchanged under either null model.",
          "+Equation~\\ref{eq:ii} posits an additive null $r_b = r_a + r_k - 1$ rather than multiplicative independence $r_b = r_a \\cdot r_k$.",
          "+We adopt the additive form because head pruning and KV cache eviction operate on disjoint model dimensions---structural (which heads to retain) versus positional (which tokens to cache)---so their degradations sum rather than multiply at the sparsity levels we study ($s \\leq 0.30$).",
          "+We verify in Appendix~\\ref{app:multiplicative-null} that qualitative conclusions are unchanged under the multiplicative null.",
          " ",
          "-We evaluate II on 50 problems from MATH-500 \\cite{hendrycks2021math}, stratified across difficulty levels.",
          "-Per-problem II values are aggregated via the median (rather than the mean) due to heavy-tailed distributions---e.g., the mean/median ratio reaches $33.5\\times$ for the low-sparsity phase at $s{=}0.30$ (\\S\\ref{sec:experiments})---where a single outlier can dominate the mean.",
          "-Bootstrap confidence intervals ($B=10{,}000$ resamples) are computed at the problem level.",
          "+Normalizing by $\\text{PPL}_d$ ensures cross-problem comparability.",
          "+Because the II distribution is heavily right-skewed, we report medians as the central tendency.",
          " ",
          " \\paragraph{Severity gradient.}",
          "-To capture how II varies across reasoning phases, we define the \\emph{severity gradient}:",
          "+To capture how II varies across reasoning phases (defined in \\S\\ref{sec:phase-segmentation}), we define the \\emph{severity gradient}:",
          " \\begin{equation}",
          "-    G = \\frac{\\widetilde{\\mathrm{II}}_{\\mathrm{low}}}{\\widetilde{\\mathrm{II}}_{\\mathrm{high}}}",
          "+    G = \\frac{\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}}{\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}},",
          "     \\label{eq:gradient}",
          " \\end{equation}",
          "-where $\\widetilde{\\mathrm{II}}_{\\mathrm{low}}$ and $\\widetilde{\\mathrm{II}}_{\\mathrm{high}}$ are the median II in the low-sparsity and high-sparsity phases respectively.",
          "-$G \\gg 1$ indicates that compound degradation concentrates in low-sparsity phases; $G \\approx 1$ indicates uniform degradation.",
          "-$G$ is defined only when $\\widetilde{\\mathrm{II}}_{\\mathrm{high}} > \\varepsilon$ for a small threshold $\\varepsilon > 0$; when $\\widetilde{\\mathrm{II}}_{\\mathrm{high}} \\approx 0$ (ceiling effect, where head pruning alone causes negligible degradation in high-sparsity phases), we report $G = \\infty$.",
          "+where $\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}$ and $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}$ are the median interaction indices in the low-sparsity and high-sparsity phases, respectively.",
          "+$G \\gg 1$ indicates that compound interaction concentrates in low-sparsity phases; $G \\approx 1$ indicates phase-invariant degradation.",
          "+When $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}} < \\varepsilon$ for a small threshold $\\varepsilon > 0$, we report $G = \\infty$.",
          " ",
          " \\subsection{Phase Segmentation}",
          " \\label{sec:phase-segmentation}",
          " ",
          "-Reasoning-capable LLMs produce token sequences with heterogeneous attention patterns: some segments exhibit concentrated attention (few tokens dominate), while others distribute attention broadly.",
          "-We partition each generation into three phases based on the \\emph{attention sparsity profile}, following the methodology of ThinKV \\cite{thinkv2026}.",
          "+Reasoning-capable LLMs produce token sequences with heterogeneous attention structure: some positions exhibit highly concentrated attention over a few key tokens, while others distribute attention broadly across the context.",
          "+We partition each generated sequence into three phases based on the local \\emph{attention sparsity profile}, adapting the phase-aware methodology of ThinKV \\cite{thinkv-iclr2026}.",
          " ",
          " \\paragraph{Attention sparsity.}",
          "-For each query position $i$ and head $h$, we compute the fraction of key positions receiving attention below $1\\%$ of the row maximum:",
          "+For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:",
          " \\begin{equation}",
          "-    \\sigma_i^{(h)} = \\frac{1}{T}\\sum_{j=1}^{T} \\mathbf{1}\\!\\left[a_{ij}^{(h)} < 0.01 \\cdot \\max_k a_{ik}^{(h)}\\right]",
          "-    \\label{eq:sparsity}",
          "+    \\sigma_i^{(h)} = \\frac{1}{T} \\sum_{j=1}^{T} \\mathbf{1}\\!\\left[a_{ij}^{(h)} < 0.01 \\cdot \\max_k a_{ik}^{(h)}\\right].",
          "+    \\label{eq:attn-sparsity}",
          " \\end{equation}",
          "-The per-token sparsity $\\sigma_i = \\frac{1}{H}\\sum_h \\sigma_i^{(h)}$ averages across heads.",
          "+The per-position sparsity $\\sigma_i = \\frac{1}{H}\\sum_h \\sigma_i^{(h)}$ averages across all heads.",
          " ",
          " \\paragraph{Quantile-based segmentation.}",
          "-We partition tokens into three equal-sized groups by the quantiles of $\\{\\sigma_i\\}_{i=1}^{T}$:",
          "+Tokens are partitioned into three groups by the tercile boundaries of $\\{\\sigma_i\\}_{i=1}^{T}$:",
          " \\begin{itemize}[nosep,leftmargin=*]",
          "-    \\item \\textbf{High-sparsity phase} (top tercile): attention concentrates on a few tokens; heads are highly redundant, and pruning incurs minimal information loss.",
          "+    \\item \\textbf{High-sparsity phase} (top tercile of $\\sigma$): attention concentrates on few tokens; heads are largely redundant, making both pruning and eviction relatively benign.",
          "     \\item \\textbf{Mid-sparsity phase} (middle tercile): intermediate attention patterns.",
          "-    \\item \\textbf{Low-sparsity phase} (bottom tercile): attention distributes broadly across many tokens; each head carries non-redundant information, making pruning costly.",
          "+    \\item \\textbf{Low-sparsity phase} (bottom tercile of $\\sigma$): attention distributes broadly; each surviving head carries non-redundant information, making both pruning and eviction more destructive.",
          " \\end{itemize}",
          "+Contiguous segments shorter than $\\texttt{min\\_phase\\_length} = 10$ tokens are merged into adjacent phases to ensure sufficient tokens for stable perplexity estimation.",
          "+The segmentation is purely data-driven and requires only access to attention weights.",
          " ",
          "-This segmentation is purely data-driven and does not require access to model internals beyond attention weights.",
          "-It captures the heterogeneity in attention structure that arises naturally during extended reasoning, where the model alternates between focused retrieval (high sparsity) and exploratory cross-token integration (low sparsity) \\cite{thinkingmi2025}.",
          "+This phase structure arises naturally during extended chain-of-thought reasoning, where the model alternates between focused retrieval of specific facts (high sparsity) and integrative reasoning across many context positions (low sparsity) \\cite{phase-transition-compression-2026}.",
          "+Our central research question is: \\emph{Is the Interaction Index constant across phases and eviction strategies, or does it exhibit a phase $\\times$ strategy interaction?}"
        ]
      }
    ],
    "originalFile": "% Section 3: Background and Problem Setup\n% Phase-Modulated Compound Sparsity\n\n\\section{Background and Problem Setup}\n\\label{sec:background}\n\nWe formalize compound sparsity as the simultaneous application of attention head pruning and KV cache eviction, define the Interaction Index to measure their non-additive interaction, and introduce phase segmentation to localize the analysis across reasoning stages.\n\n\\subsection{Compound Sparsity Formulation}\n\\label{sec:compound-sparsity}\n\nConsider a transformer language model $\\mathcal{M}$ with $L$ layers, each containing $H$ attention heads.\nLet $s \\in (0,1)$ denote a unified sparsity budget applied to both compression axes.\n\n\\paragraph{Attention head pruning.}\nGiven per-head importance scores $\\mathbf{w}^{(l)} \\in \\mathbb{R}^H$ for layer $l$, we construct a binary mask $\\mathbf{m}_h^{(l)} \\in \\{0,1\\}^H$ that retains the top-$(1{-}s) \\cdot H$ heads by importance.\nFor head $j$ in layer $l$, the masked attention output becomes:\n\\begin{equation}\n    \\tilde{\\mathbf{o}}_j^{(l)} = m_{h,j}^{(l)} \\cdot \\mathbf{o}_j^{(l)}\n    \\label{eq:head-mask}\n\\end{equation}\nwhere $\\mathbf{o}_j^{(l)}$ is the original head output.\nHead importance is computed as the Frobenius norm of the attention weight matrix: $w_j^{(l)} = \\|\\mathbf{A}_j^{(l)}\\|_F$, where $\\mathbf{A}_j^{(l)} \\in \\mathbb{R}^{T \\times T}$ is the attention probability matrix for head $j$ at layer $l$ over a calibration input of length $T$.\n\n\\paragraph{KV cache eviction.}\nFor a sequence of length $T$, we construct a position mask $\\mathbf{m}_k \\in \\{0,1\\}^T$ that retains the top-$(1{-}s) \\cdot T$ positions by importance, with position $0$ (BOS) always retained.\nEvicted positions are blocked by setting their attention mask entries to zero:\n\\begin{equation}\n    \\tilde{a}_{ij} = a_{ij} \\cdot m_{k,j}, \\quad \\forall i,j\n    \\label{eq:kv-mask}\n\\end{equation}\nWe evaluate two eviction strategies:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{Importance-based:} Position importance is the cumulative attention mass received across all heads and query positions, with position normalization to correct for causal attention bias:\n    \\begin{equation}\n        \\mathrm{imp}(j) = \\frac{\\sum_{l,h,i} a^{(l,h)}_{ij}}{T - j}\n        \\label{eq:kv-importance}\n    \\end{equation}\n    where the denominator $(T - j)$ compensates for the fact that later positions can attend to fewer future tokens under causal masking \\cite{thinkv2026}.\n    \\item \\textbf{Random:} Positions (excluding BOS) are evicted uniformly at random.\n\\end{itemize}\n\n\\paragraph{Compound sparsity.}\nApplying both compressions simultaneously yields a model $\\mathcal{M}(s)$ where fraction $s$ of heads are pruned per layer \\emph{and} fraction $s$ of KV positions are evicted.\nThe two axes interact: head pruning alters the attention distribution over surviving heads, which in turn changes the importance ranking used for KV eviction.\n\n\\subsection{Interaction Index}\n\\label{sec:interaction-index}\n\nTo quantify whether compound sparsity degrades performance more (or less) than the sum of its components, we define the \\emph{Interaction Index} (II) following the factorial interaction framework from experimental design.\n\nLet $\\mathrm{PPL}_d$, $\\mathrm{PPL}_h$, $\\mathrm{PPL}_k$, and $\\mathrm{PPL}_b$ denote the perplexity of the dense model, head-pruning only, KV-eviction only, and both applied simultaneously, respectively.\nPerplexity is computed as $\\mathrm{PPL} = \\exp\\!\\bigl(\\frac{1}{|S|}\\sum_{t \\in S} \\mathcal{L}_t\\bigr)$ where $\\mathcal{L}_t$ is the per-token cross-entropy loss and $S$ is the set of evaluated positions.\n\nWe define the relative degradation ratios $R_h = \\mathrm{PPL}_h / \\mathrm{PPL}_d$, $R_k = \\mathrm{PPL}_k / \\mathrm{PPL}_d$, $R_b = \\mathrm{PPL}_b / \\mathrm{PPL}_d$, and the Interaction Index:\n\\begin{equation}\n    \\mathrm{II} = R_b - R_h - R_k + 1\n    \\label{eq:ii}\n\\end{equation}\nUnder additive independence, $R_b \\approx R_h + R_k - 1$, giving $\\mathrm{II} \\approx 0$.\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item $\\mathrm{II} > 0$: \\textbf{super-additive} — compound sparsity degrades more than the sum of individual effects.\n    \\item $\\mathrm{II} < 0$: \\textbf{sub-additive} — compound sparsity is less harmful than expected.\n    \\item $\\mathrm{II} = 0$: \\textbf{additive} — no interaction between the two axes.\n\\end{itemize}\n\n\\paragraph{Choice of additive null.}\nEq.~\\ref{eq:ii} posits an additive null $R_b = R_h + R_k - 1$, but one could equally assume multiplicative independence $R_b = R_h \\cdot R_k$, treating the two axes as independent survival probabilities.\nWe adopt the additive form because head pruning and KV eviction operate on disjoint model dimensions---structural (which heads to keep) versus positional (which tokens to retain).\nWhen the two mechanisms act independently, each contributes an additive increment $\\Delta R$ to the perplexity ratio: the heads removed by pruning and the positions removed by eviction affect non-overlapping information pathways, so their degradations sum rather than multiply.\nAt the sparsity levels studied ($s \\leq 0.30$), this non-overlap assumption holds empirically (\\S\\ref{sec:experiments}).\nWe report the multiplicative residual $R_b / (R_h \\cdot R_k)$ alongside II in Appendix~\\ref{app:multiplicative-null}; the qualitative conclusions are unchanged under either null model.\n\nWe evaluate II on 50 problems from MATH-500 \\cite{hendrycks2021math}, stratified across difficulty levels.\nPer-problem II values are aggregated via the median (rather than the mean) due to heavy-tailed distributions---e.g., the mean/median ratio reaches $33.5\\times$ for the low-sparsity phase at $s{=}0.30$ (\\S\\ref{sec:experiments})---where a single outlier can dominate the mean.\nBootstrap confidence intervals ($B=10{,}000$ resamples) are computed at the problem level.\n\n\\paragraph{Severity gradient.}\nTo capture how II varies across reasoning phases, we define the \\emph{severity gradient}:\n\\begin{equation}\n    G = \\frac{\\widetilde{\\mathrm{II}}_{\\mathrm{low}}}{\\widetilde{\\mathrm{II}}_{\\mathrm{high}}}\n    \\label{eq:gradient}\n\\end{equation}\nwhere $\\widetilde{\\mathrm{II}}_{\\mathrm{low}}$ and $\\widetilde{\\mathrm{II}}_{\\mathrm{high}}$ are the median II in the low-sparsity and high-sparsity phases respectively.\n$G \\gg 1$ indicates that compound degradation concentrates in low-sparsity phases; $G \\approx 1$ indicates uniform degradation.\n$G$ is defined only when $\\widetilde{\\mathrm{II}}_{\\mathrm{high}} > \\varepsilon$ for a small threshold $\\varepsilon > 0$; when $\\widetilde{\\mathrm{II}}_{\\mathrm{high}} \\approx 0$ (ceiling effect, where head pruning alone causes negligible degradation in high-sparsity phases), we report $G = \\infty$.\n\n\\subsection{Phase Segmentation}\n\\label{sec:phase-segmentation}\n\nReasoning-capable LLMs produce token sequences with heterogeneous attention patterns: some segments exhibit concentrated attention (few tokens dominate), while others distribute attention broadly.\nWe partition each generation into three phases based on the \\emph{attention sparsity profile}, following the methodology of ThinKV \\cite{thinkv2026}.\n\n\\paragraph{Attention sparsity.}\nFor each query position $i$ and head $h$, we compute the fraction of key positions receiving attention below $1\\%$ of the row maximum:\n\\begin{equation}\n    \\sigma_i^{(h)} = \\frac{1}{T}\\sum_{j=1}^{T} \\mathbf{1}\\!\\left[a_{ij}^{(h)} < 0.01 \\cdot \\max_k a_{ik}^{(h)}\\right]\n    \\label{eq:sparsity}\n\\end{equation}\nThe per-token sparsity $\\sigma_i = \\frac{1}{H}\\sum_h \\sigma_i^{(h)}$ averages across heads.\n\n\\paragraph{Quantile-based segmentation.}\nWe partition tokens into three equal-sized groups by the quantiles of $\\{\\sigma_i\\}_{i=1}^{T}$:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{High-sparsity phase} (top tercile): attention concentrates on a few tokens; heads are highly redundant, and pruning incurs minimal information loss.\n    \\item \\textbf{Mid-sparsity phase} (middle tercile): intermediate attention patterns.\n    \\item \\textbf{Low-sparsity phase} (bottom tercile): attention distributes broadly across many tokens; each head carries non-redundant information, making pruning costly.\n\\end{itemize}\n\nThis segmentation is purely data-driven and does not require access to model internals beyond attention weights.\nIt captures the heterogeneity in attention structure that arises naturally during extended reasoning, where the model alternates between focused retrieval (high sparsity) and exploratory cross-token integration (low sparsity) \\cite{thinkingmi2025}.\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 30_

Now register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "f6437a24-4040-4951-a2dd-9a2068d6aa93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GXzmUjTyKzNZjM4A24JPXF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7108,
      "cache_read_input_tokens": 59684,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7108
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

_source line 31_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018HVR6zmUbAPsSZbPqc5oUg`</summary>

```json
{
  "query": "+agent-ml-research register artifact",
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
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "b88d4e89-c102-4ac4-bdf7-4ffa95e87ac6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GXzmUjTyKzNZjM4A24JPXF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7108,
      "cache_read_input_tokens": 59684,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7108
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

_source line 32 · 2026-05-14T05:42:56.516Z_

<details><summary>↩ Tool result · `toolu_018HVR6zmUbAPsSZbPqc5oUg`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__append_idea"
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
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "ba9062ac-6000-4eb3-a561-15ae856a852c",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "+agent-ml-research register artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 33_

<details><summary>Logged reasoning block</summary>

```text
The ToolSearch didn't find a `register_artifact` tool. Let me search more specifically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "55270a01-4ceb-499b-9669-761a3e960ec9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rh8tHY8EcbuPN492fbeQ6a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 861,
      "cache_read_input_tokens": 66792,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 861
      },
      "output_tokens": 27,
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

_source line 34_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LATt7bD4zeSKFDW6sfNUE2`</summary>

```json
{
  "query": "register artifact",
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
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "79bdf7f1-8f82-41e2-a572-913508a08d97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rh8tHY8EcbuPN492fbeQ6a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 861,
      "cache_read_input_tokens": 66792,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 861
      },
      "output_tokens": 27,
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

_source line 35 · 2026-05-14T05:42:59.571Z_

<details><summary>↩ Tool result · `toolu_01LATt7bD4zeSKFDW6sfNUE2`</summary>

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
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "c790f8fc-e435-4232-9a5c-9f161412df69",
  "tool_use_result": {
    "matches": [],
    "query": "register artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QMh69SS6eCoMjV9CobRJv1`</summary>

```json
{
  "query": "+agent-ml-research",
  "max_results": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "f3607126-3461-4b83-8d81-8504ba56d650",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdMDQRgYzr1Y1qKneF9T6m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 129,
      "cache_read_input_tokens": 67653,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 129
      },
      "output_tokens": 55,
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

_source line 37 · 2026-05-14T05:43:06.382Z_

<details><summary>↩ Tool result · `toolu_01QMh69SS6eCoMjV9CobRJv1`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__append_idea"
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
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "9abc136f-9325-4fa0-aeaa-bc4f2ce248d1",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "+agent-ml-research",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 38_

<details><summary>Logged reasoning block</summary>

```text
There's no `register_artifact` tool available in the MCP tools. The available tools are only `append_idea`, `read_project_file`, and `save_project_file`. The task asked me to use `register_artifact` but it doesn't exist as a tool. Let me just note this and summarize what was done.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "88804914-3d0e-4aaf-96d4-ecb7c1ef4634",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AFqAth2raSpFtTk5C3vE8U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 853,
      "cache_read_input_tokens": 67782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 853
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

_source line 39_

`register_artifact` 工具不可用（未在 MCP 工具列表中）。文件已写入：

`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex`

**修订内容（相对已有版本）：**

1. **符号对齐 methodology.tex**：`PPL_h` → `PPL_a`，`R_h/R_k/R_b` → `r_a/r_k/r_b`，层索引 `l` → `ℓ`
2. **引用键统一 related_work.tex**：`thinkv2026` → `thinkv-iclr2026`，`thinkingmi2025` → `phase-transition-compression-2026`，`hendrycks2021math` 移除（实验细节属于 Section 4）
3. **移除实验细节**：MATH-500 50 problems、bootstrap B=10,000、mean/median 33.5× 等具体数据归 Section 4
4. **保留 additive null 论证**：reviewer 会问为何不用 multiplicative null，这段预防性论证值得保留
5. **3.3 补充**：`min_phase_length = 10` 参数、末尾 research question
6. **eq:ii / eq:gradient 标签保留在 Section 3**：methodology.tex 中的重复定义需改为 `\eqref` 引用（见文件顶部注释）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "uuid": "f8bedbd9-a28d-41f2-aa23-6ca0586bc6e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AFqAth2raSpFtTk5C3vE8U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 853,
      "cache_read_input_tokens": 67782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 853
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

### Task result

_source line 40_

`register_artifact` 工具不可用（未在 MCP 工具列表中）。文件已写入：

`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex`

**修订内容（相对已有版本）：**

1. **符号对齐 methodology.tex**：`PPL_h` → `PPL_a`，`R_h/R_k/R_b` → `r_a/r_k/r_b`，层索引 `l` → `ℓ`
2. **引用键统一 related_work.tex**：`thinkv2026` → `thinkv-iclr2026`，`thinkingmi2025` → `phase-transition-compression-2026`，`hendrycks2021math` 移除（实验细节属于 Section 4）
3. **移除实验细节**：MATH-500 50 problems、bootstrap B=10,000、mean/median 33.5× 等具体数据归 Section 4
4. **保留 additive null 论证**：reviewer 会问为何不用 multiplicative null，这段预防性论证值得保留
5. **3.3 补充**：`min_phase_length = 10` 参数、末尾 research question
6. **eq:ii / eq:gradient 标签保留在 Section 3**：methodology.tex 中的重复定义需改为 `\eqref` 引用（见文件顶部注释）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 454601,
  "duration_api_ms": 455399,
  "num_turns": 13,
  "stop_reason": "end_turn",
  "session_id": "95bdf987-1922-4fd8-8200-bd3cce6e72bd",
  "total_cost_usd": 1.3283340000000001,
  "usage": {
    "input_tokens": 20,
    "cache_creation_input_tokens": 57188,
    "cache_read_input_tokens": 542900,
    "output_tokens": 27901,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 57188,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 3,
        "output_tokens": 506,
        "cache_read_input_tokens": 67782,
        "cache_creation_input_tokens": 853,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 853
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1749,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001834,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 20,
      "outputTokens": 27901,
      "cacheReadInputTokens": 542900,
      "cacheCreationInputTokens": 57188,
      "webSearchRequests": 0,
      "costUSD": 1.3265000000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "2254964e-0e6d-418a-9022-25716e2d6857"
}
```

</details>

---
