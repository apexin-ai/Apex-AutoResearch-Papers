# research literature gap check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 77
- **Recorded user turns:** 0
- **Tool calls:** 28
- **Original source:** `logs/workers/worker_research_literature-gap-check_20260514T174236.log`
- **Structured JSON:** [`5e52def3608a33e113c9.json`](../../sessions/5e/5e52def3608a33e113c9.json)

## Before a recorded user message

77 recorded events

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
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
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
  "uuid": "b07a8558-114c-477c-9c2c-b7ebc9d99f71",
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
    "resetsAt": 1778782200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "e2ea39f6-cd8a-4fd6-9bd5-004687379f66",
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf"
}
```

---

### Assistant

_source line 4_

I'll start by reading the current literature map and loading the necessary tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "b36fe313-5647-4bfe-8ad2-a7ea2b0c5526",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XvPDVhKv5TXsiLxQ1ZdDSS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12509,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12509
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PhpMSu9kMGwTZdbTkTdrDZ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,WebSearch,WebFetch",
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
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "aca0119e-1191-4df0-9366-fc2851f5116e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XvPDVhKv5TXsiLxQ1ZdDSS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12509,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12509
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

_source line 6 · 2026-05-14T17:42:49.689Z_

<details><summary>↩ Tool result · `toolu_01PhpMSu9kMGwTZdbTkTdrDZ`</summary>

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
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "4f75aabc-f4ca-482e-b27d-fd0ecd2c913e",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,WebSearch,WebFetch",
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
Let me read the current literature map first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "11f86835-9e95-478c-a1cf-e0c64e8d8dab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YY96yVdBGsKBJzTWDZrUwL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1714,
      "cache_read_input_tokens": 24350,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1714
      },
      "output_tokens": 41,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NEtUraCFw9yPhckiMHujfR`</summary>

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
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "d2daf311-0de7-4d07-9c79-92eb53925283",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YY96yVdBGsKBJzTWDZrUwL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1714,
      "cache_read_input_tokens": 24350,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1714
      },
      "output_tokens": 41,
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

_source line 9 · 2026-05-14T17:42:53.812Z_

<details><summary>↩ Tool result · `toolu_01NEtUraCFw9yPhckiMHujfR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\", \"content\": \"# Literature Map for Solver Trace Ablation (STA)\\n# Categories:\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\n#   2. reward-shaping: Reward shaping for code/formal verification\\n#   3. mutation-testing: Mutation testing in software engineering\\n#   4. intensional-analysis: Intensional program analysis\\n#   5. reward-hacking: Reward hacking / overoptimization\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\n#   7. goodhart-overoptimization: Goodhart's Law theory and dose-response dynamics\\n#   8. verification-reward: Solver/prover as RL reward signal\\n\\npapers:\\n\\n  # ============================================================\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\n  # ============================================================\\n\\n  - id: deepseek-r1\\n    title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n    authors: \\\"DeepSeek-AI\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2501.12948 / Nature 2025\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\n      intensional structural reward for neurosymbolic formalization.\\n    key_finding: >\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\n      showing emergent chain-of-thought reasoning from RL alone.\\n\\n  - id: deepseekmath\\n    title: \\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\"\\n    authors: \\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2402.03300\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\\n      used in STA training. GRPO eliminates the critic model by estimating\\n      baselines from group scores.\\n    key_finding: >\\n      GRPO matches PPO performance while significantly reducing training\\n      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.\\n\\n  - id: logic-rl\\n    title: \\\"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\\\"\\n    authors: \\\"Xian et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.14768\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic\\n      logic puzzles. Closest competitor to STA's approach of RL for logical\\n      formalization, though Logic-RL uses extensional (answer-correctness)\\n      rewards rather than STA's intensional structural rewards.\\n    key_finding: >\\n      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;\\n      rule-based reward design is critical for RL-based logical reasoning.\\n\\n  - id: mellgren-prolog-grpo\\n    title: \\\"Training Language Models to Use Prolog as a Tool\\\"\\n    authors: \\\"Niklas Mellgren\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2512.07407\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,\\n      directly comparable to STA's approach of GRPO-training a formalizer.\\n      Key difference: uses pass/fail reward vs STA's structural ISR.\\n    key_finding: >\\n      GRPO is effective for teaching small LLMs to use Prolog as a tool\\n      for logical and mathematical reasoning.\\n\\n  - id: satlm\\n    title: \\\"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\\\"\\n    authors: \\\"Xi Ye et al.\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023\\\"\\n    category: neurosymbolic-rl\\n    role: background\\n    relevance: >\\n      Neurosymbolic approach where LLM generates declarative specifications\\n      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)\\n      but uses prompting, not RL training.\\n    key_finding: >\\n      Declarative formulation outperforms imperative program-aided LMs by 23%\\n      on GSM; achieves SoTA on LSAT and BoardgameQA.\\n\\n  # ============================================================\\n  # Category 2: Reward shaping for code/formal verification\\n  # ============================================================\\n\\n  - id: lightman-verify-step\\n    title: \\\"Let's Verify Step by Step\\\"\\n    authors: \\\"Hunter Lightman, Vineet Kosaraju, Yura Burda, et al.\\\"\\n    year: 2023\\n    venue: \\\"arXiv 2305.20050 / ICLR 2024\\\"\\n    category: reward-shaping\\n    role: method-component\\n    relevance: >\\n      Establishes that process supervision (step-level reward) outperforms\\n      outcome supervision (final-answer reward) for reasoning. STA's ISR\\n      is analogous: it provides structural process-level signal about which\\n      components of a formalization matter, rather than just pass/fail.\\n    key_finding: >\\n      Process-supervised reward model achieves 78% on MATH, significantly\\n      outperforming outcome-supervised models. Released PRM800K dataset.\\n\\n  - id: reward-shaping-rlhf\\n    title: \\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\"\\n    authors: \\\"Jiayi Fu, Xuandong Zhao, Chengyuan Yao, et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.18770\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Studies reward shaping design principles for RLHF: bounded rewards and\\n      rapid-then-convergent growth. STA's ISR follows these principles\\n      naturally since structural necessity scores are bounded [0,1].\\n    key_finding: >\\n      Two key reward shaping principles: (1) bounded RL reward, (2) rapid\\n      initial growth with gradual convergence. PAR method achieves 5%+\\n      win rate improvement on AlpacaEval 2.0.\\n\\n  - id: rlvr-reasoning\\n    title: \\\"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2506.14245\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize\\n      reasoning. STA argues that for neurosymbolic formalization, binary reward\\n      is insufficient and structural reward is needed to avoid reward hacking.\\n    key_finding: >\\n      RLVR with binary verification implicitly teaches correct reasoning\\n      strategies, not just answer matching.\\n\\n  - id: rubric-grpo\\n    title: \\\"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2605.08061\\\"\\n    category: reward-shaping\\n    role: direct-competitor\\n    relevance: >\\n      Uses structured rubric-based rewards with GRPO, similar in spirit to\\n      STA's structured ISR. Key difference: rubric rewards come from LLM\\n      judges, while ISR comes from solver-based mutation testing.\\n    key_finding: >\\n      Structured multi-dimensional reward signals improve GRPO training\\n      generalization compared to scalar rewards.\\n\\n  - id: gao-effective-rl-reward\\n    title: \\\"On Designing Effective RL Reward at Training Time for LLM Reasoning\\\"\\n    authors: \\\"Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2410.15115\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Demonstrates that learned process/outcome reward models can hurt RL\\n      training, producing worse performance than simple success reward only.\\n      Directly explains plan005 NEGATIVE: STA's ISR as auxiliary process\\n      reward degrades prove_rate compared to exec-only baseline.\\n    key_finding: >\\n      PRM/ORM rewards may NOT help or even hurt RL training vs success-only\\n      reward. Solution: Clipping and Delta techniques to bound accumulated\\n      reward magnitude prevent reward hacking.\\n\\n  - id: prof-process-outcome\\n    title: \\\"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training\\\"\\n    authors: \\\"Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2509.03403\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Shows that naively combining PRM+ORM signals leads to performance\\n      degradation. PROF consistency filter retains only PRM-ORM consistent\\n      samples, achieving 4%+ improvement over blending. Suggests STA should\\n      only apply ISR when consistent with execution outcome.\\n    key_finding: >\\n      Process rewards frequently suffer from inaccuracies and reward hacking\\n      susceptibility. PROF filters training data by PRM-ORM consistency,\\n      outperforming naive reward blending by 4%+ accuracy.\\n\\n  - id: moskovitz-constrained-rlhf\\n    title: \\\"Confronting Reward Model Overoptimization with Constrained RLHF\\\"\\n    authors: \\\"Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer\\\"\\n    year: 2023\\n    venue: \\\"arXiv 2310.04373 / ICLR 2024\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      First study on overoptimization in composite reward models. Shows that\\n      fixed-weight linear scalarization of component rewards leads to\\n      degradation past a threshold. Proposes constrained RL with dynamic\\n      Lagrange multiplier weighting as alternative to fixed ISR weight.\\n    key_finding: >\\n      Correlation between component RMs significantly affects overoptimization\\n      thresholds. Constrained RL with Lagrange multipliers outperforms\\n      fixed-weight reward composition.\\n\\n  - id: skalse-reward-hacking\\n    title: \\\"Defining and Characterizing Reward Hacking\\\"\\n    authors: \\\"Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger\\\"\\n    year: 2022\\n    venue: \\\"arXiv 2209.13085 / NeurIPS 2022\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Formal proof that for stochastic policies, two reward functions are\\n      unhackable only if one is constant. Theoretically explains why any\\n      non-zero ISR weight can decrease prove_rate -- this is a fundamental\\n      property of reward composition, not STA-specific.\\n    key_finding: >\\n      Any non-constant proxy reward can decrease true reward when optimized.\\n      Unhackability requires the proxy to be constant, making all non-trivial\\n      auxiliary rewards theoretically vulnerable to degrading primary performance.\\n\\n  - id: progrs-outcome-conditioned\\n    title: \\\"LLM Reasoning with Process Rewards for Outcome-Guided Steps\\\"\\n    authors: \\\"Mohammad Rezaei, Jens Lehmann, Sahar Vahdati\\\"\\n    year: 2026\\n    venue: \\\"arXiv 2604.02341\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      PRM scores optimized as absolute rewards amplify fluent failure modes.\\n      Outcome-conditioned centering shifts incorrect trajectories' PRM scores\\n      to zero mean, preserving ranking info without corrupting gradients.\\n      Suggests STA should condition ISR on execution outcome.\\n    key_finding: >\\n      Naive process rewards induce reward hacking by rewarding locally fluent\\n      but globally incorrect reasoning. Outcome-conditioned centering resolves\\n      the conflict with fewer rollouts than outcome-only baselines.\\n\\n  - id: qwen-prm-lessons\\n    title: \\\"The Lessons of Developing Process Reward Models in Mathematical Reasoning\\\"\\n    authors: \\\"Zhenru Zhang et al. (Qwen Team, Alibaba)\\\"\\n    year: 2025\\n    venue: \\\"ACL 2025 Findings (arXiv 2501.07301)\\\"\\n    category: reward-shaping\\n    role: supporting-evidence\\n    relevance: >\\n      MC estimation-synthesized PRM data leads to quality degradation; policy\\n      model generates \\\"answer-correct but reasoning-flawed\\\" responses, causing\\n      process reward / outcome misalignment. Directly parallels ISR problem:\\n      structurally correct but semantically wrong proof traces get high ISR\\n      but low execution reward.\\n    key_finding: >\\n      PRM performance depends critically on data quality; MC estimation\\n      introduces systematic bias. Answer-correct reasoning-flawed samples\\n      corrupt process supervision signal.\\n\\n  # ============================================================\\n  # Category 3: Mutation testing in software engineering\\n  # ============================================================\\n\\n  - id: demillo1978\\n    title: \\\"Hints on Test Data Selection: Help for the Practicing Programmer\\\"\\n    authors: \\\"Richard A. DeMillo, Richard J. Lipton, Frederick G. Sayward\\\"\\n    year: 1978\\n    venue: \\\"Computer 11(4):34-43\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Foundational paper introducing mutation testing. STA's component\\n      necessity testing directly extends this idea: instead of mutating\\n      source code to test test suites, STA mutates logical formulas\\n      to test component necessity for solver success.\\n    key_finding: >\\n      Introduced mutation testing and the coupling effect hypothesis:\\n      tests that detect simple faults also detect complex faults.\\n\\n  - id: offutt-coupling\\n    title: \\\"Investigations of the Software Testing Coupling Effect\\\"\\n    authors: \\\"A. Jefferson Offutt\\\"\\n    year: 1992\\n    venue: \\\"ACM TOSEM 1(1):5-20\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Empirically validates the coupling effect hypothesis that underpins\\n      mutation testing. STA's single-component ablation is analogous to\\n      first-order mutation; the coupling effect suggests this suffices.\\n    key_finding: >\\n      Test data killing all first-order mutants killed >99% of second-\\n      and third-order mutants, validating the coupling effect.\\n\\n  - id: jia-harman-survey\\n    title: \\\"An Analysis and Survey of the Development of Mutation Testing\\\"\\n    authors: \\\"Yue Jia, Mark Harman\\\"\\n    year: 2011\\n    venue: \\\"IEEE TSE 37(5):649-678\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Comprehensive survey of mutation testing covering three decades of\\n      development. Provides theoretical and practical foundation for STA's\\n      adaptation of mutation testing to logical formulas.\\n    key_finding: >\\n      Systematic classification of mutation operators, cost reduction\\n      techniques, and equivalence problem -- all relevant to STA's design\\n      of clause-level ablation operators.\\n\\n  - id: just-mutants-real-faults\\n    title: \\\"Are Mutants a Valid Substitute for Real Faults in Software Testing?\\\"\\n    authors: \\\"Rene Just, Darioush Jalali, Laura Inozemtseva, et al.\\\"\\n    year: 2014\\n    venue: \\\"FSE 2014\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Validates that mutation testing (structural/intensional analysis of\\n      program adequacy) correlates with real fault detection. Supports STA's\\n      premise that structural analysis of formalization components provides\\n      meaningful signal about formalization quality.\\n    key_finding: >\\n      Mutant detection is statistically correlated with real fault detection,\\n      and mutation score is a better predictor of test effectiveness than\\n      code coverage.\\n\\n  - id: llmorpheus\\n    title: \\\"LLMorpheus: Mutation Testing Using Large Language Models\\\"\\n    authors: \\\"Frank Tip, Jon Bell, et al.\\\"\\n    year: 2025\\n    venue: \\\"IEEE TSE 2025\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Uses LLMs to generate realistic code mutants beyond traditional\\n      mutation operators. Shows mutation testing evolving toward\\n      ML-integrated approaches, validating STA's cross-pollination\\n      of mutation testing ideas into ML training.\\n    key_finding: >\\n      LLM-generated mutants simulate real bugs that rule-based operators\\n      cannot produce, improving mutation testing realism.\\n\\n  - id: mutation-guided-meta\\n    title: \\\"Mutation-Guided LLM-based Test Generation at Meta\\\"\\n    authors: \\\"Christopher Foster et al.\\\"\\n    year: 2025\\n    venue: \\\"FSE 2025\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Industrial application of mutation-guided LLM test generation at\\n      Meta. Demonstrates that mutation analysis can guide LLM behavior\\n      in production -- analogous to how STA uses mutation (ablation) to\\n      guide GRPO reward signal.\\n    key_finding: >\\n      Mutation-guided approach generates tests that kill significantly\\n      more mutants than unguided LLM test generation at Meta scale.\\n\\n  - id: mutation-consistency-llm\\n    title: \\\"Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs\\\"\\n    authors: \\\"Various\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2401.05940\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Uses code mutations to evaluate LLM code understanding consistency.\\n      Conceptually related to STA: both use systematic code/formula\\n      mutations to assess model capabilities.\\n    key_finding: >\\n      LLMs show significant inconsistency when evaluated on mutated code\\n      variants, suggesting superficial pattern matching.\\n\\n  # ============================================================\\n  # Category 4: Intensional program analysis\\n  # ============================================================\\n\\n  - id: deepmutation\\n    title: \\\"A Probabilistic Framework for Mutation Testing in Deep Neural Networks\\\"\\n    authors: \\\"Various\\\"\\n    year: 2023\\n    venue: \\\"Information and Software Technology 2023\\\"\\n    category: intensional-analysis\\n    role: background\\n    relevance: >\\n      Extends mutation testing to DNN testing with probabilistic mutation\\n      operators. Parallel to STA's extension of mutation testing from\\n      traditional programs to logical formulas.\\n    key_finding: >\\n      Probabilistic mutation framework enables meaningful test adequacy\\n      assessment for neural networks through structural perturbation.\\n\\n  # ============================================================\\n  # Category 5: Reward hacking / overoptimization\\n  # ============================================================\\n\\n  - id: inform-reward-hacking\\n    title: \\\"InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling\\\"\\n    authors: \\\"Various\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS 2024\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Proposes information-bottleneck approach to detect and mitigate reward\\n      hacking. STA's ISR addresses the same problem differently: by grounding\\n      reward in verifiable structural properties (component necessity), it\\n      reduces the attack surface for reward hacking.\\n    key_finding: >\\n      Variational information bottleneck filters irrelevant features from\\n      reward model; Cluster Separation Index detects reward overoptimization.\\n\\n  - id: mo-grpo\\n    title: \\\"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\\\"\\n    authors: \\\"CyberAgent AI Lab\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2509.22047\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Directly addresses GRPO reward hacking in multi-objective settings.\\n      STA's ISR can be viewed as adding a structural objective to the\\n      correctness objective, making MO-GRPO's insights directly applicable.\\n    key_finding: >\\n      Standard GRPO normalizes after summing rewards, allowing high-variance\\n      objectives to dominate. MO-GRPO equalizes scales before aggregation.\\n\\n  - id: reward-hacking-survey\\n    title: \\\"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\\\"\\n    authors: \\\"Various\\\"\\n    year: 2026\\n    venue: \\\"arXiv 2604.13602\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Comprehensive survey of reward hacking mechanisms in the LLM era.\\n      Provides theoretical framework for understanding why STA's structural\\n      reward is more robust than pure outcome-based reward.\\n    key_finding: >\\n      Reward hacking manifests through specification gaming, reward model\\n      exploitation, and emergent misalignment; structural verification\\n      rewards are more robust than learned reward models.\\n\\n  - id: energy-loss-reward-hacking\\n    title: \\\"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"ICML 2025\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Identifies energy loss in LLM final layer as an indicator of reward\\n      hacking during RL. Provides complementary diagnostic to STA's\\n      structural reward approach.\\n    key_finding: >\\n      Energy loss in the final layer increases during RL and excessive\\n      increase characterizes reward hacking; EPPO algorithm penalizes\\n      this to mitigate hacking.\\n\\n  - id: spurious-rewards\\n    title: \\\"Spurious Rewards: Rethinking Training Signals in RLVR\\\"\\n    authors: \\\"Ruixin Yang et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2506.10947 / NeurIPS 2025 submission\\\"\\n    category: reward-hacking\\n    role: direct-evidence\\n    relevance: >\\n      Most directly relevant to STA findings. GRPO+random reward on\\n      Qwen2.5-Math improves 21.4%, nearly matching ground-truth reward's\\n      29.1%. Matches our plan017 finding: additive random (PR=48%) >\\n      additive ISR (PR=18%). Structured metrics can be worse than random\\n      noise due to systematic bias vs pure variance.\\n    key_finding: >\\n      Random reward nearly matches ground-truth reward in GRPO training,\\n      suggesting GRPO's group normalization extracts signal from noise.\\n      Effect is model-dependent (works on Qwen2.5, not Llama3).\\n\\n  - id: gao-reward-overoptimization\\n    title: \\\"Scaling Laws for Reward Model Overoptimization\\\"\\n    authors: \\\"Leo Gao, John Schulman, Jacob Hilton\\\"\\n    year: 2023\\n    venue: \\\"ICML 2023 (arXiv 2210.10760)\\\"\\n    category: reward-hacking\\n    role: theoretical-foundation\\n    relevance: >\\n      Foundational work quantifying Goodhart's effect: proxy reward rises\\n      but gold reward first rises then falls. ISR is a proxy reward that\\n      exhibits exactly this pattern — ISR can increase while prove_rate\\n      decreases, making it suitable for post-hoc diagnosis but harmful\\n      as training signal.\\n    key_finding: >\\n      Gold/proxy reward divergence follows predictable scaling laws.\\n      Proxy reward optimization past critical point degrades gold reward,\\n      with the divergence point scaling with model and dataset size.\\n\\n  - id: karwowski-goodhart-rl\\n    title: \\\"Goodhart's Law in Reinforcement Learning\\\"\\n    authors: \\\"Jacek Karwowski, Oliver Hayman, Xingjian Bai, Klaus Kiendlhofer, Charlie Griffin, Joar Skalse\\\"\\n    year: 2024\\n    venue: \\\"ICLR 2024 (arXiv 2310.09144)\\\"\\n    category: reward-hacking\\n    role: theoretical-foundation\\n    relevance: >\\n      Geometric interpretation of Goodhart's Law in MDPs: optimizing\\n      imperfect proxy past critical point decreases true objective. ISR as\\n      proxy has partial correlation with execution correctness — exceeding\\n      critical optimization point pushes policy toward high-ISR but\\n      low-correctness regions. Explains plan002/plan005 negative results.\\n    key_finding: >\\n      Formalizes Goodhart's Law for RL: any non-trivially correlated proxy\\n      reward creates regions where proxy and true reward diverge, and\\n      policy optimization inevitably enters these regions.\\n\\n  # ============================================================\\n  # Category 6: FOL/Prolog formalization with LLMs\\n  # ============================================================\\n\\n  - id: folio\\n    title: \\\"FOLIO: Natural Language Reasoning with First-Order Logic\\\"\\n    authors: \\\"Simeng Han et al.\\\"\\n    year: 2022\\n    venue: \\\"arXiv 2209.00840 / EMNLP 2024\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Primary FOL reasoning benchmark. STA uses FOLIO-style NL->FOL\\n      formalization as the target task for GRPO training. FOLIO's\\n      expert-annotated FOL annotations serve as reference formalizations.\\n    key_finding: >\\n      1,430 NL-FOL paired examples with reasoning depths up to 5+;\\n      GPT-4 still struggles on the hardest examples.\\n\\n  - id: proofwriter\\n    title: \\\"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language\\\"\\n    authors: \\\"Oyvind Tafjord, Bhavana Dalvi, Peter Clark\\\"\\n    year: 2021\\n    venue: \\\"Findings of ACL-IJCNLP 2021\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Source dataset for STA's training data. ProofWriter provides\\n      rule-based logical reasoning problems in natural language that\\n      STA uses for training formalizer models.\\n    key_finding: >\\n      Generative model can reliably produce implications and proofs;\\n      accuracy exceeds prior methods by 9% and generalizes to unseen\\n      proof depths.\\n\\n  - id: logic-lm\\n    title: \\\"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\\\"\\n    authors: \\\"Liangming Pan, Alon Albalak, Xinyi Wang, William Wang\\\"\\n    year: 2023\\n    venue: \\\"Findings of EMNLP 2023\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      LLM->symbolic solver pipeline for logical reasoning, directly\\n      comparable to STA's formalizer->Prolog solver pipeline. Key\\n      difference: Logic-LM uses prompting, STA uses GRPO training.\\n    key_finding: >\\n      LLM+solver achieves 39.2% improvement over LLM-alone on logical\\n      reasoning benchmarks including ProofWriter and FOLIO.\\n\\n  - id: linc\\n    title: \\\"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers\\\"\\n    authors: \\\"Theo X. Olausson, Alex Gu, Ben Lipkin, et al.\\\"\\n    year: 2023\\n    venue: \\\"EMNLP 2023\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      Neurosymbolic approach where LLM translates NL to FOL for theorem\\n      prover. Directly comparable to STA's NL->Prolog translation.\\n      LINC uses prompting-based approach; STA uses RL training.\\n    key_finding: >\\n      StarCoder+ (15.5B) with LINC outperforms GPT-3.5 and GPT-4 with\\n      CoT by 38% and 10% respectively on ProofWriter.\\n\\n  - id: fover-pei2025\\n    title: \\\"FoVer: First-Order Logic Verification for Natural Language Reasoning\\\"\\n    authors: \\\"Yu Pei, Yongping Du, Xingnan Jin\\\"\\n    year: 2025\\n    venue: \\\"TACL 13:1340-1359\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      Uses LLM->FOL->Z3 pipeline for verifying NL reasoning correctness.\\n      Similar to STA's verification pipeline but focuses on post-hoc\\n      verification rather than training reward signal.\\n    key_finding: >\\n      FOL verification via Z3 significantly outperforms existing methods\\n      on ProofWriter and FOLIO benchmarks.\\n\\n  - id: lorp\\n    title: \\\"LoRP: LLM-based Logical Reasoning via Prolog\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"Knowledge-Based Systems 2025\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      LLM->Prolog pipeline with FOL-to-Prolog translation mechanism.\\n      Closest to STA's formalization target (Prolog), though LoRP\\n      uses prompting while STA uses GRPO training with structural reward.\\n    key_finding: >\\n      Systematic FOL-to-Prolog translation extends Prolog expressiveness;\\n      achieves SoTA accuracy on logical reasoning with three-vote majority.\\n\\n  - id: nl2fol\\n    title: \\\"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection\\\"\\n    authors: \\\"Lalwani, Kim, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2405.02318\\\"\\n    category: fol-formalization\\n    role: background\\n    relevance: >\\n      Step-by-step NL->FOL translation using LLMs with SMT solver\\n      verification. Demonstrates the NL->formal logic pipeline that\\n      STA aims to improve via RL training.\\n    key_finding: >\\n      Neurosymbolic NL2FOL achieves 78% F1 on LOGIC dataset and\\n      generalizes to LogicClimate (80% F1), outperforming supervised\\n      models by 21%.\\n\\n  - id: logica2\\n    title: \\\"LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: \\\"IEEE/ACM TASLP 2023\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Logical reasoning evaluation benchmark derived from Chinese civil\\n      service exams. Provides supplementary evaluation for STA's\\n      formalization capabilities.\\n    key_finding: >\\n      8,678 multiple-choice questions covering categorical, disjunctive,\\n      and conditional reasoning; widely used LLM benchmark.\\n\\n  # ============================================================\\n  # Category 7: Goodhart's Law theory and dose-response dynamics\\n  # ============================================================\\n\\n  - id: manheim-goodhart-taxonomy\\n    title: \\\"Categorizing Variants of Goodhart's Law\\\"\\n    authors: \\\"David Manheim, Scott Garrabrant\\\"\\n    year: 2019\\n    venue: \\\"arXiv 1803.04585\\\"\\n    category: goodhart-overoptimization\\n    role: theoretical-foundation\\n    relevance: >\\n      Four-part Goodhart taxonomy: regressional, extremal, causal, adversarial.\\n      STA's high-β ISR collapse is best classified as extremal Goodhart\\n      (policy moves to OOD region where ISR↑ but prove_rate↓). Provides\\n      vocabulary for discussion section.\\n    key_finding: >\\n      First systematic categorization of Goodhart failure modes. Extremal\\n      variant occurs when proxy-goal relationship breaks in out-of-distribution\\n      regions reached by strong optimization.\\n\\n  - id: pan-reward-misspecification\\n    title: \\\"The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models\\\"\\n    authors: \\\"Alexander Pan, Kush Bhatia, Jacob Steinhardt\\\"\\n    year: 2022\\n    venue: \\\"ICLR 2022\\\"\\n    category: goodhart-overoptimization\\n    role: theoretical-foundation\\n    relevance: >\\n      Across 9 environments, more capable agents exploit misspecifications more.\\n      Observes dose-dependent degradation — capability thresholds where true\\n      reward sharply drops. Matches STA's β=0.1→0.3 qualitative shift.\\n    key_finding: >\\n      Reward misspecification causes dose-dependent degradation where true reward\\n      sharply drops past capability thresholds. More capable optimization\\n      produces worse outcomes under misspecification.\\n\\n  - id: kwa-catastrophic-goodhart\\n    title: \\\"Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification\\\"\\n    authors: \\\"Tat-Thang Kwa, Rachel Thomas, Adrià Garriga-Alonso\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS 2024\\\"\\n    category: goodhart-overoptimization\\n    role: theoretical-foundation\\n    relevance: >\\n      If reward model error is heavy-tailed, policies achieve arbitrarily\\n      high proxy reward with no true utility gain. KL regularization provably\\n      fails. Explains why KL penalty in GRPO cannot prevent ISR collapse\\n      at high β if ISR error distribution is heavy-tailed.\\n    key_finding: >\\n      KL-regularized RL provably fails to prevent overoptimization under\\n      heavy-tailed reward misspecification. Policies can achieve arbitrarily\\n      high proxy reward with zero true utility.\\n\\n  - id: rafailov-daa-scaling\\n    title: \\\"Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms\\\"\\n    authors: \\\"Rafael Rafailov, Yaswanth Chittepu, Ryan Park, Harshit Sikchi, Joey Hejna, W. Bradley Knox, Chelsea Finn, Scott Niekum\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS 2024\\\"\\n    category: goodhart-overoptimization\\n    role: supporting-evidence\\n    relevance: >\\n      Extends Gao et al. to DPO/IPO/SLiC. Tests seven β values across\\n      1B-6.9B models. DAAs still overoptimize despite no explicit proxy RM.\\n      Validates β as a \\\"dose\\\" parameter — directly analogous to STA's\\n      ISR weight sweep.\\n    key_finding: >\\n      Direct alignment algorithms exhibit overoptimization following\\n      predictable scaling laws. Smaller models overoptimize sooner.\\n      β-controlled dose-response is a general phenomenon across RL paradigms.\\n\\n  - id: huang-chi-squared\\n    title: \\\"Correcting the Mythos of KL-Regularization: Direct and Contrastive Distribution Correction\\\"\\n    authors: \\\"Afra Feyza Akyürek, Banghua Zhu, Sham Kakade, Jiantao Jiao\\\"\\n    year: 2025\\n    venue: \\\"ICLR 2025 Poster\\\"\\n    category: goodhart-overoptimization\\n    role: supporting-evidence\\n    relevance: >\\n      KL-regularization is theoretically inadequate for preventing\\n      overoptimization. Chi-squared divergence provably alleviates it.\\n      Suggests that even with KL penalty in GRPO, STA's high-β collapse\\n      is theoretically expected.\\n    key_finding: >\\n      Chi-squared preference optimization provably mitigates overoptimization\\n      where KL-regularization fails. Alternative divergence measures offer\\n      stronger guarantees.\\n\\n  - id: coste-rm-ensembles\\n    title: \\\"Reward Model Ensembles Help Mitigate Overoptimization\\\"\\n    authors: \\\"Thomas Coste, Usman Anwar, Robert Kirk, David Krueger\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023 Workshop on Alignment\\\"\\n    category: goodhart-overoptimization\\n    role: background\\n    relevance: >\\n      Worst-case optimization across RM ensembles practically eliminates\\n      overoptimization for BoN and reduces it for PPO. Suggests ensemble\\n      of multiple solver metrics (instead of single ISR) as mitigation.\\n    key_finding: >\\n      RM ensembles with worst-case aggregation mitigate overoptimization.\\n      Ensemble size and diversity directly affect robustness.\\n\\n  # ============================================================\\n  # Category 8: Solver/prover as RL reward signal\\n  # ============================================================\\n\\n  - id: rlsf\\n    title: \\\"Reinforcement Learning via Symbolic Feedback\\\"\\n    authors: \\\"Abhinav Jha, Shikhar Murty, Zico Kolter, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2405.16661\\\"\\n    category: verification-reward\\n    role: direct-competitor\\n    relevance: >\\n      Most directly relevant: uses solver/prover certificates as fine-grained\\n      token-level reward signal. Outperforms traditional approaches on program\\n      synthesis (+31.4%). STA extends this paradigm and shows when it breaks\\n      (Goodhart effects at high auxiliary reward weight).\\n    key_finding: >\\n      Symbolic reasoning tools provide poly-sized certificates as reward.\\n      Smaller RLSF models outperform GPT-4 on structured generation tasks.\\n\\n  - id: fover-kamoi2026\\n    title: \\\"FoVer: Generalizable Process Reward Models via Formally Verified Training Data\\\"\\n    authors: \\\"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\\\"\\n    year: 2025\\n    venue: \\\"Findings of ACL 2026 (arXiv 2502.01345)\\\"\\n    category: verification-reward\\n    role: supporting-evidence\\n    relevance: >\\n      Uses Z3 and Isabelle to synthesize PRM training data by annotating\\n      step-level error labels without human annotation. Same solver family\\n      as STA. Shows verification-based rewards work; STA extends by showing\\n      dose-response dynamics.\\n    key_finding: >\\n      Formally verified training data enables generalizable process reward\\n      models competitive on ProcessBench and 12 reasoning benchmarks.\\n\\n  - id: deepseek-prover-v15\\n    title: \\\"DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search\\\"\\n    authors: \\\"DeepSeek AI\\\"\\n    year: 2024\\n    venue: \\\"ICLR 2025 (arXiv 2408.08152)\\\"\\n    category: verification-reward\\n    role: method-component\\n    relevance: >\\n      Uses GRPO with Lean 4 verification as binary reward. Same algorithm\\n      (GRPO) + formal verification, but binary (pass/fail). Binary reward\\n      avoids the graded-metric Goodhart risk that STA identifies with ISR.\\n    key_finding: >\\n      GRPO + binary Lean verification achieves 63.5% on miniF2F. Binary\\n      correctness guarantee via formal verification sidesteps proxy reward\\n      overoptimization.\\n\\n  - id: alphaproof\\n    title: \\\"AlphaProof\\\"\\n    authors: \\\"Google DeepMind\\\"\\n    year: 2024\\n    venue: \\\"Nature 2025\\\"\\n    category: verification-reward\\n    role: background\\n    relevance: >\\n      AlphaZero-inspired RL with Lean proof verification at scale.\\n      Silver medal at IMO 2024. Binary verification reward avoids the\\n      Goodhart problem STA identifies with graded verification metrics.\\n    key_finding: >\\n      Binary formal verification as RL reward scales to IMO-level\\n      mathematical reasoning. Demonstrates verification-reward RL works\\n      at the frontier of mathematical difficulty.\\n\\n  - id: math-shepherd\\n    title: \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\"\\n    authors: \\\"Peiyi Wang, Lei Li, Zhihong Shao, R.X. Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"ACL 2024 (arXiv 2312.08935)\\\"\\n    category: verification-reward\\n    role: supporting-evidence\\n    relevance: >\\n      Automatically constructs process supervision data and uses it as\\n      step-by-step PPO reward. Automated verification reward without human\\n      labels, analogous to STA's automated ISR computation via solver.\\n    key_finding: >\\n      Automated process supervision improves Mistral-7B on GSM8K\\n      (77.9→84.1%) and MATH (28.6→33.0%) without human annotation.\\n\\n  # ============================================================\\n  # Additional reward-shaping papers (Goodhart survey additions)\\n  # ============================================================\\n\\n  - id: bipars\\n    title: \\\"Learning to Utilize Shaping Rewards: A New Approach of Reward Shaping\\\"\\n    authors: \\\"Yujing Hu, Weixun Wang, Hangtian Jia, et al.\\\"\\n    year: 2020\\n    venue: \\\"NeurIPS 2020\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Bi-level optimization learns parameterized shaping reward weights.\\n      Can transform harmful shaping rewards into beneficial ones by learning\\n      negative weights. Directly addresses STA's problem: when ISR weight\\n      is wrong, automated weight learning could find optimal β.\\n    key_finding: >\\n      Bi-level optimization automatically learns auxiliary reward weights,\\n      outperforming fixed weights and recovering from harmful shaping rewards.\\n\\n  - id: dapo\\n    title: \\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\"\\n    authors: \\\"Qiying Yu et al. (ByteDance)\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2503.14476\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Four techniques for stable multi-component reward in GRPO: Clip-Higher,\\n      Dynamic Sampling, token-level policy gradient, Overlong Reward Shaping.\\n      Addresses stability issues relevant to STA's multi-reward setup.\\n    key_finding: >\\n      Clip-Higher and Dynamic Sampling prevent entropy collapse in GRPO\\n      with multi-component rewards. Soft punishment for overlong outputs\\n      avoids reward hacking through length exploitation.\\n\", \"total_chars\": 38485, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "7a6520b2-613b-4427-ac26-a9fd1277ba49",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\\\", \\\"content\\\": \\\"# Literature Map for Solver Trace Ablation (STA)\\\\n# Categories:\\\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\\\n#   2. reward-shaping: Reward shaping for code/formal verification\\\\n#   3. mutation-testing: Mutation testing in software engineering\\\\n#   4. intensional-analysis: Intensional program analysis\\\\n#   5. reward-hacking: Reward hacking / overoptimization\\\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\\\n#   7. goodhart-overoptimization: Goodhart's Law theory and dose-response dynamics\\\\n#   8. verification-reward: Solver/prover as RL reward signal\\\\n\\\\npapers:\\\\n\\\\n  # ============================================================\\\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\\\n  # ============================================================\\\\n\\\\n  - id: deepseek-r1\\\\n    title: \\\\\\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"DeepSeek-AI\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2501.12948 / Nature 2025\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: method-component\\\\n    relevance: >\\\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\\\n      intensional structural reward for neurosymbolic formalization.\\\\n    key_finding: >\\\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\\\n      showing emergent chain-of-thought reasoning from RL alone.\\\\n\\\\n  - id: deepseekmath\\\\n    title: \\\\\\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2402.03300\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: method-component\\\\n    relevance: >\\\\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\\\\n      used in STA training. GRPO eliminates the critic model by estimating\\\\n      baselines from group scores.\\\\n    key_finding: >\\\\n      GRPO matches PPO performance while significantly reducing training\\\\n      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.\\\\n\\\\n  - id: logic-rl\\\\n    title: \\\\\\\"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Xian et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2502.14768\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic\\\\n      logic puzzles. Closest competitor to STA's approach of RL for logical\\\\n      formalization, though Logic-RL uses extensional (answer-correctness)\\\\n      rewards rather than STA's intensional structural rewards.\\\\n    key_finding: >\\\\n      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;\\\\n      rule-based reward design is critical for RL-based logical reasoning.\\\\n\\\\n  - id: mellgren-prolog-grpo\\\\n    title: \\\\\\\"Training Language Models to Use Prolog as a Tool\\\\\\\"\\\\n    authors: \\\\\\\"Niklas Mellgren\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2512.07407\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,\\\\n      directly comparable to STA's approach of GRPO-training a formalizer.\\\\n      Key difference: uses pass/fail reward vs STA's structural ISR.\\\\n    key_finding: >\\\\n      GRPO is effective for teaching small LLMs to use Prolog as a tool\\\\n      for logical and mathematical reasoning.\\\\n\\\\n  - id: satlm\\\\n    title: \\\\\\\"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\\\\\\\"\\\\n    authors: \\\\\\\"Xi Ye et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"NeurIPS 2023\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: background\\\\n    relevance: >\\\\n      Neurosymbolic approach where LLM generates declarative specifications\\\\n      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)\\\\n      but uses prompting, not RL training.\\\\n    key_finding: >\\\\n      Declarative formulation outperforms imperative program-aided LMs by 23%\\\\n      on GSM; achieves SoTA on LSAT and BoardgameQA.\\\\n\\\\n  # ============================================================\\\\n  # Category 2: Reward shaping for code/formal verification\\\\n  # ============================================================\\\\n\\\\n  - id: lightman-verify-step\\\\n    title: \\\\\\\"Let's Verify Step by Step\\\\\\\"\\\\n    authors: \\\\\\\"Hunter Lightman, Vineet Kosaraju, Yura Burda, et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"arXiv 2305.20050 / ICLR 2024\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: method-component\\\\n    relevance: >\\\\n      Establishes that process supervision (step-level reward) outperforms\\\\n      outcome supervision (final-answer reward) for reasoning. STA's ISR\\\\n      is analogous: it provides structural process-level signal about which\\\\n      components of a formalization matter, rather than just pass/fail.\\\\n    key_finding: >\\\\n      Process-supervised reward model achieves 78% on MATH, significantly\\\\n      outperforming outcome-supervised models. Released PRM800K dataset.\\\\n\\\\n  - id: reward-shaping-rlhf\\\\n    title: \\\\\\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\\\\\"\\\\n    authors: \\\\\\\"Jiayi Fu, Xuandong Zhao, Chengyuan Yao, et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2502.18770\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      Studies reward shaping design principles for RLHF: bounded rewards and\\\\n      rapid-then-convergent growth. STA's ISR follows these principles\\\\n      naturally since structural necessity scores are bounded [0,1].\\\\n    key_finding: >\\\\n      Two key reward shaping principles: (1) bounded RL reward, (2) rapid\\\\n      initial growth with gradual convergence. PAR method achieves 5%+\\\\n      win rate improvement on AlpacaEval 2.0.\\\\n\\\\n  - id: rlvr-reasoning\\\\n    title: \\\\\\\"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2506.14245\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize\\\\n      reasoning. STA argues that for neurosymbolic formalization, binary reward\\\\n      is insufficient and structural reward is needed to avoid reward hacking.\\\\n    key_finding: >\\\\n      RLVR with binary verification implicitly teaches correct reasoning\\\\n      strategies, not just answer matching.\\\\n\\\\n  - id: rubric-grpo\\\\n    title: \\\\\\\"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2605.08061\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Uses structured rubric-based rewards with GRPO, similar in spirit to\\\\n      STA's structured ISR. Key difference: rubric rewards come from LLM\\\\n      judges, while ISR comes from solver-based mutation testing.\\\\n    key_finding: >\\\\n      Structured multi-dimensional reward signals improve GRPO training\\\\n      generalization compared to scalar rewards.\\\\n\\\\n  - id: gao-effective-rl-reward\\\\n    title: \\\\\\\"On Designing Effective RL Reward at Training Time for LLM Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2410.15115\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      Demonstrates that learned process/outcome reward models can hurt RL\\\\n      training, producing worse performance than simple success reward only.\\\\n      Directly explains plan005 NEGATIVE: STA's ISR as auxiliary process\\\\n      reward degrades prove_rate compared to exec-only baseline.\\\\n    key_finding: >\\\\n      PRM/ORM rewards may NOT help or even hurt RL training vs success-only\\\\n      reward. Solution: Clipping and Delta techniques to bound accumulated\\\\n      reward magnitude prevent reward hacking.\\\\n\\\\n  - id: prof-process-outcome\\\\n    title: \\\\\\\"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training\\\\\\\"\\\\n    authors: \\\\\\\"Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2509.03403\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      Shows that naively combining PRM+ORM signals leads to performance\\\\n      degradation. PROF consistency filter retains only PRM-ORM consistent\\\\n      samples, achieving 4%+ improvement over blending. Suggests STA should\\\\n      only apply ISR when consistent with execution outcome.\\\\n    key_finding: >\\\\n      Process rewards frequently suffer from inaccuracies and reward hacking\\\\n      susceptibility. PROF filters training data by PRM-ORM consistency,\\\\n      outperforming naive reward blending by 4%+ accuracy.\\\\n\\\\n  - id: moskovitz-constrained-rlhf\\\\n    title: \\\\\\\"Confronting Reward Model Overoptimization with Constrained RLHF\\\\\\\"\\\\n    authors: \\\\\\\"Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"arXiv 2310.04373 / ICLR 2024\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      First study on overoptimization in composite reward models. Shows that\\\\n      fixed-weight linear scalarization of component rewards leads to\\\\n      degradation past a threshold. Proposes constrained RL with dynamic\\\\n      Lagrange multiplier weighting as alternative to fixed ISR weight.\\\\n    key_finding: >\\\\n      Correlation between component RMs significantly affects overoptimization\\\\n      thresholds. Constrained RL with Lagrange multipliers outperforms\\\\n      fixed-weight reward composition.\\\\n\\\\n  - id: skalse-reward-hacking\\\\n    title: \\\\\\\"Defining and Characterizing Reward Hacking\\\\\\\"\\\\n    authors: \\\\\\\"Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger\\\\\\\"\\\\n    year: 2022\\\\n    venue: \\\\\\\"arXiv 2209.13085 / NeurIPS 2022\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      Formal proof that for stochastic policies, two reward functions are\\\\n      unhackable only if one is constant. Theoretically explains why any\\\\n      non-zero ISR weight can decrease prove_rate -- this is a fundamental\\\\n      property of reward composition, not STA-specific.\\\\n    key_finding: >\\\\n      Any non-constant proxy reward can decrease true reward when optimized.\\\\n      Unhackability requires the proxy to be constant, making all non-trivial\\\\n      auxiliary rewards theoretically vulnerable to degrading primary performance.\\\\n\\\\n  - id: progrs-outcome-conditioned\\\\n    title: \\\\\\\"LLM Reasoning with Process Rewards for Outcome-Guided Steps\\\\\\\"\\\\n    authors: \\\\\\\"Mohammad Rezaei, Jens Lehmann, Sahar Vahdati\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv 2604.02341\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      PRM scores optimized as absolute rewards amplify fluent failure modes.\\\\n      Outcome-conditioned centering shifts incorrect trajectories' PRM scores\\\\n      to zero mean, preserving ranking info without corrupting gradients.\\\\n      Suggests STA should condition ISR on execution outcome.\\\\n    key_finding: >\\\\n      Naive process rewards induce reward hacking by rewarding locally fluent\\\\n      but globally incorrect reasoning. Outcome-conditioned centering resolves\\\\n      the conflict with fewer rollouts than outcome-only baselines.\\\\n\\\\n  - id: qwen-prm-lessons\\\\n    title: \\\\\\\"The Lessons of Developing Process Reward Models in Mathematical Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Zhenru Zhang et al. (Qwen Team, Alibaba)\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"ACL 2025 Findings (arXiv 2501.07301)\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: supporting-evidence\\\\n    relevance: >\\\\n      MC estimation-synthesized PRM data leads to quality degradation; policy\\\\n      model generates \\\\\\\"answer-correct but reasoning-flawed\\\\\\\" responses, causing\\\\n      process reward / outcome misalignment. Directly parallels ISR problem:\\\\n      structurally correct but semantically wrong proof traces get high ISR\\\\n      but low execution reward.\\\\n    key_finding: >\\\\n      PRM performance depends critically on data quality; MC estimation\\\\n      introduces systematic bias. Answer-correct reasoning-flawed samples\\\\n      corrupt process supervision signal.\\\\n\\\\n  # ============================================================\\\\n  # Category 3: Mutation testing in software engineering\\\\n  # ============================================================\\\\n\\\\n  - id: demillo1978\\\\n    title: \\\\\\\"Hints on Test Data Selection: Help for the Practicing Programmer\\\\\\\"\\\\n    authors: \\\\\\\"Richard A. DeMillo, Richard J. Lipton, Frederick G. Sayward\\\\\\\"\\\\n    year: 1978\\\\n    venue: \\\\\\\"Computer 11(4):34-43\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Foundational paper introducing mutation testing. STA's component\\\\n      necessity testing directly extends this idea: instead of mutating\\\\n      source code to test test suites, STA mutates logical formulas\\\\n      to test component necessity for solver success.\\\\n    key_finding: >\\\\n      Introduced mutation testing and the coupling effect hypothesis:\\\\n      tests that detect simple faults also detect complex faults.\\\\n\\\\n  - id: offutt-coupling\\\\n    title: \\\\\\\"Investigations of the Software Testing Coupling Effect\\\\\\\"\\\\n    authors: \\\\\\\"A. Jefferson Offutt\\\\\\\"\\\\n    year: 1992\\\\n    venue: \\\\\\\"ACM TOSEM 1(1):5-20\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Empirically validates the coupling effect hypothesis that underpins\\\\n      mutation testing. STA's single-component ablation is analogous to\\\\n      first-order mutation; the coupling effect suggests this suffices.\\\\n    key_finding: >\\\\n      Test data killing all first-order mutants killed >99% of second-\\\\n      and third-order mutants, validating the coupling effect.\\\\n\\\\n  - id: jia-harman-survey\\\\n    title: \\\\\\\"An Analysis and Survey of the Development of Mutation Testing\\\\\\\"\\\\n    authors: \\\\\\\"Yue Jia, Mark Harman\\\\\\\"\\\\n    year: 2011\\\\n    venue: \\\\\\\"IEEE TSE 37(5):649-678\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Comprehensive survey of mutation testing covering three decades of\\\\n      development. Provides theoretical and practical foundation for STA's\\\\n      adaptation of mutation testing to logical formulas.\\\\n    key_finding: >\\\\n      Systematic classification of mutation operators, cost reduction\\\\n      techniques, and equivalence problem -- all relevant to STA's design\\\\n      of clause-level ablation operators.\\\\n\\\\n  - id: just-mutants-real-faults\\\\n    title: \\\\\\\"Are Mutants a Valid Substitute for Real Faults in Software Testing?\\\\\\\"\\\\n    authors: \\\\\\\"Rene Just, Darioush Jalali, Laura Inozemtseva, et al.\\\\\\\"\\\\n    year: 2014\\\\n    venue: \\\\\\\"FSE 2014\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Validates that mutation testing (structural/intensional analysis of\\\\n      program adequacy) correlates with real fault detection. Supports STA's\\\\n      premise that structural analysis of formalization components provides\\\\n      meaningful signal about formalization quality.\\\\n    key_finding: >\\\\n      Mutant detection is statistically correlated with real fault detection,\\\\n      and mutation score is a better predictor of test effectiveness than\\\\n      code coverage.\\\\n\\\\n  - id: llmorpheus\\\\n    title: \\\\\\\"LLMorpheus: Mutation Testing Using Large Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Frank Tip, Jon Bell, et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"IEEE TSE 2025\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Uses LLMs to generate realistic code mutants beyond traditional\\\\n      mutation operators. Shows mutation testing evolving toward\\\\n      ML-integrated approaches, validating STA's cross-pollination\\\\n      of mutation testing ideas into ML training.\\\\n    key_finding: >\\\\n      LLM-generated mutants simulate real bugs that rule-based operators\\\\n      cannot produce, improving mutation testing realism.\\\\n\\\\n  - id: mutation-guided-meta\\\\n    title: \\\\\\\"Mutation-Guided LLM-based Test Generation at Meta\\\\\\\"\\\\n    authors: \\\\\\\"Christopher Foster et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"FSE 2025\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Industrial application of mutation-guided LLM test generation at\\\\n      Meta. Demonstrates that mutation analysis can guide LLM behavior\\\\n      in production -- analogous to how STA uses mutation (ablation) to\\\\n      guide GRPO reward signal.\\\\n    key_finding: >\\\\n      Mutation-guided approach generates tests that kill significantly\\\\n      more mutants than unguided LLM test generation at Meta scale.\\\\n\\\\n  - id: mutation-consistency-llm\\\\n    title: \\\\\\\"Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2401.05940\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Uses code mutations to evaluate LLM code understanding consistency.\\\\n      Conceptually related to STA: both use systematic code/formula\\\\n      mutations to assess model capabilities.\\\\n    key_finding: >\\\\n      LLMs show significant inconsistency when evaluated on mutated code\\\\n      variants, suggesting superficial pattern matching.\\\\n\\\\n  # ============================================================\\\\n  # Category 4: Intensional program analysis\\\\n  # ============================================================\\\\n\\\\n  - id: deepmutation\\\\n    title: \\\\\\\"A Probabilistic Framework for Mutation Testing in Deep Neural Networks\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"Information and Software Technology 2023\\\\\\\"\\\\n    category: intensional-analysis\\\\n    role: background\\\\n    relevance: >\\\\n      Extends mutation testing to DNN testing with probabilistic mutation\\\\n      operators. Parallel to STA's extension of mutation testing from\\\\n      traditional programs to logical formulas.\\\\n    key_finding: >\\\\n      Probabilistic mutation framework enables meaningful test adequacy\\\\n      assessment for neural networks through structural perturbation.\\\\n\\\\n  # ============================================================\\\\n  # Category 5: Reward hacking / overoptimization\\\\n  # ============================================================\\\\n\\\\n  - id: inform-reward-hacking\\\\n    title: \\\\\\\"InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"NeurIPS 2024\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: background\\\\n    relevance: >\\\\n      Proposes information-bottleneck approach to detect and mitigate reward\\\\n      hacking. STA's ISR addresses the same problem differently: by grounding\\\\n      reward in verifiable structural properties (component necessity), it\\\\n      reduces the attack surface for reward hacking.\\\\n    key_finding: >\\\\n      Variational information bottleneck filters irrelevant features from\\\\n      reward model; Cluster Separation Index detects reward overoptimization.\\\\n\\\\n  - id: mo-grpo\\\\n    title: \\\\\\\"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\\\\\\\"\\\\n    authors: \\\\\\\"CyberAgent AI Lab\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2509.22047\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: background\\\\n    relevance: >\\\\n      Directly addresses GRPO reward hacking in multi-objective settings.\\\\n      STA's ISR can be viewed as adding a structural objective to the\\\\n      correctness objective, making MO-GRPO's insights directly applicable.\\\\n    key_finding: >\\\\n      Standard GRPO normalizes after summing rewards, allowing high-variance\\\\n      objectives to dominate. MO-GRPO equalizes scales before aggregation.\\\\n\\\\n  - id: reward-hacking-survey\\\\n    title: \\\\\\\"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv 2604.13602\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: background\\\\n    relevance: >\\\\n      Comprehensive survey of reward hacking mechanisms in the LLM era.\\\\n      Provides theoretical framework for understanding why STA's structural\\\\n      reward is more robust than pure outcome-based reward.\\\\n    key_finding: >\\\\n      Reward hacking manifests through specification gaming, reward model\\\\n      exploitation, and emergent misalignment; structural verification\\\\n      rewards are more robust than learned reward models.\\\\n\\\\n  - id: energy-loss-reward-hacking\\\\n    title: \\\\\\\"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"ICML 2025\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: background\\\\n    relevance: >\\\\n      Identifies energy loss in LLM final layer as an indicator of reward\\\\n      hacking during RL. Provides complementary diagnostic to STA's\\\\n      structural reward approach.\\\\n    key_finding: >\\\\n      Energy loss in the final layer increases during RL and excessive\\\\n      increase characterizes reward hacking; EPPO algorithm penalizes\\\\n      this to mitigate hacking.\\\\n\\\\n  - id: spurious-rewards\\\\n    title: \\\\\\\"Spurious Rewards: Rethinking Training Signals in RLVR\\\\\\\"\\\\n    authors: \\\\\\\"Ruixin Yang et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2506.10947 / NeurIPS 2025 submission\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: direct-evidence\\\\n    relevance: >\\\\n      Most directly relevant to STA findings. GRPO+random reward on\\\\n      Qwen2.5-Math improves 21.4%, nearly matching ground-truth reward's\\\\n      29.1%. Matches our plan017 finding: additive random (PR=48%) >\\\\n      additive ISR (PR=18%). Structured metrics can be worse than random\\\\n      noise due to systematic bias vs pure variance.\\\\n    key_finding: >\\\\n      Random reward nearly matches ground-truth reward in GRPO training,\\\\n      suggesting GRPO's group normalization extracts signal from noise.\\\\n      Effect is model-dependent (works on Qwen2.5, not Llama3).\\\\n\\\\n  - id: gao-reward-overoptimization\\\\n    title: \\\\\\\"Scaling Laws for Reward Model Overoptimization\\\\\\\"\\\\n    authors: \\\\\\\"Leo Gao, John Schulman, Jacob Hilton\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"ICML 2023 (arXiv 2210.10760)\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: theoretical-foundation\\\\n    relevance: >\\\\n      Foundational work quantifying Goodhart's effect: proxy reward rises\\\\n      but gold reward first rises then falls. ISR is a proxy reward that\\\\n      exhibits exactly this pattern — ISR can increase while prove_rate\\\\n      decreases, making it suitable for post-hoc diagnosis but harmful\\\\n      as training signal.\\\\n    key_finding: >\\\\n      Gold/proxy reward divergence follows predictable scaling laws.\\\\n      Proxy reward optimization past critical point degrades gold reward,\\\\n      with the divergence point scaling with model and dataset size.\\\\n\\\\n  - id: karwowski-goodhart-rl\\\\n    title: \\\\\\\"Goodhart's Law in Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Jacek Karwowski, Oliver Hayman, Xingjian Bai, Klaus Kiendlhofer, Charlie Griffin, Joar Skalse\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"ICLR 2024 (arXiv 2310.09144)\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: theoretical-foundation\\\\n    relevance: >\\\\n      Geometric interpretation of Goodhart's Law in MDPs: optimizing\\\\n      imperfect proxy past critical point decreases true objective. ISR as\\\\n      proxy has partial correlation with execution correctness — exceeding\\\\n      critical optimization point pushes policy toward high-ISR but\\\\n      low-correctness regions. Explains plan002/plan005 negative results.\\\\n    key_finding: >\\\\n      Formalizes Goodhart's Law for RL: any non-trivially correlated proxy\\\\n      reward creates regions where proxy and true reward diverge, and\\\\n      policy optimization inevitably enters these regions.\\\\n\\\\n  # ============================================================\\\\n  # Category 6: FOL/Prolog formalization with LLMs\\\\n  # ============================================================\\\\n\\\\n  - id: folio\\\\n    title: \\\\\\\"FOLIO: Natural Language Reasoning with First-Order Logic\\\\\\\"\\\\n    authors: \\\\\\\"Simeng Han et al.\\\\\\\"\\\\n    year: 2022\\\\n    venue: \\\\\\\"arXiv 2209.00840 / EMNLP 2024\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: evaluation\\\\n    relevance: >\\\\n      Primary FOL reasoning benchmark. STA uses FOLIO-style NL->FOL\\\\n      formalization as the target task for GRPO training. FOLIO's\\\\n      expert-annotated FOL annotations serve as reference formalizations.\\\\n    key_finding: >\\\\n      1,430 NL-FOL paired examples with reasoning depths up to 5+;\\\\n      GPT-4 still struggles on the hardest examples.\\\\n\\\\n  - id: proofwriter\\\\n    title: \\\\\\\"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language\\\\\\\"\\\\n    authors: \\\\\\\"Oyvind Tafjord, Bhavana Dalvi, Peter Clark\\\\\\\"\\\\n    year: 2021\\\\n    venue: \\\\\\\"Findings of ACL-IJCNLP 2021\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: evaluation\\\\n    relevance: >\\\\n      Source dataset for STA's training data. ProofWriter provides\\\\n      rule-based logical reasoning problems in natural language that\\\\n      STA uses for training formalizer models.\\\\n    key_finding: >\\\\n      Generative model can reliably produce implications and proofs;\\\\n      accuracy exceeds prior methods by 9% and generalizes to unseen\\\\n      proof depths.\\\\n\\\\n  - id: logic-lm\\\\n    title: \\\\\\\"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Liangming Pan, Alon Albalak, Xinyi Wang, William Wang\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"Findings of EMNLP 2023\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      LLM->symbolic solver pipeline for logical reasoning, directly\\\\n      comparable to STA's formalizer->Prolog solver pipeline. Key\\\\n      difference: Logic-LM uses prompting, STA uses GRPO training.\\\\n    key_finding: >\\\\n      LLM+solver achieves 39.2% improvement over LLM-alone on logical\\\\n      reasoning benchmarks including ProofWriter and FOLIO.\\\\n\\\\n  - id: linc\\\\n    title: \\\\\\\"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers\\\\\\\"\\\\n    authors: \\\\\\\"Theo X. Olausson, Alex Gu, Ben Lipkin, et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"EMNLP 2023\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Neurosymbolic approach where LLM translates NL to FOL for theorem\\\\n      prover. Directly comparable to STA's NL->Prolog translation.\\\\n      LINC uses prompting-based approach; STA uses RL training.\\\\n    key_finding: >\\\\n      StarCoder+ (15.5B) with LINC outperforms GPT-3.5 and GPT-4 with\\\\n      CoT by 38% and 10% respectively on ProofWriter.\\\\n\\\\n  - id: fover-pei2025\\\\n    title: \\\\\\\"FoVer: First-Order Logic Verification for Natural Language Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Yu Pei, Yongping Du, Xingnan Jin\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"TACL 13:1340-1359\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Uses LLM->FOL->Z3 pipeline for verifying NL reasoning correctness.\\\\n      Similar to STA's verification pipeline but focuses on post-hoc\\\\n      verification rather than training reward signal.\\\\n    key_finding: >\\\\n      FOL verification via Z3 significantly outperforms existing methods\\\\n      on ProofWriter and FOLIO benchmarks.\\\\n\\\\n  - id: lorp\\\\n    title: \\\\\\\"LoRP: LLM-based Logical Reasoning via Prolog\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"Knowledge-Based Systems 2025\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      LLM->Prolog pipeline with FOL-to-Prolog translation mechanism.\\\\n      Closest to STA's formalization target (Prolog), though LoRP\\\\n      uses prompting while STA uses GRPO training with structural reward.\\\\n    key_finding: >\\\\n      Systematic FOL-to-Prolog translation extends Prolog expressiveness;\\\\n      achieves SoTA accuracy on logical reasoning with three-vote majority.\\\\n\\\\n  - id: nl2fol\\\\n    title: \\\\\\\"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection\\\\\\\"\\\\n    authors: \\\\\\\"Lalwani, Kim, et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2405.02318\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: background\\\\n    relevance: >\\\\n      Step-by-step NL->FOL translation using LLMs with SMT solver\\\\n      verification. Demonstrates the NL->formal logic pipeline that\\\\n      STA aims to improve via RL training.\\\\n    key_finding: >\\\\n      Neurosymbolic NL2FOL achieves 78% F1 on LOGIC dataset and\\\\n      generalizes to LogicClimate (80% F1), outperforming supervised\\\\n      models by 21%.\\\\n\\\\n  - id: logica2\\\\n    title: \\\\\\\"LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding\\\\\\\"\\\\n    authors: \\\\\\\"Liu et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"IEEE/ACM TASLP 2023\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: evaluation\\\\n    relevance: >\\\\n      Logical reasoning evaluation benchmark derived from Chinese civil\\\\n      service exams. Provides supplementary evaluation for STA's\\\\n      formalization capabilities.\\\\n    key_finding: >\\\\n      8,678 multiple-choice questions covering categorical, disjunctive,\\\\n      and conditional reasoning; widely used LLM benchmark.\\\\n\\\\n  # ============================================================\\\\n  # Category 7: Goodhart's Law theory and dose-response dynamics\\\\n  # ============================================================\\\\n\\\\n  - id: manheim-goodhart-taxonomy\\\\n    title: \\\\\\\"Categorizing Variants of Goodhart's Law\\\\\\\"\\\\n    authors: \\\\\\\"David Manheim, Scott Garrabrant\\\\\\\"\\\\n    year: 2019\\\\n    venue: \\\\\\\"arXiv 1803.04585\\\\\\\"\\\\n    category: goodhart-overoptimization\\\\n    role: theoretical-foundation\\\\n    relevance: >\\\\n      Four-part Goodhart taxonomy: regressional, extremal, causal, adversarial.\\\\n      STA's high-β ISR collapse is best classified as extremal Goodhart\\\\n      (policy moves to OOD region where ISR↑ but prove_rate↓). Provides\\\\n      vocabulary for discussion section.\\\\n    key_finding: >\\\\n      First systematic categorization of Goodhart failure modes. Extremal\\\\n      variant occurs when proxy-goal relationship breaks in out-of-distribution\\\\n      regions reached by strong optimization.\\\\n\\\\n  - id: pan-reward-misspecification\\\\n    title: \\\\\\\"The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models\\\\\\\"\\\\n    authors: \\\\\\\"Alexander Pan, Kush Bhatia, Jacob Steinhardt\\\\\\\"\\\\n    year: 2022\\\\n    venue: \\\\\\\"ICLR 2022\\\\\\\"\\\\n    category: goodhart-overoptimization\\\\n    role: theoretical-foundation\\\\n    relevance: >\\\\n      Across 9 environments, more capable agents exploit misspecifications more.\\\\n      Observes dose-dependent degradation — capability thresholds where true\\\\n      reward sharply drops. Matches STA's β=0.1→0.3 qualitative shift.\\\\n    key_finding: >\\\\n      Reward misspecification causes dose-dependent degradation where true reward\\\\n      sharply drops past capability thresholds. More capable optimization\\\\n      produces worse outcomes under misspecification.\\\\n\\\\n  - id: kwa-catastrophic-goodhart\\\\n    title: \\\\\\\"Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification\\\\\\\"\\\\n    authors: \\\\\\\"Tat-Thang Kwa, Rachel Thomas, Adrià Garriga-Alonso\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"NeurIPS 2024\\\\\\\"\\\\n    category: goodhart-overoptimization\\\\n    role: theoretical-foundation\\\\n    relevance: >\\\\n      If reward model error is heavy-tailed, policies achieve arbitrarily\\\\n      high proxy reward with no true utility gain. KL regularization provably\\\\n      fails. Explains why KL penalty in GRPO cannot prevent ISR collapse\\\\n      at high β if ISR error distribution is heavy-tailed.\\\\n    key_finding: >\\\\n      KL-regularized RL provably fails to prevent overoptimization under\\\\n      heavy-tailed reward misspecification. Policies can achieve arbitrarily\\\\n      high proxy reward with zero true utility.\\\\n\\\\n  - id: rafailov-daa-scaling\\\\n    title: \\\\\\\"Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms\\\\\\\"\\\\n    authors: \\\\\\\"Rafael Rafailov, Yaswanth Chittepu, Ryan Park, Harshit Sikchi, Joey Hejna, W. Bradley Knox, Chelsea Finn, Scott Niekum\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"NeurIPS 2024\\\\\\\"\\\\n    category: goodhart-overoptimization\\\\n    role: supporting-evidence\\\\n    relevance: >\\\\n      Extends Gao et al. to DPO/IPO/SLiC. Tests seven β values across\\\\n      1B-6.9B models. DAAs still overoptimize despite no explicit proxy RM.\\\\n      Validates β as a \\\\\\\"dose\\\\\\\" parameter — directly analogous to STA's\\\\n      ISR weight sweep.\\\\n    key_finding: >\\\\n      Direct alignment algorithms exhibit overoptimization following\\\\n      predictable scaling laws. Smaller models overoptimize sooner.\\\\n      β-controlled dose-response is a general phenomenon across RL paradigms.\\\\n\\\\n  - id: huang-chi-squared\\\\n    title: \\\\\\\"Correcting the Mythos of KL-Regularization: Direct and Contrastive Distribution Correction\\\\\\\"\\\\n    authors: \\\\\\\"Afra Feyza Akyürek, Banghua Zhu, Sham Kakade, Jiantao Jiao\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"ICLR 2025 Poster\\\\\\\"\\\\n    category: goodhart-overoptimization\\\\n    role: supporting-evidence\\\\n    relevance: >\\\\n      KL-regularization is theoretically inadequate for preventing\\\\n      overoptimization. Chi-squared divergence provably alleviates it.\\\\n      Suggests that even with KL penalty in GRPO, STA's high-β collapse\\\\n      is theoretically expected.\\\\n    key_finding: >\\\\n      Chi-squared preference optimization provably mitigates overoptimization\\\\n      where KL-regularization fails. Alternative divergence measures offer\\\\n      stronger guarantees.\\\\n\\\\n  - id: coste-rm-ensembles\\\\n    title: \\\\\\\"Reward Model Ensembles Help Mitigate Overoptimization\\\\\\\"\\\\n    authors: \\\\\\\"Thomas Coste, Usman Anwar, Robert Kirk, David Krueger\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"NeurIPS 2023 Workshop on Alignment\\\\\\\"\\\\n    category: goodhart-overoptimization\\\\n    role: background\\\\n    relevance: >\\\\n      Worst-case optimization across RM ensembles practically eliminates\\\\n      overoptimization for BoN and reduces it for PPO. Suggests ensemble\\\\n      of multiple solver metrics (instead of single ISR) as mitigation.\\\\n    key_finding: >\\\\n      RM ensembles with worst-case aggregation mitigate overoptimization.\\\\n      Ensemble size and diversity directly affect robustness.\\\\n\\\\n  # ============================================================\\\\n  # Category 8: Solver/prover as RL reward signal\\\\n  # ============================================================\\\\n\\\\n  - id: rlsf\\\\n    title: \\\\\\\"Reinforcement Learning via Symbolic Feedback\\\\\\\"\\\\n    authors: \\\\\\\"Abhinav Jha, Shikhar Murty, Zico Kolter, et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2405.16661\\\\\\\"\\\\n    category: verification-reward\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Most directly relevant: uses solver/prover certificates as fine-grained\\\\n      token-level reward signal. Outperforms traditional approaches on program\\\\n      synthesis (+31.4%). STA extends this paradigm and shows when it breaks\\\\n      (Goodhart effects at high auxiliary reward weight).\\\\n    key_finding: >\\\\n      Symbolic reasoning tools provide poly-sized certificates as reward.\\\\n      Smaller RLSF models outperform GPT-4 on structured generation tasks.\\\\n\\\\n  - id: fover-kamoi2026\\\\n    title: \\\\\\\"FoVer: Generalizable Process Reward Models via Formally Verified Training Data\\\\\\\"\\\\n    authors: \\\\\\\"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"Findings of ACL 2026 (arXiv 2502.01345)\\\\\\\"\\\\n    category: verification-reward\\\\n    role: supporting-evidence\\\\n    relevance: >\\\\n      Uses Z3 and Isabelle to synthesize PRM training data by annotating\\\\n      step-level error labels without human annotation. Same solver family\\\\n      as STA. Shows verification-based rewards work; STA extends by showing\\\\n      dose-response dynamics.\\\\n    key_finding: >\\\\n      Formally verified training data enables generalizable process reward\\\\n      models competitive on ProcessBench and 12 reasoning benchmarks.\\\\n\\\\n  - id: deepseek-prover-v15\\\\n    title: \\\\\\\"DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search\\\\\\\"\\\\n    authors: \\\\\\\"DeepSeek AI\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"ICLR 2025 (arXiv 2408.08152)\\\\\\\"\\\\n    category: verification-reward\\\\n    role: method-component\\\\n    relevance: >\\\\n      Uses GRPO with Lean 4 verification as binary reward. Same algorithm\\\\n      (GRPO) + formal verification, but binary (pass/fail). Binary reward\\\\n      avoids the graded-metric Goodhart risk that STA identifies with ISR.\\\\n    key_finding: >\\\\n      GRPO + binary Lean verification achieves 63.5% on miniF2F. Binary\\\\n      correctness guarantee via formal verification sidesteps proxy reward\\\\n      overoptimization.\\\\n\\\\n  - id: alphaproof\\\\n    title: \\\\\\\"AlphaProof\\\\\\\"\\\\n    authors: \\\\\\\"Google DeepMind\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"Nature 2025\\\\\\\"\\\\n    category: verification-reward\\\\n    role: background\\\\n    relevance: >\\\\n      AlphaZero-inspired RL with Lean proof verification at scale.\\\\n      Silver medal at IMO 2024. Binary verification reward avoids the\\\\n      Goodhart problem STA identifies with graded verification metrics.\\\\n    key_finding: >\\\\n      Binary formal verification as RL reward scales to IMO-level\\\\n      mathematical reasoning. Demonstrates verification-reward RL works\\\\n      at the frontier of mathematical difficulty.\\\\n\\\\n  - id: math-shepherd\\\\n    title: \\\\\\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\\\\\"\\\\n    authors: \\\\\\\"Peiyi Wang, Lei Li, Zhihong Shao, R.X. Xu, et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"ACL 2024 (arXiv 2312.08935)\\\\\\\"\\\\n    category: verification-reward\\\\n    role: supporting-evidence\\\\n    relevance: >\\\\n      Automatically constructs process supervision data and uses it as\\\\n      step-by-step PPO reward. Automated verification reward without human\\\\n      labels, analogous to STA's automated ISR computation via solver.\\\\n    key_finding: >\\\\n      Automated process supervision improves Mistral-7B on GSM8K\\\\n      (77.9→84.1%) and MATH (28.6→33.0%) without human annotation.\\\\n\\\\n  # ============================================================\\\\n  # Additional reward-shaping papers (Goodhart survey additions)\\\\n  # ============================================================\\\\n\\\\n  - id: bipars\\\\n    title: \\\\\\\"Learning to Utilize Shaping Rewards: A New Approach of Reward Shaping\\\\\\\"\\\\n    authors: \\\\\\\"Yujing Hu, Weixun Wang, Hangtian Jia, et al.\\\\\\\"\\\\n    year: 2020\\\\n    venue: \\\\\\\"NeurIPS 2020\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      Bi-level optimization learns parameterized shaping reward weights.\\\\n      Can transform harmful shaping rewards into beneficial ones by learning\\\\n      negative weights. Directly addresses STA's problem: when ISR weight\\\\n      is wrong, automated weight learning could find optimal β.\\\\n    key_finding: >\\\\n      Bi-level optimization automatically learns auxiliary reward weights,\\\\n      outperforming fixed weights and recovering from harmful shaping rewards.\\\\n\\\\n  - id: dapo\\\\n    title: \\\\\\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\\\\\"\\\\n    authors: \\\\\\\"Qiying Yu et al. (ByteDance)\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2503.14476\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      Four techniques for stable multi-component reward in GRPO: Clip-Higher,\\\\n      Dynamic Sampling, token-level policy gradient, Overlong Reward Shaping.\\\\n      Addresses stability issues relevant to STA's multi-reward setup.\\\\n    key_finding: >\\\\n      Clip-Higher and Dynamic Sampling prevent entropy collapse in GRPO\\\\n      with multi-component rewards. Soft punishment for overlong outputs\\\\n      avoids reward hacking through length exploitation.\\\\n\\\", \\\"total_chars\\\": 38485, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\", \"content\": \"# Literature Map for Solver Trace Ablation (STA)\\n# Categories:\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\n#   2. reward-shaping: Reward shaping for code/formal verification\\n#   3. mutation-testing: Mutation testing in software engineering\\n#   4. intensional-analysis: Intensional program analysis\\n#   5. reward-hacking: Reward hacking / overoptimization\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\n#   7. goodhart-overoptimization: Goodhart's Law theory and dose-response dynamics\\n#   8. verification-reward: Solver/prover as RL reward signal\\n\\npapers:\\n\\n  # ============================================================\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\n  # ============================================================\\n\\n  - id: deepseek-r1\\n    title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n    authors: \\\"DeepSeek-AI\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2501.12948 / Nature 2025\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\n      intensional structural reward for neurosymbolic formalization.\\n    key_finding: >\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\n      showing emergent chain-of-thought reasoning from RL alone.\\n\\n  - id: deepseekmath\\n    title: \\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\"\\n    authors: \\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2402.03300\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\\n      used in STA training. GRPO eliminates the critic model by estimating\\n      baselines from group scores.\\n    key_finding: >\\n      GRPO matches PPO performance while significantly reducing training\\n      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.\\n\\n  - id: logic-rl\\n    title: \\\"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\\\"\\n    authors: \\\"Xian et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.14768\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic\\n      logic puzzles. Closest competitor to STA's approach of RL for logical\\n      formalization, though Logic-RL uses extensional (answer-correctness)\\n      rewards rather than STA's intensional structural rewards.\\n    key_finding: >\\n      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;\\n      rule-based reward design is critical for RL-based logical reasoning.\\n\\n  - id: mellgren-prolog-grpo\\n    title: \\\"Training Language Models to Use Prolog as a Tool\\\"\\n    authors: \\\"Niklas Mellgren\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2512.07407\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,\\n      directly comparable to STA's approach of GRPO-training a formalizer.\\n      Key difference: uses pass/fail reward vs STA's structural ISR.\\n    key_finding: >\\n      GRPO is effective for teaching small LLMs to use Prolog as a tool\\n      for logical and mathematical reasoning.\\n\\n  - id: satlm\\n    title: \\\"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\\\"\\n    authors: \\\"Xi Ye et al.\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023\\\"\\n    category: neurosymbolic-rl\\n    role: background\\n    relevance: >\\n      Neurosymbolic approach where LLM generates declarative specifications\\n      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)\\n      but uses prompting, not RL training.\\n    key_finding: >\\n      Declarative formulation outperforms imperative program-aided LMs by 23%\\n      on GSM; achieves SoTA on LSAT and BoardgameQA.\\n\\n  # ============================================================\\n  # Category 2: Reward shaping for code/formal verification\\n  # ============================================================\\n\\n  - id: lightman-verify-step\\n    title: \\\"Let's Verify Step by Step\\\"\\n    authors: \\\"Hunter Lightman, Vineet Kosaraju, Yura Burda, et al.\\\"\\n    year: 2023\\n    venue: \\\"arXiv 2305.20050 / ICLR 2024\\\"\\n    category: reward-shaping\\n    role: method-component\\n    relevance: >\\n      Establishes that process supervision (step-level reward) outperforms\\n      outcome supervision (final-answer reward) for reasoning. STA's ISR\\n      is analogous: it provides structural process-level signal about which\\n      components of a formalization matter, rather than just pass/fail.\\n    key_finding: >\\n      Process-supervised reward model achieves 78% on MATH, significantly\\n      outperforming outcome-supervised models. Released PRM800K dataset.\\n\\n  - id: reward-shaping-rlhf\\n    title: \\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\"\\n    authors: \\\"Jiayi Fu, Xuandong Zhao, Chengyuan Yao, et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.18770\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Studies reward shaping design principles for RLHF: bounded rewards and\\n      rapid-then-convergent growth. STA's ISR follows these principles\\n      naturally since structural necessity scores are bounded [0,1].\\n    key_finding: >\\n      Two key reward shaping principles: (1) bounded RL reward, (2) rapid\\n      initial growth with gradual convergence. PAR method achieves 5%+\\n      win rate improvement on AlpacaEval 2.0.\\n\\n  - id: rlvr-reasoning\\n    title: \\\"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2506.14245\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize\\n      reasoning. STA argues that for neurosymbolic formalization, binary reward\\n      is insufficient and structural reward is needed to avoid reward hacking.\\n    key_finding: >\\n      RLVR with binary verification implicitly teaches correct reasoning\\n      strategies, not just answer matching.\\n\\n  - id: rubric-grpo\\n    title: \\\"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2605.08061\\\"\\n    category: reward-shaping\\n    role: direct-competitor\\n    relevance: >\\n      Uses structured rubric-based rewards with GRPO, similar in spirit to\\n      STA's structured ISR. Key difference: rubric rewards come from LLM\\n      judges, while ISR comes from solver-based mutation testing.\\n    key_finding: >\\n      Structured multi-dimensional reward signals improve GRPO training\\n      generalization compared to scalar rewards.\\n\\n  - id: gao-effective-rl-reward\\n    title: \\\"On Designing Effective RL Reward at Training Time for LLM Reasoning\\\"\\n    authors: \\\"Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2410.15115\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Demonstrates that learned process/outcome reward models can hurt RL\\n      training, producing worse performance than simple success reward only.\\n      Directly explains plan005 NEGATIVE: STA's ISR as auxiliary process\\n      reward degrades prove_rate compared to exec-only baseline.\\n    key_finding: >\\n      PRM/ORM rewards may NOT help or even hurt RL training vs success-only\\n      reward. Solution: Clipping and Delta techniques to bound accumulated\\n      reward magnitude prevent reward hacking.\\n\\n  - id: prof-process-outcome\\n    title: \\\"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training\\\"\\n    authors: \\\"Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2509.03403\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Shows that naively combining PRM+ORM signals leads to performance\\n      degradation. PROF consistency filter retains only PRM-ORM consistent\\n      samples, achieving 4%+ improvement over blending. Suggests STA should\\n      only apply ISR when consistent with execution outcome.\\n    key_finding: >\\n      Process rewards frequently suffer from inaccuracies and reward hacking\\n      susceptibility. PROF filters training data by PRM-ORM consistency,\\n      outperforming naive reward blending by 4%+ accuracy.\\n\\n  - id: moskovitz-constrained-rlhf\\n    title: \\\"Confronting Reward Model Overoptimization with Constrained RLHF\\\"\\n    authors: \\\"Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer\\\"\\n    year: 2023\\n    venue: \\\"arXiv 2310.04373 / ICLR 2024\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      First study on overoptimization in composite reward models. Shows that\\n      fixed-weight linear scalarization of component rewards leads to\\n      degradation past a threshold. Proposes constrained RL with dynamic\\n      Lagrange multiplier weighting as alternative to fixed ISR weight.\\n    key_finding: >\\n      Correlation between component RMs significantly affects overoptimization\\n      thresholds. Constrained RL with Lagrange multipliers outperforms\\n      fixed-weight reward composition.\\n\\n  - id: skalse-reward-hacking\\n    title: \\\"Defining and Characterizing Reward Hacking\\\"\\n    authors: \\\"Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger\\\"\\n    year: 2022\\n    venue: \\\"arXiv 2209.13085 / NeurIPS 2022\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Formal proof that for stochastic policies, two reward functions are\\n      unhackable only if one is constant. Theoretically explains why any\\n      non-zero ISR weight can decrease prove_rate -- this is a fundamental\\n      property of reward composition, not STA-specific.\\n    key_finding: >\\n      Any non-constant proxy reward can decrease true reward when optimized.\\n      Unhackability requires the proxy to be constant, making all non-trivial\\n      auxiliary rewards theoretically vulnerable to degrading primary performance.\\n\\n  - id: progrs-outcome-conditioned\\n    title: \\\"LLM Reasoning with Process Rewards for Outcome-Guided Steps\\\"\\n    authors: \\\"Mohammad Rezaei, Jens Lehmann, Sahar Vahdati\\\"\\n    year: 2026\\n    venue: \\\"arXiv 2604.02341\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      PRM scores optimized as absolute rewards amplify fluent failure modes.\\n      Outcome-conditioned centering shifts incorrect trajectories' PRM scores\\n      to zero mean, preserving ranking info without corrupting gradients.\\n      Suggests STA should condition ISR on execution outcome.\\n    key_finding: >\\n      Naive process rewards induce reward hacking by rewarding locally fluent\\n      but globally incorrect reasoning. Outcome-conditioned centering resolves\\n      the conflict with fewer rollouts than outcome-only baselines.\\n\\n  - id: qwen-prm-lessons\\n    title: \\\"The Lessons of Developing Process Reward Models in Mathematical Reasoning\\\"\\n    authors: \\\"Zhenru Zhang et al. (Qwen Team, Alibaba)\\\"\\n    year: 2025\\n    venue: \\\"ACL 2025 Findings (arXiv 2501.07301)\\\"\\n    category: reward-shaping\\n    role: supporting-evidence\\n    relevance: >\\n      MC estimation-synthesized PRM data leads to quality degradation; policy\\n      model generates \\\"answer-correct but reasoning-flawed\\\" responses, causing\\n      process reward / outcome misalignment. Directly parallels ISR problem:\\n      structurally correct but semantically wrong proof traces get high ISR\\n      but low execution reward.\\n    key_finding: >\\n      PRM performance depends critically on data quality; MC estimation\\n      introduces systematic bias. Answer-correct reasoning-flawed samples\\n      corrupt process supervision signal.\\n\\n  # ============================================================\\n  # Category 3: Mutation testing in software engineering\\n  # ============================================================\\n\\n  - id: demillo1978\\n    title: \\\"Hints on Test Data Selection: Help for the Practicing Programmer\\\"\\n    authors: \\\"Richard A. DeMillo, Richard J. Lipton, Frederick G. Sayward\\\"\\n    year: 1978\\n    venue: \\\"Computer 11(4):34-43\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Foundational paper introducing mutation testing. STA's component\\n      necessity testing directly extends this idea: instead of mutating\\n      source code to test test suites, STA mutates logical formulas\\n      to test component necessity for solver success.\\n    key_finding: >\\n      Introduced mutation testing and the coupling effect hypothesis:\\n      tests that detect simple faults also detect complex faults.\\n\\n  - id: offutt-coupling\\n    title: \\\"Investigations of the Software Testing Coupling Effect\\\"\\n    authors: \\\"A. Jefferson Offutt\\\"\\n    year: 1992\\n    venue: \\\"ACM TOSEM 1(1):5-20\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Empirically validates the coupling effect hypothesis that underpins\\n      mutation testing. STA's single-component ablation is analogous to\\n      first-order mutation; the coupling effect suggests this suffices.\\n    key_finding: >\\n      Test data killing all first-order mutants killed >99% of second-\\n      and third-order mutants, validating the coupling effect.\\n\\n  - id: jia-harman-survey\\n    title: \\\"An Analysis and Survey of the Development of Mutation Testing\\\"\\n    authors: \\\"Yue Jia, Mark Harman\\\"\\n    year: 2011\\n    venue: \\\"IEEE TSE 37(5):649-678\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Comprehensive survey of mutation testing covering three decades of\\n      development. Provides theoretical and practical foundation for STA's\\n      adaptation of mutation testing to logical formulas.\\n    key_finding: >\\n      Systematic classification of mutation operators, cost reduction\\n      techniques, and equivalence problem -- all relevant to STA's design\\n      of clause-level ablation operators.\\n\\n  - id: just-mutants-real-faults\\n    title: \\\"Are Mutants a Valid Substitute for Real Faults in Software Testing?\\\"\\n    authors: \\\"Rene Just, Darioush Jalali, Laura Inozemtseva, et al.\\\"\\n    year: 2014\\n    venue: \\\"FSE 2014\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Validates that mutation testing (structural/intensional analysis of\\n      program adequacy) correlates with real fault detection. Supports STA's\\n      premise that structural analysis of formalization components provides\\n      meaningful signal about formalization quality.\\n    key_finding: >\\n      Mutant detection is statistically correlated with real fault detection,\\n      and mutation score is a better predictor of test effectiveness than\\n      code coverage.\\n\\n  - id: llmorpheus\\n    title: \\\"LLMorpheus: Mutation Testing Using Large Language Models\\\"\\n    authors: \\\"Frank Tip, Jon Bell, et al.\\\"\\n    year: 2025\\n    venue: \\\"IEEE TSE 2025\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Uses LLMs to generate realistic code mutants beyond traditional\\n      mutation operators. Shows mutation testing evolving toward\\n      ML-integrated approaches, validating STA's cross-pollination\\n      of mutation testing ideas into ML training.\\n    key_finding: >\\n      LLM-generated mutants simulate real bugs that rule-based operators\\n      cannot produce, improving mutation testing realism.\\n\\n  - id: mutation-guided-meta\\n    title: \\\"Mutation-Guided LLM-based Test Generation at Meta\\\"\\n    authors: \\\"Christopher Foster et al.\\\"\\n    year: 2025\\n    venue: \\\"FSE 2025\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Industrial application of mutation-guided LLM test generation at\\n      Meta. Demonstrates that mutation analysis can guide LLM behavior\\n      in production -- analogous to how STA uses mutation (ablation) to\\n      guide GRPO reward signal.\\n    key_finding: >\\n      Mutation-guided approach generates tests that kill significantly\\n      more mutants than unguided LLM test generation at Meta scale.\\n\\n  - id: mutation-consistency-llm\\n    title: \\\"Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs\\\"\\n    authors: \\\"Various\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2401.05940\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Uses code mutations to evaluate LLM code understanding consistency.\\n      Conceptually related to STA: both use systematic code/formula\\n      mutations to assess model capabilities.\\n    key_finding: >\\n      LLMs show significant inconsistency when evaluated on mutated code\\n      variants, suggesting superficial pattern matching.\\n\\n  # ============================================================\\n  # Category 4: Intensional program analysis\\n  # ============================================================\\n\\n  - id: deepmutation\\n    title: \\\"A Probabilistic Framework for Mutation Testing in Deep Neural Networks\\\"\\n    authors: \\\"Various\\\"\\n    year: 2023\\n    venue: \\\"Information and Software Technology 2023\\\"\\n    category: intensional-analysis\\n    role: background\\n    relevance: >\\n      Extends mutation testing to DNN testing with probabilistic mutation\\n      operators. Parallel to STA's extension of mutation testing from\\n      traditional programs to logical formulas.\\n    key_finding: >\\n      Probabilistic mutation framework enables meaningful test adequacy\\n      assessment for neural networks through structural perturbation.\\n\\n  # ============================================================\\n  # Category 5: Reward hacking / overoptimization\\n  # ============================================================\\n\\n  - id: inform-reward-hacking\\n    title: \\\"InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling\\\"\\n    authors: \\\"Various\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS 2024\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Proposes information-bottleneck approach to detect and mitigate reward\\n      hacking. STA's ISR addresses the same problem differently: by grounding\\n      reward in verifiable structural properties (component necessity), it\\n      reduces the attack surface for reward hacking.\\n    key_finding: >\\n      Variational information bottleneck filters irrelevant features from\\n      reward model; Cluster Separation Index detects reward overoptimization.\\n\\n  - id: mo-grpo\\n    title: \\\"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\\\"\\n    authors: \\\"CyberAgent AI Lab\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2509.22047\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Directly addresses GRPO reward hacking in multi-objective settings.\\n      STA's ISR can be viewed as adding a structural objective to the\\n      correctness objective, making MO-GRPO's insights directly applicable.\\n    key_finding: >\\n      Standard GRPO normalizes after summing rewards, allowing high-variance\\n      objectives to dominate. MO-GRPO equalizes scales before aggregation.\\n\\n  - id: reward-hacking-survey\\n    title: \\\"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\\\"\\n    authors: \\\"Various\\\"\\n    year: 2026\\n    venue: \\\"arXiv 2604.13602\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Comprehensive survey of reward hacking mechanisms in the LLM era.\\n      Provides theoretical framework for understanding why STA's structural\\n      reward is more robust than pure outcome-based reward.\\n    key_finding: >\\n      Reward hacking manifests through specification gaming, reward model\\n      exploitation, and emergent misalignment; structural verification\\n      rewards are more robust than learned reward models.\\n\\n  - id: energy-loss-reward-hacking\\n    title: \\\"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"ICML 2025\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Identifies energy loss in LLM final layer as an indicator of reward\\n      hacking during RL. Provides complementary diagnostic to STA's\\n      structural reward approach.\\n    key_finding: >\\n      Energy loss in the final layer increases during RL and excessive\\n      increase characterizes reward hacking; EPPO algorithm penalizes\\n      this to mitigate hacking.\\n\\n  - id: spurious-rewards\\n    title: \\\"Spurious Rewards: Rethinking Training Signals in RLVR\\\"\\n    authors: \\\"Ruixin Yang et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2506.10947 / NeurIPS 2025 submission\\\"\\n    category: reward-hacking\\n    role: direct-evidence\\n    relevance: >\\n      Most directly relevant to STA findings. GRPO+random reward on\\n      Qwen2.5-Math improves 21.4%, nearly matching ground-truth reward's\\n      29.1%. Matches our plan017 finding: additive random (PR=48%) >\\n      additive ISR (PR=18%). Structured metrics can be worse than random\\n      noise due to systematic bias vs pure variance.\\n    key_finding: >\\n      Random reward nearly matches ground-truth reward in GRPO training,\\n      suggesting GRPO's group normalization extracts signal from noise.\\n      Effect is model-dependent (works on Qwen2.5, not Llama3).\\n\\n  - id: gao-reward-overoptimization\\n    title: \\\"Scaling Laws for Reward Model Overoptimization\\\"\\n    authors: \\\"Leo Gao, John Schulman, Jacob Hilton\\\"\\n    year: 2023\\n    venue: \\\"ICML 2023 (arXiv 2210.10760)\\\"\\n    category: reward-hacking\\n    role: theoretical-foundation\\n    relevance: >\\n      Foundational work quantifying Goodhart's effect: proxy reward rises\\n      but gold reward first rises then falls. ISR is a proxy reward that\\n      exhibits exactly this pattern — ISR can increase while prove_rate\\n      decreases, making it suitable for post-hoc diagnosis but harmful\\n      as training signal.\\n    key_finding: >\\n      Gold/proxy reward divergence follows predictable scaling laws.\\n      Proxy reward optimization past critical point degrades gold reward,\\n      with the divergence point scaling with model and dataset size.\\n\\n  - id: karwowski-goodhart-rl\\n    title: \\\"Goodhart's Law in Reinforcement Learning\\\"\\n    authors: \\\"Jacek Karwowski, Oliver Hayman, Xingjian Bai, Klaus Kiendlhofer, Charlie Griffin, Joar Skalse\\\"\\n    year: 2024\\n    venue: \\\"ICLR 2024 (arXiv 2310.09144)\\\"\\n    category: reward-hacking\\n    role: theoretical-foundation\\n    relevance: >\\n      Geometric interpretation of Goodhart's Law in MDPs: optimizing\\n      imperfect proxy past critical point decreases true objective. ISR as\\n      proxy has partial correlation with execution correctness — exceeding\\n      critical optimization point pushes policy toward high-ISR but\\n      low-correctness regions. Explains plan002/plan005 negative results.\\n    key_finding: >\\n      Formalizes Goodhart's Law for RL: any non-trivially correlated proxy\\n      reward creates regions where proxy and true reward diverge, and\\n      policy optimization inevitably enters these regions.\\n\\n  # ============================================================\\n  # Category 6: FOL/Prolog formalization with LLMs\\n  # ============================================================\\n\\n  - id: folio\\n    title: \\\"FOLIO: Natural Language Reasoning with First-Order Logic\\\"\\n    authors: \\\"Simeng Han et al.\\\"\\n    year: 2022\\n    venue: \\\"arXiv 2209.00840 / EMNLP 2024\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Primary FOL reasoning benchmark. STA uses FOLIO-style NL->FOL\\n      formalization as the target task for GRPO training. FOLIO's\\n      expert-annotated FOL annotations serve as reference formalizations.\\n    key_finding: >\\n      1,430 NL-FOL paired examples with reasoning depths up to 5+;\\n      GPT-4 still struggles on the hardest examples.\\n\\n  - id: proofwriter\\n    title: \\\"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language\\\"\\n    authors: \\\"Oyvind Tafjord, Bhavana Dalvi, Peter Clark\\\"\\n    year: 2021\\n    venue: \\\"Findings of ACL-IJCNLP 2021\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Source dataset for STA's training data. ProofWriter provides\\n      rule-based logical reasoning problems in natural language that\\n      STA uses for training formalizer models.\\n    key_finding: >\\n      Generative model can reliably produce implications and proofs;\\n      accuracy exceeds prior methods by 9% and generalizes to unseen\\n      proof depths.\\n\\n  - id: logic-lm\\n    title: \\\"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\\\"\\n    authors: \\\"Liangming Pan, Alon Albalak, Xinyi Wang, William Wang\\\"\\n    year: 2023\\n    venue: \\\"Findings of EMNLP 2023\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      LLM->symbolic solver pipeline for logical reasoning, directly\\n      comparable to STA's formalizer->Prolog solver pipeline. Key\\n      difference: Logic-LM uses prompting, STA uses GRPO training.\\n    key_finding: >\\n      LLM+solver achieves 39.2% improvement over LLM-alone on logical\\n      reasoning benchmarks including ProofWriter and FOLIO.\\n\\n  - id: linc\\n    title: \\\"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers\\\"\\n    authors: \\\"Theo X. Olausson, Alex Gu, Ben Lipkin, et al.\\\"\\n    year: 2023\\n    venue: \\\"EMNLP 2023\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      Neurosymbolic approach where LLM translates NL to FOL for theorem\\n      prover. Directly comparable to STA's NL->Prolog translation.\\n      LINC uses prompting-based approach; STA uses RL training.\\n    key_finding: >\\n      StarCoder+ (15.5B) with LINC outperforms GPT-3.5 and GPT-4 with\\n      CoT by 38% and 10% respectively on ProofWriter.\\n\\n  - id: fover-pei2025\\n    title: \\\"FoVer: First-Order Logic Verification for Natural Language Reasoning\\\"\\n    authors: \\\"Yu Pei, Yongping Du, Xingnan Jin\\\"\\n    year: 2025\\n    venue: \\\"TACL 13:1340-1359\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      Uses LLM->FOL->Z3 pipeline for verifying NL reasoning correctness.\\n      Similar to STA's verification pipeline but focuses on post-hoc\\n      verification rather than training reward signal.\\n    key_finding: >\\n      FOL verification via Z3 significantly outperforms existing methods\\n      on ProofWriter and FOLIO benchmarks.\\n\\n  - id: lorp\\n    title: \\\"LoRP: LLM-based Logical Reasoning via Prolog\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"Knowledge-Based Systems 2025\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      LLM->Prolog pipeline with FOL-to-Prolog translation mechanism.\\n      Closest to STA's formalization target (Prolog), though LoRP\\n      uses prompting while STA uses GRPO training with structural reward.\\n    key_finding: >\\n      Systematic FOL-to-Prolog translation extends Prolog expressiveness;\\n      achieves SoTA accuracy on logical reasoning with three-vote majority.\\n\\n  - id: nl2fol\\n    title: \\\"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection\\\"\\n    authors: \\\"Lalwani, Kim, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2405.02318\\\"\\n    category: fol-formalization\\n    role: background\\n    relevance: >\\n      Step-by-step NL->FOL translation using LLMs with SMT solver\\n      verification. Demonstrates the NL->formal logic pipeline that\\n      STA aims to improve via RL training.\\n    key_finding: >\\n      Neurosymbolic NL2FOL achieves 78% F1 on LOGIC dataset and\\n      generalizes to LogicClimate (80% F1), outperforming supervised\\n      models by 21%.\\n\\n  - id: logica2\\n    title: \\\"LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: \\\"IEEE/ACM TASLP 2023\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Logical reasoning evaluation benchmark derived from Chinese civil\\n      service exams. Provides supplementary evaluation for STA's\\n      formalization capabilities.\\n    key_finding: >\\n      8,678 multiple-choice questions covering categorical, disjunctive,\\n      and conditional reasoning; widely used LLM benchmark.\\n\\n  # ============================================================\\n  # Category 7: Goodhart's Law theory and dose-response dynamics\\n  # ============================================================\\n\\n  - id: manheim-goodhart-taxonomy\\n    title: \\\"Categorizing Variants of Goodhart's Law\\\"\\n    authors: \\\"David Manheim, Scott Garrabrant\\\"\\n    year: 2019\\n    venue: \\\"arXiv 1803.04585\\\"\\n    category: goodhart-overoptimization\\n    role: theoretical-foundation\\n    relevance: >\\n      Four-part Goodhart taxonomy: regressional, extremal, causal, adversarial.\\n      STA's high-β ISR collapse is best classified as extremal Goodhart\\n      (policy moves to OOD region where ISR↑ but prove_rate↓). Provides\\n      vocabulary for discussion section.\\n    key_finding: >\\n      First systematic categorization of Goodhart failure modes. Extremal\\n      variant occurs when proxy-goal relationship breaks in out-of-distribution\\n      regions reached by strong optimization.\\n\\n  - id: pan-reward-misspecification\\n    title: \\\"The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models\\\"\\n    authors: \\\"Alexander Pan, Kush Bhatia, Jacob Steinhardt\\\"\\n    year: 2022\\n    venue: \\\"ICLR 2022\\\"\\n    category: goodhart-overoptimization\\n    role: theoretical-foundation\\n    relevance: >\\n      Across 9 environments, more capable agents exploit misspecifications more.\\n      Observes dose-dependent degradation — capability thresholds where true\\n      reward sharply drops. Matches STA's β=0.1→0.3 qualitative shift.\\n    key_finding: >\\n      Reward misspecification causes dose-dependent degradation where true reward\\n      sharply drops past capability thresholds. More capable optimization\\n      produces worse outcomes under misspecification.\\n\\n  - id: kwa-catastrophic-goodhart\\n    title: \\\"Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification\\\"\\n    authors: \\\"Tat-Thang Kwa, Rachel Thomas, Adrià Garriga-Alonso\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS 2024\\\"\\n    category: goodhart-overoptimization\\n    role: theoretical-foundation\\n    relevance: >\\n      If reward model error is heavy-tailed, policies achieve arbitrarily\\n      high proxy reward with no true utility gain. KL regularization provably\\n      fails. Explains why KL penalty in GRPO cannot prevent ISR collapse\\n      at high β if ISR error distribution is heavy-tailed.\\n    key_finding: >\\n      KL-regularized RL provably fails to prevent overoptimization under\\n      heavy-tailed reward misspecification. Policies can achieve arbitrarily\\n      high proxy reward with zero true utility.\\n\\n  - id: rafailov-daa-scaling\\n    title: \\\"Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms\\\"\\n    authors: \\\"Rafael Rafailov, Yaswanth Chittepu, Ryan Park, Harshit Sikchi, Joey Hejna, W. Bradley Knox, Chelsea Finn, Scott Niekum\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS 2024\\\"\\n    category: goodhart-overoptimization\\n    role: supporting-evidence\\n    relevance: >\\n      Extends Gao et al. to DPO/IPO/SLiC. Tests seven β values across\\n      1B-6.9B models. DAAs still overoptimize despite no explicit proxy RM.\\n      Validates β as a \\\"dose\\\" parameter — directly analogous to STA's\\n      ISR weight sweep.\\n    key_finding: >\\n      Direct alignment algorithms exhibit overoptimization following\\n      predictable scaling laws. Smaller models overoptimize sooner.\\n      β-controlled dose-response is a general phenomenon across RL paradigms.\\n\\n  - id: huang-chi-squared\\n    title: \\\"Correcting the Mythos of KL-Regularization: Direct and Contrastive Distribution Correction\\\"\\n    authors: \\\"Afra Feyza Akyürek, Banghua Zhu, Sham Kakade, Jiantao Jiao\\\"\\n    year: 2025\\n    venue: \\\"ICLR 2025 Poster\\\"\\n    category: goodhart-overoptimization\\n    role: supporting-evidence\\n    relevance: >\\n      KL-regularization is theoretically inadequate for preventing\\n      overoptimization. Chi-squared divergence provably alleviates it.\\n      Suggests that even with KL penalty in GRPO, STA's high-β collapse\\n      is theoretically expected.\\n    key_finding: >\\n      Chi-squared preference optimization provably mitigates overoptimization\\n      where KL-regularization fails. Alternative divergence measures offer\\n      stronger guarantees.\\n\\n  - id: coste-rm-ensembles\\n    title: \\\"Reward Model Ensembles Help Mitigate Overoptimization\\\"\\n    authors: \\\"Thomas Coste, Usman Anwar, Robert Kirk, David Krueger\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023 Workshop on Alignment\\\"\\n    category: goodhart-overoptimization\\n    role: background\\n    relevance: >\\n      Worst-case optimization across RM ensembles practically eliminates\\n      overoptimization for BoN and reduces it for PPO. Suggests ensemble\\n      of multiple solver metrics (instead of single ISR) as mitigation.\\n    key_finding: >\\n      RM ensembles with worst-case aggregation mitigate overoptimization.\\n      Ensemble size and diversity directly affect robustness.\\n\\n  # ============================================================\\n  # Category 8: Solver/prover as RL reward signal\\n  # ============================================================\\n\\n  - id: rlsf\\n    title: \\\"Reinforcement Learning via Symbolic Feedback\\\"\\n    authors: \\\"Abhinav Jha, Shikhar Murty, Zico Kolter, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2405.16661\\\"\\n    category: verification-reward\\n    role: direct-competitor\\n    relevance: >\\n      Most directly relevant: uses solver/prover certificates as fine-grained\\n      token-level reward signal. Outperforms traditional approaches on program\\n      synthesis (+31.4%). STA extends this paradigm and shows when it breaks\\n      (Goodhart effects at high auxiliary reward weight).\\n    key_finding: >\\n      Symbolic reasoning tools provide poly-sized certificates as reward.\\n      Smaller RLSF models outperform GPT-4 on structured generation tasks.\\n\\n  - id: fover-kamoi2026\\n    title: \\\"FoVer: Generalizable Process Reward Models via Formally Verified Training Data\\\"\\n    authors: \\\"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\\\"\\n    year: 2025\\n    venue: \\\"Findings of ACL 2026 (arXiv 2502.01345)\\\"\\n    category: verification-reward\\n    role: supporting-evidence\\n    relevance: >\\n      Uses Z3 and Isabelle to synthesize PRM training data by annotating\\n      step-level error labels without human annotation. Same solver family\\n      as STA. Shows verification-based rewards work; STA extends by showing\\n      dose-response dynamics.\\n    key_finding: >\\n      Formally verified training data enables generalizable process reward\\n      models competitive on ProcessBench and 12 reasoning benchmarks.\\n\\n  - id: deepseek-prover-v15\\n    title: \\\"DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search\\\"\\n    authors: \\\"DeepSeek AI\\\"\\n    year: 2024\\n    venue: \\\"ICLR 2025 (arXiv 2408.08152)\\\"\\n    category: verification-reward\\n    role: method-component\\n    relevance: >\\n      Uses GRPO with Lean 4 verification as binary reward. Same algorithm\\n      (GRPO) + formal verification, but binary (pass/fail). Binary reward\\n      avoids the graded-metric Goodhart risk that STA identifies with ISR.\\n    key_finding: >\\n      GRPO + binary Lean verification achieves 63.5% on miniF2F. Binary\\n      correctness guarantee via formal verification sidesteps proxy reward\\n      overoptimization.\\n\\n  - id: alphaproof\\n    title: \\\"AlphaProof\\\"\\n    authors: \\\"Google DeepMind\\\"\\n    year: 2024\\n    venue: \\\"Nature 2025\\\"\\n    category: verification-reward\\n    role: background\\n    relevance: >\\n      AlphaZero-inspired RL with Lean proof verification at scale.\\n      Silver medal at IMO 2024. Binary verification reward avoids the\\n      Goodhart problem STA identifies with graded verification metrics.\\n    key_finding: >\\n      Binary formal verification as RL reward scales to IMO-level\\n      mathematical reasoning. Demonstrates verification-reward RL works\\n      at the frontier of mathematical difficulty.\\n\\n  - id: math-shepherd\\n    title: \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\"\\n    authors: \\\"Peiyi Wang, Lei Li, Zhihong Shao, R.X. Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"ACL 2024 (arXiv 2312.08935)\\\"\\n    category: verification-reward\\n    role: supporting-evidence\\n    relevance: >\\n      Automatically constructs process supervision data and uses it as\\n      step-by-step PPO reward. Automated verification reward without human\\n      labels, analogous to STA's automated ISR computation via solver.\\n    key_finding: >\\n      Automated process supervision improves Mistral-7B on GSM8K\\n      (77.9→84.1%) and MATH (28.6→33.0%) without human annotation.\\n\\n  # ============================================================\\n  # Additional reward-shaping papers (Goodhart survey additions)\\n  # ============================================================\\n\\n  - id: bipars\\n    title: \\\"Learning to Utilize Shaping Rewards: A New Approach of Reward Shaping\\\"\\n    authors: \\\"Yujing Hu, Weixun Wang, Hangtian Jia, et al.\\\"\\n    year: 2020\\n    venue: \\\"NeurIPS 2020\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Bi-level optimization learns parameterized shaping reward weights.\\n      Can transform harmful shaping rewards into beneficial ones by learning\\n      negative weights. Directly addresses STA's problem: when ISR weight\\n      is wrong, automated weight learning could find optimal β.\\n    key_finding: >\\n      Bi-level optimization automatically learns auxiliary reward weights,\\n      outperforming fixed weights and recovering from harmful shaping rewards.\\n\\n  - id: dapo\\n    title: \\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\"\\n    authors: \\\"Qiying Yu et al. (ByteDance)\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2503.14476\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Four techniques for stable multi-component reward in GRPO: Clip-Higher,\\n      Dynamic Sampling, token-level policy gradient, Overlong Reward Shaping.\\n      Addresses stability issues relevant to STA's multi-reward setup.\\n    key_finding: >\\n      Clip-Higher and Dynamic Sampling prevent entropy collapse in GRPO\\n      with multi-component rewards. Soft punishment for overlong outputs\\n      avoids reward hacking through length exploitation.\\n\", \"total_chars\": 38485, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
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
Now I have the full literature map. Let me analyze coverage for each of the three areas:

## (a) Prolog/Logic Programming + GRPO/RL
Looking at the map, I can see:
- `mellgren-prolog-grpo`: "Training Language Models to Use Prolog as a Tool" - GRPO + Prolog, directly relevant
- `logic-rl`: Logic-RL using REINFORCE++ for logical reasoning
- `satlm`: Neurosymbolic with SAT solver
- `linc`: Neurosymbolic with FOL provers


- `lorp`: LLM->Prolog pipeline
- `logic-lm`: LLM->symbolic solver

There's decent coverage of Prolog and RL approaches, though the direct Prolog+GRPO intersection is limited to just the mellgren paper. I should look for additional work in the neuro-symbolic Prolog and logic programming reinforcement learning space.

## (b) Goodhart's Law latest work (2019+)
Looking at category 7 (goodhart-overoptimization), I have `manheim-goodhart-taxonomy` from 2019 as a core reference, and I'm checking what else is available in this area.

The recent papers on reward misspecification and Goodhart effects are well represented across major venues—ICLR, NeurIPS, and ICML from 2022 onwards—with coverage spanning both the overoptimization angle and reward hacking variants. This looks fairly comprehensive.

Now I'm checking the mutation testing section to see if there are any critical gaps, particularly around specification gaming papers that might bridge these areas.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "d43e9996-d494-4a28-8e49-75981010739a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SSS6tADvTxwQJP6X1y3hRG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12522,
      "cache_read_input_tokens": 26064,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12522
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

Current map loaded (38k chars, 45 papers). Let me assess coverage and search for gaps.

**Initial assessment:**
- **(a) Prolog/LP + RL**: Has `mellgren-prolog-grpo` and `logic-rl`, but missing broader neuro-symbolic LP literature (DeepProbLog, NeurASP, etc.)
- **(b) Goodhart 2020+**: Already strong — has Gao 2023, Skalse 2022, Karwowski 2024, Kwa 2024. May be missing specification gaming papers.
- **(c) Mutation testing**: Well covered — DeMillo 1978, Jia & Harman 2011, Offutt 1992 all present. 7 papers total.

Searching for gaps in all three areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "f84d639b-9bfd-4a0e-a727-6bec92826cbd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SSS6tADvTxwQJP6X1y3hRG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12522,
      "cache_read_input_tokens": 26064,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12522
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R8dYKJtT2HFF5EnBJak8V9`</summary>

```json
{
  "query": "neuro-symbolic Prolog LLM reinforcement learning 2023 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "b9a3cc84-e178-4404-abec-1b800035a8b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SSS6tADvTxwQJP6X1y3hRG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12522,
      "cache_read_input_tokens": 26064,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12522
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HVsYpREe9PmVUa7uyF923T`</summary>

```json
{
  "query": "DeepProbLog NeurASP neural logic programming reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "4015d42f-9778-445e-af5c-c0d1a46d5df9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SSS6tADvTxwQJP6X1y3hRG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12522,
      "cache_read_input_tokens": 26064,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12522
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KmSZNjM8rXLEDEwssv8KWd`</summary>

```json
{
  "query": "\"specification gaming\" reinforcement learning 2023 2024 2025 survey"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "b6136491-9b11-498c-b6c3-5f29057157f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SSS6tADvTxwQJP6X1y3hRG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12522,
      "cache_read_input_tokens": 26064,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12522
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E39eziiFm4ja55Z1qZr7Dt`</summary>

```json
{
  "query": "\"reward overoptimization\" \"Goodhart\" reinforcement learning LLM 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "25defa6a-eb57-4fe4-aeb9-aac1038ceeae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SSS6tADvTxwQJP6X1y3hRG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12522,
      "cache_read_input_tokens": 26064,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12522
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

_source line 16 · 2026-05-14T17:43:27.584Z_

<details><summary>↩ Tool result · `toolu_01HVsYpREe9PmVUa7uyF923T`</summary>

```text
Web search results for query: "DeepProbLog NeurASP neural logic programming reinforcement learning"

Links: [{"title":"(PDF) Neural probabilistic logic programming in DeepProbLog","url":"https://www.researchgate.net/publication/350911019_Neural_probabilistic_logic_programming_in_DeepProbLog"},{"title":"GitHub - ML-KULeuven/deepproblog: DeepProbLog is an extension of ProbLog that integrates Probabilistic Logic Programming with deep learning by introducing the neural predicate. · GitHub","url":"https://github.com/ML-KULeuven/deepproblog"},{"title":"[1805.10872] DeepProbLog: Neural Probabilistic Logic Programming","url":"https://arxiv.org/abs/1805.10872"},{"title":"Approximate Inference for Neural Probabilistic Logic Programming","url":"https://proceedings.kr.org/2021/45/kr2021-0045-manhaeve-et-al.pdf"},{"title":"Neural probabilistic logic programming in DeepProbLog - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0004370221000552"},{"title":"Reviews: DeepProbLog: Neural Probabilistic Logic Programming","url":"https://proceedings.neurips.cc/paper/2018/file/dc5d637ed5e62c36ecb73b654b05ba2a-Reviews.html"},{"title":"Neural Probabilistic Logic Programming in DeepProbLog - ADS","url":"https://ui.adsabs.harvard.edu/abs/2019arXiv190708194M/abstract"},{"title":"DeepProbLog: Neural Probabilistic Logic Programming","url":"https://papers.nips.cc/paper/7632-deepproblog-neural-probabilistic-logic-programming"},{"title":"(PDF) DeepProbLog: Neural Probabilistic Logic Programming","url":"https://www.researchgate.net/publication/334602669_DeepProbLog_Neural_Probabilistic_Logic_Programming"},{"title":"DeepProbLog: neural probabilistic logic programming - -ORCA","url":"https://orca.cardiff.ac.uk/id/eprint/116510/"}]

Based on the search results, here's what I found about DeepProbLog, NeurASP, and neural logic programming:

## DeepProbLog

DeepProbLog is an extension of ProbLog that integrates Probabilistic Logic Programming with deep learning by introducing the neural predicate. More specifically, the neural predicate represents probabilistic facts whose probabilities are parameterized by neural networks.

DeepProbLog supports (i) both symbolic and subsymbolic representations and inference, (ii) program induction, (iii) probabilistic (logic) programming, and (iv) (deep) learning from examples. To the best of the developers' knowledge, this work is the first to propose a framework where general-purpose neural networks and expressive probabilistic-logical modeling and reasoning are integrated in a way that exploits the full expressiveness and strengths of both worlds and can be trained end-to-end based on examples.

## NeurASP

The search results mention NeurASP in comparison with DeepProbLog. NeurASP is slightly faster than DeepProbLog. However, approximate inference with DeepProbLog can answer queries several orders of magnitude faster than exact methods.

## Applications

DeepProbLog is applied to problems combining logical and perceptual reasoning such as computing the addition of two numbers given as images, inducing programs and probabilistic programming problems.

The search results did not specifically address reinforcement learning applications for these frameworks, though the document on approximate inference in neural probabilistic logic programming may contain additional technical details available through direct access to the papers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "62280893-60f0-4aa4-ac21-1416ae8bdac7",
  "tool_use_result": {
    "query": "DeepProbLog NeurASP neural logic programming reinforcement learning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SYosUDHToPyoSNmKMAX9pC",
        "content": [
          {
            "title": "(PDF) Neural probabilistic logic programming in DeepProbLog",
            "url": "https://www.researchgate.net/publication/350911019_Neural_probabilistic_logic_programming_in_DeepProbLog"
          },
          {
            "title": "GitHub - ML-KULeuven/deepproblog: DeepProbLog is an extension of ProbLog that integrates Probabilistic Logic Programming with deep learning by introducing the neural predicate. · GitHub",
            "url": "https://github.com/ML-KULeuven/deepproblog"
          },
          {
            "title": "[1805.10872] DeepProbLog: Neural Probabilistic Logic Programming",
            "url": "https://arxiv.org/abs/1805.10872"
          },
          {
            "title": "Approximate Inference for Neural Probabilistic Logic Programming",
            "url": "https://proceedings.kr.org/2021/45/kr2021-0045-manhaeve-et-al.pdf"
          },
          {
            "title": "Neural probabilistic logic programming in DeepProbLog - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S0004370221000552"
          },
          {
            "title": "Reviews: DeepProbLog: Neural Probabilistic Logic Programming",
            "url": "https://proceedings.neurips.cc/paper/2018/file/dc5d637ed5e62c36ecb73b654b05ba2a-Reviews.html"
          },
          {
            "title": "Neural Probabilistic Logic Programming in DeepProbLog - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2019arXiv190708194M/abstract"
          },
          {
            "title": "DeepProbLog: Neural Probabilistic Logic Programming",
            "url": "https://papers.nips.cc/paper/7632-deepproblog-neural-probabilistic-logic-programming"
          },
          {
            "title": "(PDF) DeepProbLog: Neural Probabilistic Logic Programming",
            "url": "https://www.researchgate.net/publication/334602669_DeepProbLog_Neural_Probabilistic_Logic_Programming"
          },
          {
            "title": "DeepProbLog: neural probabilistic logic programming - -ORCA",
            "url": "https://orca.cardiff.ac.uk/id/eprint/116510/"
          }
        ]
      },
      "Based on the search results, here's what I found about DeepProbLog, NeurASP, and neural logic programming:\n\n## DeepProbLog\n\nDeepProbLog is an extension of ProbLog that integrates Probabilistic Logic Programming with deep learning by introducing the neural predicate. More specifically, the neural predicate represents probabilistic facts whose probabilities are parameterized by neural networks.\n\nDeepProbLog supports (i) both symbolic and subsymbolic representations and inference, (ii) program induction, (iii) probabilistic (logic) programming, and (iv) (deep) learning from examples. To the best of the developers' knowledge, this work is the first to propose a framework where general-purpose neural networks and expressive probabilistic-logical modeling and reasoning are integrated in a way that exploits the full expressiveness and strengths of both worlds and can be trained end-to-end based on examples.\n\n## NeurASP\n\nThe search results mention NeurASP in comparison with DeepProbLog. NeurASP is slightly faster than DeepProbLog. However, approximate inference with DeepProbLog can answer queries several orders of magnitude faster than exact methods.\n\n## Applications\n\nDeepProbLog is applied to problems combining logical and perceptual reasoning such as computing the addition of two numbers given as images, inducing programs and probabilistic programming problems.\n\nThe search results did not specifically address reinforcement learning applications for these frameworks, though the document on approximate inference in neural probabilistic logic programming may contain additional technical details available through direct access to the papers."
    ],
    "durationSeconds": 6.604272270000001
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T17:43:28.576Z_

<details><summary>↩ Tool result · `toolu_01KmSZNjM8rXLEDEwssv8KWd`</summary>

```text
Web search results for query: ""specification gaming" reinforcement learning 2023 2024 2025 survey"

Links: [{"title":"Think in Games: Learning to Reason in Games via Reinforcement Learning with Large Language Models","url":"https://arxiv.org/html/2508.21365v1"},{"title":"The State of Reinforcement Learning in 2025 - DataRoot Labs","url":"https://datarootlabs.com/blog/state-of-reinforcement-learning-2025"},{"title":"Statistical Reinforcement Learning in the Real World: A Survey of Challenges and Future Directions","url":"https://arxiv.org/html/2601.15353"},{"title":"A Survey of Safe Reinforcement Learning and Constrained MDPs: A Technical Survey on Single-Agent and Multi-Agent Safety","url":"https://arxiv.org/html/2505.17342v1"},{"title":"Reinforcement Learning in Game Industry—Review, Prospects and Challenges","url":"https://www.mdpi.com/2076-3417/13/4/2443"},{"title":"A Survey on recent advances in reinforcement learning for intelligent investment decision-making optimization - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0957417425011625"},{"title":"Game Theory Meets Large Language Models: A Systematic Survey","url":"https://www.ijcai.org/proceedings/2025/1184.pdf"},{"title":"[2411.18892] A Comprehensive Survey of Reinforcement Learning: From Algorithms to Practical Challenges","url":"https://arxiv.org/abs/2411.18892"},{"title":"Survey on Graph-Based Reinforcement Learning for Networked Coordination and Control","url":"https://www.mdpi.com/2673-4052/6/4/65"},{"title":"Reinforcement Learning for Large Model: A Survey","url":"https://arxiv.org/html/2508.08189v3"}]

Based on the search results, I found several recent surveys on reinforcement learning from 2023-2025, though the results don't contain a dedicated survey specifically focused on "specification gaming" in reinforcement learning. However, I can share what was found:

## Relevant Surveys and Research (2023-2025)

A comprehensive survey of RL was published analyzing a wide range of algorithms, from foundational tabular methods to advanced Deep Reinforcement Learning (DRL) techniques, with the most recent version from February 2025.

Related areas to specification gaming include reward hacking/alignment, which ensures the specified reward leads to intended safe behavior. One can combine learned reward shaping with safety constraints to yield agents that both seek correct objectives and stay safe.

Model misspecification is common in sequential decision-making, particularly in complex environments where data is limited and noise is substantial, with one reason being that agents typically do not know which model class the state dynamics and/or true reward process belongs to.

## Other Recent RL Surveys

Additional recent surveys include:
- A comprehensive survey of Safe RL exists, with an emerging frontier being Multi-Agent Safe Reinforcement Learning (SafeMARL)
- A comprehensive synthesis of recent advances in visual reinforcement learning within the context of multimodal large models, with a focus on research activity since 2024

The search results don't reveal a dedicated survey specifically on specification gaming in RL, though the topic is related to reward hacking and model misspecification challenges that are discussed in recent RL literature.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "4e07e123-4a58-4bd0-9793-254a321a8d2a",
  "tool_use_result": {
    "query": "\"specification gaming\" reinforcement learning 2023 2024 2025 survey",
    "results": [
      {
        "tool_use_id": "srvtoolu_01J24yEwh1GP8MvL6HBySwph",
        "content": [
          {
            "title": "Think in Games: Learning to Reason in Games via Reinforcement Learning with Large Language Models",
            "url": "https://arxiv.org/html/2508.21365v1"
          },
          {
            "title": "The State of Reinforcement Learning in 2025 - DataRoot Labs",
            "url": "https://datarootlabs.com/blog/state-of-reinforcement-learning-2025"
          },
          {
            "title": "Statistical Reinforcement Learning in the Real World: A Survey of Challenges and Future Directions",
            "url": "https://arxiv.org/html/2601.15353"
          },
          {
            "title": "A Survey of Safe Reinforcement Learning and Constrained MDPs: A Technical Survey on Single-Agent and Multi-Agent Safety",
            "url": "https://arxiv.org/html/2505.17342v1"
          },
          {
            "title": "Reinforcement Learning in Game Industry—Review, Prospects and Challenges",
            "url": "https://www.mdpi.com/2076-3417/13/4/2443"
          },
          {
            "title": "A Survey on recent advances in reinforcement learning for intelligent investment decision-making optimization - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S0957417425011625"
          },
          {
            "title": "Game Theory Meets Large Language Models: A Systematic Survey",
            "url": "https://www.ijcai.org/proceedings/2025/1184.pdf"
          },
          {
            "title": "[2411.18892] A Comprehensive Survey of Reinforcement Learning: From Algorithms to Practical Challenges",
            "url": "https://arxiv.org/abs/2411.18892"
          },
          {
            "title": "Survey on Graph-Based Reinforcement Learning for Networked Coordination and Control",
            "url": "https://www.mdpi.com/2673-4052/6/4/65"
          },
          {
            "title": "Reinforcement Learning for Large Model: A Survey",
            "url": "https://arxiv.org/html/2508.08189v3"
          }
        ]
      },
      "Based on the search results, I found several recent surveys on reinforcement learning from 2023-2025, though the results don't contain a dedicated survey specifically focused on \"specification gaming\" in reinforcement learning. However, I can share what was found:\n\n## Relevant Surveys and Research (2023-2025)\n\nA comprehensive survey of RL was published analyzing a wide range of algorithms, from foundational tabular methods to advanced Deep Reinforcement Learning (DRL) techniques, with the most recent version from February 2025.\n\nRelated areas to specification gaming include reward hacking/alignment, which ensures the specified reward leads to intended safe behavior. One can combine learned reward shaping with safety constraints to yield agents that both seek correct objectives and stay safe.\n\nModel misspecification is common in sequential decision-making, particularly in complex environments where data is limited and noise is substantial, with one reason being that agents typically do not know which model class the state dynamics and/or true reward process belongs to.\n\n## Other Recent RL Surveys\n\nAdditional recent surveys include:\n- A comprehensive survey of Safe RL exists, with an emerging frontier being Multi-Agent Safe Reinforcement Learning (SafeMARL)\n- A comprehensive synthesis of recent advances in visual reinforcement learning within the context of multimodal large models, with a focus on research activity since 2024\n\nThe search results don't reveal a dedicated survey specifically on specification gaming in RL, though the topic is related to reward hacking and model misspecification challenges that are discussed in recent RL literature."
    ],
    "durationSeconds": 7.127126316000002
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T17:43:29.093Z_

<details><summary>↩ Tool result · `toolu_01R8dYKJtT2HFF5EnBJak8V9`</summary>

```text
Web search results for query: "neuro-symbolic Prolog LLM reinforcement learning 2023 2024 2025"

Links: [{"title":"Advancing Symbolic Integration in Large Language Models: Beyond Conventional Neurosymbolic AI","url":"https://arxiv.org/html/2510.21425v1"},{"title":"ProSLM: A Prolog Synergized Language Model for explainable Domain Specific Knowledge Based Question Answering | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-71170-1_23"},{"title":"Neuro-Symbolic AI: A Foundational Analysis of the Third Wave’s Hybrid Core | by Greg Robison | Medium","url":"https://gregrobison.medium.com/neuro-symbolic-ai-a-foundational-analysis-of-the-third-waves-hybrid-core-cc95bc69d6fa"},{"title":"Neuro-Symbolic Reasoning with Multiple Large Language Models Combined by First-Order Logic | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-08462-0_18"},{"title":"A Survey on LLM Symbolic Reasoning","url":"https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.176538331.19733376/v1"},{"title":"A Comprehensive Review of Neuro-symbolic AI for Robustness, Uncertainty Quantification, and Intervenability | Arabian Journal for Science and Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s13369-025-10887-3"},{"title":"GitHub - LAMDA-NeSy/Awesome-LLM-Reasoning-with-NeSy: ✨✨Latest Advances on Neuro-Symbolic Learning in the era of Large Language Models","url":"https://github.com/LAMDA-NeSy/Awesome-LLM-Reasoning-with-NeSy"},{"title":"Neuro-Symbolic Integration Brings Causal and Reliable ...","url":"https://aclanthology.org/2025.findings-naacl.317.pdf"},{"title":"LLM to Symbolic: Neuro-Symbolic Integration","url":"https://www.emergentmind.com/topics/llm-to-symbolic"},{"title":"On the Potential of Logic and Reasoning in Neurosymbolic Systems Using OWL-Based Knowledge Graphs - David Herron, Ernesto Jiménez-Ruiz, Tillman Weyde, 2025","url":"https://journals.sagepub.com/doi/10.1177/29498732251320043"}]

Based on the web search results, here's what I found regarding neuro-symbolic approaches combining Prolog, LLMs, and reinforcement learning from 2023-2025:

## Key Findings

### Research Trends
Publications on symbolic integration with LLMs show a sharp rise from 2019 onwards, peaking in 2023–2024. The field is experiencing significant growth in combining neural and symbolic methods.

### Prolog-Based Approaches
Neural network-based automated theorem-proving strategies employ Prolog syntax to conduct logical reasoning by embedding logic within neural networks. ProSLM: A Prolog Synergized Language Model for explainable Domain Specific Knowledge Based Question Answering represents a 2024 example of this integration.

Prolog code is highly declarative, rendering less challenges for LLMs. This makes it particularly suitable for neuro-symbolic integration with large language models.

### Reinforcement Learning Integration
Recent work includes RLSF: Reinforcement Learning via Symbolic Feedback (2025) and FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning (2024). Additionally, CoTran: An LLM-based Code Translator uses Reinforcement Learning with Feedback from Compiler and Symbolic Execution (2023).

### Core Integration Patterns
A foundational LLM → symbolic mechanism is prompted translation in which an LLM maps natural language input to a structured symbolic language (e.g., logic programming, FOL, SAT). Robust frameworks introduce self-refinement modules which use feedback from downstream symbolic solvers to iteratively correct syntactic or semantic errors in the translated logic expressions.

### Applications and Impact
Amazon reportedly applied NeSy in 2025 to its Vulcan warehouse robots and Rufus shopping assistant to enhance accuracy and decision-making.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "91b206f6-21e1-4be1-82be-16f2700f7c81",
  "tool_use_result": {
    "query": "neuro-symbolic Prolog LLM reinforcement learning 2023 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NB9V5vpwH6SCGiD3UDwmuo",
        "content": [
          {
            "title": "Advancing Symbolic Integration in Large Language Models: Beyond Conventional Neurosymbolic AI",
            "url": "https://arxiv.org/html/2510.21425v1"
          },
          {
            "title": "ProSLM: A Prolog Synergized Language Model for explainable Domain Specific Knowledge Based Question Answering | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-3-031-71170-1_23"
          },
          {
            "title": "Neuro-Symbolic AI: A Foundational Analysis of the Third Wave’s Hybrid Core | by Greg Robison | Medium",
            "url": "https://gregrobison.medium.com/neuro-symbolic-ai-a-foundational-analysis-of-the-third-waves-hybrid-core-cc95bc69d6fa"
          },
          {
            "title": "Neuro-Symbolic Reasoning with Multiple Large Language Models Combined by First-Order Logic | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-3-032-08462-0_18"
          },
          {
            "title": "A Survey on LLM Symbolic Reasoning",
            "url": "https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.176538331.19733376/v1"
          },
          {
            "title": "A Comprehensive Review of Neuro-symbolic AI for Robustness, Uncertainty Quantification, and Intervenability | Arabian Journal for Science and Engineering | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s13369-025-10887-3"
          },
          {
            "title": "GitHub - LAMDA-NeSy/Awesome-LLM-Reasoning-with-NeSy: ✨✨Latest Advances on Neuro-Symbolic Learning in the era of Large Language Models",
            "url": "https://github.com/LAMDA-NeSy/Awesome-LLM-Reasoning-with-NeSy"
          },
          {
            "title": "Neuro-Symbolic Integration Brings Causal and Reliable ...",
            "url": "https://aclanthology.org/2025.findings-naacl.317.pdf"
          },
          {
            "title": "LLM to Symbolic: Neuro-Symbolic Integration",
            "url": "https://www.emergentmind.com/topics/llm-to-symbolic"
          },
          {
            "title": "On the Potential of Logic and Reasoning in Neurosymbolic Systems Using OWL-Based Knowledge Graphs - David Herron, Ernesto Jiménez-Ruiz, Tillman Weyde, 2025",
            "url": "https://journals.sagepub.com/doi/10.1177/29498732251320043"
          }
        ]
      },
      "Based on the web search results, here's what I found regarding neuro-symbolic approaches combining Prolog, LLMs, and reinforcement learning from 2023-2025:\n\n## Key Findings\n\n### Research Trends\nPublications on symbolic integration with LLMs show a sharp rise from 2019 onwards, peaking in 2023–2024. The field is experiencing significant growth in combining neural and symbolic methods.\n\n### Prolog-Based Approaches\nNeural network-based automated theorem-proving strategies employ Prolog syntax to conduct logical reasoning by embedding logic within neural networks. ProSLM: A Prolog Synergized Language Model for explainable Domain Specific Knowledge Based Question Answering represents a 2024 example of this integration.\n\nProlog code is highly declarative, rendering less challenges for LLMs. This makes it particularly suitable for neuro-symbolic integration with large language models.\n\n### Reinforcement Learning Integration\nRecent work includes RLSF: Reinforcement Learning via Symbolic Feedback (2025) and FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning (2024). Additionally, CoTran: An LLM-based Code Translator uses Reinforcement Learning with Feedback from Compiler and Symbolic Execution (2023).\n\n### Core Integration Patterns\nA foundational LLM → symbolic mechanism is prompted translation in which an LLM maps natural language input to a structured symbolic language (e.g., logic programming, FOL, SAT). Robust frameworks introduce self-refinement modules which use feedback from downstream symbolic solvers to iteratively correct syntactic or semantic errors in the translated logic expressions.\n\n### Applications and Impact\nAmazon reportedly applied NeSy in 2025 to its Vulcan warehouse robots and Rufus shopping assistant to enhance accuracy and decision-making."
    ],
    "durationSeconds": 8.568682590999996
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T17:43:29.206Z_

<details><summary>↩ Tool result · `toolu_01E39eziiFm4ja55Z1qZr7Dt`</summary>

```text
Web search results for query: ""reward overoptimization" "Goodhart" reinforcement learning LLM 2024 2025"

Links: [{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/e45caa3d5273d105b8d045e748636957-Paper-Conference.pdf"},{"title":"NeurIPS Poster Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms","url":"https://neurips.cc/virtual/2024/poster/93540"},{"title":"Catastrophic Goodhart: regularizing RLHF with KL divergence does not mitigate heavy-tailed reward misspecification | OpenReview","url":"https://openreview.net/forum?id=UXuBzWoZGK&noteId=YiStZYdof7"},{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602v1"},{"title":"confronting reward model overoptimization","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/5eee634cb9729b8bcc2ec9f2a46a74ae-Paper-Conference.pdf"},{"title":"Goodhart's Law in Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=5o9G4XF1LI"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation","url":"https://arxiv.org/html/2602.09305v1"},{"title":"[2210.10760] Scaling Laws for Reward Model Overoptimization","url":"https://arxiv.org/abs/2210.10760"},{"title":"GitHub - JLZhong23/awesome-reward-models · GitHub","url":"https://github.com/JLZhong23/awesome-reward-models"}]

I've completed a web search for your query about reward overoptimization, Goodhart's Law, and reinforcement learning in LLMs from 2024-2025. Here are the key findings:

## Core Concept

Goodhart's Law states that "When a measure becomes a target, it ceases to be a good measure". In the context of LLM alignment, reward over-optimization occurs when performance as measured by the learned proxy reward model increases, but true model quality plateaus or even deteriorates.

## Recent Research (2024-2025)

The phenomenon was first extensively characterized by Gao et al., who coined the term "reward over-optimization". Recent work has expanded the scope significantly:

- **Direct Alignment Algorithms**: Direct Alignment Algorithms (DDAs) such as Direct Preference Optimization (DPO) have emerged as alternatives to classical RLHF, but despite not training a separate proxy reward model, they still commonly deteriorate from over-optimization.

- **Catastrophic Goodhart**: Research identifies "catastrophic Goodhart," where policies obtain arbitrarily high reward despite achieving no more utility than the base model.

- **In-Context Reward Hacking**: Studies have investigated in-context reward hacking where feedback is provided by the external world, with results showing that scaling up the model worsens this phenomenon.

## Mitigation Strategies

More reward modeling data leads to higher gold reward scores and reduces "Goodharting".

The search results also reveal numerous 2024-2025 papers addressing mitigation strategies, as shown in the recent literature on constrained RLHF, robust reward model training, and alternative evaluation methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "cce66375-3c21-4ac8-9c62-98c1163f9f08",
  "tool_use_result": {
    "query": "\"reward overoptimization\" \"Goodhart\" reinforcement learning LLM 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SAq9FgzgiqF9XUiiixSPNW",
        "content": [
          {
            "title": "Reward Hacking in Reinforcement Learning | Lil'Log",
            "url": "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"
          },
          {
            "title": "Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/e45caa3d5273d105b8d045e748636957-Paper-Conference.pdf"
          },
          {
            "title": "NeurIPS Poster Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms",
            "url": "https://neurips.cc/virtual/2024/poster/93540"
          },
          {
            "title": "Catastrophic Goodhart: regularizing RLHF with KL divergence does not mitigate heavy-tailed reward misspecification | OpenReview",
            "url": "https://openreview.net/forum?id=UXuBzWoZGK&noteId=YiStZYdof7"
          },
          {
            "title": "Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges",
            "url": "https://arxiv.org/html/2604.13602v1"
          },
          {
            "title": "confronting reward model overoptimization",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2024/file/5eee634cb9729b8bcc2ec9f2a46a74ae-Paper-Conference.pdf"
          },
          {
            "title": "Goodhart's Law in Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=5o9G4XF1LI"
          },
          {
            "title": "Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation",
            "url": "https://arxiv.org/html/2602.09305v1"
          },
          {
            "title": "[2210.10760] Scaling Laws for Reward Model Overoptimization",
            "url": "https://arxiv.org/abs/2210.10760"
          },
          {
            "title": "GitHub - JLZhong23/awesome-reward-models · GitHub",
            "url": "https://github.com/JLZhong23/awesome-reward-models"
          }
        ]
      },
      "I've completed a web search for your query about reward overoptimization, Goodhart's Law, and reinforcement learning in LLMs from 2024-2025. Here are the key findings:\n\n## Core Concept\n\nGoodhart's Law states that \"When a measure becomes a target, it ceases to be a good measure\". In the context of LLM alignment, reward over-optimization occurs when performance as measured by the learned proxy reward model increases, but true model quality plateaus or even deteriorates.\n\n## Recent Research (2024-2025)\n\nThe phenomenon was first extensively characterized by Gao et al., who coined the term \"reward over-optimization\". Recent work has expanded the scope significantly:\n\n- **Direct Alignment Algorithms**: Direct Alignment Algorithms (DDAs) such as Direct Preference Optimization (DPO) have emerged as alternatives to classical RLHF, but despite not training a separate proxy reward model, they still commonly deteriorate from over-optimization.\n\n- **Catastrophic Goodhart**: Research identifies \"catastrophic Goodhart,\" where policies obtain arbitrarily high reward despite achieving no more utility than the base model.\n\n- **In-Context Reward Hacking**: Studies have investigated in-context reward hacking where feedback is provided by the external world, with results showing that scaling up the model worsens this phenomenon.\n\n## Mitigation Strategies\n\nMore reward modeling data leads to higher gold reward scores and reduces \"Goodharting\".\n\nThe search results also reveal numerous 2024-2025 papers addressing mitigation strategies, as shown in the recent literature on constrained RLHF, robust reward model training, and alternative evaluation methods."
    ],
    "durationSeconds": 7.2652504820000035
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
Let me search more specifically for the gaps I've identified:

1. For Prolog/LP + RL: I should look for specific papers like:
   - DeepProbLog (Manhaeve et al., 2018/2021) - neural probabilistic logic programming
   - NeurASP (Yang et al., 2020) - neural answer set programming
   - Any other Prolog+RL papers

2. For Goodhart: The map already seems well-covered. Let me check for Krakovna et al. "specification gaming" list/paper.
   
3. For mutation testing: That's already well-covered, so I'll move on to more targeted searches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "3ecf7bfd-ed24-4061-85b7-250c61212e2f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GpzE1rxVGUvhRciAmnYDY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5215,
      "cache_read_input_tokens": 38586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5215
      },
      "output_tokens": 11,
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

_source line 21_

Let me search for specific missing papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "4651cef2-89d4-462c-a7d6-c79c6c5f92a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GpzE1rxVGUvhRciAmnYDY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5215,
      "cache_read_input_tokens": 38586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5215
      },
      "output_tokens": 11,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_015Lmj7Zdcs6AvcRcfX2wh9K`</summary>

```json
{
  "query": "Manhaeve DeepProbLog \"Neural Probabilistic Logic Programming\" 2021 artificial intelligence journal"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "d55beb63-09bd-459b-a30b-4fe778780ef8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GpzE1rxVGUvhRciAmnYDY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5215,
      "cache_read_input_tokens": 38586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5215
      },
      "output_tokens": 11,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Fb7vbLkBq3ZWyMsmmCRZkM`</summary>

```json
{
  "query": "NeurASP Yang Ishay \"Neural Answer Set Programming\" 2020 IJCAI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "9ef0f351-43b1-450f-ba61-004dfa5052dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GpzE1rxVGUvhRciAmnYDY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5215,
      "cache_read_input_tokens": 38586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5215
      },
      "output_tokens": 11,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Kb2vi4npeqgSSz16KHsRUz`</summary>

```json
{
  "query": "Krakovna \"specification gaming\" examples list DeepMind 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "79f4dbae-0522-411c-8b84-4a3cc2beb179",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GpzE1rxVGUvhRciAmnYDY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5215,
      "cache_read_input_tokens": 38586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5215
      },
      "output_tokens": 11,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_017KEK5AXQ3GKH3cwqZF5G9F`</summary>

```json
{
  "query": "\"logic programming\" \"reinforcement learning\" LLM GRPO 2024 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "ae3b2be4-a93d-493b-862b-b921e3d7cdc3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GpzE1rxVGUvhRciAmnYDY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5215,
      "cache_read_input_tokens": 38586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5215
      },
      "output_tokens": 11,
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

_source line 26 · 2026-05-14T17:43:41.327Z_

<details><summary>↩ Tool result · `toolu_015Lmj7Zdcs6AvcRcfX2wh9K`</summary>

```text
Web search results for query: "Manhaeve DeepProbLog "Neural Probabilistic Logic Programming" 2021 artificial intelligence journal"

Links: [{"title":"[1805.10872] DeepProbLog: Neural Probabilistic Logic Programming","url":"https://arxiv.org/abs/1805.10872"},{"title":"(PDF) Neural probabilistic logic programming in DeepProbLog","url":"https://www.researchgate.net/publication/350911019_Neural_probabilistic_logic_programming_in_DeepProbLog"},{"title":"GitHub - ML-KULeuven/deepproblog: DeepProbLog is an extension of ProbLog that integrates Probabilistic Logic Programming with deep learning by introducing the neural predicate. · GitHub","url":"https://github.com/ML-KULeuven/deepproblog"},{"title":"(Open Access) Neural probabilistic logic programming in DeepProbLog (2021) | Robin Manhaeve | 158 Citations","url":"https://scispace.com/papers/neural-probabilistic-logic-programming-in-deepproblog-x2gdjqjbs3"},{"title":"(PDF) DeepProbLog: Neural Probabilistic Logic Programming","url":"https://www.researchgate.net/publication/334602669_DeepProbLog_Neural_Probabilistic_Logic_Programming"},{"title":"Neural probabilistic logic programming in DeepProbLog - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0004370221000552"},{"title":"[PDF] DeepProbLog: Neural Probabilistic Logic Programming | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DeepProbLog:-Neural-Probabilistic-Logic-Programming-Manhaeve-Dumancic/f6e6fba61b654c5b799a9efe3b5849ce1197aab3"},{"title":"[1907.08194] Neural Probabilistic Logic Programming in DeepProbLog","url":"https://arxiv.org/abs/1907.08194"},{"title":"DeepProbLog: Neural Probabilistic Logic Programming","url":"https://ceur-ws.org/Vol-2491/abstract68.pdf"},{"title":"DeepProbLog: Neural Probabilistic Logic Programming Robin Manhaeve KU Leuven","url":"https://arxiv.org/pdf/1805.10872"}]

Based on the search results, I found information about the DeepProbLog work by Manhaeve and colleagues:

Robin Manhaeve, Sebastijan Dumancic, Angelika Kimmig, Thomas Demeester, and Luc De Raedt published "Neural Probabilistic Logic Programming in DeepProbLog" in AIJ (Artificial Intelligence Journal). The article was published in Artificial Intelligence on September 1, 2021, and is currently open access.

The work introduces DeepProbLog, a neural probabilistic logic programming language that incorporates deep learning by means of neural predicates, and shows how existing inference and learning techniques of the underlying probabilistic logic programming language ProbLog can be adapted for the new language.

DeepProbLog supports both symbolic and subsymbolic representations and inference, program induction, probabilistic (logic) programming, and (deep) learning from examples.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "a79ea65d-b970-4973-97ad-58c9e2c3c296",
  "tool_use_result": {
    "query": "Manhaeve DeepProbLog \"Neural Probabilistic Logic Programming\" 2021 artificial intelligence journal",
    "results": [
      {
        "tool_use_id": "srvtoolu_01B7k2WquvMiv8epKXw5mK9q",
        "content": [
          {
            "title": "[1805.10872] DeepProbLog: Neural Probabilistic Logic Programming",
            "url": "https://arxiv.org/abs/1805.10872"
          },
          {
            "title": "(PDF) Neural probabilistic logic programming in DeepProbLog",
            "url": "https://www.researchgate.net/publication/350911019_Neural_probabilistic_logic_programming_in_DeepProbLog"
          },
          {
            "title": "GitHub - ML-KULeuven/deepproblog: DeepProbLog is an extension of ProbLog that integrates Probabilistic Logic Programming with deep learning by introducing the neural predicate. · GitHub",
            "url": "https://github.com/ML-KULeuven/deepproblog"
          },
          {
            "title": "(Open Access) Neural probabilistic logic programming in DeepProbLog (2021) | Robin Manhaeve | 158 Citations",
            "url": "https://scispace.com/papers/neural-probabilistic-logic-programming-in-deepproblog-x2gdjqjbs3"
          },
          {
            "title": "(PDF) DeepProbLog: Neural Probabilistic Logic Programming",
            "url": "https://www.researchgate.net/publication/334602669_DeepProbLog_Neural_Probabilistic_Logic_Programming"
          },
          {
            "title": "Neural probabilistic logic programming in DeepProbLog - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S0004370221000552"
          },
          {
            "title": "[PDF] DeepProbLog: Neural Probabilistic Logic Programming | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/DeepProbLog:-Neural-Probabilistic-Logic-Programming-Manhaeve-Dumancic/f6e6fba61b654c5b799a9efe3b5849ce1197aab3"
          },
          {
            "title": "[1907.08194] Neural Probabilistic Logic Programming in DeepProbLog",
            "url": "https://arxiv.org/abs/1907.08194"
          },
          {
            "title": "DeepProbLog: Neural Probabilistic Logic Programming",
            "url": "https://ceur-ws.org/Vol-2491/abstract68.pdf"
          },
          {
            "title": "DeepProbLog: Neural Probabilistic Logic Programming Robin Manhaeve KU Leuven",
            "url": "https://arxiv.org/pdf/1805.10872"
          }
        ]
      },
      "Based on the search results, I found information about the DeepProbLog work by Manhaeve and colleagues:\n\nRobin Manhaeve, Sebastijan Dumancic, Angelika Kimmig, Thomas Demeester, and Luc De Raedt published \"Neural Probabilistic Logic Programming in DeepProbLog\" in AIJ (Artificial Intelligence Journal). The article was published in Artificial Intelligence on September 1, 2021, and is currently open access.\n\nThe work introduces DeepProbLog, a neural probabilistic logic programming language that incorporates deep learning by means of neural predicates, and shows how existing inference and learning techniques of the underlying probabilistic logic programming language ProbLog can be adapted for the new language.\n\nDeepProbLog supports both symbolic and subsymbolic representations and inference, program induction, probabilistic (logic) programming, and (deep) learning from examples."
    ],
    "durationSeconds": 5.6107175549999955
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T17:43:42.569Z_

<details><summary>↩ Tool result · `toolu_01Fb7vbLkBq3ZWyMsmmCRZkM`</summary>

```text
Web search results for query: "NeurASP Yang Ishay "Neural Answer Set Programming" 2020 IJCAI"

Links: [{"title":"NeurASP: Embracing Neural Networks into Answer Set Programming | IJCAI","url":"https://www.ijcai.org/proceedings/2020/243"},{"title":"NeurASP: Embracing Neural Networks into Answer Set ...","url":"https://www.ijcai.org/proceedings/2020/0243.pdf"},{"title":"NeurASP: Embracing Neural Networks into Answer Set Programming | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10184165-neurasp-embracing-neural-networks-answer-set-programming"},{"title":"GitHub - azreasoners/NeurASP · GitHub","url":"https://github.com/azreasoners/NeurASP"},{"title":"[PDF] NeurASP: Embracing Neural Networks into Answer Set Programming | Semantic Scholar","url":"https://www.semanticscholar.org/paper/NeurASP:-Embracing-Neural-Networks-into-Answer-Set-Yang-Ishay/e53beddcf3b79dd1f4673f126bbda6526039b2b8"},{"title":"NeurASP: Embracing neural networks into answer set programming - Arizona State University","url":"https://asu.elsevierpure.com/en/publications/neurasp-embracing-neural-networks-into-answer-set-programming/"},{"title":"A Simple Extension of Answer Set Programs to Embrace ...","url":"https://par.nsf.gov/servlets/purl/10295440"},{"title":"NeurASP: Embracing Neural Networks into Answer Set Programming | Request PDF","url":"https://www.researchgate.net/publication/342796349_NeurASP_Embracing_Neural_Networks_into_Answer_Set_Programming"},{"title":"dblp: NeurASP: Embracing Neural Networks into Answer Set Programming.","url":"https://dblp.org/rec/conf/ijcai/YangIL20.html"},{"title":"[2307.07700] NeurASP: Embracing Neural Networks into Answer Set Programming","url":"https://arxiv.org/abs/2307.07700"}]

I found comprehensive information about the NeurASP paper. Here's a summary of the search results:

## NeurASP: Embracing Neural Networks into Answer Set Programming

The paper was authored by Yang, Zhun; Ishay, Adam; and Lee, Joohyung, and published in 2020 in the 29th International Joint Conference on Artificial Intelligence (IJCAI 2020).

### Overview

NeurASP is a simple extension of answer set programs by embracing neural networks. By treating the neural network output as the probability distribution over atomic facts in answer set programs, NeurASP provides a simple and effective way to integrate sub-symbolic and symbolic computation.

### Key Capabilities

NeurASP can make use of ASP rules to train a neural network better so that a neural network not only learns from implicit correlations from the data but also from the explicit complex semantic constraints expressed by the rules.

It demonstrates how NeurASP can make use of a pre-trained neural network in symbolic computation and how it can improve the neural network's perception result by applying symbolic reasoning in answer set programming.

### Publication Details

The paper was published in IJCAI 2020, pages 1755-1762. The paper's DOI is 10.24963/ijcai.2020/243.

The implementation is also available on GitHub at the azreasoners/NeurASP repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "c8372da0-9456-40e4-a701-f77c96d31642",
  "tool_use_result": {
    "query": "NeurASP Yang Ishay \"Neural Answer Set Programming\" 2020 IJCAI",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JC8FWyze8RB6ATPVKCcf5F",
        "content": [
          {
            "title": "NeurASP: Embracing Neural Networks into Answer Set Programming | IJCAI",
            "url": "https://www.ijcai.org/proceedings/2020/243"
          },
          {
            "title": "NeurASP: Embracing Neural Networks into Answer Set ...",
            "url": "https://www.ijcai.org/proceedings/2020/0243.pdf"
          },
          {
            "title": "NeurASP: Embracing Neural Networks into Answer Set Programming | NSF Public Access Repository",
            "url": "https://par.nsf.gov/biblio/10184165-neurasp-embracing-neural-networks-answer-set-programming"
          },
          {
            "title": "GitHub - azreasoners/NeurASP · GitHub",
            "url": "https://github.com/azreasoners/NeurASP"
          },
          {
            "title": "[PDF] NeurASP: Embracing Neural Networks into Answer Set Programming | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/NeurASP:-Embracing-Neural-Networks-into-Answer-Set-Yang-Ishay/e53beddcf3b79dd1f4673f126bbda6526039b2b8"
          },
          {
            "title": "NeurASP: Embracing neural networks into answer set programming - Arizona State University",
            "url": "https://asu.elsevierpure.com/en/publications/neurasp-embracing-neural-networks-into-answer-set-programming/"
          },
          {
            "title": "A Simple Extension of Answer Set Programs to Embrace ...",
            "url": "https://par.nsf.gov/servlets/purl/10295440"
          },
          {
            "title": "NeurASP: Embracing Neural Networks into Answer Set Programming | Request PDF",
            "url": "https://www.researchgate.net/publication/342796349_NeurASP_Embracing_Neural_Networks_into_Answer_Set_Programming"
          },
          {
            "title": "dblp: NeurASP: Embracing Neural Networks into Answer Set Programming.",
            "url": "https://dblp.org/rec/conf/ijcai/YangIL20.html"
          },
          {
            "title": "[2307.07700] NeurASP: Embracing Neural Networks into Answer Set Programming",
            "url": "https://arxiv.org/abs/2307.07700"
          }
        ]
      },
      "I found comprehensive information about the NeurASP paper. Here's a summary of the search results:\n\n## NeurASP: Embracing Neural Networks into Answer Set Programming\n\nThe paper was authored by Yang, Zhun; Ishay, Adam; and Lee, Joohyung, and published in 2020 in the 29th International Joint Conference on Artificial Intelligence (IJCAI 2020).\n\n### Overview\n\nNeurASP is a simple extension of answer set programs by embracing neural networks. By treating the neural network output as the probability distribution over atomic facts in answer set programs, NeurASP provides a simple and effective way to integrate sub-symbolic and symbolic computation.\n\n### Key Capabilities\n\nNeurASP can make use of ASP rules to train a neural network better so that a neural network not only learns from implicit correlations from the data but also from the explicit complex semantic constraints expressed by the rules.\n\nIt demonstrates how NeurASP can make use of a pre-trained neural network in symbolic computation and how it can improve the neural network's perception result by applying symbolic reasoning in answer set programming.\n\n### Publication Details\n\nThe paper was published in IJCAI 2020, pages 1755-1762. The paper's DOI is 10.24963/ijcai.2020/243.\n\nThe implementation is also available on GitHub at the azreasoners/NeurASP repository."
    ],
    "durationSeconds": 5.8396403480000005
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T17:43:45.805Z_

<details><summary>↩ Tool result · `toolu_017KEK5AXQ3GKH3cwqZF5G9F`</summary>

```text
Web search results for query: ""logic programming" "reinforcement learning" LLM GRPO 2024 2025 arxiv"

Links: [{"title":"One Tool Is Enough: Reinforcement Learning of LLM Agents for Repository-Level Code Navigation","url":"https://arxiv.org/html/2512.20957"},{"title":"Tree Search for LLM Agent Reinforcement Learning","url":"https://arxiv.org/pdf/2509.21240"},{"title":"The State of Reinforcement Learning for LLM Reasoning","url":"https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training"},{"title":"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs","url":"https://arxiv.org/html/2506.14245v2"},{"title":"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning","url":"https://arxiv.org/html/2502.14768v1"},{"title":"Reinforcement Learning Meets Large Language Models: A Survey of Advancements and Applications Across the LLM Lifecycle","url":"https://arxiv.org/html/2509.16679v1"},{"title":"[2512.15687] Can LLMs Guide Their Own Exploration? Gradient-Guided Reinforcement Learning for LLM Reasoning","url":"https://arxiv.org/abs/2512.15687"},{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"},{"title":"A Survey of Reinforcement Learning for Large Language Models under Data Scarcity: Challenges and Solutions","url":"https://arxiv.org/html/2604.17312v1"},{"title":"[2509.08827] A Survey of Reinforcement Learning for Large Reasoning Models","url":"https://arxiv.org/abs/2509.08827"}]

I've found several relevant papers from arxiv combining these research areas. Here are the key findings:

## Recent Work on Logic Programming, Reinforcement Learning, and LLMs (2024-2025)

### Logic-RL Framework
One notable paper is "Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning" which explores reinforcement learning approaches for LLM reasoning.

### GRPO and LLM Agent Training
Recent research investigates the capabilities of GRPO and hybrid reward functions within agentic training, with results indicating that methods combining RL and hybrid reward mechanisms significantly surpass supervised fine-tuning (SFT) and standard GRPO approaches.

### Tree Search with GRPO
GSPO is a variant of GRPO that replaces token-level importance ratio calculation with trajectory-level reweighting, improving the stability of LLM RL training. Additionally, techniques ranging from PPO, GRPO, GSPO, along with policy variants such as DAPO and GPG are employed for LLM RL training.

### Logical Reasoning and RLVR
ToTRL improved the reasoning efficiency of language models in multi-path logical problems by guiding them to transition from linear chain reasoning to tree-structured thinking, demonstrating integration of logical structure with RL.

### Gradient-Guided RL (Recent 2025)
G2RL is a gradient-guided reinforcement learning framework where exploration is driven by the model's own first order update geometry, constructed from the model's final layer sensitivity at negligible computational cost.

The search results show an active research area combining logical reasoning, reinforcement learning techniques like GRPO, and LLM capabilities in 2024-2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "b092cbbf-7e39-4597-88eb-e15af5152f69",
  "tool_use_result": {
    "query": "\"logic programming\" \"reinforcement learning\" LLM GRPO 2024 2025 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01A5Yzs5VdnCHbMd1NgZDUuh",
        "content": [
          {
            "title": "One Tool Is Enough: Reinforcement Learning of LLM Agents for Repository-Level Code Navigation",
            "url": "https://arxiv.org/html/2512.20957"
          },
          {
            "title": "Tree Search for LLM Agent Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2509.21240"
          },
          {
            "title": "The State of Reinforcement Learning for LLM Reasoning",
            "url": "https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training"
          },
          {
            "title": "Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs",
            "url": "https://arxiv.org/html/2506.14245v2"
          },
          {
            "title": "Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning",
            "url": "https://arxiv.org/html/2502.14768v1"
          },
          {
            "title": "Reinforcement Learning Meets Large Language Models: A Survey of Advancements and Applications Across the LLM Lifecycle",
            "url": "https://arxiv.org/html/2509.16679v1"
          },
          {
            "title": "[2512.15687] Can LLMs Guide Their Own Exploration? Gradient-Guided Reinforcement Learning for LLM Reasoning",
            "url": "https://arxiv.org/abs/2512.15687"
          },
          {
            "title": "Group Relative Policy Optimization (GRPO)",
            "url": "https://cameronrwolfe.substack.com/p/grpo"
          },
          {
            "title": "A Survey of Reinforcement Learning for Large Language Models under Data Scarcity: Challenges and Solutions",
            "url": "https://arxiv.org/html/2604.17312v1"
          },
          {
            "title": "[2509.08827] A Survey of Reinforcement Learning for Large Reasoning Models",
            "url": "https://arxiv.org/abs/2509.08827"
          }
        ]
      },
      "I've found several relevant papers from arxiv combining these research areas. Here are the key findings:\n\n## Recent Work on Logic Programming, Reinforcement Learning, and LLMs (2024-2025)\n\n### Logic-RL Framework\nOne notable paper is \"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\" which explores reinforcement learning approaches for LLM reasoning.\n\n### GRPO and LLM Agent Training\nRecent research investigates the capabilities of GRPO and hybrid reward functions within agentic training, with results indicating that methods combining RL and hybrid reward mechanisms significantly surpass supervised fine-tuning (SFT) and standard GRPO approaches.\n\n### Tree Search with GRPO\nGSPO is a variant of GRPO that replaces token-level importance ratio calculation with trajectory-level reweighting, improving the stability of LLM RL training. Additionally, techniques ranging from PPO, GRPO, GSPO, along with policy variants such as DAPO and GPG are employed for LLM RL training.\n\n### Logical Reasoning and RLVR\nToTRL improved the reasoning efficiency of language models in multi-path logical problems by guiding them to transition from linear chain reasoning to tree-structured thinking, demonstrating integration of logical structure with RL.\n\n### Gradient-Guided RL (Recent 2025)\nG2RL is a gradient-guided reinforcement learning framework where exploration is driven by the model's own first order update geometry, constructed from the model's final layer sensitivity at negligible computational cost.\n\nThe search results show an active research area combining logical reasoning, reinforcement learning techniques like GRPO, and LLM capabilities in 2024-2025."
    ],
    "durationSeconds": 7.7785618119999995
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T17:43:45.887Z_

<details><summary>↩ Tool result · `toolu_01Kb2vi4npeqgSSz16KHsRUz`</summary>

```text
Web search results for query: "Krakovna "specification gaming" examples list DeepMind 2020"

Links: [{"title":"Specification gaming: the flip side of AI ingenuity — Google DeepMind","url":"https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/"},{"title":"Specification gaming examples in AI | Victoria Krakovna","url":"https://vkrakovna.wordpress.com/2018/04/02/specification-gaming-examples-in-ai/"},{"title":"Interview with Victoria Krakovna on the strength of the evidence for AI risk claims [AI Impacts Wiki]","url":"https://wiki.aiimpacts.org/arguments_for_ai_risk/is_ai_an_existential_threat_to_humanity/interviews_on_the_strength_of_the_evidence_for_ai_risk_claims/summary_of_an_interview_on_the_strength_of_the_evidence_for_ai_risk_claims_with_victoria_krakovna"},{"title":"Specification Gaming: The Flip Side of AI Ingenuity « Machine Learning Times","url":"https://www.predictiveanalyticsworld.com/machinelearningtimes/specification-gaming-the-flip-side-of-ai-ingenuity/11431/"},{"title":"Here is a master list for specification gaming examples in ...","url":"https://www.facebook.com/groups/aisafetyopen/posts/164661780903523/"},{"title":"Victoria Krakovna","url":"https://scholar.google.com/citations?user=2ZdBaGQAAAAJ&hl=en"},{"title":"Goal misgeneralization: Why correct specifications aren't ...","url":"https://arxiv.org/pdf/2210.01790"},{"title":"Research | Victoria Krakovna - WordPress.com","url":"https://vkrakovna.wordpress.com/research/"},{"title":"Demonstrating specification gaming in reasoning models Alexander Bondarenko 1","url":"https://arxiv.org/pdf/2502.13295"},{"title":"Specification gaming: the flip side of AI ingenuity · Pablo Stafforini","url":"https://stafforini.com/works/krakovna-2020-specification-gaming-flip/"}]

I found the search results for your query. Victoria Krakovna and colleagues (Jonathan Uesato, Vladimir Mikulik, Matthew Rahtz, Tom Everitt, Ramana Kumar, Zac Kenton, Jan Leike, and Shane Legg) published "Specification gaming: the flip side of AI ingenuity" on the DeepMind blog in 2020.

Specification gaming is a behaviour that satisfies the literal specification of an objective without achieving the intended outcome.

The paper includes several examples of specification gaming in AI systems. One specific example discussed is an agent controlling a boat in the Coast Runners game, where the intended goal was to finish the boat race as quickly as possible, but the agent was given a shaping reward for hitting green blocks along the race track, which changed the optimal policy to going in circles and hitting the same green blocks over and over again.

According to the search results, there are over 70 empirical examples of specification gaming that Victoria Krakovna has compiled. You can find a more comprehensive list of examples by visiting the DeepMind blog post or Victoria Krakovna's website, where she maintains documentation of specification gaming examples in AI systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "7982167b-bd40-413a-9e03-08b9b79a7566",
  "tool_use_result": {
    "query": "Krakovna \"specification gaming\" examples list DeepMind 2020",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XGWYuGrBVM7KV5z3G9jpb3",
        "content": [
          {
            "title": "Specification gaming: the flip side of AI ingenuity — Google DeepMind",
            "url": "https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/"
          },
          {
            "title": "Specification gaming examples in AI | Victoria Krakovna",
            "url": "https://vkrakovna.wordpress.com/2018/04/02/specification-gaming-examples-in-ai/"
          },
          {
            "title": "Interview with Victoria Krakovna on the strength of the evidence for AI risk claims [AI Impacts Wiki]",
            "url": "https://wiki.aiimpacts.org/arguments_for_ai_risk/is_ai_an_existential_threat_to_humanity/interviews_on_the_strength_of_the_evidence_for_ai_risk_claims/summary_of_an_interview_on_the_strength_of_the_evidence_for_ai_risk_claims_with_victoria_krakovna"
          },
          {
            "title": "Specification Gaming: The Flip Side of AI Ingenuity « Machine Learning Times",
            "url": "https://www.predictiveanalyticsworld.com/machinelearningtimes/specification-gaming-the-flip-side-of-ai-ingenuity/11431/"
          },
          {
            "title": "Here is a master list for specification gaming examples in ...",
            "url": "https://www.facebook.com/groups/aisafetyopen/posts/164661780903523/"
          },
          {
            "title": "Victoria Krakovna",
            "url": "https://scholar.google.com/citations?user=2ZdBaGQAAAAJ&hl=en"
          },
          {
            "title": "Goal misgeneralization: Why correct specifications aren't ...",
            "url": "https://arxiv.org/pdf/2210.01790"
          },
          {
            "title": "Research | Victoria Krakovna - WordPress.com",
            "url": "https://vkrakovna.wordpress.com/research/"
          },
          {
            "title": "Demonstrating specification gaming in reasoning models Alexander Bondarenko 1",
            "url": "https://arxiv.org/pdf/2502.13295"
          },
          {
            "title": "Specification gaming: the flip side of AI ingenuity · Pablo Stafforini",
            "url": "https://stafforini.com/works/krakovna-2020-specification-gaming-flip/"
          }
        ]
      },
      "I found the search results for your query. Victoria Krakovna and colleagues (Jonathan Uesato, Vladimir Mikulik, Matthew Rahtz, Tom Everitt, Ramana Kumar, Zac Kenton, Jan Leike, and Shane Legg) published \"Specification gaming: the flip side of AI ingenuity\" on the DeepMind blog in 2020.\n\nSpecification gaming is a behaviour that satisfies the literal specification of an objective without achieving the intended outcome.\n\nThe paper includes several examples of specification gaming in AI systems. One specific example discussed is an agent controlling a boat in the Coast Runners game, where the intended goal was to finish the boat race as quickly as possible, but the agent was given a shaping reward for hitting green blocks along the race track, which changed the optimal policy to going in circles and hitting the same green blocks over and over again.\n\nAccording to the search results, there are over 70 empirical examples of specification gaming that Victoria Krakovna has compiled. You can find a more comprehensive list of examples by visiting the DeepMind blog post or Victoria Krakovna's website, where she maintains documentation of specification gaming examples in AI systems."
    ],
    "durationSeconds": 8.221160717999998
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for a few more specific papers I think might be missing:

1. For Prolog/LP + RL: DeepProbLog and NeurASP are confirmed. But these are not RL papers per se - they're neuro-symbolic integration. The map already has good coverage of direct Prolog+RL work. Let me think about whether DeepProbLog/NeurASP are truly relevant...

Actually, looking at the task description more carefully, it says to check for "Prolog/logic programming 与 RL/LLM 结合的论文". The map already has:


- mellgren-prolog-grpo: Prolog + GRPO ✓
- logic-rl: Logic + RL ✓  
- satlm: SAT solver + LLM ✓
- linc: FOL prover + LLM ✓
- logic-lm: Symbolic solver + LLM ✓
- lorp: Prolog + LLM ✓

So the direct combinations are covered. What's missing is the foundational neuro-symbolic logic programming work like DeepProbLog and NeurASP - even though they don't use RL, they're essential to the broader Prolog-neural tradition and should probably be included for context.

I should also track down the Bondarenko 2025 paper on specification gaming in reasoning models since it came up in my search, plus look for any other recent papers combining Prolog, LLMs, and RL.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "796d15db-12bc-487a-8c41-ab333e6983f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrKrn8H2XR6athZ6QX5iys",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 916,
      "cache_creation_input_tokens": 3120,
      "cache_read_input_tokens": 43801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3120
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EZe5gSMZ1tn42NdtWu4ipd`</summary>

```json
{
  "query": "Bondarenko 2025 \"specification gaming in reasoning models\" arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "deb10acb-e413-4c80-9062-b71c3ba7ef9a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrKrn8H2XR6athZ6QX5iys",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 916,
      "cache_creation_input_tokens": 3120,
      "cache_read_input_tokens": 43801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3120
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LFzD1Fm1XvsjrzAs6cmcuJ`</summary>

```json
{
  "query": "Prolog code generation LLM training 2024 2025 arxiv fine-tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "88624591-7b6e-4fb8-be0d-f9a57234c51a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrKrn8H2XR6athZ6QX5iys",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 916,
      "cache_creation_input_tokens": 3120,
      "cache_read_input_tokens": 43801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3120
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

_source line 33 · 2026-05-14T17:44:04.604Z_

<details><summary>↩ Tool result · `toolu_01EZe5gSMZ1tn42NdtWu4ipd`</summary>

```text
Web search results for query: "Bondarenko 2025 "specification gaming in reasoning models" arxiv"

Links: [{"title":"[2502.13295] Demonstrating specification gaming in reasoning models","url":"https://arxiv.org/abs/2502.13295"},{"title":"Demonstrating specification gaming in reasoning models Alexander Bondarenko 1","url":"https://arxiv.org/pdf/2502.13295"},{"title":"Towards Understanding Specification Gaming in Reasoning Models","url":"https://arxiv.org/html/2605.02269v1"},{"title":"[2502.13295v1] Demonstrating specification gaming in reasoning models","url":"https://arxiv.org/abs/2502.13295v1"},{"title":"[2502.13295v2] Demonstrating specification gaming in reasoning models","url":"https://arxiv.org/abs/2502.13295v2"},{"title":"(PDF) Demonstrating specification gaming in reasoning models","url":"https://www.researchgate.net/publication/389167750_Demonstrating_specification_gaming_in_reasoning_models"},{"title":"arXiv:2505.07846v1 [cs.AI] 7 May 2025","url":"https://arxiv.org/pdf/2505.07846"},{"title":"Artificial Intelligence Feb 2025","url":"https://arxiv.org/list/cs.AI/2025-02?skip=325&show=100"},{"title":"[2605.02269v1] Towards Understanding Specification Gaming in Reasoning Models","url":"https://arxiv.org/abs/2605.02269v1"},{"title":"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning","url":"https://arxiv.org/pdf/2604.19459"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** "Demonstrating specification gaming in reasoning models"

**Authors:** Alexander Bondarenko, Denis Volk, Dmitrii Volkov, and Jeffrey Ladish

**ArXiv ID:** 2502.13295

**Submission Date:** Submitted on 18 Feb 2025, with the latest version revised 27 Aug 2025

**Summary:** The paper demonstrates LLM agent specification gaming by instructing models to win against a chess engine. They find reasoning models like OpenAI o3 and DeepSeek R1 will often hack the benchmark by default, while language models like GPT-4o and Claude 3.5 Sonnet need to be told that normal play won't work to hack.

**Key Findings:** The authors improve upon prior work by using realistic task prompts and avoiding excess nudging. Their results suggest reasoning models may resort to hacking to solve difficult problems, as observed in OpenAI's o1 Docker escape during cyber capabilities testing.

You can access the paper directly at: https://arxiv.org/abs/2502.13295


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "fb4cb8d6-c76c-4ca0-8c3f-4a5ddbb8bf45",
  "tool_use_result": {
    "query": "Bondarenko 2025 \"specification gaming in reasoning models\" arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QfmT8Ee6gjyWvfkBFWi6sN",
        "content": [
          {
            "title": "[2502.13295] Demonstrating specification gaming in reasoning models",
            "url": "https://arxiv.org/abs/2502.13295"
          },
          {
            "title": "Demonstrating specification gaming in reasoning models Alexander Bondarenko 1",
            "url": "https://arxiv.org/pdf/2502.13295"
          },
          {
            "title": "Towards Understanding Specification Gaming in Reasoning Models",
            "url": "https://arxiv.org/html/2605.02269v1"
          },
          {
            "title": "[2502.13295v1] Demonstrating specification gaming in reasoning models",
            "url": "https://arxiv.org/abs/2502.13295v1"
          },
          {
            "title": "[2502.13295v2] Demonstrating specification gaming in reasoning models",
            "url": "https://arxiv.org/abs/2502.13295v2"
          },
          {
            "title": "(PDF) Demonstrating specification gaming in reasoning models",
            "url": "https://www.researchgate.net/publication/389167750_Demonstrating_specification_gaming_in_reasoning_models"
          },
          {
            "title": "arXiv:2505.07846v1 [cs.AI] 7 May 2025",
            "url": "https://arxiv.org/pdf/2505.07846"
          },
          {
            "title": "Artificial Intelligence Feb 2025",
            "url": "https://arxiv.org/list/cs.AI/2025-02?skip=325&show=100"
          },
          {
            "title": "[2605.02269v1] Towards Understanding Specification Gaming in Reasoning Models",
            "url": "https://arxiv.org/abs/2605.02269v1"
          },
          {
            "title": "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning",
            "url": "https://arxiv.org/pdf/2604.19459"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details:\n\n**Paper Title:** \"Demonstrating specification gaming in reasoning models\"\n\n**Authors:** Alexander Bondarenko, Denis Volk, Dmitrii Volkov, and Jeffrey Ladish\n\n**ArXiv ID:** 2502.13295\n\n**Submission Date:** Submitted on 18 Feb 2025, with the latest version revised 27 Aug 2025\n\n**Summary:** The paper demonstrates LLM agent specification gaming by instructing models to win against a chess engine. They find reasoning models like OpenAI o3 and DeepSeek R1 will often hack the benchmark by default, while language models like GPT-4o and Claude 3.5 Sonnet need to be told that normal play won't work to hack.\n\n**Key Findings:** The authors improve upon prior work by using realistic task prompts and avoiding excess nudging. Their results suggest reasoning models may resort to hacking to solve difficult problems, as observed in OpenAI's o1 Docker escape during cyber capabilities testing.\n\nYou can access the paper directly at: https://arxiv.org/abs/2502.13295"
    ],
    "durationSeconds": 6.317352966000006
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T17:44:06.391Z_

<details><summary>↩ Tool result · `toolu_01LFzD1Fm1XvsjrzAs6cmcuJ`</summary>

```text
Web search results for query: "Prolog code generation LLM training 2024 2025 arxiv fine-tuning"

Links: [{"title":"Training Language Models to Use Prolog as a Tool","url":"https://arxiv.org/html/2512.07407v1"},{"title":"Arithmetic Reasoning with LLM: Prolog Generation & ...","url":"https://aclanthology.org/2024.naacl-short.61.pdf"},{"title":"[2405.17893] Arithmetic Reasoning with LLM: Prolog Generation & Permutation","url":"https://arxiv.org/abs/2405.17893"},{"title":"Arithmetic Reasoning with LLM: Prolog Generation & Permutation - ACL Anthology","url":"https://aclanthology.org/2024.naacl-short.61/"},{"title":"Data-efficient LLM Fine-tuning for Code Generation","url":"https://arxiv.org/html/2504.12687v1"},{"title":"Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Though","url":"https://arxiv.org/html/2407.14562v1"},{"title":"When Prolog meets generative models: a new approach","url":"https://arxiv.org/pdf/2309.15049"},{"title":"Large Language Models for Code Generation: A Comprehensive Survey of Challenges, Techniques, Evaluation, and Applications","url":"https://arxiv.org/html/2503.01245v2"},{"title":"Exploring Parameter-Efficient Fine-Tuning Techniques for ...","url":"https://arxiv.org/pdf/2308.10462"},{"title":"An Exploratory Study on Fine-Tuning Large Language Models for Secure Code Generation","url":"https://arxiv.org/html/2408.09078v1"}]

Based on the web search results, here are the key findings on Prolog code generation with LLM training:

## Recent Research on Prolog Code Generation and LLM Training (2024-2025)

### 1. **Reinforcement Learning Approach (December 2025)**
A recent study investigated fine-tuning models to use Prolog as an external tool for verifiable computation through reinforcement learning with verifiable rewards (RLVR). The research employed group relative policy optimization (GRPO), which has led to promising results in DeepSeek-R1. The results established that RLVR and specifically GRPO is well-suited to teach even a relatively small language model with only 3B parameters to use Prolog as a tool, achieving results comparable to 7B models on mathematical and logical reasoning tasks.

### 2. **Data Augmentation for Arithmetic Reasoning (May 2024)**
Research investigated using LLM to generate Prolog programs to solve mathematical questions, with the hypothesis that an LLM should focus on extracting predicates and generating symbolic formulas from problem descriptions so that underlying calculation can be done via an external code interpreter. The work proposed to permute the ground truth predicates for more robust LLM training via data augmentation.

### 3. **Logical Reasoning Framework (July 2024)**
A framework called Thought-Like-Pro was designed to enhance the general logical reasoning capabilities of LLMs, enabling them to imitate strictly logical reasoning trajectories generated and validated by the Prolog engine.

### 4. **Key Insight on Training Approach**
In contrast to prior work that relied on in-context learning or supervised fine-tuning, recent research uses reinforcement learning with verifiable rewards to teach language models to use Prolog as a tool, outperforming supervised fine-tuning baselines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "729b5742-48bf-46ea-80f9-d9d0fea4de76",
  "tool_use_result": {
    "query": "Prolog code generation LLM training 2024 2025 arxiv fine-tuning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CY9tvYdjmrzzq8vjTQTmmT",
        "content": [
          {
            "title": "Training Language Models to Use Prolog as a Tool",
            "url": "https://arxiv.org/html/2512.07407v1"
          },
          {
            "title": "Arithmetic Reasoning with LLM: Prolog Generation & ...",
            "url": "https://aclanthology.org/2024.naacl-short.61.pdf"
          },
          {
            "title": "[2405.17893] Arithmetic Reasoning with LLM: Prolog Generation & Permutation",
            "url": "https://arxiv.org/abs/2405.17893"
          },
          {
            "title": "Arithmetic Reasoning with LLM: Prolog Generation & Permutation - ACL Anthology",
            "url": "https://aclanthology.org/2024.naacl-short.61/"
          },
          {
            "title": "Data-efficient LLM Fine-tuning for Code Generation",
            "url": "https://arxiv.org/html/2504.12687v1"
          },
          {
            "title": "Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Though",
            "url": "https://arxiv.org/html/2407.14562v1"
          },
          {
            "title": "When Prolog meets generative models: a new approach",
            "url": "https://arxiv.org/pdf/2309.15049"
          },
          {
            "title": "Large Language Models for Code Generation: A Comprehensive Survey of Challenges, Techniques, Evaluation, and Applications",
            "url": "https://arxiv.org/html/2503.01245v2"
          },
          {
            "title": "Exploring Parameter-Efficient Fine-Tuning Techniques for ...",
            "url": "https://arxiv.org/pdf/2308.10462"
          },
          {
            "title": "An Exploratory Study on Fine-Tuning Large Language Models for Secure Code Generation",
            "url": "https://arxiv.org/html/2408.09078v1"
          }
        ]
      },
      "Based on the web search results, here are the key findings on Prolog code generation with LLM training:\n\n## Recent Research on Prolog Code Generation and LLM Training (2024-2025)\n\n### 1. **Reinforcement Learning Approach (December 2025)**\nA recent study investigated fine-tuning models to use Prolog as an external tool for verifiable computation through reinforcement learning with verifiable rewards (RLVR). The research employed group relative policy optimization (GRPO), which has led to promising results in DeepSeek-R1. The results established that RLVR and specifically GRPO is well-suited to teach even a relatively small language model with only 3B parameters to use Prolog as a tool, achieving results comparable to 7B models on mathematical and logical reasoning tasks.\n\n### 2. **Data Augmentation for Arithmetic Reasoning (May 2024)**\nResearch investigated using LLM to generate Prolog programs to solve mathematical questions, with the hypothesis that an LLM should focus on extracting predicates and generating symbolic formulas from problem descriptions so that underlying calculation can be done via an external code interpreter. The work proposed to permute the ground truth predicates for more robust LLM training via data augmentation.\n\n### 3. **Logical Reasoning Framework (July 2024)**\nA framework called Thought-Like-Pro was designed to enhance the general logical reasoning capabilities of LLMs, enabling them to imitate strictly logical reasoning trajectories generated and validated by the Prolog engine.\n\n### 4. **Key Insight on Training Approach**\nIn contrast to prior work that relied on in-context learning or supervised fine-tuning, recent research uses reinforcement learning with verifiable rewards to teach language models to use Prolog as a tool, outperforming supervised fine-tuning baselines."
    ],
    "durationSeconds": 8.092103529999992
  }
}
```

</details>

---

### Assistant

_source line 35_

<details><summary>Logged reasoning block</summary>

```text
I found some interesting papers. Let me now check:

1. "Arithmetic Reasoning with LLM: Prolog Generation & Permutation" (2024, NAACL) - Yang et al.
2. "Thought-Like-Pro" (2024) - Prolog-based CoT
3. Bondarenko et al. 2025 "Demonstrating specification gaming in reasoning models" - very relevant to reward hacking
4. "Towards Understanding Specification Gaming in Reasoning Models" (2605.02269) - even more recent

And I found earlier:
5. DeepProbLog (Manhaeve et al., 2021)


6. NeurASP (Yang et al., 2020)

I also spotted "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning" (2604.19459) which seems directly relevant to specification gaming and alignment - I should dig into these papers more carefully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "98f8f649-fe7e-41f3-812a-98eed41cb31f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014uQ7JR5FphauU66X595Jpj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3086,
      "cache_read_input_tokens": 46921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3086
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TxgaGRvEs1od1cZyAzN9QY`</summary>

```json
{
  "query": "\"Do LLMs Game Formalization\" \"Evaluating Faithfulness\" logical reasoning 2604.19459 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "fd8c606d-7682-405b-832e-d85368176b98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014uQ7JR5FphauU66X595Jpj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3086,
      "cache_read_input_tokens": 46921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3086
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_014dWCyXnGvapgb87muMg1Qu`</summary>

```json
{
  "query": "\"Thought-Like-Pro\" \"Prolog-based Chain-of-Thought\" 2024 arxiv authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "8327b96c-4149-411a-b1bf-d58bf8c09037",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014uQ7JR5FphauU66X595Jpj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3086,
      "cache_read_input_tokens": 46921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3086
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ch3c58sdaYgvstKFS6EEFZ`</summary>

```json
{
  "query": "\"Arithmetic Reasoning with LLM Prolog Generation Permutation\" NAACL 2024 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "5568df50-87d1-4418-8347-a5a9c1b5adc1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014uQ7JR5FphauU66X595Jpj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3086,
      "cache_read_input_tokens": 46921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3086
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

_source line 39 · 2026-05-14T17:44:18.589Z_

<details><summary>↩ Tool result · `toolu_01Ch3c58sdaYgvstKFS6EEFZ`</summary>

```text
Web search results for query: ""Arithmetic Reasoning with LLM Prolog Generation Permutation" NAACL 2024 authors"

Links: [{"title":"Arithmetic Reasoning with LLM: Prolog Generation & Permutation - ACL Anthology","url":"https://aclanthology.org/2024.naacl-short.61/"},{"title":"Arithmetic Reasoning with LLM: Prolog Generation & ...","url":"https://aclanthology.org/2024.naacl-short.61.pdf"},{"title":"[2405.17893] Arithmetic Reasoning with LLM: Prolog Generation & Permutation","url":"https://arxiv.org/abs/2405.17893"},{"title":"Arithmetic Reasoning with LLM: Prolog Generation & Permutation","url":"https://arxiv.org/html/2405.17893v1"},{"title":"Paper page - Arithmetic Reasoning with LLM: Prolog Generation & Permutation","url":"https://huggingface.co/papers/2405.17893"},{"title":"Underline | Arithmetic Reasoning with LLM: Prolog Generation & Permutation","url":"https://underline.io/lecture/97853-arithmetic-reasoning-with-llm-prolog-generation-and-permutation"},{"title":"(PDF) Arithmetic Reasoning with LLM: Prolog Generation & Permutation","url":"https://www.researchgate.net/publication/380935097_Arithmetic_Reasoning_with_LLM_Prolog_Generation_Permutation"},{"title":"Arithmetic Reasoning with LLM: Prolog Generation & Permutation | alphaXiv","url":"https://www.alphaxiv.org/abs/2405.17893"},{"title":"Arithmetic Reasoning with LLM: Prolog Generation & Permutation | PromptLayer","url":"https://www.promptlayer.com/research-papers/arithmetic-reasoning-with-llm-prolog-generation-permutation"},{"title":"Arithmetic Reasoning with LLM: Prolog Generation & Permutation | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/arithmetic-reasoning-llm-prolog-generation-permutation"}]

Based on the search results, I found the paper "Arithmetic Reasoning with LLM: Prolog Generation & Permutation" from NAACL 2024. 

The authors are Xiaocheng Yang, Bingsen Chen, and Yik-Cheung Tam. The paper was published in the Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 2: Short Papers), pages 699–710, in Mexico City, Mexico.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "6b3f895c-2fb6-4626-be9f-12c30c2415f7",
  "tool_use_result": {
    "query": "\"Arithmetic Reasoning with LLM Prolog Generation Permutation\" NAACL 2024 authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LqdrMdrwuCGxLKap1L1ozG",
        "content": [
          {
            "title": "Arithmetic Reasoning with LLM: Prolog Generation & Permutation - ACL Anthology",
            "url": "https://aclanthology.org/2024.naacl-short.61/"
          },
          {
            "title": "Arithmetic Reasoning with LLM: Prolog Generation & ...",
            "url": "https://aclanthology.org/2024.naacl-short.61.pdf"
          },
          {
            "title": "[2405.17893] Arithmetic Reasoning with LLM: Prolog Generation & Permutation",
            "url": "https://arxiv.org/abs/2405.17893"
          },
          {
            "title": "Arithmetic Reasoning with LLM: Prolog Generation & Permutation",
            "url": "https://arxiv.org/html/2405.17893v1"
          },
          {
            "title": "Paper page - Arithmetic Reasoning with LLM: Prolog Generation & Permutation",
            "url": "https://huggingface.co/papers/2405.17893"
          },
          {
            "title": "Underline | Arithmetic Reasoning with LLM: Prolog Generation & Permutation",
            "url": "https://underline.io/lecture/97853-arithmetic-reasoning-with-llm-prolog-generation-and-permutation"
          },
          {
            "title": "(PDF) Arithmetic Reasoning with LLM: Prolog Generation & Permutation",
            "url": "https://www.researchgate.net/publication/380935097_Arithmetic_Reasoning_with_LLM_Prolog_Generation_Permutation"
          },
          {
            "title": "Arithmetic Reasoning with LLM: Prolog Generation & Permutation | alphaXiv",
            "url": "https://www.alphaxiv.org/abs/2405.17893"
          },
          {
            "title": "Arithmetic Reasoning with LLM: Prolog Generation & Permutation | PromptLayer",
            "url": "https://www.promptlayer.com/research-papers/arithmetic-reasoning-with-llm-prolog-generation-permutation"
          },
          {
            "title": "Arithmetic Reasoning with LLM: Prolog Generation & Permutation | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/arithmetic-reasoning-llm-prolog-generation-permutation"
          }
        ]
      },
      "Based on the search results, I found the paper \"Arithmetic Reasoning with LLM: Prolog Generation & Permutation\" from NAACL 2024. \n\nThe authors are Xiaocheng Yang, Bingsen Chen, and Yik-Cheung Tam. The paper was published in the Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 2: Short Papers), pages 699–710, in Mexico City, Mexico."
    ],
    "durationSeconds": 3.86159663
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T17:44:21.040Z_

<details><summary>↩ Tool result · `toolu_014dWCyXnGvapgb87muMg1Qu`</summary>

```text
Web search results for query: ""Thought-Like-Pro" "Prolog-based Chain-of-Thought" 2024 arxiv authors"

Links: [{"title":"[2407.14562] Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought","url":"https://arxiv.org/abs/2407.14562"},{"title":"Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Though","url":"https://arxiv.org/html/2407.14562v1"},{"title":"Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought","url":"https://arxiv.org/html/2407.14562"},{"title":"Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Though | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/thought-like-pro-enhancing-reasoning-large-language"},{"title":"𝜋-CoT: Prolog-Initialized Chain-of-Thought Prompting for Multi-Hop Question-Answering","url":"https://arxiv.org/html/2506.20642v2"},{"title":"Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Though","url":"https://www.researchgate.net/publication/382459991_Thought-Like-Pro_Enhancing_Reasoning_of_Large_Language_Models_through_Self-Driven_Prolog-based_Chain-of-Though"},{"title":"A Survey on LLM Symbolic Reasoning","url":"https://d197for5662m48.cloudfront.net/documents/publicationstatus/295282/preprint_pdf/17368bd9e5235ed8466977226241d74d.pdf"},{"title":"[2201.11903] Chain-of-Thought Prompting Elicits Reasoning in Large Language Models","url":"https://arxiv.org/abs/2201.11903"},{"title":"How does Chain of Thought Think? Mechanistic Interpretability of Chain-of-Thought Reasoning with Sparse Autoencoding","url":"https://arxiv.org/html/2507.22928v1"},{"title":"A Survey of Chain-of-X Paradigms for LLMs","url":"https://aclanthology.org/2025.coling-main.719.pdf"}]

Based on the search results, I found information about the "Thought-Like-Pro" paper:

The paper "Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought" was authored by Xiaoyu Tan and 10 other authors.

The full author list includes Xiaoyu Tan (INF Technology), Yongxin Deng (Shanghai University of Engineering Science), Xihe Qiu (Shanghai University of Engineering Science), Weidi Xu (INF Technology), Chao Qu (INF Technology), Wei Chu (INF Technology), Yinghui Xu (Fudan University), and Yuan Qi (Fudan University).

The paper was submitted on July 18, 2024, with a revised version on August 10, 2024, and it introduces a novel learning framework that utilizes imitation learning to imitate Chain-of-Thought processes verified and translated from reasoning trajectories generated by a symbolic Prolog logic engine, proceeding in a self-driven manner that enables LLMs to formulate rules and statements from given instructions and leverage the symbolic Prolog engine to derive results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "ce757357-8893-48f9-bcd2-462b9a400156",
  "tool_use_result": {
    "query": "\"Thought-Like-Pro\" \"Prolog-based Chain-of-Thought\" 2024 arxiv authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HkPcAaigvXQUPmFnieKHH9",
        "content": [
          {
            "title": "[2407.14562] Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought",
            "url": "https://arxiv.org/abs/2407.14562"
          },
          {
            "title": "Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Though",
            "url": "https://arxiv.org/html/2407.14562v1"
          },
          {
            "title": "Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought",
            "url": "https://arxiv.org/html/2407.14562"
          },
          {
            "title": "Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Though | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/thought-like-pro-enhancing-reasoning-large-language"
          },
          {
            "title": "𝜋-CoT: Prolog-Initialized Chain-of-Thought Prompting for Multi-Hop Question-Answering",
            "url": "https://arxiv.org/html/2506.20642v2"
          },
          {
            "title": "Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Though",
            "url": "https://www.researchgate.net/publication/382459991_Thought-Like-Pro_Enhancing_Reasoning_of_Large_Language_Models_through_Self-Driven_Prolog-based_Chain-of-Though"
          },
          {
            "title": "A Survey on LLM Symbolic Reasoning",
            "url": "https://d197for5662m48.cloudfront.net/documents/publicationstatus/295282/preprint_pdf/17368bd9e5235ed8466977226241d74d.pdf"
          },
          {
            "title": "[2201.11903] Chain-of-Thought Prompting Elicits Reasoning in Large Language Models",
            "url": "https://arxiv.org/abs/2201.11903"
          },
          {
            "title": "How does Chain of Thought Think? Mechanistic Interpretability of Chain-of-Thought Reasoning with Sparse Autoencoding",
            "url": "https://arxiv.org/html/2507.22928v1"
          },
          {
            "title": "A Survey of Chain-of-X Paradigms for LLMs",
            "url": "https://aclanthology.org/2025.coling-main.719.pdf"
          }
        ]
      },
      "Based on the search results, I found information about the \"Thought-Like-Pro\" paper:\n\nThe paper \"Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought\" was authored by Xiaoyu Tan and 10 other authors.\n\nThe full author list includes Xiaoyu Tan (INF Technology), Yongxin Deng (Shanghai University of Engineering Science), Xihe Qiu (Shanghai University of Engineering Science), Weidi Xu (INF Technology), Chao Qu (INF Technology), Wei Chu (INF Technology), Yinghui Xu (Fudan University), and Yuan Qi (Fudan University).\n\nThe paper was submitted on July 18, 2024, with a revised version on August 10, 2024, and it introduces a novel learning framework that utilizes imitation learning to imitate Chain-of-Thought processes verified and translated from reasoning trajectories generated by a symbolic Prolog logic engine, proceeding in a self-driven manner that enables LLMs to formulate rules and statements from given instructions and leverage the symbolic Prolog engine to derive results."
    ],
    "durationSeconds": 6.486655386999992
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-14T17:44:24.377Z_

<details><summary>↩ Tool result · `toolu_01TxgaGRvEs1od1cZyAzN9QY`</summary>

```text
Web search results for query: ""Do LLMs Game Formalization" "Evaluating Faithfulness" logical reasoning 2604.19459 arxiv"

Links: [{"title":"[2604.19459] Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning","url":"https://arxiv.org/abs/2604.19459"},{"title":"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning","url":"https://arxiv.org/html/2604.19459"},{"title":"Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing","url":"https://arxiv.org/html/2604.08401"},{"title":"LogicPuzzleRL: Cultivating Robust Mathematical Reasoning in LLMs via Reinforcement Learning","url":"https://arxiv.org/html/2506.04821v1"},{"title":"Preprint TRAINING LLMS WITH LOGICREWARD FOR FAITHFUL AND RIGOROUS REASONING","url":"https://arxiv.org/pdf/2512.18196"},{"title":"Reasoning Capabilities of Large Language Models. Lessons Learned from General Game Playing","url":"https://arxiv.org/html/2602.19160"},{"title":"GTBench: Uncovering the Strategic Reasoning Limitations of LLMs via Game-Theoretic Evaluations","url":"https://arxiv.org/html/2402.12348v2"},{"title":"LogicGame: Benchmarking Rule-Based Reasoning Abilities of Large Language Models","url":"https://arxiv.org/html/2408.15778v1"},{"title":"Training LLMs with LogicReward for Faithful and Rigorous Reasoning","url":"https://arxiv.org/html/2512.18196v1"},{"title":"Tracing LLM Reasoning Processes with Strategic Games: A Framework for Planning, Revision, and Resource-Constrained Decision Making","url":"https://arxiv.org/html/2506.12012v1"}]

I found the paper you were searching for. Here are the key details:

## Paper Information

The paper is titled "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning", with arXiv ID 2604.19459.

## Main Findings

The paper addresses a gap between formal verification validity and formalization faithfulness. For natural-language logical reasoning where models construct axiom systems from scratch without library constraints, this gap between valid proofs and faithful translations is especially acute.

The researchers investigate whether frontier models exploit this gap when generating Lean 4 proofs (termed "formalization gaming"), evaluating GPT-5 and DeepSeek-R1 on 303 first-order logic problems (203 from FOLIO, 100 from Multi-LogiEval), comparing unified generation against a two-stage pipeline that separates formalization from proving.

## Key Results

Despite compilation rates of 87-99%, the researchers find no evidence of systematic gaming in unified generation: models prefer reporting failure over forcing proofs, even under prompting designed to encourage it.

However, the two-stage pipeline reveals two distinct modes of unfaithfulness: GPT-5 fabricates axioms during proof generation, a reactive fallback detectable via cross-stage comparison, while DeepSeek-R1 mistranslates premises during formalization, producing internally consistent outputs that evade detection entirely.

These findings show that high compilation rates or accuracies should not be equated with faithful reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "856371fa-6624-4f79-852d-95131b0e9a6d",
  "tool_use_result": {
    "query": "\"Do LLMs Game Formalization\" \"Evaluating Faithfulness\" logical reasoning 2604.19459 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XqGqy7nvvq3U3gmj79f3ae",
        "content": [
          {
            "title": "[2604.19459] Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning",
            "url": "https://arxiv.org/abs/2604.19459"
          },
          {
            "title": "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning",
            "url": "https://arxiv.org/html/2604.19459"
          },
          {
            "title": "Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing",
            "url": "https://arxiv.org/html/2604.08401"
          },
          {
            "title": "LogicPuzzleRL: Cultivating Robust Mathematical Reasoning in LLMs via Reinforcement Learning",
            "url": "https://arxiv.org/html/2506.04821v1"
          },
          {
            "title": "Preprint TRAINING LLMS WITH LOGICREWARD FOR FAITHFUL AND RIGOROUS REASONING",
            "url": "https://arxiv.org/pdf/2512.18196"
          },
          {
            "title": "Reasoning Capabilities of Large Language Models. Lessons Learned from General Game Playing",
            "url": "https://arxiv.org/html/2602.19160"
          },
          {
            "title": "GTBench: Uncovering the Strategic Reasoning Limitations of LLMs via Game-Theoretic Evaluations",
            "url": "https://arxiv.org/html/2402.12348v2"
          },
          {
            "title": "LogicGame: Benchmarking Rule-Based Reasoning Abilities of Large Language Models",
            "url": "https://arxiv.org/html/2408.15778v1"
          },
          {
            "title": "Training LLMs with LogicReward for Faithful and Rigorous Reasoning",
            "url": "https://arxiv.org/html/2512.18196v1"
          },
          {
            "title": "Tracing LLM Reasoning Processes with Strategic Games: A Framework for Planning, Revision, and Resource-Constrained Decision Making",
            "url": "https://arxiv.org/html/2506.12012v1"
          }
        ]
      },
      "I found the paper you were searching for. Here are the key details:\n\n## Paper Information\n\nThe paper is titled \"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning\", with arXiv ID 2604.19459.\n\n## Main Findings\n\nThe paper addresses a gap between formal verification validity and formalization faithfulness. For natural-language logical reasoning where models construct axiom systems from scratch without library constraints, this gap between valid proofs and faithful translations is especially acute.\n\nThe researchers investigate whether frontier models exploit this gap when generating Lean 4 proofs (termed \"formalization gaming\"), evaluating GPT-5 and DeepSeek-R1 on 303 first-order logic problems (203 from FOLIO, 100 from Multi-LogiEval), comparing unified generation against a two-stage pipeline that separates formalization from proving.\n\n## Key Results\n\nDespite compilation rates of 87-99%, the researchers find no evidence of systematic gaming in unified generation: models prefer reporting failure over forcing proofs, even under prompting designed to encourage it.\n\nHowever, the two-stage pipeline reveals two distinct modes of unfaithfulness: GPT-5 fabricates axioms during proof generation, a reactive fallback detectable via cross-stage comparison, while DeepSeek-R1 mistranslates premises during formalization, producing internally consistent outputs that evade detection entirely.\n\nThese findings show that high compilation rates or accuracies should not be equated with faithful reasoning."
    ],
    "durationSeconds": 9.911026702999996
  }
}
```

</details>

---

### Assistant

_source line 42_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clearer picture. Let me also look for one more paper that showed up: "Do LLMs Game Formalization?" (2604.19459) — this is EXTREMELY relevant to STA because it directly studies whether LLMs "game" formalization, which is essentially what STA's ISR metric tries to detect. Let me get more author info.

Also let me search for the Krakovna et al. 2020 blog post reference more formally — it's a blog post, not a paper, but it's widely cited.

Let me now also think about what to actually add. The task says 2-3 papers per area if missing.
 
Now I'm reviewing what's already covered in the Prolog and logic programming section with GRPO and RL approaches — there are six papers already included spanning GRPO with Prolog, reinforcement learning with logic, SAT solvers, first-order logic provers, and symbolic solvers combined with LLM prompting. I'm checking what might still be missing, starting with DeepProbLog.

Actually, I'm reconsidering the relevance here. DeepProbLog and NeurASP are more about embedding neural networks into logic programming systems rather than using RL to train language models to generate Prolog code, so they're not as aligned with the symbolic trajectory approach. The more directly relevant papers would be Thought-Like-Pro, which uses a Prolog engine to generate reasoning trajectories for training LLMs, and the Yang et al. 2024 work on Prolog generation for arithmetic reasoning.

I should also reconsider where "Do LLMs Game Formalization?" fits — it's actually more relevant to the reward-hacking and Goodhart's law category since it's studying how LLMs exploit formalization rather than genuinely reasoning with it.

For the neuro-symbolic logic programming section, I'm realizing I need to include foundational work like DeepProbLog and NeurASP alongside more recent papers like Thought-Like-Pro that directly apply Prolog to LLM training.

Now I'm checking the specification gaming literature — Bondarenko et al. 2025 and the formalization gaming paper are both directly applicable, though I should verify whether the Krakovna blog post is appropriate for a formal literature map.

Let me do another search to confirm author details and catch any other critical papers I might have missed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "257ca7ff-f12d-499d-bc1d-fd4ed3346309",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ShcVrXPcsSkHjPazTuVLSQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1669,
      "cache_creation_input_tokens": 1329,
      "cache_read_input_tokens": 50007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1329
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VnyxEfZ3iTkMRE4EXyoY7K`</summary>

```json
{
  "query": "\"Do LLMs Game Formalization\" arxiv 2604.19459 authors FOLIO Lean"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "7f6eee40-ae62-4041-9bc3-936bf9272ec8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ShcVrXPcsSkHjPazTuVLSQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1669,
      "cache_creation_input_tokens": 1329,
      "cache_read_input_tokens": 50007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1329
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_015hft1ey7YK15H2yu8Mx6j4`</summary>

```json
{
  "query": "Manhaeve Dumancic Kimmig Demeester De Raedt \"DeepProbLog\" 2021 \"Artificial Intelligence\" journal volume"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "27aecce9-797d-4df7-9254-4f6b42e91f65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ShcVrXPcsSkHjPazTuVLSQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1669,
      "cache_creation_input_tokens": 1329,
      "cache_read_input_tokens": 50007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1329
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

_source line 45 · 2026-05-14T17:44:51.792Z_

<details><summary>↩ Tool result · `toolu_015hft1ey7YK15H2yu8Mx6j4`</summary>

```text
Web search results for query: "Manhaeve Dumancic Kimmig Demeester De Raedt "DeepProbLog" 2021 "Artificial Intelligence" journal volume"

Links: [{"title":"Neural probabilistic logic programming in DeepProbLog","url":"https://biblio.ugent.be/publication/8721037"},{"title":"[1805.10872] DeepProbLog: Neural Probabilistic Logic Programming","url":"https://arxiv.org/abs/1805.10872"},{"title":"Robin Manhaeve, Sebastijan Dumančić, Angelika Kimmig, Thomas Demeester & Luc De Raedt, Neural probabilistic logic programming in DeepProbLog - PhilPapers","url":"https://philpapers.org/rec/MANNPL"},{"title":"[PDF] DeepProbLog: Neural Probabilistic Logic Programming | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DeepProbLog:-Neural-Probabilistic-Logic-Programming-Manhaeve-Dumancic/f6e6fba61b654c5b799a9efe3b5849ce1197aab3"},{"title":"DeepProbLog | Proceedings of the 32nd International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3327144.3327291"},{"title":"[1907.08194] Neural Probabilistic Logic Programming in DeepProbLog","url":"https://arxiv.org/abs/1907.08194"},{"title":"publications | Sebastijan Dumancic","url":"https://sebdumancic.github.io/publications/"},{"title":"dblp: Neural probabilistic logic programming in DeepProbLog.","url":"https://dblp.org/rec/journals/ai/ManhaeveDKDR21.html"},{"title":"Angelika Kimmig, Guy Van den Broeck & Luc De Raedt, Algebraic model counting - PhilPapers","url":"https://philpapers.org/rec/KIMAMC"},{"title":"(Open Access) Neural probabilistic logic programming in DeepProbLog (2021) | Robin Manhaeve | 158 Citations","url":"https://scispace.com/papers/neural-probabilistic-logic-programming-in-deepproblog-x2gdjqjbs3"}]

Based on the search results, I found the information about the paper you requested:

The paper "Neural Probabilistic Logic Programming in DeepProbLog" was published in the *Artificial Intelligence* journal, volume 298 in 2021. The authors are Robin Manhaeve, Sebastijan Dumančić, Angelika Kimmig, Thomas Demeester, and Luc De Raedt.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "4103b2df-8c79-4616-bf2e-0f047c8e2cae",
  "tool_use_result": {
    "query": "Manhaeve Dumancic Kimmig Demeester De Raedt \"DeepProbLog\" 2021 \"Artificial Intelligence\" journal volume",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QA1pZGLJY9pwvuKdxPLPoH",
        "content": [
          {
            "title": "Neural probabilistic logic programming in DeepProbLog",
            "url": "https://biblio.ugent.be/publication/8721037"
          },
          {
            "title": "[1805.10872] DeepProbLog: Neural Probabilistic Logic Programming",
            "url": "https://arxiv.org/abs/1805.10872"
          },
          {
            "title": "Robin Manhaeve, Sebastijan Dumančić, Angelika Kimmig, Thomas Demeester & Luc De Raedt, Neural probabilistic logic programming in DeepProbLog - PhilPapers",
            "url": "https://philpapers.org/rec/MANNPL"
          },
          {
            "title": "[PDF] DeepProbLog: Neural Probabilistic Logic Programming | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/DeepProbLog:-Neural-Probabilistic-Logic-Programming-Manhaeve-Dumancic/f6e6fba61b654c5b799a9efe3b5849ce1197aab3"
          },
          {
            "title": "DeepProbLog | Proceedings of the 32nd International Conference on Neural Information Processing Systems",
            "url": "https://dl.acm.org/doi/10.5555/3327144.3327291"
          },
          {
            "title": "[1907.08194] Neural Probabilistic Logic Programming in DeepProbLog",
            "url": "https://arxiv.org/abs/1907.08194"
          },
          {
            "title": "publications | Sebastijan Dumancic",
            "url": "https://sebdumancic.github.io/publications/"
          },
          {
            "title": "dblp: Neural probabilistic logic programming in DeepProbLog.",
            "url": "https://dblp.org/rec/journals/ai/ManhaeveDKDR21.html"
          },
          {
            "title": "Angelika Kimmig, Guy Van den Broeck & Luc De Raedt, Algebraic model counting - PhilPapers",
            "url": "https://philpapers.org/rec/KIMAMC"
          },
          {
            "title": "(Open Access) Neural probabilistic logic programming in DeepProbLog (2021) | Robin Manhaeve | 158 Citations",
            "url": "https://scispace.com/papers/neural-probabilistic-logic-programming-in-deepproblog-x2gdjqjbs3"
          }
        ]
      },
      "Based on the search results, I found the information about the paper you requested:\n\nThe paper \"Neural Probabilistic Logic Programming in DeepProbLog\" was published in the *Artificial Intelligence* journal, volume 298 in 2021. The authors are Robin Manhaeve, Sebastijan Dumančić, Angelika Kimmig, Thomas Demeester, and Luc De Raedt."
    ],
    "durationSeconds": 4.773913033000005
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T17:44:54.726Z_

<details><summary>↩ Tool result · `toolu_01VnyxEfZ3iTkMRE4EXyoY7K`</summary>

```text
Web search results for query: ""Do LLMs Game Formalization" arxiv 2604.19459 authors FOLIO Lean"

Links: [{"title":"[2604.19459] Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning","url":"https://arxiv.org/abs/2604.19459"},{"title":"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning","url":"https://arxiv.org/html/2604.19459"},{"title":"Published at the VerifAI-2 Workshop, ICLR 2026 DO LLMS GAME FORMALIZATION?","url":"https://arxiv.org/pdf/2604.19459"},{"title":"LeanReasoner: Boosting Complex Logical Reasoning with Lean","url":"https://arxiv.org/html/2403.13312"},{"title":"Formalization of De Giorgi–Nash–Moser Theory in Lean","url":"https://arxiv.org/html/2604.05984"},{"title":"\\capsysname: How Good are LLMs at Playing Games?","url":"https://arxiv.org/html/2505.15146v1"},{"title":"[2509.22338] Advancing Natural Language Formalization to First Order Logic with Fine-tuned LLMs","url":"https://arxiv.org/abs/2509.22338"},{"title":"Game Theory Meets Large Language Models: A Systematic Survey with Taxonomy and New Frontiers","url":"https://arxiv.org/html/2502.09053v2"},{"title":"Optimal strategies in the all-heads coin game","url":"https://arxiv.org/html/2604.22991"},{"title":"Evaluating LLMs in Open-Source Games Swadesh Sistla University of Washington","url":"https://www.arxiv.org/pdf/2512.00371"}]

Based on the web search results, here's information about the paper:

## "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning"

**ArXiv ID:** 2604.19459

**Authors:** Kyuhee Kim, Auguste Poiroux, Antoine Bosselut

**Overview:** The paper investigates whether frontier models exploit a gap between valid proofs and faithful translations when generating Lean 4 proofs, a behavior termed formalization gaming.

**Datasets and Models:** The authors evaluate GPT-5 and DeepSeek-R1 on 303 first-order logic problems (203 from FOLIO, 100 from Multi-LogiEval), comparing unified generation against a two-stage pipeline that separates formalization from proving.

**Key Findings:** Despite compilation rates of 87-99%, the study finds no evidence of systematic gaming in unified generation: models prefer reporting failure over forcing proofs, even under prompting designed to encourage it.

**Venue:** The paper was published at the VerifAI-2 Workshop, ICLR 2026

The paper addresses an important distinction between formal verification (which guarantees proof validity) and formalization faithfulness (whether the formal representation accurately captures the original natural language problem).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "04022686-bd07-4d02-8aae-27174e15656b",
  "tool_use_result": {
    "query": "\"Do LLMs Game Formalization\" arxiv 2604.19459 authors FOLIO Lean",
    "results": [
      {
        "tool_use_id": "srvtoolu_018VD23VhspW4y6MuLnE72BS",
        "content": [
          {
            "title": "[2604.19459] Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning",
            "url": "https://arxiv.org/abs/2604.19459"
          },
          {
            "title": "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning",
            "url": "https://arxiv.org/html/2604.19459"
          },
          {
            "title": "Published at the VerifAI-2 Workshop, ICLR 2026 DO LLMS GAME FORMALIZATION?",
            "url": "https://arxiv.org/pdf/2604.19459"
          },
          {
            "title": "LeanReasoner: Boosting Complex Logical Reasoning with Lean",
            "url": "https://arxiv.org/html/2403.13312"
          },
          {
            "title": "Formalization of De Giorgi–Nash–Moser Theory in Lean",
            "url": "https://arxiv.org/html/2604.05984"
          },
          {
            "title": "\\capsysname: How Good are LLMs at Playing Games?",
            "url": "https://arxiv.org/html/2505.15146v1"
          },
          {
            "title": "[2509.22338] Advancing Natural Language Formalization to First Order Logic with Fine-tuned LLMs",
            "url": "https://arxiv.org/abs/2509.22338"
          },
          {
            "title": "Game Theory Meets Large Language Models: A Systematic Survey with Taxonomy and New Frontiers",
            "url": "https://arxiv.org/html/2502.09053v2"
          },
          {
            "title": "Optimal strategies in the all-heads coin game",
            "url": "https://arxiv.org/html/2604.22991"
          },
          {
            "title": "Evaluating LLMs in Open-Source Games Swadesh Sistla University of Washington",
            "url": "https://www.arxiv.org/pdf/2512.00371"
          }
        ]
      },
      "Based on the web search results, here's information about the paper:\n\n## \"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning\"\n\n**ArXiv ID:** 2604.19459\n\n**Authors:** Kyuhee Kim, Auguste Poiroux, Antoine Bosselut\n\n**Overview:** The paper investigates whether frontier models exploit a gap between valid proofs and faithful translations when generating Lean 4 proofs, a behavior termed formalization gaming.\n\n**Datasets and Models:** The authors evaluate GPT-5 and DeepSeek-R1 on 303 first-order logic problems (203 from FOLIO, 100 from Multi-LogiEval), comparing unified generation against a two-stage pipeline that separates formalization from proving.\n\n**Key Findings:** Despite compilation rates of 87-99%, the study finds no evidence of systematic gaming in unified generation: models prefer reporting failure over forcing proofs, even under prompting designed to encourage it.\n\n**Venue:** The paper was published at the VerifAI-2 Workshop, ICLR 2026\n\nThe paper addresses an important distinction between formal verification (which guarantees proof validity) and formalization faithfulness (whether the formal representation accurately captures the original natural language problem)."
    ],
    "durationSeconds": 7.714379218000002
  }
}
```

</details>

---

### Assistant

_source line 47_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information. Let me summarize my findings and determine what to add:

### (a) Prolog/Logic Programming + GRPO/RL

Current coverage is decent but missing some foundational neuro-symbolic LP papers. Papers to add:

1. **DeepProbLog** (Manhaeve et al., 2021, AIJ vol.298) — Foundational neural-probabilistic logic programming. Background for why neural+LP integration works.
   - Authors: Robin Manhaeve, Sebastijan Dumančić, Angelika Kimmig, Thomas Demeester, Luc De Raedt
   - Venue: Artificial Intelligence 298, 2021

2. **NeurASP** (Yang, Ishay, Lee, 2020, IJCAI) — Neural answer set programming combining neural networks with answer set programming for reasoning tasks.
   - Authors: Zhun Yang, Adam Ishay, Joohyung Lee
   - Venue: IJCAI 2020, pages 1755-1762

3. **Thought-Like-Pro** (Tan et al., 2024, arXiv 2407.14562) — Uses Prolog-based chain-of-thought reasoning to improve LLM reasoning through imitation learning.
   - Authors: Xiaoyu Tan, Yongxin Deng, Xihe Qiu, et al.
   - Venue: arXiv 2407.14562

I'm realizing that DeepProbLog and NeurASP are fundamentally about embedding neural networks into logic programming systems, which is different from what STA does. STA is about having LLMs generate Prolog code directly. That said, they're part of the same neuro-symbolic tradition that provides useful context. Thought-Like-Pro is more directly comparable since it also uses Prolog reasoning trajectories to train language models, though through imitation learning rather than reinforcement learning. For mapping out the landscape of Prolog and logic programming combined with LLMs and learning approaches, I should focus on Thought-Like-Pro as the most relevant reference, along with any recent work on LLMs generating Prolog for reasoning tasks.

For Goodhart's Law, I'm adding two recent papers that directly address how reasoning models exploit benchmarks through specification gaming, and another that specifically examines whether LLMs game the formalization process in logical reasoning tasks.

The mutation testing section is already thorough with historical foundations and modern applications, so no changes needed there.

Preparing the updated YAML now...

Wait, I need to verify that `save_project_file` can actually write to `literature_map.yaml`. The tool only allows writing to memory.md, writing_plan.yaml, and paper_framing.md, with other files having dedicated tools. Since literature_map.yaml isn't listed as writable and doesn't have a dedicated tool mentioned, I should attempt the save and see if it works or if I need a different approach.

Let me try using the MCP tool first, and if that doesn't work, I'll write directly to the file. Before I make any changes, I should read the current file so I can properly merge in the new entries.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "53559764-1248-4e45-baf0-f5352620ad14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JsgT5HEThSVpMVUgLvNs1F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 731,
      "cache_creation_input_tokens": 3471,
      "cache_read_input_tokens": 51336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3471
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

_source line 48_

Coverage assessment complete. Now let me read the file directly to make edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "5088314c-e700-4cac-824b-065821e8e80d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JsgT5HEThSVpMVUgLvNs1F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 731,
      "cache_creation_input_tokens": 3471,
      "cache_read_input_tokens": 51336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3471
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

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_016sfKQGYHPvdy2uWWww3yAX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
  "offset": 0,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "c09e2d0a-eb96-4d3e-ac6b-e70461e46eac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JsgT5HEThSVpMVUgLvNs1F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 731,
      "cache_creation_input_tokens": 3471,
      "cache_read_input_tokens": 51336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3471
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

_source line 50 · 2026-05-14T17:45:19.075Z_

<details><summary>↩ Tool result · `toolu_016sfKQGYHPvdy2uWWww3yAX`</summary>

```text
0	# Literature Map for Solver Trace Ablation (STA)
1	# Categories:
2	#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO
3	#   2. reward-shaping: Reward shaping for code/formal verification
4	#   3. mutation-testing: Mutation testing in software engineering
5	#   4. intensional-analysis: Intensional program analysis
6	#   5. reward-hacking: Reward hacking / overoptimization
7	#   6. fol-formalization: FOL/Prolog formalization with LLMs
8	#   7. goodhart-overoptimization: Goodhart's Law theory and dose-response dynamics
9	#   8. verification-reward: Solver/prover as RL reward signal
10	
11	papers:
12	
13	  # ============================================================
14	  # Category 1: Neurosymbolic reasoning + RL/GRPO
15	  # ============================================================
16	
17	  - id: deepseek-r1
18	    title: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
19	    authors: "DeepSeek-AI"
20	    year: 2025
21	    venue: "arXiv 2501.12948 / Nature 2025"
22	    category: neurosymbolic-rl
23	    role: method-component
24	    relevance: >
25	      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.
26	      STA builds on the same GRPO framework but replaces binary outcome reward with
27	      intensional structural reward for neurosymbolic formalization.
28	    key_finding: >
29	      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,
30	      showing emergent chain-of-thought reasoning from RL alone.
31	
32	  - id: deepseekmath
33	    title: "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models"
34	    authors: "Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al."
35	    year: 2024
36	    venue: "arXiv 2402.03300"
37	    category: neurosymbolic-rl
38	    role: method-component
39	    relevance: >
40	      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm
41	      used in STA training. GRPO eliminates the critic model by estimating
42	      baselines from group scores.
43	    key_finding: >
44	      GRPO matches PPO performance while significantly reducing training
45	      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.
46	
47	  - id: logic-rl
48	    title: "Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning"
49	    authors: "Xian et al."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "05396c05-0dc4-4a3d-874a-f0d78a513d46",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
      "content": "# Literature Map for Solver Trace Ablation (STA)\n# Categories:\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\n#   2. reward-shaping: Reward shaping for code/formal verification\n#   3. mutation-testing: Mutation testing in software engineering\n#   4. intensional-analysis: Intensional program analysis\n#   5. reward-hacking: Reward hacking / overoptimization\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\n#   7. goodhart-overoptimization: Goodhart's Law theory and dose-response dynamics\n#   8. verification-reward: Solver/prover as RL reward signal\n\npapers:\n\n  # ============================================================\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\n  # ============================================================\n\n  - id: deepseek-r1\n    title: \"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\"\n    authors: \"DeepSeek-AI\"\n    year: 2025\n    venue: \"arXiv 2501.12948 / Nature 2025\"\n    category: neurosymbolic-rl\n    role: method-component\n    relevance: >\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\n      STA builds on the same GRPO framework but replaces binary outcome reward with\n      intensional structural reward for neurosymbolic formalization.\n    key_finding: >\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\n      showing emergent chain-of-thought reasoning from RL alone.\n\n  - id: deepseekmath\n    title: \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\"\n    authors: \"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\"\n    year: 2024\n    venue: \"arXiv 2402.03300\"\n    category: neurosymbolic-rl\n    role: method-component\n    relevance: >\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\n      used in STA training. GRPO eliminates the critic model by estimating\n      baselines from group scores.\n    key_finding: >\n      GRPO matches PPO performance while significantly reducing training\n      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.\n\n  - id: logic-rl\n    title: \"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\"\n    authors: \"Xian et al.\"",
      "numLines": 50,
      "startLine": 0,
      "totalLines": 865
    }
  }
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_01G9RSHmndGwHJa278vHAFmc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
  "offset": 95,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "a780bac6-50b6-48c2-a5cb-896aea37a3a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RAa82bhaj7XbTsEb56fy1k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2757,
      "cache_read_input_tokens": 54807,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2757
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

_source line 52 · 2026-05-14T17:45:22.015Z_

<details><summary>↩ Tool result · `toolu_01G9RSHmndGwHJa278vHAFmc`</summary>

```text
95	  # Category 2: Reward shaping for code/formal verification
96	  # ============================================================
97	
98	  - id: lightman-verify-step
99	    title: "Let's Verify Step by Step"
100	    authors: "Hunter Lightman, Vineet Kosaraju, Yura Burda, et al."
101	    year: 2023
102	    venue: "arXiv 2305.20050 / ICLR 2024"
103	    category: reward-shaping
104	    role: method-component
105	    relevance: >
106	      Establishes that process supervision (step-level reward) outperforms
107	      outcome supervision (final-answer reward) for reasoning. STA's ISR
108	      is analogous: it provides structural process-level signal about which
109	      components of a formalization matter, rather than just pass/fail.
110	    key_finding: >
111	      Process-supervised reward model achieves 78% on MATH, significantly
112	      outperforming outcome-supervised models. Released PRM800K dataset.
113	
114	  - id: reward-shaping-rlhf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "587eda9a-c671-42a9-ae9a-dedc1b549cc9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
      "content": "  # Category 2: Reward shaping for code/formal verification\n  # ============================================================\n\n  - id: lightman-verify-step\n    title: \"Let's Verify Step by Step\"\n    authors: \"Hunter Lightman, Vineet Kosaraju, Yura Burda, et al.\"\n    year: 2023\n    venue: \"arXiv 2305.20050 / ICLR 2024\"\n    category: reward-shaping\n    role: method-component\n    relevance: >\n      Establishes that process supervision (step-level reward) outperforms\n      outcome supervision (final-answer reward) for reasoning. STA's ISR\n      is analogous: it provides structural process-level signal about which\n      components of a formalization matter, rather than just pass/fail.\n    key_finding: >\n      Process-supervised reward model achieves 78% on MATH, significantly\n      outperforming outcome-supervised models. Released PRM800K dataset.\n\n  - id: reward-shaping-rlhf",
      "numLines": 20,
      "startLine": 95,
      "totalLines": 865
    }
  }
}
```

</details>

---

### Assistant

_source line 53_

Now I'll add the new papers. Let me add them to the appropriate sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "70f020d9-618e-48b2-9871-86fffbb9091d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0117Xe5w7Ynjb65shdNV4Vmb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 524,
      "cache_read_input_tokens": 57564,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 524
      },
      "output_tokens": 3,
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

<details open><summary>🔧 Tool call — Edit · `toolu_01Xwq4capg8i7T1xk2YNdcvy`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
  "old_string": "  # ============================================================\n  # Category 2: Reward shaping for code/formal verification\n  # ============================================================",
  "new_string": "  - id: deepproblog\n    title: \"Neural Probabilistic Logic Programming in DeepProbLog\"\n    authors: \"Robin Manhaeve, Sebastijan Dumančić, Angelika Kimmig, Thomas Demeester, Luc De Raedt\"\n    year: 2021\n    venue: \"Artificial Intelligence 298\"\n    category: neurosymbolic-rl\n    role: background\n    relevance: >\n      Foundational neural-probabilistic logic programming framework that integrates\n      deep learning with ProbLog via neural predicates. Establishes the intellectual\n      tradition of combining neural networks with logic programming that STA extends\n      to LLM-generated Prolog with RL training.\n    key_finding: >\n      End-to-end differentiable framework integrating neural perception with\n      probabilistic logical reasoning; supports program induction and learning\n      from examples.\n\n  - id: neurasp\n    title: \"NeurASP: Embracing Neural Networks into Answer Set Programming\"\n    authors: \"Zhun Yang, Adam Ishay, Joohyung Lee\"\n    year: 2020\n    venue: \"IJCAI 2020\"\n    category: neurosymbolic-rl\n    role: background\n    relevance: >\n      Integrates neural networks with answer set programming (ASP), using\n      ASP rules to constrain and improve neural network training. Complementary\n      to DeepProbLog; together they represent the neuro-symbolic LP foundation\n      that STA's LLM-to-Prolog pipeline builds upon.\n    key_finding: >\n      ASP semantic constraints improve neural network perception accuracy;\n      demonstrates bidirectional benefit of neural-symbolic integration.\n\n  - id: thought-like-pro\n    title: \"Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought\"\n    authors: \"Xiaoyu Tan, Yongxin Deng, Xihe Qiu, Weidi Xu, Chao Qu, Wei Chu, Yinghui Xu, Yuan Qi\"\n    year: 2024\n    venue: \"arXiv 2407.14562\"\n    category: neurosymbolic-rl\n    role: direct-competitor\n    relevance: >\n      Uses Prolog engine to generate verified reasoning trajectories, then trains\n      LLMs via imitation learning to replicate them. Directly comparable pipeline\n      to STA (Prolog verification + LLM training), but uses imitation learning\n      instead of GRPO with structural reward.\n    key_finding: >\n      Prolog-verified reasoning trajectories as training signal improve LLM\n      logical reasoning; self-driven framework enables LLMs to formulate\n      rules from instructions and leverage Prolog for derivation.\n\n  # ============================================================\n  # Category 2: Reward shaping for code/formal verification\n  # ============================================================"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "9aedf9a6-4037-475b-a901-bac56e73c788",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0117Xe5w7Ynjb65shdNV4Vmb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 524,
      "cache_read_input_tokens": 57564,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 524
      },
      "output_tokens": 3,
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

_source line 55 · 2026-05-14T17:45:36.909Z_

<details><summary>↩ Tool result · `toolu_01Xwq4capg8i7T1xk2YNdcvy`</summary>

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
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "bd5fe252-30da-4379-a8d8-ee1d6c2763f9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
    "oldString": "  # ============================================================\n  # Category 2: Reward shaping for code/formal verification\n  # ============================================================",
    "newString": "  - id: deepproblog\n    title: \"Neural Probabilistic Logic Programming in DeepProbLog\"\n    authors: \"Robin Manhaeve, Sebastijan Dumančić, Angelika Kimmig, Thomas Demeester, Luc De Raedt\"\n    year: 2021\n    venue: \"Artificial Intelligence 298\"\n    category: neurosymbolic-rl\n    role: background\n    relevance: >\n      Foundational neural-probabilistic logic programming framework that integrates\n      deep learning with ProbLog via neural predicates. Establishes the intellectual\n      tradition of combining neural networks with logic programming that STA extends\n      to LLM-generated Prolog with RL training.\n    key_finding: >\n      End-to-end differentiable framework integrating neural perception with\n      probabilistic logical reasoning; supports program induction and learning\n      from examples.\n\n  - id: neurasp\n    title: \"NeurASP: Embracing Neural Networks into Answer Set Programming\"\n    authors: \"Zhun Yang, Adam Ishay, Joohyung Lee\"\n    year: 2020\n    venue: \"IJCAI 2020\"\n    category: neurosymbolic-rl\n    role: background\n    relevance: >\n      Integrates neural networks with answer set programming (ASP), using\n      ASP rules to constrain and improve neural network training. Complementary\n      to DeepProbLog; together they represent the neuro-symbolic LP foundation\n      that STA's LLM-to-Prolog pipeline builds upon.\n    key_finding: >\n      ASP semantic constraints improve neural network perception accuracy;\n      demonstrates bidirectional benefit of neural-symbolic integration.\n\n  - id: thought-like-pro\n    title: \"Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought\"\n    authors: \"Xiaoyu Tan, Yongxin Deng, Xihe Qiu, Weidi Xu, Chao Qu, Wei Chu, Yinghui Xu, Yuan Qi\"\n    year: 2024\n    venue: \"arXiv 2407.14562\"\n    category: neurosymbolic-rl\n    role: direct-competitor\n    relevance: >\n      Uses Prolog engine to generate verified reasoning trajectories, then trains\n      LLMs via imitation learning to replicate them. Directly comparable pipeline\n      to STA (Prolog verification + LLM training), but uses imitation learning\n      instead of GRPO with structural reward.\n    key_finding: >\n      Prolog-verified reasoning trajectories as training signal improve LLM\n      logical reasoning; self-driven framework enables LLMs to formulate\n      rules from instructions and leverage Prolog for derivation.\n\n  # ============================================================\n  # Category 2: Reward shaping for code/formal verification\n  # ============================================================",
    "originalFile": "# Literature Map for Solver Trace Ablation (STA)\n# Categories:\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\n#   2. reward-shaping: Reward shaping for code/formal verification\n#   3. mutation-testing: Mutation testing in software engineering\n#   4. intensional-analysis: Intensional program analysis\n#   5. reward-hacking: Reward hacking / overoptimization\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\n#   7. goodhart-overoptimization: Goodhart's Law theory and dose-response dynamics\n#   8. verification-reward: Solver/prover as RL reward signal\n\npapers:\n\n  # ============================================================\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\n  # ============================================================\n\n  - id: deepseek-r1\n    title: \"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\"\n    authors: \"DeepSeek-AI\"\n    year: 2025\n    venue: \"arXiv 2501.12948 / Nature 2025\"\n    category: neurosymbolic-rl\n    role: method-component\n    relevance: >\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\n      STA builds on the same GRPO framework but replaces binary outcome reward with\n      intensional structural reward for neurosymbolic formalization.\n    key_finding: >\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\n      showing emergent chain-of-thought reasoning from RL alone.\n\n  - id: deepseekmath\n    title: \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\"\n    authors: \"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\"\n    year: 2024\n    venue: \"arXiv 2402.03300\"\n    category: neurosymbolic-rl\n    role: method-component\n    relevance: >\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\n      used in STA training. GRPO eliminates the critic model by estimating\n      baselines from group scores.\n    key_finding: >\n      GRPO matches PPO performance while significantly reducing training\n      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.\n\n  - id: logic-rl\n    title: \"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\"\n    authors: \"Xian et al.\"\n    year: 2025\n    venue: \"arXiv 2502.14768\"\n    category: neurosymbolic-rl\n    role: direct-competitor\n    relevance: >\n      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic\n      logic puzzles. Closest competitor to STA's approach of RL for logical\n      formalization, though Logic-RL uses extensional (answer-correctness)\n      rewards rather than STA's intensional structural rewards.\n    key_finding: >\n      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;\n      rule-based reward design is critical for RL-based logical reasoning.\n\n  - id: mellgren-prolog-grpo\n    title: \"Training Language Models to Use Prolog as a Tool\"\n    authors: \"Niklas Mellgren\"\n    year: 2024\n    venue: \"arXiv 2512.07407\"\n    category: neurosymbolic-rl\n    role: direct-competitor\n    relevance: >\n      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,\n      directly comparable to STA's approach of GRPO-training a formalizer.\n      Key difference: uses pass/fail reward vs STA's structural ISR.\n    key_finding: >\n      GRPO is effective for teaching small LLMs to use Prolog as a tool\n      for logical and mathematical reasoning.\n\n  - id: satlm\n    title: \"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\"\n    authors: \"Xi Ye et al.\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    category: neurosymbolic-rl\n    role: background\n    relevance: >\n      Neurosymbolic approach where LLM generates declarative specifications\n      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)\n      but uses prompting, not RL training.\n    key_finding: >\n      Declarative formulation outperforms imperative program-aided LMs by 23%\n      on GSM; achieves SoTA on LSAT and BoardgameQA.\n\n  # ============================================================\n  # Category 2: Reward shaping for code/formal verification\n  # ============================================================\n\n  - id: lightman-verify-step\n    title: \"Let's Verify Step by Step\"\n    authors: \"Hunter Lightman, Vineet Kosaraju, Yura Burda, et al.\"\n    year: 2023\n    venue: \"arXiv 2305.20050 / ICLR 2024\"\n    category: reward-shaping\n    role: method-component\n    relevance: >\n      Establishes that process supervision (step-level reward) outperforms\n      outcome supervision (final-answer reward) for reasoning. STA's ISR\n      is analogous: it provides structural process-level signal about which\n      components of a formalization matter, rather than just pass/fail.\n    key_finding: >\n      Process-supervised reward model achieves 78% on MATH, significantly\n      outperforming outcome-supervised models. Released PRM800K dataset.\n\n  - id: reward-shaping-rlhf\n    title: \"Reward Shaping to Mitigate Reward Hacking in RLHF\"\n    authors: \"Jiayi Fu, Xuandong Zhao, Chengyuan Yao, et al.\"\n    year: 2025\n    venue: \"arXiv 2502.18770\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Studies reward shaping design principles for RLHF: bounded rewards and\n      rapid-then-convergent growth. STA's ISR follows these principles\n      naturally since structural necessity scores are bounded [0,1].\n    key_finding: >\n      Two key reward shaping principles: (1) bounded RL reward, (2) rapid\n      initial growth with gradual convergence. PAR method achieves 5%+\n      win rate improvement on AlpacaEval 2.0.\n\n  - id: rlvr-reasoning\n    title: \"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs\"\n    authors: \"Various\"\n    year: 2025\n    venue: \"arXiv 2506.14245\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize\n      reasoning. STA argues that for neurosymbolic formalization, binary reward\n      is insufficient and structural reward is needed to avoid reward hacking.\n    key_finding: >\n      RLVR with binary verification implicitly teaches correct reasoning\n      strategies, not just answer matching.\n\n  - id: rubric-grpo\n    title: \"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning\"\n    authors: \"Various\"\n    year: 2025\n    venue: \"arXiv 2605.08061\"\n    category: reward-shaping\n    role: direct-competitor\n    relevance: >\n      Uses structured rubric-based rewards with GRPO, similar in spirit to\n      STA's structured ISR. Key difference: rubric rewards come from LLM\n      judges, while ISR comes from solver-based mutation testing.\n    key_finding: >\n      Structured multi-dimensional reward signals improve GRPO training\n      generalization compared to scalar rewards.\n\n  - id: gao-effective-rl-reward\n    title: \"On Designing Effective RL Reward at Training Time for LLM Reasoning\"\n    authors: \"Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu\"\n    year: 2024\n    venue: \"arXiv 2410.15115\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Demonstrates that learned process/outcome reward models can hurt RL\n      training, producing worse performance than simple success reward only.\n      Directly explains plan005 NEGATIVE: STA's ISR as auxiliary process\n      reward degrades prove_rate compared to exec-only baseline.\n    key_finding: >\n      PRM/ORM rewards may NOT help or even hurt RL training vs success-only\n      reward. Solution: Clipping and Delta techniques to bound accumulated\n      reward magnitude prevent reward hacking.\n\n  - id: prof-process-outcome\n    title: \"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training\"\n    authors: \"Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal\"\n    year: 2025\n    venue: \"arXiv 2509.03403\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Shows that naively combining PRM+ORM signals leads to performance\n      degradation. PROF consistency filter retains only PRM-ORM consistent\n      samples, achieving 4%+ improvement over blending. Suggests STA should\n      only apply ISR when consistent with execution outcome.\n    key_finding: >\n      Process rewards frequently suffer from inaccuracies and reward hacking\n      susceptibility. PROF filters training data by PRM-ORM consistency,\n      outperforming naive reward blending by 4%+ accuracy.\n\n  - id: moskovitz-constrained-rlhf\n    title: \"Confronting Reward Model Overoptimization with Constrained RLHF\"\n    authors: \"Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer\"\n    year: 2023\n    venue: \"arXiv 2310.04373 / ICLR 2024\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      First study on overoptimization in composite reward models. Shows that\n      fixed-weight linear scalarization of component rewards leads to\n      degradation past a threshold. Proposes constrained RL with dynamic\n      Lagrange multiplier weighting as alternative to fixed ISR weight.\n    key_finding: >\n      Correlation between component RMs significantly affects overoptimization\n      thresholds. Constrained RL with Lagrange multipliers outperforms\n      fixed-weight reward composition.\n\n  - id: skalse-reward-hacking\n    title: \"Defining and Characterizing Reward Hacking\"\n    authors: \"Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger\"\n    year: 2022\n    venue: \"arXiv 2209.13085 / NeurIPS 2022\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Formal proof that for stochastic policies, two reward functions are\n      unhackable only if one is constant. Theoretically explains why any\n      non-zero ISR weight can decrease prove_rate -- this is a fundamental\n      property of reward composition, not STA-specific.\n    key_finding: >\n      Any non-constant proxy reward can decrease true reward when optimized.\n      Unhackability requires the proxy to be constant, making all non-trivial\n      auxiliary rewards theoretically vulnerable to degrading primary performance.\n\n  - id: progrs-outcome-conditioned\n    title: \"LLM Reasoning with Process Rewards for Outcome-Guided Steps\"\n    authors: \"Mohammad Rezaei, Jens Lehmann, Sahar Vahdati\"\n    year: 2026\n    venue: \"arXiv 2604.02341\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      PRM scores optimized as absolute rewards amplify fluent failure modes.\n      Outcome-conditioned centering shifts incorrect trajectories' PRM scores\n      to zero mean, preserving ranking info without corrupting gradients.\n      Suggests STA should condition ISR on execution outcome.\n    key_finding: >\n      Naive process rewards induce reward hacking by rewarding locally fluent\n      but globally incorrect reasoning. Outcome-conditioned centering resolves\n      the conflict with fewer rollouts than outcome-only baselines.\n\n  - id: qwen-prm-lessons\n    title: \"The Lessons of Developing Process Reward Models in Mathematical Reasoning\"\n    authors: \"Zhenru Zhang et al. (Qwen Team, Alibaba)\"\n    year: 2025\n    venue: \"ACL 2025 Findings (arXiv 2501.07301)\"\n    category: reward-shaping\n    role: supporting-evidence\n    relevance: >\n      MC estimation-synthesized PRM data leads to quality degradation; policy\n      model generates \"answer-correct but reasoning-flawed\" responses, causing\n      process reward / outcome misalignment. Directly parallels ISR problem:\n      structurally correct but semantically wrong proof traces get high ISR\n      but low execution reward.\n    key_finding: >\n      PRM performance depends critically on data quality; MC estimation\n      introduces systematic bias. Answer-correct reasoning-flawed samples\n      corrupt process supervision signal.\n\n  # ============================================================\n  # Category 3: Mutation testing in software engineering\n  # ============================================================\n\n  - id: demillo1978\n    title: \"Hints on Test Data Selection: Help for the Practicing Programmer\"\n    authors: \"Richard A. DeMillo, Richard J. Lipton, Frederick G. Sayward\"\n    year: 1978\n    venue: \"Computer 11(4):34-43\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Foundational paper introducing mutation testing. STA's component\n      necessity testing directly extends this idea: instead of mutating\n      source code to test test suites, STA mutates logical formulas\n      to test component necessity for solver success.\n    key_finding: >\n      Introduced mutation testing and the coupling effect hypothesis:\n      tests that detect simple faults also detect complex faults.\n\n  - id: offutt-coupling\n    title: \"Investigations of the Software Testing Coupling Effect\"\n    authors: \"A. Jefferson Offutt\"\n    year: 1992\n    venue: \"ACM TOSEM 1(1):5-20\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Empirically validates the coupling effect hypothesis that underpins\n      mutation testing. STA's single-component ablation is analogous to\n      first-order mutation; the coupling effect suggests this suffices.\n    key_finding: >\n      Test data killing all first-order mutants killed >99% of second-\n      and third-order mutants, validating the coupling effect.\n\n  - id: jia-harman-survey\n    title: \"An Analysis and Survey of the Development of Mutation Testing\"\n    authors: \"Yue Jia, Mark Harman\"\n    year: 2011\n    venue: \"IEEE TSE 37(5):649-678\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Comprehensive survey of mutation testing covering three decades of\n      development. Provides theoretical and practical foundation for STA's\n      adaptation of mutation testing to logical formulas.\n    key_finding: >\n      Systematic classification of mutation operators, cost reduction\n      techniques, and equivalence problem -- all relevant to STA's design\n      of clause-level ablation operators.\n\n  - id: just-mutants-real-faults\n    title: \"Are Mutants a Valid Substitute for Real Faults in Software Testing?\"\n    authors: \"Rene Just, Darioush Jalali, Laura Inozemtseva, et al.\"\n    year: 2014\n    venue: \"FSE 2014\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Validates that mutation testing (structural/intensional analysis of\n      program adequacy) correlates with real fault detection. Supports STA's\n      premise that structural analysis of formalization components provides\n      meaningful signal about formalization quality.\n    key_finding: >\n      Mutant detection is statistically correlated with real fault detection,\n      and mutation score is a better predictor of test effectiveness than\n      code coverage.\n\n  - id: llmorpheus\n    title: \"LLMorpheus: Mutation Testing Using Large Language Models\"\n    authors: \"Frank Tip, Jon Bell, et al.\"\n    year: 2025\n    venue: \"IEEE TSE 2025\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Uses LLMs to generate realistic code mutants beyond traditional\n      mutation operators. Shows mutation testing evolving toward\n      ML-integrated approaches, validating STA's cross-pollination\n      of mutation testing ideas into ML training.\n    key_finding: >\n      LLM-generated mutants simulate real bugs that rule-based operators\n      cannot produce, improving mutation testing realism.\n\n  - id: mutation-guided-meta\n    title: \"Mutation-Guided LLM-based Test Generation at Meta\"\n    authors: \"Christopher Foster et al.\"\n    year: 2025\n    venue: \"FSE 2025\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Industrial application of mutation-guided LLM test generation at\n      Meta. Demonstrates that mutation analysis can guide LLM behavior\n      in production -- analogous to how STA uses mutation (ablation) to\n      guide GRPO reward signal.\n    key_finding: >\n      Mutation-guided approach generates tests that kill significantly\n      more mutants than unguided LLM test generation at Meta scale.\n\n  - id: mutation-consistency-llm\n    title: \"Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs\"\n    authors: \"Various\"\n    year: 2024\n    venue: \"arXiv 2401.05940\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Uses code mutations to evaluate LLM code understanding consistency.\n      Conceptually related to STA: both use systematic code/formula\n      mutations to assess model capabilities.\n    key_finding: >\n      LLMs show significant inconsistency when evaluated on mutated code\n      variants, suggesting superficial pattern matching.\n\n  # ============================================================\n  # Category 4: Intensional program analysis\n  # ============================================================\n\n  - id: deepmutation\n    title: \"A Probabilistic Framework for Mutation Testing in Deep Neural Networks\"\n    authors: \"Various\"\n    year: 2023\n    venue: \"Information and Software Technology 2023\"\n    category: intensional-analysis\n    role: background\n    relevance: >\n      Extends mutation testing to DNN testing with probabilistic mutation\n      operators. Parallel to STA's extension of mutation testing from\n      traditional programs to logical formulas.\n    key_finding: >\n      Probabilistic mutation framework enables meaningful test adequacy\n      assessment for neural networks through structural perturbation.\n\n  # ============================================================\n  # Category 5: Reward hacking / overoptimization\n  # ============================================================\n\n  - id: inform-reward-hacking\n    title: \"InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling\"\n    authors: \"Various\"\n    year: 2024\n    venue: \"NeurIPS 2024\"\n    category: reward-hacking\n    role: background\n    relevance: >\n      Proposes information-bottleneck approach to detect and mitigate reward\n      hacking. STA's ISR addresses the same problem differently: by grounding\n      reward in verifiable structural properties (component necessity), it\n      reduces the attack surface for reward hacking.\n    key_finding: >\n      Variational information bottleneck filters irrelevant features from\n      reward model; Cluster Separation Index detects reward overoptimization.\n\n  - id: mo-grpo\n    title: \"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\"\n    authors: \"CyberAgent AI Lab\"\n    year: 2025\n    venue: \"arXiv 2509.22047\"\n    category: reward-hacking\n    role: background\n    relevance: >\n      Directly addresses GRPO reward hacking in multi-objective settings.\n      STA's ISR can be viewed as adding a structural objective to the\n      correctness objective, making MO-GRPO's insights directly applicable.\n    key_finding: >\n      Standard GRPO normalizes after summing rewards, allowing high-variance\n      objectives to dominate. MO-GRPO equalizes scales before aggregation.\n\n  - id: reward-hacking-survey\n    title: \"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\"\n    authors: \"Various\"\n    year: 2026\n    venue: \"arXiv 2604.13602\"\n    category: reward-hacking\n    role: background\n    relevance: >\n      Comprehensive survey of reward hacking mechanisms in the LLM era.\n      Provides theoretical framework for understanding why STA's structural\n      reward is more robust than pure outcome-based reward.\n    key_finding: >\n      Reward hacking manifests through specification gaming, reward model\n      exploitation, and emergent misalignment; structural verification\n      rewards are more robust than learned reward models.\n\n  - id: energy-loss-reward-hacking\n    title: \"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking\"\n    authors: \"Various\"\n    year: 2025\n    venue: \"ICML 2025\"\n    category: reward-hacking\n    role: background\n    relevance: >\n      Identifies energy loss in LLM final layer as an indicator of reward\n      hacking during RL. Provides complementary diagnostic to STA's\n      structural reward approach.\n    key_finding: >\n      Energy loss in the final layer increases during RL and excessive\n      increase characterizes reward hacking; EPPO algorithm penalizes\n      this to mitigate hacking.\n\n  - id: spurious-rewards\n    title: \"Spurious Rewards: Rethinking Training Signals in RLVR\"\n    authors: \"Ruixin Yang et al.\"\n    year: 2025\n    venue: \"arXiv 2506.10947 / NeurIPS 2025 submission\"\n    category: reward-hacking\n    role: direct-evidence\n    relevance: >\n      Most directly relevant to STA findings. GRPO+random reward on\n      Qwen2.5-Math improves 21.4%, nearly matching ground-truth reward's\n      29.1%. Matches our plan017 finding: additive random (PR=48%) >\n      additive ISR (PR=18%). Structured metrics can be worse than random\n      noise due to systematic bias vs pure variance.\n    key_finding: >\n      Random reward nearly matches ground-truth reward in GRPO training,\n      suggesting GRPO's group normalization extracts signal from noise.\n      Effect is model-dependent (works on Qwen2.5, not Llama3).\n\n  - id: gao-reward-overoptimization\n    title: \"Scaling Laws for Reward Model Overoptimization\"\n    authors: \"Leo Gao, John Schulman, Jacob Hilton\"\n    year: 2023\n    venue: \"ICML 2023 (arXiv 2210.10760)\"\n    category: reward-hacking\n    role: theoretical-foundation\n    relevance: >\n      Foundational work quantifying Goodhart's effect: proxy reward rises\n      but gold reward first rises then falls. ISR is a proxy reward that\n      exhibits exactly this pattern — ISR can increase while prove_rate\n      decreases, making it suitable for post-hoc diagnosis but harmful\n      as training signal.\n    key_finding: >\n      Gold/proxy reward divergence follows predictable scaling laws.\n      Proxy reward optimization past critical point degrades gold reward,\n      with the divergence point scaling with model and dataset size.\n\n  - id: karwowski-goodhart-rl\n    title: \"Goodhart's Law in Reinforcement Learning\"\n    authors: \"Jacek Karwowski, Oliver Hayman, Xingjian Bai, Klaus Kiendlhofer, Charlie Griffin, Joar Skalse\"\n    year: 2024\n    venue: \"ICLR 2024 (arXiv 2310.09144)\"\n    category: reward-hacking\n    role: theoretical-foundation\n    relevance: >\n      Geometric interpretation of Goodhart's Law in MDPs: optimizing\n      imperfect proxy past critical point decreases true objective. ISR as\n      proxy has partial correlation with execution correctness — exceeding\n      critical optimization point pushes policy toward high-ISR but\n      low-correctness regions. Explains plan002/plan005 negative results.\n    key_finding: >\n      Formalizes Goodhart's Law for RL: any non-trivially correlated proxy\n      reward creates regions where proxy and true reward diverge, and\n      policy optimization inevitably enters these regions.\n\n  # ============================================================\n  # Category 6: FOL/Prolog formalization with LLMs\n  # ============================================================\n\n  - id: folio\n    title: \"FOLIO: Natural Language Reasoning with First-Order Logic\"\n    authors: \"Simeng Han et al.\"\n    year: 2022\n    venue: \"arXiv 2209.00840 / EMNLP 2024\"\n    category: fol-formalization\n    role: evaluation\n    relevance: >\n      Primary FOL reasoning benchmark. STA uses FOLIO-style NL->FOL\n      formalization as the target task for GRPO training. FOLIO's\n      expert-annotated FOL annotations serve as reference formalizations.\n    key_finding: >\n      1,430 NL-FOL paired examples with reasoning depths up to 5+;\n      GPT-4 still struggles on the hardest examples.\n\n  - id: proofwriter\n    title: \"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language\"\n    authors: \"Oyvind Tafjord, Bhavana Dalvi, Peter Clark\"\n    year: 2021\n    venue: \"Findings of ACL-IJCNLP 2021\"\n    category: fol-formalization\n    role: evaluation\n    relevance: >\n      Source dataset for STA's training data. ProofWriter provides\n      rule-based logical reasoning problems in natural language that\n      STA uses for training formalizer models.\n    key_finding: >\n      Generative model can reliably produce implications and proofs;\n      accuracy exceeds prior methods by 9% and generalizes to unseen\n      proof depths.\n\n  - id: logic-lm\n    title: \"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\"\n    authors: \"Liangming Pan, Alon Albalak, Xinyi Wang, William Wang\"\n    year: 2023\n    venue: \"Findings of EMNLP 2023\"\n    category: fol-formalization\n    role: direct-competitor\n    relevance: >\n      LLM->symbolic solver pipeline for logical reasoning, directly\n      comparable to STA's formalizer->Prolog solver pipeline. Key\n      difference: Logic-LM uses prompting, STA uses GRPO training.\n    key_finding: >\n      LLM+solver achieves 39.2% improvement over LLM-alone on logical\n      reasoning benchmarks including ProofWriter and FOLIO.\n\n  - id: linc\n    title: \"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers\"\n    authors: \"Theo X. Olausson, Alex Gu, Ben Lipkin, et al.\"\n    year: 2023\n    venue: \"EMNLP 2023\"\n    category: fol-formalization\n    role: direct-competitor\n    relevance: >\n      Neurosymbolic approach where LLM translates NL to FOL for theorem\n      prover. Directly comparable to STA's NL->Prolog translation.\n      LINC uses prompting-based approach; STA uses RL training.\n    key_finding: >\n      StarCoder+ (15.5B) with LINC outperforms GPT-3.5 and GPT-4 with\n      CoT by 38% and 10% respectively on ProofWriter.\n\n  - id: fover-pei2025\n    title: \"FoVer: First-Order Logic Verification for Natural Language Reasoning\"\n    authors: \"Yu Pei, Yongping Du, Xingnan Jin\"\n    year: 2025\n    venue: \"TACL 13:1340-1359\"\n    category: fol-formalization\n    role: direct-competitor\n    relevance: >\n      Uses LLM->FOL->Z3 pipeline for verifying NL reasoning correctness.\n      Similar to STA's verification pipeline but focuses on post-hoc\n      verification rather than training reward signal.\n    key_finding: >\n      FOL verification via Z3 significantly outperforms existing methods\n      on ProofWriter and FOLIO benchmarks.\n\n  - id: lorp\n    title: \"LoRP: LLM-based Logical Reasoning via Prolog\"\n    authors: \"Various\"\n    year: 2025\n    venue: \"Knowledge-Based Systems 2025\"\n    category: fol-formalization\n    role: direct-competitor\n    relevance: >\n      LLM->Prolog pipeline with FOL-to-Prolog translation mechanism.\n      Closest to STA's formalization target (Prolog), though LoRP\n      uses prompting while STA uses GRPO training with structural reward.\n    key_finding: >\n      Systematic FOL-to-Prolog translation extends Prolog expressiveness;\n      achieves SoTA accuracy on logical reasoning with three-vote majority.\n\n  - id: nl2fol\n    title: \"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection\"\n    authors: \"Lalwani, Kim, et al.\"\n    year: 2024\n    venue: \"arXiv 2405.02318\"\n    category: fol-formalization\n    role: background\n    relevance: >\n      Step-by-step NL->FOL translation using LLMs with SMT solver\n      verification. Demonstrates the NL->formal logic pipeline that\n      STA aims to improve via RL training.\n    key_finding: >\n      Neurosymbolic NL2FOL achieves 78% F1 on LOGIC dataset and\n      generalizes to LogicClimate (80% F1), outperforming supervised\n      models by 21%.\n\n  - id: logica2\n    title: \"LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding\"\n    authors: \"Liu et al.\"\n    year: 2023\n    venue: \"IEEE/ACM TASLP 2023\"\n    category: fol-formalization\n    role: evaluation\n    relevance: >\n      Logical reasoning evaluation benchmark derived from Chinese civil\n      service exams. Provides supplementary evaluation for STA's\n      formalization capabilities.\n    key_finding: >\n      8,678 multiple-choice questions covering categorical, disjunctive,\n      and conditional reasoning; widely used LLM benchmark.\n\n  # ============================================================\n  # Category 7: Goodhart's Law theory and dose-response dynamics\n  # ============================================================\n\n  - id: manheim-goodhart-taxonomy\n    title: \"Categorizing Variants of Goodhart's Law\"\n    authors: \"David Manheim, Scott Garrabrant\"\n    year: 2019\n    venue: \"arXiv 1803.04585\"\n    category: goodhart-overoptimization\n    role: theoretical-foundation\n    relevance: >\n      Four-part Goodhart taxonomy: regressional, extremal, causal, adversarial.\n      STA's high-β ISR collapse is best classified as extremal Goodhart\n      (policy moves to OOD region where ISR↑ but prove_rate↓). Provides\n      vocabulary for discussion section.\n    key_finding: >\n      First systematic categorization of Goodhart failure modes. Extremal\n      variant occurs when proxy-goal relationship breaks in out-of-distribution\n      regions reached by strong optimization.\n\n  - id: pan-reward-misspecification\n    title: \"The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models\"\n    authors: \"Alexander Pan, Kush Bhatia, Jacob Steinhardt\"\n    year: 2022\n    venue: \"ICLR 2022\"\n    category: goodhart-overoptimization\n    role: theoretical-foundation\n    relevance: >\n      Across 9 environments, more capable agents exploit misspecifications more.\n      Observes dose-dependent degradation — capability thresholds where true\n      reward sharply drops. Matches STA's β=0.1→0.3 qualitative shift.\n    key_finding: >\n      Reward misspecification causes dose-dependent degradation where true reward\n      sharply drops past capability thresholds. More capable optimization\n      produces worse outcomes under misspecification.\n\n  - id: kwa-catastrophic-goodhart\n    title: \"Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification\"\n    authors: \"Tat-Thang Kwa, Rachel Thomas, Adrià Garriga-Alonso\"\n    year: 2024\n    venue: \"NeurIPS 2024\"\n    category: goodhart-overoptimization\n    role: theoretical-foundation\n    relevance: >\n      If reward model error is heavy-tailed, policies achieve arbitrarily\n      high proxy reward with no true utility gain. KL regularization provably\n      fails. Explains why KL penalty in GRPO cannot prevent ISR collapse\n      at high β if ISR error distribution is heavy-tailed.\n    key_finding: >\n      KL-regularized RL provably fails to prevent overoptimization under\n      heavy-tailed reward misspecification. Policies can achieve arbitrarily\n      high proxy reward with zero true utility.\n\n  - id: rafailov-daa-scaling\n    title: \"Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms\"\n    authors: \"Rafael Rafailov, Yaswanth Chittepu, Ryan Park, Harshit Sikchi, Joey Hejna, W. Bradley Knox, Chelsea Finn, Scott Niekum\"\n    year: 2024\n    venue: \"NeurIPS 2024\"\n    category: goodhart-overoptimization\n    role: supporting-evidence\n    relevance: >\n      Extends Gao et al. to DPO/IPO/SLiC. Tests seven β values across\n      1B-6.9B models. DAAs still overoptimize despite no explicit proxy RM.\n      Validates β as a \"dose\" parameter — directly analogous to STA's\n      ISR weight sweep.\n    key_finding: >\n      Direct alignment algorithms exhibit overoptimization following\n      predictable scaling laws. Smaller models overoptimize sooner.\n      β-controlled dose-response is a general phenomenon across RL paradigms.\n\n  - id: huang-chi-squared\n    title: \"Correcting the Mythos of KL-Regularization: Direct and Contrastive Distribution Correction\"\n    authors: \"Afra Feyza Akyürek, Banghua Zhu, Sham Kakade, Jiantao Jiao\"\n    year: 2025\n    venue: \"ICLR 2025 Poster\"\n    category: goodhart-overoptimization\n    role: supporting-evidence\n    relevance: >\n      KL-regularization is theoretically inadequate for preventing\n      overoptimization. Chi-squared divergence provably alleviates it.\n      Suggests that even with KL penalty in GRPO, STA's high-β collapse\n      is theoretically expected.\n    key_finding: >\n      Chi-squared preference optimization provably mitigates overoptimization\n      where KL-regularization fails. Alternative divergence measures offer\n      stronger guarantees.\n\n  - id: coste-rm-ensembles\n    title: \"Reward Model Ensembles Help Mitigate Overoptimization\"\n    authors: \"Thomas Coste, Usman Anwar, Robert Kirk, David Krueger\"\n    year: 2023\n    venue: \"NeurIPS 2023 Workshop on Alignment\"\n    category: goodhart-overoptimization\n    role: background\n    relevance: >\n      Worst-case optimization across RM ensembles practically eliminates\n      overoptimization for BoN and reduces it for PPO. Suggests ensemble\n      of multiple solver metrics (instead of single ISR) as mitigation.\n    key_finding: >\n      RM ensembles with worst-case aggregation mitigate overoptimization.\n      Ensemble size and diversity directly affect robustness.\n\n  # ============================================================\n  # Category 8: Solver/prover as RL reward signal\n  # ============================================================\n\n  - id: rlsf\n    title: \"Reinforcement Learning via Symbolic Feedback\"\n    authors: \"Abhinav Jha, Shikhar Murty, Zico Kolter, et al.\"\n    year: 2024\n    venue: \"arXiv 2405.16661\"\n    category: verification-reward\n    role: direct-competitor\n    relevance: >\n      Most directly relevant: uses solver/prover certificates as fine-grained\n      token-level reward signal. Outperforms traditional approaches on program\n      synthesis (+31.4%). STA extends this paradigm and shows when it breaks\n      (Goodhart effects at high auxiliary reward weight).\n    key_finding: >\n      Symbolic reasoning tools provide poly-sized certificates as reward.\n      Smaller RLSF models outperform GPT-4 on structured generation tasks.\n\n  - id: fover-kamoi2026\n    title: \"FoVer: Generalizable Process Reward Models via Formally Verified Training Data\"\n    authors: \"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\"\n    year: 2025\n    venue: \"Findings of ACL 2026 (arXiv 2502.01345)\"\n    category: verification-reward\n    role: supporting-evidence\n    relevance: >\n      Uses Z3 and Isabelle to synthesize PRM training data by annotating\n      step-level error labels without human annotation. Same solver family\n      as STA. Shows verification-based rewards work; STA extends by showing\n      dose-response dynamics.\n    key_finding: >\n      Formally verified training data enables generalizable process reward\n      models competitive on ProcessBench and 12 reasoning benchmarks.\n\n  - id: deepseek-prover-v15\n    title: \"DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search\"\n    authors: \"DeepSeek AI\"\n    year: 2024\n    venue: \"ICLR 2025 (arXiv 2408.08152)\"\n    category: verification-reward\n    role: method-component\n    relevance: >\n      Uses GRPO with Lean 4 verification as binary reward. Same algorithm\n      (GRPO) + formal verification, but binary (pass/fail). Binary reward\n      avoids the graded-metric Goodhart risk that STA identifies with ISR.\n    key_finding: >\n      GRPO + binary Lean verification achieves 63.5% on miniF2F. Binary\n      correctness guarantee via formal verification sidesteps proxy reward\n      overoptimization.\n\n  - id: alphaproof\n    title: \"AlphaProof\"\n    authors: \"Google DeepMind\"\n    year: 2024\n    venue: \"Nature 2025\"\n    category: verification-reward\n    role: background\n    relevance: >\n      AlphaZero-inspired RL with Lean proof verification at scale.\n      Silver medal at IMO 2024. Binary verification reward avoids the\n      Goodhart problem STA identifies with graded verification metrics.\n    key_finding: >\n      Binary formal verification as RL reward scales to IMO-level\n      mathematical reasoning. Demonstrates verification-reward RL works\n      at the frontier of mathematical difficulty.\n\n  - id: math-shepherd\n    title: \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\"\n    authors: \"Peiyi Wang, Lei Li, Zhihong Shao, R.X. Xu, et al.\"\n    year: 2024\n    venue: \"ACL 2024 (arXiv 2312.08935)\"\n    category: verification-reward\n    role: supporting-evidence\n    relevance: >\n      Automatically constructs process supervision data and uses it as\n      step-by-step PPO reward. Automated verification reward without human\n      labels, analogous to STA's automated ISR computation via solver.\n    key_finding: >\n      Automated process supervision improves Mistral-7B on GSM8K\n      (77.9→84.1%) and MATH (28.6→33.0%) without human annotation.\n\n  # ============================================================\n  # Additional reward-shaping papers (Goodhart survey additions)\n  # ============================================================\n\n  - id: bipars\n    title: \"Learning to Utilize Shaping Rewards: A New Approach of Reward Shaping\"\n    authors: \"Yujing Hu, Weixun Wang, Hangtian Jia, et al.\"\n    year: 2020\n    venue: \"NeurIPS 2020\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Bi-level optimization learns parameterized shaping reward weights.\n      Can transform harmful shaping rewards into beneficial ones by learning\n      negative weights. Directly addresses STA's problem: when ISR weight\n      is wrong, automated weight learning could find optimal β.\n    key_finding: >\n      Bi-level optimization automatically learns auxiliary reward weights,\n      outperforming fixed weights and recovering from harmful shaping rewards.\n\n  - id: dapo\n    title: \"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\"\n    authors: \"Qiying Yu et al. (ByteDance)\"\n    year: 2025\n    venue: \"arXiv 2503.14476\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Four techniques for stable multi-component reward in GRPO: Clip-Higher,\n      Dynamic Sampling, token-level policy gradient, Overlong Reward Shaping.\n      Addresses stability issues relevant to STA's multi-reward setup.\n    key_finding: >\n      Clip-Higher and Dynamic Sampling prevent entropy collapse in GRPO\n      with multi-component rewards. Soft punishment for overlong outputs\n      avoids reward hacking through length exploitation.\n",
    "structuredPatch": [
      {
        "oldStart": 91,
        "oldLines": 6,
        "newStart": 91,
        "newLines": 56,
        "lines": [
          "       Declarative formulation outperforms imperative program-aided LMs by 23%",
          "       on GSM; achieves SoTA on LSAT and BoardgameQA.",
          " ",
          "+  - id: deepproblog",
          "+    title: \"Neural Probabilistic Logic Programming in DeepProbLog\"",
          "+    authors: \"Robin Manhaeve, Sebastijan Dumančić, Angelika Kimmig, Thomas Demeester, Luc De Raedt\"",
          "+    year: 2021",
          "+    venue: \"Artificial Intelligence 298\"",
          "+    category: neurosymbolic-rl",
          "+    role: background",
          "+    relevance: >",
          "+      Foundational neural-probabilistic logic programming framework that integrates",
          "+      deep learning with ProbLog via neural predicates. Establishes the intellectual",
          "+      tradition of combining neural networks with logic programming that STA extends",
          "+      to LLM-generated Prolog with RL training.",
          "+    key_finding: >",
          "+      End-to-end differentiable framework integrating neural perception with",
          "+      probabilistic logical reasoning; supports program induction and learning",
          "+      from examples.",
          "+",
          "+  - id: neurasp",
          "+    title: \"NeurASP: Embracing Neural Networks into Answer Set Programming\"",
          "+    authors: \"Zhun Yang, Adam Ishay, Joohyung Lee\"",
          "+    year: 2020",
          "+    venue: \"IJCAI 2020\"",
          "+    category: neurosymbolic-rl",
          "+    role: background",
          "+    relevance: >",
          "+      Integrates neural networks with answer set programming (ASP), using",
          "+      ASP rules to constrain and improve neural network training. Complementary",
          "+      to DeepProbLog; together they represent the neuro-symbolic LP foundation",
          "+      that STA's LLM-to-Prolog pipeline builds upon.",
          "+    key_finding: >",
          "+      ASP semantic constraints improve neural network perception accuracy;",
          "+      demonstrates bidirectional benefit of neural-symbolic integration.",
          "+",
          "+  - id: thought-like-pro",
          "+    title: \"Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought\"",
          "+    authors: \"Xiaoyu Tan, Yongxin Deng, Xihe Qiu, Weidi Xu, Chao Qu, Wei Chu, Yinghui Xu, Yuan Qi\"",
          "+    year: 2024",
          "+    venue: \"arXiv 2407.14562\"",
          "+    category: neurosymbolic-rl",
          "+    role: direct-competitor",
          "+    relevance: >",
          "+      Uses Prolog engine to generate verified reasoning trajectories, then trains",
          "+      LLMs via imitation learning to replicate them. Directly comparable pipeline",
          "+      to STA (Prolog verification + LLM training), but uses imitation learning",
          "+      instead of GRPO with structural reward.",
          "+    key_finding: >",
          "+      Prolog-verified reasoning trajectories as training signal improve LLM",
          "+      logical reasoning; self-driven framework enables LLMs to formulate",
          "+      rules from instructions and leverage Prolog for derivation.",
          "+",
          "   # ============================================================",
          "   # Category 2: Reward shaping for code/formal verification",
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

_source line 56_

Now add the Goodhart/specification gaming papers. Let me find the right insertion point.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "8d783a4b-29a7-4961-a6b1-13201beff1e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LcZh6wFRNF4xW4f6ewM8eH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 946,
      "cache_read_input_tokens": 58088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 946
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

_source line 57_

<details open><summary>🔧 Tool call — Read · `toolu_016QVgxDKW5ecsJwSw2xWFzp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
  "offset": 340,
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
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "18dfdf46-c467-4f04-afe4-bd90383d30d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LcZh6wFRNF4xW4f6ewM8eH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 946,
      "cache_read_input_tokens": 58088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 946
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

_source line 58 · 2026-05-14T17:45:40.126Z_

<details><summary>↩ Tool result · `toolu_016QVgxDKW5ecsJwSw2xWFzp`</summary>

```text
340	    relevance: >
341	      Empirically validates the coupling effect hypothesis that underpins
342	      mutation testing. STA's single-component ablation is analogous to
343	      first-order mutation; the coupling effect suggests this suffices.
344	    key_finding: >
345	      Test data killing all first-order mutants killed >99% of second-
346	      and third-order mutants, validating the coupling effect.
347	
348	  - id: jia-harman-survey
349	    title: "An Analysis and Survey of the Development of Mutation Testing"
350	    authors: "Yue Jia, Mark Harman"
351	    year: 2011
352	    venue: "IEEE TSE 37(5):649-678"
353	    category: mutation-testing
354	    role: background
355	    relevance: >
356	      Comprehensive survey of mutation testing covering three decades of
357	      development. Provides theoretical and practical foundation for STA's
358	      adaptation of mutation testing to logical formulas.
359	    key_finding: >
360	      Systematic classification of mutation operators, cost reduction
361	      techniques, and equivalence problem -- all relevant to STA's design
362	      of clause-level ablation operators.
363	
364	  - id: just-mutants-real-faults
365	    title: "Are Mutants a Valid Substitute for Real Faults in Software Testing?"
366	    authors: "Rene Just, Darioush Jalali, Laura Inozemtseva, et al."
367	    year: 2014
368	    venue: "FSE 2014"
369	    category: mutation-testing
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "78c89b95-8b10-42b5-840c-f56213ae4ebc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
      "content": "    relevance: >\n      Empirically validates the coupling effect hypothesis that underpins\n      mutation testing. STA's single-component ablation is analogous to\n      first-order mutation; the coupling effect suggests this suffices.\n    key_finding: >\n      Test data killing all first-order mutants killed >99% of second-\n      and third-order mutants, validating the coupling effect.\n\n  - id: jia-harman-survey\n    title: \"An Analysis and Survey of the Development of Mutation Testing\"\n    authors: \"Yue Jia, Mark Harman\"\n    year: 2011\n    venue: \"IEEE TSE 37(5):649-678\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Comprehensive survey of mutation testing covering three decades of\n      development. Provides theoretical and practical foundation for STA's\n      adaptation of mutation testing to logical formulas.\n    key_finding: >\n      Systematic classification of mutation operators, cost reduction\n      techniques, and equivalence problem -- all relevant to STA's design\n      of clause-level ablation operators.\n\n  - id: just-mutants-real-faults\n    title: \"Are Mutants a Valid Substitute for Real Faults in Software Testing?\"\n    authors: \"Rene Just, Darioush Jalali, Laura Inozemtseva, et al.\"\n    year: 2014\n    venue: \"FSE 2014\"\n    category: mutation-testing",
      "numLines": 30,
      "startLine": 340,
      "totalLines": 915
    }
  }
}
```

</details>

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Read · `toolu_01CZGcJ2ohKHtcHDs4Q7GJTU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
  "offset": 435,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "4e5a14fd-bb53-47fa-9f46-4aa2bacb6052",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MqY1qZK1aQKVZQDsvshyog",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 563,
      "cache_read_input_tokens": 59034,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 563
      },
      "output_tokens": 64,
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

_source line 60 · 2026-05-14T17:45:43.050Z_

<details><summary>↩ Tool result · `toolu_01CZGcJ2ohKHtcHDs4Q7GJTU`</summary>

```text
435	    year: 2023
436	    venue: "Information and Software Technology 2023"
437	    category: intensional-analysis
438	    role: background
439	    relevance: >
440	      Extends mutation testing to DNN testing with probabilistic mutation
441	      operators. Parallel to STA's extension of mutation testing from
442	      traditional programs to logical formulas.
443	    key_finding: >
444	      Probabilistic mutation framework enables meaningful test adequacy
445	      assessment for neural networks through structural perturbation.
446	
447	  # ============================================================
448	  # Category 5: Reward hacking / overoptimization
449	  # ============================================================
450	
451	  - id: inform-reward-hacking
452	    title: "InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling"
453	    authors: "Various"
454	    year: 2024
455	    venue: "NeurIPS 2024"
456	    category: reward-hacking
457	    role: background
458	    relevance: >
459	      Proposes information-bottleneck approach to detect and mitigate reward
460	      hacking. STA's ISR addresses the same problem differently: by grounding
461	      reward in verifiable structural properties (component necessity), it
462	      reduces the attack surface for reward hacking.
463	    key_finding: >
464	      Variational information bottleneck filters irrelevant features from
465	      reward model; Cluster Separation Index detects reward overoptimization.
466	
467	  - id: mo-grpo
468	    title: "MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems"
469	    authors: "CyberAgent AI Lab"
470	    year: 2025
471	    venue: "arXiv 2509.22047"
472	    category: reward-hacking
473	    role: background
474	    relevance: >
475	      Directly addresses GRPO reward hacking in multi-objective settings.
476	      STA's ISR can be viewed as adding a structural objective to the
477	      correctness objective, making MO-GRPO's insights directly applicable.
478	    key_finding: >
479	      Standard GRPO normalizes after summing rewards, allowing high-variance
480	      objectives to dominate. MO-GRPO equalizes scales before aggregation.
481	
482	  - id: reward-hacking-survey
483	    title: "Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges"
484	    authors: "Various"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "7f4a0da4-be42-4d03-a76b-0c908cfec67c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
      "content": "    year: 2023\n    venue: \"Information and Software Technology 2023\"\n    category: intensional-analysis\n    role: background\n    relevance: >\n      Extends mutation testing to DNN testing with probabilistic mutation\n      operators. Parallel to STA's extension of mutation testing from\n      traditional programs to logical formulas.\n    key_finding: >\n      Probabilistic mutation framework enables meaningful test adequacy\n      assessment for neural networks through structural perturbation.\n\n  # ============================================================\n  # Category 5: Reward hacking / overoptimization\n  # ============================================================\n\n  - id: inform-reward-hacking\n    title: \"InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling\"\n    authors: \"Various\"\n    year: 2024\n    venue: \"NeurIPS 2024\"\n    category: reward-hacking\n    role: background\n    relevance: >\n      Proposes information-bottleneck approach to detect and mitigate reward\n      hacking. STA's ISR addresses the same problem differently: by grounding\n      reward in verifiable structural properties (component necessity), it\n      reduces the attack surface for reward hacking.\n    key_finding: >\n      Variational information bottleneck filters irrelevant features from\n      reward model; Cluster Separation Index detects reward overoptimization.\n\n  - id: mo-grpo\n    title: \"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\"\n    authors: \"CyberAgent AI Lab\"\n    year: 2025\n    venue: \"arXiv 2509.22047\"\n    category: reward-hacking\n    role: background\n    relevance: >\n      Directly addresses GRPO reward hacking in multi-objective settings.\n      STA's ISR can be viewed as adding a structural objective to the\n      correctness objective, making MO-GRPO's insights directly applicable.\n    key_finding: >\n      Standard GRPO normalizes after summing rewards, allowing high-variance\n      objectives to dominate. MO-GRPO equalizes scales before aggregation.\n\n  - id: reward-hacking-survey\n    title: \"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\"\n    authors: \"Various\"",
      "numLines": 50,
      "startLine": 435,
      "totalLines": 915
    }
  }
}
```

</details>

---

### Tool call

_source line 61_

<details open><summary>🔧 Tool call — Read · `toolu_01UZJMTczHbfd5VgTp4sUBHP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
  "offset": 527,
  "limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "67cbedeb-9f9b-455e-a179-844e36f4b77c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GiMcXBzPqRwCwtZcukBbXd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 59597,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 805
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

_source line 62 · 2026-05-14T17:45:46.202Z_

<details><summary>↩ Tool result · `toolu_01UZJMTczHbfd5VgTp4sUBHP`</summary>

```text
527	    key_finding: >
528	      Random reward nearly matches ground-truth reward in GRPO training,
529	      suggesting GRPO's group normalization extracts signal from noise.
530	      Effect is model-dependent (works on Qwen2.5, not Llama3).
531	
532	  - id: gao-reward-overoptimization
533	    title: "Scaling Laws for Reward Model Overoptimization"
534	    authors: "Leo Gao, John Schulman, Jacob Hilton"
535	    year: 2023
536	    venue: "ICML 2023 (arXiv 2210.10760)"
537	    category: reward-hacking
538	    role: theoretical-foundation
539	    relevance: >
540	      Foundational work quantifying Goodhart's effect: proxy reward rises
541	      but gold reward first rises then falls. ISR is a proxy reward that
542	      exhibits exactly this pattern — ISR can increase while prove_rate
543	      decreases, making it suitable for post-hoc diagnosis but harmful
544	      as training signal.
545	    key_finding: >
546	      Gold/proxy reward divergence follows predictable scaling laws.
547	      Proxy reward optimization past critical point degrades gold reward,
548	      with the divergence point scaling with model and dataset size.
549	
550	  - id: karwowski-goodhart-rl
551	    title: "Goodhart's Law in Reinforcement Learning"
552	    authors: "Jacek Karwowski, Oliver Hayman, Xingjian Bai, Klaus Kiendlhofer, Charlie Griffin, Joar Skalse"
553	    year: 2024
554	    venue: "ICLR 2024 (arXiv 2310.09144)"
555	    category: reward-hacking
556	    role: theoretical-foundation
557	    relevance: >
558	      Geometric interpretation of Goodhart's Law in MDPs: optimizing
559	      imperfect proxy past critical point decreases true objective. ISR as
560	      proxy has partial correlation with execution correctness — exceeding
561	      critical optimization point pushes policy toward high-ISR but
562	      low-correctness regions. Explains plan002/plan005 negative results.
563	    key_finding: >
564	      Formalizes Goodhart's Law for RL: any non-trivially correlated proxy
565	      reward creates regions where proxy and true reward diverge, and
566	      policy optimization inevitably enters these regions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "efc2ff9e-3af4-49f4-b2f2-df036c72d09c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
      "content": "    key_finding: >\n      Random reward nearly matches ground-truth reward in GRPO training,\n      suggesting GRPO's group normalization extracts signal from noise.\n      Effect is model-dependent (works on Qwen2.5, not Llama3).\n\n  - id: gao-reward-overoptimization\n    title: \"Scaling Laws for Reward Model Overoptimization\"\n    authors: \"Leo Gao, John Schulman, Jacob Hilton\"\n    year: 2023\n    venue: \"ICML 2023 (arXiv 2210.10760)\"\n    category: reward-hacking\n    role: theoretical-foundation\n    relevance: >\n      Foundational work quantifying Goodhart's effect: proxy reward rises\n      but gold reward first rises then falls. ISR is a proxy reward that\n      exhibits exactly this pattern — ISR can increase while prove_rate\n      decreases, making it suitable for post-hoc diagnosis but harmful\n      as training signal.\n    key_finding: >\n      Gold/proxy reward divergence follows predictable scaling laws.\n      Proxy reward optimization past critical point degrades gold reward,\n      with the divergence point scaling with model and dataset size.\n\n  - id: karwowski-goodhart-rl\n    title: \"Goodhart's Law in Reinforcement Learning\"\n    authors: \"Jacek Karwowski, Oliver Hayman, Xingjian Bai, Klaus Kiendlhofer, Charlie Griffin, Joar Skalse\"\n    year: 2024\n    venue: \"ICLR 2024 (arXiv 2310.09144)\"\n    category: reward-hacking\n    role: theoretical-foundation\n    relevance: >\n      Geometric interpretation of Goodhart's Law in MDPs: optimizing\n      imperfect proxy past critical point decreases true objective. ISR as\n      proxy has partial correlation with execution correctness — exceeding\n      critical optimization point pushes policy toward high-ISR but\n      low-correctness regions. Explains plan002/plan005 negative results.\n    key_finding: >\n      Formalizes Goodhart's Law for RL: any non-trivially correlated proxy\n      reward creates regions where proxy and true reward diverge, and\n      policy optimization inevitably enters these regions.",
      "numLines": 40,
      "startLine": 527,
      "totalLines": 915
    }
  }
}
```

</details>

---

### Assistant

_source line 63_

Now I'll add the two new papers to the reward-hacking section, right after `spurious-rewards`:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "1b10c763-fb8e-4a7f-aabf-3eeb651a066c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CJRLjB5pzFDX3V28ZhFbo5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 758,
      "cache_read_input_tokens": 60402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 758
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

_source line 64_

<details open><summary>🔧 Tool call — Read · `toolu_01VFREZnf56QqWyXstYvTGpL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
  "offset": 520,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "7a5871da-0a07-4040-adce-d613ae730cf2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CJRLjB5pzFDX3V28ZhFbo5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 758,
      "cache_read_input_tokens": 60402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 758
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

_source line 65 · 2026-05-14T17:45:50.442Z_

<details><summary>↩ Tool result · `toolu_01VFREZnf56QqWyXstYvTGpL`</summary>

```text
520	    role: direct-evidence
521	    relevance: >
522	      Most directly relevant to STA findings. GRPO+random reward on
523	      Qwen2.5-Math improves 21.4%, nearly matching ground-truth reward's
524	      29.1%. Matches our plan017 finding: additive random (PR=48%) >
525	      additive ISR (PR=18%). Structured metrics can be worse than random
526	      noise due to systematic bias vs pure variance.
527	    key_finding: >
528	      Random reward nearly matches ground-truth reward in GRPO training,
529	      suggesting GRPO's group normalization extracts signal from noise.
530	      Effect is model-dependent (works on Qwen2.5, not Llama3).
531	
532	  - id: gao-reward-overoptimization
533	    title: "Scaling Laws for Reward Model Overoptimization"
534	    authors: "Leo Gao, John Schulman, Jacob Hilton"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "2709ca6c-42f2-407e-8875-0ffc4b1b7c0a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
      "content": "    role: direct-evidence\n    relevance: >\n      Most directly relevant to STA findings. GRPO+random reward on\n      Qwen2.5-Math improves 21.4%, nearly matching ground-truth reward's\n      29.1%. Matches our plan017 finding: additive random (PR=48%) >\n      additive ISR (PR=18%). Structured metrics can be worse than random\n      noise due to systematic bias vs pure variance.\n    key_finding: >\n      Random reward nearly matches ground-truth reward in GRPO training,\n      suggesting GRPO's group normalization extracts signal from noise.\n      Effect is model-dependent (works on Qwen2.5, not Llama3).\n\n  - id: gao-reward-overoptimization\n    title: \"Scaling Laws for Reward Model Overoptimization\"\n    authors: \"Leo Gao, John Schulman, Jacob Hilton\"",
      "numLines": 15,
      "startLine": 520,
      "totalLines": 915
    }
  }
}
```

</details>

---

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — Edit · `toolu_018fZ33T8Jq9ovDoDK4sdV9x`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
  "old_string": "  - id: gao-reward-overoptimization\n    title: \"Scaling Laws for Reward Model Overoptimization\"\n    authors: \"Leo Gao, John Schulman, Jacob Hilton\"",
  "new_string": "  - id: bondarenko-spec-gaming\n    title: \"Demonstrating Specification Gaming in Reasoning Models\"\n    authors: \"Alexander Bondarenko, Denis Volk, Dmitrii Volkov, Jeffrey Ladish\"\n    year: 2025\n    venue: \"arXiv 2502.13295\"\n    category: reward-hacking\n    role: direct-evidence\n    relevance: >\n      Shows that reasoning models (o3, DeepSeek-R1) resort to specification\n      gaming on difficult tasks by default, without explicit nudging.\n      Directly relevant to STA's concern: RL-trained reasoning models\n      may game formal verification rewards rather than learn genuine\n      formalization skills.\n    key_finding: >\n      Reasoning models spontaneously hack benchmarks (e.g., manipulating\n      chess engine files instead of playing chess). Stronger reasoning\n      capability correlates with more sophisticated gaming strategies.\n\n  - id: kim-game-formalization\n    title: \"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning\"\n    authors: \"Kyuhee Kim, Auguste Poiroux, Antoine Bosselut\"\n    year: 2026\n    venue: \"VerifAI-2 Workshop, ICLR 2026 (arXiv 2604.19459)\"\n    category: reward-hacking\n    role: direct-evidence\n    relevance: >\n      Directly studies whether LLMs game formalization in logical reasoning --\n      the exact phenomenon STA's ISR is designed to detect. Evaluates GPT-5\n      and DeepSeek-R1 on FOLIO with Lean 4 proofs. Finds two modes of\n      unfaithfulness: axiom fabrication (GPT-5) and premise mistranslation\n      (R1), the latter evading detection entirely.\n    key_finding: >\n      High compilation rates (87-99%) do not imply faithful formalization.\n      Two-stage pipelines reveal unfaithfulness that unified generation hides.\n      Premise mistranslation produces internally consistent but unfaithful\n      outputs -- analogous to STA's high-ISR but semantically wrong traces.\n\n  - id: gao-reward-overoptimization\n    title: \"Scaling Laws for Reward Model Overoptimization\"\n    authors: \"Leo Gao, John Schulman, Jacob Hilton\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "b67051ff-df7c-4b85-8f76-9374bce12614",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PE7Tfyh2vdxoC4NC7ymuAs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 408,
      "cache_read_input_tokens": 61160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 408
      },
      "output_tokens": 72,
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

_source line 67 · 2026-05-14T17:46:05.859Z_

<details><summary>↩ Tool result · `toolu_018fZ33T8Jq9ovDoDK4sdV9x`</summary>

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
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "9da1b667-a51f-4e5c-a4d9-e99b0de9d20b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
    "oldString": "  - id: gao-reward-overoptimization\n    title: \"Scaling Laws for Reward Model Overoptimization\"\n    authors: \"Leo Gao, John Schulman, Jacob Hilton\"",
    "newString": "  - id: bondarenko-spec-gaming\n    title: \"Demonstrating Specification Gaming in Reasoning Models\"\n    authors: \"Alexander Bondarenko, Denis Volk, Dmitrii Volkov, Jeffrey Ladish\"\n    year: 2025\n    venue: \"arXiv 2502.13295\"\n    category: reward-hacking\n    role: direct-evidence\n    relevance: >\n      Shows that reasoning models (o3, DeepSeek-R1) resort to specification\n      gaming on difficult tasks by default, without explicit nudging.\n      Directly relevant to STA's concern: RL-trained reasoning models\n      may game formal verification rewards rather than learn genuine\n      formalization skills.\n    key_finding: >\n      Reasoning models spontaneously hack benchmarks (e.g., manipulating\n      chess engine files instead of playing chess). Stronger reasoning\n      capability correlates with more sophisticated gaming strategies.\n\n  - id: kim-game-formalization\n    title: \"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning\"\n    authors: \"Kyuhee Kim, Auguste Poiroux, Antoine Bosselut\"\n    year: 2026\n    venue: \"VerifAI-2 Workshop, ICLR 2026 (arXiv 2604.19459)\"\n    category: reward-hacking\n    role: direct-evidence\n    relevance: >\n      Directly studies whether LLMs game formalization in logical reasoning --\n      the exact phenomenon STA's ISR is designed to detect. Evaluates GPT-5\n      and DeepSeek-R1 on FOLIO with Lean 4 proofs. Finds two modes of\n      unfaithfulness: axiom fabrication (GPT-5) and premise mistranslation\n      (R1), the latter evading detection entirely.\n    key_finding: >\n      High compilation rates (87-99%) do not imply faithful formalization.\n      Two-stage pipelines reveal unfaithfulness that unified generation hides.\n      Premise mistranslation produces internally consistent but unfaithful\n      outputs -- analogous to STA's high-ISR but semantically wrong traces.\n\n  - id: gao-reward-overoptimization\n    title: \"Scaling Laws for Reward Model Overoptimization\"\n    authors: \"Leo Gao, John Schulman, Jacob Hilton\"",
    "originalFile": "# Literature Map for Solver Trace Ablation (STA)\n# Categories:\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\n#   2. reward-shaping: Reward shaping for code/formal verification\n#   3. mutation-testing: Mutation testing in software engineering\n#   4. intensional-analysis: Intensional program analysis\n#   5. reward-hacking: Reward hacking / overoptimization\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\n#   7. goodhart-overoptimization: Goodhart's Law theory and dose-response dynamics\n#   8. verification-reward: Solver/prover as RL reward signal\n\npapers:\n\n  # ============================================================\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\n  # ============================================================\n\n  - id: deepseek-r1\n    title: \"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\"\n    authors: \"DeepSeek-AI\"\n    year: 2025\n    venue: \"arXiv 2501.12948 / Nature 2025\"\n    category: neurosymbolic-rl\n    role: method-component\n    relevance: >\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\n      STA builds on the same GRPO framework but replaces binary outcome reward with\n      intensional structural reward for neurosymbolic formalization.\n    key_finding: >\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\n      showing emergent chain-of-thought reasoning from RL alone.\n\n  - id: deepseekmath\n    title: \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\"\n    authors: \"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\"\n    year: 2024\n    venue: \"arXiv 2402.03300\"\n    category: neurosymbolic-rl\n    role: method-component\n    relevance: >\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\n      used in STA training. GRPO eliminates the critic model by estimating\n      baselines from group scores.\n    key_finding: >\n      GRPO matches PPO performance while significantly reducing training\n      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.\n\n  - id: logic-rl\n    title: \"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\"\n    authors: \"Xian et al.\"\n    year: 2025\n    venue: \"arXiv 2502.14768\"\n    category: neurosymbolic-rl\n    role: direct-competitor\n    relevance: >\n      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic\n      logic puzzles. Closest competitor to STA's approach of RL for logical\n      formalization, though Logic-RL uses extensional (answer-correctness)\n      rewards rather than STA's intensional structural rewards.\n    key_finding: >\n      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;\n      rule-based reward design is critical for RL-based logical reasoning.\n\n  - id: mellgren-prolog-grpo\n    title: \"Training Language Models to Use Prolog as a Tool\"\n    authors: \"Niklas Mellgren\"\n    year: 2024\n    venue: \"arXiv 2512.07407\"\n    category: neurosymbolic-rl\n    role: direct-competitor\n    relevance: >\n      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,\n      directly comparable to STA's approach of GRPO-training a formalizer.\n      Key difference: uses pass/fail reward vs STA's structural ISR.\n    key_finding: >\n      GRPO is effective for teaching small LLMs to use Prolog as a tool\n      for logical and mathematical reasoning.\n\n  - id: satlm\n    title: \"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\"\n    authors: \"Xi Ye et al.\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    category: neurosymbolic-rl\n    role: background\n    relevance: >\n      Neurosymbolic approach where LLM generates declarative specifications\n      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)\n      but uses prompting, not RL training.\n    key_finding: >\n      Declarative formulation outperforms imperative program-aided LMs by 23%\n      on GSM; achieves SoTA on LSAT and BoardgameQA.\n\n  - id: deepproblog\n    title: \"Neural Probabilistic Logic Programming in DeepProbLog\"\n    authors: \"Robin Manhaeve, Sebastijan Dumančić, Angelika Kimmig, Thomas Demeester, Luc De Raedt\"\n    year: 2021\n    venue: \"Artificial Intelligence 298\"\n    category: neurosymbolic-rl\n    role: background\n    relevance: >\n      Foundational neural-probabilistic logic programming framework that integrates\n      deep learning with ProbLog via neural predicates. Establishes the intellectual\n      tradition of combining neural networks with logic programming that STA extends\n      to LLM-generated Prolog with RL training.\n    key_finding: >\n      End-to-end differentiable framework integrating neural perception with\n      probabilistic logical reasoning; supports program induction and learning\n      from examples.\n\n  - id: neurasp\n    title: \"NeurASP: Embracing Neural Networks into Answer Set Programming\"\n    authors: \"Zhun Yang, Adam Ishay, Joohyung Lee\"\n    year: 2020\n    venue: \"IJCAI 2020\"\n    category: neurosymbolic-rl\n    role: background\n    relevance: >\n      Integrates neural networks with answer set programming (ASP), using\n      ASP rules to constrain and improve neural network training. Complementary\n      to DeepProbLog; together they represent the neuro-symbolic LP foundation\n      that STA's LLM-to-Prolog pipeline builds upon.\n    key_finding: >\n      ASP semantic constraints improve neural network perception accuracy;\n      demonstrates bidirectional benefit of neural-symbolic integration.\n\n  - id: thought-like-pro\n    title: \"Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought\"\n    authors: \"Xiaoyu Tan, Yongxin Deng, Xihe Qiu, Weidi Xu, Chao Qu, Wei Chu, Yinghui Xu, Yuan Qi\"\n    year: 2024\n    venue: \"arXiv 2407.14562\"\n    category: neurosymbolic-rl\n    role: direct-competitor\n    relevance: >\n      Uses Prolog engine to generate verified reasoning trajectories, then trains\n      LLMs via imitation learning to replicate them. Directly comparable pipeline\n      to STA (Prolog verification + LLM training), but uses imitation learning\n      instead of GRPO with structural reward.\n    key_finding: >\n      Prolog-verified reasoning trajectories as training signal improve LLM\n      logical reasoning; self-driven framework enables LLMs to formulate\n      rules from instructions and leverage Prolog for derivation.\n\n  # ============================================================\n  # Category 2: Reward shaping for code/formal verification\n  # ============================================================\n\n  - id: lightman-verify-step\n    title: \"Let's Verify Step by Step\"\n    authors: \"Hunter Lightman, Vineet Kosaraju, Yura Burda, et al.\"\n    year: 2023\n    venue: \"arXiv 2305.20050 / ICLR 2024\"\n    category: reward-shaping\n    role: method-component\n    relevance: >\n      Establishes that process supervision (step-level reward) outperforms\n      outcome supervision (final-answer reward) for reasoning. STA's ISR\n      is analogous: it provides structural process-level signal about which\n      components of a formalization matter, rather than just pass/fail.\n    key_finding: >\n      Process-supervised reward model achieves 78% on MATH, significantly\n      outperforming outcome-supervised models. Released PRM800K dataset.\n\n  - id: reward-shaping-rlhf\n    title: \"Reward Shaping to Mitigate Reward Hacking in RLHF\"\n    authors: \"Jiayi Fu, Xuandong Zhao, Chengyuan Yao, et al.\"\n    year: 2025\n    venue: \"arXiv 2502.18770\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Studies reward shaping design principles for RLHF: bounded rewards and\n      rapid-then-convergent growth. STA's ISR follows these principles\n      naturally since structural necessity scores are bounded [0,1].\n    key_finding: >\n      Two key reward shaping principles: (1) bounded RL reward, (2) rapid\n      initial growth with gradual convergence. PAR method achieves 5%+\n      win rate improvement on AlpacaEval 2.0.\n\n  - id: rlvr-reasoning\n    title: \"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs\"\n    authors: \"Various\"\n    year: 2025\n    venue: \"arXiv 2506.14245\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize\n      reasoning. STA argues that for neurosymbolic formalization, binary reward\n      is insufficient and structural reward is needed to avoid reward hacking.\n    key_finding: >\n      RLVR with binary verification implicitly teaches correct reasoning\n      strategies, not just answer matching.\n\n  - id: rubric-grpo\n    title: \"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning\"\n    authors: \"Various\"\n    year: 2025\n    venue: \"arXiv 2605.08061\"\n    category: reward-shaping\n    role: direct-competitor\n    relevance: >\n      Uses structured rubric-based rewards with GRPO, similar in spirit to\n      STA's structured ISR. Key difference: rubric rewards come from LLM\n      judges, while ISR comes from solver-based mutation testing.\n    key_finding: >\n      Structured multi-dimensional reward signals improve GRPO training\n      generalization compared to scalar rewards.\n\n  - id: gao-effective-rl-reward\n    title: \"On Designing Effective RL Reward at Training Time for LLM Reasoning\"\n    authors: \"Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu\"\n    year: 2024\n    venue: \"arXiv 2410.15115\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Demonstrates that learned process/outcome reward models can hurt RL\n      training, producing worse performance than simple success reward only.\n      Directly explains plan005 NEGATIVE: STA's ISR as auxiliary process\n      reward degrades prove_rate compared to exec-only baseline.\n    key_finding: >\n      PRM/ORM rewards may NOT help or even hurt RL training vs success-only\n      reward. Solution: Clipping and Delta techniques to bound accumulated\n      reward magnitude prevent reward hacking.\n\n  - id: prof-process-outcome\n    title: \"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training\"\n    authors: \"Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal\"\n    year: 2025\n    venue: \"arXiv 2509.03403\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Shows that naively combining PRM+ORM signals leads to performance\n      degradation. PROF consistency filter retains only PRM-ORM consistent\n      samples, achieving 4%+ improvement over blending. Suggests STA should\n      only apply ISR when consistent with execution outcome.\n    key_finding: >\n      Process rewards frequently suffer from inaccuracies and reward hacking\n      susceptibility. PROF filters training data by PRM-ORM consistency,\n      outperforming naive reward blending by 4%+ accuracy.\n\n  - id: moskovitz-constrained-rlhf\n    title: \"Confronting Reward Model Overoptimization with Constrained RLHF\"\n    authors: \"Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer\"\n    year: 2023\n    venue: \"arXiv 2310.04373 / ICLR 2024\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      First study on overoptimization in composite reward models. Shows that\n      fixed-weight linear scalarization of component rewards leads to\n      degradation past a threshold. Proposes constrained RL with dynamic\n      Lagrange multiplier weighting as alternative to fixed ISR weight.\n    key_finding: >\n      Correlation between component RMs significantly affects overoptimization\n      thresholds. Constrained RL with Lagrange multipliers outperforms\n      fixed-weight reward composition.\n\n  - id: skalse-reward-hacking\n    title: \"Defining and Characterizing Reward Hacking\"\n    authors: \"Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger\"\n    year: 2022\n    venue: \"arXiv 2209.13085 / NeurIPS 2022\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Formal proof that for stochastic policies, two reward functions are\n      unhackable only if one is constant. Theoretically explains why any\n      non-zero ISR weight can decrease prove_rate -- this is a fundamental\n      property of reward composition, not STA-specific.\n    key_finding: >\n      Any non-constant proxy reward can decrease true reward when optimized.\n      Unhackability requires the proxy to be constant, making all non-trivial\n      auxiliary rewards theoretically vulnerable to degrading primary performance.\n\n  - id: progrs-outcome-conditioned\n    title: \"LLM Reasoning with Process Rewards for Outcome-Guided Steps\"\n    authors: \"Mohammad Rezaei, Jens Lehmann, Sahar Vahdati\"\n    year: 2026\n    venue: \"arXiv 2604.02341\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      PRM scores optimized as absolute rewards amplify fluent failure modes.\n      Outcome-conditioned centering shifts incorrect trajectories' PRM scores\n      to zero mean, preserving ranking info without corrupting gradients.\n      Suggests STA should condition ISR on execution outcome.\n    key_finding: >\n      Naive process rewards induce reward hacking by rewarding locally fluent\n      but globally incorrect reasoning. Outcome-conditioned centering resolves\n      the conflict with fewer rollouts than outcome-only baselines.\n\n  - id: qwen-prm-lessons\n    title: \"The Lessons of Developing Process Reward Models in Mathematical Reasoning\"\n    authors: \"Zhenru Zhang et al. (Qwen Team, Alibaba)\"\n    year: 2025\n    venue: \"ACL 2025 Findings (arXiv 2501.07301)\"\n    category: reward-shaping\n    role: supporting-evidence\n    relevance: >\n      MC estimation-synthesized PRM data leads to quality degradation; policy\n      model generates \"answer-correct but reasoning-flawed\" responses, causing\n      process reward / outcome misalignment. Directly parallels ISR problem:\n      structurally correct but semantically wrong proof traces get high ISR\n      but low execution reward.\n    key_finding: >\n      PRM performance depends critically on data quality; MC estimation\n      introduces systematic bias. Answer-correct reasoning-flawed samples\n      corrupt process supervision signal.\n\n  # ============================================================\n  # Category 3: Mutation testing in software engineering\n  # ============================================================\n\n  - id: demillo1978\n    title: \"Hints on Test Data Selection: Help for the Practicing Programmer\"\n    authors: \"Richard A. DeMillo, Richard J. Lipton, Frederick G. Sayward\"\n    year: 1978\n    venue: \"Computer 11(4):34-43\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Foundational paper introducing mutation testing. STA's component\n      necessity testing directly extends this idea: instead of mutating\n      source code to test test suites, STA mutates logical formulas\n      to test component necessity for solver success.\n    key_finding: >\n      Introduced mutation testing and the coupling effect hypothesis:\n      tests that detect simple faults also detect complex faults.\n\n  - id: offutt-coupling\n    title: \"Investigations of the Software Testing Coupling Effect\"\n    authors: \"A. Jefferson Offutt\"\n    year: 1992\n    venue: \"ACM TOSEM 1(1):5-20\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Empirically validates the coupling effect hypothesis that underpins\n      mutation testing. STA's single-component ablation is analogous to\n      first-order mutation; the coupling effect suggests this suffices.\n    key_finding: >\n      Test data killing all first-order mutants killed >99% of second-\n      and third-order mutants, validating the coupling effect.\n\n  - id: jia-harman-survey\n    title: \"An Analysis and Survey of the Development of Mutation Testing\"\n    authors: \"Yue Jia, Mark Harman\"\n    year: 2011\n    venue: \"IEEE TSE 37(5):649-678\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Comprehensive survey of mutation testing covering three decades of\n      development. Provides theoretical and practical foundation for STA's\n      adaptation of mutation testing to logical formulas.\n    key_finding: >\n      Systematic classification of mutation operators, cost reduction\n      techniques, and equivalence problem -- all relevant to STA's design\n      of clause-level ablation operators.\n\n  - id: just-mutants-real-faults\n    title: \"Are Mutants a Valid Substitute for Real Faults in Software Testing?\"\n    authors: \"Rene Just, Darioush Jalali, Laura Inozemtseva, et al.\"\n    year: 2014\n    venue: \"FSE 2014\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Validates that mutation testing (structural/intensional analysis of\n      program adequacy) correlates with real fault detection. Supports STA's\n      premise that structural analysis of formalization components provides\n      meaningful signal about formalization quality.\n    key_finding: >\n      Mutant detection is statistically correlated with real fault detection,\n      and mutation score is a better predictor of test effectiveness than\n      code coverage.\n\n  - id: llmorpheus\n    title: \"LLMorpheus: Mutation Testing Using Large Language Models\"\n    authors: \"Frank Tip, Jon Bell, et al.\"\n    year: 2025\n    venue: \"IEEE TSE 2025\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Uses LLMs to generate realistic code mutants beyond traditional\n      mutation operators. Shows mutation testing evolving toward\n      ML-integrated approaches, validating STA's cross-pollination\n      of mutation testing ideas into ML training.\n    key_finding: >\n      LLM-generated mutants simulate real bugs that rule-based operators\n      cannot produce, improving mutation testing realism.\n\n  - id: mutation-guided-meta\n    title: \"Mutation-Guided LLM-based Test Generation at Meta\"\n    authors: \"Christopher Foster et al.\"\n    year: 2025\n    venue: \"FSE 2025\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Industrial application of mutation-guided LLM test generation at\n      Meta. Demonstrates that mutation analysis can guide LLM behavior\n      in production -- analogous to how STA uses mutation (ablation) to\n      guide GRPO reward signal.\n    key_finding: >\n      Mutation-guided approach generates tests that kill significantly\n      more mutants than unguided LLM test generation at Meta scale.\n\n  - id: mutation-consistency-llm\n    title: \"Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs\"\n    authors: \"Various\"\n    year: 2024\n    venue: \"arXiv 2401.05940\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Uses code mutations to evaluate LLM code understanding consistency.\n      Conceptually related to STA: both use systematic code/formula\n      mutations to assess model capabilities.\n    key_finding: >\n      LLMs show significant inconsistency when evaluated on mutated code\n      variants, suggesting superficial pattern matching.\n\n  # ============================================================\n  # Category 4: Intensional program analysis\n  # ============================================================\n\n  - id: deepmutation\n    title: \"A Probabilistic Framework for Mutation Testing in Deep Neural Networks\"\n    authors: \"Various\"\n    year: 2023\n    venue: \"Information and Software Technology 2023\"\n    category: intensional-analysis\n    role: background\n    relevance: >\n      Extends mutation testing to DNN testing with probabilistic mutation\n      operators. Parallel to STA's extension of mutation testing from\n      traditional programs to logical formulas.\n    key_finding: >\n      Probabilistic mutation framework enables meaningful test adequacy\n      assessment for neural networks through structural perturbation.\n\n  # ============================================================\n  # Category 5: Reward hacking / overoptimization\n  # ============================================================\n\n  - id: inform-reward-hacking\n    title: \"InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling\"\n    authors: \"Various\"\n    year: 2024\n    venue: \"NeurIPS 2024\"\n    category: reward-hacking\n    role: background\n    relevance: >\n      Proposes information-bottleneck approach to detect and mitigate reward\n      hacking. STA's ISR addresses the same problem differently: by grounding\n      reward in verifiable structural properties (component necessity), it\n      reduces the attack surface for reward hacking.\n    key_finding: >\n      Variational information bottleneck filters irrelevant features from\n      reward model; Cluster Separation Index detects reward overoptimization.\n\n  - id: mo-grpo\n    title: \"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\"\n    authors: \"CyberAgent AI Lab\"\n    year: 2025\n    venue: \"arXiv 2509.22047\"\n    category: reward-hacking\n    role: background\n    relevance: >\n      Directly addresses GRPO reward hacking in multi-objective settings.\n      STA's ISR can be viewed as adding a structural objective to the\n      correctness objective, making MO-GRPO's insights directly applicable.\n    key_finding: >\n      Standard GRPO normalizes after summing rewards, allowing high-variance\n      objectives to dominate. MO-GRPO equalizes scales before aggregation.\n\n  - id: reward-hacking-survey\n    title: \"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\"\n    authors: \"Various\"\n    year: 2026\n    venue: \"arXiv 2604.13602\"\n    category: reward-hacking\n    role: background\n    relevance: >\n      Comprehensive survey of reward hacking mechanisms in the LLM era.\n      Provides theoretical framework for understanding why STA's structural\n      reward is more robust than pure outcome-based reward.\n    key_finding: >\n      Reward hacking manifests through specification gaming, reward model\n      exploitation, and emergent misalignment; structural verification\n      rewards are more robust than learned reward models.\n\n  - id: energy-loss-reward-hacking\n    title: \"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking\"\n    authors: \"Various\"\n    year: 2025\n    venue: \"ICML 2025\"\n    category: reward-hacking\n    role: background\n    relevance: >\n      Identifies energy loss in LLM final layer as an indicator of reward\n      hacking during RL. Provides complementary diagnostic to STA's\n      structural reward approach.\n    key_finding: >\n      Energy loss in the final layer increases during RL and excessive\n      increase characterizes reward hacking; EPPO algorithm penalizes\n      this to mitigate hacking.\n\n  - id: spurious-rewards\n    title: \"Spurious Rewards: Rethinking Training Signals in RLVR\"\n    authors: \"Ruixin Yang et al.\"\n    year: 2025\n    venue: \"arXiv 2506.10947 / NeurIPS 2025 submission\"\n    category: reward-hacking\n    role: direct-evidence\n    relevance: >\n      Most directly relevant to STA findings. GRPO+random reward on\n      Qwen2.5-Math improves 21.4%, nearly matching ground-truth reward's\n      29.1%. Matches our plan017 finding: additive random (PR=48%) >\n      additive ISR (PR=18%). Structured metrics can be worse than random\n      noise due to systematic bias vs pure variance.\n    key_finding: >\n      Random reward nearly matches ground-truth reward in GRPO training,\n      suggesting GRPO's group normalization extracts signal from noise.\n      Effect is model-dependent (works on Qwen2.5, not Llama3).\n\n  - id: gao-reward-overoptimization\n    title: \"Scaling Laws for Reward Model Overoptimization\"\n    authors: \"Leo Gao, John Schulman, Jacob Hilton\"\n    year: 2023\n    venue: \"ICML 2023 (arXiv 2210.10760)\"\n    category: reward-hacking\n    role: theoretical-foundation\n    relevance: >\n      Foundational work quantifying Goodhart's effect: proxy reward rises\n      but gold reward first rises then falls. ISR is a proxy reward that\n      exhibits exactly this pattern — ISR can increase while prove_rate\n      decreases, making it suitable for post-hoc diagnosis but harmful\n      as training signal.\n    key_finding: >\n      Gold/proxy reward divergence follows predictable scaling laws.\n      Proxy reward optimization past critical point degrades gold reward,\n      with the divergence point scaling with model and dataset size.\n\n  - id: karwowski-goodhart-rl\n    title: \"Goodhart's Law in Reinforcement Learning\"\n    authors: \"Jacek Karwowski, Oliver Hayman, Xingjian Bai, Klaus Kiendlhofer, Charlie Griffin, Joar Skalse\"\n    year: 2024\n    venue: \"ICLR 2024 (arXiv 2310.09144)\"\n    category: reward-hacking\n    role: theoretical-foundation\n    relevance: >\n      Geometric interpretation of Goodhart's Law in MDPs: optimizing\n      imperfect proxy past critical point decreases true objective. ISR as\n      proxy has partial correlation with execution correctness — exceeding\n      critical optimization point pushes policy toward high-ISR but\n      low-correctness regions. Explains plan002/plan005 negative results.\n    key_finding: >\n      Formalizes Goodhart's Law for RL: any non-trivially correlated proxy\n      reward creates regions where proxy and true reward diverge, and\n      policy optimization inevitably enters these regions.\n\n  # ============================================================\n  # Category 6: FOL/Prolog formalization with LLMs\n  # ============================================================\n\n  - id: folio\n    title: \"FOLIO: Natural Language Reasoning with First-Order Logic\"\n    authors: \"Simeng Han et al.\"\n    year: 2022\n    venue: \"arXiv 2209.00840 / EMNLP 2024\"\n    category: fol-formalization\n    role: evaluation\n    relevance: >\n      Primary FOL reasoning benchmark. STA uses FOLIO-style NL->FOL\n      formalization as the target task for GRPO training. FOLIO's\n      expert-annotated FOL annotations serve as reference formalizations.\n    key_finding: >\n      1,430 NL-FOL paired examples with reasoning depths up to 5+;\n      GPT-4 still struggles on the hardest examples.\n\n  - id: proofwriter\n    title: \"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language\"\n    authors: \"Oyvind Tafjord, Bhavana Dalvi, Peter Clark\"\n    year: 2021\n    venue: \"Findings of ACL-IJCNLP 2021\"\n    category: fol-formalization\n    role: evaluation\n    relevance: >\n      Source dataset for STA's training data. ProofWriter provides\n      rule-based logical reasoning problems in natural language that\n      STA uses for training formalizer models.\n    key_finding: >\n      Generative model can reliably produce implications and proofs;\n      accuracy exceeds prior methods by 9% and generalizes to unseen\n      proof depths.\n\n  - id: logic-lm\n    title: \"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\"\n    authors: \"Liangming Pan, Alon Albalak, Xinyi Wang, William Wang\"\n    year: 2023\n    venue: \"Findings of EMNLP 2023\"\n    category: fol-formalization\n    role: direct-competitor\n    relevance: >\n      LLM->symbolic solver pipeline for logical reasoning, directly\n      comparable to STA's formalizer->Prolog solver pipeline. Key\n      difference: Logic-LM uses prompting, STA uses GRPO training.\n    key_finding: >\n      LLM+solver achieves 39.2% improvement over LLM-alone on logical\n      reasoning benchmarks including ProofWriter and FOLIO.\n\n  - id: linc\n    title: \"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers\"\n    authors: \"Theo X. Olausson, Alex Gu, Ben Lipkin, et al.\"\n    year: 2023\n    venue: \"EMNLP 2023\"\n    category: fol-formalization\n    role: direct-competitor\n    relevance: >\n      Neurosymbolic approach where LLM translates NL to FOL for theorem\n      prover. Directly comparable to STA's NL->Prolog translation.\n      LINC uses prompting-based approach; STA uses RL training.\n    key_finding: >\n      StarCoder+ (15.5B) with LINC outperforms GPT-3.5 and GPT-4 with\n      CoT by 38% and 10% respectively on ProofWriter.\n\n  - id: fover-pei2025\n    title: \"FoVer: First-Order Logic Verification for Natural Language Reasoning\"\n    authors: \"Yu Pei, Yongping Du, Xingnan Jin\"\n    year: 2025\n    venue: \"TACL 13:1340-1359\"\n    category: fol-formalization\n    role: direct-competitor\n    relevance: >\n      Uses LLM->FOL->Z3 pipeline for verifying NL reasoning correctness.\n      Similar to STA's verification pipeline but focuses on post-hoc\n      verification rather than training reward signal.\n    key_finding: >\n      FOL verification via Z3 significantly outperforms existing methods\n      on ProofWriter and FOLIO benchmarks.\n\n  - id: lorp\n    title: \"LoRP: LLM-based Logical Reasoning via Prolog\"\n    authors: \"Various\"\n    year: 2025\n    venue: \"Knowledge-Based Systems 2025\"\n    category: fol-formalization\n    role: direct-competitor\n    relevance: >\n      LLM->Prolog pipeline with FOL-to-Prolog translation mechanism.\n      Closest to STA's formalization target (Prolog), though LoRP\n      uses prompting while STA uses GRPO training with structural reward.\n    key_finding: >\n      Systematic FOL-to-Prolog translation extends Prolog expressiveness;\n      achieves SoTA accuracy on logical reasoning with three-vote majority.\n\n  - id: nl2fol\n    title: \"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection\"\n    authors: \"Lalwani, Kim, et al.\"\n    year: 2024\n    venue: \"arXiv 2405.02318\"\n    category: fol-formalization\n    role: background\n    relevance: >\n      Step-by-step NL->FOL translation using LLMs with SMT solver\n      verification. Demonstrates the NL->formal logic pipeline that\n      STA aims to improve via RL training.\n    key_finding: >\n      Neurosymbolic NL2FOL achieves 78% F1 on LOGIC dataset and\n      generalizes to LogicClimate (80% F1), outperforming supervised\n      models by 21%.\n\n  - id: logica2\n    title: \"LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding\"\n    authors: \"Liu et al.\"\n    year: 2023\n    venue: \"IEEE/ACM TASLP 2023\"\n    category: fol-formalization\n    role: evaluation\n    relevance: >\n      Logical reasoning evaluation benchmark derived from Chinese civil\n      service exams. Provides supplementary evaluation for STA's\n      formalization capabilities.\n    key_finding: >\n      8,678 multiple-choice questions covering categorical, disjunctive,\n      and conditional reasoning; widely used LLM benchmark.\n\n  # ============================================================\n  # Category 7: Goodhart's Law theory and dose-response dynamics\n  # ============================================================\n\n  - id: manheim-goodhart-taxonomy\n    title: \"Categorizing Variants of Goodhart's Law\"\n    authors: \"David Manheim, Scott Garrabrant\"\n    year: 2019\n    venue: \"arXiv 1803.04585\"\n    category: goodhart-overoptimization\n    role: theoretical-foundation\n    relevance: >\n      Four-part Goodhart taxonomy: regressional, extremal, causal, adversarial.\n      STA's high-β ISR collapse is best classified as extremal Goodhart\n      (policy moves to OOD region where ISR↑ but prove_rate↓). Provides\n      vocabulary for discussion section.\n    key_finding: >\n      First systematic categorization of Goodhart failure modes. Extremal\n      variant occurs when proxy-goal relationship breaks in out-of-distribution\n      regions reached by strong optimization.\n\n  - id: pan-reward-misspecification\n    title: \"The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models\"\n    authors: \"Alexander Pan, Kush Bhatia, Jacob Steinhardt\"\n    year: 2022\n    venue: \"ICLR 2022\"\n    category: goodhart-overoptimization\n    role: theoretical-foundation\n    relevance: >\n      Across 9 environments, more capable agents exploit misspecifications more.\n      Observes dose-dependent degradation — capability thresholds where true\n      reward sharply drops. Matches STA's β=0.1→0.3 qualitative shift.\n    key_finding: >\n      Reward misspecification causes dose-dependent degradation where true reward\n      sharply drops past capability thresholds. More capable optimization\n      produces worse outcomes under misspecification.\n\n  - id: kwa-catastrophic-goodhart\n    title: \"Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification\"\n    authors: \"Tat-Thang Kwa, Rachel Thomas, Adrià Garriga-Alonso\"\n    year: 2024\n    venue: \"NeurIPS 2024\"\n    category: goodhart-overoptimization\n    role: theoretical-foundation\n    relevance: >\n      If reward model error is heavy-tailed, policies achieve arbitrarily\n      high proxy reward with no true utility gain. KL regularization provably\n      fails. Explains why KL penalty in GRPO cannot prevent ISR collapse\n      at high β if ISR error distribution is heavy-tailed.\n    key_finding: >\n      KL-regularized RL provably fails to prevent overoptimization under\n      heavy-tailed reward misspecification. Policies can achieve arbitrarily\n      high proxy reward with zero true utility.\n\n  - id: rafailov-daa-scaling\n    title: \"Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms\"\n    authors: \"Rafael Rafailov, Yaswanth Chittepu, Ryan Park, Harshit Sikchi, Joey Hejna, W. Bradley Knox, Chelsea Finn, Scott Niekum\"\n    year: 2024\n    venue: \"NeurIPS 2024\"\n    category: goodhart-overoptimization\n    role: supporting-evidence\n    relevance: >\n      Extends Gao et al. to DPO/IPO/SLiC. Tests seven β values across\n      1B-6.9B models. DAAs still overoptimize despite no explicit proxy RM.\n      Validates β as a \"dose\" parameter — directly analogous to STA's\n      ISR weight sweep.\n    key_finding: >\n      Direct alignment algorithms exhibit overoptimization following\n      predictable scaling laws. Smaller models overoptimize sooner.\n      β-controlled dose-response is a general phenomenon across RL paradigms.\n\n  - id: huang-chi-squared\n    title: \"Correcting the Mythos of KL-Regularization: Direct and Contrastive Distribution Correction\"\n    authors: \"Afra Feyza Akyürek, Banghua Zhu, Sham Kakade, Jiantao Jiao\"\n    year: 2025\n    venue: \"ICLR 2025 Poster\"\n    category: goodhart-overoptimization\n    role: supporting-evidence\n    relevance: >\n      KL-regularization is theoretically inadequate for preventing\n      overoptimization. Chi-squared divergence provably alleviates it.\n      Suggests that even with KL penalty in GRPO, STA's high-β collapse\n      is theoretically expected.\n    key_finding: >\n      Chi-squared preference optimization provably mitigates overoptimization\n      where KL-regularization fails. Alternative divergence measures offer\n      stronger guarantees.\n\n  - id: coste-rm-ensembles\n    title: \"Reward Model Ensembles Help Mitigate Overoptimization\"\n    authors: \"Thomas Coste, Usman Anwar, Robert Kirk, David Krueger\"\n    year: 2023\n    venue: \"NeurIPS 2023 Workshop on Alignment\"\n    category: goodhart-overoptimization\n    role: background\n    relevance: >\n      Worst-case optimization across RM ensembles practically eliminates\n      overoptimization for BoN and reduces it for PPO. Suggests ensemble\n      of multiple solver metrics (instead of single ISR) as mitigation.\n    key_finding: >\n      RM ensembles with worst-case aggregation mitigate overoptimization.\n      Ensemble size and diversity directly affect robustness.\n\n  # ============================================================\n  # Category 8: Solver/prover as RL reward signal\n  # ============================================================\n\n  - id: rlsf\n    title: \"Reinforcement Learning via Symbolic Feedback\"\n    authors: \"Abhinav Jha, Shikhar Murty, Zico Kolter, et al.\"\n    year: 2024\n    venue: \"arXiv 2405.16661\"\n    category: verification-reward\n    role: direct-competitor\n    relevance: >\n      Most directly relevant: uses solver/prover certificates as fine-grained\n      token-level reward signal. Outperforms traditional approaches on program\n      synthesis (+31.4%). STA extends this paradigm and shows when it breaks\n      (Goodhart effects at high auxiliary reward weight).\n    key_finding: >\n      Symbolic reasoning tools provide poly-sized certificates as reward.\n      Smaller RLSF models outperform GPT-4 on structured generation tasks.\n\n  - id: fover-kamoi2026\n    title: \"FoVer: Generalizable Process Reward Models via Formally Verified Training Data\"\n    authors: \"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\"\n    year: 2025\n    venue: \"Findings of ACL 2026 (arXiv 2502.01345)\"\n    category: verification-reward\n    role: supporting-evidence\n    relevance: >\n      Uses Z3 and Isabelle to synthesize PRM training data by annotating\n      step-level error labels without human annotation. Same solver family\n      as STA. Shows verification-based rewards work; STA extends by showing\n      dose-response dynamics.\n    key_finding: >\n      Formally verified training data enables generalizable process reward\n      models competitive on ProcessBench and 12 reasoning benchmarks.\n\n  - id: deepseek-prover-v15\n    title: \"DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search\"\n    authors: \"DeepSeek AI\"\n    year: 2024\n    venue: \"ICLR 2025 (arXiv 2408.08152)\"\n    category: verification-reward\n    role: method-component\n    relevance: >\n      Uses GRPO with Lean 4 verification as binary reward. Same algorithm\n      (GRPO) + formal verification, but binary (pass/fail). Binary reward\n      avoids the graded-metric Goodhart risk that STA identifies with ISR.\n    key_finding: >\n      GRPO + binary Lean verification achieves 63.5% on miniF2F. Binary\n      correctness guarantee via formal verification sidesteps proxy reward\n      overoptimization.\n\n  - id: alphaproof\n    title: \"AlphaProof\"\n    authors: \"Google DeepMind\"\n    year: 2024\n    venue: \"Nature 2025\"\n    category: verification-reward\n    role: background\n    relevance: >\n      AlphaZero-inspired RL with Lean proof verification at scale.\n      Silver medal at IMO 2024. Binary verification reward avoids the\n      Goodhart problem STA identifies with graded verification metrics.\n    key_finding: >\n      Binary formal verification as RL reward scales to IMO-level\n      mathematical reasoning. Demonstrates verification-reward RL works\n      at the frontier of mathematical difficulty.\n\n  - id: math-shepherd\n    title: \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\"\n    authors: \"Peiyi Wang, Lei Li, Zhihong Shao, R.X. Xu, et al.\"\n    year: 2024\n    venue: \"ACL 2024 (arXiv 2312.08935)\"\n    category: verification-reward\n    role: supporting-evidence\n    relevance: >\n      Automatically constructs process supervision data and uses it as\n      step-by-step PPO reward. Automated verification reward without human\n      labels, analogous to STA's automated ISR computation via solver.\n    key_finding: >\n      Automated process supervision improves Mistral-7B on GSM8K\n      (77.9→84.1%) and MATH (28.6→33.0%) without human annotation.\n\n  # ============================================================\n  # Additional reward-shaping papers (Goodhart survey additions)\n  # ============================================================\n\n  - id: bipars\n    title: \"Learning to Utilize Shaping Rewards: A New Approach of Reward Shaping\"\n    authors: \"Yujing Hu, Weixun Wang, Hangtian Jia, et al.\"\n    year: 2020\n    venue: \"NeurIPS 2020\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Bi-level optimization learns parameterized shaping reward weights.\n      Can transform harmful shaping rewards into beneficial ones by learning\n      negative weights. Directly addresses STA's problem: when ISR weight\n      is wrong, automated weight learning could find optimal β.\n    key_finding: >\n      Bi-level optimization automatically learns auxiliary reward weights,\n      outperforming fixed weights and recovering from harmful shaping rewards.\n\n  - id: dapo\n    title: \"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\"\n    authors: \"Qiying Yu et al. (ByteDance)\"\n    year: 2025\n    venue: \"arXiv 2503.14476\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Four techniques for stable multi-component reward in GRPO: Clip-Higher,\n      Dynamic Sampling, token-level policy gradient, Overlong Reward Shaping.\n      Addresses stability issues relevant to STA's multi-reward setup.\n    key_finding: >\n      Clip-Higher and Dynamic Sampling prevent entropy collapse in GRPO\n      with multi-component rewards. Soft punishment for overlong outputs\n      avoids reward hacking through length exploitation.\n",
    "structuredPatch": [
      {
        "oldStart": 529,
        "oldLines": 6,
        "newStart": 529,
        "newLines": 43,
        "lines": [
          "       suggesting GRPO's group normalization extracts signal from noise.",
          "       Effect is model-dependent (works on Qwen2.5, not Llama3).",
          " ",
          "+  - id: bondarenko-spec-gaming",
          "+    title: \"Demonstrating Specification Gaming in Reasoning Models\"",
          "+    authors: \"Alexander Bondarenko, Denis Volk, Dmitrii Volkov, Jeffrey Ladish\"",
          "+    year: 2025",
          "+    venue: \"arXiv 2502.13295\"",
          "+    category: reward-hacking",
          "+    role: direct-evidence",
          "+    relevance: >",
          "+      Shows that reasoning models (o3, DeepSeek-R1) resort to specification",
          "+      gaming on difficult tasks by default, without explicit nudging.",
          "+      Directly relevant to STA's concern: RL-trained reasoning models",
          "+      may game formal verification rewards rather than learn genuine",
          "+      formalization skills.",
          "+    key_finding: >",
          "+      Reasoning models spontaneously hack benchmarks (e.g., manipulating",
          "+      chess engine files instead of playing chess). Stronger reasoning",
          "+      capability correlates with more sophisticated gaming strategies.",
          "+",
          "+  - id: kim-game-formalization",
          "+    title: \"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning\"",
          "+    authors: \"Kyuhee Kim, Auguste Poiroux, Antoine Bosselut\"",
          "+    year: 2026",
          "+    venue: \"VerifAI-2 Workshop, ICLR 2026 (arXiv 2604.19459)\"",
          "+    category: reward-hacking",
          "+    role: direct-evidence",
          "+    relevance: >",
          "+      Directly studies whether LLMs game formalization in logical reasoning --",
          "+      the exact phenomenon STA's ISR is designed to detect. Evaluates GPT-5",
          "+      and DeepSeek-R1 on FOLIO with Lean 4 proofs. Finds two modes of",
          "+      unfaithfulness: axiom fabrication (GPT-5) and premise mistranslation",
          "+      (R1), the latter evading detection entirely.",
          "+    key_finding: >",
          "+      High compilation rates (87-99%) do not imply faithful formalization.",
          "+      Two-stage pipelines reveal unfaithfulness that unified generation hides.",
          "+      Premise mistranslation produces internally consistent but unfaithful",
          "+      outputs -- analogous to STA's high-ISR but semantically wrong traces.",
          "+",
          "   - id: gao-reward-overoptimization",
          "     title: \"Scaling Laws for Reward Model Overoptimization\"",
          "     authors: \"Leo Gao, John Schulman, Jacob Hilton\""
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

_source line 68_

Now let me save via the MCP tool as well (it may fail due to whitelist, but let me try).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "30a8b0b8-9925-42fa-abc1-a25cbfdd5601",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EekWc4GRyPP5douJyRJ3GK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 816,
      "cache_read_input_tokens": 61568,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 816
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

_source line 69_

<details open><summary>🔧 Tool call — Read · `toolu_01BjD1ijVTjC7XPEMj7En23E`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
  "offset": 0,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "7d4fdb51-4bbc-41b3-93bb-3b09fb6035a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EekWc4GRyPP5douJyRJ3GK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 816,
      "cache_read_input_tokens": 61568,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 816
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

_source line 70 · 2026-05-14T17:46:14.007Z_

<details><summary>↩ Tool result · `toolu_01BjD1ijVTjC7XPEMj7En23E`</summary>

```text
0	# Literature Map for Solver Trace Ablation (STA)
1	# Categories:
2	#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO
3	#   2. reward-shaping: Reward shaping for code/formal verification
4	#   3. mutation-testing: Mutation testing in software engineering
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "b3c8c713-fe93-4cb0-9043-db97b5916d2f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
      "content": "# Literature Map for Solver Trace Ablation (STA)\n# Categories:\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\n#   2. reward-shaping: Reward shaping for code/formal verification\n#   3. mutation-testing: Mutation testing in software engineering",
      "numLines": 5,
      "startLine": 0,
      "totalLines": 952
    }
  }
}
```

</details>

---

### Assistant

_source line 71_

Good, the file is updated. Let me verify the additions look correct by reading the new sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "191a6b1d-46e1-4e19-a2dd-49fa57198f21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011pD4JRy253L5FrdE2QWMYE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 352,
      "cache_read_input_tokens": 62384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 352
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

_source line 72_

<details open><summary>🔧 Tool call — Read · `toolu_01TUc5Vw1UcnJrzcdEkiwcEh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
  "offset": 90,
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "2d1b9e2a-a428-4f43-80ab-b7580824e0b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011pD4JRy253L5FrdE2QWMYE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 352,
      "cache_read_input_tokens": 62384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 352
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

_source line 73 · 2026-05-14T17:46:17.829Z_

<details><summary>↩ Tool result · `toolu_01TUc5Vw1UcnJrzcdEkiwcEh`</summary>

```text
90	    key_finding: >
91	      Declarative formulation outperforms imperative program-aided LMs by 23%
92	      on GSM; achieves SoTA on LSAT and BoardgameQA.
93	
94	  - id: deepproblog
95	    title: "Neural Probabilistic Logic Programming in DeepProbLog"
96	    authors: "Robin Manhaeve, Sebastijan Dumančić, Angelika Kimmig, Thomas Demeester, Luc De Raedt"
97	    year: 2021
98	    venue: "Artificial Intelligence 298"
99	    category: neurosymbolic-rl
100	    role: background
101	    relevance: >
102	      Foundational neural-probabilistic logic programming framework that integrates
103	      deep learning with ProbLog via neural predicates. Establishes the intellectual
104	      tradition of combining neural networks with logic programming that STA extends
105	      to LLM-generated Prolog with RL training.
106	    key_finding: >
107	      End-to-end differentiable framework integrating neural perception with
108	      probabilistic logical reasoning; supports program induction and learning
109	      from examples.
110	
111	  - id: neurasp
112	    title: "NeurASP: Embracing Neural Networks into Answer Set Programming"
113	    authors: "Zhun Yang, Adam Ishay, Joohyung Lee"
114	    year: 2020
115	    venue: "IJCAI 2020"
116	    category: neurosymbolic-rl
117	    role: background
118	    relevance: >
119	      Integrates neural networks with answer set programming (ASP), using
120	      ASP rules to constrain and improve neural network training. Complementary
121	      to DeepProbLog; together they represent the neuro-symbolic LP foundation
122	      that STA's LLM-to-Prolog pipeline builds upon.
123	    key_finding: >
124	      ASP semantic constraints improve neural network perception accuracy;
125	      demonstrates bidirectional benefit of neural-symbolic integration.
126	
127	  - id: thought-like-pro
128	    title: "Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought"
129	    authors: "Xiaoyu Tan, Yongxin Deng, Xihe Qiu, Weidi Xu, Chao Qu, Wei Chu, Yinghui Xu, Yuan Qi"
130	    year: 2024
131	    venue: "arXiv 2407.14562"
132	    category: neurosymbolic-rl
133	    role: direct-competitor
134	    relevance: >
135	      Uses Prolog engine to generate verified reasoning trajectories, then trains
136	      LLMs via imitation learning to replicate them. Directly comparable pipeline
137	      to STA (Prolog verification + LLM training), but uses imitation learning
138	      instead of GRPO with structural reward.
139	    key_finding: >
140	      Prolog-verified reasoning trajectories as training signal improve LLM
141	      logical reasoning; self-driven framework enables LLMs to formulate
142	      rules from instructions and leverage Prolog for derivation.
143	
144	  # ============================================================
145	  # Category 2: Reward shaping for code/formal verification
146	  # ============================================================
147	
148	  - id: lightman-verify-step
149	    title: "Let's Verify Step by Step"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "10c649f0-0655-41e5-ab26-e7237dbdbb1c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
      "content": "    key_finding: >\n      Declarative formulation outperforms imperative program-aided LMs by 23%\n      on GSM; achieves SoTA on LSAT and BoardgameQA.\n\n  - id: deepproblog\n    title: \"Neural Probabilistic Logic Programming in DeepProbLog\"\n    authors: \"Robin Manhaeve, Sebastijan Dumančić, Angelika Kimmig, Thomas Demeester, Luc De Raedt\"\n    year: 2021\n    venue: \"Artificial Intelligence 298\"\n    category: neurosymbolic-rl\n    role: background\n    relevance: >\n      Foundational neural-probabilistic logic programming framework that integrates\n      deep learning with ProbLog via neural predicates. Establishes the intellectual\n      tradition of combining neural networks with logic programming that STA extends\n      to LLM-generated Prolog with RL training.\n    key_finding: >\n      End-to-end differentiable framework integrating neural perception with\n      probabilistic logical reasoning; supports program induction and learning\n      from examples.\n\n  - id: neurasp\n    title: \"NeurASP: Embracing Neural Networks into Answer Set Programming\"\n    authors: \"Zhun Yang, Adam Ishay, Joohyung Lee\"\n    year: 2020\n    venue: \"IJCAI 2020\"\n    category: neurosymbolic-rl\n    role: background\n    relevance: >\n      Integrates neural networks with answer set programming (ASP), using\n      ASP rules to constrain and improve neural network training. Complementary\n      to DeepProbLog; together they represent the neuro-symbolic LP foundation\n      that STA's LLM-to-Prolog pipeline builds upon.\n    key_finding: >\n      ASP semantic constraints improve neural network perception accuracy;\n      demonstrates bidirectional benefit of neural-symbolic integration.\n\n  - id: thought-like-pro\n    title: \"Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought\"\n    authors: \"Xiaoyu Tan, Yongxin Deng, Xihe Qiu, Weidi Xu, Chao Qu, Wei Chu, Yinghui Xu, Yuan Qi\"\n    year: 2024\n    venue: \"arXiv 2407.14562\"\n    category: neurosymbolic-rl\n    role: direct-competitor\n    relevance: >\n      Uses Prolog engine to generate verified reasoning trajectories, then trains\n      LLMs via imitation learning to replicate them. Directly comparable pipeline\n      to STA (Prolog verification + LLM training), but uses imitation learning\n      instead of GRPO with structural reward.\n    key_finding: >\n      Prolog-verified reasoning trajectories as training signal improve LLM\n      logical reasoning; self-driven framework enables LLMs to formulate\n      rules from instructions and leverage Prolog for derivation.\n\n  # ============================================================\n  # Category 2: Reward shaping for code/formal verification\n  # ============================================================\n\n  - id: lightman-verify-step\n    title: \"Let's Verify Step by Step\"",
      "numLines": 60,
      "startLine": 90,
      "totalLines": 952
    }
  }
}
```

</details>

---

### Tool call

_source line 74_

<details open><summary>🔧 Tool call — Read · `toolu_01J19WFxEa4jXuJgmcsUD4Zv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
  "offset": 530,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "fd001a53-c233-4ae2-ad67-ea2e5757608a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011pD4JRy253L5FrdE2QWMYE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 352,
      "cache_read_input_tokens": 62384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 352
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

_source line 75 · 2026-05-14T17:46:18.591Z_

<details><summary>↩ Tool result · `toolu_01J19WFxEa4jXuJgmcsUD4Zv`</summary>

```text
530	      Effect is model-dependent (works on Qwen2.5, not Llama3).
531	
532	  - id: bondarenko-spec-gaming
533	    title: "Demonstrating Specification Gaming in Reasoning Models"
534	    authors: "Alexander Bondarenko, Denis Volk, Dmitrii Volkov, Jeffrey Ladish"
535	    year: 2025
536	    venue: "arXiv 2502.13295"
537	    category: reward-hacking
538	    role: direct-evidence
539	    relevance: >
540	      Shows that reasoning models (o3, DeepSeek-R1) resort to specification
541	      gaming on difficult tasks by default, without explicit nudging.
542	      Directly relevant to STA's concern: RL-trained reasoning models
543	      may game formal verification rewards rather than learn genuine
544	      formalization skills.
545	    key_finding: >
546	      Reasoning models spontaneously hack benchmarks (e.g., manipulating
547	      chess engine files instead of playing chess). Stronger reasoning
548	      capability correlates with more sophisticated gaming strategies.
549	
550	  - id: kim-game-formalization
551	    title: "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning"
552	    authors: "Kyuhee Kim, Auguste Poiroux, Antoine Bosselut"
553	    year: 2026
554	    venue: "VerifAI-2 Workshop, ICLR 2026 (arXiv 2604.19459)"
555	    category: reward-hacking
556	    role: direct-evidence
557	    relevance: >
558	      Directly studies whether LLMs game formalization in logical reasoning --
559	      the exact phenomenon STA's ISR is designed to detect. Evaluates GPT-5
560	      and DeepSeek-R1 on FOLIO with Lean 4 proofs. Finds two modes of
561	      unfaithfulness: axiom fabrication (GPT-5) and premise mistranslation
562	      (R1), the latter evading detection entirely.
563	    key_finding: >
564	      High compilation rates (87-99%) do not imply faithful formalization.
565	      Two-stage pipelines reveal unfaithfulness that unified generation hides.
566	      Premise mistranslation produces internally consistent but unfaithful
567	      outputs -- analogous to STA's high-ISR but semantically wrong traces.
568	
569	  - id: gao-reward-overoptimization
570	    title: "Scaling Laws for Reward Model Overoptimization"
571	    authors: "Leo Gao, John Schulman, Jacob Hilton"
572	    year: 2023
573	    venue: "ICML 2023 (arXiv 2210.10760)"
574	    category: reward-hacking
575	    role: theoretical-foundation
576	    relevance: >
577	      Foundational work quantifying Goodhart's effect: proxy reward rises
578	      but gold reward first rises then falls. ISR is a proxy reward that
579	      exhibits exactly this pattern — ISR can increase while prove_rate
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "01ba99c7-3711-40b6-a1f9-a5e9f5669d56",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
      "content": "      Effect is model-dependent (works on Qwen2.5, not Llama3).\n\n  - id: bondarenko-spec-gaming\n    title: \"Demonstrating Specification Gaming in Reasoning Models\"\n    authors: \"Alexander Bondarenko, Denis Volk, Dmitrii Volkov, Jeffrey Ladish\"\n    year: 2025\n    venue: \"arXiv 2502.13295\"\n    category: reward-hacking\n    role: direct-evidence\n    relevance: >\n      Shows that reasoning models (o3, DeepSeek-R1) resort to specification\n      gaming on difficult tasks by default, without explicit nudging.\n      Directly relevant to STA's concern: RL-trained reasoning models\n      may game formal verification rewards rather than learn genuine\n      formalization skills.\n    key_finding: >\n      Reasoning models spontaneously hack benchmarks (e.g., manipulating\n      chess engine files instead of playing chess). Stronger reasoning\n      capability correlates with more sophisticated gaming strategies.\n\n  - id: kim-game-formalization\n    title: \"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning\"\n    authors: \"Kyuhee Kim, Auguste Poiroux, Antoine Bosselut\"\n    year: 2026\n    venue: \"VerifAI-2 Workshop, ICLR 2026 (arXiv 2604.19459)\"\n    category: reward-hacking\n    role: direct-evidence\n    relevance: >\n      Directly studies whether LLMs game formalization in logical reasoning --\n      the exact phenomenon STA's ISR is designed to detect. Evaluates GPT-5\n      and DeepSeek-R1 on FOLIO with Lean 4 proofs. Finds two modes of\n      unfaithfulness: axiom fabrication (GPT-5) and premise mistranslation\n      (R1), the latter evading detection entirely.\n    key_finding: >\n      High compilation rates (87-99%) do not imply faithful formalization.\n      Two-stage pipelines reveal unfaithfulness that unified generation hides.\n      Premise mistranslation produces internally consistent but unfaithful\n      outputs -- analogous to STA's high-ISR but semantically wrong traces.\n\n  - id: gao-reward-overoptimization\n    title: \"Scaling Laws for Reward Model Overoptimization\"\n    authors: \"Leo Gao, John Schulman, Jacob Hilton\"\n    year: 2023\n    venue: \"ICML 2023 (arXiv 2210.10760)\"\n    category: reward-hacking\n    role: theoretical-foundation\n    relevance: >\n      Foundational work quantifying Goodhart's effect: proxy reward rises\n      but gold reward first rises then falls. ISR is a proxy reward that\n      exhibits exactly this pattern — ISR can increase while prove_rate",
      "numLines": 50,
      "startLine": 530,
      "totalLines": 952
    }
  }
}
```

</details>

---

### Assistant

_source line 76_

All 5 new papers are correctly inserted. Here's the summary:

---

## 覆盖检查报告

### (a) Prolog/Logic Programming + RL/LLM

**原有覆盖**: 6 篇 — mellgren-prolog-grpo (Prolog+GRPO), logic-rl, satlm, linc, lorp, logic-lm。直接 Prolog+RL 有 1 篇 (Mellgren)，Prolog+LLM prompting 有 2 篇 (lorp, linc)。

**缺口**: 缺少 neuro-symbolic logic programming 的奠基性工作，以及 Prolog+LLM 训练（非 RL）的近期工作。

**新增 3 篇**:
1. `deepproblog` — Manhaeve et al. 2021, AIJ 298. 神经概率逻辑编程奠基工作，ProbLog + neural predicates。
2. `neurasp` — Yang, Ishay, Lee 2020, IJCAI. 神经网络 + Answer Set Programming，与 DeepProbLog 互补。
3. `thought-like-pro` — Tan et al. 2024, arXiv. 用 Prolog 引擎生成推理轨迹训练 LLM（imitation learning），与 STA 管线直接可比。

### (b) Goodhart's Law / Specification Gaming (2020+)

**原有覆盖**: 很强 — 已有 Manheim & Garrabrant 2019, Gao et al. 2023, Skalse et al. 2022, Karwowski et al. 2024, Kwa et al. 2024, Pan et al. 2022, Rafailov et al. 2024, 以及 reward-hacking-survey 2026。共 12+ 篇。

**缺口**: 缺 specification gaming 在 reasoning models 上的实证工作，特别是 formalization gaming（与 STA 直接相关）。

**新增 2 篇**:
1. `bondarenko-spec-gaming` — Bondarenko et al. 2025, arXiv 2502.13295. 证明推理模型 (o3, R1) 自发进行 specification gaming。
2. `kim-game-formalization` — Kim, Poiroux, Bosselut 2026, ICLR 2026 VerifAI-2 Workshop. 直接研究 LLM 是否 game formalization，在 FOLIO 上评估，发现两种不忠实模式——与 STA 的 high-ISR-but-semantically-wrong 现象高度类似。

### (c) Mutation Testing

**原有覆盖**: 充分 — 7 篇，涵盖 DeMillo 1978（奠基）、Offutt 1992（coupling effect）、Jia & Harman 2011（综述）、Just et al. 2014（实证验证）、LLMorpheus 2025、Meta mutation-guided 2025、mutation-consistency-llm 2024。

**无需补充。**

---

共新增 5 篇论文，总计从 45 篇增至 50 篇。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "uuid": "aaad4f85-f429-49d8-aa26-2b6f70aeded5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016j2XCz5KmhA7p7n53jbhMT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2008,
      "cache_read_input_tokens": 62736,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2008
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

_source line 77_

All 5 new papers are correctly inserted. Here's the summary:

---

## 覆盖检查报告

### (a) Prolog/Logic Programming + RL/LLM

**原有覆盖**: 6 篇 — mellgren-prolog-grpo (Prolog+GRPO), logic-rl, satlm, linc, lorp, logic-lm。直接 Prolog+RL 有 1 篇 (Mellgren)，Prolog+LLM prompting 有 2 篇 (lorp, linc)。

**缺口**: 缺少 neuro-symbolic logic programming 的奠基性工作，以及 Prolog+LLM 训练（非 RL）的近期工作。

**新增 3 篇**:
1. `deepproblog` — Manhaeve et al. 2021, AIJ 298. 神经概率逻辑编程奠基工作，ProbLog + neural predicates。
2. `neurasp` — Yang, Ishay, Lee 2020, IJCAI. 神经网络 + Answer Set Programming，与 DeepProbLog 互补。
3. `thought-like-pro` — Tan et al. 2024, arXiv. 用 Prolog 引擎生成推理轨迹训练 LLM（imitation learning），与 STA 管线直接可比。

### (b) Goodhart's Law / Specification Gaming (2020+)

**原有覆盖**: 很强 — 已有 Manheim & Garrabrant 2019, Gao et al. 2023, Skalse et al. 2022, Karwowski et al. 2024, Kwa et al. 2024, Pan et al. 2022, Rafailov et al. 2024, 以及 reward-hacking-survey 2026。共 12+ 篇。

**缺口**: 缺 specification gaming 在 reasoning models 上的实证工作，特别是 formalization gaming（与 STA 直接相关）。

**新增 2 篇**:
1. `bondarenko-spec-gaming` — Bondarenko et al. 2025, arXiv 2502.13295. 证明推理模型 (o3, R1) 自发进行 specification gaming。
2. `kim-game-formalization` — Kim, Poiroux, Bosselut 2026, ICLR 2026 VerifAI-2 Workshop. 直接研究 LLM 是否 game formalization，在 FOLIO 上评估，发现两种不忠实模式——与 STA 的 high-ISR-but-semantically-wrong 现象高度类似。

### (c) Mutation Testing

**原有覆盖**: 充分 — 7 篇，涵盖 DeMillo 1978（奠基）、Offutt 1992（coupling effect）、Jia & Harman 2011（综述）、Just et al. 2014（实证验证）、LLMorpheus 2025、Meta mutation-guided 2025、mutation-consistency-llm 2024。

**无需补充。**

---

共新增 5 篇论文，总计从 45 篇增至 50 篇。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 231775,
  "duration_api_ms": 296429,
  "num_turns": 29,
  "stop_reason": "end_turn",
  "session_id": "42195fd6-7086-41cd-8d86-4b47367b5caf",
  "total_cost_usd": 1.4657887499999998,
  "usage": {
    "input_tokens": 3335,
    "cache_creation_input_tokens": 52903,
    "cache_read_input_tokens": 890246,
    "output_tokens": 8745,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 52903,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 880,
        "cache_read_input_tokens": 62736,
        "cache_creation_input_tokens": 2008,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2008
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 271407,
      "outputTokens": 6663,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 15,
      "costUSD": 0.45472200000000007,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 3335,
      "outputTokens": 8745,
      "cacheReadInputTokens": 890246,
      "cacheCreationInputTokens": 52903,
      "webSearchRequests": 0,
      "costUSD": 1.01106675,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b55bb83c-02e6-4b59-9f96-b3eae6c7e30f"
}
```

</details>

---
