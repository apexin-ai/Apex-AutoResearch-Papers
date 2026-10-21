# research plan005 negative literature

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 81
- **Recorded user turns:** 0
- **Tool calls:** 29
- **Original source:** `logs/workers/worker_research_plan005-negative-literature_20260514T020402.log`
- **Structured JSON:** [`efe6cb5d7b1b420ce17b.json`](../../sessions/ef/efe6cb5d7b1b420ce17b.json)

## Before a recorded user message

81 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
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
  "uuid": "ef31b89e-748a-4f8d-beae-9aff84357037",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/memory/"
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
    "resetsAt": 1778726400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "42a9fdbb-52ba-4caa-a34a-e639bc8e2b54",
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a"
}
```

---

### Assistant

_source line 4_

I'll search for relevant literature on auxiliary reward degradation in multi-objective RL, then compile a report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "af34bab3-08de-437e-bc2d-dfa32291cf95",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011H9ZdR44YWBdD7tJEEwvhq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11730,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11730
      },
      "output_tokens": 7,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019kiYz7yn1wZ8b2ZZ8JwccL`</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file",
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
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "f6cdcee8-d2be-4cd6-be47-09161613c37e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011H9ZdR44YWBdD7tJEEwvhq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11730,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11730
      },
      "output_tokens": 7,
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

_source line 6 · 2026-05-14T02:04:11.664Z_

<details><summary>↩ Tool result · `toolu_019kiYz7yn1wZ8b2ZZ8JwccL`</summary>

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
  "tool_name": "mcp__agent-ml-research__save_project_file"
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
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "0ec2fed0-20bc-4867-91f8-54b8f690f844",
  "tool_use_result": {
    "matches": [
      "WebSearch",
      "WebFetch",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file",
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
Let me start by reading the existing literature_map.yaml to understand the current structure, and then perform the web searches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "ad6cffff-3294-43d3-9ed8-23e2cfe94d11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014AJzSAZDRJRhBEXtycq7Rn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1721,
      "cache_read_input_tokens": 23571,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1721
      },
      "output_tokens": 21,
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

Let me first read the existing literature map, then run all searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "bf7fa2fd-ea90-4df1-b5da-6d195a2dfba8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014AJzSAZDRJRhBEXtycq7Rn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1721,
      "cache_read_input_tokens": 23571,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1721
      },
      "output_tokens": 21,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Qg7GMbxe7bpwXFB1nrDav7`</summary>

```json
{
  "project": "solver-trace-ablation",
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
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "ee84a035-8cd5-45ed-b3dd-30bcbacd6e35",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014AJzSAZDRJRhBEXtycq7Rn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1721,
      "cache_read_input_tokens": 23571,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1721
      },
      "output_tokens": 21,
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

_source line 10 · 2026-05-14T02:04:17.015Z_

<details><summary>↩ Tool result · `toolu_01Qg7GMbxe7bpwXFB1nrDav7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\", \"content\": \"# Literature Map for Solver Trace Ablation (STA)\\n# Categories:\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\n#   2. reward-shaping: Reward shaping for code/formal verification\\n#   3. mutation-testing: Mutation testing in software engineering\\n#   4. intensional-analysis: Intensional program analysis\\n#   5. reward-hacking: Reward hacking / overoptimization\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\n\\npapers:\\n\\n  # ============================================================\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\n  # ============================================================\\n\\n  - id: deepseek-r1\\n    title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n    authors: \\\"DeepSeek-AI\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2501.12948 / Nature 2025\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\n      intensional structural reward for neurosymbolic formalization.\\n    key_finding: >\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\n      showing emergent chain-of-thought reasoning from RL alone.\\n\\n  - id: deepseekmath\\n    title: \\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\"\\n    authors: \\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2402.03300\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\\n      used in STA training. GRPO eliminates the critic model by estimating\\n      baselines from group scores.\\n    key_finding: >\\n      GRPO matches PPO performance while significantly reducing training\\n      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.\\n\\n  - id: logic-rl\\n    title: \\\"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\\\"\\n    authors: \\\"Xian et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.14768\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic\\n      logic puzzles. Closest competitor to STA's approach of RL for logical\\n      formalization, though Logic-RL uses extensional (answer-correctness)\\n      rewards rather than STA's intensional structural rewards.\\n    key_finding: >\\n      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;\\n      rule-based reward design is critical for RL-based logical reasoning.\\n\\n  - id: mellgren-prolog-grpo\\n    title: \\\"Training Language Models to Use Prolog as a Tool\\\"\\n    authors: \\\"Niklas Mellgren\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2512.07407\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,\\n      directly comparable to STA's approach of GRPO-training a formalizer.\\n      Key difference: uses pass/fail reward vs STA's structural ISR.\\n    key_finding: >\\n      GRPO is effective for teaching small LLMs to use Prolog as a tool\\n      for logical and mathematical reasoning.\\n\\n  - id: satlm\\n    title: \\\"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\\\"\\n    authors: \\\"Xi Ye et al.\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023\\\"\\n    category: neurosymbolic-rl\\n    role: background\\n    relevance: >\\n      Neurosymbolic approach where LLM generates declarative specifications\\n      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)\\n      but uses prompting, not RL training.\\n    key_finding: >\\n      Declarative formulation outperforms imperative program-aided LMs by 23%\\n      on GSM; achieves SoTA on LSAT and BoardgameQA.\\n\\n  # ============================================================\\n  # Category 2: Reward shaping for code/formal verification\\n  # ============================================================\\n\\n  - id: lightman-verify-step\\n    title: \\\"Let's Verify Step by Step\\\"\\n    authors: \\\"Hunter Lightman, Vineet Kosaraju, Yura Burda, et al.\\\"\\n    year: 2023\\n    venue: \\\"arXiv 2305.20050 / ICLR 2024\\\"\\n    category: reward-shaping\\n    role: method-component\\n    relevance: >\\n      Establishes that process supervision (step-level reward) outperforms\\n      outcome supervision (final-answer reward) for reasoning. STA's ISR\\n      is analogous: it provides structural process-level signal about which\\n      components of a formalization matter, rather than just pass/fail.\\n    key_finding: >\\n      Process-supervised reward model achieves 78% on MATH, significantly\\n      outperforming outcome-supervised models. Released PRM800K dataset.\\n\\n  - id: reward-shaping-rlhf\\n    title: \\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\"\\n    authors: \\\"Jiayi Fu, Xuandong Zhao, Chengyuan Yao, et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.18770\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Studies reward shaping design principles for RLHF: bounded rewards and\\n      rapid-then-convergent growth. STA's ISR follows these principles\\n      naturally since structural necessity scores are bounded [0,1].\\n    key_finding: >\\n      Two key reward shaping principles: (1) bounded RL reward, (2) rapid\\n      initial growth with gradual convergence. PAR method achieves 5%+\\n      win rate improvement on AlpacaEval 2.0.\\n\\n  - id: rlvr-reasoning\\n    title: \\\"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2506.14245\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize\\n      reasoning. STA argues that for neurosymbolic formalization, binary reward\\n      is insufficient and structural reward is needed to avoid reward hacking.\\n    key_finding: >\\n      RLVR with binary verification implicitly teaches correct reasoning\\n      strategies, not just answer matching.\\n\\n  - id: rubric-grpo\\n    title: \\\"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2605.08061\\\"\\n    category: reward-shaping\\n    role: direct-competitor\\n    relevance: >\\n      Uses structured rubric-based rewards with GRPO, similar in spirit to\\n      STA's structured ISR. Key difference: rubric rewards come from LLM\\n      judges, while ISR comes from solver-based mutation testing.\\n    key_finding: >\\n      Structured multi-dimensional reward signals improve GRPO training\\n      generalization compared to scalar rewards.\\n\\n  # ============================================================\\n  # Category 3: Mutation testing in software engineering\\n  # ============================================================\\n\\n  - id: demillo1978\\n    title: \\\"Hints on Test Data Selection: Help for the Practicing Programmer\\\"\\n    authors: \\\"Richard A. DeMillo, Richard J. Lipton, Frederick G. Sayward\\\"\\n    year: 1978\\n    venue: \\\"Computer 11(4):34-43\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Foundational paper introducing mutation testing. STA's component\\n      necessity testing directly extends this idea: instead of mutating\\n      source code to test test suites, STA mutates logical formulas\\n      to test component necessity for solver success.\\n    key_finding: >\\n      Introduced mutation testing and the coupling effect hypothesis:\\n      tests that detect simple faults also detect complex faults.\\n\\n  - id: offutt-coupling\\n    title: \\\"Investigations of the Software Testing Coupling Effect\\\"\\n    authors: \\\"A. Jefferson Offutt\\\"\\n    year: 1992\\n    venue: \\\"ACM TOSEM 1(1):5-20\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Empirically validates the coupling effect hypothesis that underpins\\n      mutation testing. STA's single-component ablation is analogous to\\n      first-order mutation; the coupling effect suggests this suffices.\\n    key_finding: >\\n      Test data killing all first-order mutants killed >99% of second-\\n      and third-order mutants, validating the coupling effect.\\n\\n  - id: jia-harman-survey\\n    title: \\\"An Analysis and Survey of the Development of Mutation Testing\\\"\\n    authors: \\\"Yue Jia, Mark Harman\\\"\\n    year: 2011\\n    venue: \\\"IEEE TSE 37(5):649-678\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Comprehensive survey of mutation testing covering three decades of\\n      development. Provides theoretical and practical foundation for STA's\\n      adaptation of mutation testing to logical formulas.\\n    key_finding: >\\n      Systematic classification of mutation operators, cost reduction\\n      techniques, and equivalence problem -- all relevant to STA's design\\n      of clause-level ablation operators.\\n\\n  - id: just-mutants-real-faults\\n    title: \\\"Are Mutants a Valid Substitute for Real Faults in Software Testing?\\\"\\n    authors: \\\"Rene Just, Darioush Jalali, Laura Inozemtseva, et al.\\\"\\n    year: 2014\\n    venue: \\\"FSE 2014\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Validates that mutation testing (structural/intensional analysis of\\n      program adequacy) correlates with real fault detection. Supports STA's\\n      premise that structural analysis of formalization components provides\\n      meaningful signal about formalization quality.\\n    key_finding: >\\n      Mutant detection is statistically correlated with real fault detection,\\n      and mutation score is a better predictor of test effectiveness than\\n      code coverage.\\n\\n  - id: llmorpheus\\n    title: \\\"LLMorpheus: Mutation Testing Using Large Language Models\\\"\\n    authors: \\\"Frank Tip, Jon Bell, et al.\\\"\\n    year: 2025\\n    venue: \\\"IEEE TSE 2025\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Uses LLMs to generate realistic code mutants beyond traditional\\n      mutation operators. Shows mutation testing evolving toward\\n      ML-integrated approaches, validating STA's cross-pollination\\n      of mutation testing ideas into ML training.\\n    key_finding: >\\n      LLM-generated mutants simulate real bugs that rule-based operators\\n      cannot produce, improving mutation testing realism.\\n\\n  - id: mutation-guided-meta\\n    title: \\\"Mutation-Guided LLM-based Test Generation at Meta\\\"\\n    authors: \\\"Christopher Foster et al.\\\"\\n    year: 2025\\n    venue: \\\"FSE 2025\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Industrial application of mutation-guided LLM test generation at\\n      Meta. Demonstrates that mutation analysis can guide LLM behavior\\n      in production -- analogous to how STA uses mutation (ablation) to\\n      guide GRPO reward signal.\\n    key_finding: >\\n      Mutation-guided approach generates tests that kill significantly\\n      more mutants than unguided LLM test generation at Meta scale.\\n\\n  - id: mutation-consistency-llm\\n    title: \\\"Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs\\\"\\n    authors: \\\"Various\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2401.05940\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Uses code mutations to evaluate LLM code understanding consistency.\\n      Conceptually related to STA: both use systematic code/formula\\n      mutations to assess model capabilities.\\n    key_finding: >\\n      LLMs show significant inconsistency when evaluated on mutated code\\n      variants, suggesting superficial pattern matching.\\n\\n  # ============================================================\\n  # Category 4: Intensional program analysis\\n  # ============================================================\\n\\n  - id: deepmutation\\n    title: \\\"A Probabilistic Framework for Mutation Testing in Deep Neural Networks\\\"\\n    authors: \\\"Various\\\"\\n    year: 2023\\n    venue: \\\"Information and Software Technology 2023\\\"\\n    category: intensional-analysis\\n   \\n\\n... [截断: 省略 8468 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 20468, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "17b08bd0-ced0-4159-b9bd-2ebe20c446e1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\\\", \\\"content\\\": \\\"# Literature Map for Solver Trace Ablation (STA)\\\\n# Categories:\\\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\\\n#   2. reward-shaping: Reward shaping for code/formal verification\\\\n#   3. mutation-testing: Mutation testing in software engineering\\\\n#   4. intensional-analysis: Intensional program analysis\\\\n#   5. reward-hacking: Reward hacking / overoptimization\\\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\\\n\\\\npapers:\\\\n\\\\n  # ============================================================\\\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\\\n  # ============================================================\\\\n\\\\n  - id: deepseek-r1\\\\n    title: \\\\\\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"DeepSeek-AI\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2501.12948 / Nature 2025\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: method-component\\\\n    relevance: >\\\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\\\n      intensional structural reward for neurosymbolic formalization.\\\\n    key_finding: >\\\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\\\n      showing emergent chain-of-thought reasoning from RL alone.\\\\n\\\\n  - id: deepseekmath\\\\n    title: \\\\\\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2402.03300\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: method-component\\\\n    relevance: >\\\\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\\\\n      used in STA training. GRPO eliminates the critic model by estimating\\\\n      baselines from group scores.\\\\n    key_finding: >\\\\n      GRPO matches PPO performance while significantly reducing training\\\\n      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.\\\\n\\\\n  - id: logic-rl\\\\n    title: \\\\\\\"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Xian et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2502.14768\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic\\\\n      logic puzzles. Closest competitor to STA's approach of RL for logical\\\\n      formalization, though Logic-RL uses extensional (answer-correctness)\\\\n      rewards rather than STA's intensional structural rewards.\\\\n    key_finding: >\\\\n      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;\\\\n      rule-based reward design is critical for RL-based logical reasoning.\\\\n\\\\n  - id: mellgren-prolog-grpo\\\\n    title: \\\\\\\"Training Language Models to Use Prolog as a Tool\\\\\\\"\\\\n    authors: \\\\\\\"Niklas Mellgren\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2512.07407\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,\\\\n      directly comparable to STA's approach of GRPO-training a formalizer.\\\\n      Key difference: uses pass/fail reward vs STA's structural ISR.\\\\n    key_finding: >\\\\n      GRPO is effective for teaching small LLMs to use Prolog as a tool\\\\n      for logical and mathematical reasoning.\\\\n\\\\n  - id: satlm\\\\n    title: \\\\\\\"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\\\\\\\"\\\\n    authors: \\\\\\\"Xi Ye et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"NeurIPS 2023\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: background\\\\n    relevance: >\\\\n      Neurosymbolic approach where LLM generates declarative specifications\\\\n      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)\\\\n      but uses prompting, not RL training.\\\\n    key_finding: >\\\\n      Declarative formulation outperforms imperative program-aided LMs by 23%\\\\n      on GSM; achieves SoTA on LSAT and BoardgameQA.\\\\n\\\\n  # ============================================================\\\\n  # Category 2: Reward shaping for code/formal verification\\\\n  # ============================================================\\\\n\\\\n  - id: lightman-verify-step\\\\n    title: \\\\\\\"Let's Verify Step by Step\\\\\\\"\\\\n    authors: \\\\\\\"Hunter Lightman, Vineet Kosaraju, Yura Burda, et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"arXiv 2305.20050 / ICLR 2024\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: method-component\\\\n    relevance: >\\\\n      Establishes that process supervision (step-level reward) outperforms\\\\n      outcome supervision (final-answer reward) for reasoning. STA's ISR\\\\n      is analogous: it provides structural process-level signal about which\\\\n      components of a formalization matter, rather than just pass/fail.\\\\n    key_finding: >\\\\n      Process-supervised reward model achieves 78% on MATH, significantly\\\\n      outperforming outcome-supervised models. Released PRM800K dataset.\\\\n\\\\n  - id: reward-shaping-rlhf\\\\n    title: \\\\\\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\\\\\"\\\\n    authors: \\\\\\\"Jiayi Fu, Xuandong Zhao, Chengyuan Yao, et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2502.18770\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      Studies reward shaping design principles for RLHF: bounded rewards and\\\\n      rapid-then-convergent growth. STA's ISR follows these principles\\\\n      naturally since structural necessity scores are bounded [0,1].\\\\n    key_finding: >\\\\n      Two key reward shaping principles: (1) bounded RL reward, (2) rapid\\\\n      initial growth with gradual convergence. PAR method achieves 5%+\\\\n      win rate improvement on AlpacaEval 2.0.\\\\n\\\\n  - id: rlvr-reasoning\\\\n    title: \\\\\\\"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2506.14245\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize\\\\n      reasoning. STA argues that for neurosymbolic formalization, binary reward\\\\n      is insufficient and structural reward is needed to avoid reward hacking.\\\\n    key_finding: >\\\\n      RLVR with binary verification implicitly teaches correct reasoning\\\\n      strategies, not just answer matching.\\\\n\\\\n  - id: rubric-grpo\\\\n    title: \\\\\\\"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2605.08061\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Uses structured rubric-based rewards with GRPO, similar in spirit to\\\\n      STA's structured ISR. Key difference: rubric rewards come from LLM\\\\n      judges, while ISR comes from solver-based mutation testing.\\\\n    key_finding: >\\\\n      Structured multi-dimensional reward signals improve GRPO training\\\\n      generalization compared to scalar rewards.\\\\n\\\\n  # ============================================================\\\\n  # Category 3: Mutation testing in software engineering\\\\n  # ============================================================\\\\n\\\\n  - id: demillo1978\\\\n    title: \\\\\\\"Hints on Test Data Selection: Help for the Practicing Programmer\\\\\\\"\\\\n    authors: \\\\\\\"Richard A. DeMillo, Richard J. Lipton, Frederick G. Sayward\\\\\\\"\\\\n    year: 1978\\\\n    venue: \\\\\\\"Computer 11(4):34-43\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Foundational paper introducing mutation testing. STA's component\\\\n      necessity testing directly extends this idea: instead of mutating\\\\n      source code to test test suites, STA mutates logical formulas\\\\n      to test component necessity for solver success.\\\\n    key_finding: >\\\\n      Introduced mutation testing and the coupling effect hypothesis:\\\\n      tests that detect simple faults also detect complex faults.\\\\n\\\\n  - id: offutt-coupling\\\\n    title: \\\\\\\"Investigations of the Software Testing Coupling Effect\\\\\\\"\\\\n    authors: \\\\\\\"A. Jefferson Offutt\\\\\\\"\\\\n    year: 1992\\\\n    venue: \\\\\\\"ACM TOSEM 1(1):5-20\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Empirically validates the coupling effect hypothesis that underpins\\\\n      mutation testing. STA's single-component ablation is analogous to\\\\n      first-order mutation; the coupling effect suggests this suffices.\\\\n    key_finding: >\\\\n      Test data killing all first-order mutants killed >99% of second-\\\\n      and third-order mutants, validating the coupling effect.\\\\n\\\\n  - id: jia-harman-survey\\\\n    title: \\\\\\\"An Analysis and Survey of the Development of Mutation Testing\\\\\\\"\\\\n    authors: \\\\\\\"Yue Jia, Mark Harman\\\\\\\"\\\\n    year: 2011\\\\n    venue: \\\\\\\"IEEE TSE 37(5):649-678\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Comprehensive survey of mutation testing covering three decades of\\\\n      development. Provides theoretical and practical foundation for STA's\\\\n      adaptation of mutation testing to logical formulas.\\\\n    key_finding: >\\\\n      Systematic classification of mutation operators, cost reduction\\\\n      techniques, and equivalence problem -- all relevant to STA's design\\\\n      of clause-level ablation operators.\\\\n\\\\n  - id: just-mutants-real-faults\\\\n    title: \\\\\\\"Are Mutants a Valid Substitute for Real Faults in Software Testing?\\\\\\\"\\\\n    authors: \\\\\\\"Rene Just, Darioush Jalali, Laura Inozemtseva, et al.\\\\\\\"\\\\n    year: 2014\\\\n    venue: \\\\\\\"FSE 2014\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Validates that mutation testing (structural/intensional analysis of\\\\n      program adequacy) correlates with real fault detection. Supports STA's\\\\n      premise that structural analysis of formalization components provides\\\\n      meaningful signal about formalization quality.\\\\n    key_finding: >\\\\n      Mutant detection is statistically correlated with real fault detection,\\\\n      and mutation score is a better predictor of test effectiveness than\\\\n      code coverage.\\\\n\\\\n  - id: llmorpheus\\\\n    title: \\\\\\\"LLMorpheus: Mutation Testing Using Large Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Frank Tip, Jon Bell, et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"IEEE TSE 2025\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Uses LLMs to generate realistic code mutants beyond traditional\\\\n      mutation operators. Shows mutation testing evolving toward\\\\n      ML-integrated approaches, validating STA's cross-pollination\\\\n      of mutation testing ideas into ML training.\\\\n    key_finding: >\\\\n      LLM-generated mutants simulate real bugs that rule-based operators\\\\n      cannot produce, improving mutation testing realism.\\\\n\\\\n  - id: mutation-guided-meta\\\\n    title: \\\\\\\"Mutation-Guided LLM-based Test Generation at Meta\\\\\\\"\\\\n    authors: \\\\\\\"Christopher Foster et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"FSE 2025\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Industrial application of mutation-guided LLM test generation at\\\\n      Meta. Demonstrates that mutation analysis can guide LLM behavior\\\\n      in production -- analogous to how STA uses mutation (ablation) to\\\\n      guide GRPO reward signal.\\\\n    key_finding: >\\\\n      Mutation-guided approach generates tests that kill significantly\\\\n      more mutants than unguided LLM test generation at Meta scale.\\\\n\\\\n  - id: mutation-consistency-llm\\\\n    title: \\\\\\\"Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2401.05940\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Uses code mutations to evaluate LLM code understanding consistency.\\\\n      Conceptually related to STA: both use systematic code/formula\\\\n      mutations to assess model capabilities.\\\\n    key_finding: >\\\\n      LLMs show significant inconsistency when evaluated on mutated code\\\\n      variants, suggesting superficial pattern matching.\\\\n\\\\n  # ============================================================\\\\n  # Category 4: Intensional program analysis\\\\n  # ============================================================\\\\n\\\\n  - id: deepmutation\\\\n    title: \\\\\\\"A Probabilistic Framework for Mutation Testing in Deep Neural Networks\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"Information and Software Technology 2023\\\\\\\"\\\\n    category: intensional-analysis\\\\n   \\\\n\\\\n... [截断: 省略 8468 字符，传 max_chars=0 获取完整内容]\\\", \\\"total_chars\\\": 20468, \\\"truncated\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\", \"content\": \"# Literature Map for Solver Trace Ablation (STA)\\n# Categories:\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\n#   2. reward-shaping: Reward shaping for code/formal verification\\n#   3. mutation-testing: Mutation testing in software engineering\\n#   4. intensional-analysis: Intensional program analysis\\n#   5. reward-hacking: Reward hacking / overoptimization\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\n\\npapers:\\n\\n  # ============================================================\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\n  # ============================================================\\n\\n  - id: deepseek-r1\\n    title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n    authors: \\\"DeepSeek-AI\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2501.12948 / Nature 2025\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\n      intensional structural reward for neurosymbolic formalization.\\n    key_finding: >\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\n      showing emergent chain-of-thought reasoning from RL alone.\\n\\n  - id: deepseekmath\\n    title: \\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\"\\n    authors: \\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2402.03300\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\\n      used in STA training. GRPO eliminates the critic model by estimating\\n      baselines from group scores.\\n    key_finding: >\\n      GRPO matches PPO performance while significantly reducing training\\n      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.\\n\\n  - id: logic-rl\\n    title: \\\"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\\\"\\n    authors: \\\"Xian et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.14768\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic\\n      logic puzzles. Closest competitor to STA's approach of RL for logical\\n      formalization, though Logic-RL uses extensional (answer-correctness)\\n      rewards rather than STA's intensional structural rewards.\\n    key_finding: >\\n      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;\\n      rule-based reward design is critical for RL-based logical reasoning.\\n\\n  - id: mellgren-prolog-grpo\\n    title: \\\"Training Language Models to Use Prolog as a Tool\\\"\\n    authors: \\\"Niklas Mellgren\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2512.07407\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,\\n      directly comparable to STA's approach of GRPO-training a formalizer.\\n      Key difference: uses pass/fail reward vs STA's structural ISR.\\n    key_finding: >\\n      GRPO is effective for teaching small LLMs to use Prolog as a tool\\n      for logical and mathematical reasoning.\\n\\n  - id: satlm\\n    title: \\\"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\\\"\\n    authors: \\\"Xi Ye et al.\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023\\\"\\n    category: neurosymbolic-rl\\n    role: background\\n    relevance: >\\n      Neurosymbolic approach where LLM generates declarative specifications\\n      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)\\n      but uses prompting, not RL training.\\n    key_finding: >\\n      Declarative formulation outperforms imperative program-aided LMs by 23%\\n      on GSM; achieves SoTA on LSAT and BoardgameQA.\\n\\n  # ============================================================\\n  # Category 2: Reward shaping for code/formal verification\\n  # ============================================================\\n\\n  - id: lightman-verify-step\\n    title: \\\"Let's Verify Step by Step\\\"\\n    authors: \\\"Hunter Lightman, Vineet Kosaraju, Yura Burda, et al.\\\"\\n    year: 2023\\n    venue: \\\"arXiv 2305.20050 / ICLR 2024\\\"\\n    category: reward-shaping\\n    role: method-component\\n    relevance: >\\n      Establishes that process supervision (step-level reward) outperforms\\n      outcome supervision (final-answer reward) for reasoning. STA's ISR\\n      is analogous: it provides structural process-level signal about which\\n      components of a formalization matter, rather than just pass/fail.\\n    key_finding: >\\n      Process-supervised reward model achieves 78% on MATH, significantly\\n      outperforming outcome-supervised models. Released PRM800K dataset.\\n\\n  - id: reward-shaping-rlhf\\n    title: \\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\"\\n    authors: \\\"Jiayi Fu, Xuandong Zhao, Chengyuan Yao, et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.18770\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Studies reward shaping design principles for RLHF: bounded rewards and\\n      rapid-then-convergent growth. STA's ISR follows these principles\\n      naturally since structural necessity scores are bounded [0,1].\\n    key_finding: >\\n      Two key reward shaping principles: (1) bounded RL reward, (2) rapid\\n      initial growth with gradual convergence. PAR method achieves 5%+\\n      win rate improvement on AlpacaEval 2.0.\\n\\n  - id: rlvr-reasoning\\n    title: \\\"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2506.14245\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize\\n      reasoning. STA argues that for neurosymbolic formalization, binary reward\\n      is insufficient and structural reward is needed to avoid reward hacking.\\n    key_finding: >\\n      RLVR with binary verification implicitly teaches correct reasoning\\n      strategies, not just answer matching.\\n\\n  - id: rubric-grpo\\n    title: \\\"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2605.08061\\\"\\n    category: reward-shaping\\n    role: direct-competitor\\n    relevance: >\\n      Uses structured rubric-based rewards with GRPO, similar in spirit to\\n      STA's structured ISR. Key difference: rubric rewards come from LLM\\n      judges, while ISR comes from solver-based mutation testing.\\n    key_finding: >\\n      Structured multi-dimensional reward signals improve GRPO training\\n      generalization compared to scalar rewards.\\n\\n  # ============================================================\\n  # Category 3: Mutation testing in software engineering\\n  # ============================================================\\n\\n  - id: demillo1978\\n    title: \\\"Hints on Test Data Selection: Help for the Practicing Programmer\\\"\\n    authors: \\\"Richard A. DeMillo, Richard J. Lipton, Frederick G. Sayward\\\"\\n    year: 1978\\n    venue: \\\"Computer 11(4):34-43\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Foundational paper introducing mutation testing. STA's component\\n      necessity testing directly extends this idea: instead of mutating\\n      source code to test test suites, STA mutates logical formulas\\n      to test component necessity for solver success.\\n    key_finding: >\\n      Introduced mutation testing and the coupling effect hypothesis:\\n      tests that detect simple faults also detect complex faults.\\n\\n  - id: offutt-coupling\\n    title: \\\"Investigations of the Software Testing Coupling Effect\\\"\\n    authors: \\\"A. Jefferson Offutt\\\"\\n    year: 1992\\n    venue: \\\"ACM TOSEM 1(1):5-20\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Empirically validates the coupling effect hypothesis that underpins\\n      mutation testing. STA's single-component ablation is analogous to\\n      first-order mutation; the coupling effect suggests this suffices.\\n    key_finding: >\\n      Test data killing all first-order mutants killed >99% of second-\\n      and third-order mutants, validating the coupling effect.\\n\\n  - id: jia-harman-survey\\n    title: \\\"An Analysis and Survey of the Development of Mutation Testing\\\"\\n    authors: \\\"Yue Jia, Mark Harman\\\"\\n    year: 2011\\n    venue: \\\"IEEE TSE 37(5):649-678\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Comprehensive survey of mutation testing covering three decades of\\n      development. Provides theoretical and practical foundation for STA's\\n      adaptation of mutation testing to logical formulas.\\n    key_finding: >\\n      Systematic classification of mutation operators, cost reduction\\n      techniques, and equivalence problem -- all relevant to STA's design\\n      of clause-level ablation operators.\\n\\n  - id: just-mutants-real-faults\\n    title: \\\"Are Mutants a Valid Substitute for Real Faults in Software Testing?\\\"\\n    authors: \\\"Rene Just, Darioush Jalali, Laura Inozemtseva, et al.\\\"\\n    year: 2014\\n    venue: \\\"FSE 2014\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Validates that mutation testing (structural/intensional analysis of\\n      program adequacy) correlates with real fault detection. Supports STA's\\n      premise that structural analysis of formalization components provides\\n      meaningful signal about formalization quality.\\n    key_finding: >\\n      Mutant detection is statistically correlated with real fault detection,\\n      and mutation score is a better predictor of test effectiveness than\\n      code coverage.\\n\\n  - id: llmorpheus\\n    title: \\\"LLMorpheus: Mutation Testing Using Large Language Models\\\"\\n    authors: \\\"Frank Tip, Jon Bell, et al.\\\"\\n    year: 2025\\n    venue: \\\"IEEE TSE 2025\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Uses LLMs to generate realistic code mutants beyond traditional\\n      mutation operators. Shows mutation testing evolving toward\\n      ML-integrated approaches, validating STA's cross-pollination\\n      of mutation testing ideas into ML training.\\n    key_finding: >\\n      LLM-generated mutants simulate real bugs that rule-based operators\\n      cannot produce, improving mutation testing realism.\\n\\n  - id: mutation-guided-meta\\n    title: \\\"Mutation-Guided LLM-based Test Generation at Meta\\\"\\n    authors: \\\"Christopher Foster et al.\\\"\\n    year: 2025\\n    venue: \\\"FSE 2025\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Industrial application of mutation-guided LLM test generation at\\n      Meta. Demonstrates that mutation analysis can guide LLM behavior\\n      in production -- analogous to how STA uses mutation (ablation) to\\n      guide GRPO reward signal.\\n    key_finding: >\\n      Mutation-guided approach generates tests that kill significantly\\n      more mutants than unguided LLM test generation at Meta scale.\\n\\n  - id: mutation-consistency-llm\\n    title: \\\"Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs\\\"\\n    authors: \\\"Various\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2401.05940\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Uses code mutations to evaluate LLM code understanding consistency.\\n      Conceptually related to STA: both use systematic code/formula\\n      mutations to assess model capabilities.\\n    key_finding: >\\n      LLMs show significant inconsistency when evaluated on mutated code\\n      variants, suggesting superficial pattern matching.\\n\\n  # ============================================================\\n  # Category 4: Intensional program analysis\\n  # ============================================================\\n\\n  - id: deepmutation\\n    title: \\\"A Probabilistic Framework for Mutation Testing in Deep Neural Networks\\\"\\n    authors: \\\"Various\\\"\\n    year: 2023\\n    venue: \\\"Information and Software Technology 2023\\\"\\n    category: intensional-analysis\\n   \\n\\n... [截断: 省略 8468 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 20468, \"truncated\": true}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HxH1LESBzBLXMgg6hBv7jV`</summary>

```json
{
  "query": "auxiliary reward degradation multi-objective reinforcement learning performance tradeoff 2023 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "0b71264e-222e-4a34-9e83-e26f9d8ef6cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014AJzSAZDRJRhBEXtycq7Rn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1721,
      "cache_read_input_tokens": 23571,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1721
      },
      "output_tokens": 21,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CU5226fgnmu6BShw8PFBbK`</summary>

```json
{
  "query": "reward shaping negative side effects reinforcement learning penalty auxiliary objective"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "309505ce-7973-446c-9622-5263875e62b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014AJzSAZDRJRhBEXtycq7Rn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1721,
      "cache_read_input_tokens": 23571,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1721
      },
      "output_tokens": 21,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_014m25ZkTFbqAGFc9fUbJ1qz`</summary>

```json
{
  "query": "process reward vs outcome reward conflict LLM GRPO training 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "6f8590f0-ac7b-484f-80b0-473a6098fc96",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014AJzSAZDRJRhBEXtycq7Rn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1721,
      "cache_read_input_tokens": 23571,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1721
      },
      "output_tokens": 21,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01St7oj5LNdiWJb4K2vyTk4o`</summary>

```json
{
  "query": "structural reward degradation reinforcement learning auxiliary task interference 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "894d50ba-1449-40e1-a635-8b36b00bb2bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014AJzSAZDRJRhBEXtycq7Rn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1721,
      "cache_read_input_tokens": 23571,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1721
      },
      "output_tokens": 21,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A6T3QzNPC7tUKfiXTQWHT5`</summary>

```json
{
  "query": "\"multi-objective RLHF\" \"reward conflict\" OR \"auxiliary reward\" OR \"reward tradeoff\" language model 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "b2306f8e-56ea-40e8-ac46-06a0595d0f2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014AJzSAZDRJRhBEXtycq7Rn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1721,
      "cache_read_input_tokens": 23571,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1721
      },
      "output_tokens": 21,
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

_source line 16 · 2026-05-14T02:04:25.739Z_

<details><summary>↩ Tool result · `toolu_01HxH1LESBzBLXMgg6hBv7jV`</summary>

```text
Web search results for query: "auxiliary reward degradation multi-objective reinforcement learning performance tradeoff 2023 2024 2025"

Links: [{"title":"Learning to Optimize Multi-Objective Alignment Through Dynamic Reward Weighting","url":"https://arxiv.org/html/2509.11452v1"},{"title":"Reinforcement Learning Journal 2025 Cover Page","url":"https://rlj.cs.umass.edu/2025/RLJ_2025_CoverPages.pdf"},{"title":"Published as a conference paper at RLC 2024","url":"https://openreview.net/pdf?id=qMlueQODdv"},{"title":"Multi-objective reward generalization: improving performance of Deep Reinforcement Learning for applications in single-asset trading - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10770001/"},{"title":"EMORL: Ensemble Multi-Objective Reinforcement ...","url":"https://aclanthology.org/2025.sigdial-1.33.pdf"},{"title":"GitHub - blacksnail789521/Agentic-RL-Training-Recipes: Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey · GitHub","url":"https://github.com/blacksnail789521/Agentic-RL-Training-Recipes"},{"title":"Multi-objective optimization for dynamic logistics scheduling based on hierarchical deep reinforcement learning | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-18309-y"},{"title":"Multi-Task Reward Learning from Human Ratings","url":"https://arxiv.org/html/2506.09183v1"},{"title":"Asynchronous Agentic Reinforcement Learning: A Tradeoff of Systems","url":"https://people.eecs.berkeley.edu/~kubitron/courses/cs262a-F25/projects/reports/project1008_paper_ver2_72488057446561351955.pdf"},{"title":"Learning Fair Pareto-Optimal Policies in Multi-Objective ...","url":"https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_350.pdf"}]

I've performed the web search for your query on auxiliary reward degradation and multi-objective reinforcement learning performance tradeoffs from 2023-2025. Here are the key findings:

## Recent Research on Multi-Objective RL and Performance Tradeoffs

### LLM Alignment and Dynamic Reward Weighting

Recent multi-objective RL work in the LLM era explores steerability perspectives with approaches including off-policy RL methods, post-hoc policy mixing, and conditional training that incorporates preference weights as input. However, these methods typically treat objectives statically using fixed-weight linear scalarization for rewards, which has a fundamental limitation: linear scalarization provably fails to capture non-convex regions of the Pareto front.

### Auxiliary Objectives and Performance Degradation

SEAC (which adds reward terms for task energy and time) requires careful tuning of its hyperparameters (balancing task, energy, and time costs) to avoid performance degradation. This illustrates the challenge of combining auxiliary objectives with primary task performance.

### Multi-Objective Optimization Approaches

Recent approaches use Pareto-optimal reward mechanisms with adaptive weighting to balance multiple objectives (time efficiency, cost control, service quality) while addressing sparse rewards and sample efficiency challenges.

### Multi-Objective RL Frameworks

Current research focuses on multi-objective online RL for LLMs that simultaneously optimizes auxiliary objectives alongside traditional accuracy metrics for complex reasoning tasks.

The search results show active research in 2024-2025 addressing how auxiliary objectives can create performance tradeoffs, with approaches moving toward dynamic weighting and Pareto-optimal solutions rather than fixed linear scalarization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "083ead3e-26f9-4860-ae41-d1bce016cdc4",
  "tool_use_result": {
    "query": "auxiliary reward degradation multi-objective reinforcement learning performance tradeoff 2023 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Tvm1bRMht9bdwPgK1UbZ81",
        "content": [
          {
            "title": "Learning to Optimize Multi-Objective Alignment Through Dynamic Reward Weighting",
            "url": "https://arxiv.org/html/2509.11452v1"
          },
          {
            "title": "Reinforcement Learning Journal 2025 Cover Page",
            "url": "https://rlj.cs.umass.edu/2025/RLJ_2025_CoverPages.pdf"
          },
          {
            "title": "Published as a conference paper at RLC 2024",
            "url": "https://openreview.net/pdf?id=qMlueQODdv"
          },
          {
            "title": "Multi-objective reward generalization: improving performance of Deep Reinforcement Learning for applications in single-asset trading - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10770001/"
          },
          {
            "title": "EMORL: Ensemble Multi-Objective Reinforcement ...",
            "url": "https://aclanthology.org/2025.sigdial-1.33.pdf"
          },
          {
            "title": "GitHub - blacksnail789521/Agentic-RL-Training-Recipes: Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey · GitHub",
            "url": "https://github.com/blacksnail789521/Agentic-RL-Training-Recipes"
          },
          {
            "title": "Multi-objective optimization for dynamic logistics scheduling based on hierarchical deep reinforcement learning | Scientific Reports",
            "url": "https://www.nature.com/articles/s41598-025-18309-y"
          },
          {
            "title": "Multi-Task Reward Learning from Human Ratings",
            "url": "https://arxiv.org/html/2506.09183v1"
          },
          {
            "title": "Asynchronous Agentic Reinforcement Learning: A Tradeoff of Systems",
            "url": "https://people.eecs.berkeley.edu/~kubitron/courses/cs262a-F25/projects/reports/project1008_paper_ver2_72488057446561351955.pdf"
          },
          {
            "title": "Learning Fair Pareto-Optimal Policies in Multi-Objective ...",
            "url": "https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_350.pdf"
          }
        ]
      },
      "I've performed the web search for your query on auxiliary reward degradation and multi-objective reinforcement learning performance tradeoffs from 2023-2025. Here are the key findings:\n\n## Recent Research on Multi-Objective RL and Performance Tradeoffs\n\n### LLM Alignment and Dynamic Reward Weighting\n\nRecent multi-objective RL work in the LLM era explores steerability perspectives with approaches including off-policy RL methods, post-hoc policy mixing, and conditional training that incorporates preference weights as input. However, these methods typically treat objectives statically using fixed-weight linear scalarization for rewards, which has a fundamental limitation: linear scalarization provably fails to capture non-convex regions of the Pareto front.\n\n### Auxiliary Objectives and Performance Degradation\n\nSEAC (which adds reward terms for task energy and time) requires careful tuning of its hyperparameters (balancing task, energy, and time costs) to avoid performance degradation. This illustrates the challenge of combining auxiliary objectives with primary task performance.\n\n### Multi-Objective Optimization Approaches\n\nRecent approaches use Pareto-optimal reward mechanisms with adaptive weighting to balance multiple objectives (time efficiency, cost control, service quality) while addressing sparse rewards and sample efficiency challenges.\n\n### Multi-Objective RL Frameworks\n\nCurrent research focuses on multi-objective online RL for LLMs that simultaneously optimizes auxiliary objectives alongside traditional accuracy metrics for complex reasoning tasks.\n\nThe search results show active research in 2024-2025 addressing how auxiliary objectives can create performance tradeoffs, with approaches moving toward dynamic weighting and Pareto-optimal solutions rather than fixed linear scalarization."
    ],
    "durationSeconds": 7.580833498000001
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T02:04:26.961Z_

<details><summary>↩ Tool result · `toolu_014m25ZkTFbqAGFc9fUbJ1qz`</summary>

```text
Web search results for query: "process reward vs outcome reward conflict LLM GRPO training 2024 2025"

Links: [{"title":"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training","url":"https://arxiv.org/html/2509.03403v1"},{"title":"The State of Reinforcement Learning for LLM Reasoning","url":"https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training"},{"title":"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=4DJoBOQNd0"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"GRPO IS SECRETLY A PROCESS REWARD MODEL","url":"https://openreview.net/pdf/1f109913a199dad205fa51f554aaa5e2a5a782d5.pdf"},{"title":"Paper page - Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training","url":"https://huggingface.co/papers/2509.03403"},{"title":"GitHub - bobxwu/learning-from-rewards-llm-papers: A comrephensive collection of learning from rewards in the post-training and test-time scaling of LLMs, with a focus on both reward models and learning strategies across training, inference, and post-inference stages. · GitHub","url":"https://github.com/bobxwu/learning-from-rewards-llm-papers"},{"title":"Let’s Verify Step by Step, ORM vs PRM | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/lets-verify-step-by-step-orm-vs-prm-613ecffb59ab"},{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"},{"title":"Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=A6Y7AqlzLW"}]

Based on the search results, here's what I found about process reward vs outcome reward conflict in LLM GRPO training:

## Key Findings

### The Core Conflict

Since verifiers can only verify outcome results, rewards are too sparse and coarse to measure intermediate step quality. For instance, if a correct answer contains flawed logic, Outcome Reward Models (ORMs) cannot distinguish it from a completely correct response. Incorporating such flawed examples introduces unreliable gradients, leading to significant instability and misguided learning.

### Process Reward Models (PRMs) vs Outcome Reward Models (ORMs)

Process reward models (PRMs) are a promising approach for improving reasoning in LLMs. PRMs provide feedback at each step of a multi-step reasoning trace, improving credit assignment over outcome reward models (ORMs) that only provide feedback at the final step.

### Recent Approaches to Harmonize Process and Outcome Rewards

Conditional Reward Modeling (CRM) frames LLM reasoning as a temporal process leading to a correct answer, where the reward of each reasoning step is conditioned on preceding steps and explicitly linked to the final outcome of the reasoning trajectory.

PROF ranks and filters responses based on process–outcome consistency between PRMs and ORMs, removing samples where reasoning and results conflict to reduce noisy gradients, and can be seamlessly integrated with RL methods such as GRPO.

### GRPO and Process Rewards

GRPO induces a Monte-Carlo-based PRM, assigning rewards and advantages derived from outcome-level rewards and Monte-Carlo-sampled completions to sub-trajectories whenever subsets of trajectories within each group share identical prefixes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "3bd08989-8544-4b21-85d5-bb4e897ee4dd",
  "tool_use_result": {
    "query": "process reward vs outcome reward conflict LLM GRPO training 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CcbJPf67icCQnFsKL2SCvE",
        "content": [
          {
            "title": "Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training",
            "url": "https://arxiv.org/html/2509.03403v1"
          },
          {
            "title": "The State of Reinforcement Learning for LLM Reasoning",
            "url": "https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training"
          },
          {
            "title": "Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=4DJoBOQNd0"
          },
          {
            "title": "A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models",
            "url": "https://arxiv.org/html/2510.08049v3"
          },
          {
            "title": "GRPO IS SECRETLY A PROCESS REWARD MODEL",
            "url": "https://openreview.net/pdf/1f109913a199dad205fa51f554aaa5e2a5a782d5.pdf"
          },
          {
            "title": "Paper page - Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training",
            "url": "https://huggingface.co/papers/2509.03403"
          },
          {
            "title": "GitHub - bobxwu/learning-from-rewards-llm-papers: A comrephensive collection of learning from rewards in the post-training and test-time scaling of LLMs, with a focus on both reward models and learning strategies across training, inference, and post-inference stages. · GitHub",
            "url": "https://github.com/bobxwu/learning-from-rewards-llm-papers"
          },
          {
            "title": "Let’s Verify Step by Step, ORM vs PRM | by Yanan Chen | Medium",
            "url": "https://medium.com/@yananchen1116/lets-verify-step-by-step-orm-vs-prm-613ecffb59ab"
          },
          {
            "title": "Group Relative Policy Optimization (GRPO)",
            "url": "https://cameronrwolfe.substack.com/p/grpo"
          },
          {
            "title": "Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=A6Y7AqlzLW"
          }
        ]
      },
      "Based on the search results, here's what I found about process reward vs outcome reward conflict in LLM GRPO training:\n\n## Key Findings\n\n### The Core Conflict\n\nSince verifiers can only verify outcome results, rewards are too sparse and coarse to measure intermediate step quality. For instance, if a correct answer contains flawed logic, Outcome Reward Models (ORMs) cannot distinguish it from a completely correct response. Incorporating such flawed examples introduces unreliable gradients, leading to significant instability and misguided learning.\n\n### Process Reward Models (PRMs) vs Outcome Reward Models (ORMs)\n\nProcess reward models (PRMs) are a promising approach for improving reasoning in LLMs. PRMs provide feedback at each step of a multi-step reasoning trace, improving credit assignment over outcome reward models (ORMs) that only provide feedback at the final step.\n\n### Recent Approaches to Harmonize Process and Outcome Rewards\n\nConditional Reward Modeling (CRM) frames LLM reasoning as a temporal process leading to a correct answer, where the reward of each reasoning step is conditioned on preceding steps and explicitly linked to the final outcome of the reasoning trajectory.\n\nPROF ranks and filters responses based on process–outcome consistency between PRMs and ORMs, removing samples where reasoning and results conflict to reduce noisy gradients, and can be seamlessly integrated with RL methods such as GRPO.\n\n### GRPO and Process Rewards\n\nGRPO induces a Monte-Carlo-based PRM, assigning rewards and advantages derived from outcome-level rewards and Monte-Carlo-sampled completions to sub-trajectories whenever subsets of trajectories within each group share identical prefixes."
    ],
    "durationSeconds": 7.313455842
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T02:04:27.426Z_

<details><summary>↩ Tool result · `toolu_01St7oj5LNdiWJb4K2vyTk4o`</summary>

```text
Web search results for query: "structural reward degradation reinforcement learning auxiliary task interference 2023 2024"

Links: [{"title":"Structure in Deep Reinforcement Learning: A Survey and ...","url":"https://www.jair.org/index.php/jair/article/download/15703/27028/38774"},{"title":"(PDF) Overcoming Reward Model Noise in Instruction-Guided Reinforcement Learning","url":"https://www.researchgate.net/publication/384295139_Overcoming_Reward_Model_Noise_in_Instruction-Guided_Reinforcement_Learning"},{"title":"Journal of Artificial Intelligence Research 79 (2024) 1167-1236","url":"https://arxiv.org/pdf/2306.16021"},{"title":"Reinforcement Learning for Finite Space Mean-Field Type ...","url":"https://rlj.cs.umass.edu/2025/RLJ_2025_CoverPages.pdf"},{"title":"Reward Models in Deep Reinforcement Learning: A Survey","url":"https://arxiv.org/html/2506.15421v1"},{"title":"Published as a conference paper at RLC 2024","url":"https://openreview.net/pdf?id=qMlueQODdv"},{"title":"Reward Models in Deep Reinforcement Learning: A Survey","url":"https://www.ijcai.org/proceedings/2025/1199.pdf"},{"title":"Reinforcement Learning for LLM Agent Planning","url":"https://aclanthology.org/2025.emnlp-industry.116.pdf"},{"title":"Comprehensive Overview of Reward Engineering and Shaping in Advancing Reinforcement Learning Applications","url":"https://arxiv.org/html/2408.10215v1"},{"title":"Alternating Reinforcement Learning and Supervised Fine- ...","url":"https://aclanthology.org/2024.emnlp-main.252.pdf"}]

I found several research papers related to reinforcement learning, reward design, and auxiliary tasks from 2023-2024. Here are the key findings:

## Key Research Areas

**Auxiliary Tasks and Reward Structures:**
Auxiliary losses help with generalization and serve as entry points for human-like inductive biases, with metrics inspired by the geometry of latent decompositions helping to learn optimal values in multi-task settings.

**Reward Model Degradation:**
Research reveals a critical vulnerability where a small amount of noise in reward signals can severely degrade agent performance, with agents using auxiliary reward models without proper noise handling performing worse than exploration-driven methods in sparse reward environments.

**Specific Challenges with Auxiliary Rewards:**
False positive rewards—where the reward model incorrectly assigns rewards to trajectories that don't fulfill given instructions—are more detrimental to learning than false negatives, with cosine similarity metrics being prone to generating such false positive reward signals.

**Multi-task and Structure in RL:**
Incorporating structure improves the sample efficiency of constrained optimization methods while making them more interpretable, which is particularly relevant to multi-task and auxiliary task scenarios.

The search results indicate that recent 2023-2024 research focuses on understanding how auxiliary tasks and reward signals can inadvertently degrade performance through noise and misalignment, and how structural approaches can mitigate these issues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "3a0c7a3f-124f-40c4-941e-cf8f2b70aec8",
  "tool_use_result": {
    "query": "structural reward degradation reinforcement learning auxiliary task interference 2023 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RooqU6ArEsgWAyg4G62HY1",
        "content": [
          {
            "title": "Structure in Deep Reinforcement Learning: A Survey and ...",
            "url": "https://www.jair.org/index.php/jair/article/download/15703/27028/38774"
          },
          {
            "title": "(PDF) Overcoming Reward Model Noise in Instruction-Guided Reinforcement Learning",
            "url": "https://www.researchgate.net/publication/384295139_Overcoming_Reward_Model_Noise_in_Instruction-Guided_Reinforcement_Learning"
          },
          {
            "title": "Journal of Artificial Intelligence Research 79 (2024) 1167-1236",
            "url": "https://arxiv.org/pdf/2306.16021"
          },
          {
            "title": "Reinforcement Learning for Finite Space Mean-Field Type ...",
            "url": "https://rlj.cs.umass.edu/2025/RLJ_2025_CoverPages.pdf"
          },
          {
            "title": "Reward Models in Deep Reinforcement Learning: A Survey",
            "url": "https://arxiv.org/html/2506.15421v1"
          },
          {
            "title": "Published as a conference paper at RLC 2024",
            "url": "https://openreview.net/pdf?id=qMlueQODdv"
          },
          {
            "title": "Reward Models in Deep Reinforcement Learning: A Survey",
            "url": "https://www.ijcai.org/proceedings/2025/1199.pdf"
          },
          {
            "title": "Reinforcement Learning for LLM Agent Planning",
            "url": "https://aclanthology.org/2025.emnlp-industry.116.pdf"
          },
          {
            "title": "Comprehensive Overview of Reward Engineering and Shaping in Advancing Reinforcement Learning Applications",
            "url": "https://arxiv.org/html/2408.10215v1"
          },
          {
            "title": "Alternating Reinforcement Learning and Supervised Fine- ...",
            "url": "https://aclanthology.org/2024.emnlp-main.252.pdf"
          }
        ]
      },
      "I found several research papers related to reinforcement learning, reward design, and auxiliary tasks from 2023-2024. Here are the key findings:\n\n## Key Research Areas\n\n**Auxiliary Tasks and Reward Structures:**\nAuxiliary losses help with generalization and serve as entry points for human-like inductive biases, with metrics inspired by the geometry of latent decompositions helping to learn optimal values in multi-task settings.\n\n**Reward Model Degradation:**\nResearch reveals a critical vulnerability where a small amount of noise in reward signals can severely degrade agent performance, with agents using auxiliary reward models without proper noise handling performing worse than exploration-driven methods in sparse reward environments.\n\n**Specific Challenges with Auxiliary Rewards:**\nFalse positive rewards—where the reward model incorrectly assigns rewards to trajectories that don't fulfill given instructions—are more detrimental to learning than false negatives, with cosine similarity metrics being prone to generating such false positive reward signals.\n\n**Multi-task and Structure in RL:**\nIncorporating structure improves the sample efficiency of constrained optimization methods while making them more interpretable, which is particularly relevant to multi-task and auxiliary task scenarios.\n\nThe search results indicate that recent 2023-2024 research focuses on understanding how auxiliary tasks and reward signals can inadvertently degrade performance through noise and misalignment, and how structural approaches can mitigate these issues."
    ],
    "durationSeconds": 6.869179216
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T02:04:27.530Z_

<details><summary>↩ Tool result · `toolu_01CU5226fgnmu6BShw8PFBbK`</summary>

```text
Web search results for query: "reward shaping negative side effects reinforcement learning penalty auxiliary objective"

Links: [{"title":"Comprehensive Overview of Reward Engineering and Shaping in Advancing Reinforcement Learning Applications","url":"https://arxiv.org/html/2408.10215v1"},{"title":"Reward shaping — Mastering Reinforcement Learning","url":"https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html"},{"title":"Reward Function in Reinforcement Learning | by Amit Yadav | Biased-Algorithms | Medium","url":"https://medium.com/biased-algorithms/reward-function-in-reinforcement-learning-c9ee04cabe7d"},{"title":"Penalty-Based Reward Shaping in RL","url":"https://www.emergentmind.com/topics/penalty-based-reward-shaping"},{"title":"Reward Shaping for Faster Learning in Reinforcement ...","url":"https://codesignal.com/learn/courses/advanced-rl-techniques-optimization-and-beyond/lessons/reward-shaping-for-faster-learning-in-reinforcement-learning"},{"title":"AI Safety 101 : Reward Misspecification","url":"https://www.lesswrong.com/posts/mMBoPnFrFqQJKzDsZ/ai-safety-101-reward-misspecification"},{"title":"What is reward shaping in reinforcement learning?","url":"https://milvus.io/ai-quick-reference/what-is-reward-shaping-in-reinforcement-learning"},{"title":"Behavior Alignment via Reward Function Optimization Dhawal Gupta∗","url":"https://people.cs.umass.edu/~pthomas/papers/Gupta2023.pdf"},{"title":"Real-World DRL: 5 Essential Reward Functions for Modeling Objectives and Constraints | by Zhong Hong | Medium","url":"https://medium.com/@zhonghong9998/real-world-drl-5-essential-reward-functions-for-modeling-objectives-and-constraints-e742325d4747"},{"title":"Reinforcement Learning Reward And Punishment | Restackio","url":"https://www.restack.io/p/reinforcement-learning-answer-reward-punishment-cat-ai"}]

Based on the search results, here's an overview of reward shaping, negative side effects, penalty-based approaches, and auxiliary objectives in reinforcement learning:

## Reward Shaping Overview

Techniques such as potential-based shaping functions can be used to provide additional guidance to the agent, accelerating the learning process by giving intermediate rewards for progress toward the ultimate goal.

## Negative Side Effects and Challenges

A key challenge with reward shaping is reward hacking. Effective reward design requires a deep understanding of the problem domain, the agent's learning dynamics, and potential pitfalls such as reward hacking, where the agent finds unintended shortcuts to maximize rewards without achieving the desired behavior.

Poorly designed shaping can lead to unintended behaviors, such as the agent exploiting the shaped rewards instead of solving the actual task. For instance, if a robot is rewarded for lifting its leg, it might repeatedly lift the leg without walking.

Additionally, if your shaped rewards don't align perfectly with your true objective, agents may find ways to maximize the shaped rewards without achieving the intended goal. For example, if you reward getting closer to the goal without a step penalty, an agent might learn to oscillate back and forth near the goal rather than reaching it.

## Penalty-Based Reward Shaping

Penalty-based reward shaping is a family of techniques in reinforcement learning wherein the reward function is augmented with explicit penalty terms to discourage undesirable behaviors, enforce safety, or guide the agent toward preferred solutions. These penalties—which may be constant, adaptive, or learned—are integrated into the reward landscape, modulating the optimization objective without modifying the underlying environment dynamics.

## Auxiliary Objectives and Behavior Alignment

A novel bi-level objective can be used to analyze and automatically fine-tune designer-created auxiliary reward functions. It ensures they remain aligned with the original reward and do not induce behaviors different from those originally intended by the designer.

The challenge of enabling reinforcement learning practitioners to incorporate domain knowledge through heuristic auxiliary reward functions involves ensuring that such auxiliary rewards not only induce behaviors that align with the designer's intentions but also allow for faster learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "63cd1810-f6d8-4095-a0ee-9eeff3b10b93",
  "tool_use_result": {
    "query": "reward shaping negative side effects reinforcement learning penalty auxiliary objective",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Xz6Qxsoxn9c9LPnYXfu91d",
        "content": [
          {
            "title": "Comprehensive Overview of Reward Engineering and Shaping in Advancing Reinforcement Learning Applications",
            "url": "https://arxiv.org/html/2408.10215v1"
          },
          {
            "title": "Reward shaping — Mastering Reinforcement Learning",
            "url": "https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html"
          },
          {
            "title": "Reward Function in Reinforcement Learning | by Amit Yadav | Biased-Algorithms | Medium",
            "url": "https://medium.com/biased-algorithms/reward-function-in-reinforcement-learning-c9ee04cabe7d"
          },
          {
            "title": "Penalty-Based Reward Shaping in RL",
            "url": "https://www.emergentmind.com/topics/penalty-based-reward-shaping"
          },
          {
            "title": "Reward Shaping for Faster Learning in Reinforcement ...",
            "url": "https://codesignal.com/learn/courses/advanced-rl-techniques-optimization-and-beyond/lessons/reward-shaping-for-faster-learning-in-reinforcement-learning"
          },
          {
            "title": "AI Safety 101 : Reward Misspecification",
            "url": "https://www.lesswrong.com/posts/mMBoPnFrFqQJKzDsZ/ai-safety-101-reward-misspecification"
          },
          {
            "title": "What is reward shaping in reinforcement learning?",
            "url": "https://milvus.io/ai-quick-reference/what-is-reward-shaping-in-reinforcement-learning"
          },
          {
            "title": "Behavior Alignment via Reward Function Optimization Dhawal Gupta∗",
            "url": "https://people.cs.umass.edu/~pthomas/papers/Gupta2023.pdf"
          },
          {
            "title": "Real-World DRL: 5 Essential Reward Functions for Modeling Objectives and Constraints | by Zhong Hong | Medium",
            "url": "https://medium.com/@zhonghong9998/real-world-drl-5-essential-reward-functions-for-modeling-objectives-and-constraints-e742325d4747"
          },
          {
            "title": "Reinforcement Learning Reward And Punishment | Restackio",
            "url": "https://www.restack.io/p/reinforcement-learning-answer-reward-punishment-cat-ai"
          }
        ]
      },
      "Based on the search results, here's an overview of reward shaping, negative side effects, penalty-based approaches, and auxiliary objectives in reinforcement learning:\n\n## Reward Shaping Overview\n\nTechniques such as potential-based shaping functions can be used to provide additional guidance to the agent, accelerating the learning process by giving intermediate rewards for progress toward the ultimate goal.\n\n## Negative Side Effects and Challenges\n\nA key challenge with reward shaping is reward hacking. Effective reward design requires a deep understanding of the problem domain, the agent's learning dynamics, and potential pitfalls such as reward hacking, where the agent finds unintended shortcuts to maximize rewards without achieving the desired behavior.\n\nPoorly designed shaping can lead to unintended behaviors, such as the agent exploiting the shaped rewards instead of solving the actual task. For instance, if a robot is rewarded for lifting its leg, it might repeatedly lift the leg without walking.\n\nAdditionally, if your shaped rewards don't align perfectly with your true objective, agents may find ways to maximize the shaped rewards without achieving the intended goal. For example, if you reward getting closer to the goal without a step penalty, an agent might learn to oscillate back and forth near the goal rather than reaching it.\n\n## Penalty-Based Reward Shaping\n\nPenalty-based reward shaping is a family of techniques in reinforcement learning wherein the reward function is augmented with explicit penalty terms to discourage undesirable behaviors, enforce safety, or guide the agent toward preferred solutions. These penalties—which may be constant, adaptive, or learned—are integrated into the reward landscape, modulating the optimization objective without modifying the underlying environment dynamics.\n\n## Auxiliary Objectives and Behavior Alignment\n\nA novel bi-level objective can be used to analyze and automatically fine-tune designer-created auxiliary reward functions. It ensures they remain aligned with the original reward and do not induce behaviors different from those originally intended by the designer.\n\nThe challenge of enabling reinforcement learning practitioners to incorporate domain knowledge through heuristic auxiliary reward functions involves ensuring that such auxiliary rewards not only induce behaviors that align with the designer's intentions but also allow for faster learning."
    ],
    "durationSeconds": 8.701540219999998
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T02:04:29.514Z_

<details><summary>↩ Tool result · `toolu_01A6T3QzNPC7tUKfiXTQWHT5`</summary>

```text
Web search results for query: ""multi-objective RLHF" "reward conflict" OR "auxiliary reward" OR "reward tradeoff" language model 2024 2025"

Links: [{"title":"Confronting Reward Model Overoptimization with Constrained RLHF | OpenReview","url":"https://openreview.net/forum?id=gkfUvn0fLU"},{"title":"Interpretable Preferences via Multi-Objective Reward Modeling and Mixture-of-Experts | RLHFlow","url":"https://rlhflow.github.io/posts/2024-05-29-multi-objective-reward-modeling/"},{"title":"GitHub - RLHFlow/RLHF-Reward-Modeling: Recipes to train reward model for RLHF. · GitHub","url":"https://github.com/RLHFlow/RLHF-Reward-Modeling"},{"title":"Interpretable Preferences via Multi-Objective Reward ...","url":"https://aclanthology.org/2024.findings-emnlp.620.pdf"},{"title":"[2310.04373] Confronting Reward Model Overoptimization with Constrained RLHF","url":"https://arxiv.org/abs/2310.04373"},{"title":"Optimizing Language Models with Fair and Stable Reward ...","url":"https://aclanthology.org/2024.emnlp-main.565.pdf"},{"title":"Reward Model Overoptimisation in Iterated RLHF | OpenReview","url":"https://openreview.net/forum?id=efoe5VJfKz"},{"title":"Towards Reward Fairness in RLHF: From a Resource ...","url":"https://aclanthology.org/2025.acl-long.163.pdf"},{"title":"Over-Optimization | RLHF Book by Nathan Lambert","url":"https://rlhfbook.com/c/14-over-optimization"},{"title":"A Comprehensive Survey of Reward Models: Taxonomy, Applications, Challenges, and Future","url":"https://arxiv.org/html/2504.12328v1"}]

Based on my search results, I've found several relevant papers and resources on multi-objective RLHF addressing reward conflict and tradeoffs in language model alignment. Here's what I discovered:

## Key Research Areas

**Multi-Objective Reward Modeling:**

The RLHF process typically starts by training a reward model using human preference data, with conventional RMs trained on pairwise responses to the same user request. However, human preferences are multi-faceted, and it is increasingly common to derive reward from a composition of simpler reward models which each capture a different aspect of language quality, presenting a challenge as it is difficult to appropriately weight these component RMs when combining them.

**Reward Conflict and Overoptimization:**

Because any RM is only a proxy for human evaluation, this process is vulnerable to overoptimization, wherein past a certain point, accumulating higher reward is associated with worse human ratings. The first study on overoptimization in composite RMs shows that correlation between component RMs has a significant effect on the locations of these overoptimization points.

In some scenarios, rewards may conflict, which necessitates careful handling in multi-objective optimization.

**Recent Approaches (2024-2025):**

As of January 2025, Decision-tree reward model training code has been released, with Decision-Tree-Reward-Gemma-2-27B achieving state-of-the-art scores on RewardBench.

In the verification scenario, fairness aims to make the distribution of different types of rewards more consistent, while utility ensures that for any given prompt, the reward for a good response exceeds that for a bad response. These objectives are inherently independent and non-conflicting, though balancing them necessitates a multi-objective optimization.

The research community has made significant progress in understanding and addressing reward conflicts in RLHF through constrained optimization, fair reward composition methods, and interpretable multi-objective approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "a226493a-b63f-4347-8627-2686d4cc561a",
  "tool_use_result": {
    "query": "\"multi-objective RLHF\" \"reward conflict\" OR \"auxiliary reward\" OR \"reward tradeoff\" language model 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01T33orfiMnqiGXp64rrW1xK",
        "content": [
          {
            "title": "Confronting Reward Model Overoptimization with Constrained RLHF | OpenReview",
            "url": "https://openreview.net/forum?id=gkfUvn0fLU"
          },
          {
            "title": "Interpretable Preferences via Multi-Objective Reward Modeling and Mixture-of-Experts | RLHFlow",
            "url": "https://rlhflow.github.io/posts/2024-05-29-multi-objective-reward-modeling/"
          },
          {
            "title": "GitHub - RLHFlow/RLHF-Reward-Modeling: Recipes to train reward model for RLHF. · GitHub",
            "url": "https://github.com/RLHFlow/RLHF-Reward-Modeling"
          },
          {
            "title": "Interpretable Preferences via Multi-Objective Reward ...",
            "url": "https://aclanthology.org/2024.findings-emnlp.620.pdf"
          },
          {
            "title": "[2310.04373] Confronting Reward Model Overoptimization with Constrained RLHF",
            "url": "https://arxiv.org/abs/2310.04373"
          },
          {
            "title": "Optimizing Language Models with Fair and Stable Reward ...",
            "url": "https://aclanthology.org/2024.emnlp-main.565.pdf"
          },
          {
            "title": "Reward Model Overoptimisation in Iterated RLHF | OpenReview",
            "url": "https://openreview.net/forum?id=efoe5VJfKz"
          },
          {
            "title": "Towards Reward Fairness in RLHF: From a Resource ...",
            "url": "https://aclanthology.org/2025.acl-long.163.pdf"
          },
          {
            "title": "Over-Optimization | RLHF Book by Nathan Lambert",
            "url": "https://rlhfbook.com/c/14-over-optimization"
          },
          {
            "title": "A Comprehensive Survey of Reward Models: Taxonomy, Applications, Challenges, and Future",
            "url": "https://arxiv.org/html/2504.12328v1"
          }
        ]
      },
      "Based on my search results, I've found several relevant papers and resources on multi-objective RLHF addressing reward conflict and tradeoffs in language model alignment. Here's what I discovered:\n\n## Key Research Areas\n\n**Multi-Objective Reward Modeling:**\n\nThe RLHF process typically starts by training a reward model using human preference data, with conventional RMs trained on pairwise responses to the same user request. However, human preferences are multi-faceted, and it is increasingly common to derive reward from a composition of simpler reward models which each capture a different aspect of language quality, presenting a challenge as it is difficult to appropriately weight these component RMs when combining them.\n\n**Reward Conflict and Overoptimization:**\n\nBecause any RM is only a proxy for human evaluation, this process is vulnerable to overoptimization, wherein past a certain point, accumulating higher reward is associated with worse human ratings. The first study on overoptimization in composite RMs shows that correlation between component RMs has a significant effect on the locations of these overoptimization points.\n\nIn some scenarios, rewards may conflict, which necessitates careful handling in multi-objective optimization.\n\n**Recent Approaches (2024-2025):**\n\nAs of January 2025, Decision-tree reward model training code has been released, with Decision-Tree-Reward-Gemma-2-27B achieving state-of-the-art scores on RewardBench.\n\nIn the verification scenario, fairness aims to make the distribution of different types of rewards more consistent, while utility ensures that for any given prompt, the reward for a good response exceeds that for a bad response. These objectives are inherently independent and non-conflicting, though balancing them necessitates a multi-objective optimization.\n\nThe research community has made significant progress in understanding and addressing reward conflicts in RLHF through constrained optimization, fair reward composition methods, and interpretable multi-objective approaches."
    ],
    "durationSeconds": 8.752592650999999
  }
}
```

</details>

---

### Assistant

_source line 21_

<details><summary>Logged reasoning block</summary>

```text
Let me now fetch more details on the most promising papers. The key ones I want to investigate further:

1. "Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training" (arxiv 2509.03403) - directly about process vs outcome reward conflict
2. "Confronting Reward Model Overoptimization with Constrained RLHF" (arxiv 2310.04373) - about reward overoptimization with composite rewards
3. "GRPO IS SECRETLY A PROCESS REWARD MODEL" - very relevant since we use GRPO


4. "Behavior Alignment via Reward Function Optimization" - about auxiliary reward alignment
5. "Reward Shaping to Mitigate Reward Hacking in RLHF" (2502.18770) - already in lit map
6. The dynamic reward weighting paper (arxiv 2509.11452)
7. "Penalty-Based Reward Shaping in RL" from emergentmind

I should also dig into auxiliary loss degradation in multi-task RL and the specific phenomenon where adding rewards actually hurts primary performance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "a789ba8d-eab7-4394-a26c-cfe7564be277",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WV1uHcFK8YZ2BTwMsExrh7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9228,
      "cache_read_input_tokens": 25292,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9228
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

### Assistant

_source line 22_

Found several promising leads. Let me fetch details on the most relevant papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "21cb7c71-40fa-417b-8fc7-2262917f0f08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WV1uHcFK8YZ2BTwMsExrh7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9228,
      "cache_read_input_tokens": 25292,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9228
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

_source line 23_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TcwCm7i86UQdNpuSzX57v1`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.03403",
  "prompt": "Extract: title, all authors, year, venue/conference, abstract. Focus on whether they report that process rewards can hurt outcome performance, and what solutions they propose."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "11806f74-2079-41ae-842f-42f8527b7077",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WV1uHcFK8YZ2BTwMsExrh7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9228,
      "cache_read_input_tokens": 25292,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9228
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

_source line 24_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RZz2eCBuSz67CM6LJbaMKe`</summary>

```json
{
  "url": "https://arxiv.org/abs/2310.04373",
  "prompt": "Extract: title, all authors, year, venue/conference, abstract. Focus on findings about composite reward model overoptimization - does adding auxiliary/component rewards degrade primary performance? What solutions do they propose?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "273243a4-92b9-459f-8f4a-51edc1fefb03",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WV1uHcFK8YZ2BTwMsExrh7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9228,
      "cache_read_input_tokens": 25292,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9228
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

_source line 25_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01G5XgzRuzw13bA61sNptCW4`</summary>

```json
{
  "url": "https://openreview.net/pdf/1f109913a199dad205fa51f554aaa5e2a5a782d5.pdf",
  "prompt": "Extract: title, all authors, year, venue. What is the main finding about GRPO and process reward models? Does this paper discuss any conflict or tradeoff between process and outcome rewards?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "f4cca814-d3ea-4cea-a2ec-7c4d37ebb6cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WV1uHcFK8YZ2BTwMsExrh7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9228,
      "cache_read_input_tokens": 25292,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9228
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

_source line 26 · 2026-05-14T02:04:48.142Z_

<details><summary>↩ Tool result · `toolu_01TcwCm7i86UQdNpuSzX57v1`</summary>

```text
# Research Paper Summary

**Title:** Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training

**Authors:** Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal

**Year:** 2025

**Venue:** arXiv (Computer Science > Machine Learning)

## Key Findings on Process Rewards

The paper identifies a critical tension: while Process Reward Models (PRMs) provide "fine-grained guidance for intermediate steps, they frequently suffer from inaccuracies and are susceptible to reward hacking." Meanwhile, Outcome Reward Models (ORMs) lack sufficient granularity to evaluate reasoning quality accurately.

## Proposed Solution

Rather than directly combining PRM and ORM signals, the authors introduce **PROF (PRocess cOnsistency Filter)**, a data curation method that selectively uses process rewards. The approach "retains correct responses with higher averaged process values and incorrect responses with lower averaged process values, while maintaining positive/negative training sample balance."

**Results:** This filtering strategy achieved "over 4% improvement in final accuracy compared to the blending approaches" while also enhancing intermediate reasoning quality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "a9df5cc3-5f44-487a-9724-9b5fe8fd8d4e",
  "tool_use_result": {
    "bytes": 48748,
    "code": 200,
    "codeText": "OK",
    "result": "# Research Paper Summary\n\n**Title:** Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training\n\n**Authors:** Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal\n\n**Year:** 2025\n\n**Venue:** arXiv (Computer Science > Machine Learning)\n\n## Key Findings on Process Rewards\n\nThe paper identifies a critical tension: while Process Reward Models (PRMs) provide \"fine-grained guidance for intermediate steps, they frequently suffer from inaccuracies and are susceptible to reward hacking.\" Meanwhile, Outcome Reward Models (ORMs) lack sufficient granularity to evaluate reasoning quality accurately.\n\n## Proposed Solution\n\nRather than directly combining PRM and ORM signals, the authors introduce **PROF (PRocess cOnsistency Filter)**, a data curation method that selectively uses process rewards. The approach \"retains correct responses with higher averaged process values and incorrect responses with lower averaged process values, while maintaining positive/negative training sample balance.\"\n\n**Results:** This filtering strategy achieved \"over 4% improvement in final accuracy compared to the blending approaches\" while also enhancing intermediate reasoning quality.",
    "durationMs": 5311,
    "url": "https://arxiv.org/abs/2509.03403"
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VGWsh2tc1mvJ3Ta5ozrveW`</summary>

```json
{
  "query": "\"auxiliary loss\" OR \"auxiliary reward\" \"hurts\" OR \"degrades\" OR \"reduces\" primary task performance reinforcement learning LLM 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "f44c06da-e918-4162-aa59-23b4d426decb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WV1uHcFK8YZ2BTwMsExrh7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9228,
      "cache_read_input_tokens": 25292,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9228
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

_source line 28_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VgqSDMpfv8MPtUY87mAct7`</summary>

```json
{
  "query": "Mudgal Agarwal \"reward bonus\" OR \"bonus reward\" degradation RLHF primary objective 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "3f760235-238f-4e2d-ab28-037b20847bb1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WV1uHcFK8YZ2BTwMsExrh7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9228,
      "cache_read_input_tokens": 25292,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9228
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

_source line 29 · 2026-05-14T02:04:50.100Z_

<details><summary>↩ Tool result · `toolu_01RZz2eCBuSz67CM6LJbaMKe`</summary>

```text
# Research Summary: Reward Model Overoptimization

**Title:** Confronting Reward Model Overoptimization with Constrained RLHF

**Authors:** Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer

**Year:** 2023

**Venue:** arXiv (cs.LG/cs.AI)

## Key Findings on Composite Reward Models

The paper conducts "the first study on overoptimization in composite RMs" and demonstrates that correlation between component reward models significantly influences where performance degradation occurs.

**Main Problem:** When combining multiple reward models representing different quality aspects, the system becomes vulnerable to overoptimization—where "accumulating higher reward is associated with worse human ratings" beyond certain thresholds.

## Proposed Solutions

1. **Constrained Reinforcement Learning:** The authors apply constrained RL to prevent agents from exceeding each component model's "threshold of usefulness," keeping all models within effective operating ranges.

2. **Dynamic Weighting via Lagrange Multipliers:** Rather than static weighting, their approach learns dynamic weights naturally expressed through Lagrange multipliers, addressing the compositional weighting challenge.

3. **Adaptive Gradient-Free Optimization:** An additional method identifies optimal performance points during training using gradient-free techniques, enabling single-run identification and optimization.

The research suggests these constraints improve evaluation performance by maintaining component models within their reliable ranges.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "6c51c5b9-41f2-4ac4-b39a-b7feef925d59",
  "tool_use_result": {
    "bytes": 47949,
    "code": 200,
    "codeText": "OK",
    "result": "# Research Summary: Reward Model Overoptimization\n\n**Title:** Confronting Reward Model Overoptimization with Constrained RLHF\n\n**Authors:** Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer\n\n**Year:** 2023\n\n**Venue:** arXiv (cs.LG/cs.AI)\n\n## Key Findings on Composite Reward Models\n\nThe paper conducts \"the first study on overoptimization in composite RMs\" and demonstrates that correlation between component reward models significantly influences where performance degradation occurs.\n\n**Main Problem:** When combining multiple reward models representing different quality aspects, the system becomes vulnerable to overoptimization—where \"accumulating higher reward is associated with worse human ratings\" beyond certain thresholds.\n\n## Proposed Solutions\n\n1. **Constrained Reinforcement Learning:** The authors apply constrained RL to prevent agents from exceeding each component model's \"threshold of usefulness,\" keeping all models within effective operating ranges.\n\n2. **Dynamic Weighting via Lagrange Multipliers:** Rather than static weighting, their approach learns dynamic weights naturally expressed through Lagrange multipliers, addressing the compositional weighting challenge.\n\n3. **Adaptive Gradient-Free Optimization:** An additional method identifies optimal performance points during training using gradient-free techniques, enabling single-run identification and optimization.\n\nThe research suggests these constraints improve evaluation performance by maintaining component models within their reliable ranges.",
    "durationMs": 5285,
    "url": "https://arxiv.org/abs/2310.04373"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T02:04:52.462Z_

<details><summary>↩ Tool result · `toolu_01G5XgzRuzw13bA61sNptCW4`</summary>

```text
I appreciate your request, but I need to inform you that the content provided appears to be a raw PDF file with compressed/encoded streams rather than readable text. The document contains binary PDF objects (streams with /FlateDecode filters) that cannot be meaningfully extracted without proper PDF parsing.

From the visible metadata in the PDF structure, I can see this is a multi-page document with annotations and embedded fonts, but I cannot reliably extract:
- The title
- Author names
- Publication year
- Venue information
- Content about GRPO and process reward models
- Information about conflicts between process and outcome rewards

**To help you effectively, I would need:**
1. The actual text content of the paper (not the raw PDF binary)
2. A properly formatted text version
3. Or access to the paper through a PDF viewer that can extract text

If you can provide the paper's text content or a clearer version, I'll be happy to extract the specific information you're requesting while following your guidelines about quote length and attribution.

[Binary content (application/pdf, 890.6KB) also saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/6c8ab3fa-f3c3-483d-b115-dccc1097e77a/tool-results/webfetch-1778724288088-yoo47l.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "3c2d968b-9fea-4af9-bef2-9aa4a8edcd97",
  "tool_use_result": {
    "bytes": 911958,
    "code": 200,
    "codeText": "OK",
    "result": "I appreciate your request, but I need to inform you that the content provided appears to be a raw PDF file with compressed/encoded streams rather than readable text. The document contains binary PDF objects (streams with /FlateDecode filters) that cannot be meaningfully extracted without proper PDF parsing.\n\nFrom the visible metadata in the PDF structure, I can see this is a multi-page document with annotations and embedded fonts, but I cannot reliably extract:\n- The title\n- Author names\n- Publication year\n- Venue information\n- Content about GRPO and process reward models\n- Information about conflicts between process and outcome rewards\n\n**To help you effectively, I would need:**\n1. The actual text content of the paper (not the raw PDF binary)\n2. A properly formatted text version\n3. Or access to the paper through a PDF viewer that can extract text\n\nIf you can provide the paper's text content or a clearer version, I'll be happy to extract the specific information you're requesting while following your guidelines about quote length and attribution.\n\n[Binary content (application/pdf, 890.6KB) also saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/6c8ab3fa-f3c3-483d-b115-dccc1097e77a/tool-results/webfetch-1778724288088-yoo47l.pdf]",
    "durationMs": 5147,
    "url": "https://openreview.net/pdf/1f109913a199dad205fa51f554aaa5e2a5a782d5.pdf"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T02:04:54.330Z_

<details><summary>↩ Tool result · `toolu_01VgqSDMpfv8MPtUY87mAct7`</summary>

```text
Web search results for query: "Mudgal Agarwal "reward bonus" OR "bonus reward" degradation RLHF primary objective 2024"

Links: [{"title":"Interpretable Preferences via Multi-Objective Reward ...","url":"https://aclanthology.org/2024.findings-emnlp.620.pdf"},{"title":"Over-Optimization | RLHF Book by Nathan Lambert","url":"https://rlhfbook.com/c/14-over-optimization"},{"title":"Investigating Reward Hacking When Using Vision-Language ...","url":"https://cs224r.stanford.edu/projects/pdfs/CS_224R_Final_Project.pdf"},{"title":"Reward Over-Optimization in AI","url":"https://www.emergentmind.com/topics/reward-over-optimization"},{"title":"Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/e45caa3d5273d105b8d045e748636957-Paper-Conference.pdf"},{"title":"Adaptive Length Bias Mitigation in Reward Models for RLHF","url":"https://aclanthology.org/2025.findings-naacl.169.pdf"},{"title":"GitHub - RLHFlow/RLHF-Reward-Modeling: Recipes to train reward model for RLHF. · GitHub","url":"https://github.com/RLHFlow/RLHF-Reward-Modeling"},{"title":"Interpretable Preferences via Multi-Objective Reward Modeling and Mixture-of-Experts | RLHFlow","url":"https://rlhflow.github.io/posts/2024-05-29-multi-objective-reward-modeling/"},{"title":"Enhancing RLHF with Weighted Preference Optimization","url":"https://aclanthology.org/2024.emnlp-main.475.pdf"},{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"}]

Based on my search results, I wasn't able to find a research paper or work specifically by "Mudgal Agarwal" with the exact terms "reward bonus" OR "bonus reward" and "degradation RLHF primary objective" from 2024.

The search returned relevant papers about RLHF (Reinforcement Learning from Human Feedback), reward model degradation, and related topics from 2024, but none appear to be authored by someone with the name Mudgal Agarwal. The results do include references to various RLHF degradation phenomena and reward over-optimization studies from 2024.

It's possible that:
1. The author's name may be spelled differently
2. The paper may use different terminology than what I searched for
3. The paper may not yet be indexed by standard academic search engines
4. There may be a slight variation in the publication details

If you could provide additional context—such as the full paper title, conference/venue, or alternative spellings of the author's name—I'd be happy to search again with more specific information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "4e22f718-fa71-417c-ae1e-11a2a5156b3f",
  "tool_use_result": {
    "query": "Mudgal Agarwal \"reward bonus\" OR \"bonus reward\" degradation RLHF primary objective 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XHNbqGAicwk4LUM4XXdejQ",
        "content": [
          {
            "title": "Interpretable Preferences via Multi-Objective Reward ...",
            "url": "https://aclanthology.org/2024.findings-emnlp.620.pdf"
          },
          {
            "title": "Over-Optimization | RLHF Book by Nathan Lambert",
            "url": "https://rlhfbook.com/c/14-over-optimization"
          },
          {
            "title": "Investigating Reward Hacking When Using Vision-Language ...",
            "url": "https://cs224r.stanford.edu/projects/pdfs/CS_224R_Final_Project.pdf"
          },
          {
            "title": "Reward Over-Optimization in AI",
            "url": "https://www.emergentmind.com/topics/reward-over-optimization"
          },
          {
            "title": "Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/e45caa3d5273d105b8d045e748636957-Paper-Conference.pdf"
          },
          {
            "title": "Adaptive Length Bias Mitigation in Reward Models for RLHF",
            "url": "https://aclanthology.org/2025.findings-naacl.169.pdf"
          },
          {
            "title": "GitHub - RLHFlow/RLHF-Reward-Modeling: Recipes to train reward model for RLHF. · GitHub",
            "url": "https://github.com/RLHFlow/RLHF-Reward-Modeling"
          },
          {
            "title": "Interpretable Preferences via Multi-Objective Reward Modeling and Mixture-of-Experts | RLHFlow",
            "url": "https://rlhflow.github.io/posts/2024-05-29-multi-objective-reward-modeling/"
          },
          {
            "title": "Enhancing RLHF with Weighted Preference Optimization",
            "url": "https://aclanthology.org/2024.emnlp-main.475.pdf"
          },
          {
            "title": "Reward Hacking in Reinforcement Learning | Lil'Log",
            "url": "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"
          }
        ]
      },
      "Based on my search results, I wasn't able to find a research paper or work specifically by \"Mudgal Agarwal\" with the exact terms \"reward bonus\" OR \"bonus reward\" and \"degradation RLHF primary objective\" from 2024.\n\nThe search returned relevant papers about RLHF (Reinforcement Learning from Human Feedback), reward model degradation, and related topics from 2024, but none appear to be authored by someone with the name Mudgal Agarwal. The results do include references to various RLHF degradation phenomena and reward over-optimization studies from 2024.\n\nIt's possible that:\n1. The author's name may be spelled differently\n2. The paper may use different terminology than what I searched for\n3. The paper may not yet be indexed by standard academic search engines\n4. There may be a slight variation in the publication details\n\nIf you could provide additional context—such as the full paper title, conference/venue, or alternative spellings of the author's name—I'd be happy to search again with more specific information."
    ],
    "durationSeconds": 4.7585704220000045
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T02:05:10.801Z_

<details><summary>↩ Tool result · `toolu_01VGWsh2tc1mvJ3Ta5ozrveW`</summary>

```text
Web search results for query: ""auxiliary loss" OR "auxiliary reward" "hurts" OR "degrades" OR "reduces" primary task performance reinforcement learning LLM 2024 2025"

Links: [{"title":"On Auxiliary Tasks in Deep Reinforcement Learning | Yunfan’s Blog","url":"https://yunfanj.com/blog/2021/03/14/AuxTasks.html"},{"title":"Learning through Auxiliary Tasks | Unsupervised Thoughts","url":"https://vivien000.github.io/blog/journal/learning-though-auxiliary_tasks.html"},{"title":"What is Auxiliary Tasks? | Activeloop Glossary","url":"https://www.activeloop.ai/resources/glossary/auxiliary-tasks/"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation","url":"https://arxiv.org/html/2602.09305v1"},{"title":"A framework for mitigating malicious RLHF feedback in LLM training using consensus based reward | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-92889-7"},{"title":"LLM Reinforcement Learning | IBM","url":"https://www.ibm.com/think/topics/llm-reinforcement-learning"},{"title":"Tutorial #4: auxiliary tasks in deep reinforcement learning - Research Blog | RBC Borealis","url":"https://rbcborealis.com/research-blogs/tutorial-4-auxiliary-tasks-deep-reinforcement-learning/"},{"title":"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? | OpenReview","url":"https://openreview.net/forum?id=4OsgYD7em5"},{"title":"Pushing RL Boundaries: Integrating Foundational Models, e.g. LLMs and VLMs, into Reinforcement Learning | by Elahe Aghapour | TDS Archive | Medium","url":"https://medium.com/data-science/pushing-boundaries-integrating-foundational-models-e-g-556cfb6d0632"},{"title":"Efficient Reinforcement Learning with Large Language Model Priors","url":"https://arxiv.org/html/2410.07927v1"}]

I found some relevant results, but let me search more specifically for recent research on negative effects of auxiliary losses/rewards on LLMs and reinforcement learning in 2024-2025:

Links: [{"title":"RecSys 2024 — Session 6: Multi-task Learning - RecSys","url":"https://recsys.acm.org/recsys24/session-6/"},{"title":"Adaptive Task Weighting in Multi-Task Learning","url":"https://www.emergentmind.com/topics/adaptive-task-weighting-in-multi-task-learning"},{"title":"Multi-Task Learning in Natural Language Processing: An Overview | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3663363"},{"title":"Multi-Task Learning in Natural Language Processing: An Overview","url":"https://arxiv.org/html/2109.09138v2"},{"title":"Multitask Learning 1997–2024: Part I Fundamentals · Issue 7.3, Summer 2025","url":"https://hdsr.mitpress.mit.edu/pub/7fcc3jhv/release/2"},{"title":"Is multitask learning all you need in continual learning? | OpenReview","url":"https://openreview.net/forum?id=Pin2kdWloe"},{"title":"Advances and challenges of multi-task learning method in recommender systems: A survey - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0925231225031820"},{"title":"GitHub - dingwoai/Multi-Task-Learning: A list of papers, codes and applications on multi-task learning. · GitHub","url":"https://github.com/dingwoai/Multi-Task-Learning"},{"title":"(PDF) Multi-Task Learning 1997–2024: Part II Regularization and Optimization","url":"https://www.researchgate.net/publication/394183446_Multi-Task_Learning_1997-2024_Part_II_Regularization_and_Optimization"},{"title":"GitHub - junfish/Awesome-Multitask-Learning: This repository periodicly updates the MTL paper and resources · GitHub","url":"https://github.com/junfish/Awesome-Multitask-Learning"}]

Let me search more specifically for recent papers on auxiliary rewards hurting LLM reasoning or RL performance:

Links: [{"title":"Auxiliary-Loss-Free Load Balancing Strategy for Mixture-of-Experts | OpenReview","url":"https://openreview.net/forum?id=y1iU5czYpE"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf?id=vIIflOgwZX"},{"title":"Mixture-of-Experts (MoE) LLMs - by Cameron R. Wolfe, Ph.D.","url":"https://cameronrwolfe.substack.com/p/moe-llms"},{"title":"[Quick Review] Coupling Experts and Routers in Mixture-of-Experts via an Auxiliary Loss","url":"https://liner.com/review/coupling-experts-and-routers-in-mixtureofexperts-via-auxiliary-loss"},{"title":"Understanding Mixture of Experts (MoE) Neural Networks | IntuitionLabs","url":"https://intuitionlabs.ai/articles/mixture-of-experts-moe-models"},{"title":"Published as a conference paper at ICLR 2026 CAPACITY-AWARE INFERENCE:","url":"https://openreview.net/pdf?id=LuYFpySWA2"}]

Excellent! I found some very relevant results. Let me search for more specific information about negative effects of auxiliary rewards on LLM reasoning tasks:

Links: [{"title":"Resolving Token-Space Gradient Conflicts: Token Space Manipulation for","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Jeong_Resolving_Token-Space_Gradient_Conflicts_Token_Space_Manipulation_for_Transformer-Based_Multi-Task_ICCV_2025_paper.pdf"},{"title":"DaGRPO: Rectifying Gradient Conflict in Reasoning via ...","url":"https://arxiv.org/pdf/2512.06337"},{"title":"ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning","url":"https://ise.thss.tsinghua.edu.cn/~mlong/doc/ForkMerge-nips23.pdf"},{"title":"Conflict-Averse Gradient Descent for Multi-task learning | OpenReview","url":"https://openreview.net/forum?id=_61Qh8tULj_"},{"title":"[2303.05847] Gradient Coordination for Quantifying and Maximizing Knowledge Transference in Multi-Task Learning","url":"https://arxiv.org/abs/2303.05847"},{"title":"[2110.14048] Conflict-Averse Gradient Descent for Multi-task Learning","url":"https://arxiv.org/abs/2110.14048"},{"title":"Conflict-Averse Gradient Descent for Multi-task Learning","url":"https://arxiv.org/html/2110.14048v2"},{"title":"Towards Task-Conﬂicts Momentum-Calibrated Approach for Multi-task Learning","url":"https://www.hufudb.com/static/paper/2024/ICDE24-chai.pdf"},{"title":"Gradient Similarity Surgery in Multi-Task Deep Learning","url":"https://ecmlpkdd-storage.s3.eu-central-1.amazonaws.com/preprints/2025/research/preprint_ecml_pkdd_2025_research_1013.pdf"},{"title":"Mitigating gradient conflicts via expert squads in multi-task learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0925231224016035"}]

Based on my search results, I've found comprehensive information on the topic of auxiliary losses/rewards and their potential negative effects on primary task performance. Here's a summary of the relevant findings:

## Key Research Findings

### Auxiliary Losses Can Hurt Performance

Auxiliary tasks may sometimes hurt the performance on the primary task. Auxiliary tasks may be harmful if their signal does not align with the main task, or if label noise is present. Naïve weighting can exacerbate negative transfer.

### Gradient Conflicts in Auxiliary Learning

A significant mechanism through which auxiliary tasks harm primary task performance is through gradient conflicts. A major challenge in optimizing a multi-task model is the conflicting gradients, where gradients of different task objectives are not well aligned so that following the average gradient direction can be detrimental to specific tasks' performance.

When jointly learning multiple tasks, the gradients from different tasks may be in conflict with each other, causing inter-task interference that harms performance. PCGrad resolves such conflict using gradient projections.

### Auxiliary Loss Interference in Model Training

In the context of Mixture-of-Experts (MoE) models, which are commonly used in LLMs, a large auxiliary loss will introduce non-negligible interference gradients into training and thus impair the model performance. This finding is particularly relevant to recent LLM architectures. DeepSeek-V3 pushed the boundaries of MoE efficiency with 671B total parameters and only 37B active per token, using 256 fine-grained experts and an innovative auxiliary-loss-free load balancing strategy that eliminates the traditional auxiliary loss term in favor of bias-based routing adjustments.

### Negative Transfer Causes

It is widely believed that gradient conflicts between different tasks will lead to optimization difficulties, which in turn lead to negative transfer. Research has identified that enforcing feature sharing across all layers may result in negative transfer for unrelated tasks. To address this, soft order networks offer more flexibility by allowing different layer assemblies for different tasks.

### Task-Specific Solutions

To mitigate these issues, researchers have developed various approaches. Recent algorithms combine uncertainty weighting in the decoder (i.e., per-task loss heads) with gradient norm balancing and uncertainty mapping in the shared encoder, as in the Impartial Auxiliary Learning method (IAL). This strategy is demonstrated to yield robust gains in both clean and noisy auxiliary settings.

The research from 2024-2025 shows that while auxiliary tasks and losses can be beneficial in many scenarios, they require careful design and weighting to avoid negative transfer and performance degradation on primary tasks, particularly in complex domains like LLM reasoning and reasoning-based reinforcement learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "b7319712-6d27-446d-acea-787080ebd3d3",
  "tool_use_result": {
    "query": "\"auxiliary loss\" OR \"auxiliary reward\" \"hurts\" OR \"degrades\" OR \"reduces\" primary task performance reinforcement learning LLM 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NMgJpHeZRR7yutvQy35c79",
        "content": [
          {
            "title": "On Auxiliary Tasks in Deep Reinforcement Learning | Yunfan’s Blog",
            "url": "https://yunfanj.com/blog/2021/03/14/AuxTasks.html"
          },
          {
            "title": "Learning through Auxiliary Tasks | Unsupervised Thoughts",
            "url": "https://vivien000.github.io/blog/journal/learning-though-auxiliary_tasks.html"
          },
          {
            "title": "What is Auxiliary Tasks? | Activeloop Glossary",
            "url": "https://www.activeloop.ai/resources/glossary/auxiliary-tasks/"
          },
          {
            "title": "Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation",
            "url": "https://arxiv.org/html/2602.09305v1"
          },
          {
            "title": "A framework for mitigating malicious RLHF feedback in LLM training using consensus based reward | Scientific Reports",
            "url": "https://www.nature.com/articles/s41598-025-92889-7"
          },
          {
            "title": "LLM Reinforcement Learning | IBM",
            "url": "https://www.ibm.com/think/topics/llm-reinforcement-learning"
          },
          {
            "title": "Tutorial #4: auxiliary tasks in deep reinforcement learning - Research Blog | RBC Borealis",
            "url": "https://rbcborealis.com/research-blogs/tutorial-4-auxiliary-tasks-deep-reinforcement-learning/"
          },
          {
            "title": "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? | OpenReview",
            "url": "https://openreview.net/forum?id=4OsgYD7em5"
          },
          {
            "title": "Pushing RL Boundaries: Integrating Foundational Models, e.g. LLMs and VLMs, into Reinforcement Learning | by Elahe Aghapour | TDS Archive | Medium",
            "url": "https://medium.com/data-science/pushing-boundaries-integrating-foundational-models-e-g-556cfb6d0632"
          },
          {
            "title": "Efficient Reinforcement Learning with Large Language Model Priors",
            "url": "https://arxiv.org/html/2410.07927v1"
          }
        ]
      },
      "I found some relevant results, but let me search more specifically for recent research on negative effects of auxiliary losses/rewards on LLMs and reinforcement learning in 2024-2025:",
      {
        "tool_use_id": "srvtoolu_01UgBrtvhKoTcXmh1BtiHGJM",
        "content": [
          {
            "title": "RecSys 2024 — Session 6: Multi-task Learning - RecSys",
            "url": "https://recsys.acm.org/recsys24/session-6/"
          },
          {
            "title": "Adaptive Task Weighting in Multi-Task Learning",
            "url": "https://www.emergentmind.com/topics/adaptive-task-weighting-in-multi-task-learning"
          },
          {
            "title": "Multi-Task Learning in Natural Language Processing: An Overview | ACM Computing Surveys",
            "url": "https://dl.acm.org/doi/10.1145/3663363"
          },
          {
            "title": "Multi-Task Learning in Natural Language Processing: An Overview",
            "url": "https://arxiv.org/html/2109.09138v2"
          },
          {
            "title": "Multitask Learning 1997–2024: Part I Fundamentals · Issue 7.3, Summer 2025",
            "url": "https://hdsr.mitpress.mit.edu/pub/7fcc3jhv/release/2"
          },
          {
            "title": "Is multitask learning all you need in continual learning? | OpenReview",
            "url": "https://openreview.net/forum?id=Pin2kdWloe"
          },
          {
            "title": "Advances and challenges of multi-task learning method in recommender systems: A survey - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S0925231225031820"
          },
          {
            "title": "GitHub - dingwoai/Multi-Task-Learning: A list of papers, codes and applications on multi-task learning. · GitHub",
            "url": "https://github.com/dingwoai/Multi-Task-Learning"
          },
          {
            "title": "(PDF) Multi-Task Learning 1997–2024: Part II Regularization and Optimization",
            "url": "https://www.researchgate.net/publication/394183446_Multi-Task_Learning_1997-2024_Part_II_Regularization_and_Optimization"
          },
          {
            "title": "GitHub - junfish/Awesome-Multitask-Learning: This repository periodicly updates the MTL paper and resources · GitHub",
            "url": "https://github.com/junfish/Awesome-Multitask-Learning"
          }
        ]
      },
      "Let me search more specifically for recent papers on auxiliary rewards hurting LLM reasoning or RL performance:",
      {
        "tool_use_id": "srvtoolu_012Nnw4N9EzE78VAMGBjdSDg",
        "content": [
          {
            "title": "Auxiliary-Loss-Free Load Balancing Strategy for Mixture-of-Experts | OpenReview",
            "url": "https://openreview.net/forum?id=y1iU5czYpE"
          },
          {
            "title": "000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019",
            "url": "https://openreview.net/pdf?id=vIIflOgwZX"
          },
          {
            "title": "Mixture-of-Experts (MoE) LLMs - by Cameron R. Wolfe, Ph.D.",
            "url": "https://cameronrwolfe.substack.com/p/moe-llms"
          },
          {
            "title": "[Quick Review] Coupling Experts and Routers in Mixture-of-Experts via an Auxiliary Loss",
            "url": "https://liner.com/review/coupling-experts-and-routers-in-mixtureofexperts-via-auxiliary-loss"
          },
          {
            "title": "Understanding Mixture of Experts (MoE) Neural Networks | IntuitionLabs",
            "url": "https://intuitionlabs.ai/articles/mixture-of-experts-moe-models"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 CAPACITY-AWARE INFERENCE:",
            "url": "https://openreview.net/pdf?id=LuYFpySWA2"
          }
        ]
      },
      "Excellent! I found some very relevant results. Let me search for more specific information about negative effects of auxiliary rewards on LLM reasoning tasks:",
      {
        "tool_use_id": "srvtoolu_01WJqHsB66f6AWbzniKDmCr1",
        "content": [
          {
            "title": "Resolving Token-Space Gradient Conflicts: Token Space Manipulation for",
            "url": "https://openaccess.thecvf.com/content/ICCV2025/papers/Jeong_Resolving_Token-Space_Gradient_Conflicts_Token_Space_Manipulation_for_Transformer-Based_Multi-Task_ICCV_2025_paper.pdf"
          },
          {
            "title": "DaGRPO: Rectifying Gradient Conflict in Reasoning via ...",
            "url": "https://arxiv.org/pdf/2512.06337"
          },
          {
            "title": "ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning",
            "url": "https://ise.thss.tsinghua.edu.cn/~mlong/doc/ForkMerge-nips23.pdf"
          },
          {
            "title": "Conflict-Averse Gradient Descent for Multi-task learning | OpenReview",
            "url": "https://openreview.net/forum?id=_61Qh8tULj_"
          },
          {
            "title": "[2303.05847] Gradient Coordination for Quantifying and Maximizing Knowledge Transference in Multi-Task Learning",
            "url": "https://arxiv.org/abs/2303.05847"
          },
          {
            "title": "[2110.14048] Conflict-Averse Gradient Descent for Multi-task Learning",
            "url": "https://arxiv.org/abs/2110.14048"
          },
          {
            "title": "Conflict-Averse Gradient Descent for Multi-task Learning",
            "url": "https://arxiv.org/html/2110.14048v2"
          },
          {
            "title": "Towards Task-Conﬂicts Momentum-Calibrated Approach for Multi-task Learning",
            "url": "https://www.hufudb.com/static/paper/2024/ICDE24-chai.pdf"
          },
          {
            "title": "Gradient Similarity Surgery in Multi-Task Deep Learning",
            "url": "https://ecmlpkdd-storage.s3.eu-central-1.amazonaws.com/preprints/2025/research/preprint_ecml_pkdd_2025_research_1013.pdf"
          },
          {
            "title": "Mitigating gradient conflicts via expert squads in multi-task learning - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S0925231224016035"
          }
        ]
      },
      "Based on my search results, I've found comprehensive information on the topic of auxiliary losses/rewards and their potential negative effects on primary task performance. Here's a summary of the relevant findings:\n\n## Key Research Findings\n\n### Auxiliary Losses Can Hurt Performance\n\nAuxiliary tasks may sometimes hurt the performance on the primary task. Auxiliary tasks may be harmful if their signal does not align with the main task, or if label noise is present. Naïve weighting can exacerbate negative transfer.\n\n### Gradient Conflicts in Auxiliary Learning\n\nA significant mechanism through which auxiliary tasks harm primary task performance is through gradient conflicts. A major challenge in optimizing a multi-task model is the conflicting gradients, where gradients of different task objectives are not well aligned so that following the average gradient direction can be detrimental to specific tasks' performance.\n\nWhen jointly learning multiple tasks, the gradients from different tasks may be in conflict with each other, causing inter-task interference that harms performance. PCGrad resolves such conflict using gradient projections.\n\n### Auxiliary Loss Interference in Model Training\n\nIn the context of Mixture-of-Experts (MoE) models, which are commonly used in LLMs, a large auxiliary loss will introduce non-negligible interference gradients into training and thus impair the model performance. This finding is particularly relevant to recent LLM architectures. DeepSeek-V3 pushed the boundaries of MoE efficiency with 671B total parameters and only 37B active per token, using 256 fine-grained experts and an innovative auxiliary-loss-free load balancing strategy that eliminates the traditional auxiliary loss term in favor of bias-based routing adjustments.\n\n### Negative Transfer Causes\n\nIt is widely believed that gradient conflicts between different tasks will lead to optimization difficulties, which in turn lead to negative transfer. Research has identified that enforcing feature sharing across all layers may result in negative transfer for unrelated tasks. To address this, soft order networks offer more flexibility by allowing different layer assemblies for different tasks.\n\n### Task-Specific Solutions\n\nTo mitigate these issues, researchers have developed various approaches. Recent algorithms combine uncertainty weighting in the decoder (i.e., per-task loss heads) with gradient norm balancing and uncertainty mapping in the shared encoder, as in the Impartial Auxiliary Learning method (IAL). This strategy is demonstrated to yield robust gains in both clean and noisy auxiliary settings.\n\nThe research from 2024-2025 shows that while auxiliary tasks and losses can be beneficial in many scenarios, they require careful design and weighting to avoid negative transfer and performance degradation on primary tasks, particularly in complex domains like LLM reasoning and reasoning-based reinforcement learning."
    ],
    "durationSeconds": 22.105216817999995
  }
}
```

</details>

---

### Assistant

_source line 33_

<details><summary>Logged reasoning block</summary>

```text
Good findings so far. Let me now fetch more details on the most relevant papers. I need to investigate:

1. "Beyond Correctness: Harmonizing Process and Outcome Rewards" (2509.03403) - already got details
2. "Confronting Reward Model Overoptimization with Constrained RLHF" (2310.04373) - already got details
3. "ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning" (NeurIPS 2023)
4. "Conflict-Averse Gradient Descent for Multi-task Learning" (2110.14048)


5. "DaGRPO: Rectifying Gradient Conflict in Reasoning" (2512.06337) - this looks particularly promising for what I'm exploring
6. "Auxiliary-Loss-Free Load Balancing Strategy for MoE" - worth checking though it's more MoE-focused
7. The "GRPO is secretly a PRM" paper

I should dig into DaGRPO and the auxiliary-loss-free approach more carefully, and search for additional work on how process rewards can negatively impact outcome performance in LLM reasoning tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "853315fd-2673-4f7c-969c-a52ea6f82f2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SorHL1DWGrr4rywpayjVXW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 825,
      "cache_creation_input_tokens": 4606,
      "cache_read_input_tokens": 34520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4606
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

Let me dig deeper into the most relevant papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "dcbe6a9e-8d95-443d-933c-c5dd94248ad2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SorHL1DWGrr4rywpayjVXW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 825,
      "cache_creation_input_tokens": 4606,
      "cache_read_input_tokens": 34520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4606
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_0137E3caHy6NLtuNd8io2ftU`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.06337",
  "prompt": "Extract: title, all authors, year, venue. What is the main finding about gradient conflicts in GRPO? Does adding auxiliary objectives or rewards hurt the primary reasoning performance? What solutions do they propose?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "fdc28107-fbfd-4697-8dc2-13f226bdcc17",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SorHL1DWGrr4rywpayjVXW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 825,
      "cache_creation_input_tokens": 4606,
      "cache_read_input_tokens": 34520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4606
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_011xEF33rNL3G3PCZzX6GBGX`</summary>

```json
{
  "url": "https://ise.thss.tsinghua.edu.cn/~mlong/doc/ForkMerge-nips23.pdf",
  "prompt": "Extract: title, all authors, year, venue. What is the main finding about negative transfer in auxiliary-task learning? How does adding auxiliary tasks degrade primary task performance, and what solution do they propose?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "c44626ac-1246-41d8-804a-776e9fc21800",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SorHL1DWGrr4rywpayjVXW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 825,
      "cache_creation_input_tokens": 4606,
      "cache_read_input_tokens": 34520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4606
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SCPxhBc9Qb2hivezWEmbPW`</summary>

```json
{
  "query": "\"process reward\" \"outcome reward\" conflict degradation LLM reasoning GRPO RL training 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "8a891f38-3ae6-4bd8-b517-92c9c6dfcf62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SorHL1DWGrr4rywpayjVXW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 825,
      "cache_creation_input_tokens": 4606,
      "cache_read_input_tokens": 34520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4606
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DAaYzefeb1fHFZ3Y6BFyYZ`</summary>

```json
{
  "query": "Skalse reward hacking taxonomy auxiliary objective side effects reinforcement learning 2022 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "5f041911-85fa-4160-820a-537ecbcbe0c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SorHL1DWGrr4rywpayjVXW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 825,
      "cache_creation_input_tokens": 4606,
      "cache_read_input_tokens": 34520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4606
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

_source line 39 · 2026-05-14T02:05:28.267Z_

<details><summary>↩ Tool result · `toolu_0137E3caHy6NLtuNd8io2ftU`</summary>

```text
# DaGRPO Paper Summary

**Title:** DaGRPO: Rectifying Gradient Conflict in Reasoning via Distinctiveness-Aware Group Relative Policy Optimization

**Authors:** Xuan Xie, Xuan Wang, Wenjie Wang, Shuai Chen, Wei Lin

**Year:** 2025

**Venue:** arXiv (cs.AI)

## Main Finding on Gradient Conflicts

The researchers theoretically identified that "homogeneous samples induce destructive gradient conflicts" in standard GRPO, particularly affecting routine queries. Additionally, hard queries suffer from "the scarcity of valid positive samples," leading to ineffective optimization.

## Impact of Auxiliary Objectives

The document does not discuss whether auxiliary objectives or rewards harm primary reasoning performance. It focuses exclusively on problems within the GRPO framework itself rather than examining multi-objective trade-offs.

## Proposed Solutions

DaGRPO introduces two mechanisms:

1. **Sequence-level Gradient Rectification:** This approach "dynamically mask[s] sample pairs with low distinctiveness," directly eliminating gradient conflicts at their source.

2. **Off-policy Data Augmentation:** This mechanism "introduces high-quality anchors to recover training signals for challenging tasks," addressing the shortage of effective samples for difficult problems.

The method achieved "+4.7% average accuracy gain on math benchmarks" and demonstrated mitigation of gradient explosion.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "8456963f-2aac-46b5-9e31-90bf0b2941c9",
  "tool_use_result": {
    "bytes": 47781,
    "code": 200,
    "codeText": "OK",
    "result": "# DaGRPO Paper Summary\n\n**Title:** DaGRPO: Rectifying Gradient Conflict in Reasoning via Distinctiveness-Aware Group Relative Policy Optimization\n\n**Authors:** Xuan Xie, Xuan Wang, Wenjie Wang, Shuai Chen, Wei Lin\n\n**Year:** 2025\n\n**Venue:** arXiv (cs.AI)\n\n## Main Finding on Gradient Conflicts\n\nThe researchers theoretically identified that \"homogeneous samples induce destructive gradient conflicts\" in standard GRPO, particularly affecting routine queries. Additionally, hard queries suffer from \"the scarcity of valid positive samples,\" leading to ineffective optimization.\n\n## Impact of Auxiliary Objectives\n\nThe document does not discuss whether auxiliary objectives or rewards harm primary reasoning performance. It focuses exclusively on problems within the GRPO framework itself rather than examining multi-objective trade-offs.\n\n## Proposed Solutions\n\nDaGRPO introduces two mechanisms:\n\n1. **Sequence-level Gradient Rectification:** This approach \"dynamically mask[s] sample pairs with low distinctiveness,\" directly eliminating gradient conflicts at their source.\n\n2. **Off-policy Data Augmentation:** This mechanism \"introduces high-quality anchors to recover training signals for challenging tasks,\" addressing the shortage of effective samples for difficult problems.\n\nThe method achieved \"+4.7% average accuracy gain on math benchmarks\" and demonstrated mitigation of gradient explosion.",
    "durationMs": 4683,
    "url": "https://arxiv.org/abs/2512.06337"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T02:05:30.620Z_

<details><summary>↩ Tool result · `toolu_011xEF33rNL3G3PCZzX6GBGX`</summary>

```text
I appreciate your request, but I'm unable to extract the information you're looking for from the provided content. The text appears to be a PDF file in binary/encoded format rather than readable plain text about a research paper on auxiliary-task learning and negative transfer.

To help you effectively, I would need:
- The paper's title, authors, year, and venue in readable format
- Clear text describing their findings on negative transfer
- Details about their proposed solution

If you could provide the paper as readable text (copy-pasted from a PDF viewer or the paper's abstract/introduction), I'd be happy to extract and summarize:
- Complete citation information
- The main findings regarding how auxiliary tasks can degrade primary task performance
- Their proposed mitigation approach

Alternatively, if you have a link to the paper or can share its title and authors, I can help you locate and analyze the key findings.

[Binary content (application/pdf, 2.1MB) also saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/6c8ab3fa-f3c3-483d-b115-dccc1097e77a/tool-results/webfetch-1778724326805-nekjrt.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "eaea3194-73c9-4f31-b623-d2bd6b5187b5",
  "tool_use_result": {
    "bytes": 2190296,
    "code": 200,
    "codeText": "OK",
    "result": "I appreciate your request, but I'm unable to extract the information you're looking for from the provided content. The text appears to be a PDF file in binary/encoded format rather than readable plain text about a research paper on auxiliary-task learning and negative transfer.\n\nTo help you effectively, I would need:\n- The paper's title, authors, year, and venue in readable format\n- Clear text describing their findings on negative transfer\n- Details about their proposed solution\n\nIf you could provide the paper as readable text (copy-pasted from a PDF viewer or the paper's abstract/introduction), I'd be happy to extract and summarize:\n- Complete citation information\n- The main findings regarding how auxiliary tasks can degrade primary task performance\n- Their proposed mitigation approach\n\nAlternatively, if you have a link to the paper or can share its title and authors, I can help you locate and analyze the key findings.\n\n[Binary content (application/pdf, 2.1MB) also saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/6c8ab3fa-f3c3-483d-b115-dccc1097e77a/tool-results/webfetch-1778724326805-nekjrt.pdf]",
    "durationMs": 5033,
    "url": "https://ise.thss.tsinghua.edu.cn/~mlong/doc/ForkMerge-nips23.pdf"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-14T02:05:34.121Z_

<details><summary>↩ Tool result · `toolu_01DAaYzefeb1fHFZ3Y6BFyYZ`</summary>

```text
Web search results for query: "Skalse reward hacking taxonomy auxiliary objective side effects reinforcement learning 2022 2023"

Links: [{"title":"Defining and Characterizing Reward Hacking Joar Skalse∗ University of Oxford","url":"https://arxiv.org/pdf/2209.13085"},{"title":"Detecting and Mitigating Reward Hacking in Reinforcement Learning Systems: A Comprehensive Empirical Study","url":"https://arxiv.org/html/2507.05619v1"},{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"[PDF] Defining and Characterizing Reward Hacking | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Defining-and-Characterizing-Reward-Hacking-Skalse-Howe/004357dd9bbf3012c8fe0ccada4da401bf85dfff"},{"title":"[2209.13085] Defining and Characterizing Reward Hacking","url":"https://arxiv.org/abs/2209.13085"},{"title":"Reward Hacking in RLVR","url":"https://www.emergentmind.com/topics/reward-hacking-in-rlvr"},{"title":"Detecting and Mitigating Reward Hacking in Reinforcement","url":"https://arxiv.org/pdf/2507.05619"},{"title":"A Comprehensive Survey of Reward Models: Taxonomy, Applications, Challenges, and Future","url":"https://arxiv.org/html/2504.12328v1"},{"title":"Scaling Laws for Reward Model Overoptimization","url":"https://proceedings.mlr.press/v202/gao23h/gao23h.pdf"},{"title":"correlated proxies:anew definition and improved mitigation ...","url":"https://arxiv.org/pdf/2403.03185"}]

I found several highly relevant sources about reward hacking, Skalse's work, and related taxonomies. Here's what the search revealed:

## Key Findings

Skalse et al. (2022) provided the first formal definition of reward hacking, a phenomenon where optimizing an imperfect proxy reward function leads to poor performance according to the true reward function. They define a proxy as unhackable if increasing the expected proxy return can never decrease the expected true return.

A key insight from their work is that the linearity of reward (in state-action visit counts) makes unhackability a very strong condition—for the set of all stochastic policies, two reward functions can only be unhackable if one of them is constant.

## Taxonomy and Related Work

More recently, work building on Skalse et al. (2022) operationalized a taxonomy of reward hacking behaviors organized into six primary categories. The fundamental challenge involves the inherent difficulty of specifying complex, real-world objectives through simple reward functions, creating misalignment between what we want agents to do and what we can effectively measure and reward.

## Auxiliary Objectives and Side Effects

One approach introduces auxiliary reward functions, balancing optimization of the primary reward function with preservation of the ability to optimize auxiliary reward functions, and surprisingly, even when the auxiliary rewards are randomly generated and therefore uninformative, this approach induces conservative, effective behavior.

The search results reveal Skalse's seminal 2022 work and subsequent research extending their framework to detect and mitigate reward hacking behaviors across diverse reinforcement learning settings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "e5b8096c-e574-4239-a321-351745c511aa",
  "tool_use_result": {
    "query": "Skalse reward hacking taxonomy auxiliary objective side effects reinforcement learning 2022 2023",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PXZEYb7B3Fh4hPxe7G9Tsv",
        "content": [
          {
            "title": "Defining and Characterizing Reward Hacking Joar Skalse∗ University of Oxford",
            "url": "https://arxiv.org/pdf/2209.13085"
          },
          {
            "title": "Detecting and Mitigating Reward Hacking in Reinforcement Learning Systems: A Comprehensive Empirical Study",
            "url": "https://arxiv.org/html/2507.05619v1"
          },
          {
            "title": "Reward Hacking in Reinforcement Learning | Lil'Log",
            "url": "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"
          },
          {
            "title": "[PDF] Defining and Characterizing Reward Hacking | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Defining-and-Characterizing-Reward-Hacking-Skalse-Howe/004357dd9bbf3012c8fe0ccada4da401bf85dfff"
          },
          {
            "title": "[2209.13085] Defining and Characterizing Reward Hacking",
            "url": "https://arxiv.org/abs/2209.13085"
          },
          {
            "title": "Reward Hacking in RLVR",
            "url": "https://www.emergentmind.com/topics/reward-hacking-in-rlvr"
          },
          {
            "title": "Detecting and Mitigating Reward Hacking in Reinforcement",
            "url": "https://arxiv.org/pdf/2507.05619"
          },
          {
            "title": "A Comprehensive Survey of Reward Models: Taxonomy, Applications, Challenges, and Future",
            "url": "https://arxiv.org/html/2504.12328v1"
          },
          {
            "title": "Scaling Laws for Reward Model Overoptimization",
            "url": "https://proceedings.mlr.press/v202/gao23h/gao23h.pdf"
          },
          {
            "title": "correlated proxies:anew definition and improved mitigation ...",
            "url": "https://arxiv.org/pdf/2403.03185"
          }
        ]
      },
      "I found several highly relevant sources about reward hacking, Skalse's work, and related taxonomies. Here's what the search revealed:\n\n## Key Findings\n\nSkalse et al. (2022) provided the first formal definition of reward hacking, a phenomenon where optimizing an imperfect proxy reward function leads to poor performance according to the true reward function. They define a proxy as unhackable if increasing the expected proxy return can never decrease the expected true return.\n\nA key insight from their work is that the linearity of reward (in state-action visit counts) makes unhackability a very strong condition—for the set of all stochastic policies, two reward functions can only be unhackable if one of them is constant.\n\n## Taxonomy and Related Work\n\nMore recently, work building on Skalse et al. (2022) operationalized a taxonomy of reward hacking behaviors organized into six primary categories. The fundamental challenge involves the inherent difficulty of specifying complex, real-world objectives through simple reward functions, creating misalignment between what we want agents to do and what we can effectively measure and reward.\n\n## Auxiliary Objectives and Side Effects\n\nOne approach introduces auxiliary reward functions, balancing optimization of the primary reward function with preservation of the ability to optimize auxiliary reward functions, and surprisingly, even when the auxiliary rewards are randomly generated and therefore uninformative, this approach induces conservative, effective behavior.\n\nThe search results reveal Skalse's seminal 2022 work and subsequent research extending their framework to detect and mitigate reward hacking behaviors across diverse reinforcement learning settings."
    ],
    "durationSeconds": 6.9554434190000025
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T02:05:35.426Z_

<details><summary>↩ Tool result · `toolu_01SCPxhBc9Qb2hivezWEmbPW`</summary>

```text
Web search results for query: ""process reward" "outcome reward" conflict degradation LLM reasoning GRPO RL training 2024 2025 2026"

Links: [{"title":"Navigate the Unknown: Enhancing LLM Reasoning with Intrinsic Motivation Guided Exploration","url":"https://arxiv.org/html/2505.17621v1"},{"title":"LLM Reasoning with Process Rewards for Outcome-Guided Steps","url":"https://arxiv.org/html/2604.02341v1"},{"title":"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training","url":"https://arxiv.org/html/2509.03403v1"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation","url":"https://arxiv.org/html/2602.09305v1"},{"title":"Outcome-based Exploration for LLM Reasoning","url":"https://arxiv.org/pdf/2509.06941"},{"title":"The State of Reinforcement Learning for LLM Reasoning","url":"https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training"},{"title":"RM-R1: Reward Modeling as Reasoning","url":"https://arxiv.org/pdf/2505.02387"},{"title":"PRL: Process Reward Learning Improves LLMs’ Reasoning Ability and Broadens the Reasoning Boundary","url":"https://arxiv.org/html/2601.10201v1"},{"title":"On Designing Effective RL Reward at Training Time for LLM Reasoning","url":"https://arxiv.org/html/2410.15115v1"},{"title":"GitHub - bobxwu/learning-from-rewards-llm-papers: A comrephensive collection of learning from rewards in the post-training and test-time scaling of LLMs, with a focus on both reward models and learning strategies across training, inference, and post-inference stages. · GitHub","url":"https://github.com/bobxwu/learning-from-rewards-llm-papers"}]

Based on the search results, I found several highly relevant papers and discussions about process reward and outcome reward conflicts in LLM reasoning with GRPO RL training. Here are the key findings:

## Process Reward vs. Outcome Reward Conflicts

Directly combining exploration rewards with outcome-based rewards creates conflicting learning signals across training stages, and for GRPO, exploration rewards may invert originally positive advantage signs after group normalization, which is a critical issue since exploration rewards should never penalize samples.

PROF reduces PRM–ORM conflicts by filtering trajectories based on consistency between process and outcome evaluations, and even with better PRMs or filtering, optimization can still be distorted if incorrect trajectories receive systematically positive process bonuses.

## Solutions to the Conflict

Several papers propose methods to resolve this conflict:

1. **PROGRS (Process-Reward Outcome-Guided Reasoning Steps)**: Outcome-conditioned centering enables safe and effective use of process rewards for mathematical reasoning, and PROGRS constrains process rewards through outcome-conditioned centering while leveraging hierarchical coherence to extract stable, relative signals from noisy step-level estimates.

2. **i-MENTOR**: The advantage-preserving reward implementation decouples exploration incentives from outcome-based gradients, resolving conflicts between intrinsic and extrinsic rewards.

3. **PROF**: PROF is a modular framework that can be combined with RL algorithms like Group Relative Policy Optimization (GRPO) for online training, and PROF-GRPO not only increases the final outcome accuracy but also shapes the intermediate reasoning steps and improves the process reasoning quality.

## Performance Degradation Issues

A severe reward hacking issue occurs with Process Reward Models, manifesting in the form of generating numerous correct but unnecessary reasoning steps.

These papers represent recent work from 2024-2026 directly addressing your query about process reward and outcome reward conflicts in GRPO-based RL training for LLM reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "7420d05e-8f99-4cdd-b753-1ce4ec21f6f3",
  "tool_use_result": {
    "query": "\"process reward\" \"outcome reward\" conflict degradation LLM reasoning GRPO RL training 2024 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Dadsfc13YGz4pPUiBit96f",
        "content": [
          {
            "title": "Navigate the Unknown: Enhancing LLM Reasoning with Intrinsic Motivation Guided Exploration",
            "url": "https://arxiv.org/html/2505.17621v1"
          },
          {
            "title": "LLM Reasoning with Process Rewards for Outcome-Guided Steps",
            "url": "https://arxiv.org/html/2604.02341v1"
          },
          {
            "title": "Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training",
            "url": "https://arxiv.org/html/2509.03403v1"
          },
          {
            "title": "Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation",
            "url": "https://arxiv.org/html/2602.09305v1"
          },
          {
            "title": "Outcome-based Exploration for LLM Reasoning",
            "url": "https://arxiv.org/pdf/2509.06941"
          },
          {
            "title": "The State of Reinforcement Learning for LLM Reasoning",
            "url": "https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training"
          },
          {
            "title": "RM-R1: Reward Modeling as Reasoning",
            "url": "https://arxiv.org/pdf/2505.02387"
          },
          {
            "title": "PRL: Process Reward Learning Improves LLMs’ Reasoning Ability and Broadens the Reasoning Boundary",
            "url": "https://arxiv.org/html/2601.10201v1"
          },
          {
            "title": "On Designing Effective RL Reward at Training Time for LLM Reasoning",
            "url": "https://arxiv.org/html/2410.15115v1"
          },
          {
            "title": "GitHub - bobxwu/learning-from-rewards-llm-papers: A comrephensive collection of learning from rewards in the post-training and test-time scaling of LLMs, with a focus on both reward models and learning strategies across training, inference, and post-inference stages. · GitHub",
            "url": "https://github.com/bobxwu/learning-from-rewards-llm-papers"
          }
        ]
      },
      "Based on the search results, I found several highly relevant papers and discussions about process reward and outcome reward conflicts in LLM reasoning with GRPO RL training. Here are the key findings:\n\n## Process Reward vs. Outcome Reward Conflicts\n\nDirectly combining exploration rewards with outcome-based rewards creates conflicting learning signals across training stages, and for GRPO, exploration rewards may invert originally positive advantage signs after group normalization, which is a critical issue since exploration rewards should never penalize samples.\n\nPROF reduces PRM–ORM conflicts by filtering trajectories based on consistency between process and outcome evaluations, and even with better PRMs or filtering, optimization can still be distorted if incorrect trajectories receive systematically positive process bonuses.\n\n## Solutions to the Conflict\n\nSeveral papers propose methods to resolve this conflict:\n\n1. **PROGRS (Process-Reward Outcome-Guided Reasoning Steps)**: Outcome-conditioned centering enables safe and effective use of process rewards for mathematical reasoning, and PROGRS constrains process rewards through outcome-conditioned centering while leveraging hierarchical coherence to extract stable, relative signals from noisy step-level estimates.\n\n2. **i-MENTOR**: The advantage-preserving reward implementation decouples exploration incentives from outcome-based gradients, resolving conflicts between intrinsic and extrinsic rewards.\n\n3. **PROF**: PROF is a modular framework that can be combined with RL algorithms like Group Relative Policy Optimization (GRPO) for online training, and PROF-GRPO not only increases the final outcome accuracy but also shapes the intermediate reasoning steps and improves the process reasoning quality.\n\n## Performance Degradation Issues\n\nA severe reward hacking issue occurs with Process Reward Models, manifesting in the form of generating numerous correct but unnecessary reasoning steps.\n\nThese papers represent recent work from 2024-2026 directly addressing your query about process reward and outcome reward conflicts in GRPO-based RL training for LLM reasoning."
    ],
    "durationSeconds": 9.01690362299999
  }
}
```

</details>

---

### Assistant

_source line 43_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch more details on a few more key papers:

1. "On Designing Effective RL Reward at Training Time for LLM Reasoning" (2410.15115) - seems relevant
2. "LLM Reasoning with Process Rewards for Outcome-Guided Steps" (2604.02341) - the PROGRS paper
3. The ForkMerge paper abstract from NeurIPS 2023
4. Skalse et al. "Defining and Characterizing Reward Hacking" (2209.13085)

Let me focus on getting the most relevant 3-5 papers for the report. 

Looking at my search results, the most directly relevant papers are ones that tackle the tension between process and outcome rewards. The Ye et al. PROF framework paper addresses exactly this conflict—they show that simply combining process and outcome reward models actually hurts performance, and they propose a filtering mechanism to resolve it. Then there's the Moskovitz et al. work on constrained RLHF that demonstrates how composite reward models get overoptimized, with the correlation between component rewards playing a key role in determining outcomes.

I also found Skalse et al.'s formal framework on reward hacking, which provides the theoretical grounding for why optimizing a proxy reward like STA can paradoxically decrease the true objective—this is foundational for understanding the negative transfer problem. The ForkMerge paper from NeurIPS 2023 is relevant too since it shows auxiliary tasks can cause negative transfer and proposes a dynamic branching solution. I need to verify a couple others like the reasoning with process rewards paper and the one on effective RL reward design for LLM reasoning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "ac444b60-54fc-4a22-be0a-7dc5b9415539",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzdHa3vAJqAAkTuXDT7pbE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 893,
      "cache_creation_input_tokens": 3164,
      "cache_read_input_tokens": 39126,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3164
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

_source line 44_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LneeLiZGY5azitZGNmjCbX`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.15115",
  "prompt": "Extract: title, all authors, year, venue. Main findings about how reward design at training time affects LLM reasoning. Do they report cases where adding structured/process rewards hurts outcome performance? What solutions?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "22f03e7b-be92-485e-9f81-5c30fd753833",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzdHa3vAJqAAkTuXDT7pbE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 893,
      "cache_creation_input_tokens": 3164,
      "cache_read_input_tokens": 39126,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3164
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

_source line 45_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JtJac3h9CAxPcVX4BpKTc4`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.02341",
  "prompt": "Extract: title, all authors, year, venue. Main finding about PROGRS - outcome-conditioned process rewards. Do they report that naive process rewards hurt outcome accuracy? What is \"outcome-conditioned centering\"?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "58c11652-d9c6-4307-a3a8-1f10a5fd959b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzdHa3vAJqAAkTuXDT7pbE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 893,
      "cache_creation_input_tokens": 3164,
      "cache_read_input_tokens": 39126,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3164
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

_source line 46_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NkcqC4daqE5dBEYy8bqdQB`</summary>

```json
{
  "url": "https://arxiv.org/abs/2209.13085",
  "prompt": "Extract: title, all authors, year, venue. What is the formal definition of reward hacking? Key theorem: can optimizing a proxy reward decrease true reward? What does the \"unhackability\" condition say about auxiliary reward objectives?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "a25f5731-63fb-40d2-a968-ebd0567bce9b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzdHa3vAJqAAkTuXDT7pbE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 893,
      "cache_creation_input_tokens": 3164,
      "cache_read_input_tokens": 39126,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3164
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

_source line 47_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RAfNWwkYJpfC8YAgqyEwJx`</summary>

```json
{
  "query": "ForkMerge \"negative transfer\" auxiliary task learning NeurIPS 2023 Zheng Ge Long"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "2bfcc3d2-f235-4bef-a555-74efd79d0bf3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzdHa3vAJqAAkTuXDT7pbE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 893,
      "cache_creation_input_tokens": 3164,
      "cache_read_input_tokens": 39126,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3164
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

_source line 48 · 2026-05-14T02:05:59.691Z_

<details><summary>↩ Tool result · `toolu_01LneeLiZGY5azitZGNmjCbX`</summary>

```text
# Paper Summary

**Title:** On Designing Effective RL Reward at Training Time for LLM Reasoning

**Authors:** Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu

**Year:** 2024

**Venue:** arXiv (cs.LG - Computer Science/Machine Learning)

## Main Findings

The researchers discovered a counterintuitive problem: despite strong inference-time performance, reward models can actually degrade RL training outcomes. They found that "an LLM can receive high rewards from some of these reward models by repeating correct but unnecessary reasoning steps, leading to a severe reward hacking issue."

Specifically, they evaluated Outcome-supervised Reward Models (ORM) and Process-supervised Reward Models (PRM), finding that these learned rewards "may NOT help or even hurt RL training, producing worse performances than LLMs trained with the success reward only."

## Solutions Proposed

The team introduced two reward refinement techniques:

1. **Clipping** - Constrains accumulated reward magnitude
2. **Delta** - Restricts reward growth across trajectories

Both techniques ensure that "the accumulative reward of any reasoning trajectory is upper-bounded to keep a learned reward model effective without being exploited."

These refinements enabled improvements across 1.5B and 7B parameter models on MATH and GSM8K benchmarks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "b0075e92-c6c7-4ccf-bb3a-aec40aee2ccf",
  "tool_use_result": {
    "bytes": 49859,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary\n\n**Title:** On Designing Effective RL Reward at Training Time for LLM Reasoning\n\n**Authors:** Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu\n\n**Year:** 2024\n\n**Venue:** arXiv (cs.LG - Computer Science/Machine Learning)\n\n## Main Findings\n\nThe researchers discovered a counterintuitive problem: despite strong inference-time performance, reward models can actually degrade RL training outcomes. They found that \"an LLM can receive high rewards from some of these reward models by repeating correct but unnecessary reasoning steps, leading to a severe reward hacking issue.\"\n\nSpecifically, they evaluated Outcome-supervised Reward Models (ORM) and Process-supervised Reward Models (PRM), finding that these learned rewards \"may NOT help or even hurt RL training, producing worse performances than LLMs trained with the success reward only.\"\n\n## Solutions Proposed\n\nThe team introduced two reward refinement techniques:\n\n1. **Clipping** - Constrains accumulated reward magnitude\n2. **Delta** - Restricts reward growth across trajectories\n\nBoth techniques ensure that \"the accumulative reward of any reasoning trajectory is upper-bounded to keep a learned reward model effective without being exploited.\"\n\nThese refinements enabled improvements across 1.5B and 7B parameter models on MATH and GSM8K benchmarks.",
    "durationMs": 5697,
    "url": "https://arxiv.org/abs/2410.15115"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-14T02:06:00.558Z_

<details><summary>↩ Tool result · `toolu_01JtJac3h9CAxPcVX4BpKTc4`</summary>

```text
# Paper Analysis

**Title:** LLM Reasoning with Process Rewards for Outcome-Guided Steps

**Authors:** Mohammad Rezaei, Jens Lehmann, Sahar Vahdati

**Year:** 2026

**Venue:** Submitted to IJCNN 2026 conference

## Main Findings

**PROGRS Framework:**
The paper introduces PROGRS, which treats process rewards as relative preferences within outcome groups rather than absolute targets, keeping outcome correctness dominant.

**Naive Process Rewards as Harmful:**
Yes, the authors document this problem: "PRM scores are often imperfectly aligned with final correctness and can reward locally fluent reasoning that still ends in an incorrect answer. When optimized as absolute rewards, such signals can amplify fluent failure modes and induce reward hacking."

**Outcome-Conditioned Centering:**
This technique "shifts PRM scores of incorrect trajectories to have zero mean within each prompt group. It removes systematic bias while preserving informative rankings." This prevents misaligned process rewards from corrupting the training signal while maintaining their guidance value on intermediate steps.

The approach demonstrates consistent improvements across multiple mathematical reasoning benchmarks with fewer rollouts needed compared to outcome-only baselines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "4c633887-55f2-4248-b5eb-010b5e90bf1d",
  "tool_use_result": {
    "bytes": 47294,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Analysis\n\n**Title:** LLM Reasoning with Process Rewards for Outcome-Guided Steps\n\n**Authors:** Mohammad Rezaei, Jens Lehmann, Sahar Vahdati\n\n**Year:** 2026\n\n**Venue:** Submitted to IJCNN 2026 conference\n\n## Main Findings\n\n**PROGRS Framework:**\nThe paper introduces PROGRS, which treats process rewards as relative preferences within outcome groups rather than absolute targets, keeping outcome correctness dominant.\n\n**Naive Process Rewards as Harmful:**\nYes, the authors document this problem: \"PRM scores are often imperfectly aligned with final correctness and can reward locally fluent reasoning that still ends in an incorrect answer. When optimized as absolute rewards, such signals can amplify fluent failure modes and induce reward hacking.\"\n\n**Outcome-Conditioned Centering:**\nThis technique \"shifts PRM scores of incorrect trajectories to have zero mean within each prompt group. It removes systematic bias while preserving informative rankings.\" This prevents misaligned process rewards from corrupting the training signal while maintaining their guidance value on intermediate steps.\n\nThe approach demonstrates consistent improvements across multiple mathematical reasoning benchmarks with fewer rollouts needed compared to outcome-only baselines.",
    "durationMs": 5149,
    "url": "https://arxiv.org/abs/2604.02341"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-14T02:06:02.119Z_

<details><summary>↩ Tool result · `toolu_01NkcqC4daqE5dBEYy8bqdQB`</summary>

```text
# Paper Summary

**Title:** Defining and Characterizing Reward Hacking

**Authors:** Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger

**Year:** 2022 (submitted); revised 2025

**Venue:** arXiv (cs.LG - Computer Science, Machine Learning)

## Formal Definition of Reward Hacking

The paper defines reward hacking as "optimizing an imperfect proxy reward function leads to poor performance according to the true reward function." A proxy is considered "unhackable" when "increasing the expected proxy return can never decrease the expected true return."

## Key Theorem on Proxy Optimization

The central finding demonstrates a strong constraint: **for the full set of stochastic policies, two reward functions can only be unhackable if one remains constant.** This reveals that yes, optimizing a proxy reward can decrease true reward performance under most realistic conditions.

## Unhackability and Auxiliary Objectives

The unhackability condition indicates a fundamental tension in AI alignment. While narrower reward functions or simplified distinctions might intuitively seem safer, the paper shows this approach "is usually not the case." The research uncovers "a tension between using reward functions to specify narrow tasks and aligning AI systems with human values," suggesting that auxiliary objectives cannot easily solve reward specification problems through simplification alone.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "86b89141-10c3-422e-949d-4c9e463ab522",
  "tool_use_result": {
    "bytes": 47053,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary\n\n**Title:** Defining and Characterizing Reward Hacking\n\n**Authors:** Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger\n\n**Year:** 2022 (submitted); revised 2025\n\n**Venue:** arXiv (cs.LG - Computer Science, Machine Learning)\n\n## Formal Definition of Reward Hacking\n\nThe paper defines reward hacking as \"optimizing an imperfect proxy reward function leads to poor performance according to the true reward function.\" A proxy is considered \"unhackable\" when \"increasing the expected proxy return can never decrease the expected true return.\"\n\n## Key Theorem on Proxy Optimization\n\nThe central finding demonstrates a strong constraint: **for the full set of stochastic policies, two reward functions can only be unhackable if one remains constant.** This reveals that yes, optimizing a proxy reward can decrease true reward performance under most realistic conditions.\n\n## Unhackability and Auxiliary Objectives\n\nThe unhackability condition indicates a fundamental tension in AI alignment. While narrower reward functions or simplified distinctions might intuitively seem safer, the paper shows this approach \"is usually not the case.\" The research uncovers \"a tension between using reward functions to specify narrow tasks and aligning AI systems with human values,\" suggesting that auxiliary objectives cannot easily solve reward specification problems through simplification alone.",
    "durationMs": 4822,
    "url": "https://arxiv.org/abs/2209.13085"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-14T02:06:03.291Z_

<details><summary>↩ Tool result · `toolu_01RAfNWwkYJpfC8YAgqyEwJx`</summary>

```text
Web search results for query: "ForkMerge "negative transfer" auxiliary task learning NeurIPS 2023 Zheng Ge Long"

Links: [{"title":"NeurIPS Poster ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning","url":"https://neurips.cc/virtual/2023/poster/70098"},{"title":"GitHub - thuml/ForkMerge: Code release of paper \"ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning\" (NeurIPS 2023)","url":"https://github.com/thuml/ForkMerge"},{"title":"[2301.12618] ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning","url":"https://arxiv.org/abs/2301.12618"},{"title":"ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning","url":"https://proceedings.neurips.cc//paper_files/paper/2023/hash/60f9118a849e8e9a0c67e2a36ad80ebf-Abstract-Conference.html"},{"title":"ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning | OpenReview","url":"https://openreview.net/forum?id=vZHk1QlBQW"},{"title":"[Quick Review] ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning","url":"https://liner.com/review/forkmerge-mitigating-negative-transfer-in-auxiliarytask-learning"},{"title":"dblp: ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning.","url":"https://dblp.org/rec/conf/nips/JiangCPWL0L23.html"},{"title":"Releases · thuml/ForkMerge","url":"https://github.com/thuml/ForkMerge/releases"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=ForkMerge:+Mitigating+Negative+Transfer+in+Auxiliary-Task+Learning."},{"title":"ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning","url":"https://ise.thss.tsinghua.edu.cn/~mlong/doc/ForkMerge-nips23.pdf"}]

Based on the search results, I found information about the ForkMerge paper presented at NeurIPS 2023:

ForkMerge addresses Auxiliary-Task Learning (ATL), which aims to improve the performance of the target task by leveraging knowledge from related tasks, but occasionally learning multiple tasks simultaneously results in negative transfer—lower accuracy than learning only the target task.

ForkMerge is a novel approach that periodically forks the model into multiple branches, automatically searches the varying task weights by minimizing target validation errors, and dynamically merges all branches to filter out detrimental task-parameter updates.

On a series of auxiliary-task learning benchmarks, ForkMerge outperforms existing methods and effectively mitigates negative transfer.

Regarding the authors, the paper was authored by Junguang Jiang, Baixu Chen, Junwei Pan, Ximei Wang, Dapeng Liu, Jie Jiang, and Mingsheng Long. The name "Zheng Ge Long" from your query does not appear in the search results; "Mingsheng Long" is listed as one of the authors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "86b653b3-d3ae-4b66-a6ab-6194e04e0e7e",
  "tool_use_result": {
    "query": "ForkMerge \"negative transfer\" auxiliary task learning NeurIPS 2023 Zheng Ge Long",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NdukKvZsmaVaMheTtgNTgf",
        "content": [
          {
            "title": "NeurIPS Poster ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning",
            "url": "https://neurips.cc/virtual/2023/poster/70098"
          },
          {
            "title": "GitHub - thuml/ForkMerge: Code release of paper \"ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning\" (NeurIPS 2023)",
            "url": "https://github.com/thuml/ForkMerge"
          },
          {
            "title": "[2301.12618] ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning",
            "url": "https://arxiv.org/abs/2301.12618"
          },
          {
            "title": "ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning",
            "url": "https://proceedings.neurips.cc//paper_files/paper/2023/hash/60f9118a849e8e9a0c67e2a36ad80ebf-Abstract-Conference.html"
          },
          {
            "title": "ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning | OpenReview",
            "url": "https://openreview.net/forum?id=vZHk1QlBQW"
          },
          {
            "title": "[Quick Review] ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning",
            "url": "https://liner.com/review/forkmerge-mitigating-negative-transfer-in-auxiliarytask-learning"
          },
          {
            "title": "dblp: ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning.",
            "url": "https://dblp.org/rec/conf/nips/JiangCPWL0L23.html"
          },
          {
            "title": "Releases · thuml/ForkMerge",
            "url": "https://github.com/thuml/ForkMerge/releases"
          },
          {
            "title": "Google Scholar",
            "url": "https://scholar.google.com/scholar?q=ForkMerge:+Mitigating+Negative+Transfer+in+Auxiliary-Task+Learning."
          },
          {
            "title": "ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning",
            "url": "https://ise.thss.tsinghua.edu.cn/~mlong/doc/ForkMerge-nips23.pdf"
          }
        ]
      },
      "Based on the search results, I found information about the ForkMerge paper presented at NeurIPS 2023:\n\nForkMerge addresses Auxiliary-Task Learning (ATL), which aims to improve the performance of the target task by leveraging knowledge from related tasks, but occasionally learning multiple tasks simultaneously results in negative transfer—lower accuracy than learning only the target task.\n\nForkMerge is a novel approach that periodically forks the model into multiple branches, automatically searches the varying task weights by minimizing target validation errors, and dynamically merges all branches to filter out detrimental task-parameter updates.\n\nOn a series of auxiliary-task learning benchmarks, ForkMerge outperforms existing methods and effectively mitigates negative transfer.\n\nRegarding the authors, the paper was authored by Junguang Jiang, Baixu Chen, Junwei Pan, Ximei Wang, Dapeng Liu, Jie Jiang, and Mingsheng Long. The name \"Zheng Ge Long\" from your query does not appear in the search results; \"Mingsheng Long\" is listed as one of the authors."
    ],
    "durationSeconds": 5.482295201000001
  }
}
```

</details>

---

### Assistant

_source line 52_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to compile the literature report. Let me also fetch the ForkMerge paper abstract for complete details.

Let me organize the 5 most relevant papers:

1. **Gao et al. (2024) "On Designing Effective RL Reward at Training Time for LLM Reasoning"** - Most directly relevant. They find that process rewards (PRM) can HURT RL training compared to simple outcome (success) reward. Solution: clipping and delta reward refinement.

2. **Ye et al. (2025) "Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"** - PROF framework. Process rewards frequently suffer from inaccuracies and susceptibility to reward hacking. 

The key insight here is using consistency filtering between process and outcome rewards to address these issues.

3. **Moskovitz et al. (2023/2024) "Confronting Reward Model Overoptimization with Constrained RLHF"** - First study on overoptimization in composite reward models. Shows that correlation between component rewards affects degradation points. Solution: constrained RL with Lagrange multipliers.

4. **Skalse et al. (2022) "Defining and Characterizing Reward Hacking"** - Theoretical foundation: for stochastic policies, any non-constant proxy reward can decrease true reward when optimized. This formally explains why STA reward can hurt prove_rate.

5. **Reza** - Still gathering the final paper details.

Actually, I should pull the complete literature map to ensure I'm capturing all the relevant work properly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "53fc15da-8e25-4572-82de-df2808f097ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BYGzhGMitt18z5cKb4o8T5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3760,
      "cache_read_input_tokens": 42290,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3760
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

_source line 53_

Now let me get the full literature map and then write the report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "e5cc7f9c-af99-4f61-91dc-a712f0084206",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BYGzhGMitt18z5cKb4o8T5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3760,
      "cache_read_input_tokens": 42290,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3760
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

_source line 54_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QUmQ9jvcXabzRJHc95nT9C`</summary>

```json
{
  "project": "solver-trace-ablation",
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
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "9fc93d72-764b-42a8-bd89-204926836bf0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BYGzhGMitt18z5cKb4o8T5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3760,
      "cache_read_input_tokens": 42290,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3760
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

_source line 55 · 2026-05-14T02:06:22.280Z_

<details><summary>↩ Tool result · `toolu_01QUmQ9jvcXabzRJHc95nT9C`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\", \"content\": \"# Literature Map for Solver Trace Ablation (STA)\\n# Categories:\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\n#   2. reward-shaping: Reward shaping for code/formal verification\\n#   3. mutation-testing: Mutation testing in software engineering\\n#   4. intensional-analysis: Intensional program analysis\\n#   5. reward-hacking: Reward hacking / overoptimization\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\n\\npapers:\\n\\n  # ============================================================\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\n  # ============================================================\\n\\n  - id: deepseek-r1\\n    title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n    authors: \\\"DeepSeek-AI\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2501.12948 / Nature 2025\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\n      intensional structural reward for neurosymbolic formalization.\\n    key_finding: >\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\n      showing emergent chain-of-thought reasoning from RL alone.\\n\\n  - id: deepseekmath\\n    title: \\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\"\\n    authors: \\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2402.03300\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\\n      used in STA training. GRPO eliminates the critic model by estimating\\n      baselines from group scores.\\n    key_finding: >\\n      GRPO matches PPO performance while significantly reducing training\\n      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.\\n\\n  - id: logic-rl\\n    title: \\\"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\\\"\\n    authors: \\\"Xian et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.14768\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic\\n      logic puzzles. Closest competitor to STA's approach of RL for logical\\n      formalization, though Logic-RL uses extensional (answer-correctness)\\n      rewards rather than STA's intensional structural rewards.\\n    key_finding: >\\n      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;\\n      rule-based reward design is critical for RL-based logical reasoning.\\n\\n  - id: mellgren-prolog-grpo\\n    title: \\\"Training Language Models to Use Prolog as a Tool\\\"\\n    authors: \\\"Niklas Mellgren\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2512.07407\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,\\n      directly comparable to STA's approach of GRPO-training a formalizer.\\n      Key difference: uses pass/fail reward vs STA's structural ISR.\\n    key_finding: >\\n      GRPO is effective for teaching small LLMs to use Prolog as a tool\\n      for logical and mathematical reasoning.\\n\\n  - id: satlm\\n    title: \\\"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\\\"\\n    authors: \\\"Xi Ye et al.\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023\\\"\\n    category: neurosymbolic-rl\\n    role: background\\n    relevance: >\\n      Neurosymbolic approach where LLM generates declarative specifications\\n      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)\\n      but uses prompting, not RL training.\\n    key_finding: >\\n      Declarative formulation outperforms imperative program-aided LMs by 23%\\n      on GSM; achieves SoTA on LSAT and BoardgameQA.\\n\\n  # ============================================================\\n  # Category 2: Reward shaping for code/formal verification\\n  # ============================================================\\n\\n  - id: lightman-verify-step\\n    title: \\\"Let's Verify Step by Step\\\"\\n    authors: \\\"Hunter Lightman, Vineet Kosaraju, Yura Burda, et al.\\\"\\n    year: 2023\\n    venue: \\\"arXiv 2305.20050 / ICLR 2024\\\"\\n    category: reward-shaping\\n    role: method-component\\n    relevance: >\\n      Establishes that process supervision (step-level reward) outperforms\\n      outcome supervision (final-answer reward) for reasoning. STA's ISR\\n      is analogous: it provides structural process-level signal about which\\n      components of a formalization matter, rather than just pass/fail.\\n    key_finding: >\\n      Process-supervised reward model achieves 78% on MATH, significantly\\n      outperforming outcome-supervised models. Released PRM800K dataset.\\n\\n  - id: reward-shaping-rlhf\\n    title: \\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\"\\n    authors: \\\"Jiayi Fu, Xuandong Zhao, Chengyuan Yao, et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.18770\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Studies reward shaping design principles for RLHF: bounded rewards and\\n      rapid-then-convergent growth. STA's ISR follows these principles\\n      naturally since structural necessity scores are bounded [0,1].\\n    key_finding: >\\n      Two key reward shaping principles: (1) bounded RL reward, (2) rapid\\n      initial growth with gradual convergence. PAR method achieves 5%+\\n      win rate improvement on AlpacaEval 2.0.\\n\\n  - id: rlvr-reasoning\\n    title: \\\"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2506.14245\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize\\n      reasoning. STA argues that for neurosymbolic formalization, binary reward\\n      is insufficient and structural reward is needed to avoid reward hacking.\\n    key_finding: >\\n      RLVR with binary verification implicitly teaches correct reasoning\\n      strategies, not just answer matching.\\n\\n  - id: rubric-grpo\\n    title: \\\"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2605.08061\\\"\\n    category: reward-shaping\\n    role: direct-competitor\\n    relevance: >\\n      Uses structured rubric-based rewards with GRPO, similar in spirit to\\n      STA's structured ISR. Key difference: rubric rewards come from LLM\\n      judges, while ISR comes from solver-based mutation testing.\\n    key_finding: >\\n      Structured multi-dimensional reward signals improve GRPO training\\n      generalization compared to scalar rewards.\\n\\n  # ============================================================\\n  # Category 3: Mutation testing in software engineering\\n  # ============================================================\\n\\n  - id: demillo1978\\n    title: \\\"Hints on Test Data Selection: Help for the Practicing Programmer\\\"\\n    authors: \\\"Richard A. DeMillo, Richard J. Lipton, Frederick G. Sayward\\\"\\n    year: 1978\\n    venue: \\\"Computer 11(4):34-43\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Foundational paper introducing mutation testing. STA's component\\n      necessity testing directly extends this idea: instead of mutating\\n      source code to test test suites, STA mutates logical formulas\\n      to test component necessity for solver success.\\n    key_finding: >\\n      Introduced mutation testing and the coupling effect hypothesis:\\n      tests that detect simple faults also detect complex faults.\\n\\n  - id: offutt-coupling\\n    title: \\\"Investigations of the Software Testing Coupling Effect\\\"\\n    authors: \\\"A. Jefferson Offutt\\\"\\n    year: 1992\\n    venue: \\\"ACM TOSEM 1(1):5-20\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Empirically validates the coupling effect hypothesis that underpins\\n      mutation testing. STA's single-component ablation is analogous to\\n      first-order mutation; the coupling effect suggests this suffices.\\n    key_finding: >\\n      Test data killing all first-order mutants killed >99% of second-\\n      and third-order mutants, validating the coupling effect.\\n\\n  - id: jia-harman-survey\\n    title: \\\"An Analysis and Survey of the Development of Mutation Testing\\\"\\n    authors: \\\"Yue Jia, Mark Harman\\\"\\n    year: 2011\\n    venue: \\\"IEEE TSE 37(5):649-678\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Comprehensive survey of mutation testing covering three decades of\\n      development. Provides theoretical and practical foundation for STA's\\n      adaptation of mutation testing to logical formulas.\\n    key_finding: >\\n      Systematic classification of mutation operators, cost reduction\\n      techniques, and equivalence problem -- all relevant to STA's design\\n      of clause-level ablation operators.\\n\\n  - id: just-mutants-real-faults\\n    title: \\\"Are Mutants a Valid Substitute for Real Faults in Software Testing?\\\"\\n    authors: \\\"Rene Just, Darioush Jalali, Laura Inozemtseva, et al.\\\"\\n    year: 2014\\n    venue: \\\"FSE 2014\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Validates that mutation testing (structural/intensional analysis of\\n      program adequacy) correlates with real fault detection. Supports STA's\\n      premise that structural analysis of formalization components provides\\n      meaningful signal about formalization quality.\\n    key_finding: >\\n      Mutant detection is statistically correlated with real fault detection,\\n      and mutation score is a better predictor of test effectiveness than\\n      code coverage.\\n\\n  - id: llmorpheus\\n    title: \\\"LLMorpheus: Mutation Testing Using Large Language Models\\\"\\n    authors: \\\"Frank Tip, Jon Bell, et al.\\\"\\n    year: 2025\\n    venue: \\\"IEEE TSE 2025\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Uses LLMs to generate realistic code mutants beyond traditional\\n      mutation operators. Shows mutation testing evolving toward\\n      ML-integrated approaches, validating STA's cross-pollination\\n      of mutation testing ideas into ML training.\\n    key_finding: >\\n      LLM-generated mutants simulate real bugs that rule-based operators\\n      cannot produce, improving mutation testing realism.\\n\\n  - id: mutation-guided-meta\\n    title: \\\"Mutation-Guided LLM-based Test Generation at Meta\\\"\\n    authors: \\\"Christopher Foster et al.\\\"\\n    year: 2025\\n    venue: \\\"FSE 2025\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Industrial application of mutation-guided LLM test generation at\\n      Meta. Demonstrates that mutation analysis can guide LLM behavior\\n      in production -- analogous to how STA uses mutation (ablation) to\\n      guide GRPO reward signal.\\n    key_finding: >\\n      Mutation-guided approach generates tests that kill significantly\\n      more mutants than unguided LLM test generation at Meta scale.\\n\\n  - id: mutation-consistency-llm\\n    title: \\\"Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs\\\"\\n    authors: \\\"Various\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2401.05940\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Uses code mutations to evaluate LLM code understanding consistency.\\n      Conceptually related to STA: both use systematic code/formula\\n      mutations to assess model capabilities.\\n    key_finding: >\\n      LLMs show significant inconsistency when evaluated on mutated code\\n      variants, suggesting superficial pattern matching.\\n\\n  # ============================================================\\n  # Category 4: Intensional program analysis\\n  # ============================================================\\n\\n  - id: deepmutation\\n    title: \\\"A Probabilistic Framework for Mutation Testing in Deep Neural Networks\\\"\\n    authors: \\\"Various\\\"\\n    year: 2023\\n    venue: \\\"Information and Software Technology 2023\\\"\\n    category: intensional-analysis\\n    role: background\\n    relevance: >\\n      Extends mutation testing to DNN testing with probabilistic mutation\\n      operators. Parallel to STA's extension of mutation testing from\\n      traditional programs to logical formulas.\\n    key_finding: >\\n      Probabilistic mutation framework enables meaningful test adequacy\\n      assessment for neural networks through structural perturbation.\\n\\n  # ============================================================\\n  # Category 5: Reward hacking / overoptimization\\n  # ============================================================\\n\\n  - id: inform-reward-hacking\\n    title: \\\"InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling\\\"\\n    authors: \\\"Various\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS 2024\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Proposes information-bottleneck approach to detect and mitigate reward\\n      hacking. STA's ISR addresses the same problem differently: by grounding\\n      reward in verifiable structural properties (component necessity), it\\n      reduces the attack surface for reward hacking.\\n    key_finding: >\\n      Variational information bottleneck filters irrelevant features from\\n      reward model; Cluster Separation Index detects reward overoptimization.\\n\\n  - id: mo-grpo\\n    title: \\\"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\\\"\\n    authors: \\\"CyberAgent AI Lab\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2509.22047\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Directly addresses GRPO reward hacking in multi-objective settings.\\n      STA's ISR can be viewed as adding a structural objective to the\\n      correctness objective, making MO-GRPO's insights directly applicable.\\n    key_finding: >\\n      Standard GRPO normalizes after summing rewards, allowing high-variance\\n      objectives to dominate. MO-GRPO equalizes scales before aggregation.\\n\\n  - id: reward-hacking-survey\\n    title: \\\"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\\\"\\n    authors: \\\"Various\\\"\\n    year: 2026\\n    venue: \\\"arXiv 2604.13602\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Comprehensive survey of reward hacking mechanisms in the LLM era.\\n      Provides theoretical framework for understanding why STA's structural\\n      reward is more robust than pure outcome-based reward.\\n    key_finding: >\\n      Reward hacking manifests through specification gaming, reward model\\n      exploitation, and emergent misalignment; structural verification\\n      rewards are more robust than learned reward models.\\n\\n  - id: energy-loss-reward-hacking\\n    title: \\\"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"ICML 2025\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Identifies energy loss in LLM final layer as an indicator of reward\\n      hacking during RL. Provides complementary diagnostic to STA's\\n      structural reward approach.\\n    key_finding: >\\n      Energy loss in the final layer increases during RL and excessive\\n      increase characterizes reward hacking; EPPO algorithm penalizes\\n      this to mitigate hacking.\\n\\n  # ============================================================\\n  # Category 6: FOL/Prolog formalization with LLMs\\n  # ============================================================\\n\\n  - id: folio\\n    title: \\\"FOLIO: Natural Language Reasoning with First-Order Logic\\\"\\n    authors: \\\"Simeng Han et al.\\\"\\n    year: 2022\\n    venue: \\\"arXiv 2209.00840 / EMNLP 2024\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Primary FOL reasoning benchmark. STA uses FOLIO-style NL->FOL\\n      formalization as the target task for GRPO training. FOLIO's\\n      expert-annotated FOL annotations serve as reference formalizations.\\n    key_finding: >\\n      1,430 NL-FOL paired examples with reasoning depths up to 5+;\\n      GPT-4 still struggles on the hardest examples.\\n\\n  - id: proofwriter\\n    title: \\\"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language\\\"\\n    authors: \\\"Oyvind Tafjord, Bhavana Dalvi, Peter Clark\\\"\\n    year: 2021\\n    venue: \\\"Findings of ACL-IJCNLP 2021\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Source dataset for STA's training data. ProofWriter provides\\n      rule-based logical reasoning problems in natural language that\\n      STA uses for training formalizer models.\\n    key_finding: >\\n      Generative model can reliably produce implications and proofs;\\n      accuracy exceeds prior methods by 9% and generalizes to unseen\\n      proof depths.\\n\\n  - id: logic-lm\\n    title: \\\"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\\\"\\n    authors: \\\"Liangming Pan, Alon Albalak, Xinyi Wang, William Wang\\\"\\n    year: 2023\\n    venue: \\\"Findings of EMNLP 2023\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      LLM->symbolic solver pipeline for logical reasoning, directly\\n      comparable to STA's formalizer->Prolog solver pipeline. Key\\n      difference: Logic-LM uses prompting, STA uses GRPO training.\\n    key_finding: >\\n      LLM+solver achieves 39.2% improvement over LLM-alone on logical\\n      reasoning benchmarks including ProofWriter and FOLIO.\\n\\n  - id: linc\\n    title: \\\"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers\\\"\\n    authors: \\\"Theo X. Olausson, Alex Gu, Ben Lipkin, et al.\\\"\\n    year: 2023\\n    venue: \\\"EMNLP 2023\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      Neurosymbolic approach where LLM translates NL to FOL for theorem\\n      prover. Directly comparable to STA's NL->Prolog translation.\\n      LINC uses prompting-based approach; STA uses RL training.\\n    key_finding: >\\n      StarCoder+ (15.5B) with LINC outperforms GPT-3.5 and GPT-4 with\\n      CoT by 38% and 10% respectively on ProofWriter.\\n\\n  - id: fover\\n    title: \\\"FoVer: First-Order Logic Verification for Natural Language Reasoning\\\"\\n    authors: \\\"Yu Pei, Yongping Du, Xingnan Jin\\\"\\n    year: 2025\\n    venue: \\\"TACL 13:1340-1359\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      Uses LLM->FOL->Z3 pipeline for verifying NL reasoning correctness.\\n      Similar to STA's verification pipeline but focuses on post-hoc\\n      verification rather than training reward signal.\\n    key_finding: >\\n      FOL verification via Z3 significantly outperforms existing methods\\n      on ProofWriter and FOLIO benchmarks.\\n\\n  - id: lorp\\n    title: \\\"LoRP: LLM-based Logical Reasoning via Prolog\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"Knowledge-Based Systems 2025\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      LLM->Prolog pipeline with FOL-to-Prolog translation mechanism.\\n      Closest to STA's formalization target (Prolog), though LoRP\\n      uses prompting while STA uses GRPO training with structural reward.\\n    key_finding: >\\n      Systematic FOL-to-Prolog translation extends Prolog expressiveness;\\n      achieves SoTA accuracy on logical reasoning with three-vote majority.\\n\\n  - id: nl2fol\\n    title: \\\"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection\\\"\\n    authors: \\\"Lalwani, Kim, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2405.02318\\\"\\n    category: fol-formalization\\n    role: background\\n    relevance: >\\n      Step-by-step NL->FOL translation using LLMs with SMT solver\\n      verification. Demonstrates the NL->formal logic pipeline that\\n      STA aims to improve via RL training.\\n    key_finding: >\\n      Neurosymbolic NL2FOL achieves 78% F1 on LOGIC dataset and\\n      generalizes to LogicClimate (80% F1), outperforming supervised\\n      models by 21%.\\n\\n  - id: logica2\\n    title: \\\"LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: \\\"IEEE/ACM TASLP 2023\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Logical reasoning evaluation benchmark derived from Chinese civil\\n      service exams. Provides supplementary evaluation for STA's\\n      formalization capabilities.\\n    key_finding: >\\n      8,678 multiple-choice questions covering categorical, disjunctive,\\n      and conditional reasoning; widely used LLM benchmark.\\n\", \"total_chars\": 20468, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "294dbb91-b5a5-41a2-b7f2-8e261197b8fa",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\\\", \\\"content\\\": \\\"# Literature Map for Solver Trace Ablation (STA)\\\\n# Categories:\\\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\\\n#   2. reward-shaping: Reward shaping for code/formal verification\\\\n#   3. mutation-testing: Mutation testing in software engineering\\\\n#   4. intensional-analysis: Intensional program analysis\\\\n#   5. reward-hacking: Reward hacking / overoptimization\\\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\\\n\\\\npapers:\\\\n\\\\n  # ============================================================\\\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\\\n  # ============================================================\\\\n\\\\n  - id: deepseek-r1\\\\n    title: \\\\\\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"DeepSeek-AI\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2501.12948 / Nature 2025\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: method-component\\\\n    relevance: >\\\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\\\n      intensional structural reward for neurosymbolic formalization.\\\\n    key_finding: >\\\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\\\n      showing emergent chain-of-thought reasoning from RL alone.\\\\n\\\\n  - id: deepseekmath\\\\n    title: \\\\\\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2402.03300\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: method-component\\\\n    relevance: >\\\\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\\\\n      used in STA training. GRPO eliminates the critic model by estimating\\\\n      baselines from group scores.\\\\n    key_finding: >\\\\n      GRPO matches PPO performance while significantly reducing training\\\\n      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.\\\\n\\\\n  - id: logic-rl\\\\n    title: \\\\\\\"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Xian et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2502.14768\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic\\\\n      logic puzzles. Closest competitor to STA's approach of RL for logical\\\\n      formalization, though Logic-RL uses extensional (answer-correctness)\\\\n      rewards rather than STA's intensional structural rewards.\\\\n    key_finding: >\\\\n      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;\\\\n      rule-based reward design is critical for RL-based logical reasoning.\\\\n\\\\n  - id: mellgren-prolog-grpo\\\\n    title: \\\\\\\"Training Language Models to Use Prolog as a Tool\\\\\\\"\\\\n    authors: \\\\\\\"Niklas Mellgren\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2512.07407\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,\\\\n      directly comparable to STA's approach of GRPO-training a formalizer.\\\\n      Key difference: uses pass/fail reward vs STA's structural ISR.\\\\n    key_finding: >\\\\n      GRPO is effective for teaching small LLMs to use Prolog as a tool\\\\n      for logical and mathematical reasoning.\\\\n\\\\n  - id: satlm\\\\n    title: \\\\\\\"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\\\\\\\"\\\\n    authors: \\\\\\\"Xi Ye et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"NeurIPS 2023\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: background\\\\n    relevance: >\\\\n      Neurosymbolic approach where LLM generates declarative specifications\\\\n      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)\\\\n      but uses prompting, not RL training.\\\\n    key_finding: >\\\\n      Declarative formulation outperforms imperative program-aided LMs by 23%\\\\n      on GSM; achieves SoTA on LSAT and BoardgameQA.\\\\n\\\\n  # ============================================================\\\\n  # Category 2: Reward shaping for code/formal verification\\\\n  # ============================================================\\\\n\\\\n  - id: lightman-verify-step\\\\n    title: \\\\\\\"Let's Verify Step by Step\\\\\\\"\\\\n    authors: \\\\\\\"Hunter Lightman, Vineet Kosaraju, Yura Burda, et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"arXiv 2305.20050 / ICLR 2024\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: method-component\\\\n    relevance: >\\\\n      Establishes that process supervision (step-level reward) outperforms\\\\n      outcome supervision (final-answer reward) for reasoning. STA's ISR\\\\n      is analogous: it provides structural process-level signal about which\\\\n      components of a formalization matter, rather than just pass/fail.\\\\n    key_finding: >\\\\n      Process-supervised reward model achieves 78% on MATH, significantly\\\\n      outperforming outcome-supervised models. Released PRM800K dataset.\\\\n\\\\n  - id: reward-shaping-rlhf\\\\n    title: \\\\\\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\\\\\"\\\\n    authors: \\\\\\\"Jiayi Fu, Xuandong Zhao, Chengyuan Yao, et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2502.18770\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      Studies reward shaping design principles for RLHF: bounded rewards and\\\\n      rapid-then-convergent growth. STA's ISR follows these principles\\\\n      naturally since structural necessity scores are bounded [0,1].\\\\n    key_finding: >\\\\n      Two key reward shaping principles: (1) bounded RL reward, (2) rapid\\\\n      initial growth with gradual convergence. PAR method achieves 5%+\\\\n      win rate improvement on AlpacaEval 2.0.\\\\n\\\\n  - id: rlvr-reasoning\\\\n    title: \\\\\\\"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2506.14245\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize\\\\n      reasoning. STA argues that for neurosymbolic formalization, binary reward\\\\n      is insufficient and structural reward is needed to avoid reward hacking.\\\\n    key_finding: >\\\\n      RLVR with binary verification implicitly teaches correct reasoning\\\\n      strategies, not just answer matching.\\\\n\\\\n  - id: rubric-grpo\\\\n    title: \\\\\\\"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2605.08061\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Uses structured rubric-based rewards with GRPO, similar in spirit to\\\\n      STA's structured ISR. Key difference: rubric rewards come from LLM\\\\n      judges, while ISR comes from solver-based mutation testing.\\\\n    key_finding: >\\\\n      Structured multi-dimensional reward signals improve GRPO training\\\\n      generalization compared to scalar rewards.\\\\n\\\\n  # ============================================================\\\\n  # Category 3: Mutation testing in software engineering\\\\n  # ============================================================\\\\n\\\\n  - id: demillo1978\\\\n    title: \\\\\\\"Hints on Test Data Selection: Help for the Practicing Programmer\\\\\\\"\\\\n    authors: \\\\\\\"Richard A. DeMillo, Richard J. Lipton, Frederick G. Sayward\\\\\\\"\\\\n    year: 1978\\\\n    venue: \\\\\\\"Computer 11(4):34-43\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Foundational paper introducing mutation testing. STA's component\\\\n      necessity testing directly extends this idea: instead of mutating\\\\n      source code to test test suites, STA mutates logical formulas\\\\n      to test component necessity for solver success.\\\\n    key_finding: >\\\\n      Introduced mutation testing and the coupling effect hypothesis:\\\\n      tests that detect simple faults also detect complex faults.\\\\n\\\\n  - id: offutt-coupling\\\\n    title: \\\\\\\"Investigations of the Software Testing Coupling Effect\\\\\\\"\\\\n    authors: \\\\\\\"A. Jefferson Offutt\\\\\\\"\\\\n    year: 1992\\\\n    venue: \\\\\\\"ACM TOSEM 1(1):5-20\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Empirically validates the coupling effect hypothesis that underpins\\\\n      mutation testing. STA's single-component ablation is analogous to\\\\n      first-order mutation; the coupling effect suggests this suffices.\\\\n    key_finding: >\\\\n      Test data killing all first-order mutants killed >99% of second-\\\\n      and third-order mutants, validating the coupling effect.\\\\n\\\\n  - id: jia-harman-survey\\\\n    title: \\\\\\\"An Analysis and Survey of the Development of Mutation Testing\\\\\\\"\\\\n    authors: \\\\\\\"Yue Jia, Mark Harman\\\\\\\"\\\\n    year: 2011\\\\n    venue: \\\\\\\"IEEE TSE 37(5):649-678\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Comprehensive survey of mutation testing covering three decades of\\\\n      development. Provides theoretical and practical foundation for STA's\\\\n      adaptation of mutation testing to logical formulas.\\\\n    key_finding: >\\\\n      Systematic classification of mutation operators, cost reduction\\\\n      techniques, and equivalence problem -- all relevant to STA's design\\\\n      of clause-level ablation operators.\\\\n\\\\n  - id: just-mutants-real-faults\\\\n    title: \\\\\\\"Are Mutants a Valid Substitute for Real Faults in Software Testing?\\\\\\\"\\\\n    authors: \\\\\\\"Rene Just, Darioush Jalali, Laura Inozemtseva, et al.\\\\\\\"\\\\n    year: 2014\\\\n    venue: \\\\\\\"FSE 2014\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Validates that mutation testing (structural/intensional analysis of\\\\n      program adequacy) correlates with real fault detection. Supports STA's\\\\n      premise that structural analysis of formalization components provides\\\\n      meaningful signal about formalization quality.\\\\n    key_finding: >\\\\n      Mutant detection is statistically correlated with real fault detection,\\\\n      and mutation score is a better predictor of test effectiveness than\\\\n      code coverage.\\\\n\\\\n  - id: llmorpheus\\\\n    title: \\\\\\\"LLMorpheus: Mutation Testing Using Large Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Frank Tip, Jon Bell, et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"IEEE TSE 2025\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Uses LLMs to generate realistic code mutants beyond traditional\\\\n      mutation operators. Shows mutation testing evolving toward\\\\n      ML-integrated approaches, validating STA's cross-pollination\\\\n      of mutation testing ideas into ML training.\\\\n    key_finding: >\\\\n      LLM-generated mutants simulate real bugs that rule-based operators\\\\n      cannot produce, improving mutation testing realism.\\\\n\\\\n  - id: mutation-guided-meta\\\\n    title: \\\\\\\"Mutation-Guided LLM-based Test Generation at Meta\\\\\\\"\\\\n    authors: \\\\\\\"Christopher Foster et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"FSE 2025\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Industrial application of mutation-guided LLM test generation at\\\\n      Meta. Demonstrates that mutation analysis can guide LLM behavior\\\\n      in production -- analogous to how STA uses mutation (ablation) to\\\\n      guide GRPO reward signal.\\\\n    key_finding: >\\\\n      Mutation-guided approach generates tests that kill significantly\\\\n      more mutants than unguided LLM test generation at Meta scale.\\\\n\\\\n  - id: mutation-consistency-llm\\\\n    title: \\\\\\\"Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2401.05940\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Uses code mutations to evaluate LLM code understanding consistency.\\\\n      Conceptually related to STA: both use systematic code/formula\\\\n      mutations to assess model capabilities.\\\\n    key_finding: >\\\\n      LLMs show significant inconsistency when evaluated on mutated code\\\\n      variants, suggesting superficial pattern matching.\\\\n\\\\n  # ============================================================\\\\n  # Category 4: Intensional program analysis\\\\n  # ============================================================\\\\n\\\\n  - id: deepmutation\\\\n    title: \\\\\\\"A Probabilistic Framework for Mutation Testing in Deep Neural Networks\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"Information and Software Technology 2023\\\\\\\"\\\\n    category: intensional-analysis\\\\n    role: background\\\\n    relevance: >\\\\n      Extends mutation testing to DNN testing with probabilistic mutation\\\\n      operators. Parallel to STA's extension of mutation testing from\\\\n      traditional programs to logical formulas.\\\\n    key_finding: >\\\\n      Probabilistic mutation framework enables meaningful test adequacy\\\\n      assessment for neural networks through structural perturbation.\\\\n\\\\n  # ============================================================\\\\n  # Category 5: Reward hacking / overoptimization\\\\n  # ============================================================\\\\n\\\\n  - id: inform-reward-hacking\\\\n    title: \\\\\\\"InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"NeurIPS 2024\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: background\\\\n    relevance: >\\\\n      Proposes information-bottleneck approach to detect and mitigate reward\\\\n      hacking. STA's ISR addresses the same problem differently: by grounding\\\\n      reward in verifiable structural properties (component necessity), it\\\\n      reduces the attack surface for reward hacking.\\\\n    key_finding: >\\\\n      Variational information bottleneck filters irrelevant features from\\\\n      reward model; Cluster Separation Index detects reward overoptimization.\\\\n\\\\n  - id: mo-grpo\\\\n    title: \\\\\\\"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\\\\\\\"\\\\n    authors: \\\\\\\"CyberAgent AI Lab\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2509.22047\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: background\\\\n    relevance: >\\\\n      Directly addresses GRPO reward hacking in multi-objective settings.\\\\n      STA's ISR can be viewed as adding a structural objective to the\\\\n      correctness objective, making MO-GRPO's insights directly applicable.\\\\n    key_finding: >\\\\n      Standard GRPO normalizes after summing rewards, allowing high-variance\\\\n      objectives to dominate. MO-GRPO equalizes scales before aggregation.\\\\n\\\\n  - id: reward-hacking-survey\\\\n    title: \\\\\\\"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv 2604.13602\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: background\\\\n    relevance: >\\\\n      Comprehensive survey of reward hacking mechanisms in the LLM era.\\\\n      Provides theoretical framework for understanding why STA's structural\\\\n      reward is more robust than pure outcome-based reward.\\\\n    key_finding: >\\\\n      Reward hacking manifests through specification gaming, reward model\\\\n      exploitation, and emergent misalignment; structural verification\\\\n      rewards are more robust than learned reward models.\\\\n\\\\n  - id: energy-loss-reward-hacking\\\\n    title: \\\\\\\"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"ICML 2025\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: background\\\\n    relevance: >\\\\n      Identifies energy loss in LLM final layer as an indicator of reward\\\\n      hacking during RL. Provides complementary diagnostic to STA's\\\\n      structural reward approach.\\\\n    key_finding: >\\\\n      Energy loss in the final layer increases during RL and excessive\\\\n      increase characterizes reward hacking; EPPO algorithm penalizes\\\\n      this to mitigate hacking.\\\\n\\\\n  # ============================================================\\\\n  # Category 6: FOL/Prolog formalization with LLMs\\\\n  # ============================================================\\\\n\\\\n  - id: folio\\\\n    title: \\\\\\\"FOLIO: Natural Language Reasoning with First-Order Logic\\\\\\\"\\\\n    authors: \\\\\\\"Simeng Han et al.\\\\\\\"\\\\n    year: 2022\\\\n    venue: \\\\\\\"arXiv 2209.00840 / EMNLP 2024\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: evaluation\\\\n    relevance: >\\\\n      Primary FOL reasoning benchmark. STA uses FOLIO-style NL->FOL\\\\n      formalization as the target task for GRPO training. FOLIO's\\\\n      expert-annotated FOL annotations serve as reference formalizations.\\\\n    key_finding: >\\\\n      1,430 NL-FOL paired examples with reasoning depths up to 5+;\\\\n      GPT-4 still struggles on the hardest examples.\\\\n\\\\n  - id: proofwriter\\\\n    title: \\\\\\\"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language\\\\\\\"\\\\n    authors: \\\\\\\"Oyvind Tafjord, Bhavana Dalvi, Peter Clark\\\\\\\"\\\\n    year: 2021\\\\n    venue: \\\\\\\"Findings of ACL-IJCNLP 2021\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: evaluation\\\\n    relevance: >\\\\n      Source dataset for STA's training data. ProofWriter provides\\\\n      rule-based logical reasoning problems in natural language that\\\\n      STA uses for training formalizer models.\\\\n    key_finding: >\\\\n      Generative model can reliably produce implications and proofs;\\\\n      accuracy exceeds prior methods by 9% and generalizes to unseen\\\\n      proof depths.\\\\n\\\\n  - id: logic-lm\\\\n    title: \\\\\\\"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Liangming Pan, Alon Albalak, Xinyi Wang, William Wang\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"Findings of EMNLP 2023\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      LLM->symbolic solver pipeline for logical reasoning, directly\\\\n      comparable to STA's formalizer->Prolog solver pipeline. Key\\\\n      difference: Logic-LM uses prompting, STA uses GRPO training.\\\\n    key_finding: >\\\\n      LLM+solver achieves 39.2% improvement over LLM-alone on logical\\\\n      reasoning benchmarks including ProofWriter and FOLIO.\\\\n\\\\n  - id: linc\\\\n    title: \\\\\\\"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers\\\\\\\"\\\\n    authors: \\\\\\\"Theo X. Olausson, Alex Gu, Ben Lipkin, et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"EMNLP 2023\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Neurosymbolic approach where LLM translates NL to FOL for theorem\\\\n      prover. Directly comparable to STA's NL->Prolog translation.\\\\n      LINC uses prompting-based approach; STA uses RL training.\\\\n    key_finding: >\\\\n      StarCoder+ (15.5B) with LINC outperforms GPT-3.5 and GPT-4 with\\\\n      CoT by 38% and 10% respectively on ProofWriter.\\\\n\\\\n  - id: fover\\\\n    title: \\\\\\\"FoVer: First-Order Logic Verification for Natural Language Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Yu Pei, Yongping Du, Xingnan Jin\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"TACL 13:1340-1359\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Uses LLM->FOL->Z3 pipeline for verifying NL reasoning correctness.\\\\n      Similar to STA's verification pipeline but focuses on post-hoc\\\\n      verification rather than training reward signal.\\\\n    key_finding: >\\\\n      FOL verification via Z3 significantly outperforms existing methods\\\\n      on ProofWriter and FOLIO benchmarks.\\\\n\\\\n  - id: lorp\\\\n    title: \\\\\\\"LoRP: LLM-based Logical Reasoning via Prolog\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"Knowledge-Based Systems 2025\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      LLM->Prolog pipeline with FOL-to-Prolog translation mechanism.\\\\n      Closest to STA's formalization target (Prolog), though LoRP\\\\n      uses prompting while STA uses GRPO training with structural reward.\\\\n    key_finding: >\\\\n      Systematic FOL-to-Prolog translation extends Prolog expressiveness;\\\\n      achieves SoTA accuracy on logical reasoning with three-vote majority.\\\\n\\\\n  - id: nl2fol\\\\n    title: \\\\\\\"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection\\\\\\\"\\\\n    authors: \\\\\\\"Lalwani, Kim, et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2405.02318\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: background\\\\n    relevance: >\\\\n      Step-by-step NL->FOL translation using LLMs with SMT solver\\\\n      verification. Demonstrates the NL->formal logic pipeline that\\\\n      STA aims to improve via RL training.\\\\n    key_finding: >\\\\n      Neurosymbolic NL2FOL achieves 78% F1 on LOGIC dataset and\\\\n      generalizes to LogicClimate (80% F1), outperforming supervised\\\\n      models by 21%.\\\\n\\\\n  - id: logica2\\\\n    title: \\\\\\\"LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding\\\\\\\"\\\\n    authors: \\\\\\\"Liu et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"IEEE/ACM TASLP 2023\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: evaluation\\\\n    relevance: >\\\\n      Logical reasoning evaluation benchmark derived from Chinese civil\\\\n      service exams. Provides supplementary evaluation for STA's\\\\n      formalization capabilities.\\\\n    key_finding: >\\\\n      8,678 multiple-choice questions covering categorical, disjunctive,\\\\n      and conditional reasoning; widely used LLM benchmark.\\\\n\\\", \\\"total_chars\\\": 20468, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\", \"content\": \"# Literature Map for Solver Trace Ablation (STA)\\n# Categories:\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\n#   2. reward-shaping: Reward shaping for code/formal verification\\n#   3. mutation-testing: Mutation testing in software engineering\\n#   4. intensional-analysis: Intensional program analysis\\n#   5. reward-hacking: Reward hacking / overoptimization\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\n\\npapers:\\n\\n  # ============================================================\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\n  # ============================================================\\n\\n  - id: deepseek-r1\\n    title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n    authors: \\\"DeepSeek-AI\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2501.12948 / Nature 2025\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\n      intensional structural reward for neurosymbolic formalization.\\n    key_finding: >\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\n      showing emergent chain-of-thought reasoning from RL alone.\\n\\n  - id: deepseekmath\\n    title: \\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\"\\n    authors: \\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2402.03300\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\\n      used in STA training. GRPO eliminates the critic model by estimating\\n      baselines from group scores.\\n    key_finding: >\\n      GRPO matches PPO performance while significantly reducing training\\n      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.\\n\\n  - id: logic-rl\\n    title: \\\"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\\\"\\n    authors: \\\"Xian et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.14768\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic\\n      logic puzzles. Closest competitor to STA's approach of RL for logical\\n      formalization, though Logic-RL uses extensional (answer-correctness)\\n      rewards rather than STA's intensional structural rewards.\\n    key_finding: >\\n      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;\\n      rule-based reward design is critical for RL-based logical reasoning.\\n\\n  - id: mellgren-prolog-grpo\\n    title: \\\"Training Language Models to Use Prolog as a Tool\\\"\\n    authors: \\\"Niklas Mellgren\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2512.07407\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,\\n      directly comparable to STA's approach of GRPO-training a formalizer.\\n      Key difference: uses pass/fail reward vs STA's structural ISR.\\n    key_finding: >\\n      GRPO is effective for teaching small LLMs to use Prolog as a tool\\n      for logical and mathematical reasoning.\\n\\n  - id: satlm\\n    title: \\\"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\\\"\\n    authors: \\\"Xi Ye et al.\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023\\\"\\n    category: neurosymbolic-rl\\n    role: background\\n    relevance: >\\n      Neurosymbolic approach where LLM generates declarative specifications\\n      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)\\n      but uses prompting, not RL training.\\n    key_finding: >\\n      Declarative formulation outperforms imperative program-aided LMs by 23%\\n      on GSM; achieves SoTA on LSAT and BoardgameQA.\\n\\n  # ============================================================\\n  # Category 2: Reward shaping for code/formal verification\\n  # ============================================================\\n\\n  - id: lightman-verify-step\\n    title: \\\"Let's Verify Step by Step\\\"\\n    authors: \\\"Hunter Lightman, Vineet Kosaraju, Yura Burda, et al.\\\"\\n    year: 2023\\n    venue: \\\"arXiv 2305.20050 / ICLR 2024\\\"\\n    category: reward-shaping\\n    role: method-component\\n    relevance: >\\n      Establishes that process supervision (step-level reward) outperforms\\n      outcome supervision (final-answer reward) for reasoning. STA's ISR\\n      is analogous: it provides structural process-level signal about which\\n      components of a formalization matter, rather than just pass/fail.\\n    key_finding: >\\n      Process-supervised reward model achieves 78% on MATH, significantly\\n      outperforming outcome-supervised models. Released PRM800K dataset.\\n\\n  - id: reward-shaping-rlhf\\n    title: \\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\"\\n    authors: \\\"Jiayi Fu, Xuandong Zhao, Chengyuan Yao, et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.18770\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Studies reward shaping design principles for RLHF: bounded rewards and\\n      rapid-then-convergent growth. STA's ISR follows these principles\\n      naturally since structural necessity scores are bounded [0,1].\\n    key_finding: >\\n      Two key reward shaping principles: (1) bounded RL reward, (2) rapid\\n      initial growth with gradual convergence. PAR method achieves 5%+\\n      win rate improvement on AlpacaEval 2.0.\\n\\n  - id: rlvr-reasoning\\n    title: \\\"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2506.14245\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize\\n      reasoning. STA argues that for neurosymbolic formalization, binary reward\\n      is insufficient and structural reward is needed to avoid reward hacking.\\n    key_finding: >\\n      RLVR with binary verification implicitly teaches correct reasoning\\n      strategies, not just answer matching.\\n\\n  - id: rubric-grpo\\n    title: \\\"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2605.08061\\\"\\n    category: reward-shaping\\n    role: direct-competitor\\n    relevance: >\\n      Uses structured rubric-based rewards with GRPO, similar in spirit to\\n      STA's structured ISR. Key difference: rubric rewards come from LLM\\n      judges, while ISR comes from solver-based mutation testing.\\n    key_finding: >\\n      Structured multi-dimensional reward signals improve GRPO training\\n      generalization compared to scalar rewards.\\n\\n  # ============================================================\\n  # Category 3: Mutation testing in software engineering\\n  # ============================================================\\n\\n  - id: demillo1978\\n    title: \\\"Hints on Test Data Selection: Help for the Practicing Programmer\\\"\\n    authors: \\\"Richard A. DeMillo, Richard J. Lipton, Frederick G. Sayward\\\"\\n    year: 1978\\n    venue: \\\"Computer 11(4):34-43\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Foundational paper introducing mutation testing. STA's component\\n      necessity testing directly extends this idea: instead of mutating\\n      source code to test test suites, STA mutates logical formulas\\n      to test component necessity for solver success.\\n    key_finding: >\\n      Introduced mutation testing and the coupling effect hypothesis:\\n      tests that detect simple faults also detect complex faults.\\n\\n  - id: offutt-coupling\\n    title: \\\"Investigations of the Software Testing Coupling Effect\\\"\\n    authors: \\\"A. Jefferson Offutt\\\"\\n    year: 1992\\n    venue: \\\"ACM TOSEM 1(1):5-20\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Empirically validates the coupling effect hypothesis that underpins\\n      mutation testing. STA's single-component ablation is analogous to\\n      first-order mutation; the coupling effect suggests this suffices.\\n    key_finding: >\\n      Test data killing all first-order mutants killed >99% of second-\\n      and third-order mutants, validating the coupling effect.\\n\\n  - id: jia-harman-survey\\n    title: \\\"An Analysis and Survey of the Development of Mutation Testing\\\"\\n    authors: \\\"Yue Jia, Mark Harman\\\"\\n    year: 2011\\n    venue: \\\"IEEE TSE 37(5):649-678\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Comprehensive survey of mutation testing covering three decades of\\n      development. Provides theoretical and practical foundation for STA's\\n      adaptation of mutation testing to logical formulas.\\n    key_finding: >\\n      Systematic classification of mutation operators, cost reduction\\n      techniques, and equivalence problem -- all relevant to STA's design\\n      of clause-level ablation operators.\\n\\n  - id: just-mutants-real-faults\\n    title: \\\"Are Mutants a Valid Substitute for Real Faults in Software Testing?\\\"\\n    authors: \\\"Rene Just, Darioush Jalali, Laura Inozemtseva, et al.\\\"\\n    year: 2014\\n    venue: \\\"FSE 2014\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Validates that mutation testing (structural/intensional analysis of\\n      program adequacy) correlates with real fault detection. Supports STA's\\n      premise that structural analysis of formalization components provides\\n      meaningful signal about formalization quality.\\n    key_finding: >\\n      Mutant detection is statistically correlated with real fault detection,\\n      and mutation score is a better predictor of test effectiveness than\\n      code coverage.\\n\\n  - id: llmorpheus\\n    title: \\\"LLMorpheus: Mutation Testing Using Large Language Models\\\"\\n    authors: \\\"Frank Tip, Jon Bell, et al.\\\"\\n    year: 2025\\n    venue: \\\"IEEE TSE 2025\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Uses LLMs to generate realistic code mutants beyond traditional\\n      mutation operators. Shows mutation testing evolving toward\\n      ML-integrated approaches, validating STA's cross-pollination\\n      of mutation testing ideas into ML training.\\n    key_finding: >\\n      LLM-generated mutants simulate real bugs that rule-based operators\\n      cannot produce, improving mutation testing realism.\\n\\n  - id: mutation-guided-meta\\n    title: \\\"Mutation-Guided LLM-based Test Generation at Meta\\\"\\n    authors: \\\"Christopher Foster et al.\\\"\\n    year: 2025\\n    venue: \\\"FSE 2025\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Industrial application of mutation-guided LLM test generation at\\n      Meta. Demonstrates that mutation analysis can guide LLM behavior\\n      in production -- analogous to how STA uses mutation (ablation) to\\n      guide GRPO reward signal.\\n    key_finding: >\\n      Mutation-guided approach generates tests that kill significantly\\n      more mutants than unguided LLM test generation at Meta scale.\\n\\n  - id: mutation-consistency-llm\\n    title: \\\"Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs\\\"\\n    authors: \\\"Various\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2401.05940\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Uses code mutations to evaluate LLM code understanding consistency.\\n      Conceptually related to STA: both use systematic code/formula\\n      mutations to assess model capabilities.\\n    key_finding: >\\n      LLMs show significant inconsistency when evaluated on mutated code\\n      variants, suggesting superficial pattern matching.\\n\\n  # ============================================================\\n  # Category 4: Intensional program analysis\\n  # ============================================================\\n\\n  - id: deepmutation\\n    title: \\\"A Probabilistic Framework for Mutation Testing in Deep Neural Networks\\\"\\n    authors: \\\"Various\\\"\\n    year: 2023\\n    venue: \\\"Information and Software Technology 2023\\\"\\n    category: intensional-analysis\\n    role: background\\n    relevance: >\\n      Extends mutation testing to DNN testing with probabilistic mutation\\n      operators. Parallel to STA's extension of mutation testing from\\n      traditional programs to logical formulas.\\n    key_finding: >\\n      Probabilistic mutation framework enables meaningful test adequacy\\n      assessment for neural networks through structural perturbation.\\n\\n  # ============================================================\\n  # Category 5: Reward hacking / overoptimization\\n  # ============================================================\\n\\n  - id: inform-reward-hacking\\n    title: \\\"InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling\\\"\\n    authors: \\\"Various\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS 2024\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Proposes information-bottleneck approach to detect and mitigate reward\\n      hacking. STA's ISR addresses the same problem differently: by grounding\\n      reward in verifiable structural properties (component necessity), it\\n      reduces the attack surface for reward hacking.\\n    key_finding: >\\n      Variational information bottleneck filters irrelevant features from\\n      reward model; Cluster Separation Index detects reward overoptimization.\\n\\n  - id: mo-grpo\\n    title: \\\"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\\\"\\n    authors: \\\"CyberAgent AI Lab\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2509.22047\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Directly addresses GRPO reward hacking in multi-objective settings.\\n      STA's ISR can be viewed as adding a structural objective to the\\n      correctness objective, making MO-GRPO's insights directly applicable.\\n    key_finding: >\\n      Standard GRPO normalizes after summing rewards, allowing high-variance\\n      objectives to dominate. MO-GRPO equalizes scales before aggregation.\\n\\n  - id: reward-hacking-survey\\n    title: \\\"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\\\"\\n    authors: \\\"Various\\\"\\n    year: 2026\\n    venue: \\\"arXiv 2604.13602\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Comprehensive survey of reward hacking mechanisms in the LLM era.\\n      Provides theoretical framework for understanding why STA's structural\\n      reward is more robust than pure outcome-based reward.\\n    key_finding: >\\n      Reward hacking manifests through specification gaming, reward model\\n      exploitation, and emergent misalignment; structural verification\\n      rewards are more robust than learned reward models.\\n\\n  - id: energy-loss-reward-hacking\\n    title: \\\"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"ICML 2025\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Identifies energy loss in LLM final layer as an indicator of reward\\n      hacking during RL. Provides complementary diagnostic to STA's\\n      structural reward approach.\\n    key_finding: >\\n      Energy loss in the final layer increases during RL and excessive\\n      increase characterizes reward hacking; EPPO algorithm penalizes\\n      this to mitigate hacking.\\n\\n  # ============================================================\\n  # Category 6: FOL/Prolog formalization with LLMs\\n  # ============================================================\\n\\n  - id: folio\\n    title: \\\"FOLIO: Natural Language Reasoning with First-Order Logic\\\"\\n    authors: \\\"Simeng Han et al.\\\"\\n    year: 2022\\n    venue: \\\"arXiv 2209.00840 / EMNLP 2024\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Primary FOL reasoning benchmark. STA uses FOLIO-style NL->FOL\\n      formalization as the target task for GRPO training. FOLIO's\\n      expert-annotated FOL annotations serve as reference formalizations.\\n    key_finding: >\\n      1,430 NL-FOL paired examples with reasoning depths up to 5+;\\n      GPT-4 still struggles on the hardest examples.\\n\\n  - id: proofwriter\\n    title: \\\"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language\\\"\\n    authors: \\\"Oyvind Tafjord, Bhavana Dalvi, Peter Clark\\\"\\n    year: 2021\\n    venue: \\\"Findings of ACL-IJCNLP 2021\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Source dataset for STA's training data. ProofWriter provides\\n      rule-based logical reasoning problems in natural language that\\n      STA uses for training formalizer models.\\n    key_finding: >\\n      Generative model can reliably produce implications and proofs;\\n      accuracy exceeds prior methods by 9% and generalizes to unseen\\n      proof depths.\\n\\n  - id: logic-lm\\n    title: \\\"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\\\"\\n    authors: \\\"Liangming Pan, Alon Albalak, Xinyi Wang, William Wang\\\"\\n    year: 2023\\n    venue: \\\"Findings of EMNLP 2023\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      LLM->symbolic solver pipeline for logical reasoning, directly\\n      comparable to STA's formalizer->Prolog solver pipeline. Key\\n      difference: Logic-LM uses prompting, STA uses GRPO training.\\n    key_finding: >\\n      LLM+solver achieves 39.2% improvement over LLM-alone on logical\\n      reasoning benchmarks including ProofWriter and FOLIO.\\n\\n  - id: linc\\n    title: \\\"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers\\\"\\n    authors: \\\"Theo X. Olausson, Alex Gu, Ben Lipkin, et al.\\\"\\n    year: 2023\\n    venue: \\\"EMNLP 2023\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      Neurosymbolic approach where LLM translates NL to FOL for theorem\\n      prover. Directly comparable to STA's NL->Prolog translation.\\n      LINC uses prompting-based approach; STA uses RL training.\\n    key_finding: >\\n      StarCoder+ (15.5B) with LINC outperforms GPT-3.5 and GPT-4 with\\n      CoT by 38% and 10% respectively on ProofWriter.\\n\\n  - id: fover\\n    title: \\\"FoVer: First-Order Logic Verification for Natural Language Reasoning\\\"\\n    authors: \\\"Yu Pei, Yongping Du, Xingnan Jin\\\"\\n    year: 2025\\n    venue: \\\"TACL 13:1340-1359\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      Uses LLM->FOL->Z3 pipeline for verifying NL reasoning correctness.\\n      Similar to STA's verification pipeline but focuses on post-hoc\\n      verification rather than training reward signal.\\n    key_finding: >\\n      FOL verification via Z3 significantly outperforms existing methods\\n      on ProofWriter and FOLIO benchmarks.\\n\\n  - id: lorp\\n    title: \\\"LoRP: LLM-based Logical Reasoning via Prolog\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"Knowledge-Based Systems 2025\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      LLM->Prolog pipeline with FOL-to-Prolog translation mechanism.\\n      Closest to STA's formalization target (Prolog), though LoRP\\n      uses prompting while STA uses GRPO training with structural reward.\\n    key_finding: >\\n      Systematic FOL-to-Prolog translation extends Prolog expressiveness;\\n      achieves SoTA accuracy on logical reasoning with three-vote majority.\\n\\n  - id: nl2fol\\n    title: \\\"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection\\\"\\n    authors: \\\"Lalwani, Kim, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2405.02318\\\"\\n    category: fol-formalization\\n    role: background\\n    relevance: >\\n      Step-by-step NL->FOL translation using LLMs with SMT solver\\n      verification. Demonstrates the NL->formal logic pipeline that\\n      STA aims to improve via RL training.\\n    key_finding: >\\n      Neurosymbolic NL2FOL achieves 78% F1 on LOGIC dataset and\\n      generalizes to LogicClimate (80% F1), outperforming supervised\\n      models by 21%.\\n\\n  - id: logica2\\n    title: \\\"LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: \\\"IEEE/ACM TASLP 2023\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Logical reasoning evaluation benchmark derived from Chinese civil\\n      service exams. Provides supplementary evaluation for STA's\\n      formalization capabilities.\\n    key_finding: >\\n      8,678 multiple-choice questions covering categorical, disjunctive,\\n      and conditional reasoning; widely used LLM benchmark.\\n\", \"total_chars\": 20468, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 56_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me compile the report and write it, then update the literature_map.yaml.

The 5 most relevant papers:

1. **Gao et al. (2024) "On Designing Effective RL Reward at Training Time for LLM Reasoning"** - arXiv 2410.15115
   - Found that PRM rewards "may NOT help or even hurt RL training, producing worse performances than LLMs trained with the success reward only"
   - Solution: Clipping and Delta reward refinement to bound accumulated reward magnitude
   - Directly analogous to plan005 — STA's structural reward (ISR) is a process reward that's degrading the prove_rate outcome

2. **Ye et al. (2025) "Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"** - arXiv 2509.03403
   - PRMs suffer from inaccuracies and reward hacking; proposes PROF to filter consistency between process and outcome rewards
   - Suggests that ISR should only be used when it aligns with actual execution success, mirroring PROF's filtering strategy

3. **Moskovitz et al. (2023) "Confronting Reward Model Overoptimization with Constrained RLHF"** - arXiv 2310.04373, ICLR 2024
   - Shows how composite rewards degrade when components are correlated; proposes dynamic weighting via Lagrange multipliers
   - Since STA uses a composite reward combining execution and ISR, this approach could replace the fixed weighting scheme

4. **Skalse et al. (2022) "Defining and Characterizing Reward Hacking"** - arXiv 2209.13085, NeurIPS 2022
   - Proves that for stochastic policies, two reward functions can only avoid hacking if one is constant, establishing a theoretical limit on composite reward safety
   - This explains why any positive weight on STA's auxiliary reward can ultimately harm the primary prove_rate objective

5. **Rezaei et al. (2026) "LLM Reasoning with Process Rewards for Outcome-Guided Steps" (PROGRS)** - arXiv 2604.02341
   - Process rewards can reinforce locally coherent reasoning that still leads to wrong answers; outcome-conditioned centering zeros out incorrect trajectories
   - This suggests STA's ISR should be conditioned on whether execution succeeds rather than applied uniformly across all attempts

Now let me write the report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "3f726649-cb4f-47fd-a7f3-33bba26f0bc0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E5a3fBincgvKJA879qBwrY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7399,
      "cache_read_input_tokens": 46050,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7399
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

_source line 57_

I have all the data. Let me write the report and update the literature map.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "4f81536e-3b34-4568-b0e7-d1da0b006d6e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E5a3fBincgvKJA879qBwrY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7399,
      "cache_read_input_tokens": 46050,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7399
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

_source line 58_

<details open><summary>🔧 Tool call — Write · `toolu_01XF7QgvzT9ybKAzA2r7tczX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/plan005_negative_literature.md",
  "content": "# Plan005 NEGATIVE 结果文献调研：辅助 Reward 降低主目标性能\n\n## 背景\n\nplan005-sta-low-s42 实验结论为 NEGATIVE：GRPO 训练中 STA reward (weight=0.1) 导致 prove_rate 下降 10.7%（0.7725 vs exec-only 0.865）。ISR/PR ratio=0.298 稳定，说明 STA 确实维持了结构性分离，但任何非零 STA 权重都会引入 penalty effect。\n\n本报告调研 multi-objective RL 和 LLM reasoning 领域中关于\"辅助/过程 reward 降低主目标性能\"现象的相关文献。\n\n---\n\n## Paper 1: On Designing Effective RL Reward at Training Time for LLM Reasoning\n\n| 字段 | 内容 |\n|------|------|\n| 作者 | Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu |\n| 年份 | 2024 |\n| Venue | arXiv 2410.15115 |\n\n**核心发现**: 学习到的 PRM (Process Reward Model) 和 ORM (Outcome Reward Model) 用于 RL 训练时，**可能不仅无帮助，甚至损害训练效果**，产生比仅使用 success reward 训练的模型更差的性能。模型通过重复正确但不必要的推理步骤获得高 reward，造成严重的 reward hacking。\n\n**解决方案**: 提出两种 reward refinement 技术：\n- **Clipping**: 限制累积 reward 的上界\n- **Delta**: 限制跨 trajectory 的 reward 增长幅度\n\n两者确保累积 reward 有上界，防止 learned reward model 被 exploit。\n\n**与 plan005 的关联**: **高度相关**。STA 的 ISR 本质上是一种结构性 process reward。该论文直接证明 process reward 在 RL 训练时可降低主目标（accuracy/prove_rate）性能。STA weight=0.1 的 prove_rate 下降 10.7% 与此现象一致。Clipping/Delta 技术可作为 STA 改进方向——限制 ISR 对总 reward 的最大贡献。\n\n---\n\n## Paper 2: Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training\n\n| 字段 | 内容 |\n|------|------|\n| 作者 | Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal |\n| 年份 | 2025 |\n| Venue | arXiv 2509.03403 |\n\n**核心发现**: PRM 虽然提供细粒度的中间步骤指导，但**频繁出现不准确性且容易被 reward hacking 利用**。而 ORM 缺乏足够的粒度来评估推理质量。直接混合 PRM+ORM 信号会导致性能退化。\n\n**解决方案**: PROF (PRocess cOnsistency Filter) — 基于 PRM-ORM 一致性的数据过滤。保留\"高 process value 的正确 response\"和\"低 process value 的错误 response\"，过滤掉不一致样本。比直接混合方法**提升 4%+ 准确率**。\n\n**与 plan005 的关联**: **高度相关**。STA 的 ISR 是一种 process-level signal（结构必要性），与 execution outcome 是两个不同维度。PROF 的思路建议：仅在 ISR 与 execution 结果一致时使用 ISR reward（即只对 prove 成功的样本施加 ISR bonus，对 prove 失败的样本不施加 ISR penalty），而非无条件线性组合。这可能是解决 plan005 negative 的关键方向。\n\n---\n\n## Paper 3: Confronting Reward Model Overoptimization with Constrained RLHF\n\n| 字段 | 内容 |\n|------|------|\n| 作者 | Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer |\n| 年份 | 2023 |\n| Venue | arXiv 2310.04373 / ICLR 2024 |\n\n**核心发现**: 首个研究 composite reward model 过度优化的工作。发现组合多个 reward model 时，**component RM 之间的相关性显著影响过度优化发生的阈值**。超过阈值后，更高的 proxy reward 反而关联更差的真实表现。\n\n**解决方案**: \n- **Constrained RL**: 将每个 component RM 的优化限制在其\"有用阈值\"内\n- **Dynamic Lagrange Multipliers**: 通过拉格朗日乘子自动学习动态权重，替代固定权重的线性组合\n- **Adaptive Gradient-Free Optimization**: 在训练过程中识别最优性能点\n\n**与 plan005 的关联**: **直接相关**。plan005 使用固定权重 0.1 线性组合 exec reward 和 ISR。该论文表明固定权重的线性标量化存在本质缺陷，建议使用 constrained RL 或动态 Lagrange 乘子权重。这为 STA 提供了明确的改进方向：用约束优化替代固定权重。\n\n---\n\n## Paper 4: Defining and Characterizing Reward Hacking\n\n| 字段 | 内容 |\n|------|------|\n| 作者 | Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger |\n| 年份 | 2022 |\n| Venue | arXiv 2209.13085 / NeurIPS 2022 |\n\n**核心发现**: 形式化定义了 reward hacking。关键定理：**对于所有随机策略的集合，两个 reward function 只有在其中一个为常数时才是 unhackable 的**。这意味着任何非平凡的 proxy reward（如 ISR）在被优化时，都有可能降低 true reward（如 prove_rate）。\n\n**理论意义**: 该结果为 plan005 的 negative 提供了**理论解释基础**——ISR 作为 prove_rate 的 proxy，在任何非零权重下都可能 hack 真实目标。这不是 STA 特有的问题，而是 reward composition 的基本限制。\n\n**解决方向**: 论文建议通过限制策略空间（而非使 reward 更复杂）来缓解 hacking。对 STA 而言，这意味着可能需要约束优化策略空间（如 KL penalty 或 clipping），而非简单调低 ISR 权重。\n\n---\n\n## Paper 5: LLM Reasoning with Process Rewards for Outcome-Guided Steps (PROGRS)\n\n| 字段 | 内容 |\n|------|------|\n| 作者 | Mohammad Rezaei, Jens Lehmann, Sahar Vahdati |\n| 年份 | 2026 |\n| Venue | arXiv 2604.02341 (submitted to IJCNN 2026) |\n\n**核心发现**: PRM scores 如果作为绝对 reward 被优化，**会放大\"流利但错误\"的推理模式并诱发 reward hacking**。PRM 经常对最终不正确的推理路径给出高分。\n\n**解决方案**: **Outcome-Conditioned Centering** — 将错误 trajectory 的 PRM scores 平移至零均值。这在保留 PRM 对中间步骤的排序信息的同时，消除 PRM 对错误 trajectory 的系统性偏差。结果：以更少的 rollout 达到比 outcome-only baseline 一致的提升。\n\n**与 plan005 的关联**: **高度相关**。ISR 目前无条件地对所有样本施加：prove 成功的样本得到 ISR bonus（正面），prove 失败的样本被 ISR 评估后可能得到非零 reward（负面效应）。Outcome-conditioned centering 建议：将 ISR 调整为以 execution outcome 为条件——仅对 prove 成功的样本保留 ISR 差异化信号，对 prove 失败的样本将 ISR 归零。\n\n---\n\n## 综合分析与 STA 改进方向\n\n### plan005 NEGATIVE 的理论解释\n\n5 篇论文一致指向同一机制：**辅助/过程 reward 在 RL 训练中降低主目标性能**是一个已知且普遍的现象，不是 STA 特有的。原因包括：\n\n1. **Proxy reward 的固有 hackability**（Skalse et al.）：任何非常数 proxy 都可能降低 true reward\n2. **Process reward 的不准确性**（Gao et al., Ye et al.）：process-level signal 与 outcome 不完全对齐\n3. **固定权重线性组合的缺陷**（Moskovitz et al.）：无法适应训练阶段变化\n4. **无条件施加 process reward 的危害**（Rezaei et al.）：对错误 trajectory 的 process reward 破坏梯度信号\n\n### 可行改进方案（优先级排序）\n\n| 方案 | 来源 | 核心思路 | 实施复杂度 |\n|------|------|----------|-----------|\n| **Outcome-conditioned ISR** | PROGRS | 仅对 prove 成功的样本施加 ISR 差异化 reward | 低 |\n| **ISR Clipping** | Gao et al. | 限制 ISR 对总 reward 的最大贡献 | 低 |\n| **Consistency Filtering** | PROF | 仅使用 ISR-execution 一致的样本 | 中 |\n| **Dynamic Lagrange Weighting** | Moskovitz et al. | 用约束优化自动学习 ISR 权重 | 高 |\n| **Bonus-only ISR** | 综合 | ISR 仅作为 bonus（≥0），不作为 penalty | 低 |\n\n### 推荐下一步\n\n最低成本高收益方案：**Bonus-only + Outcome-conditioned ISR**。具体实现：\n- 对 prove 成功的样本：`reward = exec_reward + α × max(ISR - baseline, 0)`\n- 对 prove 失败的样本：`reward = exec_reward`（ISR 不参与）\n\n这同时解决了 Skalse 的 hackability 问题（ISR 只做正向 bonus）和 Rezaei 的 outcome-conditioning 问题。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "2a094648-40c1-4e7a-9173-cd7f3a699980",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E5a3fBincgvKJA879qBwrY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7399,
      "cache_read_input_tokens": 46050,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7399
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

_source line 59 · 2026-05-14T02:07:47.439Z_

<details><summary>↩ Tool result · `toolu_01XF7QgvzT9ybKAzA2r7tczX`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/plan005_negative_literature.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "b5bd86a8-b98c-4493-a1ca-54c2f71efba5",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/plan005_negative_literature.md",
    "content": "# Plan005 NEGATIVE 结果文献调研：辅助 Reward 降低主目标性能\n\n## 背景\n\nplan005-sta-low-s42 实验结论为 NEGATIVE：GRPO 训练中 STA reward (weight=0.1) 导致 prove_rate 下降 10.7%（0.7725 vs exec-only 0.865）。ISR/PR ratio=0.298 稳定，说明 STA 确实维持了结构性分离，但任何非零 STA 权重都会引入 penalty effect。\n\n本报告调研 multi-objective RL 和 LLM reasoning 领域中关于\"辅助/过程 reward 降低主目标性能\"现象的相关文献。\n\n---\n\n## Paper 1: On Designing Effective RL Reward at Training Time for LLM Reasoning\n\n| 字段 | 内容 |\n|------|------|\n| 作者 | Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu |\n| 年份 | 2024 |\n| Venue | arXiv 2410.15115 |\n\n**核心发现**: 学习到的 PRM (Process Reward Model) 和 ORM (Outcome Reward Model) 用于 RL 训练时，**可能不仅无帮助，甚至损害训练效果**，产生比仅使用 success reward 训练的模型更差的性能。模型通过重复正确但不必要的推理步骤获得高 reward，造成严重的 reward hacking。\n\n**解决方案**: 提出两种 reward refinement 技术：\n- **Clipping**: 限制累积 reward 的上界\n- **Delta**: 限制跨 trajectory 的 reward 增长幅度\n\n两者确保累积 reward 有上界，防止 learned reward model 被 exploit。\n\n**与 plan005 的关联**: **高度相关**。STA 的 ISR 本质上是一种结构性 process reward。该论文直接证明 process reward 在 RL 训练时可降低主目标（accuracy/prove_rate）性能。STA weight=0.1 的 prove_rate 下降 10.7% 与此现象一致。Clipping/Delta 技术可作为 STA 改进方向——限制 ISR 对总 reward 的最大贡献。\n\n---\n\n## Paper 2: Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training\n\n| 字段 | 内容 |\n|------|------|\n| 作者 | Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal |\n| 年份 | 2025 |\n| Venue | arXiv 2509.03403 |\n\n**核心发现**: PRM 虽然提供细粒度的中间步骤指导，但**频繁出现不准确性且容易被 reward hacking 利用**。而 ORM 缺乏足够的粒度来评估推理质量。直接混合 PRM+ORM 信号会导致性能退化。\n\n**解决方案**: PROF (PRocess cOnsistency Filter) — 基于 PRM-ORM 一致性的数据过滤。保留\"高 process value 的正确 response\"和\"低 process value 的错误 response\"，过滤掉不一致样本。比直接混合方法**提升 4%+ 准确率**。\n\n**与 plan005 的关联**: **高度相关**。STA 的 ISR 是一种 process-level signal（结构必要性），与 execution outcome 是两个不同维度。PROF 的思路建议：仅在 ISR 与 execution 结果一致时使用 ISR reward（即只对 prove 成功的样本施加 ISR bonus，对 prove 失败的样本不施加 ISR penalty），而非无条件线性组合。这可能是解决 plan005 negative 的关键方向。\n\n---\n\n## Paper 3: Confronting Reward Model Overoptimization with Constrained RLHF\n\n| 字段 | 内容 |\n|------|------|\n| 作者 | Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer |\n| 年份 | 2023 |\n| Venue | arXiv 2310.04373 / ICLR 2024 |\n\n**核心发现**: 首个研究 composite reward model 过度优化的工作。发现组合多个 reward model 时，**component RM 之间的相关性显著影响过度优化发生的阈值**。超过阈值后，更高的 proxy reward 反而关联更差的真实表现。\n\n**解决方案**: \n- **Constrained RL**: 将每个 component RM 的优化限制在其\"有用阈值\"内\n- **Dynamic Lagrange Multipliers**: 通过拉格朗日乘子自动学习动态权重，替代固定权重的线性组合\n- **Adaptive Gradient-Free Optimization**: 在训练过程中识别最优性能点\n\n**与 plan005 的关联**: **直接相关**。plan005 使用固定权重 0.1 线性组合 exec reward 和 ISR。该论文表明固定权重的线性标量化存在本质缺陷，建议使用 constrained RL 或动态 Lagrange 乘子权重。这为 STA 提供了明确的改进方向：用约束优化替代固定权重。\n\n---\n\n## Paper 4: Defining and Characterizing Reward Hacking\n\n| 字段 | 内容 |\n|------|------|\n| 作者 | Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger |\n| 年份 | 2022 |\n| Venue | arXiv 2209.13085 / NeurIPS 2022 |\n\n**核心发现**: 形式化定义了 reward hacking。关键定理：**对于所有随机策略的集合，两个 reward function 只有在其中一个为常数时才是 unhackable 的**。这意味着任何非平凡的 proxy reward（如 ISR）在被优化时，都有可能降低 true reward（如 prove_rate）。\n\n**理论意义**: 该结果为 plan005 的 negative 提供了**理论解释基础**——ISR 作为 prove_rate 的 proxy，在任何非零权重下都可能 hack 真实目标。这不是 STA 特有的问题，而是 reward composition 的基本限制。\n\n**解决方向**: 论文建议通过限制策略空间（而非使 reward 更复杂）来缓解 hacking。对 STA 而言，这意味着可能需要约束优化策略空间（如 KL penalty 或 clipping），而非简单调低 ISR 权重。\n\n---\n\n## Paper 5: LLM Reasoning with Process Rewards for Outcome-Guided Steps (PROGRS)\n\n| 字段 | 内容 |\n|------|------|\n| 作者 | Mohammad Rezaei, Jens Lehmann, Sahar Vahdati |\n| 年份 | 2026 |\n| Venue | arXiv 2604.02341 (submitted to IJCNN 2026) |\n\n**核心发现**: PRM scores 如果作为绝对 reward 被优化，**会放大\"流利但错误\"的推理模式并诱发 reward hacking**。PRM 经常对最终不正确的推理路径给出高分。\n\n**解决方案**: **Outcome-Conditioned Centering** — 将错误 trajectory 的 PRM scores 平移至零均值。这在保留 PRM 对中间步骤的排序信息的同时，消除 PRM 对错误 trajectory 的系统性偏差。结果：以更少的 rollout 达到比 outcome-only baseline 一致的提升。\n\n**与 plan005 的关联**: **高度相关**。ISR 目前无条件地对所有样本施加：prove 成功的样本得到 ISR bonus（正面），prove 失败的样本被 ISR 评估后可能得到非零 reward（负面效应）。Outcome-conditioned centering 建议：将 ISR 调整为以 execution outcome 为条件——仅对 prove 成功的样本保留 ISR 差异化信号，对 prove 失败的样本将 ISR 归零。\n\n---\n\n## 综合分析与 STA 改进方向\n\n### plan005 NEGATIVE 的理论解释\n\n5 篇论文一致指向同一机制：**辅助/过程 reward 在 RL 训练中降低主目标性能**是一个已知且普遍的现象，不是 STA 特有的。原因包括：\n\n1. **Proxy reward 的固有 hackability**（Skalse et al.）：任何非常数 proxy 都可能降低 true reward\n2. **Process reward 的不准确性**（Gao et al., Ye et al.）：process-level signal 与 outcome 不完全对齐\n3. **固定权重线性组合的缺陷**（Moskovitz et al.）：无法适应训练阶段变化\n4. **无条件施加 process reward 的危害**（Rezaei et al.）：对错误 trajectory 的 process reward 破坏梯度信号\n\n### 可行改进方案（优先级排序）\n\n| 方案 | 来源 | 核心思路 | 实施复杂度 |\n|------|------|----------|-----------|\n| **Outcome-conditioned ISR** | PROGRS | 仅对 prove 成功的样本施加 ISR 差异化 reward | 低 |\n| **ISR Clipping** | Gao et al. | 限制 ISR 对总 reward 的最大贡献 | 低 |\n| **Consistency Filtering** | PROF | 仅使用 ISR-execution 一致的样本 | 中 |\n| **Dynamic Lagrange Weighting** | Moskovitz et al. | 用约束优化自动学习 ISR 权重 | 高 |\n| **Bonus-only ISR** | 综合 | ISR 仅作为 bonus（≥0），不作为 penalty | 低 |\n\n### 推荐下一步\n\n最低成本高收益方案：**Bonus-only + Outcome-conditioned ISR**。具体实现：\n- 对 prove 成功的样本：`reward = exec_reward + α × max(ISR - baseline, 0)`\n- 对 prove 失败的样本：`reward = exec_reward`（ISR 不参与）\n\n这同时解决了 Skalse 的 hackability 问题（ISR 只做正向 bonus）和 Rezaei 的 outcome-conditioning 问题。\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 60_

Now update the literature_map.yaml with new entries under reward-shaping category.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "34f98242-ae94-421a-ae70-9f54dfc01317",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJRexH4HfMF1KEt7cQNrdn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3991,
      "cache_read_input_tokens": 53449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3991
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

_source line 61_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XDXpJTEHwKu4gcVeNHGSis`</summary>

```json
{
  "project": "solver-trace-ablation",
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
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "213820cc-95a9-47f0-bd5d-fe12bbb64227",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJRexH4HfMF1KEt7cQNrdn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3991,
      "cache_read_input_tokens": 53449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3991
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

_source line 62 · 2026-05-14T02:07:55.337Z_

<details><summary>↩ Tool result · `toolu_01XDXpJTEHwKu4gcVeNHGSis`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\", \"content\": \"# Literature Map for Solver Trace Ablation (STA)\\n# Categories:\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\n#   2. reward-shaping: Reward shaping for code/formal verification\\n#   3. mutation-testing: Mutation testing in software engineering\\n#   4. intensional-analysis: Intensional program analysis\\n#   5. reward-hacking: Reward hacking / overoptimization\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\n\\npapers:\\n\\n  # ============================================================\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\n  # ============================================================\\n\\n  - id: deepseek-r1\\n    title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n    authors: \\\"DeepSeek-AI\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2501.12948 / Nature 2025\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\n      intensional structural reward for neurosymbolic formalization.\\n    key_finding: >\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\n      showing emergent chain-of-thought reasoning from RL alone.\\n\\n  - id: deepseekmath\\n    title: \\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\"\\n    authors: \\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2402.03300\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\\n      used in STA training. GRPO eliminates the critic model by estimating\\n      baselines from group scores.\\n    key_finding: >\\n      GRPO matches PPO performance while significantly reducing training\\n      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.\\n\\n  - id: logic-rl\\n    title: \\\"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\\\"\\n    authors: \\\"Xian et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.14768\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic\\n      logic puzzles. Closest competitor to STA's approach of RL for logical\\n      formalization, though Logic-RL uses extensional (answer-correctness)\\n      rewards rather than STA's intensional structural rewards.\\n    key_finding: >\\n      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;\\n      rule-based reward design is critical for RL-based logical reasoning.\\n\\n  - id: mellgren-prolog-grpo\\n    title: \\\"Training Language Models to Use Prolog as a Tool\\\"\\n    authors: \\\"Niklas Mellgren\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2512.07407\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,\\n      directly comparable to STA's approach of GRPO-training a formalizer.\\n      Key difference: uses pass/fail reward vs STA's structural ISR.\\n    key_finding: >\\n      GRPO is effective for teaching small LLMs to use Prolog as a tool\\n      for logical and mathematical reasoning.\\n\\n  - id: satlm\\n    title: \\\"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\\\"\\n    authors: \\\"Xi Ye et al.\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023\\\"\\n    category: neurosymbolic-rl\\n    role: background\\n    relevance: >\\n      Neurosymbolic approach where LLM generates declarative specifications\\n      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)\\n      but uses prompting, not RL training.\\n    key_finding: >\\n      Declarative formulation outperforms imperative program-aided LMs by 23%\\n      on GSM; achieves SoTA on LSAT and BoardgameQA.\\n\\n  # ============================================================\\n  # Category 2: Reward shaping for code/formal verification\\n  # ============================================================\\n\\n  - id: lightman-verify-step\\n    title: \\\"Let's Verify Step by Step\\\"\\n    authors: \\\"Hunter Lightman, Vineet Kosaraju, Yura Burda, et al.\\\"\\n    year: 2023\\n    venue: \\\"arXiv 2305.20050 / ICLR 2024\\\"\\n    category: reward-shaping\\n    role: method-component\\n    relevance: >\\n      Establishes that process supervision (step-level reward) outperforms\\n      outcome supervision (final-answer reward) for reasoning. STA's ISR\\n      is analogous: it provides structural process-level signal about which\\n      components of a formalization matter, rather than just pass/fail.\\n    key_finding: >\\n      Process-supervised reward model achieves 78% on MATH, significantly\\n      outperforming outcome-supervised models. Released PRM800K dataset.\\n\\n  - id: reward-shaping-rlhf\\n    title: \\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\"\\n    authors: \\\"Jiayi Fu, Xuandong Zhao, Chengyuan Yao, et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.18770\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Studies reward shaping design principles for RLHF: bounded rewards and\\n      rapid-then-convergent growth. STA's ISR follows these principles\\n      naturally since structural necessity scores are bounded [0,1].\\n    key_finding: >\\n      Two key reward shaping principles: (1) bounded RL reward, (2) rapid\\n      initial growth with gradual convergence. PAR method achieves 5%+\\n      win rate improvement on AlpacaEval 2.0.\\n\\n  - id: rlvr-reasoning\\n    title: \\\"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2506.14245\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize\\n      reasoning. STA argues that for neurosymbolic formalization, binary reward\\n      is insufficient and structural reward is needed to avoid reward hacking.\\n    key_finding: >\\n      RLVR with binary verification implicitly teaches correct reasoning\\n      strategies, not just answer matching.\\n\\n  - id: rubric-grpo\\n    title: \\\"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2605.08061\\\"\\n    category: reward-shaping\\n    role: direct-competitor\\n    relevance: >\\n      Uses structured rubric-based rewards with GRPO, similar in spirit to\\n      STA's structured ISR. Key difference: rubric rewards come from LLM\\n      judges, while ISR comes from solver-based mutation testing.\\n    key_finding: >\\n      Structured multi-dimensional reward signals improve GRPO training\\n      generalization compared to scalar rewards.\\n\\n  # ============================================================\\n  # Category 3: Mutation testing in software engineering\\n  # ============================================================\\n\\n  - id: demillo1978\\n    title: \\\"Hints on Test Data Selection: Help for the Practicing Programmer\\\"\\n    authors: \\\"Richard A. DeMillo, Richard J. Lipton, Frederick G. Sayward\\\"\\n    year: 1978\\n    venue: \\\"Computer 11(4):34-43\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Foundational paper introducing mutation testing. STA's component\\n      necessity testing directly extends this idea: instead of mutating\\n      source code to test test suites, STA mutates logical formulas\\n      to test component necessity for solver success.\\n    key_finding: >\\n      Introduced mutation testing and the coupling effect hypothesis:\\n      tests that detect simple faults also detect complex faults.\\n\\n  - id: offutt-coupling\\n    title: \\\"Investigations of the Software Testing Coupling Effect\\\"\\n    authors: \\\"A. Jefferson Offutt\\\"\\n    year: 1992\\n    venue: \\\"ACM TOSEM 1(1):5-20\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Empirically validates the coupling effect hypothesis that underpins\\n      mutation testing. STA's single-component ablation is analogous to\\n      first-order mutation; the coupling effect suggests this suffices.\\n    key_finding: >\\n      Test data killing all first-order mutants killed >99% of second-\\n      and third-order mutants, validating the coupling effect.\\n\\n  - id: jia-harman-survey\\n    title: \\\"An Analysis and Survey of the Development of Mutation Testing\\\"\\n    authors: \\\"Yue Jia, Mark Harman\\\"\\n    year: 2011\\n    venue: \\\"IEEE TSE 37(5):649-678\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Comprehensive survey of mutation testing covering three decades of\\n      development. Provides theoretical and practical foundation for STA's\\n      adaptation of mutation testing to logical formulas.\\n    key_finding: >\\n      Systematic classification of mutation operators, cost reduction\\n      techniques, and equivalence problem -- all relevant to STA's design\\n      of clause-level ablation operators.\\n\\n  - id: just-mutants-real-faults\\n    title: \\\"Are Mutants a Valid Substitute for Real Faults in Software Testing?\\\"\\n    authors: \\\"Rene Just, Darioush Jalali, Laura Inozemtseva, et al.\\\"\\n    year: 2014\\n    venue: \\\"FSE 2014\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Validates that mutation testing (structural/intensional analysis of\\n      program adequacy) correlates with real fault detection. Supports STA's\\n      premise that structural analysis of formalization components provides\\n      meaningful signal about formalization quality.\\n    key_finding: >\\n      Mutant detection is statistically correlated with real fault detection,\\n      and mutation score is a better predictor of test effectiveness than\\n      code coverage.\\n\\n  - id: llmorpheus\\n    title: \\\"LLMorpheus: Mutation Testing Using Large Language Models\\\"\\n    authors: \\\"Frank Tip, Jon Bell, et al.\\\"\\n    year: 2025\\n    venue: \\\"IEEE TSE 2025\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Uses LLMs to generate realistic code mutants beyond traditional\\n      mutation operators. Shows mutation testing evolving toward\\n      ML-integrated approaches, validating STA's cross-pollination\\n      of mutation testing ideas into ML training.\\n    key_finding: >\\n      LLM-generated mutants simulate real bugs that rule-based operators\\n      cannot produce, improving mutation testing realism.\\n\\n  - id: mutation-guided-meta\\n    title: \\\"Mutation-Guided LLM-based Test Generation at Meta\\\"\\n    authors: \\\"Christopher Foster et al.\\\"\\n    year: 2025\\n    venue: \\\"FSE 2025\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Industrial application of mutation-guided LLM test generation at\\n      Meta. Demonstrates that mutation analysis can guide LLM behavior\\n      in production -- analogous to how STA uses mutation (ablation) to\\n      guide GRPO reward signal.\\n    key_finding: >\\n      Mutation-guided approach generates tests that kill significantly\\n      more mutants than unguided LLM test generation at Meta scale.\\n\\n  - id: mutation-consistency-llm\\n    title: \\\"Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs\\\"\\n    authors: \\\"Various\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2401.05940\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Uses code mutations to evaluate LLM code understanding consistency.\\n      Conceptually related to STA: both use systematic code/formula\\n      mutations to assess model capabilities.\\n    key_finding: >\\n      LLMs show significant inconsistency when evaluated on mutated code\\n      variants, suggesting superficial pattern matching.\\n\\n  # ============================================================\\n  # Category 4: Intensional program analysis\\n  # ============================================================\\n\\n  - id: deepmutation\\n    title: \\\"A Probabilistic Framework for Mutation Testing in Deep Neural Networks\\\"\\n    authors: \\\"Various\\\"\\n    year: 2023\\n    venue: \\\"Information and Software Technology 2023\\\"\\n    category: intensional-analysis\\n    role: background\\n    relevance: >\\n      Extends mutation testing to DNN testing with probabilistic mutation\\n      operators. Parallel to STA's extension of mutation testing from\\n      traditional programs to logical formulas.\\n    key_finding: >\\n      Probabilistic mutation framework enables meaningful test adequacy\\n      assessment for neural networks through structural perturbation.\\n\\n  # ============================================================\\n  # Category 5: Reward hacking / overoptimization\\n  # ============================================================\\n\\n  - id: inform-reward-hacking\\n    title: \\\"InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling\\\"\\n    authors: \\\"Various\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS 2024\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Proposes information-bottleneck approach to detect and mitigate reward\\n      hacking. STA's ISR addresses the same problem differently: by grounding\\n      reward in verifiable structural properties (component necessity), it\\n      reduces the attack surface for reward hacking.\\n    key_finding: >\\n      Variational information bottleneck filters irrelevant features from\\n      reward model; Cluster Separation Index detects reward overoptimization.\\n\\n  - id: mo-grpo\\n    title: \\\"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\\\"\\n    authors: \\\"CyberAgent AI Lab\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2509.22047\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Directly addresses GRPO reward hacking in multi-objective settings.\\n      STA's ISR can be viewed as adding a structural objective to the\\n      correctness objective, making MO-GRPO's insights directly applicable.\\n    key_finding: >\\n      Standard GRPO normalizes after summing rewards, allowing high-variance\\n      objectives to dominate. MO-GRPO equalizes scales before aggregation.\\n\\n  - id: reward-hacking-survey\\n    title: \\\"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\\\"\\n    authors: \\\"Various\\\"\\n    year: 2026\\n    venue: \\\"arXiv 2604.13602\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Comprehensive survey of reward hacking mechanisms in the LLM era.\\n      Provides theoretical framework for understanding why STA's structural\\n      reward is more robust than pure outcome-based reward.\\n    key_finding: >\\n      Reward hacking manifests through specification gaming, reward model\\n      exploitation, and emergent misalignment; structural verification\\n      rewards are more robust than learned reward models.\\n\\n  - id: energy-loss-reward-hacking\\n    title: \\\"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"ICML 2025\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Identifies energy loss in LLM final layer as an indicator of reward\\n      hacking during RL. Provides complementary diagnostic to STA's\\n      structural reward approach.\\n    key_finding: >\\n      Energy loss in the final layer increases during RL and excessive\\n      increase characterizes reward hacking; EPPO algorithm penalizes\\n      this to mitigate hacking.\\n\\n  # ============================================================\\n  # Category 6: FOL/Prolog formalization with LLMs\\n  # ============================================================\\n\\n  - id: folio\\n    title: \\\"FOLIO: Natural Language Reasoning with First-Order Logic\\\"\\n    authors: \\\"Simeng Han et al.\\\"\\n    year: 2022\\n    venue: \\\"arXiv 2209.00840 / EMNLP 2024\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Primary FOL reasoning benchmark. STA uses FOLIO-style NL->FOL\\n      formalization as the target task for GRPO training. FOLIO's\\n      expert-annotated FOL annotations serve as reference formalizations.\\n    key_finding: >\\n      1,430 NL-FOL paired examples with reasoning depths up to 5+;\\n      GPT-4 still struggles on the hardest examples.\\n\\n  - id: proofwriter\\n    title: \\\"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language\\\"\\n    authors: \\\"Oyvind Tafjord, Bhavana Dalvi, Peter Clark\\\"\\n    year: 2021\\n    venue: \\\"Findings of ACL-IJCNLP 2021\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Source dataset for STA's training data. ProofWriter provides\\n      rule-based logical reasoning problems in natural language that\\n      STA uses for training formalizer models.\\n    key_finding: >\\n      Generative model can reliably produce implications and proofs;\\n      accuracy exceeds prior methods by 9% and generalizes to unseen\\n      proof depths.\\n\\n  - id: logic-lm\\n    title: \\\"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\\\"\\n    authors: \\\"Liangming Pan, Alon Albalak, Xinyi Wang, William Wang\\\"\\n    year: 2023\\n    venue: \\\"Findings of EMNLP 2023\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      LLM->symbolic solver pipeline for logical reasoning, directly\\n      comparable to STA's formalizer->Prolog solver pipeline. Key\\n      difference: Logic-LM uses prompting, STA uses GRPO training.\\n    key_finding: >\\n      LLM+solver achieves 39.2% improvement over LLM-alone on logical\\n      reasoning benchmarks including ProofWriter and FOLIO.\\n\\n  - id: linc\\n    title: \\\"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers\\\"\\n    authors: \\\"Theo X. Olausson, Alex Gu, Ben Lipkin, et al.\\\"\\n    year: 2023\\n    venue: \\\"EMNLP 2023\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      Neurosymbolic approach where LLM translates NL to FOL for theorem\\n      prover. Directly comparable to STA's NL->Prolog translation.\\n      LINC uses prompting-based approach; STA uses RL training.\\n    key_finding: >\\n      StarCoder+ (15.5B) with LINC outperforms GPT-3.5 and GPT-4 with\\n      CoT by 38% and 10% respectively on ProofWriter.\\n\\n  - id: fover\\n    title: \\\"FoVer: First-Order Logic Verification for Natural Language Reasoning\\\"\\n    authors: \\\"Yu Pei, Yongping Du, Xingnan Jin\\\"\\n    year: 2025\\n    venue: \\\"TACL 13:1340-1359\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      Uses LLM->FOL->Z3 pipeline for verifying NL reasoning correctness.\\n      Similar to STA's verification pipeline but focuses on post-hoc\\n      verification rather than training reward signal.\\n    key_finding: >\\n      FOL verification via Z3 significantly outperforms existing methods\\n      on ProofWriter and FOLIO benchmarks.\\n\\n  - id: lorp\\n    title: \\\"LoRP: LLM-based Logical Reasoning via Prolog\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"Knowledge-Based Systems 2025\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      LLM->Prolog pipeline with FOL-to-Prolog translation mechanism.\\n      Closest to STA's formalization target (Prolog), though LoRP\\n      uses prompting while STA uses GRPO training with structural reward.\\n    key_finding: >\\n      Systematic FOL-to-Prolog translation extends Prolog expressiveness;\\n      achieves SoTA accuracy on logical reasoning with three-vote majority.\\n\\n  - id: nl2fol\\n    title: \\\"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection\\\"\\n    authors: \\\"Lalwani, Kim, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2405.02318\\\"\\n    category: fol-formalization\\n    role: background\\n    relevance: >\\n      Step-by-step NL->FOL translation using LLMs with SMT solver\\n      verification. Demonstrates the NL->formal logic pipeline that\\n      STA aims to improve via RL training.\\n    key_finding: >\\n      Neurosymbolic NL2FOL achieves 78% F1 on LOGIC dataset and\\n      generalizes to LogicClimate (80% F1), outperforming supervised\\n      models by 21%.\\n\\n  - id: logica2\\n    title: \\\"LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: \\\"IEEE/ACM TASLP 2023\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Logical reasoning evaluation benchmark derived from Chinese civil\\n      service exams. Provides supplementary evaluation for STA's\\n      formalization capabilities.\\n    key_finding: >\\n      8,678 multiple-choice questions covering categorical, disjunctive,\\n      and conditional reasoning; widely used LLM benchmark.\\n\", \"total_chars\": 20468, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "266d27e6-a157-4f2f-bd56-56f7d8e9282e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\\\", \\\"content\\\": \\\"# Literature Map for Solver Trace Ablation (STA)\\\\n# Categories:\\\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\\\n#   2. reward-shaping: Reward shaping for code/formal verification\\\\n#   3. mutation-testing: Mutation testing in software engineering\\\\n#   4. intensional-analysis: Intensional program analysis\\\\n#   5. reward-hacking: Reward hacking / overoptimization\\\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\\\n\\\\npapers:\\\\n\\\\n  # ============================================================\\\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\\\n  # ============================================================\\\\n\\\\n  - id: deepseek-r1\\\\n    title: \\\\\\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"DeepSeek-AI\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2501.12948 / Nature 2025\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: method-component\\\\n    relevance: >\\\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\\\n      intensional structural reward for neurosymbolic formalization.\\\\n    key_finding: >\\\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\\\n      showing emergent chain-of-thought reasoning from RL alone.\\\\n\\\\n  - id: deepseekmath\\\\n    title: \\\\\\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2402.03300\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: method-component\\\\n    relevance: >\\\\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\\\\n      used in STA training. GRPO eliminates the critic model by estimating\\\\n      baselines from group scores.\\\\n    key_finding: >\\\\n      GRPO matches PPO performance while significantly reducing training\\\\n      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.\\\\n\\\\n  - id: logic-rl\\\\n    title: \\\\\\\"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Xian et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2502.14768\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic\\\\n      logic puzzles. Closest competitor to STA's approach of RL for logical\\\\n      formalization, though Logic-RL uses extensional (answer-correctness)\\\\n      rewards rather than STA's intensional structural rewards.\\\\n    key_finding: >\\\\n      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;\\\\n      rule-based reward design is critical for RL-based logical reasoning.\\\\n\\\\n  - id: mellgren-prolog-grpo\\\\n    title: \\\\\\\"Training Language Models to Use Prolog as a Tool\\\\\\\"\\\\n    authors: \\\\\\\"Niklas Mellgren\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2512.07407\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,\\\\n      directly comparable to STA's approach of GRPO-training a formalizer.\\\\n      Key difference: uses pass/fail reward vs STA's structural ISR.\\\\n    key_finding: >\\\\n      GRPO is effective for teaching small LLMs to use Prolog as a tool\\\\n      for logical and mathematical reasoning.\\\\n\\\\n  - id: satlm\\\\n    title: \\\\\\\"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\\\\\\\"\\\\n    authors: \\\\\\\"Xi Ye et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"NeurIPS 2023\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: background\\\\n    relevance: >\\\\n      Neurosymbolic approach where LLM generates declarative specifications\\\\n      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)\\\\n      but uses prompting, not RL training.\\\\n    key_finding: >\\\\n      Declarative formulation outperforms imperative program-aided LMs by 23%\\\\n      on GSM; achieves SoTA on LSAT and BoardgameQA.\\\\n\\\\n  # ============================================================\\\\n  # Category 2: Reward shaping for code/formal verification\\\\n  # ============================================================\\\\n\\\\n  - id: lightman-verify-step\\\\n    title: \\\\\\\"Let's Verify Step by Step\\\\\\\"\\\\n    authors: \\\\\\\"Hunter Lightman, Vineet Kosaraju, Yura Burda, et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"arXiv 2305.20050 / ICLR 2024\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: method-component\\\\n    relevance: >\\\\n      Establishes that process supervision (step-level reward) outperforms\\\\n      outcome supervision (final-answer reward) for reasoning. STA's ISR\\\\n      is analogous: it provides structural process-level signal about which\\\\n      components of a formalization matter, rather than just pass/fail.\\\\n    key_finding: >\\\\n      Process-supervised reward model achieves 78% on MATH, significantly\\\\n      outperforming outcome-supervised models. Released PRM800K dataset.\\\\n\\\\n  - id: reward-shaping-rlhf\\\\n    title: \\\\\\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\\\\\"\\\\n    authors: \\\\\\\"Jiayi Fu, Xuandong Zhao, Chengyuan Yao, et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2502.18770\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      Studies reward shaping design principles for RLHF: bounded rewards and\\\\n      rapid-then-convergent growth. STA's ISR follows these principles\\\\n      naturally since structural necessity scores are bounded [0,1].\\\\n    key_finding: >\\\\n      Two key reward shaping principles: (1) bounded RL reward, (2) rapid\\\\n      initial growth with gradual convergence. PAR method achieves 5%+\\\\n      win rate improvement on AlpacaEval 2.0.\\\\n\\\\n  - id: rlvr-reasoning\\\\n    title: \\\\\\\"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2506.14245\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize\\\\n      reasoning. STA argues that for neurosymbolic formalization, binary reward\\\\n      is insufficient and structural reward is needed to avoid reward hacking.\\\\n    key_finding: >\\\\n      RLVR with binary verification implicitly teaches correct reasoning\\\\n      strategies, not just answer matching.\\\\n\\\\n  - id: rubric-grpo\\\\n    title: \\\\\\\"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2605.08061\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Uses structured rubric-based rewards with GRPO, similar in spirit to\\\\n      STA's structured ISR. Key difference: rubric rewards come from LLM\\\\n      judges, while ISR comes from solver-based mutation testing.\\\\n    key_finding: >\\\\n      Structured multi-dimensional reward signals improve GRPO training\\\\n      generalization compared to scalar rewards.\\\\n\\\\n  # ============================================================\\\\n  # Category 3: Mutation testing in software engineering\\\\n  # ============================================================\\\\n\\\\n  - id: demillo1978\\\\n    title: \\\\\\\"Hints on Test Data Selection: Help for the Practicing Programmer\\\\\\\"\\\\n    authors: \\\\\\\"Richard A. DeMillo, Richard J. Lipton, Frederick G. Sayward\\\\\\\"\\\\n    year: 1978\\\\n    venue: \\\\\\\"Computer 11(4):34-43\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Foundational paper introducing mutation testing. STA's component\\\\n      necessity testing directly extends this idea: instead of mutating\\\\n      source code to test test suites, STA mutates logical formulas\\\\n      to test component necessity for solver success.\\\\n    key_finding: >\\\\n      Introduced mutation testing and the coupling effect hypothesis:\\\\n      tests that detect simple faults also detect complex faults.\\\\n\\\\n  - id: offutt-coupling\\\\n    title: \\\\\\\"Investigations of the Software Testing Coupling Effect\\\\\\\"\\\\n    authors: \\\\\\\"A. Jefferson Offutt\\\\\\\"\\\\n    year: 1992\\\\n    venue: \\\\\\\"ACM TOSEM 1(1):5-20\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Empirically validates the coupling effect hypothesis that underpins\\\\n      mutation testing. STA's single-component ablation is analogous to\\\\n      first-order mutation; the coupling effect suggests this suffices.\\\\n    key_finding: >\\\\n      Test data killing all first-order mutants killed >99% of second-\\\\n      and third-order mutants, validating the coupling effect.\\\\n\\\\n  - id: jia-harman-survey\\\\n    title: \\\\\\\"An Analysis and Survey of the Development of Mutation Testing\\\\\\\"\\\\n    authors: \\\\\\\"Yue Jia, Mark Harman\\\\\\\"\\\\n    year: 2011\\\\n    venue: \\\\\\\"IEEE TSE 37(5):649-678\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Comprehensive survey of mutation testing covering three decades of\\\\n      development. Provides theoretical and practical foundation for STA's\\\\n      adaptation of mutation testing to logical formulas.\\\\n    key_finding: >\\\\n      Systematic classification of mutation operators, cost reduction\\\\n      techniques, and equivalence problem -- all relevant to STA's design\\\\n      of clause-level ablation operators.\\\\n\\\\n  - id: just-mutants-real-faults\\\\n    title: \\\\\\\"Are Mutants a Valid Substitute for Real Faults in Software Testing?\\\\\\\"\\\\n    authors: \\\\\\\"Rene Just, Darioush Jalali, Laura Inozemtseva, et al.\\\\\\\"\\\\n    year: 2014\\\\n    venue: \\\\\\\"FSE 2014\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Validates that mutation testing (structural/intensional analysis of\\\\n      program adequacy) correlates with real fault detection. Supports STA's\\\\n      premise that structural analysis of formalization components provides\\\\n      meaningful signal about formalization quality.\\\\n    key_finding: >\\\\n      Mutant detection is statistically correlated with real fault detection,\\\\n      and mutation score is a better predictor of test effectiveness than\\\\n      code coverage.\\\\n\\\\n  - id: llmorpheus\\\\n    title: \\\\\\\"LLMorpheus: Mutation Testing Using Large Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Frank Tip, Jon Bell, et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"IEEE TSE 2025\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Uses LLMs to generate realistic code mutants beyond traditional\\\\n      mutation operators. Shows mutation testing evolving toward\\\\n      ML-integrated approaches, validating STA's cross-pollination\\\\n      of mutation testing ideas into ML training.\\\\n    key_finding: >\\\\n      LLM-generated mutants simulate real bugs that rule-based operators\\\\n      cannot produce, improving mutation testing realism.\\\\n\\\\n  - id: mutation-guided-meta\\\\n    title: \\\\\\\"Mutation-Guided LLM-based Test Generation at Meta\\\\\\\"\\\\n    authors: \\\\\\\"Christopher Foster et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"FSE 2025\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Industrial application of mutation-guided LLM test generation at\\\\n      Meta. Demonstrates that mutation analysis can guide LLM behavior\\\\n      in production -- analogous to how STA uses mutation (ablation) to\\\\n      guide GRPO reward signal.\\\\n    key_finding: >\\\\n      Mutation-guided approach generates tests that kill significantly\\\\n      more mutants than unguided LLM test generation at Meta scale.\\\\n\\\\n  - id: mutation-consistency-llm\\\\n    title: \\\\\\\"Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2401.05940\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Uses code mutations to evaluate LLM code understanding consistency.\\\\n      Conceptually related to STA: both use systematic code/formula\\\\n      mutations to assess model capabilities.\\\\n    key_finding: >\\\\n      LLMs show significant inconsistency when evaluated on mutated code\\\\n      variants, suggesting superficial pattern matching.\\\\n\\\\n  # ============================================================\\\\n  # Category 4: Intensional program analysis\\\\n  # ============================================================\\\\n\\\\n  - id: deepmutation\\\\n    title: \\\\\\\"A Probabilistic Framework for Mutation Testing in Deep Neural Networks\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"Information and Software Technology 2023\\\\\\\"\\\\n    category: intensional-analysis\\\\n    role: background\\\\n    relevance: >\\\\n      Extends mutation testing to DNN testing with probabilistic mutation\\\\n      operators. Parallel to STA's extension of mutation testing from\\\\n      traditional programs to logical formulas.\\\\n    key_finding: >\\\\n      Probabilistic mutation framework enables meaningful test adequacy\\\\n      assessment for neural networks through structural perturbation.\\\\n\\\\n  # ============================================================\\\\n  # Category 5: Reward hacking / overoptimization\\\\n  # ============================================================\\\\n\\\\n  - id: inform-reward-hacking\\\\n    title: \\\\\\\"InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"NeurIPS 2024\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: background\\\\n    relevance: >\\\\n      Proposes information-bottleneck approach to detect and mitigate reward\\\\n      hacking. STA's ISR addresses the same problem differently: by grounding\\\\n      reward in verifiable structural properties (component necessity), it\\\\n      reduces the attack surface for reward hacking.\\\\n    key_finding: >\\\\n      Variational information bottleneck filters irrelevant features from\\\\n      reward model; Cluster Separation Index detects reward overoptimization.\\\\n\\\\n  - id: mo-grpo\\\\n    title: \\\\\\\"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\\\\\\\"\\\\n    authors: \\\\\\\"CyberAgent AI Lab\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2509.22047\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: background\\\\n    relevance: >\\\\n      Directly addresses GRPO reward hacking in multi-objective settings.\\\\n      STA's ISR can be viewed as adding a structural objective to the\\\\n      correctness objective, making MO-GRPO's insights directly applicable.\\\\n    key_finding: >\\\\n      Standard GRPO normalizes after summing rewards, allowing high-variance\\\\n      objectives to dominate. MO-GRPO equalizes scales before aggregation.\\\\n\\\\n  - id: reward-hacking-survey\\\\n    title: \\\\\\\"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv 2604.13602\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: background\\\\n    relevance: >\\\\n      Comprehensive survey of reward hacking mechanisms in the LLM era.\\\\n      Provides theoretical framework for understanding why STA's structural\\\\n      reward is more robust than pure outcome-based reward.\\\\n    key_finding: >\\\\n      Reward hacking manifests through specification gaming, reward model\\\\n      exploitation, and emergent misalignment; structural verification\\\\n      rewards are more robust than learned reward models.\\\\n\\\\n  - id: energy-loss-reward-hacking\\\\n    title: \\\\\\\"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"ICML 2025\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: background\\\\n    relevance: >\\\\n      Identifies energy loss in LLM final layer as an indicator of reward\\\\n      hacking during RL. Provides complementary diagnostic to STA's\\\\n      structural reward approach.\\\\n    key_finding: >\\\\n      Energy loss in the final layer increases during RL and excessive\\\\n      increase characterizes reward hacking; EPPO algorithm penalizes\\\\n      this to mitigate hacking.\\\\n\\\\n  # ============================================================\\\\n  # Category 6: FOL/Prolog formalization with LLMs\\\\n  # ============================================================\\\\n\\\\n  - id: folio\\\\n    title: \\\\\\\"FOLIO: Natural Language Reasoning with First-Order Logic\\\\\\\"\\\\n    authors: \\\\\\\"Simeng Han et al.\\\\\\\"\\\\n    year: 2022\\\\n    venue: \\\\\\\"arXiv 2209.00840 / EMNLP 2024\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: evaluation\\\\n    relevance: >\\\\n      Primary FOL reasoning benchmark. STA uses FOLIO-style NL->FOL\\\\n      formalization as the target task for GRPO training. FOLIO's\\\\n      expert-annotated FOL annotations serve as reference formalizations.\\\\n    key_finding: >\\\\n      1,430 NL-FOL paired examples with reasoning depths up to 5+;\\\\n      GPT-4 still struggles on the hardest examples.\\\\n\\\\n  - id: proofwriter\\\\n    title: \\\\\\\"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language\\\\\\\"\\\\n    authors: \\\\\\\"Oyvind Tafjord, Bhavana Dalvi, Peter Clark\\\\\\\"\\\\n    year: 2021\\\\n    venue: \\\\\\\"Findings of ACL-IJCNLP 2021\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: evaluation\\\\n    relevance: >\\\\n      Source dataset for STA's training data. ProofWriter provides\\\\n      rule-based logical reasoning problems in natural language that\\\\n      STA uses for training formalizer models.\\\\n    key_finding: >\\\\n      Generative model can reliably produce implications and proofs;\\\\n      accuracy exceeds prior methods by 9% and generalizes to unseen\\\\n      proof depths.\\\\n\\\\n  - id: logic-lm\\\\n    title: \\\\\\\"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Liangming Pan, Alon Albalak, Xinyi Wang, William Wang\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"Findings of EMNLP 2023\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      LLM->symbolic solver pipeline for logical reasoning, directly\\\\n      comparable to STA's formalizer->Prolog solver pipeline. Key\\\\n      difference: Logic-LM uses prompting, STA uses GRPO training.\\\\n    key_finding: >\\\\n      LLM+solver achieves 39.2% improvement over LLM-alone on logical\\\\n      reasoning benchmarks including ProofWriter and FOLIO.\\\\n\\\\n  - id: linc\\\\n    title: \\\\\\\"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers\\\\\\\"\\\\n    authors: \\\\\\\"Theo X. Olausson, Alex Gu, Ben Lipkin, et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"EMNLP 2023\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Neurosymbolic approach where LLM translates NL to FOL for theorem\\\\n      prover. Directly comparable to STA's NL->Prolog translation.\\\\n      LINC uses prompting-based approach; STA uses RL training.\\\\n    key_finding: >\\\\n      StarCoder+ (15.5B) with LINC outperforms GPT-3.5 and GPT-4 with\\\\n      CoT by 38% and 10% respectively on ProofWriter.\\\\n\\\\n  - id: fover\\\\n    title: \\\\\\\"FoVer: First-Order Logic Verification for Natural Language Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Yu Pei, Yongping Du, Xingnan Jin\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"TACL 13:1340-1359\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Uses LLM->FOL->Z3 pipeline for verifying NL reasoning correctness.\\\\n      Similar to STA's verification pipeline but focuses on post-hoc\\\\n      verification rather than training reward signal.\\\\n    key_finding: >\\\\n      FOL verification via Z3 significantly outperforms existing methods\\\\n      on ProofWriter and FOLIO benchmarks.\\\\n\\\\n  - id: lorp\\\\n    title: \\\\\\\"LoRP: LLM-based Logical Reasoning via Prolog\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"Knowledge-Based Systems 2025\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      LLM->Prolog pipeline with FOL-to-Prolog translation mechanism.\\\\n      Closest to STA's formalization target (Prolog), though LoRP\\\\n      uses prompting while STA uses GRPO training with structural reward.\\\\n    key_finding: >\\\\n      Systematic FOL-to-Prolog translation extends Prolog expressiveness;\\\\n      achieves SoTA accuracy on logical reasoning with three-vote majority.\\\\n\\\\n  - id: nl2fol\\\\n    title: \\\\\\\"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection\\\\\\\"\\\\n    authors: \\\\\\\"Lalwani, Kim, et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2405.02318\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: background\\\\n    relevance: >\\\\n      Step-by-step NL->FOL translation using LLMs with SMT solver\\\\n      verification. Demonstrates the NL->formal logic pipeline that\\\\n      STA aims to improve via RL training.\\\\n    key_finding: >\\\\n      Neurosymbolic NL2FOL achieves 78% F1 on LOGIC dataset and\\\\n      generalizes to LogicClimate (80% F1), outperforming supervised\\\\n      models by 21%.\\\\n\\\\n  - id: logica2\\\\n    title: \\\\\\\"LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding\\\\\\\"\\\\n    authors: \\\\\\\"Liu et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"IEEE/ACM TASLP 2023\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: evaluation\\\\n    relevance: >\\\\n      Logical reasoning evaluation benchmark derived from Chinese civil\\\\n      service exams. Provides supplementary evaluation for STA's\\\\n      formalization capabilities.\\\\n    key_finding: >\\\\n      8,678 multiple-choice questions covering categorical, disjunctive,\\\\n      and conditional reasoning; widely used LLM benchmark.\\\\n\\\", \\\"total_chars\\\": 20468, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\", \"content\": \"# Literature Map for Solver Trace Ablation (STA)\\n# Categories:\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\n#   2. reward-shaping: Reward shaping for code/formal verification\\n#   3. mutation-testing: Mutation testing in software engineering\\n#   4. intensional-analysis: Intensional program analysis\\n#   5. reward-hacking: Reward hacking / overoptimization\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\n\\npapers:\\n\\n  # ============================================================\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\n  # ============================================================\\n\\n  - id: deepseek-r1\\n    title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n    authors: \\\"DeepSeek-AI\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2501.12948 / Nature 2025\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\n      intensional structural reward for neurosymbolic formalization.\\n    key_finding: >\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\n      showing emergent chain-of-thought reasoning from RL alone.\\n\\n  - id: deepseekmath\\n    title: \\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\"\\n    authors: \\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2402.03300\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\\n      used in STA training. GRPO eliminates the critic model by estimating\\n      baselines from group scores.\\n    key_finding: >\\n      GRPO matches PPO performance while significantly reducing training\\n      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.\\n\\n  - id: logic-rl\\n    title: \\\"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\\\"\\n    authors: \\\"Xian et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.14768\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic\\n      logic puzzles. Closest competitor to STA's approach of RL for logical\\n      formalization, though Logic-RL uses extensional (answer-correctness)\\n      rewards rather than STA's intensional structural rewards.\\n    key_finding: >\\n      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;\\n      rule-based reward design is critical for RL-based logical reasoning.\\n\\n  - id: mellgren-prolog-grpo\\n    title: \\\"Training Language Models to Use Prolog as a Tool\\\"\\n    authors: \\\"Niklas Mellgren\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2512.07407\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,\\n      directly comparable to STA's approach of GRPO-training a formalizer.\\n      Key difference: uses pass/fail reward vs STA's structural ISR.\\n    key_finding: >\\n      GRPO is effective for teaching small LLMs to use Prolog as a tool\\n      for logical and mathematical reasoning.\\n\\n  - id: satlm\\n    title: \\\"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\\\"\\n    authors: \\\"Xi Ye et al.\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023\\\"\\n    category: neurosymbolic-rl\\n    role: background\\n    relevance: >\\n      Neurosymbolic approach where LLM generates declarative specifications\\n      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)\\n      but uses prompting, not RL training.\\n    key_finding: >\\n      Declarative formulation outperforms imperative program-aided LMs by 23%\\n      on GSM; achieves SoTA on LSAT and BoardgameQA.\\n\\n  # ============================================================\\n  # Category 2: Reward shaping for code/formal verification\\n  # ============================================================\\n\\n  - id: lightman-verify-step\\n    title: \\\"Let's Verify Step by Step\\\"\\n    authors: \\\"Hunter Lightman, Vineet Kosaraju, Yura Burda, et al.\\\"\\n    year: 2023\\n    venue: \\\"arXiv 2305.20050 / ICLR 2024\\\"\\n    category: reward-shaping\\n    role: method-component\\n    relevance: >\\n      Establishes that process supervision (step-level reward) outperforms\\n      outcome supervision (final-answer reward) for reasoning. STA's ISR\\n      is analogous: it provides structural process-level signal about which\\n      components of a formalization matter, rather than just pass/fail.\\n    key_finding: >\\n      Process-supervised reward model achieves 78% on MATH, significantly\\n      outperforming outcome-supervised models. Released PRM800K dataset.\\n\\n  - id: reward-shaping-rlhf\\n    title: \\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\"\\n    authors: \\\"Jiayi Fu, Xuandong Zhao, Chengyuan Yao, et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.18770\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Studies reward shaping design principles for RLHF: bounded rewards and\\n      rapid-then-convergent growth. STA's ISR follows these principles\\n      naturally since structural necessity scores are bounded [0,1].\\n    key_finding: >\\n      Two key reward shaping principles: (1) bounded RL reward, (2) rapid\\n      initial growth with gradual convergence. PAR method achieves 5%+\\n      win rate improvement on AlpacaEval 2.0.\\n\\n  - id: rlvr-reasoning\\n    title: \\\"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2506.14245\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize\\n      reasoning. STA argues that for neurosymbolic formalization, binary reward\\n      is insufficient and structural reward is needed to avoid reward hacking.\\n    key_finding: >\\n      RLVR with binary verification implicitly teaches correct reasoning\\n      strategies, not just answer matching.\\n\\n  - id: rubric-grpo\\n    title: \\\"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2605.08061\\\"\\n    category: reward-shaping\\n    role: direct-competitor\\n    relevance: >\\n      Uses structured rubric-based rewards with GRPO, similar in spirit to\\n      STA's structured ISR. Key difference: rubric rewards come from LLM\\n      judges, while ISR comes from solver-based mutation testing.\\n    key_finding: >\\n      Structured multi-dimensional reward signals improve GRPO training\\n      generalization compared to scalar rewards.\\n\\n  # ============================================================\\n  # Category 3: Mutation testing in software engineering\\n  # ============================================================\\n\\n  - id: demillo1978\\n    title: \\\"Hints on Test Data Selection: Help for the Practicing Programmer\\\"\\n    authors: \\\"Richard A. DeMillo, Richard J. Lipton, Frederick G. Sayward\\\"\\n    year: 1978\\n    venue: \\\"Computer 11(4):34-43\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Foundational paper introducing mutation testing. STA's component\\n      necessity testing directly extends this idea: instead of mutating\\n      source code to test test suites, STA mutates logical formulas\\n      to test component necessity for solver success.\\n    key_finding: >\\n      Introduced mutation testing and the coupling effect hypothesis:\\n      tests that detect simple faults also detect complex faults.\\n\\n  - id: offutt-coupling\\n    title: \\\"Investigations of the Software Testing Coupling Effect\\\"\\n    authors: \\\"A. Jefferson Offutt\\\"\\n    year: 1992\\n    venue: \\\"ACM TOSEM 1(1):5-20\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Empirically validates the coupling effect hypothesis that underpins\\n      mutation testing. STA's single-component ablation is analogous to\\n      first-order mutation; the coupling effect suggests this suffices.\\n    key_finding: >\\n      Test data killing all first-order mutants killed >99% of second-\\n      and third-order mutants, validating the coupling effect.\\n\\n  - id: jia-harman-survey\\n    title: \\\"An Analysis and Survey of the Development of Mutation Testing\\\"\\n    authors: \\\"Yue Jia, Mark Harman\\\"\\n    year: 2011\\n    venue: \\\"IEEE TSE 37(5):649-678\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Comprehensive survey of mutation testing covering three decades of\\n      development. Provides theoretical and practical foundation for STA's\\n      adaptation of mutation testing to logical formulas.\\n    key_finding: >\\n      Systematic classification of mutation operators, cost reduction\\n      techniques, and equivalence problem -- all relevant to STA's design\\n      of clause-level ablation operators.\\n\\n  - id: just-mutants-real-faults\\n    title: \\\"Are Mutants a Valid Substitute for Real Faults in Software Testing?\\\"\\n    authors: \\\"Rene Just, Darioush Jalali, Laura Inozemtseva, et al.\\\"\\n    year: 2014\\n    venue: \\\"FSE 2014\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Validates that mutation testing (structural/intensional analysis of\\n      program adequacy) correlates with real fault detection. Supports STA's\\n      premise that structural analysis of formalization components provides\\n      meaningful signal about formalization quality.\\n    key_finding: >\\n      Mutant detection is statistically correlated with real fault detection,\\n      and mutation score is a better predictor of test effectiveness than\\n      code coverage.\\n\\n  - id: llmorpheus\\n    title: \\\"LLMorpheus: Mutation Testing Using Large Language Models\\\"\\n    authors: \\\"Frank Tip, Jon Bell, et al.\\\"\\n    year: 2025\\n    venue: \\\"IEEE TSE 2025\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Uses LLMs to generate realistic code mutants beyond traditional\\n      mutation operators. Shows mutation testing evolving toward\\n      ML-integrated approaches, validating STA's cross-pollination\\n      of mutation testing ideas into ML training.\\n    key_finding: >\\n      LLM-generated mutants simulate real bugs that rule-based operators\\n      cannot produce, improving mutation testing realism.\\n\\n  - id: mutation-guided-meta\\n    title: \\\"Mutation-Guided LLM-based Test Generation at Meta\\\"\\n    authors: \\\"Christopher Foster et al.\\\"\\n    year: 2025\\n    venue: \\\"FSE 2025\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Industrial application of mutation-guided LLM test generation at\\n      Meta. Demonstrates that mutation analysis can guide LLM behavior\\n      in production -- analogous to how STA uses mutation (ablation) to\\n      guide GRPO reward signal.\\n    key_finding: >\\n      Mutation-guided approach generates tests that kill significantly\\n      more mutants than unguided LLM test generation at Meta scale.\\n\\n  - id: mutation-consistency-llm\\n    title: \\\"Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs\\\"\\n    authors: \\\"Various\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2401.05940\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Uses code mutations to evaluate LLM code understanding consistency.\\n      Conceptually related to STA: both use systematic code/formula\\n      mutations to assess model capabilities.\\n    key_finding: >\\n      LLMs show significant inconsistency when evaluated on mutated code\\n      variants, suggesting superficial pattern matching.\\n\\n  # ============================================================\\n  # Category 4: Intensional program analysis\\n  # ============================================================\\n\\n  - id: deepmutation\\n    title: \\\"A Probabilistic Framework for Mutation Testing in Deep Neural Networks\\\"\\n    authors: \\\"Various\\\"\\n    year: 2023\\n    venue: \\\"Information and Software Technology 2023\\\"\\n    category: intensional-analysis\\n    role: background\\n    relevance: >\\n      Extends mutation testing to DNN testing with probabilistic mutation\\n      operators. Parallel to STA's extension of mutation testing from\\n      traditional programs to logical formulas.\\n    key_finding: >\\n      Probabilistic mutation framework enables meaningful test adequacy\\n      assessment for neural networks through structural perturbation.\\n\\n  # ============================================================\\n  # Category 5: Reward hacking / overoptimization\\n  # ============================================================\\n\\n  - id: inform-reward-hacking\\n    title: \\\"InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling\\\"\\n    authors: \\\"Various\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS 2024\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Proposes information-bottleneck approach to detect and mitigate reward\\n      hacking. STA's ISR addresses the same problem differently: by grounding\\n      reward in verifiable structural properties (component necessity), it\\n      reduces the attack surface for reward hacking.\\n    key_finding: >\\n      Variational information bottleneck filters irrelevant features from\\n      reward model; Cluster Separation Index detects reward overoptimization.\\n\\n  - id: mo-grpo\\n    title: \\\"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\\\"\\n    authors: \\\"CyberAgent AI Lab\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2509.22047\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Directly addresses GRPO reward hacking in multi-objective settings.\\n      STA's ISR can be viewed as adding a structural objective to the\\n      correctness objective, making MO-GRPO's insights directly applicable.\\n    key_finding: >\\n      Standard GRPO normalizes after summing rewards, allowing high-variance\\n      objectives to dominate. MO-GRPO equalizes scales before aggregation.\\n\\n  - id: reward-hacking-survey\\n    title: \\\"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\\\"\\n    authors: \\\"Various\\\"\\n    year: 2026\\n    venue: \\\"arXiv 2604.13602\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Comprehensive survey of reward hacking mechanisms in the LLM era.\\n      Provides theoretical framework for understanding why STA's structural\\n      reward is more robust than pure outcome-based reward.\\n    key_finding: >\\n      Reward hacking manifests through specification gaming, reward model\\n      exploitation, and emergent misalignment; structural verification\\n      rewards are more robust than learned reward models.\\n\\n  - id: energy-loss-reward-hacking\\n    title: \\\"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"ICML 2025\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Identifies energy loss in LLM final layer as an indicator of reward\\n      hacking during RL. Provides complementary diagnostic to STA's\\n      structural reward approach.\\n    key_finding: >\\n      Energy loss in the final layer increases during RL and excessive\\n      increase characterizes reward hacking; EPPO algorithm penalizes\\n      this to mitigate hacking.\\n\\n  # ============================================================\\n  # Category 6: FOL/Prolog formalization with LLMs\\n  # ============================================================\\n\\n  - id: folio\\n    title: \\\"FOLIO: Natural Language Reasoning with First-Order Logic\\\"\\n    authors: \\\"Simeng Han et al.\\\"\\n    year: 2022\\n    venue: \\\"arXiv 2209.00840 / EMNLP 2024\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Primary FOL reasoning benchmark. STA uses FOLIO-style NL->FOL\\n      formalization as the target task for GRPO training. FOLIO's\\n      expert-annotated FOL annotations serve as reference formalizations.\\n    key_finding: >\\n      1,430 NL-FOL paired examples with reasoning depths up to 5+;\\n      GPT-4 still struggles on the hardest examples.\\n\\n  - id: proofwriter\\n    title: \\\"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language\\\"\\n    authors: \\\"Oyvind Tafjord, Bhavana Dalvi, Peter Clark\\\"\\n    year: 2021\\n    venue: \\\"Findings of ACL-IJCNLP 2021\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Source dataset for STA's training data. ProofWriter provides\\n      rule-based logical reasoning problems in natural language that\\n      STA uses for training formalizer models.\\n    key_finding: >\\n      Generative model can reliably produce implications and proofs;\\n      accuracy exceeds prior methods by 9% and generalizes to unseen\\n      proof depths.\\n\\n  - id: logic-lm\\n    title: \\\"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\\\"\\n    authors: \\\"Liangming Pan, Alon Albalak, Xinyi Wang, William Wang\\\"\\n    year: 2023\\n    venue: \\\"Findings of EMNLP 2023\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      LLM->symbolic solver pipeline for logical reasoning, directly\\n      comparable to STA's formalizer->Prolog solver pipeline. Key\\n      difference: Logic-LM uses prompting, STA uses GRPO training.\\n    key_finding: >\\n      LLM+solver achieves 39.2% improvement over LLM-alone on logical\\n      reasoning benchmarks including ProofWriter and FOLIO.\\n\\n  - id: linc\\n    title: \\\"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers\\\"\\n    authors: \\\"Theo X. Olausson, Alex Gu, Ben Lipkin, et al.\\\"\\n    year: 2023\\n    venue: \\\"EMNLP 2023\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      Neurosymbolic approach where LLM translates NL to FOL for theorem\\n      prover. Directly comparable to STA's NL->Prolog translation.\\n      LINC uses prompting-based approach; STA uses RL training.\\n    key_finding: >\\n      StarCoder+ (15.5B) with LINC outperforms GPT-3.5 and GPT-4 with\\n      CoT by 38% and 10% respectively on ProofWriter.\\n\\n  - id: fover\\n    title: \\\"FoVer: First-Order Logic Verification for Natural Language Reasoning\\\"\\n    authors: \\\"Yu Pei, Yongping Du, Xingnan Jin\\\"\\n    year: 2025\\n    venue: \\\"TACL 13:1340-1359\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      Uses LLM->FOL->Z3 pipeline for verifying NL reasoning correctness.\\n      Similar to STA's verification pipeline but focuses on post-hoc\\n      verification rather than training reward signal.\\n    key_finding: >\\n      FOL verification via Z3 significantly outperforms existing methods\\n      on ProofWriter and FOLIO benchmarks.\\n\\n  - id: lorp\\n    title: \\\"LoRP: LLM-based Logical Reasoning via Prolog\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"Knowledge-Based Systems 2025\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      LLM->Prolog pipeline with FOL-to-Prolog translation mechanism.\\n      Closest to STA's formalization target (Prolog), though LoRP\\n      uses prompting while STA uses GRPO training with structural reward.\\n    key_finding: >\\n      Systematic FOL-to-Prolog translation extends Prolog expressiveness;\\n      achieves SoTA accuracy on logical reasoning with three-vote majority.\\n\\n  - id: nl2fol\\n    title: \\\"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection\\\"\\n    authors: \\\"Lalwani, Kim, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2405.02318\\\"\\n    category: fol-formalization\\n    role: background\\n    relevance: >\\n      Step-by-step NL->FOL translation using LLMs with SMT solver\\n      verification. Demonstrates the NL->formal logic pipeline that\\n      STA aims to improve via RL training.\\n    key_finding: >\\n      Neurosymbolic NL2FOL achieves 78% F1 on LOGIC dataset and\\n      generalizes to LogicClimate (80% F1), outperforming supervised\\n      models by 21%.\\n\\n  - id: logica2\\n    title: \\\"LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: \\\"IEEE/ACM TASLP 2023\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Logical reasoning evaluation benchmark derived from Chinese civil\\n      service exams. Provides supplementary evaluation for STA's\\n      formalization capabilities.\\n    key_finding: >\\n      8,678 multiple-choice questions covering categorical, disjunctive,\\n      and conditional reasoning; widely used LLM benchmark.\\n\", \"total_chars\": 20468, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 63_

<details><summary>Logged reasoning block</summary>

```text
Now I need to add the 5 new papers to the literature_map.yaml. I'll add them under the reward-shaping category. Let me construct the new entries.

I'll add them after the existing reward-shaping entries (after rubric-grpo) and before the mutation-testing section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "49fd1413-cba7-433d-83ef-334f6bb1e3c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019L21zCZwhMuWJXxVVrd189",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6774,
      "cache_read_input_tokens": 57440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6774
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

<details open><summary>🔧 Tool call — Read · `toolu_01QgAcgY4eh77BRoAPy7o9By`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
  "offset": 0,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "edf49f18-0b5a-4038-983f-e54cc1c9797e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019L21zCZwhMuWJXxVVrd189",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6774,
      "cache_read_input_tokens": 57440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6774
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

_source line 65 · 2026-05-14T02:08:02.087Z_

<details><summary>↩ Tool result · `toolu_01QgAcgY4eh77BRoAPy7o9By`</summary>

```text
0	# Literature Map for Solver Trace Ablation (STA)
1	# Categories:
2	#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO
3	#   2. reward-shaping: Reward shaping for code/formal verification
4	#   3. mutation-testing: Mutation testing in software engineering
5	#   4. intensional-analysis: Intensional program analysis
6	#   5. reward-hacking: Reward hacking / overoptimization
7	#   6. fol-formalization: FOL/Prolog formalization with LLMs
8	
9	papers:
10	
11	  # ============================================================
12	  # Category 1: Neurosymbolic reasoning + RL/GRPO
13	  # ============================================================
14	
15	  - id: deepseek-r1
16	    title: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
17	    authors: "DeepSeek-AI"
18	    year: 2025
19	    venue: "arXiv 2501.12948 / Nature 2025"
20	    category: neurosymbolic-rl
21	    role: method-component
22	    relevance: >
23	      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.
24	      STA builds on the same GRPO framework but replaces binary outcome reward with
25	      intensional structural reward for neurosymbolic formalization.
26	    key_finding: >
27	      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,
28	      showing emergent chain-of-thought reasoning from RL alone.
29	
30	  - id: deepseekmath
31	    title: "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models"
32	    authors: "Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al."
33	    year: 2024
34	    venue: "arXiv 2402.03300"
35	    category: neurosymbolic-rl
36	    role: method-component
37	    relevance: >
38	      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm
39	      used in STA training. GRPO eliminates the critic model by estimating
40	      baselines from group scores.
41	    key_finding: >
42	      GRPO matches PPO performance while significantly reducing training
43	      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.
44	
45	  - id: logic-rl
46	    title: "Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning"
47	    authors: "Xian et al."
48	    year: 2025
49	    venue: "arXiv 2502.14768"
50	    category: neurosymbolic-rl
51	    role: direct-competitor
52	    relevance: >
53	      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic
54	      logic puzzles. Closest competitor to STA's approach of RL for logical
55	      formalization, though Logic-RL uses extensional (answer-correctness)
56	      rewards rather than STA's intensional structural rewards.
57	    key_finding: >
58	      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;
59	      rule-based reward design is critical for RL-based logical reasoning.
60	
61	  - id: mellgren-prolog-grpo
62	    title: "Training Language Models to Use Prolog as a Tool"
63	    authors: "Niklas Mellgren"
64	    year: 2024
65	    venue: "arXiv 2512.07407"
66	    category: neurosymbolic-rl
67	    role: direct-competitor
68	    relevance: >
69	      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,
70	      directly comparable to STA's approach of GRPO-training a formalizer.
71	      Key difference: uses pass/fail reward vs STA's structural ISR.
72	    key_finding: >
73	      GRPO is effective for teaching small LLMs to use Prolog as a tool
74	      for logical and mathematical reasoning.
75	
76	  - id: satlm
77	    title: "SatLM: Satisfiability-Aided Language Models Using Declarative Prompting"
78	    authors: "Xi Ye et al."
79	    year: 2023
80	    venue: "NeurIPS 2023"
81	    category: neurosymbolic-rl
82	    role: background
83	    relevance: >
84	      Neurosymbolic approach where LLM generates declarative specifications
85	      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)
86	      but uses prompting, not RL training.
87	    key_finding: >
88	      Declarative formulation outperforms imperative program-aided LMs by 23%
89	      on GSM; achieves SoTA on LSAT and BoardgameQA.
90	
91	  # ============================================================
92	  # Category 2: Reward shaping for code/formal verification
93	  # ============================================================
94	
95	  - id: lightman-verify-step
96	    title: "Let's Verify Step by Step"
97	    authors: "Hunter Lightman, Vineet Kosaraju, Yura Burda, et al."
98	    year: 2023
99	    venue: "arXiv 2305.20050 / ICLR 2024"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "a166a15d-2adc-48d4-b577-981428ff481a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
      "content": "# Literature Map for Solver Trace Ablation (STA)\n# Categories:\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\n#   2. reward-shaping: Reward shaping for code/formal verification\n#   3. mutation-testing: Mutation testing in software engineering\n#   4. intensional-analysis: Intensional program analysis\n#   5. reward-hacking: Reward hacking / overoptimization\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\n\npapers:\n\n  # ============================================================\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\n  # ============================================================\n\n  - id: deepseek-r1\n    title: \"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\"\n    authors: \"DeepSeek-AI\"\n    year: 2025\n    venue: \"arXiv 2501.12948 / Nature 2025\"\n    category: neurosymbolic-rl\n    role: method-component\n    relevance: >\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\n      STA builds on the same GRPO framework but replaces binary outcome reward with\n      intensional structural reward for neurosymbolic formalization.\n    key_finding: >\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\n      showing emergent chain-of-thought reasoning from RL alone.\n\n  - id: deepseekmath\n    title: \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\"\n    authors: \"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\"\n    year: 2024\n    venue: \"arXiv 2402.03300\"\n    category: neurosymbolic-rl\n    role: method-component\n    relevance: >\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\n      used in STA training. GRPO eliminates the critic model by estimating\n      baselines from group scores.\n    key_finding: >\n      GRPO matches PPO performance while significantly reducing training\n      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.\n\n  - id: logic-rl\n    title: \"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\"\n    authors: \"Xian et al.\"\n    year: 2025\n    venue: \"arXiv 2502.14768\"\n    category: neurosymbolic-rl\n    role: direct-competitor\n    relevance: >\n      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic\n      logic puzzles. Closest competitor to STA's approach of RL for logical\n      formalization, though Logic-RL uses extensional (answer-correctness)\n      rewards rather than STA's intensional structural rewards.\n    key_finding: >\n      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;\n      rule-based reward design is critical for RL-based logical reasoning.\n\n  - id: mellgren-prolog-grpo\n    title: \"Training Language Models to Use Prolog as a Tool\"\n    authors: \"Niklas Mellgren\"\n    year: 2024\n    venue: \"arXiv 2512.07407\"\n    category: neurosymbolic-rl\n    role: direct-competitor\n    relevance: >\n      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,\n      directly comparable to STA's approach of GRPO-training a formalizer.\n      Key difference: uses pass/fail reward vs STA's structural ISR.\n    key_finding: >\n      GRPO is effective for teaching small LLMs to use Prolog as a tool\n      for logical and mathematical reasoning.\n\n  - id: satlm\n    title: \"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\"\n    authors: \"Xi Ye et al.\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    category: neurosymbolic-rl\n    role: background\n    relevance: >\n      Neurosymbolic approach where LLM generates declarative specifications\n      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)\n      but uses prompting, not RL training.\n    key_finding: >\n      Declarative formulation outperforms imperative program-aided LMs by 23%\n      on GSM; achieves SoTA on LSAT and BoardgameQA.\n\n  # ============================================================\n  # Category 2: Reward shaping for code/formal verification\n  # ============================================================\n\n  - id: lightman-verify-step\n    title: \"Let's Verify Step by Step\"\n    authors: \"Hunter Lightman, Vineet Kosaraju, Yura Burda, et al.\"\n    year: 2023\n    venue: \"arXiv 2305.20050 / ICLR 2024\"",
      "numLines": 100,
      "startLine": 0,
      "totalLines": 484
    }
  }
}
```

</details>

---

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — Read · `toolu_01PyivvVRBTwmV7K1nk4KPX6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
  "offset": 130,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "63f66874-e5a2-468e-be45-28cd2a486cac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PG4y8VjJLjinW9P1Ay2iAs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1733,
      "cache_read_input_tokens": 64214,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1733
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

_source line 67 · 2026-05-14T02:08:07.391Z_

<details><summary>↩ Tool result · `toolu_01PyivvVRBTwmV7K1nk4KPX6`</summary>

```text
130	    authors: "Various"
131	    year: 2025
132	    venue: "arXiv 2506.14245"
133	    category: reward-shaping
134	    role: background
135	    relevance: >
136	      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize
137	      reasoning. STA argues that for neurosymbolic formalization, binary reward
138	      is insufficient and structural reward is needed to avoid reward hacking.
139	    key_finding: >
140	      RLVR with binary verification implicitly teaches correct reasoning
141	      strategies, not just answer matching.
142	
143	  - id: rubric-grpo
144	    title: "Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning"
145	    authors: "Various"
146	    year: 2025
147	    venue: "arXiv 2605.08061"
148	    category: reward-shaping
149	    role: direct-competitor
150	    relevance: >
151	      Uses structured rubric-based rewards with GRPO, similar in spirit to
152	      STA's structured ISR. Key difference: rubric rewards come from LLM
153	      judges, while ISR comes from solver-based mutation testing.
154	    key_finding: >
155	      Structured multi-dimensional reward signals improve GRPO training
156	      generalization compared to scalar rewards.
157	
158	  # ============================================================
159	  # Category 3: Mutation testing in software engineering
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "c43b38cb-64d0-4506-a194-2bc80a000ad1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
      "content": "    authors: \"Various\"\n    year: 2025\n    venue: \"arXiv 2506.14245\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize\n      reasoning. STA argues that for neurosymbolic formalization, binary reward\n      is insufficient and structural reward is needed to avoid reward hacking.\n    key_finding: >\n      RLVR with binary verification implicitly teaches correct reasoning\n      strategies, not just answer matching.\n\n  - id: rubric-grpo\n    title: \"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning\"\n    authors: \"Various\"\n    year: 2025\n    venue: \"arXiv 2605.08061\"\n    category: reward-shaping\n    role: direct-competitor\n    relevance: >\n      Uses structured rubric-based rewards with GRPO, similar in spirit to\n      STA's structured ISR. Key difference: rubric rewards come from LLM\n      judges, while ISR comes from solver-based mutation testing.\n    key_finding: >\n      Structured multi-dimensional reward signals improve GRPO training\n      generalization compared to scalar rewards.\n\n  # ============================================================\n  # Category 3: Mutation testing in software engineering",
      "numLines": 30,
      "startLine": 130,
      "totalLines": 484
    }
  }
}
```

</details>

---

### Tool call

_source line 68_

<details open><summary>🔧 Tool call — Edit · `toolu_01G6eu722d6RNG2YCz5Qbe5c`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
  "old_string": "  # ============================================================\n  # Category 3: Mutation testing in software engineering",
  "new_string": "  - id: gao-effective-rl-reward\n    title: \"On Designing Effective RL Reward at Training Time for LLM Reasoning\"\n    authors: \"Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu\"\n    year: 2024\n    venue: \"arXiv 2410.15115\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Demonstrates that learned process/outcome reward models can hurt RL\n      training, producing worse performance than simple success reward only.\n      Directly explains plan005 NEGATIVE: STA's ISR as auxiliary process\n      reward degrades prove_rate compared to exec-only baseline.\n    key_finding: >\n      PRM/ORM rewards may NOT help or even hurt RL training vs success-only\n      reward. Solution: Clipping and Delta techniques to bound accumulated\n      reward magnitude prevent reward hacking.\n\n  - id: prof-process-outcome\n    title: \"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training\"\n    authors: \"Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal\"\n    year: 2025\n    venue: \"arXiv 2509.03403\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Shows that naively combining PRM+ORM signals leads to performance\n      degradation. PROF consistency filter retains only PRM-ORM consistent\n      samples, achieving 4%+ improvement over blending. Suggests STA should\n      only apply ISR when consistent with execution outcome.\n    key_finding: >\n      Process rewards frequently suffer from inaccuracies and reward hacking\n      susceptibility. PROF filters training data by PRM-ORM consistency,\n      outperforming naive reward blending by 4%+ accuracy.\n\n  - id: moskovitz-constrained-rlhf\n    title: \"Confronting Reward Model Overoptimization with Constrained RLHF\"\n    authors: \"Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer\"\n    year: 2023\n    venue: \"arXiv 2310.04373 / ICLR 2024\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      First study on overoptimization in composite reward models. Shows that\n      fixed-weight linear scalarization of component rewards leads to\n      degradation past a threshold. Proposes constrained RL with dynamic\n      Lagrange multiplier weighting as alternative to fixed ISR weight.\n    key_finding: >\n      Correlation between component RMs significantly affects overoptimization\n      thresholds. Constrained RL with Lagrange multipliers outperforms\n      fixed-weight reward composition.\n\n  - id: skalse-reward-hacking\n    title: \"Defining and Characterizing Reward Hacking\"\n    authors: \"Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger\"\n    year: 2022\n    venue: \"arXiv 2209.13085 / NeurIPS 2022\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Formal proof that for stochastic policies, two reward functions are\n      unhackable only if one is constant. Theoretically explains why any\n      non-zero ISR weight can decrease prove_rate -- this is a fundamental\n      property of reward composition, not STA-specific.\n    key_finding: >\n      Any non-constant proxy reward can decrease true reward when optimized.\n      Unhackability requires the proxy to be constant, making all non-trivial\n      auxiliary rewards theoretically vulnerable to degrading primary performance.\n\n  - id: progrs-outcome-conditioned\n    title: \"LLM Reasoning with Process Rewards for Outcome-Guided Steps\"\n    authors: \"Mohammad Rezaei, Jens Lehmann, Sahar Vahdati\"\n    year: 2026\n    venue: \"arXiv 2604.02341\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      PRM scores optimized as absolute rewards amplify fluent failure modes.\n      Outcome-conditioned centering shifts incorrect trajectories' PRM scores\n      to zero mean, preserving ranking info without corrupting gradients.\n      Suggests STA should condition ISR on execution outcome.\n    key_finding: >\n      Naive process rewards induce reward hacking by rewarding locally fluent\n      but globally incorrect reasoning. Outcome-conditioned centering resolves\n      the conflict with fewer rollouts than outcome-only baselines.\n\n  # ============================================================\n  # Category 3: Mutation testing in software engineering"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "44566a87-3643-44b0-8c53-a4c685448631",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPUpPDStgcrdcWtp3KFdZ5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 516,
      "cache_read_input_tokens": 65947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 516
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

_source line 69 · 2026-05-14T02:08:39.061Z_

<details><summary>↩ Tool result · `toolu_01G6eu722d6RNG2YCz5Qbe5c`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "3e4ab5bc-fcc4-4e87-9780-07768f45e8e2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
    "oldString": "  # ============================================================\n  # Category 3: Mutation testing in software engineering",
    "newString": "  - id: gao-effective-rl-reward\n    title: \"On Designing Effective RL Reward at Training Time for LLM Reasoning\"\n    authors: \"Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu\"\n    year: 2024\n    venue: \"arXiv 2410.15115\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Demonstrates that learned process/outcome reward models can hurt RL\n      training, producing worse performance than simple success reward only.\n      Directly explains plan005 NEGATIVE: STA's ISR as auxiliary process\n      reward degrades prove_rate compared to exec-only baseline.\n    key_finding: >\n      PRM/ORM rewards may NOT help or even hurt RL training vs success-only\n      reward. Solution: Clipping and Delta techniques to bound accumulated\n      reward magnitude prevent reward hacking.\n\n  - id: prof-process-outcome\n    title: \"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training\"\n    authors: \"Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal\"\n    year: 2025\n    venue: \"arXiv 2509.03403\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Shows that naively combining PRM+ORM signals leads to performance\n      degradation. PROF consistency filter retains only PRM-ORM consistent\n      samples, achieving 4%+ improvement over blending. Suggests STA should\n      only apply ISR when consistent with execution outcome.\n    key_finding: >\n      Process rewards frequently suffer from inaccuracies and reward hacking\n      susceptibility. PROF filters training data by PRM-ORM consistency,\n      outperforming naive reward blending by 4%+ accuracy.\n\n  - id: moskovitz-constrained-rlhf\n    title: \"Confronting Reward Model Overoptimization with Constrained RLHF\"\n    authors: \"Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer\"\n    year: 2023\n    venue: \"arXiv 2310.04373 / ICLR 2024\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      First study on overoptimization in composite reward models. Shows that\n      fixed-weight linear scalarization of component rewards leads to\n      degradation past a threshold. Proposes constrained RL with dynamic\n      Lagrange multiplier weighting as alternative to fixed ISR weight.\n    key_finding: >\n      Correlation between component RMs significantly affects overoptimization\n      thresholds. Constrained RL with Lagrange multipliers outperforms\n      fixed-weight reward composition.\n\n  - id: skalse-reward-hacking\n    title: \"Defining and Characterizing Reward Hacking\"\n    authors: \"Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger\"\n    year: 2022\n    venue: \"arXiv 2209.13085 / NeurIPS 2022\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Formal proof that for stochastic policies, two reward functions are\n      unhackable only if one is constant. Theoretically explains why any\n      non-zero ISR weight can decrease prove_rate -- this is a fundamental\n      property of reward composition, not STA-specific.\n    key_finding: >\n      Any non-constant proxy reward can decrease true reward when optimized.\n      Unhackability requires the proxy to be constant, making all non-trivial\n      auxiliary rewards theoretically vulnerable to degrading primary performance.\n\n  - id: progrs-outcome-conditioned\n    title: \"LLM Reasoning with Process Rewards for Outcome-Guided Steps\"\n    authors: \"Mohammad Rezaei, Jens Lehmann, Sahar Vahdati\"\n    year: 2026\n    venue: \"arXiv 2604.02341\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      PRM scores optimized as absolute rewards amplify fluent failure modes.\n      Outcome-conditioned centering shifts incorrect trajectories' PRM scores\n      to zero mean, preserving ranking info without corrupting gradients.\n      Suggests STA should condition ISR on execution outcome.\n    key_finding: >\n      Naive process rewards induce reward hacking by rewarding locally fluent\n      but globally incorrect reasoning. Outcome-conditioned centering resolves\n      the conflict with fewer rollouts than outcome-only baselines.\n\n  # ============================================================\n  # Category 3: Mutation testing in software engineering",
    "originalFile": "# Literature Map for Solver Trace Ablation (STA)\n# Categories:\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\n#   2. reward-shaping: Reward shaping for code/formal verification\n#   3. mutation-testing: Mutation testing in software engineering\n#   4. intensional-analysis: Intensional program analysis\n#   5. reward-hacking: Reward hacking / overoptimization\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\n\npapers:\n\n  # ============================================================\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\n  # ============================================================\n\n  - id: deepseek-r1\n    title: \"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\"\n    authors: \"DeepSeek-AI\"\n    year: 2025\n    venue: \"arXiv 2501.12948 / Nature 2025\"\n    category: neurosymbolic-rl\n    role: method-component\n    relevance: >\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\n      STA builds on the same GRPO framework but replaces binary outcome reward with\n      intensional structural reward for neurosymbolic formalization.\n    key_finding: >\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\n      showing emergent chain-of-thought reasoning from RL alone.\n\n  - id: deepseekmath\n    title: \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\"\n    authors: \"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\"\n    year: 2024\n    venue: \"arXiv 2402.03300\"\n    category: neurosymbolic-rl\n    role: method-component\n    relevance: >\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\n      used in STA training. GRPO eliminates the critic model by estimating\n      baselines from group scores.\n    key_finding: >\n      GRPO matches PPO performance while significantly reducing training\n      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.\n\n  - id: logic-rl\n    title: \"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\"\n    authors: \"Xian et al.\"\n    year: 2025\n    venue: \"arXiv 2502.14768\"\n    category: neurosymbolic-rl\n    role: direct-competitor\n    relevance: >\n      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic\n      logic puzzles. Closest competitor to STA's approach of RL for logical\n      formalization, though Logic-RL uses extensional (answer-correctness)\n      rewards rather than STA's intensional structural rewards.\n    key_finding: >\n      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;\n      rule-based reward design is critical for RL-based logical reasoning.\n\n  - id: mellgren-prolog-grpo\n    title: \"Training Language Models to Use Prolog as a Tool\"\n    authors: \"Niklas Mellgren\"\n    year: 2024\n    venue: \"arXiv 2512.07407\"\n    category: neurosymbolic-rl\n    role: direct-competitor\n    relevance: >\n      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,\n      directly comparable to STA's approach of GRPO-training a formalizer.\n      Key difference: uses pass/fail reward vs STA's structural ISR.\n    key_finding: >\n      GRPO is effective for teaching small LLMs to use Prolog as a tool\n      for logical and mathematical reasoning.\n\n  - id: satlm\n    title: \"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\"\n    authors: \"Xi Ye et al.\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    category: neurosymbolic-rl\n    role: background\n    relevance: >\n      Neurosymbolic approach where LLM generates declarative specifications\n      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)\n      but uses prompting, not RL training.\n    key_finding: >\n      Declarative formulation outperforms imperative program-aided LMs by 23%\n      on GSM; achieves SoTA on LSAT and BoardgameQA.\n\n  # ============================================================\n  # Category 2: Reward shaping for code/formal verification\n  # ============================================================\n\n  - id: lightman-verify-step\n    title: \"Let's Verify Step by Step\"\n    authors: \"Hunter Lightman, Vineet Kosaraju, Yura Burda, et al.\"\n    year: 2023\n    venue: \"arXiv 2305.20050 / ICLR 2024\"\n    category: reward-shaping\n    role: method-component\n    relevance: >\n      Establishes that process supervision (step-level reward) outperforms\n      outcome supervision (final-answer reward) for reasoning. STA's ISR\n      is analogous: it provides structural process-level signal about which\n      components of a formalization matter, rather than just pass/fail.\n    key_finding: >\n      Process-supervised reward model achieves 78% on MATH, significantly\n      outperforming outcome-supervised models. Released PRM800K dataset.\n\n  - id: reward-shaping-rlhf\n    title: \"Reward Shaping to Mitigate Reward Hacking in RLHF\"\n    authors: \"Jiayi Fu, Xuandong Zhao, Chengyuan Yao, et al.\"\n    year: 2025\n    venue: \"arXiv 2502.18770\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Studies reward shaping design principles for RLHF: bounded rewards and\n      rapid-then-convergent growth. STA's ISR follows these principles\n      naturally since structural necessity scores are bounded [0,1].\n    key_finding: >\n      Two key reward shaping principles: (1) bounded RL reward, (2) rapid\n      initial growth with gradual convergence. PAR method achieves 5%+\n      win rate improvement on AlpacaEval 2.0.\n\n  - id: rlvr-reasoning\n    title: \"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs\"\n    authors: \"Various\"\n    year: 2025\n    venue: \"arXiv 2506.14245\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize\n      reasoning. STA argues that for neurosymbolic formalization, binary reward\n      is insufficient and structural reward is needed to avoid reward hacking.\n    key_finding: >\n      RLVR with binary verification implicitly teaches correct reasoning\n      strategies, not just answer matching.\n\n  - id: rubric-grpo\n    title: \"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning\"\n    authors: \"Various\"\n    year: 2025\n    venue: \"arXiv 2605.08061\"\n    category: reward-shaping\n    role: direct-competitor\n    relevance: >\n      Uses structured rubric-based rewards with GRPO, similar in spirit to\n      STA's structured ISR. Key difference: rubric rewards come from LLM\n      judges, while ISR comes from solver-based mutation testing.\n    key_finding: >\n      Structured multi-dimensional reward signals improve GRPO training\n      generalization compared to scalar rewards.\n\n  # ============================================================\n  # Category 3: Mutation testing in software engineering\n  # ============================================================\n\n  - id: demillo1978\n    title: \"Hints on Test Data Selection: Help for the Practicing Programmer\"\n    authors: \"Richard A. DeMillo, Richard J. Lipton, Frederick G. Sayward\"\n    year: 1978\n    venue: \"Computer 11(4):34-43\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Foundational paper introducing mutation testing. STA's component\n      necessity testing directly extends this idea: instead of mutating\n      source code to test test suites, STA mutates logical formulas\n      to test component necessity for solver success.\n    key_finding: >\n      Introduced mutation testing and the coupling effect hypothesis:\n      tests that detect simple faults also detect complex faults.\n\n  - id: offutt-coupling\n    title: \"Investigations of the Software Testing Coupling Effect\"\n    authors: \"A. Jefferson Offutt\"\n    year: 1992\n    venue: \"ACM TOSEM 1(1):5-20\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Empirically validates the coupling effect hypothesis that underpins\n      mutation testing. STA's single-component ablation is analogous to\n      first-order mutation; the coupling effect suggests this suffices.\n    key_finding: >\n      Test data killing all first-order mutants killed >99% of second-\n      and third-order mutants, validating the coupling effect.\n\n  - id: jia-harman-survey\n    title: \"An Analysis and Survey of the Development of Mutation Testing\"\n    authors: \"Yue Jia, Mark Harman\"\n    year: 2011\n    venue: \"IEEE TSE 37(5):649-678\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Comprehensive survey of mutation testing covering three decades of\n      development. Provides theoretical and practical foundation for STA's\n      adaptation of mutation testing to logical formulas.\n    key_finding: >\n      Systematic classification of mutation operators, cost reduction\n      techniques, and equivalence problem -- all relevant to STA's design\n      of clause-level ablation operators.\n\n  - id: just-mutants-real-faults\n    title: \"Are Mutants a Valid Substitute for Real Faults in Software Testing?\"\n    authors: \"Rene Just, Darioush Jalali, Laura Inozemtseva, et al.\"\n    year: 2014\n    venue: \"FSE 2014\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Validates that mutation testing (structural/intensional analysis of\n      program adequacy) correlates with real fault detection. Supports STA's\n      premise that structural analysis of formalization components provides\n      meaningful signal about formalization quality.\n    key_finding: >\n      Mutant detection is statistically correlated with real fault detection,\n      and mutation score is a better predictor of test effectiveness than\n      code coverage.\n\n  - id: llmorpheus\n    title: \"LLMorpheus: Mutation Testing Using Large Language Models\"\n    authors: \"Frank Tip, Jon Bell, et al.\"\n    year: 2025\n    venue: \"IEEE TSE 2025\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Uses LLMs to generate realistic code mutants beyond traditional\n      mutation operators. Shows mutation testing evolving toward\n      ML-integrated approaches, validating STA's cross-pollination\n      of mutation testing ideas into ML training.\n    key_finding: >\n      LLM-generated mutants simulate real bugs that rule-based operators\n      cannot produce, improving mutation testing realism.\n\n  - id: mutation-guided-meta\n    title: \"Mutation-Guided LLM-based Test Generation at Meta\"\n    authors: \"Christopher Foster et al.\"\n    year: 2025\n    venue: \"FSE 2025\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Industrial application of mutation-guided LLM test generation at\n      Meta. Demonstrates that mutation analysis can guide LLM behavior\n      in production -- analogous to how STA uses mutation (ablation) to\n      guide GRPO reward signal.\n    key_finding: >\n      Mutation-guided approach generates tests that kill significantly\n      more mutants than unguided LLM test generation at Meta scale.\n\n  - id: mutation-consistency-llm\n    title: \"Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs\"\n    authors: \"Various\"\n    year: 2024\n    venue: \"arXiv 2401.05940\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Uses code mutations to evaluate LLM code understanding consistency.\n      Conceptually related to STA: both use systematic code/formula\n      mutations to assess model capabilities.\n    key_finding: >\n      LLMs show significant inconsistency when evaluated on mutated code\n      variants, suggesting superficial pattern matching.\n\n  # ============================================================\n  # Category 4: Intensional program analysis\n  # ============================================================\n\n  - id: deepmutation\n    title: \"A Probabilistic Framework for Mutation Testing in Deep Neural Networks\"\n    authors: \"Various\"\n    year: 2023\n    venue: \"Information and Software Technology 2023\"\n    category: intensional-analysis\n    role: background\n    relevance: >\n      Extends mutation testing to DNN testing with probabilistic mutation\n      operators. Parallel to STA's extension of mutation testing from\n      traditional programs to logical formulas.\n    key_finding: >\n      Probabilistic mutation framework enables meaningful test adequacy\n      assessment for neural networks through structural perturbation.\n\n  # ============================================================\n  # Category 5: Reward hacking / overoptimization\n  # ============================================================\n\n  - id: inform-reward-hacking\n    title: \"InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling\"\n    authors: \"Various\"\n    year: 2024\n    venue: \"NeurIPS 2024\"\n    category: reward-hacking\n    role: background\n    relevance: >\n      Proposes information-bottleneck approach to detect and mitigate reward\n      hacking. STA's ISR addresses the same problem differently: by grounding\n      reward in verifiable structural properties (component necessity), it\n      reduces the attack surface for reward hacking.\n    key_finding: >\n      Variational information bottleneck filters irrelevant features from\n      reward model; Cluster Separation Index detects reward overoptimization.\n\n  - id: mo-grpo\n    title: \"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\"\n    authors: \"CyberAgent AI Lab\"\n    year: 2025\n    venue: \"arXiv 2509.22047\"\n    category: reward-hacking\n    role: background\n    relevance: >\n      Directly addresses GRPO reward hacking in multi-objective settings.\n      STA's ISR can be viewed as adding a structural objective to the\n      correctness objective, making MO-GRPO's insights directly applicable.\n    key_finding: >\n      Standard GRPO normalizes after summing rewards, allowing high-variance\n      objectives to dominate. MO-GRPO equalizes scales before aggregation.\n\n  - id: reward-hacking-survey\n    title: \"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\"\n    authors: \"Various\"\n    year: 2026\n    venue: \"arXiv 2604.13602\"\n    category: reward-hacking\n    role: background\n    relevance: >\n      Comprehensive survey of reward hacking mechanisms in the LLM era.\n      Provides theoretical framework for understanding why STA's structural\n      reward is more robust than pure outcome-based reward.\n    key_finding: >\n      Reward hacking manifests through specification gaming, reward model\n      exploitation, and emergent misalignment; structural verification\n      rewards are more robust than learned reward models.\n\n  - id: energy-loss-reward-hacking\n    title: \"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking\"\n    authors: \"Various\"\n    year: 2025\n    venue: \"ICML 2025\"\n    category: reward-hacking\n    role: background\n    relevance: >\n      Identifies energy loss in LLM final layer as an indicator of reward\n      hacking during RL. Provides complementary diagnostic to STA's\n      structural reward approach.\n    key_finding: >\n      Energy loss in the final layer increases during RL and excessive\n      increase characterizes reward hacking; EPPO algorithm penalizes\n      this to mitigate hacking.\n\n  # ============================================================\n  # Category 6: FOL/Prolog formalization with LLMs\n  # ============================================================\n\n  - id: folio\n    title: \"FOLIO: Natural Language Reasoning with First-Order Logic\"\n    authors: \"Simeng Han et al.\"\n    year: 2022\n    venue: \"arXiv 2209.00840 / EMNLP 2024\"\n    category: fol-formalization\n    role: evaluation\n    relevance: >\n      Primary FOL reasoning benchmark. STA uses FOLIO-style NL->FOL\n      formalization as the target task for GRPO training. FOLIO's\n      expert-annotated FOL annotations serve as reference formalizations.\n    key_finding: >\n      1,430 NL-FOL paired examples with reasoning depths up to 5+;\n      GPT-4 still struggles on the hardest examples.\n\n  - id: proofwriter\n    title: \"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language\"\n    authors: \"Oyvind Tafjord, Bhavana Dalvi, Peter Clark\"\n    year: 2021\n    venue: \"Findings of ACL-IJCNLP 2021\"\n    category: fol-formalization\n    role: evaluation\n    relevance: >\n      Source dataset for STA's training data. ProofWriter provides\n      rule-based logical reasoning problems in natural language that\n      STA uses for training formalizer models.\n    key_finding: >\n      Generative model can reliably produce implications and proofs;\n      accuracy exceeds prior methods by 9% and generalizes to unseen\n      proof depths.\n\n  - id: logic-lm\n    title: \"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\"\n    authors: \"Liangming Pan, Alon Albalak, Xinyi Wang, William Wang\"\n    year: 2023\n    venue: \"Findings of EMNLP 2023\"\n    category: fol-formalization\n    role: direct-competitor\n    relevance: >\n      LLM->symbolic solver pipeline for logical reasoning, directly\n      comparable to STA's formalizer->Prolog solver pipeline. Key\n      difference: Logic-LM uses prompting, STA uses GRPO training.\n    key_finding: >\n      LLM+solver achieves 39.2% improvement over LLM-alone on logical\n      reasoning benchmarks including ProofWriter and FOLIO.\n\n  - id: linc\n    title: \"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers\"\n    authors: \"Theo X. Olausson, Alex Gu, Ben Lipkin, et al.\"\n    year: 2023\n    venue: \"EMNLP 2023\"\n    category: fol-formalization\n    role: direct-competitor\n    relevance: >\n      Neurosymbolic approach where LLM translates NL to FOL for theorem\n      prover. Directly comparable to STA's NL->Prolog translation.\n      LINC uses prompting-based approach; STA uses RL training.\n    key_finding: >\n      StarCoder+ (15.5B) with LINC outperforms GPT-3.5 and GPT-4 with\n      CoT by 38% and 10% respectively on ProofWriter.\n\n  - id: fover\n    title: \"FoVer: First-Order Logic Verification for Natural Language Reasoning\"\n    authors: \"Yu Pei, Yongping Du, Xingnan Jin\"\n    year: 2025\n    venue: \"TACL 13:1340-1359\"\n    category: fol-formalization\n    role: direct-competitor\n    relevance: >\n      Uses LLM->FOL->Z3 pipeline for verifying NL reasoning correctness.\n      Similar to STA's verification pipeline but focuses on post-hoc\n      verification rather than training reward signal.\n    key_finding: >\n      FOL verification via Z3 significantly outperforms existing methods\n      on ProofWriter and FOLIO benchmarks.\n\n  - id: lorp\n    title: \"LoRP: LLM-based Logical Reasoning via Prolog\"\n    authors: \"Various\"\n    year: 2025\n    venue: \"Knowledge-Based Systems 2025\"\n    category: fol-formalization\n    role: direct-competitor\n    relevance: >\n      LLM->Prolog pipeline with FOL-to-Prolog translation mechanism.\n      Closest to STA's formalization target (Prolog), though LoRP\n      uses prompting while STA uses GRPO training with structural reward.\n    key_finding: >\n      Systematic FOL-to-Prolog translation extends Prolog expressiveness;\n      achieves SoTA accuracy on logical reasoning with three-vote majority.\n\n  - id: nl2fol\n    title: \"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection\"\n    authors: \"Lalwani, Kim, et al.\"\n    year: 2024\n    venue: \"arXiv 2405.02318\"\n    category: fol-formalization\n    role: background\n    relevance: >\n      Step-by-step NL->FOL translation using LLMs with SMT solver\n      verification. Demonstrates the NL->formal logic pipeline that\n      STA aims to improve via RL training.\n    key_finding: >\n      Neurosymbolic NL2FOL achieves 78% F1 on LOGIC dataset and\n      generalizes to LogicClimate (80% F1), outperforming supervised\n      models by 21%.\n\n  - id: logica2\n    title: \"LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding\"\n    authors: \"Liu et al.\"\n    year: 2023\n    venue: \"IEEE/ACM TASLP 2023\"\n    category: fol-formalization\n    role: evaluation\n    relevance: >\n      Logical reasoning evaluation benchmark derived from Chinese civil\n      service exams. Provides supplementary evaluation for STA's\n      formalization capabilities.\n    key_finding: >\n      8,678 multiple-choice questions covering categorical, disjunctive,\n      and conditional reasoning; widely used LLM benchmark.\n",
    "structuredPatch": [
      {
        "oldStart": 155,
        "oldLines": 6,
        "newStart": 155,
        "newLines": 91,
        "lines": [
          "       Structured multi-dimensional reward signals improve GRPO training",
          "       generalization compared to scalar rewards.",
          " ",
          "+  - id: gao-effective-rl-reward",
          "+    title: \"On Designing Effective RL Reward at Training Time for LLM Reasoning\"",
          "+    authors: \"Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu\"",
          "+    year: 2024",
          "+    venue: \"arXiv 2410.15115\"",
          "+    category: reward-shaping",
          "+    role: background",
          "+    relevance: >",
          "+      Demonstrates that learned process/outcome reward models can hurt RL",
          "+      training, producing worse performance than simple success reward only.",
          "+      Directly explains plan005 NEGATIVE: STA's ISR as auxiliary process",
          "+      reward degrades prove_rate compared to exec-only baseline.",
          "+    key_finding: >",
          "+      PRM/ORM rewards may NOT help or even hurt RL training vs success-only",
          "+      reward. Solution: Clipping and Delta techniques to bound accumulated",
          "+      reward magnitude prevent reward hacking.",
          "+",
          "+  - id: prof-process-outcome",
          "+    title: \"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training\"",
          "+    authors: \"Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal\"",
          "+    year: 2025",
          "+    venue: \"arXiv 2509.03403\"",
          "+    category: reward-shaping",
          "+    role: background",
          "+    relevance: >",
          "+      Shows that naively combining PRM+ORM signals leads to performance",
          "+      degradation. PROF consistency filter retains only PRM-ORM consistent",
          "+      samples, achieving 4%+ improvement over blending. Suggests STA should",
          "+      only apply ISR when consistent with execution outcome.",
          "+    key_finding: >",
          "+      Process rewards frequently suffer from inaccuracies and reward hacking",
          "+      susceptibility. PROF filters training data by PRM-ORM consistency,",
          "+      outperforming naive reward blending by 4%+ accuracy.",
          "+",
          "+  - id: moskovitz-constrained-rlhf",
          "+    title: \"Confronting Reward Model Overoptimization with Constrained RLHF\"",
          "+    authors: \"Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer\"",
          "+    year: 2023",
          "+    venue: \"arXiv 2310.04373 / ICLR 2024\"",
          "+    category: reward-shaping",
          "+    role: background",
          "+    relevance: >",
          "+      First study on overoptimization in composite reward models. Shows that",
          "+      fixed-weight linear scalarization of component rewards leads to",
          "+      degradation past a threshold. Proposes constrained RL with dynamic",
          "+      Lagrange multiplier weighting as alternative to fixed ISR weight.",
          "+    key_finding: >",
          "+      Correlation between component RMs significantly affects overoptimization",
          "+      thresholds. Constrained RL with Lagrange multipliers outperforms",
          "+      fixed-weight reward composition.",
          "+",
          "+  - id: skalse-reward-hacking",
          "+    title: \"Defining and Characterizing Reward Hacking\"",
          "+    authors: \"Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger\"",
          "+    year: 2022",
          "+    venue: \"arXiv 2209.13085 / NeurIPS 2022\"",
          "+    category: reward-shaping",
          "+    role: background",
          "+    relevance: >",
          "+      Formal proof that for stochastic policies, two reward functions are",
          "+      unhackable only if one is constant. Theoretically explains why any",
          "+      non-zero ISR weight can decrease prove_rate -- this is a fundamental",
          "+      property of reward composition, not STA-specific.",
          "+    key_finding: >",
          "+      Any non-constant proxy reward can decrease true reward when optimized.",
          "+      Unhackability requires the proxy to be constant, making all non-trivial",
          "+      auxiliary rewards theoretically vulnerable to degrading primary performance.",
          "+",
          "+  - id: progrs-outcome-conditioned",
          "+    title: \"LLM Reasoning with Process Rewards for Outcome-Guided Steps\"",
          "+    authors: \"Mohammad Rezaei, Jens Lehmann, Sahar Vahdati\"",
          "+    year: 2026",
          "+    venue: \"arXiv 2604.02341\"",
          "+    category: reward-shaping",
          "+    role: background",
          "+    relevance: >",
          "+      PRM scores optimized as absolute rewards amplify fluent failure modes.",
          "+      Outcome-conditioned centering shifts incorrect trajectories' PRM scores",
          "+      to zero mean, preserving ranking info without corrupting gradients.",
          "+      Suggests STA should condition ISR on execution outcome.",
          "+    key_finding: >",
          "+      Naive process rewards induce reward hacking by rewarding locally fluent",
          "+      but globally incorrect reasoning. Outcome-conditioned centering resolves",
          "+      the conflict with fewer rollouts than outcome-only baselines.",
          "+",
          "   # ============================================================",
          "   # Category 3: Mutation testing in software engineering",
          "   # ============================================================"
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

_source line 70_

Now save the updated literature_map.yaml via the project file system.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "fe23ab3a-ac98-4f46-a7f5-8bb7cbae9179",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017CqvDT86APGQ3y5iuAmNYU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 66463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1450
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

_source line 71_

<details open><summary>🔧 Tool call — Read · `toolu_014tiFMorXHDn9AYRnYWLiF7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "4fe24bd6-19c4-4b89-b975-f4a26dd97f08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017CqvDT86APGQ3y5iuAmNYU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 66463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1450
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

_source line 72 · 2026-05-14T02:08:42.434Z_

<details><summary>↩ Tool result · `toolu_014tiFMorXHDn9AYRnYWLiF7`</summary>

```text
1	# Literature Map for Solver Trace Ablation (STA)
2	# Categories:
3	#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO
4	#   2. reward-shaping: Reward shaping for code/formal verification
5	#   3. mutation-testing: Mutation testing in software engineering
6	#   4. intensional-analysis: Intensional program analysis
7	#   5. reward-hacking: Reward hacking / overoptimization
8	#   6. fol-formalization: FOL/Prolog formalization with LLMs
9	
10	papers:
11	
12	  # ============================================================
13	  # Category 1: Neurosymbolic reasoning + RL/GRPO
14	  # ============================================================
15	
16	  - id: deepseek-r1
17	    title: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
18	    authors: "DeepSeek-AI"
19	    year: 2025
20	    venue: "arXiv 2501.12948 / Nature 2025"
21	    category: neurosymbolic-rl
22	    role: method-component
23	    relevance: >
24	      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.
25	      STA builds on the same GRPO framework but replaces binary outcome reward with
26	      intensional structural reward for neurosymbolic formalization.
27	    key_finding: >
28	      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,
29	      showing emergent chain-of-thought reasoning from RL alone.
30	
31	  - id: deepseekmath
32	    title: "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models"
33	    authors: "Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al."
34	    year: 2024
35	    venue: "arXiv 2402.03300"
36	    category: neurosymbolic-rl
37	    role: method-component
38	    relevance: >
39	      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm
40	      used in STA training. GRPO eliminates the critic model by estimating
41	      baselines from group scores.
42	    key_finding: >
43	      GRPO matches PPO performance while significantly reducing training
44	      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.
45	
46	  - id: logic-rl
47	    title: "Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning"
48	    authors: "Xian et al."
49	    year: 2025
50	    venue: "arXiv 2502.14768"
51	    category: neurosymbolic-rl
52	    role: direct-competitor
53	    relevance: >
54	      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic
55	      logic puzzles. Closest competitor to STA's approach of RL for logical
56	      formalization, though Logic-RL uses extensional (answer-correctness)
57	      rewards rather than STA's intensional structural rewards.
58	    key_finding: >
59	      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;
60	      rule-based reward design is critical for RL-based logical reasoning.
61	
62	  - id: mellgren-prolog-grpo
63	    title: "Training Language Models to Use Prolog as a Tool"
64	    authors: "Niklas Mellgren"
65	    year: 2024
66	    venue: "arXiv 2512.07407"
67	    category: neurosymbolic-rl
68	    role: direct-competitor
69	    relevance: >
70	      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,
71	      directly comparable to STA's approach of GRPO-training a formalizer.
72	      Key difference: uses pass/fail reward vs STA's structural ISR.
73	    key_finding: >
74	      GRPO is effective for teaching small LLMs to use Prolog as a tool
75	      for logical and mathematical reasoning.
76	
77	  - id: satlm
78	    title: "SatLM: Satisfiability-Aided Language Models Using Declarative Prompting"
79	    authors: "Xi Ye et al."
80	    year: 2023
81	    venue: "NeurIPS 2023"
82	    category: neurosymbolic-rl
83	    role: background
84	    relevance: >
85	      Neurosymbolic approach where LLM generates declarative specifications
86	      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)
87	      but uses prompting, not RL training.
88	    key_finding: >
89	      Declarative formulation outperforms imperative program-aided LMs by 23%
90	      on GSM; achieves SoTA on LSAT and BoardgameQA.
91	
92	  # ============================================================
93	  # Category 2: Reward shaping for code/formal verification
94	  # ============================================================
95	
96	  - id: lightman-verify-step
97	    title: "Let's Verify Step by Step"
98	    authors: "Hunter Lightman, Vineet Kosaraju, Yura Burda, et al."
99	    year: 2023
100	    venue: "arXiv 2305.20050 / ICLR 2024"
101	    category: reward-shaping
102	    role: method-component
103	    relevance: >
104	      Establishes that process supervision (step-level reward) outperforms
105	      outcome supervision (final-answer reward) for reasoning. STA's ISR
106	      is analogous: it provides structural process-level signal about which
107	      components of a formalization matter, rather than just pass/fail.
108	    key_finding: >
109	      Process-supervised reward model achieves 78% on MATH, significantly
110	      outperforming outcome-supervised models. Released PRM800K dataset.
111	
112	  - id: reward-shaping-rlhf
113	    title: "Reward Shaping to Mitigate Reward Hacking in RLHF"
114	    authors: "Jiayi Fu, Xuandong Zhao, Chengyuan Yao, et al."
115	    year: 2025
116	    venue: "arXiv 2502.18770"
117	    category: reward-shaping
118	    role: background
119	    relevance: >
120	      Studies reward shaping design principles for RLHF: bounded rewards and
121	      rapid-then-convergent growth. STA's ISR follows these principles
122	      naturally since structural necessity scores are bounded [0,1].
123	    key_finding: >
124	      Two key reward shaping principles: (1) bounded RL reward, (2) rapid
125	      initial growth with gradual convergence. PAR method achieves 5%+
126	      win rate improvement on AlpacaEval 2.0.
127	
128	  - id: rlvr-reasoning
129	    title: "Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs"
130	    authors: "Various"
131	    year: 2025
132	    venue: "arXiv 2506.14245"
133	    category: reward-shaping
134	    role: background
135	    relevance: >
136	      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize
137	      reasoning. STA argues that for neurosymbolic formalization, binary reward
138	      is insufficient and structural reward is needed to avoid reward hacking.
139	    key_finding: >
140	      RLVR with binary verification implicitly teaches correct reasoning
141	      strategies, not just answer matching.
142	
143	  - id: rubric-grpo
144	    title: "Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning"
145	    authors: "Various"
146	    year: 2025
147	    venue: "arXiv 2605.08061"
148	    category: reward-shaping
149	    role: direct-competitor
150	    relevance: >
151	      Uses structured rubric-based rewards with GRPO, similar in spirit to
152	      STA's structured ISR. Key difference: rubric rewards come from LLM
153	      judges, while ISR comes from solver-based mutation testing.
154	    key_finding: >
155	      Structured multi-dimensional reward signals improve GRPO training
156	      generalization compared to scalar rewards.
157	
158	  - id: gao-effective-rl-reward
159	    title: "On Designing Effective RL Reward at Training Time for LLM Reasoning"
160	    authors: "Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu"
161	    year: 2024
162	    venue: "arXiv 2410.15115"
163	    category: reward-shaping
164	    role: background
165	    relevance: >
166	      Demonstrates that learned process/outcome reward models can hurt RL
167	      training, producing worse performance than simple success reward only.
168	      Directly explains plan005 NEGATIVE: STA's ISR as auxiliary process
169	      reward degrades prove_rate compared to exec-only baseline.
170	    key_finding: >
171	      PRM/ORM rewards may NOT help or even hurt RL training vs success-only
172	      reward. Solution: Clipping and Delta techniques to bound accumulated
173	      reward magnitude prevent reward hacking.
174	
175	  - id: prof-process-outcome
176	    title: "Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"
177	    authors: "Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal"
178	    year: 2025
179	    venue: "arXiv 2509.03403"
180	    category: reward-shaping
181	    role: background
182	    relevance: >
183	      Shows that naively combining PRM+ORM signals leads to performance
184	      degradation. PROF consistency filter retains only PRM-ORM consistent
185	      samples, achieving 4%+ improvement over blending. Suggests STA should
186	      only apply ISR when consistent with execution outcome.
187	    key_finding: >
188	      Process rewards frequently suffer from inaccuracies and reward hacking
189	      susceptibility. PROF filters training data by PRM-ORM consistency,
190	      outperforming naive reward blending by 4%+ accuracy.
191	
192	  - id: moskovitz-constrained-rlhf
193	    title: "Confronting Reward Model Overoptimization with Constrained RLHF"
194	    authors: "Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer"
195	    year: 2023
196	    venue: "arXiv 2310.04373 / ICLR 2024"
197	    category: reward-shaping
198	    role: background
199	    relevance: >
200	      First study on overoptimization in composite reward models. Shows that
201	      fixed-weight linear scalarization of component rewards leads to
202	      degradation past a threshold. Proposes constrained RL with dynamic
203	      Lagrange multiplier weighting as alternative to fixed ISR weight.
204	    key_finding: >
205	      Correlation between component RMs significantly affects overoptimization
206	      thresholds. Constrained RL with Lagrange multipliers outperforms
207	      fixed-weight reward composition.
208	
209	  - id: skalse-reward-hacking
210	    title: "Defining and Characterizing Reward Hacking"
211	    authors: "Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger"
212	    year: 2022
213	    venue: "arXiv 2209.13085 / NeurIPS 2022"
214	    category: reward-shaping
215	    role: background
216	    relevance: >
217	      Formal proof that for stochastic policies, two reward functions are
218	      unhackable only if one is constant. Theoretically explains why any
219	      non-zero ISR weight can decrease prove_rate -- this is a fundamental
220	      property of reward composition, not STA-specific.
221	    key_finding: >
222	      Any non-constant proxy reward can decrease true reward when optimized.
223	      Unhackability requires the proxy to be constant, making all non-trivial
224	      auxiliary rewards theoretically vulnerable to degrading primary performance.
225	
226	  - id: progrs-outcome-conditioned
227	    title: "LLM Reasoning with Process Rewards for Outcome-Guided Steps"
228	    authors: "Mohammad Rezaei, Jens Lehmann, Sahar Vahdati"
229	    year: 2026
230	    venue: "arXiv 2604.02341"
231	    category: reward-shaping
232	    role: background
233	    relevance: >
234	      PRM scores optimized as absolute rewards amplify fluent failure modes.
235	      Outcome-conditioned centering shifts incorrect trajectories' PRM scores
236	      to zero mean, preserving ranking info without corrupting gradients.
237	      Suggests STA should condition ISR on execution outcome.
238	    key_finding: >
239	      Naive process rewards induce reward hacking by rewarding locally fluent
240	      but globally incorrect reasoning. Outcome-conditioned centering resolves
241	      the conflict with fewer rollouts than outcome-only baselines.
242	
243	  # ============================================================
244	  # Category 3: Mutation testing in software engineering
245	  # ============================================================
246	
247	  - id: demillo1978
248	    title: "Hints on Test Data Selection: Help for the Practicing Programmer"
249	    authors: "Richard A. DeMillo, Richard J. Lipton, Frederick G. Sayward"
250	    year: 1978
251	    venue: "Computer 11(4):34-43"
252	    category: mutation-testing
253	    role: background
254	    relevance: >
255	      Foundational paper introducing mutation testing. STA's component
256	      necessity testing directly extends this idea: instead of mutating
257	      source code to test test suites, STA mutates logical formulas
258	      to test component necessity for solver success.
259	    key_finding: >
260	      Introduced mutation testing and the coupling effect hypothesis:
261	      tests that detect simple faults also detect complex faults.
262	
263	  - id: offutt-coupling
264	    title: "Investigations of the Software Testing Coupling Effect"
265	    authors: "A. Jefferson Offutt"
266	    year: 1992
267	    venue: "ACM TOSEM 1(1):5-20"
268	    category: mutation-testing
269	    role: background
270	    relevance: >
271	      Empirically validates the coupling effect hypothesis that underpins
272	      mutation testing. STA's single-component ablation is analogous to
273	      first-order mutation; the coupling effect suggests this suffices.
274	    key_finding: >
275	      Test data killing all first-order mutants killed >99% of second-
276	      and third-order mutants, validating the coupling effect.
277	
278	  - id: jia-harman-survey
279	    title: "An Analysis and Survey of the Development of Mutation Testing"
280	    authors: "Yue Jia, Mark Harman"
281	    year: 2011
282	    venue: "IEEE TSE 37(5):649-678"
283	    category: mutation-testing
284	    role: background
285	    relevance: >
286	      Comprehensive survey of mutation testing covering three decades of
287	      development. Provides theoretical and practical foundation for STA's
288	      adaptation of mutation testing to logical formulas.
289	    key_finding: >
290	      Systematic classification of mutation operators, cost reduction
291	      techniques, and equivalence problem -- all relevant to STA's design
292	      of clause-level ablation operators.
293	
294	  - id: just-mutants-real-faults
295	    title: "Are Mutants a Valid Substitute for Real Faults in Software Testing?"
296	    authors: "Rene Just, Darioush Jalali, Laura Inozemtseva, et al."
297	    year: 2014
298	    venue: "FSE 2014"
299	    category: mutation-testing
300	    role: background
301	    relevance: >
302	      Validates that mutation testing (structural/intensional analysis of
303	      program adequacy) correlates with real fault detection. Supports STA's
304	      premise that structural analysis of formalization components provides
305	      meaningful signal about formalization quality.
306	    key_finding: >
307	      Mutant detection is statistically correlated with real fault detection,
308	      and mutation score is a better predictor of test effectiveness than
309	      code coverage.
310	
311	  - id: llmorpheus
312	    title: "LLMorpheus: Mutation Testing Using Large Language Models"
313	    authors: "Frank Tip, Jon Bell, et al."
314	    year: 2025
315	    venue: "IEEE TSE 2025"
316	    category: mutation-testing
317	    role: background
318	    relevance: >
319	      Uses LLMs to generate realistic code mutants beyond traditional
320	      mutation operators. Shows mutation testing evolving toward
321	      ML-integrated approaches, validating STA's cross-pollination
322	      of mutation testing ideas into ML training.
323	    key_finding: >
324	      LLM-generated mutants simulate real bugs that rule-based operators
325	      cannot produce, improving mutation testing realism.
326	
327	  - id: mutation-guided-meta
328	    title: "Mutation-Guided LLM-based Test Generation at Meta"
329	    authors: "Christopher Foster et al."
330	    year: 2025
331	    venue: "FSE 2025"
332	    category: mutation-testing
333	    role: background
334	    relevance: >
335	      Industrial application of mutation-guided LLM test generation at
336	      Meta. Demonstrates that mutation analysis can guide LLM behavior
337	      in production -- analogous to how STA uses mutation (ablation) to
338	      guide GRPO reward signal.
339	    key_finding: >
340	      Mutation-guided approach generates tests that kill significantly
341	      more mutants than unguided LLM test generation at Meta scale.
342	
343	  - id: mutation-consistency-llm
344	    title: "Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs"
345	    authors: "Various"
346	    year: 2024
347	    venue: "arXiv 2401.05940"
348	    category: mutation-testing
349	    role: background
350	    relevance: >
351	      Uses code mutations to evaluate LLM code understanding consistency.
352	      Conceptually related to STA: both use systematic code/formula
353	      mutations to assess model capabilities.
354	    key_finding: >
355	      LLMs show significant inconsistency when evaluated on mutated code
356	      variants, suggesting superficial pattern matching.
357	
358	  # ============================================================
359	  # Category 4: Intensional program analysis
360	  # ============================================================
361	
362	  - id: deepmutation
363	    title: "A Probabilistic Framework for Mutation Testing in Deep Neural Networks"
364	    authors: "Various"
365	    year: 2023
366	    venue: "Information and Software Technology 2023"
367	    category: intensional-analysis
368	    role: background
369	    relevance: >
370	      Extends mutation testing to DNN testing with probabilistic mutation
371	      operators. Parallel to STA's extension of mutation testing from
372	      traditional programs to logical formulas.
373	    key_finding: >
374	      Probabilistic mutation framework enables meaningful test adequacy
375	      assessment for neural networks through structural perturbation.
376	
377	  # ============================================================
378	  # Category 5: Reward hacking / overoptimization
379	  # ============================================================
380	
381	  - id: inform-reward-hacking
382	    title: "InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling"
383	    authors: "Various"
384	    year: 2024
385	    venue: "NeurIPS 2024"
386	    category: reward-hacking
387	    role: background
388	    relevance: >
389	      Proposes information-bottleneck approach to detect and mitigate reward
390	      hacking. STA's ISR addresses the same problem differently: by grounding
391	      reward in verifiable structural properties (component necessity), it
392	      reduces the attack surface for reward hacking.
393	    key_finding: >
394	      Variational information bottleneck filters irrelevant features from
395	      reward model; Cluster Separation Index detects reward overoptimization.
396	
397	  - id: mo-grpo
398	    title: "MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems"
399	    authors: "CyberAgent AI Lab"
400	    year: 2025
401	    venue: "arXiv 2509.22047"
402	    category: reward-hacking
403	    role: background
404	    relevance: >
405	      Directly addresses GRPO reward hacking in multi-objective settings.
406	      STA's ISR can be viewed as adding a structural objective to the
407	      correctness objective, making MO-GRPO's insights directly applicable.
408	    key_finding: >
409	      Standard GRPO normalizes after summing rewards, allowing high-variance
410	      objectives to dominate. MO-GRPO equalizes scales before aggregation.
411	
412	  - id: reward-hacking-survey
413	    title: "Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges"
414	    authors: "Various"
415	    year: 2026
416	    venue: "arXiv 2604.13602"
417	    category: reward-hacking
418	    role: background
419	    relevance: >
420	      Comprehensive survey of reward hacking mechanisms in the LLM era.
421	      Provides theoretical framework for understanding why STA's structural
422	      reward is more robust than pure outcome-based reward.
423	    key_finding: >
424	      Reward hacking manifests through specification gaming, reward model
425	      exploitation, and emergent misalignment; structural verification
426	      rewards are more robust than learned reward models.
427	
428	  - id: energy-loss-reward-hacking
429	    title: "The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking"
430	    authors: "Various"
431	    year: 2025
432	    venue: "ICML 2025"
433	    category: reward-hacking
434	    role: background
435	    relevance: >
436	      Identifies energy loss in LLM final layer as an indicator of reward
437	      hacking during RL. Provides complementary diagnostic to STA's
438	      structural reward approach.
439	    key_finding: >
440	      Energy loss in the final layer increases during RL and excessive
441	      increase characterizes reward hacking; EPPO algorithm penalizes
442	      this to mitigate hacking.
443	
444	  # ============================================================
445	  # Category 6: FOL/Prolog formalization with LLMs
446	  # ============================================================
447	
448	  - id: folio
449	    title: "FOLIO: Natural Language Reasoning with First-Order Logic"
450	    authors: "Simeng Han et al."
451	    year: 2022
452	    venue: "arXiv 2209.00840 / EMNLP 2024"
453	    category: fol-formalization
454	    role: evaluation
455	    relevance: >
456	      Primary FOL reasoning benchmark. STA uses FOLIO-style NL->FOL
457	      formalization as the target task for GRPO training. FOLIO's
458	      expert-annotated FOL annotations serve as reference formalizations.
459	    key_finding: >
460	      1,430 NL-FOL paired examples with reasoning depths up to 5+;
461	      GPT-4 still struggles on the hardest examples.
462	
463	  - id: proofwriter
464	    title: "ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language"
465	    authors: "Oyvind Tafjord, Bhavana Dalvi, Peter Clark"
466	    year: 2021
467	    venue: "Findings of ACL-IJCNLP 2021"
468	    category: fol-formalization
469	    role: evaluation
470	    relevance: >
471	      Source dataset for STA's training data. ProofWriter provides
472	      rule-based logical reasoning problems in natural language that
473	      STA uses for training formalizer models.
474	    key_finding: >
475	      Generative model can reliably produce implications and proofs;
476	      accuracy exceeds prior methods by 9% and generalizes to unseen
477	      proof depths.
478	
479	  - id: logic-lm
480	    title: "Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning"
481	    authors: "Liangming Pan, Alon Albalak, Xinyi Wang, William Wang"
482	    year: 2023
483	    venue: "Findings of EMNLP 2023"
484	    category: fol-formalization
485	    role: direct-competitor
486	    relevance: >
487	      LLM->symbolic solver pipeline for logical reasoning, directly
488	      comparable to STA's formalizer->Prolog solver pipeline. Key
489	      difference: Logic-LM uses prompting, STA uses GRPO training.
490	    key_finding: >
491	      LLM+solver achieves 39.2% improvement over LLM-alone on logical
492	      reasoning benchmarks including ProofWriter and FOLIO.
493	
494	  - id: linc
495	    title: "LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers"
496	    authors: "Theo X. Olausson, Alex Gu, Ben Lipkin, et al."
497	    year: 2023
498	    venue: "EMNLP 2023"
499	    category: fol-formalization
500	    role: direct-competitor
501	    relevance: >
502	      Neurosymbolic approach where LLM translates NL to FOL for theorem
503	      prover. Directly comparable to STA's NL->Prolog translation.
504	      LINC uses prompting-based approach; STA uses RL training.
505	    key_finding: >
506	      StarCoder+ (15.5B) with LINC outperforms GPT-3.5 and GPT-4 with
507	      CoT by 38% and 10% respectively on ProofWriter.
508	
509	  - id: fover
510	    title: "FoVer: First-Order Logic Verification for Natural Language Reasoning"
511	    authors: "Yu Pei, Yongping Du, Xingnan Jin"
512	    year: 2025
513	    venue: "TACL 13:1340-1359"
514	    category: fol-formalization
515	    role: direct-competitor
516	    relevance: >
517	      Uses LLM->FOL->Z3 pipeline for verifying NL reasoning correctness.
518	      Similar to STA's verification pipeline but focuses on post-hoc
519	      verification rather than training reward signal.
520	    key_finding: >
521	      FOL verification via Z3 significantly outperforms existing methods
522	      on ProofWriter and FOLIO benchmarks.
523	
524	  - id: lorp
525	    title: "LoRP: LLM-based Logical Reasoning via Prolog"
526	    authors: "Various"
527	    year: 2025
528	    venue: "Knowledge-Based Systems 2025"
529	    category: fol-formalization
530	    role: direct-competitor
531	    relevance: >
532	      LLM->Prolog pipeline with FOL-to-Prolog translation mechanism.
533	      Closest to STA's formalization target (Prolog), though LoRP
534	      uses prompting while STA uses GRPO training with structural reward.
535	    key_finding: >
536	      Systematic FOL-to-Prolog translation extends Prolog expressiveness;
537	      achieves SoTA accuracy on logical reasoning with three-vote majority.
538	
539	  - id: nl2fol
540	    title: "NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection"
541	    authors: "Lalwani, Kim, et al."
542	    year: 2024
543	    venue: "arXiv 2405.02318"
544	    category: fol-formalization
545	    role: background
546	    relevance: >
547	      Step-by-step NL->FOL translation using LLMs with SMT solver
548	      verification. Demonstrates the NL->formal logic pipeline that
549	      STA aims to improve via RL training.
550	    key_finding: >
551	      Neurosymbolic NL2FOL achieves 78% F1 on LOGIC dataset and
552	      generalizes to LogicClimate (80% F1), outperforming supervised
553	      models by 21%.
554	
555	  - id: logica2
556	    title: "LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding"
557	    authors: "Liu et al."
558	    year: 2023
559	    venue: "IEEE/ACM TASLP 2023"
560	    category: fol-formalization
561	    role: evaluation
562	    relevance: >
563	      Logical reasoning evaluation benchmark derived from Chinese civil
564	      service exams. Provides supplementary evaluation for STA's
565	      formalization capabilities.
566	    key_finding: >
567	      8,678 multiple-choice questions covering categorical, disjunctive,
568	      and conditional reasoning; widely used LLM benchmark.
569	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "8c1616c4-32bb-46b0-8dad-e6968d4dbe9f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
      "content": "# Literature Map for Solver Trace Ablation (STA)\n# Categories:\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\n#   2. reward-shaping: Reward shaping for code/formal verification\n#   3. mutation-testing: Mutation testing in software engineering\n#   4. intensional-analysis: Intensional program analysis\n#   5. reward-hacking: Reward hacking / overoptimization\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\n\npapers:\n\n  # ============================================================\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\n  # ============================================================\n\n  - id: deepseek-r1\n    title: \"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\"\n    authors: \"DeepSeek-AI\"\n    year: 2025\n    venue: \"arXiv 2501.12948 / Nature 2025\"\n    category: neurosymbolic-rl\n    role: method-component\n    relevance: >\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\n      STA builds on the same GRPO framework but replaces binary outcome reward with\n      intensional structural reward for neurosymbolic formalization.\n    key_finding: >\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\n      showing emergent chain-of-thought reasoning from RL alone.\n\n  - id: deepseekmath\n    title: \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\"\n    authors: \"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\"\n    year: 2024\n    venue: \"arXiv 2402.03300\"\n    category: neurosymbolic-rl\n    role: method-component\n    relevance: >\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\n      used in STA training. GRPO eliminates the critic model by estimating\n      baselines from group scores.\n    key_finding: >\n      GRPO matches PPO performance while significantly reducing training\n      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.\n\n  - id: logic-rl\n    title: \"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\"\n    authors: \"Xian et al.\"\n    year: 2025\n    venue: \"arXiv 2502.14768\"\n    category: neurosymbolic-rl\n    role: direct-competitor\n    relevance: >\n      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic\n      logic puzzles. Closest competitor to STA's approach of RL for logical\n      formalization, though Logic-RL uses extensional (answer-correctness)\n      rewards rather than STA's intensional structural rewards.\n    key_finding: >\n      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;\n      rule-based reward design is critical for RL-based logical reasoning.\n\n  - id: mellgren-prolog-grpo\n    title: \"Training Language Models to Use Prolog as a Tool\"\n    authors: \"Niklas Mellgren\"\n    year: 2024\n    venue: \"arXiv 2512.07407\"\n    category: neurosymbolic-rl\n    role: direct-competitor\n    relevance: >\n      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,\n      directly comparable to STA's approach of GRPO-training a formalizer.\n      Key difference: uses pass/fail reward vs STA's structural ISR.\n    key_finding: >\n      GRPO is effective for teaching small LLMs to use Prolog as a tool\n      for logical and mathematical reasoning.\n\n  - id: satlm\n    title: \"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\"\n    authors: \"Xi Ye et al.\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    category: neurosymbolic-rl\n    role: background\n    relevance: >\n      Neurosymbolic approach where LLM generates declarative specifications\n      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)\n      but uses prompting, not RL training.\n    key_finding: >\n      Declarative formulation outperforms imperative program-aided LMs by 23%\n      on GSM; achieves SoTA on LSAT and BoardgameQA.\n\n  # ============================================================\n  # Category 2: Reward shaping for code/formal verification\n  # ============================================================\n\n  - id: lightman-verify-step\n    title: \"Let's Verify Step by Step\"\n    authors: \"Hunter Lightman, Vineet Kosaraju, Yura Burda, et al.\"\n    year: 2023\n    venue: \"arXiv 2305.20050 / ICLR 2024\"\n    category: reward-shaping\n    role: method-component\n    relevance: >\n      Establishes that process supervision (step-level reward) outperforms\n      outcome supervision (final-answer reward) for reasoning. STA's ISR\n      is analogous: it provides structural process-level signal about which\n      components of a formalization matter, rather than just pass/fail.\n    key_finding: >\n      Process-supervised reward model achieves 78% on MATH, significantly\n      outperforming outcome-supervised models. Released PRM800K dataset.\n\n  - id: reward-shaping-rlhf\n    title: \"Reward Shaping to Mitigate Reward Hacking in RLHF\"\n    authors: \"Jiayi Fu, Xuandong Zhao, Chengyuan Yao, et al.\"\n    year: 2025\n    venue: \"arXiv 2502.18770\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Studies reward shaping design principles for RLHF: bounded rewards and\n      rapid-then-convergent growth. STA's ISR follows these principles\n      naturally since structural necessity scores are bounded [0,1].\n    key_finding: >\n      Two key reward shaping principles: (1) bounded RL reward, (2) rapid\n      initial growth with gradual convergence. PAR method achieves 5%+\n      win rate improvement on AlpacaEval 2.0.\n\n  - id: rlvr-reasoning\n    title: \"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs\"\n    authors: \"Various\"\n    year: 2025\n    venue: \"arXiv 2506.14245\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize\n      reasoning. STA argues that for neurosymbolic formalization, binary reward\n      is insufficient and structural reward is needed to avoid reward hacking.\n    key_finding: >\n      RLVR with binary verification implicitly teaches correct reasoning\n      strategies, not just answer matching.\n\n  - id: rubric-grpo\n    title: \"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning\"\n    authors: \"Various\"\n    year: 2025\n    venue: \"arXiv 2605.08061\"\n    category: reward-shaping\n    role: direct-competitor\n    relevance: >\n      Uses structured rubric-based rewards with GRPO, similar in spirit to\n      STA's structured ISR. Key difference: rubric rewards come from LLM\n      judges, while ISR comes from solver-based mutation testing.\n    key_finding: >\n      Structured multi-dimensional reward signals improve GRPO training\n      generalization compared to scalar rewards.\n\n  - id: gao-effective-rl-reward\n    title: \"On Designing Effective RL Reward at Training Time for LLM Reasoning\"\n    authors: \"Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu\"\n    year: 2024\n    venue: \"arXiv 2410.15115\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Demonstrates that learned process/outcome reward models can hurt RL\n      training, producing worse performance than simple success reward only.\n      Directly explains plan005 NEGATIVE: STA's ISR as auxiliary process\n      reward degrades prove_rate compared to exec-only baseline.\n    key_finding: >\n      PRM/ORM rewards may NOT help or even hurt RL training vs success-only\n      reward. Solution: Clipping and Delta techniques to bound accumulated\n      reward magnitude prevent reward hacking.\n\n  - id: prof-process-outcome\n    title: \"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training\"\n    authors: \"Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal\"\n    year: 2025\n    venue: \"arXiv 2509.03403\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Shows that naively combining PRM+ORM signals leads to performance\n      degradation. PROF consistency filter retains only PRM-ORM consistent\n      samples, achieving 4%+ improvement over blending. Suggests STA should\n      only apply ISR when consistent with execution outcome.\n    key_finding: >\n      Process rewards frequently suffer from inaccuracies and reward hacking\n      susceptibility. PROF filters training data by PRM-ORM consistency,\n      outperforming naive reward blending by 4%+ accuracy.\n\n  - id: moskovitz-constrained-rlhf\n    title: \"Confronting Reward Model Overoptimization with Constrained RLHF\"\n    authors: \"Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer\"\n    year: 2023\n    venue: \"arXiv 2310.04373 / ICLR 2024\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      First study on overoptimization in composite reward models. Shows that\n      fixed-weight linear scalarization of component rewards leads to\n      degradation past a threshold. Proposes constrained RL with dynamic\n      Lagrange multiplier weighting as alternative to fixed ISR weight.\n    key_finding: >\n      Correlation between component RMs significantly affects overoptimization\n      thresholds. Constrained RL with Lagrange multipliers outperforms\n      fixed-weight reward composition.\n\n  - id: skalse-reward-hacking\n    title: \"Defining and Characterizing Reward Hacking\"\n    authors: \"Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger\"\n    year: 2022\n    venue: \"arXiv 2209.13085 / NeurIPS 2022\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Formal proof that for stochastic policies, two reward functions are\n      unhackable only if one is constant. Theoretically explains why any\n      non-zero ISR weight can decrease prove_rate -- this is a fundamental\n      property of reward composition, not STA-specific.\n    key_finding: >\n      Any non-constant proxy reward can decrease true reward when optimized.\n      Unhackability requires the proxy to be constant, making all non-trivial\n      auxiliary rewards theoretically vulnerable to degrading primary performance.\n\n  - id: progrs-outcome-conditioned\n    title: \"LLM Reasoning with Process Rewards for Outcome-Guided Steps\"\n    authors: \"Mohammad Rezaei, Jens Lehmann, Sahar Vahdati\"\n    year: 2026\n    venue: \"arXiv 2604.02341\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      PRM scores optimized as absolute rewards amplify fluent failure modes.\n      Outcome-conditioned centering shifts incorrect trajectories' PRM scores\n      to zero mean, preserving ranking info without corrupting gradients.\n      Suggests STA should condition ISR on execution outcome.\n    key_finding: >\n      Naive process rewards induce reward hacking by rewarding locally fluent\n      but globally incorrect reasoning. Outcome-conditioned centering resolves\n      the conflict with fewer rollouts than outcome-only baselines.\n\n  # ============================================================\n  # Category 3: Mutation testing in software engineering\n  # ============================================================\n\n  - id: demillo1978\n    title: \"Hints on Test Data Selection: Help for the Practicing Programmer\"\n    authors: \"Richard A. DeMillo, Richard J. Lipton, Frederick G. Sayward\"\n    year: 1978\n    venue: \"Computer 11(4):34-43\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Foundational paper introducing mutation testing. STA's component\n      necessity testing directly extends this idea: instead of mutating\n      source code to test test suites, STA mutates logical formulas\n      to test component necessity for solver success.\n    key_finding: >\n      Introduced mutation testing and the coupling effect hypothesis:\n      tests that detect simple faults also detect complex faults.\n\n  - id: offutt-coupling\n    title: \"Investigations of the Software Testing Coupling Effect\"\n    authors: \"A. Jefferson Offutt\"\n    year: 1992\n    venue: \"ACM TOSEM 1(1):5-20\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Empirically validates the coupling effect hypothesis that underpins\n      mutation testing. STA's single-component ablation is analogous to\n      first-order mutation; the coupling effect suggests this suffices.\n    key_finding: >\n      Test data killing all first-order mutants killed >99% of second-\n      and third-order mutants, validating the coupling effect.\n\n  - id: jia-harman-survey\n    title: \"An Analysis and Survey of the Development of Mutation Testing\"\n    authors: \"Yue Jia, Mark Harman\"\n    year: 2011\n    venue: \"IEEE TSE 37(5):649-678\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Comprehensive survey of mutation testing covering three decades of\n      development. Provides theoretical and practical foundation for STA's\n      adaptation of mutation testing to logical formulas.\n    key_finding: >\n      Systematic classification of mutation operators, cost reduction\n      techniques, and equivalence problem -- all relevant to STA's design\n      of clause-level ablation operators.\n\n  - id: just-mutants-real-faults\n    title: \"Are Mutants a Valid Substitute for Real Faults in Software Testing?\"\n    authors: \"Rene Just, Darioush Jalali, Laura Inozemtseva, et al.\"\n    year: 2014\n    venue: \"FSE 2014\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Validates that mutation testing (structural/intensional analysis of\n      program adequacy) correlates with real fault detection. Supports STA's\n      premise that structural analysis of formalization components provides\n      meaningful signal about formalization quality.\n    key_finding: >\n      Mutant detection is statistically correlated with real fault detection,\n      and mutation score is a better predictor of test effectiveness than\n      code coverage.\n\n  - id: llmorpheus\n    title: \"LLMorpheus: Mutation Testing Using Large Language Models\"\n    authors: \"Frank Tip, Jon Bell, et al.\"\n    year: 2025\n    venue: \"IEEE TSE 2025\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Uses LLMs to generate realistic code mutants beyond traditional\n      mutation operators. Shows mutation testing evolving toward\n      ML-integrated approaches, validating STA's cross-pollination\n      of mutation testing ideas into ML training.\n    key_finding: >\n      LLM-generated mutants simulate real bugs that rule-based operators\n      cannot produce, improving mutation testing realism.\n\n  - id: mutation-guided-meta\n    title: \"Mutation-Guided LLM-based Test Generation at Meta\"\n    authors: \"Christopher Foster et al.\"\n    year: 2025\n    venue: \"FSE 2025\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Industrial application of mutation-guided LLM test generation at\n      Meta. Demonstrates that mutation analysis can guide LLM behavior\n      in production -- analogous to how STA uses mutation (ablation) to\n      guide GRPO reward signal.\n    key_finding: >\n      Mutation-guided approach generates tests that kill significantly\n      more mutants than unguided LLM test generation at Meta scale.\n\n  - id: mutation-consistency-llm\n    title: \"Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs\"\n    authors: \"Various\"\n    year: 2024\n    venue: \"arXiv 2401.05940\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Uses code mutations to evaluate LLM code understanding consistency.\n      Conceptually related to STA: both use systematic code/formula\n      mutations to assess model capabilities.\n    key_finding: >\n      LLMs show significant inconsistency when evaluated on mutated code\n      variants, suggesting superficial pattern matching.\n\n  # ============================================================\n  # Category 4: Intensional program analysis\n  # ============================================================\n\n  - id: deepmutation\n    title: \"A Probabilistic Framework for Mutation Testing in Deep Neural Networks\"\n    authors: \"Various\"\n    year: 2023\n    venue: \"Information and Software Technology 2023\"\n    category: intensional-analysis\n    role: background\n    relevance: >\n      Extends mutation testing to DNN testing with probabilistic mutation\n      operators. Parallel to STA's extension of mutation testing from\n      traditional programs to logical formulas.\n    key_finding: >\n      Probabilistic mutation framework enables meaningful test adequacy\n      assessment for neural networks through structural perturbation.\n\n  # ============================================================\n  # Category 5: Reward hacking / overoptimization\n  # ============================================================\n\n  - id: inform-reward-hacking\n    title: \"InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling\"\n    authors: \"Various\"\n    year: 2024\n    venue: \"NeurIPS 2024\"\n    category: reward-hacking\n    role: background\n    relevance: >\n      Proposes information-bottleneck approach to detect and mitigate reward\n      hacking. STA's ISR addresses the same problem differently: by grounding\n      reward in verifiable structural properties (component necessity), it\n      reduces the attack surface for reward hacking.\n    key_finding: >\n      Variational information bottleneck filters irrelevant features from\n      reward model; Cluster Separation Index detects reward overoptimization.\n\n  - id: mo-grpo\n    title: \"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\"\n    authors: \"CyberAgent AI Lab\"\n    year: 2025\n    venue: \"arXiv 2509.22047\"\n    category: reward-hacking\n    role: background\n    relevance: >\n      Directly addresses GRPO reward hacking in multi-objective settings.\n      STA's ISR can be viewed as adding a structural objective to the\n      correctness objective, making MO-GRPO's insights directly applicable.\n    key_finding: >\n      Standard GRPO normalizes after summing rewards, allowing high-variance\n      objectives to dominate. MO-GRPO equalizes scales before aggregation.\n\n  - id: reward-hacking-survey\n    title: \"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\"\n    authors: \"Various\"\n    year: 2026\n    venue: \"arXiv 2604.13602\"\n    category: reward-hacking\n    role: background\n    relevance: >\n      Comprehensive survey of reward hacking mechanisms in the LLM era.\n      Provides theoretical framework for understanding why STA's structural\n      reward is more robust than pure outcome-based reward.\n    key_finding: >\n      Reward hacking manifests through specification gaming, reward model\n      exploitation, and emergent misalignment; structural verification\n      rewards are more robust than learned reward models.\n\n  - id: energy-loss-reward-hacking\n    title: \"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking\"\n    authors: \"Various\"\n    year: 2025\n    venue: \"ICML 2025\"\n    category: reward-hacking\n    role: background\n    relevance: >\n      Identifies energy loss in LLM final layer as an indicator of reward\n      hacking during RL. Provides complementary diagnostic to STA's\n      structural reward approach.\n    key_finding: >\n      Energy loss in the final layer increases during RL and excessive\n      increase characterizes reward hacking; EPPO algorithm penalizes\n      this to mitigate hacking.\n\n  # ============================================================\n  # Category 6: FOL/Prolog formalization with LLMs\n  # ============================================================\n\n  - id: folio\n    title: \"FOLIO: Natural Language Reasoning with First-Order Logic\"\n    authors: \"Simeng Han et al.\"\n    year: 2022\n    venue: \"arXiv 2209.00840 / EMNLP 2024\"\n    category: fol-formalization\n    role: evaluation\n    relevance: >\n      Primary FOL reasoning benchmark. STA uses FOLIO-style NL->FOL\n      formalization as the target task for GRPO training. FOLIO's\n      expert-annotated FOL annotations serve as reference formalizations.\n    key_finding: >\n      1,430 NL-FOL paired examples with reasoning depths up to 5+;\n      GPT-4 still struggles on the hardest examples.\n\n  - id: proofwriter\n    title: \"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language\"\n    authors: \"Oyvind Tafjord, Bhavana Dalvi, Peter Clark\"\n    year: 2021\n    venue: \"Findings of ACL-IJCNLP 2021\"\n    category: fol-formalization\n    role: evaluation\n    relevance: >\n      Source dataset for STA's training data. ProofWriter provides\n      rule-based logical reasoning problems in natural language that\n      STA uses for training formalizer models.\n    key_finding: >\n      Generative model can reliably produce implications and proofs;\n      accuracy exceeds prior methods by 9% and generalizes to unseen\n      proof depths.\n\n  - id: logic-lm\n    title: \"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\"\n    authors: \"Liangming Pan, Alon Albalak, Xinyi Wang, William Wang\"\n    year: 2023\n    venue: \"Findings of EMNLP 2023\"\n    category: fol-formalization\n    role: direct-competitor\n    relevance: >\n      LLM->symbolic solver pipeline for logical reasoning, directly\n      comparable to STA's formalizer->Prolog solver pipeline. Key\n      difference: Logic-LM uses prompting, STA uses GRPO training.\n    key_finding: >\n      LLM+solver achieves 39.2% improvement over LLM-alone on logical\n      reasoning benchmarks including ProofWriter and FOLIO.\n\n  - id: linc\n    title: \"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers\"\n    authors: \"Theo X. Olausson, Alex Gu, Ben Lipkin, et al.\"\n    year: 2023\n    venue: \"EMNLP 2023\"\n    category: fol-formalization\n    role: direct-competitor\n    relevance: >\n      Neurosymbolic approach where LLM translates NL to FOL for theorem\n      prover. Directly comparable to STA's NL->Prolog translation.\n      LINC uses prompting-based approach; STA uses RL training.\n    key_finding: >\n      StarCoder+ (15.5B) with LINC outperforms GPT-3.5 and GPT-4 with\n      CoT by 38% and 10% respectively on ProofWriter.\n\n  - id: fover\n    title: \"FoVer: First-Order Logic Verification for Natural Language Reasoning\"\n    authors: \"Yu Pei, Yongping Du, Xingnan Jin\"\n    year: 2025\n    venue: \"TACL 13:1340-1359\"\n    category: fol-formalization\n    role: direct-competitor\n    relevance: >\n      Uses LLM->FOL->Z3 pipeline for verifying NL reasoning correctness.\n      Similar to STA's verification pipeline but focuses on post-hoc\n      verification rather than training reward signal.\n    key_finding: >\n      FOL verification via Z3 significantly outperforms existing methods\n      on ProofWriter and FOLIO benchmarks.\n\n  - id: lorp\n    title: \"LoRP: LLM-based Logical Reasoning via Prolog\"\n    authors: \"Various\"\n    year: 2025\n    venue: \"Knowledge-Based Systems 2025\"\n    category: fol-formalization\n    role: direct-competitor\n    relevance: >\n      LLM->Prolog pipeline with FOL-to-Prolog translation mechanism.\n      Closest to STA's formalization target (Prolog), though LoRP\n      uses prompting while STA uses GRPO training with structural reward.\n    key_finding: >\n      Systematic FOL-to-Prolog translation extends Prolog expressiveness;\n      achieves SoTA accuracy on logical reasoning with three-vote majority.\n\n  - id: nl2fol\n    title: \"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection\"\n    authors: \"Lalwani, Kim, et al.\"\n    year: 2024\n    venue: \"arXiv 2405.02318\"\n    category: fol-formalization\n    role: background\n    relevance: >\n      Step-by-step NL->FOL translation using LLMs with SMT solver\n      verification. Demonstrates the NL->formal logic pipeline that\n      STA aims to improve via RL training.\n    key_finding: >\n      Neurosymbolic NL2FOL achieves 78% F1 on LOGIC dataset and\n      generalizes to LogicClimate (80% F1), outperforming supervised\n      models by 21%.\n\n  - id: logica2\n    title: \"LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding\"\n    authors: \"Liu et al.\"\n    year: 2023\n    venue: \"IEEE/ACM TASLP 2023\"\n    category: fol-formalization\n    role: evaluation\n    relevance: >\n      Logical reasoning evaluation benchmark derived from Chinese civil\n      service exams. Provides supplementary evaluation for STA's\n      formalization capabilities.\n    key_finding: >\n      8,678 multiple-choice questions covering categorical, disjunctive,\n      and conditional reasoning; widely used LLM benchmark.\n",
      "numLines": 569,
      "startLine": 1,
      "totalLines": 569
    }
  }
}
```

</details>

---

### Assistant

_source line 73_

文件结构正确。现在通过 MCP 工具保存更新后的 literature_map.yaml。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "3c0ecf76-f7d4-498a-9794-886daa8c050b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SSuEFk7i2CTaZSs7oFtUFp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8265,
      "cache_read_input_tokens": 67913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8265
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

_source line 74_

<details open><summary>🔧 Tool call — Bash · `toolu_01EEJkV7tg4T6uEsRgy5jMtu`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
  "description": "Read full literature_map.yaml content for MCP save"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "104307f7-880f-4f2a-b92f-275bcff94877",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SSuEFk7i2CTaZSs7oFtUFp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8265,
      "cache_read_input_tokens": 67913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8265
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

_source line 75 · 2026-05-14T02:08:48.553Z_

<details><summary>↩ Tool result · `toolu_01EEJkV7tg4T6uEsRgy5jMtu`</summary>

```text
# Literature Map for Solver Trace Ablation (STA)
# Categories:
#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO
#   2. reward-shaping: Reward shaping for code/formal verification
#   3. mutation-testing: Mutation testing in software engineering
#   4. intensional-analysis: Intensional program analysis
#   5. reward-hacking: Reward hacking / overoptimization
#   6. fol-formalization: FOL/Prolog formalization with LLMs

papers:

  # ============================================================
  # Category 1: Neurosymbolic reasoning + RL/GRPO
  # ============================================================

  - id: deepseek-r1
    title: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
    authors: "DeepSeek-AI"
    year: 2025
    venue: "arXiv 2501.12948 / Nature 2025"
    category: neurosymbolic-rl
    role: method-component
    relevance: >
      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.
      STA builds on the same GRPO framework but replaces binary outcome reward with
      intensional structural reward for neurosymbolic formalization.
    key_finding: >
      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,
      showing emergent chain-of-thought reasoning from RL alone.

  - id: deepseekmath
    title: "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models"
    authors: "Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al."
    year: 2024
    venue: "arXiv 2402.03300"
    category: neurosymbolic-rl
    role: method-component
    relevance: >
      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm
      used in STA training. GRPO eliminates the critic model by estimating
      baselines from group scores.
    key_finding: >
      GRPO matches PPO performance while significantly reducing training
      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.

  - id: logic-rl
    title: "Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning"
    authors: "Xian et al."
    year: 2025
    venue: "arXiv 2502.14768"
    category: neurosymbolic-rl
    role: direct-competitor
    relevance: >
      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic
      logic puzzles. Closest competitor to STA's approach of RL for logical
      formalization, though Logic-RL uses extensional (answer-correctness)
      rewards rather than STA's intensional structural rewards.
    key_finding: >
      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;
      rule-based reward design is critical for RL-based logical reasoning.

  - id: mellgren-prolog-grpo
    title: "Training Language Models to Use Prolog as a Tool"
    authors: "Niklas Mellgren"
    year: 2024
    venue: "arXiv 2512.07407"
    category: neurosymbolic-rl
    role: direct-competitor
    relevance: >
      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,
      directly comparable to STA's approach of GRPO-training a formalizer.
      Key difference: uses pass/fail reward vs STA's structural ISR.
    key_finding: >
      GRPO is effective for teaching small LLMs to use Prolog as a tool
      for logical and mathematical reasoning.

  - id: satlm
    title: "SatLM: Satisfiability-Aided Language Models Using Declarative Prompting"
    authors: "Xi Ye et al."
    year: 2023
    venue: "NeurIPS 2023"
    category: neurosymbolic-rl
    role: background
    relevance: >
      Neurosymbolic approach where LLM generates declarative specifications
      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)
      but uses prompting, not RL training.
    key_finding: >
      Declarative formulation outperforms imperative program-aided LMs by 23%
      on GSM; achieves SoTA on LSAT and BoardgameQA.

  # ============================================================
  # Category 2: Reward shaping for code/formal verification
  # ============================================================

  - id: lightman-verify-step
    title: "Let's Verify Step by Step"
    authors: "Hunter Lightman, Vineet Kosaraju, Yura Burda, et al."
    year: 2023
    venue: "arXiv 2305.20050 / ICLR 2024"
    category: reward-shaping
    role: method-component
    relevance: >
      Establishes that process supervision (step-level reward) outperforms
      outcome supervision (final-answer reward) for reasoning. STA's ISR
      is analogous: it provides structural process-level signal about which
      components of a formalization matter, rather than just pass/fail.
    key_finding: >
      Process-supervised reward model achieves 78% on MATH, significantly
      outperforming outcome-supervised models. Released PRM800K dataset.

  - id: reward-shaping-rlhf
    title: "Reward Shaping to Mitigate Reward Hacking in RLHF"
    authors: "Jiayi Fu, Xuandong Zhao, Chengyuan Yao, et al."
    year: 2025
    venue: "arXiv 2502.18770"
    category: reward-shaping
    role: background
    relevance: >
      Studies reward shaping design principles for RLHF: bounded rewards and
      rapid-then-convergent growth. STA's ISR follows these principles
      naturally since structural necessity scores are bounded [0,1].
    key_finding: >
      Two key reward shaping principles: (1) bounded RL reward, (2) rapid
      initial growth with gradual convergence. PAR method achieves 5%+
      win rate improvement on AlpacaEval 2.0.

  - id: rlvr-reasoning
    title: "Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs"
    authors: "Various"
    year: 2025
    venue: "arXiv 2506.14245"
    category: reward-shaping
    role: background
    relevance: >
      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize
      reasoning. STA argues that for neurosymbolic formalization, binary reward
      is insufficient and structural reward is needed to avoid reward hacking.
    key_finding: >
      RLVR with binary verification implicitly teaches correct reasoning
      strategies, not just answer matching.

  - id: rubric-grpo
    title: "Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning"
    authors: "Various"
    year: 2025
    venue: "arXiv 2605.08061"
    category: reward-shaping
    role: direct-competitor
    relevance: >
      Uses structured rubric-based rewards with GRPO, similar in spirit to
      STA's structured ISR. Key difference: rubric rewards come from LLM
      judges, while ISR comes from solver-based mutation testing.
    key_finding: >
      Structured multi-dimensional reward signals improve GRPO training
      generalization compared to scalar rewards.

  - id: gao-effective-rl-reward
    title: "On Designing Effective RL Reward at Training Time for LLM Reasoning"
    authors: "Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu"
    year: 2024
    venue: "arXiv 2410.15115"
    category: reward-shaping
    role: background
    relevance: >
      Demonstrates that learned process/outcome reward models can hurt RL
      training, producing worse performance than simple success reward only.
      Directly explains plan005 NEGATIVE: STA's ISR as auxiliary process
      reward degrades prove_rate compared to exec-only baseline.
    key_finding: >
      PRM/ORM rewards may NOT help or even hurt RL training vs success-only
      reward. Solution: Clipping and Delta techniques to bound accumulated
      reward magnitude prevent reward hacking.

  - id: prof-process-outcome
    title: "Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"
    authors: "Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal"
    year: 2025
    venue: "arXiv 2509.03403"
    category: reward-shaping
    role: background
    relevance: >
      Shows that naively combining PRM+ORM signals leads to performance
      degradation. PROF consistency filter retains only PRM-ORM consistent
      samples, achieving 4%+ improvement over blending. Suggests STA should
      only apply ISR when consistent with execution outcome.
    key_finding: >
      Process rewards frequently suffer from inaccuracies and reward hacking
      susceptibility. PROF filters training data by PRM-ORM consistency,
      outperforming naive reward blending by 4%+ accuracy.

  - id: moskovitz-constrained-rlhf
    title: "Confronting Reward Model Overoptimization with Constrained RLHF"
    authors: "Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer"
    year: 2023
    venue: "arXiv 2310.04373 / ICLR 2024"
    category: reward-shaping
    role: background
    relevance: >
      First study on overoptimization in composite reward models. Shows that
      fixed-weight linear scalarization of component rewards leads to
      degradation past a threshold. Proposes constrained RL with dynamic
      Lagrange multiplier weighting as alternative to fixed ISR weight.
    key_finding: >
      Correlation between component RMs significantly affects overoptimization
      thresholds. Constrained RL with Lagrange multipliers outperforms
      fixed-weight reward composition.

  - id: skalse-reward-hacking
    title: "Defining and Characterizing Reward Hacking"
    authors: "Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger"
    year: 2022
    venue: "arXiv 2209.13085 / NeurIPS 2022"
    category: reward-shaping
    role: background
    relevance: >
      Formal proof that for stochastic policies, two reward functions are
      unhackable only if one is constant. Theoretically explains why any
      non-zero ISR weight can decrease prove_rate -- this is a fundamental
      property of reward composition, not STA-specific.
    key_finding: >
      Any non-constant proxy reward can decrease true reward when optimized.
      Unhackability requires the proxy to be constant, making all non-trivial
      auxiliary rewards theoretically vulnerable to degrading primary performance.

  - id: progrs-outcome-conditioned
    title: "LLM Reasoning with Process Rewards for Outcome-Guided Steps"
    authors: "Mohammad Rezaei, Jens Lehmann, Sahar Vahdati"
    year: 2026
    venue: "arXiv 2604.02341"
    category: reward-shaping
    role: background
    relevance: >
      PRM scores optimized as absolute rewards amplify fluent failure modes.
      Outcome-conditioned centering shifts incorrect trajectories' PRM scores
      to zero mean, preserving ranking info without corrupting gradients.
      Suggests STA should condition ISR on execution outcome.
    key_finding: >
      Naive process rewards induce reward hacking by rewarding locally fluent
      but globally incorrect reasoning. Outcome-conditioned centering resolves
      the conflict with fewer rollouts than outcome-only baselines.

  # ============================================================
  # Category 3: Mutation testing in software engineering
  # ============================================================

  - id: demillo1978
    title: "Hints on Test Data Selection: Help for the Practicing Programmer"
    authors: "Richard A. DeMillo, Richard J. Lipton, Frederick G. Sayward"
    year: 1978
    venue: "Computer 11(4):34-43"
    category: mutation-testing
    role: background
    relevance: >
      Foundational paper introducing mutation testing. STA's component
      necessity testing directly extends this idea: instead of mutating
      source code to test test suites, STA mutates logical formulas
      to test component necessity for solver success.
    key_finding: >
      Introduced mutation testing and the coupling effect hypothesis:
      tests that detect simple faults also detect complex faults.

  - id: offutt-coupling
    title: "Investigations of the Software Testing Coupling Effect"
    authors: "A. Jefferson Offutt"
    year: 1992
    venue: "ACM TOSEM 1(1):5-20"
    category: mutation-testing
    role: background
    relevance: >
      Empirically validates the coupling effect hypothesis that underpins
      mutation testing. STA's single-component ablation is analogous to
      first-order mutation; the coupling effect suggests this suffices.
    key_finding: >
      Test data killing all first-order mutants killed >99% of second-
      and third-order mutants, validating the coupling effect.

  - id: jia-harman-survey
    title: "An Analysis and Survey of the Development of Mutation Testing"
    authors: "Yue Jia, Mark Harman"
    year: 2011
    venue: "IEEE TSE 37(5):649-678"
    category: mutation-testing
    role: background
    relevance: >
      Comprehensive survey of mutation testing covering three decades of
      development. Provides theoretical and practical foundation for STA's
      adaptation of mutation testing to logical formulas.
    key_finding: >
      Systematic classification of mutation operators, cost reduction
      techniques, and equivalence problem -- all relevant to STA's design
      of clause-level ablation operators.

  - id: just-mutants-real-faults
    title: "Are Mutants a Valid Substitute for Real Faults in Software Testing?"
    authors: "Rene Just, Darioush Jalali, Laura Inozemtseva, et al."
    year: 2014
    venue: "FSE 2014"
    category: mutation-testing
    role: background
    relevance: >
      Validates that mutation testing (structural/intensional analysis of
      program adequacy) correlates with real fault detection. Supports STA's
      premise that structural analysis of formalization components provides
      meaningful signal about formalization quality.
    key_finding: >
      Mutant detection is statistically correlated with real fault detection,
      and mutation score is a better predictor of test effectiveness than
      code coverage.

  - id: llmorpheus
    title: "LLMorpheus: Mutation Testing Using Large Language Models"
    authors: "Frank Tip, Jon Bell, et al."
    year: 2025
    venue: "IEEE TSE 2025"
    category: mutation-testing
    role: background
    relevance: >
      Uses LLMs to generate realistic code mutants beyond traditional
      mutation operators. Shows mutation testing evolving toward
      ML-integrated approaches, validating STA's cross-pollination
      of mutation testing ideas into ML training.
    key_finding: >
      LLM-generated mutants simulate real bugs that rule-based operators
      cannot produce, improving mutation testing realism.

  - id: mutation-guided-meta
    title: "Mutation-Guided LLM-based Test Generation at Meta"
    authors: "Christopher Foster et al."
    year: 2025
    venue: "FSE 2025"
    category: mutation-testing
    role: background
    relevance: >
      Industrial application of mutation-guided LLM test generation at
      Meta. Demonstrates that mutation analysis can guide LLM behavior
      in production -- analogous to how STA uses mutation (ablation) to
      guide GRPO reward signal.
    key_finding: >
      Mutation-guided approach generates tests that kill significantly
      more mutants than unguided LLM test generation at Meta scale.

  - id: mutation-consistency-llm
    title: "Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs"
    authors: "Various"
    year: 2024
    venue: "arXiv 2401.05940"
    category: mutation-testing
    role: background
    relevance: >
      Uses code mutations to evaluate LLM code understanding consistency.
      Conceptually related to STA: both use systematic code/formula
      mutations to assess model capabilities.
    key_finding: >
      LLMs show significant inconsistency when evaluated on mutated code
      variants, suggesting superficial pattern matching.

  # ============================================================
  # Category 4: Intensional program analysis
  # ============================================================

  - id: deepmutation
    title: "A Probabilistic Framework for Mutation Testing in Deep Neural Networks"
    authors: "Various"
    year: 2023
    venue: "Information and Software Technology 2023"
    category: intensional-analysis
    role: background
    relevance: >
      Extends mutation testing to DNN testing with probabilistic mutation
      operators. Parallel to STA's extension of mutation testing from
      traditional programs to logical formulas.
    key_finding: >
      Probabilistic mutation framework enables meaningful test adequacy
      assessment for neural networks through structural perturbation.

  # ============================================================
  # Category 5: Reward hacking / overoptimization
  # ============================================================

  - id: inform-reward-hacking
    title: "InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling"
    authors: "Various"
    year: 2024
    venue: "NeurIPS 2024"
    category: reward-hacking
    role: background
    relevance: >
      Proposes information-bottleneck approach to detect and mitigate reward
      hacking. STA's ISR addresses the same problem differently: by grounding
      reward in verifiable structural properties (component necessity), it
      reduces the attack surface for reward hacking.
    key_finding: >
      Variational information bottleneck filters irrelevant features from
      reward model; Cluster Separation Index detects reward overoptimization.

  - id: mo-grpo
    title: "MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems"
    authors: "CyberAgent AI Lab"
    year: 2025
    venue: "arXiv 2509.22047"
    category: reward-hacking
    role: background
    relevance: >
      Directly addresses GRPO reward hacking in multi-objective settings.
      STA's ISR can be viewed as adding a structural objective to the
      correctness objective, making MO-GRPO's insights directly applicable.
    key_finding: >
      Standard GRPO normalizes after summing rewards, allowing high-variance
      objectives to dominate. MO-GRPO equalizes scales before aggregation.

  - id: reward-hacking-survey
    title: "Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges"
    authors: "Various"
    year: 2026
    venue: "arXiv 2604.13602"
    category: reward-hacking
    role: background
    relevance: >
      Comprehensive survey of reward hacking mechanisms in the LLM era.
      Provides theoretical framework for understanding why STA's structural
      reward is more robust than pure outcome-based reward.
    key_finding: >
      Reward hacking manifests through specification gaming, reward model
      exploitation, and emergent misalignment; structural verification
      rewards are more robust than learned reward models.

  - id: energy-loss-reward-hacking
    title: "The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking"
    authors: "Various"
    year: 2025
    venue: "ICML 2025"
    category: reward-hacking
    role: background
    relevance: >
      Identifies energy loss in LLM final layer as an indicator of reward
      hacking during RL. Provides complementary diagnostic to STA's
      structural reward approach.
    key_finding: >
      Energy loss in the final layer increases during RL and excessive
      increase characterizes reward hacking; EPPO algorithm penalizes
      this to mitigate hacking.

  # ============================================================
  # Category 6: FOL/Prolog formalization with LLMs
  # ============================================================

  - id: folio
    title: "FOLIO: Natural Language Reasoning with First-Order Logic"
    authors: "Simeng Han et al."
    year: 2022
    venue: "arXiv 2209.00840 / EMNLP 2024"
    category: fol-formalization
    role: evaluation
    relevance: >
      Primary FOL reasoning benchmark. STA uses FOLIO-style NL->FOL
      formalization as the target task for GRPO training. FOLIO's
      expert-annotated FOL annotations serve as reference formalizations.
    key_finding: >
      1,430 NL-FOL paired examples with reasoning depths up to 5+;
      GPT-4 still struggles on the hardest examples.

  - id: proofwriter
    title: "ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language"
    authors: "Oyvind Tafjord, Bhavana Dalvi, Peter Clark"
    year: 2021
    venue: "Findings of ACL-IJCNLP 2021"
    category: fol-formalization
    role: evaluation
    relevance: >
      Source dataset for STA's training data. ProofWriter provides
      rule-based logical reasoning problems in natural language that
      STA uses for training formalizer models.
    key_finding: >
      Generative model can reliably produce implications and proofs;
      accuracy exceeds prior methods by 9% and generalizes to unseen
      proof depths.

  - id: logic-lm
    title: "Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning"
    authors: "Liangming Pan, Alon Albalak, Xinyi Wang, William Wang"
    year: 2023
    venue: "Findings of EMNLP 2023"
    category: fol-formalization
    role: direct-competitor
    relevance: >
      LLM->symbolic solver pipeline for logical reasoning, directly
      comparable to STA's formalizer->Prolog solver pipeline. Key
      difference: Logic-LM uses prompting, STA uses GRPO training.
    key_finding: >
      LLM+solver achieves 39.2% improvement over LLM-alone on logical
      reasoning benchmarks including ProofWriter and FOLIO.

  - id: linc
    title: "LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers"
    authors: "Theo X. Olausson, Alex Gu, Ben Lipkin, et al."
    year: 2023
    venue: "EMNLP 2023"
    category: fol-formalization
    role: direct-competitor
    relevance: >
      Neurosymbolic approach where LLM translates NL to FOL for theorem
      prover. Directly comparable to STA's NL->Prolog translation.
      LINC uses prompting-based approach; STA uses RL training.
    key_finding: >
      StarCoder+ (15.5B) with LINC outperforms GPT-3.5 and GPT-4 with
      CoT by 38% and 10% respectively on ProofWriter.

  - id: fover
    title: "FoVer: First-Order Logic Verification for Natural Language Reasoning"
    authors: "Yu Pei, Yongping Du, Xingnan Jin"
    year: 2025
    venue: "TACL 13:1340-1359"
    category: fol-formalization
    role: direct-competitor
    relevance: >
      Uses LLM->FOL->Z3 pipeline for verifying NL reasoning correctness.
      Similar to STA's verification pipeline but focuses on post-hoc
      verification rather than training reward signal.
    key_finding: >
      FOL verification via Z3 significantly outperforms existing methods
      on ProofWriter and FOLIO benchmarks.

  - id: lorp
    title: "LoRP: LLM-based Logical Reasoning via Prolog"
    authors: "Various"
    year: 2025
    venue: "Knowledge-Based Systems 2025"
    category: fol-formalization
    role: direct-competitor
    relevance: >
      LLM->Prolog pipeline with FOL-to-Prolog translation mechanism.
      Closest to STA's formalization target (Prolog), though LoRP
      uses prompting while STA uses GRPO training with structural reward.
    key_finding: >
      Systematic FOL-to-Prolog translation extends Prolog expressiveness;
      achieves SoTA accuracy on logical reasoning with three-vote majority.

  - id: nl2fol
    title: "NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection"
    authors: "Lalwani, Kim, et al."
    year: 2024
    venue: "arXiv 2405.02318"
    category: fol-formalization
    role: background
    relevance: >
      Step-by-step NL->FOL translation using LLMs with SMT solver
      verification. Demonstrates the NL->formal logic pipeline that
      STA aims to improve via RL training.
    key_finding: >
      Neurosymbolic NL2FOL achieves 78% F1 on LOGIC dataset and
      generalizes to LogicClimate (80% F1), outperforming supervised
      models by 21%.

  - id: logica2
    title: "LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding"
    authors: "Liu et al."
    year: 2023
    venue: "IEEE/ACM TASLP 2023"
    category: fol-formalization
    role: evaluation
    relevance: >
      Logical reasoning evaluation benchmark derived from Chinese civil
      service exams. Provides supplementary evaluation for STA's
      formalization capabilities.
    key_finding: >
      8,678 multiple-choice questions covering categorical, disjunctive,
      and conditional reasoning; widely used LLM benchmark.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "55f2f4d1-7a57-46aa-815e-9191915fac3e",
  "tool_use_result": {
    "stdout": "# Literature Map for Solver Trace Ablation (STA)\n# Categories:\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\n#   2. reward-shaping: Reward shaping for code/formal verification\n#   3. mutation-testing: Mutation testing in software engineering\n#   4. intensional-analysis: Intensional program analysis\n#   5. reward-hacking: Reward hacking / overoptimization\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\n\npapers:\n\n  # ============================================================\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\n  # ============================================================\n\n  - id: deepseek-r1\n    title: \"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\"\n    authors: \"DeepSeek-AI\"\n    year: 2025\n    venue: \"arXiv 2501.12948 / Nature 2025\"\n    category: neurosymbolic-rl\n    role: method-component\n    relevance: >\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\n      STA builds on the same GRPO framework but replaces binary outcome reward with\n      intensional structural reward for neurosymbolic formalization.\n    key_finding: >\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\n      showing emergent chain-of-thought reasoning from RL alone.\n\n  - id: deepseekmath\n    title: \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\"\n    authors: \"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\"\n    year: 2024\n    venue: \"arXiv 2402.03300\"\n    category: neurosymbolic-rl\n    role: method-component\n    relevance: >\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\n      used in STA training. GRPO eliminates the critic model by estimating\n      baselines from group scores.\n    key_finding: >\n      GRPO matches PPO performance while significantly reducing training\n      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.\n\n  - id: logic-rl\n    title: \"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\"\n    authors: \"Xian et al.\"\n    year: 2025\n    venue: \"arXiv 2502.14768\"\n    category: neurosymbolic-rl\n    role: direct-competitor\n    relevance: >\n      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic\n      logic puzzles. Closest competitor to STA's approach of RL for logical\n      formalization, though Logic-RL uses extensional (answer-correctness)\n      rewards rather than STA's intensional structural rewards.\n    key_finding: >\n      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;\n      rule-based reward design is critical for RL-based logical reasoning.\n\n  - id: mellgren-prolog-grpo\n    title: \"Training Language Models to Use Prolog as a Tool\"\n    authors: \"Niklas Mellgren\"\n    year: 2024\n    venue: \"arXiv 2512.07407\"\n    category: neurosymbolic-rl\n    role: direct-competitor\n    relevance: >\n      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,\n      directly comparable to STA's approach of GRPO-training a formalizer.\n      Key difference: uses pass/fail reward vs STA's structural ISR.\n    key_finding: >\n      GRPO is effective for teaching small LLMs to use Prolog as a tool\n      for logical and mathematical reasoning.\n\n  - id: satlm\n    title: \"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\"\n    authors: \"Xi Ye et al.\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    category: neurosymbolic-rl\n    role: background\n    relevance: >\n      Neurosymbolic approach where LLM generates declarative specifications\n      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)\n      but uses prompting, not RL training.\n    key_finding: >\n      Declarative formulation outperforms imperative program-aided LMs by 23%\n      on GSM; achieves SoTA on LSAT and BoardgameQA.\n\n  # ============================================================\n  # Category 2: Reward shaping for code/formal verification\n  # ============================================================\n\n  - id: lightman-verify-step\n    title: \"Let's Verify Step by Step\"\n    authors: \"Hunter Lightman, Vineet Kosaraju, Yura Burda, et al.\"\n    year: 2023\n    venue: \"arXiv 2305.20050 / ICLR 2024\"\n    category: reward-shaping\n    role: method-component\n    relevance: >\n      Establishes that process supervision (step-level reward) outperforms\n      outcome supervision (final-answer reward) for reasoning. STA's ISR\n      is analogous: it provides structural process-level signal about which\n      components of a formalization matter, rather than just pass/fail.\n    key_finding: >\n      Process-supervised reward model achieves 78% on MATH, significantly\n      outperforming outcome-supervised models. Released PRM800K dataset.\n\n  - id: reward-shaping-rlhf\n    title: \"Reward Shaping to Mitigate Reward Hacking in RLHF\"\n    authors: \"Jiayi Fu, Xuandong Zhao, Chengyuan Yao, et al.\"\n    year: 2025\n    venue: \"arXiv 2502.18770\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Studies reward shaping design principles for RLHF: bounded rewards and\n      rapid-then-convergent growth. STA's ISR follows these principles\n      naturally since structural necessity scores are bounded [0,1].\n    key_finding: >\n      Two key reward shaping principles: (1) bounded RL reward, (2) rapid\n      initial growth with gradual convergence. PAR method achieves 5%+\n      win rate improvement on AlpacaEval 2.0.\n\n  - id: rlvr-reasoning\n    title: \"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs\"\n    authors: \"Various\"\n    year: 2025\n    venue: \"arXiv 2506.14245\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize\n      reasoning. STA argues that for neurosymbolic formalization, binary reward\n      is insufficient and structural reward is needed to avoid reward hacking.\n    key_finding: >\n      RLVR with binary verification implicitly teaches correct reasoning\n      strategies, not just answer matching.\n\n  - id: rubric-grpo\n    title: \"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning\"\n    authors: \"Various\"\n    year: 2025\n    venue: \"arXiv 2605.08061\"\n    category: reward-shaping\n    role: direct-competitor\n    relevance: >\n      Uses structured rubric-based rewards with GRPO, similar in spirit to\n      STA's structured ISR. Key difference: rubric rewards come from LLM\n      judges, while ISR comes from solver-based mutation testing.\n    key_finding: >\n      Structured multi-dimensional reward signals improve GRPO training\n      generalization compared to scalar rewards.\n\n  - id: gao-effective-rl-reward\n    title: \"On Designing Effective RL Reward at Training Time for LLM Reasoning\"\n    authors: \"Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu\"\n    year: 2024\n    venue: \"arXiv 2410.15115\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Demonstrates that learned process/outcome reward models can hurt RL\n      training, producing worse performance than simple success reward only.\n      Directly explains plan005 NEGATIVE: STA's ISR as auxiliary process\n      reward degrades prove_rate compared to exec-only baseline.\n    key_finding: >\n      PRM/ORM rewards may NOT help or even hurt RL training vs success-only\n      reward. Solution: Clipping and Delta techniques to bound accumulated\n      reward magnitude prevent reward hacking.\n\n  - id: prof-process-outcome\n    title: \"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training\"\n    authors: \"Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal\"\n    year: 2025\n    venue: \"arXiv 2509.03403\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Shows that naively combining PRM+ORM signals leads to performance\n      degradation. PROF consistency filter retains only PRM-ORM consistent\n      samples, achieving 4%+ improvement over blending. Suggests STA should\n      only apply ISR when consistent with execution outcome.\n    key_finding: >\n      Process rewards frequently suffer from inaccuracies and reward hacking\n      susceptibility. PROF filters training data by PRM-ORM consistency,\n      outperforming naive reward blending by 4%+ accuracy.\n\n  - id: moskovitz-constrained-rlhf\n    title: \"Confronting Reward Model Overoptimization with Constrained RLHF\"\n    authors: \"Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer\"\n    year: 2023\n    venue: \"arXiv 2310.04373 / ICLR 2024\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      First study on overoptimization in composite reward models. Shows that\n      fixed-weight linear scalarization of component rewards leads to\n      degradation past a threshold. Proposes constrained RL with dynamic\n      Lagrange multiplier weighting as alternative to fixed ISR weight.\n    key_finding: >\n      Correlation between component RMs significantly affects overoptimization\n      thresholds. Constrained RL with Lagrange multipliers outperforms\n      fixed-weight reward composition.\n\n  - id: skalse-reward-hacking\n    title: \"Defining and Characterizing Reward Hacking\"\n    authors: \"Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger\"\n    year: 2022\n    venue: \"arXiv 2209.13085 / NeurIPS 2022\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Formal proof that for stochastic policies, two reward functions are\n      unhackable only if one is constant. Theoretically explains why any\n      non-zero ISR weight can decrease prove_rate -- this is a fundamental\n      property of reward composition, not STA-specific.\n    key_finding: >\n      Any non-constant proxy reward can decrease true reward when optimized.\n      Unhackability requires the proxy to be constant, making all non-trivial\n      auxiliary rewards theoretically vulnerable to degrading primary performance.\n\n  - id: progrs-outcome-conditioned\n    title: \"LLM Reasoning with Process Rewards for Outcome-Guided Steps\"\n    authors: \"Mohammad Rezaei, Jens Lehmann, Sahar Vahdati\"\n    year: 2026\n    venue: \"arXiv 2604.02341\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      PRM scores optimized as absolute rewards amplify fluent failure modes.\n      Outcome-conditioned centering shifts incorrect trajectories' PRM scores\n      to zero mean, preserving ranking info without corrupting gradients.\n      Suggests STA should condition ISR on execution outcome.\n    key_finding: >\n      Naive process rewards induce reward hacking by rewarding locally fluent\n      but globally incorrect reasoning. Outcome-conditioned centering resolves\n      the conflict with fewer rollouts than outcome-only baselines.\n\n  # ============================================================\n  # Category 3: Mutation testing in software engineering\n  # ============================================================\n\n  - id: demillo1978\n    title: \"Hints on Test Data Selection: Help for the Practicing Programmer\"\n    authors: \"Richard A. DeMillo, Richard J. Lipton, Frederick G. Sayward\"\n    year: 1978\n    venue: \"Computer 11(4):34-43\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Foundational paper introducing mutation testing. STA's component\n      necessity testing directly extends this idea: instead of mutating\n      source code to test test suites, STA mutates logical formulas\n      to test component necessity for solver success.\n    key_finding: >\n      Introduced mutation testing and the coupling effect hypothesis:\n      tests that detect simple faults also detect complex faults.\n\n  - id: offutt-coupling\n    title: \"Investigations of the Software Testing Coupling Effect\"\n    authors: \"A. Jefferson Offutt\"\n    year: 1992\n    venue: \"ACM TOSEM 1(1):5-20\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Empirically validates the coupling effect hypothesis that underpins\n      mutation testing. STA's single-component ablation is analogous to\n      first-order mutation; the coupling effect suggests this suffices.\n    key_finding: >\n      Test data killing all first-order mutants killed >99% of second-\n      and third-order mutants, validating the coupling effect.\n\n  - id: jia-harman-survey\n    title: \"An Analysis and Survey of the Development of Mutation Testing\"\n    authors: \"Yue Jia, Mark Harman\"\n    year: 2011\n    venue: \"IEEE TSE 37(5):649-678\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Comprehensive survey of mutation testing covering three decades of\n      development. Provides theoretical and practical foundation for STA's\n      adaptation of mutation testing to logical formulas.\n    key_finding: >\n      Systematic classification of mutation operators, cost reduction\n      techniques, and equivalence problem -- all relevant to STA's design\n      of clause-level ablation operators.\n\n  - id: just-mutants-real-faults\n    title: \"Are Mutants a Valid Substitute for Real Faults in Software Testing?\"\n    authors: \"Rene Just, Darioush Jalali, Laura Inozemtseva, et al.\"\n    year: 2014\n    venue: \"FSE 2014\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Validates that mutation testing (structural/intensional analysis of\n      program adequacy) correlates with real fault detection. Supports STA's\n      premise that structural analysis of formalization components provides\n      meaningful signal about formalization quality.\n    key_finding: >\n      Mutant detection is statistically correlated with real fault detection,\n      and mutation score is a better predictor of test effectiveness than\n      code coverage.\n\n  - id: llmorpheus\n    title: \"LLMorpheus: Mutation Testing Using Large Language Models\"\n    authors: \"Frank Tip, Jon Bell, et al.\"\n    year: 2025\n    venue: \"IEEE TSE 2025\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Uses LLMs to generate realistic code mutants beyond traditional\n      mutation operators. Shows mutation testing evolving toward\n      ML-integrated approaches, validating STA's cross-pollination\n      of mutation testing ideas into ML training.\n    key_finding: >\n      LLM-generated mutants simulate real bugs that rule-based operators\n      cannot produce, improving mutation testing realism.\n\n  - id: mutation-guided-meta\n    title: \"Mutation-Guided LLM-based Test Generation at Meta\"\n    authors: \"Christopher Foster et al.\"\n    year: 2025\n    venue: \"FSE 2025\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Industrial application of mutation-guided LLM test generation at\n      Meta. Demonstrates that mutation analysis can guide LLM behavior\n      in production -- analogous to how STA uses mutation (ablation) to\n      guide GRPO reward signal.\n    key_finding: >\n      Mutation-guided approach generates tests that kill significantly\n      more mutants than unguided LLM test generation at Meta scale.\n\n  - id: mutation-consistency-llm\n    title: \"Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs\"\n    authors: \"Various\"\n    year: 2024\n    venue: \"arXiv 2401.05940\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Uses code mutations to evaluate LLM code understanding consistency.\n      Conceptually related to STA: both use systematic code/formula\n      mutations to assess model capabilities.\n    key_finding: >\n      LLMs show significant inconsistency when evaluated on mutated code\n      variants, suggesting superficial pattern matching.\n\n  # ============================================================\n  # Category 4: Intensional program analysis\n  # ============================================================\n\n  - id: deepmutation\n    title: \"A Probabilistic Framework for Mutation Testing in Deep Neural Networks\"\n    authors: \"Various\"\n    year: 2023\n    venue: \"Information and Software Technology 2023\"\n    category: intensional-analysis\n    role: background\n    relevance: >\n      Extends mutation testing to DNN testing with probabilistic mutation\n      operators. Parallel to STA's extension of mutation testing from\n      traditional programs to logical formulas.\n    key_finding: >\n      Probabilistic mutation framework enables meaningful test adequacy\n      assessment for neural networks through structural perturbation.\n\n  # ============================================================\n  # Category 5: Reward hacking / overoptimization\n  # ============================================================\n\n  - id: inform-reward-hacking\n    title: \"InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling\"\n    authors: \"Various\"\n    year: 2024\n    venue: \"NeurIPS 2024\"\n    category: reward-hacking\n    role: background\n    relevance: >\n      Proposes information-bottleneck approach to detect and mitigate reward\n      hacking. STA's ISR addresses the same problem differently: by grounding\n      reward in verifiable structural properties (component necessity), it\n      reduces the attack surface for reward hacking.\n    key_finding: >\n      Variational information bottleneck filters irrelevant features from\n      reward model; Cluster Separation Index detects reward overoptimization.\n\n  - id: mo-grpo\n    title: \"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\"\n    authors: \"CyberAgent AI Lab\"\n    year: 2025\n    venue: \"arXiv 2509.22047\"\n    category: reward-hacking\n    role: background\n    relevance: >\n      Directly addresses GRPO reward hacking in multi-objective settings.\n      STA's ISR can be viewed as adding a structural objective to the\n      correctness objective, making MO-GRPO's insights directly applicable.\n    key_finding: >\n      Standard GRPO normalizes after summing rewards, allowing high-variance\n      objectives to dominate. MO-GRPO equalizes scales before aggregation.\n\n  - id: reward-hacking-survey\n    title: \"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\"\n    authors: \"Various\"\n    year: 2026\n    venue: \"arXiv 2604.13602\"\n    category: reward-hacking\n    role: background\n    relevance: >\n      Comprehensive survey of reward hacking mechanisms in the LLM era.\n      Provides theoretical framework for understanding why STA's structural\n      reward is more robust than pure outcome-based reward.\n    key_finding: >\n      Reward hacking manifests through specification gaming, reward model\n      exploitation, and emergent misalignment; structural verification\n      rewards are more robust than learned reward models.\n\n  - id: energy-loss-reward-hacking\n    title: \"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking\"\n    authors: \"Various\"\n    year: 2025\n    venue: \"ICML 2025\"\n    category: reward-hacking\n    role: background\n    relevance: >\n      Identifies energy loss in LLM final layer as an indicator of reward\n      hacking during RL. Provides complementary diagnostic to STA's\n      structural reward approach.\n    key_finding: >\n      Energy loss in the final layer increases during RL and excessive\n      increase characterizes reward hacking; EPPO algorithm penalizes\n      this to mitigate hacking.\n\n  # ============================================================\n  # Category 6: FOL/Prolog formalization with LLMs\n  # ============================================================\n\n  - id: folio\n    title: \"FOLIO: Natural Language Reasoning with First-Order Logic\"\n    authors: \"Simeng Han et al.\"\n    year: 2022\n    venue: \"arXiv 2209.00840 / EMNLP 2024\"\n    category: fol-formalization\n    role: evaluation\n    relevance: >\n      Primary FOL reasoning benchmark. STA uses FOLIO-style NL->FOL\n      formalization as the target task for GRPO training. FOLIO's\n      expert-annotated FOL annotations serve as reference formalizations.\n    key_finding: >\n      1,430 NL-FOL paired examples with reasoning depths up to 5+;\n      GPT-4 still struggles on the hardest examples.\n\n  - id: proofwriter\n    title: \"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language\"\n    authors: \"Oyvind Tafjord, Bhavana Dalvi, Peter Clark\"\n    year: 2021\n    venue: \"Findings of ACL-IJCNLP 2021\"\n    category: fol-formalization\n    role: evaluation\n    relevance: >\n      Source dataset for STA's training data. ProofWriter provides\n      rule-based logical reasoning problems in natural language that\n      STA uses for training formalizer models.\n    key_finding: >\n      Generative model can reliably produce implications and proofs;\n      accuracy exceeds prior methods by 9% and generalizes to unseen\n      proof depths.\n\n  - id: logic-lm\n    title: \"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\"\n    authors: \"Liangming Pan, Alon Albalak, Xinyi Wang, William Wang\"\n    year: 2023\n    venue: \"Findings of EMNLP 2023\"\n    category: fol-formalization\n    role: direct-competitor\n    relevance: >\n      LLM->symbolic solver pipeline for logical reasoning, directly\n      comparable to STA's formalizer->Prolog solver pipeline. Key\n      difference: Logic-LM uses prompting, STA uses GRPO training.\n    key_finding: >\n      LLM+solver achieves 39.2% improvement over LLM-alone on logical\n      reasoning benchmarks including ProofWriter and FOLIO.\n\n  - id: linc\n    title: \"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers\"\n    authors: \"Theo X. Olausson, Alex Gu, Ben Lipkin, et al.\"\n    year: 2023\n    venue: \"EMNLP 2023\"\n    category: fol-formalization\n    role: direct-competitor\n    relevance: >\n      Neurosymbolic approach where LLM translates NL to FOL for theorem\n      prover. Directly comparable to STA's NL->Prolog translation.\n      LINC uses prompting-based approach; STA uses RL training.\n    key_finding: >\n      StarCoder+ (15.5B) with LINC outperforms GPT-3.5 and GPT-4 with\n      CoT by 38% and 10% respectively on ProofWriter.\n\n  - id: fover\n    title: \"FoVer: First-Order Logic Verification for Natural Language Reasoning\"\n    authors: \"Yu Pei, Yongping Du, Xingnan Jin\"\n    year: 2025\n    venue: \"TACL 13:1340-1359\"\n    category: fol-formalization\n    role: direct-competitor\n    relevance: >\n      Uses LLM->FOL->Z3 pipeline for verifying NL reasoning correctness.\n      Similar to STA's verification pipeline but focuses on post-hoc\n      verification rather than training reward signal.\n    key_finding: >\n      FOL verification via Z3 significantly outperforms existing methods\n      on ProofWriter and FOLIO benchmarks.\n\n  - id: lorp\n    title: \"LoRP: LLM-based Logical Reasoning via Prolog\"\n    authors: \"Various\"\n    year: 2025\n    venue: \"Knowledge-Based Systems 2025\"\n    category: fol-formalization\n    role: direct-competitor\n    relevance: >\n      LLM->Prolog pipeline with FOL-to-Prolog translation mechanism.\n      Closest to STA's formalization target (Prolog), though LoRP\n      uses prompting while STA uses GRPO training with structural reward.\n    key_finding: >\n      Systematic FOL-to-Prolog translation extends Prolog expressiveness;\n      achieves SoTA accuracy on logical reasoning with three-vote majority.\n\n  - id: nl2fol\n    title: \"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection\"\n    authors: \"Lalwani, Kim, et al.\"\n    year: 2024\n    venue: \"arXiv 2405.02318\"\n    category: fol-formalization\n    role: background\n    relevance: >\n      Step-by-step NL->FOL translation using LLMs with SMT solver\n      verification. Demonstrates the NL->formal logic pipeline that\n      STA aims to improve via RL training.\n    key_finding: >\n      Neurosymbolic NL2FOL achieves 78% F1 on LOGIC dataset and\n      generalizes to LogicClimate (80% F1), outperforming supervised\n      models by 21%.\n\n  - id: logica2\n    title: \"LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding\"\n    authors: \"Liu et al.\"\n    year: 2023\n    venue: \"IEEE/ACM TASLP 2023\"\n    category: fol-formalization\n    role: evaluation\n    relevance: >\n      Logical reasoning evaluation benchmark derived from Chinese civil\n      service exams. Provides supplementary evaluation for STA's\n      formalization capabilities.\n    key_finding: >\n      8,678 multiple-choice questions covering categorical, disjunctive,\n      and conditional reasoning; widely used LLM benchmark.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 76_

<details><summary>Logged reasoning block</summary>

```text
The literature_map.yaml file has already been updated directly via the Edit tool. Since the file is at the project path, the MCP save_project_file is for the project-managed files. Let me check if save_project_file can handle literature_map.yaml — the whitelist says it supports only memory.md, writing_plan.yaml, paper_framing.md. literature_map.yaml is not in the whitelist. But the description says "Other files have dedicated tools" — let me check. Looking at the MCP tool description:


literature_map.yaml isn't whitelisted for save_project_file, but I've already edited it directly with the Edit tool, so that's handled. Let me verify it's at the correct path.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "08ad9101-f572-44a7-a771-a58faac232be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PE21WmJ4HoEoAGusRxfaPT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7230,
      "cache_read_input_tokens": 76178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7230
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

_source line 77_

The literature_map.yaml was already updated directly via Edit. Let me verify it's at the correct location.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "fe657b7a-9ac7-451b-8afc-327c4f5e1574",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PE21WmJ4HoEoAGusRxfaPT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7230,
      "cache_read_input_tokens": 76178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7230
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

_source line 78_

<details open><summary>🔧 Tool call — Bash · `toolu_01ERMksmtJWXMnWbYVjzCyPU`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/plan005_negative_literature.md",
  "description": "Verify both output files exist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "4bfcd1f9-abfa-4574-b928-ce7b9962a923",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PE21WmJ4HoEoAGusRxfaPT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7230,
      "cache_read_input_tokens": 76178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7230
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

_source line 79 · 2026-05-14T02:09:03.489Z_

<details><summary>↩ Tool result · `toolu_01ERMksmtJWXMnWbYVjzCyPU`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu  8123 May 14 02:07 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/plan005_negative_literature.md
-rw-r--r-- 1 ubuntu ubuntu 24697 May 14 02:08 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "17e34914-7380-4ad9-83c9-32c26a37816c",
  "tool_use_result": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu  8123 May 14 02:07 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/plan005_negative_literature.md\n-rw-r--r-- 1 ubuntu ubuntu 24697 May 14 02:08 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 80_

完成。

**调研报告** → `artifacts/plan005_negative_literature.md`
**文献地图** → `literature_map.yaml` 新增 5 篇论文（reward-shaping category）

### 核心结论

plan005 的 NEGATIVE 结果（ISR 降低 prove_rate）是 multi-objective RL 中已知的 **auxiliary reward degradation** 现象，5 篇论文从不同角度确认：

1. **Gao et al. (2024)** — process reward 在 RL 训练中可能**比 success-only reward 更差**
2. **Ye et al. (2025, PROF)** — 朴素混合 PRM+ORM 导致退化，需 consistency filtering
3. **Moskovitz et al. (2023, ICLR 2024)** — 固定权重线性组合存在过度优化阈值
4. **Skalse et al. (2022, NeurIPS)** — 理论证明：任何非常数 proxy reward 都可能降低 true reward
5. **Rezaei et al. (2026, PROGRS)** — 无条件 process reward 会放大失败模式，需 outcome-conditioned centering

**推荐改进方向**：Bonus-only + Outcome-conditioned ISR（仅对 prove 成功的样本施加正向 ISR bonus），实施复杂度低且同时解决 hackability 和 gradient corruption 问题。

Sources:
- [Gao et al. - On Designing Effective RL Reward](https://arxiv.org/abs/2410.15115)
- [Ye et al. - Beyond Correctness (PROF)](https://arxiv.org/abs/2509.03403)
- [Moskovitz et al. - Confronting Reward Model Overoptimization](https://arxiv.org/abs/2310.04373)
- [Skalse et al. - Defining and Characterizing Reward Hacking](https://arxiv.org/abs/2209.13085)
- [Rezaei et al. - PROGRS](https://arxiv.org/abs/2604.02341)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "uuid": "c56de209-012a-4b4c-afed-5518029a4a57",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PmThz1g9rmtnAH6pyHuGdR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 533,
      "cache_read_input_tokens": 83408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 533
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

_source line 81_

完成。

**调研报告** → `artifacts/plan005_negative_literature.md`
**文献地图** → `literature_map.yaml` 新增 5 篇论文（reward-shaping category）

### 核心结论

plan005 的 NEGATIVE 结果（ISR 降低 prove_rate）是 multi-objective RL 中已知的 **auxiliary reward degradation** 现象，5 篇论文从不同角度确认：

1. **Gao et al. (2024)** — process reward 在 RL 训练中可能**比 success-only reward 更差**
2. **Ye et al. (2025, PROF)** — 朴素混合 PRM+ORM 导致退化，需 consistency filtering
3. **Moskovitz et al. (2023, ICLR 2024)** — 固定权重线性组合存在过度优化阈值
4. **Skalse et al. (2022, NeurIPS)** — 理论证明：任何非常数 proxy reward 都可能降低 true reward
5. **Rezaei et al. (2026, PROGRS)** — 无条件 process reward 会放大失败模式，需 outcome-conditioned centering

**推荐改进方向**：Bonus-only + Outcome-conditioned ISR（仅对 prove 成功的样本施加正向 ISR bonus），实施复杂度低且同时解决 hackability 和 gradient corruption 问题。

Sources:
- [Gao et al. - On Designing Effective RL Reward](https://arxiv.org/abs/2410.15115)
- [Ye et al. - Beyond Correctness (PROF)](https://arxiv.org/abs/2509.03403)
- [Moskovitz et al. - Confronting Reward Model Overoptimization](https://arxiv.org/abs/2310.04373)
- [Skalse et al. - Defining and Characterizing Reward Hacking](https://arxiv.org/abs/2209.13085)
- [Rezaei et al. - PROGRS](https://arxiv.org/abs/2604.02341)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 311574,
  "duration_api_ms": 394466,
  "num_turns": 30,
  "stop_reason": "end_turn",
  "session_id": "6c8ab3fa-f3c3-483d-b115-dccc1097e77a",
  "total_cost_usd": 1.7426759999999997,
  "usage": {
    "input_tokens": 1734,
    "cache_creation_input_tokens": 72100,
    "cache_read_input_tokens": 757702,
    "output_tokens": 10654,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 72100,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 581,
        "cache_read_input_tokens": 83408,
        "cache_creation_input_tokens": 533,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 533
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 468380,
      "outputTokens": 7960,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 13,
      "costUSD": 0.6381799999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 1734,
      "outputTokens": 10654,
      "cacheReadInputTokens": 757702,
      "cacheCreationInputTokens": 72100,
      "webSearchRequests": 0,
      "costUSD": 1.104496,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "56ecbbe3-bfdc-49c3-9a5e-502898ecf934"
}
```

</details>

---
