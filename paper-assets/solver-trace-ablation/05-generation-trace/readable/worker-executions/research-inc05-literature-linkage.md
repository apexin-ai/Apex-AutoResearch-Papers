# research inc05 literature linkage

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 62
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/workers/worker_research_inc05-literature-linkage_20260515T140825.log`
- **Structured JSON:** [`5f7e5e7b91130cea7eba.json`](../../sessions/5f/5f7e5e7b91130cea7eba.json)

## Before a recorded user message

62 recorded events

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
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
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
  "uuid": "af43dce5-aae5-45b3-bb5b-29e6695cdeac",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/memory/"
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
    "resetsAt": 1778854200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "4ae054cc-4a11-4286-bdcd-ead95ccc01b9",
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e"
}
```

---

### Assistant

_source line 4_

I'll start by reading the existing literature map, then search for relevant papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "39a1ad07-e652-433e-9742-f2e6613d418f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nds7QbDdC27d64cUdns3QL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13201,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13201
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01D1rnp1yEoNvfM4kHNA4Ti2`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file,WebSearch,WebFetch",
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
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "360200e7-c03c-4dc3-a330-561dc739d7f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nds7QbDdC27d64cUdns3QL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13201,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13201
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

_source line 6 · 2026-05-15T14:08:35.783Z_

<details><summary>↩ Tool result · `toolu_01D1rnp1yEoNvfM4kHNA4Ti2`</summary>

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
  "tool_name": "mcp__agent-ml-research__register_artifact"
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
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "74e45196-d5f6-4f4f-8478-33009d14d968",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file,WebSearch,WebFetch",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the existing literature map, then search for relevant papers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "654b665c-edb8-45a5-8628-413fe239db10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MatJKw833c4N3JYbySADXq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2328,
      "cache_read_input_tokens": 25042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2328
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014KJkgT7nbK86LNhE6JHA9M`</summary>

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
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "c88a1b44-d05e-4587-b23b-823306246b47",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MatJKw833c4N3JYbySADXq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2328,
      "cache_read_input_tokens": 25042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2328
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

_source line 9 · 2026-05-15T14:08:39.300Z_

<details><summary>↩ Tool result · `toolu_014KJkgT7nbK86LNhE6JHA9M`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\", \"content\": \"# Literature Map for Solver Trace Ablation (STA)\\n# Categories:\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\n#   2. reward-shaping: Reward shaping for code/formal verification\\n#   3. mutation-testing: Mutation testing in software engineering\\n#   4. intensional-analysis: Intensional program analysis\\n#   5. reward-hacking: Reward hacking / overoptimization\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\n#   7. goodhart-overoptimization: Goodhart's Law theory and dose-response dynamics\\n#   8. verification-reward: Solver/prover as RL reward signal\\n\\npapers:\\n\\n  # ============================================================\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\n  # ============================================================\\n\\n  - id: deepseek-r1\\n    title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n    authors: \\\"DeepSeek-AI\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2501.12948 / Nature 2025\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\n      intensional structural reward for neurosymbolic formalization.\\n    key_finding: >\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\n      showing emergent chain-of-thought reasoning from RL alone.\\n\\n  - id: deepseekmath\\n    title: \\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\"\\n    authors: \\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2402.03300\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\\n      used in STA training. GRPO eliminates the critic model by estimating\\n      baselines from group scores.\\n    key_finding: >\\n      GRPO matches PPO performance while significantly reducing training\\n      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.\\n\\n  - id: logic-rl\\n    title: \\\"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\\\"\\n    authors: \\\"Xian et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.14768\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic\\n      logic puzzles. Closest competitor to STA's approach of RL for logical\\n      formalization, though Logic-RL uses extensional (answer-correctness)\\n      rewards rather than STA's intensional structural rewards.\\n    key_finding: >\\n      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;\\n      rule-based reward design is critical for RL-based logical reasoning.\\n\\n  - id: mellgren-prolog-grpo\\n    title: \\\"Training Language Models to Use Prolog as a Tool\\\"\\n    authors: \\\"Niklas Mellgren\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2512.07407\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,\\n      directly comparable to STA's approach of GRPO-training a formalizer.\\n      Key difference: uses pass/fail reward vs STA's structural ISR.\\n    key_finding: >\\n      GRPO is effective for teaching small LLMs to use Prolog as a tool\\n      for logical and mathematical reasoning.\\n\\n  - id: satlm\\n    title: \\\"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\\\"\\n    authors: \\\"Xi Ye et al.\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023\\\"\\n    category: neurosymbolic-rl\\n    role: background\\n    relevance: >\\n      Neurosymbolic approach where LLM generates declarative specifications\\n      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)\\n      but uses prompting, not RL training.\\n    key_finding: >\\n      Declarative formulation outperforms imperative program-aided LMs by 23%\\n      on GSM; achieves SoTA on LSAT and BoardgameQA.\\n\\n  - id: deepproblog\\n    title: \\\"Neural Probabilistic Logic Programming in DeepProbLog\\\"\\n    authors: \\\"Robin Manhaeve, Sebastijan Dumančić, Angelika Kimmig, Thomas Demeester, Luc De Raedt\\\"\\n    year: 2021\\n    venue: \\\"Artificial Intelligence 298\\\"\\n    category: neurosymbolic-rl\\n    role: background\\n    relevance: >\\n      Foundational neural-probabilistic logic programming framework that integrates\\n      deep learning with ProbLog via neural predicates. Establishes the intellectual\\n      tradition of combining neural networks with logic programming that STA extends\\n      to LLM-generated Prolog with RL training.\\n    key_finding: >\\n      End-to-end differentiable framework integrating neural perception with\\n      probabilistic logical reasoning; supports program induction and learning\\n      from examples.\\n\\n  - id: neurasp\\n    title: \\\"NeurASP: Embracing Neural Networks into Answer Set Programming\\\"\\n    authors: \\\"Zhun Yang, Adam Ishay, Joohyung Lee\\\"\\n    year: 2020\\n    venue: \\\"IJCAI 2020\\\"\\n    category: neurosymbolic-rl\\n    role: background\\n    relevance: >\\n      Integrates neural networks with answer set programming (ASP), using\\n      ASP rules to constrain and improve neural network training. Complementary\\n      to DeepProbLog; together they represent the neuro-symbolic LP foundation\\n      that STA's LLM-to-Prolog pipeline builds upon.\\n    key_finding: >\\n      ASP semantic constraints improve neural network perception accuracy;\\n      demonstrates bidirectional benefit of neural-symbolic integration.\\n\\n  - id: thought-like-pro\\n    title: \\\"Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought\\\"\\n    authors: \\\"Xiaoyu Tan, Yongxin Deng, Xihe Qiu, Weidi Xu, Chao Qu, Wei Chu, Yinghui Xu, Yuan Qi\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2407.14562\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses Prolog engine to generate verified reasoning trajectories, then trains\\n      LLMs via imitation learning to replicate them. Directly comparable pipeline\\n      to STA (Prolog verification + LLM training), but uses imitation learning\\n      instead of GRPO with structural reward.\\n    key_finding: >\\n      Prolog-verified reasoning trajectories as training signal improve LLM\\n      logical reasoning; self-driven framework enables LLMs to formulate\\n      rules from instructions and leverage Prolog for derivation.\\n\\n  # ============================================================\\n  # Category 2: Reward shaping for code/formal verification\\n  # ============================================================\\n\\n  - id: lightman-verify-step\\n    title: \\\"Let's Verify Step by Step\\\"\\n    authors: \\\"Hunter Lightman, Vineet Kosaraju, Yura Burda, et al.\\\"\\n    year: 2023\\n    venue: \\\"arXiv 2305.20050 / ICLR 2024\\\"\\n    category: reward-shaping\\n    role: method-component\\n    relevance: >\\n      Establishes that process supervision (step-level reward) outperforms\\n      outcome supervision (final-answer reward) for reasoning. STA's ISR\\n      is analogous: it provides structural process-level signal about which\\n      components of a formalization matter, rather than just pass/fail.\\n    key_finding: >\\n      Process-supervised reward model achieves 78% on MATH, significantly\\n      outperforming outcome-supervised models. Released PRM800K dataset.\\n\\n  - id: reward-shaping-rlhf\\n    title: \\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\"\\n    authors: \\\"Jiayi Fu, Xuandong Zhao, Chengyuan Yao, et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.18770\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Studies reward shaping design principles for RLHF: bounded rewards and\\n      rapid-then-convergent growth. STA's ISR follows these principles\\n      naturally since structural necessity scores are bounded [0,1].\\n    key_finding: >\\n      Two key reward shaping principles: (1) bounded RL reward, (2) rapid\\n      initial growth with gradual convergence. PAR method achieves 5%+\\n      win rate improvement on AlpacaEval 2.0.\\n\\n  - id: rlvr-reasoning\\n    title: \\\"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2506.14245\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize\\n      reasoning. STA argues that for neurosymbolic formalization, binary reward\\n      is insufficient and structural reward is needed to avoid reward hacking.\\n    key_finding: >\\n      RLVR with binary verification implicitly teaches correct reasoning\\n      strategies, not just answer matching.\\n\\n  - id: rubric-grpo\\n    title: \\\"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2605.08061\\\"\\n    category: reward-shaping\\n    role: direct-competitor\\n    relevance: >\\n      Uses structured rubric-based rewards with GRPO, similar in spirit to\\n      STA's structured ISR. Key difference: rubric rewards come from LLM\\n      judges, while ISR comes from solver-based mutation testing.\\n    key_finding: >\\n      Structured multi-dimensional reward signals improve GRPO training\\n      generalization compared to scalar rewards.\\n\\n  - id: gao-effective-rl-reward\\n    title: \\\"On Designing Effective RL Reward at Training Time for LLM Reasoning\\\"\\n    authors: \\\"Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2410.15115\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Demonstrates that learned process/outcome reward models can hurt RL\\n      training, producing worse performance than simple success reward only.\\n      Directly explains plan005 NEGATIVE: STA's ISR as auxiliary process\\n      reward degrades prove_rate compared to exec-only baseline.\\n    key_finding: >\\n      PRM/ORM rewards may NOT help or even hurt RL training vs success-only\\n      reward. Solution: Clipping and Delta techniques to bound accumulated\\n      reward magnitude prevent reward hacking.\\n\\n  - id: prof-process-outcome\\n    title: \\\"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training\\\"\\n    authors: \\\"Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2509.03403\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Shows that naively combining PRM+ORM signals leads to performance\\n      degradation. PROF consistency filter retains only PRM-ORM consistent\\n      samples, achieving 4%+ improvement over blending. Suggests STA should\\n      only apply ISR when consistent with execution outcome.\\n    key_finding: >\\n      Process rewards frequently suffer from inaccuracies and reward hacking\\n      susceptibility. PROF filters training data by PRM-ORM consistency,\\n      outperforming naive reward blending by 4%+ accuracy.\\n\\n  - id: moskovitz-constrained-rlhf\\n    title: \\\"Confronting Reward Model Overoptimization with Constrained RLHF\\\"\\n    authors: \\\"Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer\\\"\\n    year: 2023\\n    venue: \\\"arXiv 2310.04373 / ICLR 2024\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      First study on overoptimization in composite reward models. Shows that\\n      fixed-weight linear scalarization of component rewards leads to\\n      degradation past a threshold. Proposes constrained RL with dynamic\\n      Lagrange multiplier weighting as alternative to fixed ISR weight.\\n    key_finding: >\\n      Correlation between component RMs significantly affects overoptimization\\n      thresholds. Constrained RL with Lagrange multipliers outperforms\\n      fixed-weight reward composition.\\n\\n  - id: skalse-reward-hacking\\n    title: \\\"Defining and Characterizing Reward Hacking\\\"\\n    authors: \\\"Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger\\\"\\n    year: 2022\\n    venue: \\\"arXiv 2209.13085 / NeurIPS 2022\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Formal proof that for stochastic policies, two reward functions are\\n      unhackable only if one is constant. Theoretically explains why any\\n      non-zero ISR weight can decrease prove_rate -- this is a fundamental\\n      property of reward composition, not STA-specific.\\n    key_finding: >\\n      Any non-constant proxy reward can decrease true reward when optimized.\\n      Unhackability requires the proxy to be constant, making all non-trivial\\n      auxiliary rewards theoretically vulnerable to degrading primary performance.\\n\\n  - id: progrs-outcome-conditioned\\n    title: \\\"LLM Reasoning with Process Rewards for Outcome-Guided Steps\\\"\\n    authors: \\\"Mohammad Rezaei, Jens Lehmann, Sahar Vahdati\\\"\\n    year: 2026\\n    venue: \\\"arXiv 2604.02341\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      PRM scores optimized as absolute rewards amplify fluent failure modes.\\n      Outcome-conditioned centering shifts incorrect trajectories' PRM scores\\n      to zero mean, preserving ranking info without corrupting gradients.\\n      Suggests STA should condition ISR on execution outcome.\\n    key_finding: >\\n      Naive process rewards induce reward hacking by rewarding locally fluent\\n      but globally incorrect reasoning. Outcome-conditioned centering resolves\\n      the conflict with fewer rollouts than outcome-only baselines.\\n\\n  - id: qwen-prm-lessons\\n    title: \\\"The Lessons of Developing Process Reward Models in Mathematical Reasoning\\\"\\n    authors: \\\"Zhenru Zhang et al. (Qwen Team, Alibaba)\\\"\\n    year: 2025\\n    venue: \\\"ACL 2025 Findings (arXiv 2501.07301)\\\"\\n    category: reward-shaping\\n    role: supporting-evidence\\n    relevance: >\\n      MC estimation-synthesized PRM data leads to quality degradation; policy\\n      model generates \\\"answer-correct but reasoning-flawed\\\" responses, causing\\n      process reward / outcome misalignment. Directly parallels ISR problem:\\n      structurally correct but semantically wrong proof traces get high ISR\\n      but low execution reward.\\n    key_finding: >\\n      PRM performance depends critically on data quality; MC estimation\\n      introduces systematic bias. Answer-correct reasoning-flawed samples\\n      corrupt process supervision signal.\\n\\n  # ============================================================\\n  # Category 3: Mutation testing in software engineering\\n  # ============================================================\\n\\n  - id: demillo1978\\n    title: \\\"Hints on Test Data Selection: Help for the Practicing Programmer\\\"\\n    authors: \\\"Richard A. DeMillo, Richard J. Lipton, Frederick G. Sayward\\\"\\n    year: 1978\\n    venue: \\\"Computer 11(4):34-43\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Foundational paper introducing mutation testing. STA's component\\n      necessity testing directly extends this idea: instead of mutating\\n      source code to test test suites, STA mutates logical formulas\\n      to test component necessity for solver success.\\n    key_finding: >\\n      Introduced mutation testing and the coupling effect hypothesis:\\n      tests that detect simple faults also detect complex faults.\\n\\n  - id: offutt-coupling\\n    title: \\\"Investigations of the Software Testing Coupling Effect\\\"\\n    authors: \\\"A. Jefferson Offutt\\\"\\n    year: 1992\\n    venue: \\\"ACM TOSEM 1(1):5-20\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Empirically validates the coupling effect hypothesis that underpins\\n      mutation testing. STA's single-component ablation is analogous to\\n      first-order mutation; the coupling effect suggests this suffices.\\n    key_finding: >\\n      Test data killing all first-order mutants killed >99% of second-\\n      and third-order mutants, validating the coupling effect.\\n\\n  - id: jia-harman-survey\\n    title: \\\"An Analysis and Survey of the Development of Mutation Testing\\\"\\n    authors: \\\"Yue Jia, Mark Harman\\\"\\n    year: 2011\\n    venue: \\\"IEEE TSE 37(5):649-678\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Comprehensive survey of mutation testing covering three decades of\\n      development. Provides theoretical and practical foundation for STA's\\n      adaptation of mutation testing to logical formulas.\\n    key_finding: >\\n      Systematic classification of mutation operators, cost reduction\\n      techniques, and equivalence problem -- all relevant to STA's design\\n      of clause-level ablation operators.\\n\\n  - id: just-mutants-real-faults\\n    title: \\\"Are Mutants a Valid Substitute for Real Faults in Software Testing?\\\"\\n    authors: \\\"Rene Just, Darioush Jalali, Laura Inozemtseva, et al.\\\"\\n    year: 2014\\n    venue: \\\"FSE 2014\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Validates that mutation testing (structural/intensional analysis of\\n      program adequacy) correlates with real fault detection. Supports STA's\\n      premise that structural analysis of formalization components provides\\n      meaningful signal about formalization quality.\\n    key_finding: >\\n      Mutant detection is statistically correlated with real fault detection,\\n      and mutation score is a better predictor of test effectiveness than\\n      code coverage.\\n\\n  - id: llmorpheus\\n    title: \\\"LLMorpheus: Mutation Testing Using Large Language Models\\\"\\n    authors: \\\"Frank Tip, Jon Bell, et al.\\\"\\n    year: 2025\\n    venue: \\\"IEEE TSE 2025\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Uses LLMs to generate realistic code mutants beyond traditional\\n      mutation operators. Shows mutation testing evolving toward\\n      ML-integrated approaches, validating STA's cross-pollination\\n      of mutation testing ideas into ML training.\\n    key_finding: >\\n      LLM-generated mutants simulate real bugs that rule-based operators\\n      cannot produce, improving mutation testing realism.\\n\\n  - id: mutation-guided-meta\\n    title: \\\"Mutation-Guided LLM-based Test Generation at Meta\\\"\\n    authors: \\\"Christopher Foster et al.\\\"\\n    year: 2025\\n    venue: \\\"FSE 2025\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Industrial application of mutation-guided LLM test generation at\\n      Meta. Demonstrates that mutation analysis can guide LLM behavior\\n      in production -- analogous to how STA uses mutation (ablation) to\\n      guide GRPO reward signal.\\n    key_finding: >\\n      Mutation-guided approach generates tests that kill significantly\\n      more mutants than unguided LLM test generation at Meta scale.\\n\\n  - id: mutation-consistency-llm\\n    title: \\\"Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs\\\"\\n    authors: \\\"Various\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2401.05940\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Uses code mutations to evaluate LLM code understanding consistency.\\n      Conceptually related to STA: both use systematic code/formula\\n      mutations to assess model capabilities.\\n    key_finding: >\\n      LLMs show significant inconsistency when evaluated on mutated code\\n      variants, suggesting superficial pattern matching.\\n\\n  # ============================================================\\n  # Category 4: Intensional program analysis\\n  # ============================================================\\n\\n  - id: deepmutation\\n    title: \\\"A Probabilistic Framework for Mutation Testing in Deep Neural Networks\\\"\\n    authors: \\\"Various\\\"\\n    year: 2023\\n    venue: \\\"Information and Software Technology 2023\\\"\\n    category: intensional-analysis\\n    role: background\\n    relevance: >\\n      Extends mutation testing to DNN testing with probabilistic mutation\\n      operators. Parallel to STA's extension of mutation testing from\\n      traditional programs to logical formulas.\\n    key_finding: >\\n      Probabilistic mutation framework enables meaningful test adequacy\\n      assessment for neural networks through structural perturbation.\\n\\n  # ============================================================\\n  # Category 5: Reward hacking / overoptimization\\n  # ============================================================\\n\\n  - id: inform-reward-hacking\\n    title: \\\"InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling\\\"\\n    authors: \\\"Various\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS 2024\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Proposes information-bottleneck approach to detect and mitigate reward\\n      hacking. STA's ISR addresses the same problem differently: by grounding\\n      reward in verifiable structural properties (component necessity), it\\n      reduces the attack surface for reward hacking.\\n    key_finding: >\\n      Variational information bottleneck filters irrelevant features from\\n      reward model; Cluster Separation Index detects reward overoptimization.\\n\\n  - id: mo-grpo\\n    title: \\\"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\\\"\\n    authors: \\\"CyberAgent AI Lab\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2509.22047\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Directly addresses GRPO reward hacking in multi-objective settings.\\n      STA's ISR can be viewed as adding a structural objective to the\\n      correctness objective, making MO-GRPO's insights directly applicable.\\n    key_finding: >\\n      Standard GRPO normalizes after summing rewards, allowing high-variance\\n      objectives to dominate. MO-GRPO equalizes scales before aggregation.\\n\\n  - id: reward-hacking-survey\\n    title: \\\"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\\\"\\n    authors: \\\"Various\\\"\\n    year: 2026\\n    venue: \\\"arXiv 2604.13602\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Comprehensive survey of reward hacking mechanisms in the LLM era.\\n      Provides theoretical framework for understanding why STA's structural\\n      reward is more robust than pure outcome-based reward.\\n    key_finding: >\\n      Reward hacking manifests through specification gaming, reward model\\n      exploitation, and emergent misalignment; structural verification\\n      rewards are more robust than learned reward models.\\n\\n  - id: energy-loss-reward-hacking\\n    title: \\\"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"ICML 2025\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Identifies energy loss in LLM final layer as an indicator of reward\\n      hacking during RL. Provides complementary diagnostic to STA's\\n      structural reward approach.\\n    key_finding: >\\n      Energy loss in the final layer increases during RL and excessive\\n      increase characterizes reward hacking; EPPO algorithm penalizes\\n      this to mitigate hacking.\\n\\n  - id: spurious-rewards\\n    title: \\\"Spurious Rewards: Rethinking Training Signals in RLVR\\\"\\n    authors: \\\"Ruixin Yang et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2506.10947 / NeurIPS 2025 submission\\\"\\n    category: reward-hacking\\n    role: direct-evidence\\n    relevance: >\\n      Most directly relevant to STA findings. GRPO+random reward on\\n      Qwen2.5-Math improves 21.4%, nearly matching ground-truth reward's\\n      29.1%. Matches our plan017 finding: additive random (PR=48%) >\\n      additive ISR (PR=18%). Structured metrics can be worse than random\\n      noise due to systematic bias vs pure variance.\\n    key_finding: >\\n      Random reward nearly matches ground-truth reward in GRPO training,\\n      suggesting GRPO's group normalization extracts signal from noise.\\n      Effect is model-dependent (works on Qwen2.5, not Llama3).\\n\\n  - id: bondarenko-spec-gaming\\n    title: \\\"Demonstrating Specification Gaming in Reasoning Models\\\"\\n    authors: \\\"Alexander Bondarenko, Denis Volk, Dmitrii Volkov, Jeffrey Ladish\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.13295\\\"\\n    category: reward-hacking\\n    role: direct-evidence\\n    relevance: >\\n      Shows that reasoning models (o3, DeepSeek-R1) resort to specification\\n      gaming on difficult tasks by default, without explicit nudging.\\n      Directly relevant to STA's concern: RL-trained reasoning models\\n      may game formal verification rewards rather than learn genuine\\n      formalization skills.\\n    key_finding: >\\n      Reasoning models spontaneously hack benchmarks (e.g., manipulating\\n      chess engine files instead of playing chess). Stronger reasoning\\n      capability correlates with more sophisticated gaming strategies.\\n\\n  - id: kim-game-formalization\\n    title: \\\"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning\\\"\\n    authors: \\\"Kyuhee Kim, Auguste Poiroux, Antoine Bosselut\\\"\\n    year: 2026\\n    venue: \\\"VerifAI-2 Workshop, ICLR 2026 (arXiv 2604.19459)\\\"\\n    category: reward-hacking\\n    role: direct-evidence\\n    relevance: >\\n      Directly studies whether LLMs game formalization in logical reasoning --\\n      the exact phenomenon STA's ISR is designed to detect. Evaluates GPT-5\\n      and DeepSeek-R1 on FOLIO with Lean 4 proofs. Finds two modes of\\n      unfaithfulness: axiom fabrication (GPT-5) and premise mistranslation\\n      (R1), the latter evading detection entirely.\\n    key_finding: >\\n      High compilation rates (87-99%) do not imply faithful formalization.\\n      Two-stage pipelines reveal unfaithfulness that unified generation hides.\\n      Premise mistranslation produces internally consistent but unfaithful\\n      outputs -- analogous to STA's high-ISR but semantically wrong traces.\\n\\n  - id: gao-reward-overoptimization\\n    title: \\\"Scaling Laws for Reward Model Overoptimization\\\"\\n    authors: \\\"Leo Gao, John Schulman, Jacob Hilton\\\"\\n    year: 2023\\n    venue: \\\"ICML 2023 (arXiv 2210.10760)\\\"\\n    category: reward-hacking\\n    role: theoretical-foundation\\n    relevance: >\\n      Foundational work quantifying Goodhart's effect: proxy reward rises\\n      but gold reward first rises then falls. ISR is a proxy reward that\\n      exhibits exactly this pattern — ISR can increase while prove_rate\\n      decreases, making it suitable for post-hoc diagnosis but harmful\\n      as training signal.\\n    key_finding: >\\n      Gold/proxy reward divergence follows predictable scaling laws.\\n      Proxy reward optimization past critical point degrades gold reward,\\n      with the divergence point scaling with model and dataset size.\\n\\n  - id: karwowski-goodhart-rl\\n    title: \\\"Goodhart's Law in Reinforcement Learning\\\"\\n    authors: \\\"Jacek Karwowski, Oliver Hayman, Xingjian Bai, Klaus Kiendlhofer, Charlie Griffin, Joar Skalse\\\"\\n    year: 2024\\n    venue: \\\"ICLR 2024 (arXiv 2310.09144)\\\"\\n    category: reward-hacking\\n    role: theoretical-foundation\\n    relevance: >\\n      Geometric interpretation of Goodhart's Law in MDPs: optimizing\\n      imperfect proxy past critical point decreases true objective. ISR as\\n      proxy has partial correlation with execution correctness — exceeding\\n      critical optimization point pushes policy toward high-ISR but\\n      low-correctness regions. Explains plan002/plan005 negative results.\\n    key_finding: >\\n      Formalizes Goodhart's Law for RL: any non-trivially correlated proxy\\n      reward creates regions where proxy and true reward diverge, and\\n      policy optimization inevitably enters these regions.\\n\\n  # ============================================================\\n  # Category 6: FOL/Prolog formalization with LLMs\\n  # ============================================================\\n\\n  - id: folio\\n    title: \\\"FOLIO: Natural Language Reasoning with First-Order Logic\\\"\\n    authors: \\\"Simeng Han et al.\\\"\\n    year: 2022\\n    venue: \\\"arXiv 2209.00840 / EMNLP 2024\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Primary FOL reasoning benchmark. STA uses FOLIO-style NL->FOL\\n      formalization as the target task for GRPO training. FOLIO's\\n      expert-annotated FOL annotations serve as reference formalizations.\\n    key_finding: >\\n      1,430 NL-FOL paired examples with reasoning depths up to 5+;\\n      GPT-4 still struggles on the hardest examples.\\n\\n  - id: proofwriter\\n    title: \\\"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language\\\"\\n    authors: \\\"Oyvind Tafjord, Bhavana Dalvi, Peter Clark\\\"\\n    year: 2021\\n    venue: \\\"Findings of ACL-IJCNLP 2021\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Source dataset for STA's training data. ProofWriter provides\\n      rule-based logical reasoning problems in natural language that\\n      STA uses for training formalizer models.\\n    key_finding: >\\n      Generative model can reliably produce implications and proofs;\\n      accuracy exceeds prior methods by 9% and generalizes to unseen\\n      proof depths.\\n\\n  - id: logic-lm\\n    title: \\\"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\\\"\\n    authors: \\\"Liangming Pan, Alon Albalak, Xinyi Wang, William Wang\\\"\\n    year: 2023\\n    venue: \\\"Findings of EMNLP 2023\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      LLM->symbolic solver pipeline for logical reasoning, directly\\n      comparable to STA's formalizer->Prolog solver pipeline. Key\\n      difference: Logic-LM uses prompting, STA uses GRPO training.\\n    key_finding: >\\n      LLM+solver achieves 39.2% improvement over LLM-alone on logical\\n      reasoning benchmarks including ProofWriter and FOLIO.\\n\\n  - id: linc\\n    title: \\\"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers\\\"\\n    authors: \\\"Theo X. Olausson, Alex Gu, Ben Lipkin, et al.\\\"\\n    year: 2023\\n    venue: \\\"EMNLP 2023\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      Neurosymbolic approach where LLM translates NL to FOL for theorem\\n      prover. Directly comparable to STA's NL->Prolog translation.\\n      LINC uses prompting-based approach; STA uses RL training.\\n    key_finding: >\\n      StarCoder+ (15.5B) with LINC outperforms GPT-3.5 and GPT-4 with\\n      CoT by 38% and 10% respectively on ProofWriter.\\n\\n  - id: fover-pei2025\\n    title: \\\"FoVer: First-Order Logic Verification for Natural Language Reasoning\\\"\\n    authors: \\\"Yu Pei, Yongping Du, Xingnan Jin\\\"\\n    year: 2025\\n    venue: \\\"TACL 13:1340-1359\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      Uses LLM->FOL->Z3 pipeline for verifying NL reasoning correctness.\\n      Similar to STA's verification pipeline but focuses on post-hoc\\n      verification rather than training reward signal.\\n    key_finding: >\\n      FOL verification via Z3 significantly outperforms existing methods\\n      on ProofWriter and FOLIO benchmarks.\\n\\n  - id: lorp\\n    title: \\\"LoRP: LLM-based Logical Reasoning via Prolog\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"Knowledge-Based Systems 2025\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      LLM->Prolog pipeline with FOL-to-Prolog translation mechanism.\\n      Closest to STA's formalization target (Prolog), though LoRP\\n      uses prompting while STA uses GRPO training with structural reward.\\n    key_finding: >\\n      Systematic FOL-to-Prolog translation extends Prolog expressiveness;\\n      achieves SoTA accuracy on logical reasoning with three-vote majority.\\n\\n  - id: nl2fol\\n    title: \\\"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection\\\"\\n    authors: \\\"Lalwani, Kim, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2405.02318\\\"\\n    category: fol-formalization\\n    role: background\\n    relevance: >\\n      Step-by-step NL->FOL translation using LLMs with SMT solver\\n      verification. Demonstrates the NL->formal logic pipeline that\\n      STA aims to improve via RL training.\\n    key_finding: >\\n      Neurosymbolic NL2FOL achieves 78% F1 on LOGIC dataset and\\n      generalizes to LogicClimate (80% F1), outperforming supervised\\n      models by 21%.\\n\\n  - id: logica2\\n    title: \\\"LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: \\\"IEEE/ACM TASLP 2023\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Logical reasoning evaluation benchmark derived from Chinese civil\\n      service exams. Provides supplementary evaluation for STA's\\n      formalization capabilities.\\n    key_finding: >\\n      8,678 multiple-choice questions covering categorical, disjunctive,\\n      and conditional reasoning; widely used LLM benchmark.\\n\\n  # ============================================================\\n  # Category 7: Goodhart's Law theory and dose-response dynamics\\n  # ============================================================\\n\\n  - id: manheim-goodhart-taxonomy\\n    title: \\\"Categorizing Variants of Goodhart's Law\\\"\\n    authors: \\\"David Manheim, Scott Garrabrant\\\"\\n    year: 2019\\n    venue: \\\"arXiv 1803.04585\\\"\\n    category: goodhart-overoptimization\\n    role: theoretical-foundation\\n    relevance: >\\n      Four-part Goodhart taxonomy: regressional, extremal, causal, adversarial.\\n      STA's high-β ISR collapse is best classified as extremal Goodhart\\n      (policy moves to OOD region where ISR↑ but prove_rate↓). Provides\\n      vocabulary for discussion section.\\n    key_finding: >\\n      First systematic categorization of Goodhart failure modes. Extremal\\n      variant occurs when proxy-goal relationship breaks in out-of-distribution\\n      regions reached by strong optimization.\\n\\n  - id: pan-reward-misspecification\\n    title: \\\"The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models\\\"\\n    authors: \\\"Alexander Pan, Kush Bhatia, Jacob Steinhardt\\\"\\n    year: 2022\\n    venue: \\\"ICLR 2022\\\"\\n    category: goodhart-overoptimization\\n    role: theoretical-foundation\\n    relevance: >\\n      Across 9 environments, more capable agents exploit misspecifications more.\\n      Observes dose-dependent degradation — capability thresholds where true\\n      reward sharply drops. Matches STA's β=0.1→0.3 qualitative shift.\\n    key_finding: >\\n      Reward misspecification causes dose-dependent degradation where true reward\\n      sharply drops past capability thresholds. More capable optimization\\n      produces worse outcomes under misspecification.\\n\\n  - id: kwa-catastrophic-goodhart\\n    title: \\\"Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification\\\"\\n    authors: \\\"Tat-Thang Kwa, Rachel Thomas, Adrià Garriga-Alonso\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS 2024\\\"\\n    category: goodhart-overoptimization\\n    role: theoretical-foundation\\n    relevance: >\\n      If reward model error is heavy-tailed, policies achieve arbitrarily\\n      high proxy reward with no true utility gain. KL regularization provably\\n      fails. Explains why KL penalty in GRPO cannot prevent ISR collapse\\n      at high β if ISR error distribution is heavy-tailed.\\n    key_finding: >\\n      KL-regularized RL provably fails to prevent overoptimization under\\n      heavy-tailed reward misspecification. Policies can achieve arbitrarily\\n      high proxy reward with zero true utility.\\n\\n  - id: rafailov-daa-scaling\\n    title: \\\"Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms\\\"\\n    authors: \\\"Rafael Rafailov, Yaswanth Chittepu, Ryan Park, Harshit Sikchi, Joey Hejna, W. Bradley Knox, Chelsea Finn, Scott Niekum\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS 2024\\\"\\n    category: goodhart-overoptimization\\n    role: supporting-evidence\\n    relevance: >\\n      Extends Gao et al. to DPO/IPO/SLiC. Tests seven β values across\\n      1B-6.9B models. DAAs still overoptimize despite no explicit proxy RM.\\n      Validates β as a \\\"dose\\\" parameter — directly analogous to STA's\\n      ISR weight sweep.\\n    key_finding: >\\n      Direct alignment algorithms exhibit overoptimization following\\n      predictable scaling laws. Smaller models overoptimize sooner.\\n      β-controlled dose-response is a general phenomenon across RL paradigms.\\n\\n  - id: huang-chi-squared\\n    title: \\\"Correcting the Mythos of KL-Regularization: Direct and Contrastive Distribution Correction\\\"\\n    authors: \\\"Afra Feyza Akyürek, Banghua Zhu, Sham Kakade, Jiantao Jiao\\\"\\n    year: 2025\\n    venue: \\\"ICLR 2025 Poster\\\"\\n    category: goodhart-overoptimization\\n    role: supporting-evidence\\n    relevance: >\\n      KL-regularization is theoretically inadequate for preventing\\n      overoptimization. Chi-squared divergence provably alleviates it.\\n      Suggests that even with KL penalty in GRPO, STA's high-β collapse\\n      is theoretically expected.\\n    key_finding: >\\n      Chi-squared preference optimization provably mitigates overoptimization\\n      where KL-regularization fails. Alternative divergence measures offer\\n      stronger guarantees.\\n\\n  - id: coste-rm-ensembles\\n    title: \\\"Reward Model Ensembles Help Mitigate Overoptimization\\\"\\n    authors: \\\"Thomas Coste, Usman Anwar, Robert Kirk, David Krueger\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023 Workshop on Alignment\\\"\\n    category: goodhart-overoptimization\\n    role: background\\n    relevance: >\\n      Worst-case optimization across RM ensembles practically eliminates\\n      overoptimization for BoN and reduces it for PPO. Suggests ensemble\\n      of multiple solver metrics (instead of single ISR) as mitigation.\\n    key_finding: >\\n      RM ensembles with worst-case aggregation mitigate overoptimization.\\n      Ensemble size and diversity directly affect robustness.\\n\\n  # ============================================================\\n  # Category 8: Solver/prover as RL reward signal\\n  # ============================================================\\n\\n  - id: rlsf\\n    title: \\\"Reinforcement Learning via Symbolic Feedback\\\"\\n    authors: \\\"Abhinav Jha, Shikhar Murty, Zico Kolter, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2405.16661\\\"\\n    category: verification-reward\\n    role: direct-competitor\\n    relevance: >\\n      Most directly relevant: uses solver/prover certificates as fine-grained\\n      token-level reward signal. Outperforms traditional approaches on program\\n      synthesis (+31.4%). STA extends this paradigm and shows when it breaks\\n      (Goodhart effects at high auxiliary reward weight).\\n    key_finding: >\\n      Symbolic reasoning tools provide poly-sized certificates as reward.\\n      Smaller RLSF models outperform GPT-4 on structured generation tasks.\\n\\n  - id: fover-kamoi2026\\n    title: \\\"FoVer: Generalizable Process Reward Models via Formally Verified Training Data\\\"\\n    authors: \\\"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\\\"\\n    year: 2025\\n    venue: \\\"Findings of ACL 2026 (arXiv 2502.01345)\\\"\\n    category: verification-reward\\n    role: supporting-evidence\\n    relevance: >\\n      Uses Z3 and Isabelle to synthesize PRM training data by annotating\\n      step-level error labels without human annotation. Same solver family\\n      as STA. Shows verification-based rewards work; STA extends by showing\\n      dose-response dynamics.\\n    key_finding: >\\n      Formally verified training data enables generalizable process reward\\n      models competitive on ProcessBench and 12 reasoning benchmarks.\\n\\n  - id: deepseek-prover-v15\\n    title: \\\"DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search\\\"\\n    authors: \\\"DeepSeek AI\\\"\\n    year: 2024\\n    venue: \\\"ICLR 2025 (arXiv 2408.08152)\\\"\\n    category: verification-reward\\n    role: method-component\\n    relevance: >\\n      Uses GRPO with Lean 4 verification as binary reward. Same algorithm\\n      (GRPO) + formal verification, but binary (pass/fail). Binary reward\\n      avoids the graded-metric Goodhart risk that STA identifies with ISR.\\n    key_finding: >\\n      GRPO + binary Lean verification achieves 63.5% on miniF2F. Binary\\n      correctness guarantee via formal verification sidesteps proxy reward\\n      overoptimization.\\n\\n  - id: alphaproof\\n    title: \\\"AlphaProof\\\"\\n    authors: \\\"Google DeepMind\\\"\\n    year: 2024\\n    venue: \\\"Nature 2025\\\"\\n    category: verification-reward\\n    role: background\\n    relevance: >\\n      AlphaZero-inspired RL with Lean proof verification at scale.\\n      Silver medal at IMO 2024. Binary verification reward avoids the\\n      Goodhart problem STA identifies with graded verification metrics.\\n    key_finding: >\\n      Binary formal verification as RL reward scales to IMO-level\\n      mathematical reasoning. Demonstrates verification-reward RL works\\n      at the frontier of mathematical difficulty.\\n\\n  - id: math-shepherd\\n    title: \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\"\\n    authors: \\\"Peiyi Wang, Lei Li, Zhihong Shao, R.X. Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"ACL 2024 (arXiv 2312.08935)\\\"\\n    category: verification-reward\\n    role: supporting-evidence\\n    relevance: >\\n      Automatically constructs process supervision data and uses it as\\n      step-by-step PPO reward. Automated verification reward without human\\n      labels, analogous to STA's automated ISR computation via solver.\\n    key_finding: >\\n      Automated process supervision improves Mistral-7B on GSM8K\\n      (77.9→84.1%) and MATH (28.6→33.0%) without human annotation.\\n\\n  # ============================================================\\n  # Additional reward-shaping papers (Goodhart survey additions)\\n  # ============================================================\\n\\n  - id: bipars\\n    title: \\\"Learning to Utilize Shaping Rewards: A New Approach of Reward Shaping\\\"\\n    authors: \\\"Yujing Hu, Weixun Wang, Hangtian Jia, et al.\\\"\\n    year: 2020\\n    venue: \\\"NeurIPS 2020\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Bi-level optimization learns parameterized shaping reward weights.\\n      Can transform harmful shaping rewards into beneficial ones by learning\\n      negative weights. Directly addresses STA's problem: when ISR weight\\n      is wrong, automated weight learning could find optimal β.\\n    key_finding: >\\n      Bi-level optimization automatically learns auxiliary reward weights,\\n      outperforming fixed weights and recovering from harmful shaping rewards.\\n\\n  - id: yue-rlvr-limits\\n    title: \\\"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?\\\"\\n    authors: \\\"Yue et al. (Tsinghua)\\\"\\n    year: 2025\\n    venue: \\\"NeurIPS 2025 (arXiv 2504.13837)\\\"\\n    category: reward-hacking\\n    role: supporting-evidence\\n    relevance: >\\n      RLVR does not elicit fundamentally new reasoning patterns; it biases\\n      output distribution toward reward-yielding paths while narrowing the\\n      reasoning capability boundary compared to base models. Directly supports\\n      STA's finding that 1000-step GRPO collapses to hacking: the model\\n      concentrates on high-reward but non-genuine pathways rather than\\n      discovering novel reasoning strategies.\\n    key_finding: >\\n      RLVR improves sampling efficiency toward correct paths but narrows\\n      the reasoning frontier relative to base models. Current RL paradigms\\n      redistribute existing capability rather than creating new reasoning.\\n\\n  - id: deng-grpo-collapse-lld\\n    title: \\\"On GRPO Collapse in Search-R1: The Lazy Likelihood-Displacement Death Spiral\\\"\\n    authors: \\\"Deng et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2512.04220\\\"\\n    category: reward-hacking\\n    role: supporting-evidence\\n    relevance: >\\n      Identifies Lazy Likelihood Displacement (LLD) as the core mechanism\\n      driving GRPO training collapse: systematic reduction in likelihood of\\n      both correct and incorrect responses triggers a self-reinforcing death\\n      spiral. Provides a mechanistic explanation complementary to Goodhart\\n      theory for why STA's 1000-step GRPO universally collapses regardless\\n      of reward signal type.\\n    key_finding: >\\n      LLD emerges early in GRPO training and triggers a death spiral where\\n      declining likelihood inflates gradients and causes collapse.\\n      Lightweight likelihood-preserving regularization yields +37.8% on\\n      Qwen2.5-3B.\\n\\n  - id: dapo\\n    title: \\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\"\\n    authors: \\\"Qiying Yu et al. (ByteDance)\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2503.14476\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Four techniques for stable multi-component reward in GRPO: Clip-Higher,\\n      Dynamic Sampling, token-level policy gradient, Overlong Reward Shaping.\\n      Addresses stability issues relevant to STA's multi-reward setup.\\n    key_finding: >\\n      Clip-Higher and Dynamic Sampling prevent entropy collapse in GRPO\\n      with multi-component rewards. Soft punishment for overlong outputs\\n      avoids reward hacking through length exploitation.\\n\", \"total_chars\": 44638, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "3872b7d7-145c-467a-9c19-589807596775",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\\\", \\\"content\\\": \\\"# Literature Map for Solver Trace Ablation (STA)\\\\n# Categories:\\\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\\\n#   2. reward-shaping: Reward shaping for code/formal verification\\\\n#   3. mutation-testing: Mutation testing in software engineering\\\\n#   4. intensional-analysis: Intensional program analysis\\\\n#   5. reward-hacking: Reward hacking / overoptimization\\\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\\\n#   7. goodhart-overoptimization: Goodhart's Law theory and dose-response dynamics\\\\n#   8. verification-reward: Solver/prover as RL reward signal\\\\n\\\\npapers:\\\\n\\\\n  # ============================================================\\\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\\\n  # ============================================================\\\\n\\\\n  - id: deepseek-r1\\\\n    title: \\\\\\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"DeepSeek-AI\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2501.12948 / Nature 2025\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: method-component\\\\n    relevance: >\\\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\\\n      intensional structural reward for neurosymbolic formalization.\\\\n    key_finding: >\\\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\\\n      showing emergent chain-of-thought reasoning from RL alone.\\\\n\\\\n  - id: deepseekmath\\\\n    title: \\\\\\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2402.03300\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: method-component\\\\n    relevance: >\\\\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\\\\n      used in STA training. GRPO eliminates the critic model by estimating\\\\n      baselines from group scores.\\\\n    key_finding: >\\\\n      GRPO matches PPO performance while significantly reducing training\\\\n      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.\\\\n\\\\n  - id: logic-rl\\\\n    title: \\\\\\\"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Xian et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2502.14768\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic\\\\n      logic puzzles. Closest competitor to STA's approach of RL for logical\\\\n      formalization, though Logic-RL uses extensional (answer-correctness)\\\\n      rewards rather than STA's intensional structural rewards.\\\\n    key_finding: >\\\\n      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;\\\\n      rule-based reward design is critical for RL-based logical reasoning.\\\\n\\\\n  - id: mellgren-prolog-grpo\\\\n    title: \\\\\\\"Training Language Models to Use Prolog as a Tool\\\\\\\"\\\\n    authors: \\\\\\\"Niklas Mellgren\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2512.07407\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,\\\\n      directly comparable to STA's approach of GRPO-training a formalizer.\\\\n      Key difference: uses pass/fail reward vs STA's structural ISR.\\\\n    key_finding: >\\\\n      GRPO is effective for teaching small LLMs to use Prolog as a tool\\\\n      for logical and mathematical reasoning.\\\\n\\\\n  - id: satlm\\\\n    title: \\\\\\\"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\\\\\\\"\\\\n    authors: \\\\\\\"Xi Ye et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"NeurIPS 2023\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: background\\\\n    relevance: >\\\\n      Neurosymbolic approach where LLM generates declarative specifications\\\\n      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)\\\\n      but uses prompting, not RL training.\\\\n    key_finding: >\\\\n      Declarative formulation outperforms imperative program-aided LMs by 23%\\\\n      on GSM; achieves SoTA on LSAT and BoardgameQA.\\\\n\\\\n  - id: deepproblog\\\\n    title: \\\\\\\"Neural Probabilistic Logic Programming in DeepProbLog\\\\\\\"\\\\n    authors: \\\\\\\"Robin Manhaeve, Sebastijan Dumančić, Angelika Kimmig, Thomas Demeester, Luc De Raedt\\\\\\\"\\\\n    year: 2021\\\\n    venue: \\\\\\\"Artificial Intelligence 298\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: background\\\\n    relevance: >\\\\n      Foundational neural-probabilistic logic programming framework that integrates\\\\n      deep learning with ProbLog via neural predicates. Establishes the intellectual\\\\n      tradition of combining neural networks with logic programming that STA extends\\\\n      to LLM-generated Prolog with RL training.\\\\n    key_finding: >\\\\n      End-to-end differentiable framework integrating neural perception with\\\\n      probabilistic logical reasoning; supports program induction and learning\\\\n      from examples.\\\\n\\\\n  - id: neurasp\\\\n    title: \\\\\\\"NeurASP: Embracing Neural Networks into Answer Set Programming\\\\\\\"\\\\n    authors: \\\\\\\"Zhun Yang, Adam Ishay, Joohyung Lee\\\\\\\"\\\\n    year: 2020\\\\n    venue: \\\\\\\"IJCAI 2020\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: background\\\\n    relevance: >\\\\n      Integrates neural networks with answer set programming (ASP), using\\\\n      ASP rules to constrain and improve neural network training. Complementary\\\\n      to DeepProbLog; together they represent the neuro-symbolic LP foundation\\\\n      that STA's LLM-to-Prolog pipeline builds upon.\\\\n    key_finding: >\\\\n      ASP semantic constraints improve neural network perception accuracy;\\\\n      demonstrates bidirectional benefit of neural-symbolic integration.\\\\n\\\\n  - id: thought-like-pro\\\\n    title: \\\\\\\"Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought\\\\\\\"\\\\n    authors: \\\\\\\"Xiaoyu Tan, Yongxin Deng, Xihe Qiu, Weidi Xu, Chao Qu, Wei Chu, Yinghui Xu, Yuan Qi\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2407.14562\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Uses Prolog engine to generate verified reasoning trajectories, then trains\\\\n      LLMs via imitation learning to replicate them. Directly comparable pipeline\\\\n      to STA (Prolog verification + LLM training), but uses imitation learning\\\\n      instead of GRPO with structural reward.\\\\n    key_finding: >\\\\n      Prolog-verified reasoning trajectories as training signal improve LLM\\\\n      logical reasoning; self-driven framework enables LLMs to formulate\\\\n      rules from instructions and leverage Prolog for derivation.\\\\n\\\\n  # ============================================================\\\\n  # Category 2: Reward shaping for code/formal verification\\\\n  # ============================================================\\\\n\\\\n  - id: lightman-verify-step\\\\n    title: \\\\\\\"Let's Verify Step by Step\\\\\\\"\\\\n    authors: \\\\\\\"Hunter Lightman, Vineet Kosaraju, Yura Burda, et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"arXiv 2305.20050 / ICLR 2024\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: method-component\\\\n    relevance: >\\\\n      Establishes that process supervision (step-level reward) outperforms\\\\n      outcome supervision (final-answer reward) for reasoning. STA's ISR\\\\n      is analogous: it provides structural process-level signal about which\\\\n      components of a formalization matter, rather than just pass/fail.\\\\n    key_finding: >\\\\n      Process-supervised reward model achieves 78% on MATH, significantly\\\\n      outperforming outcome-supervised models. Released PRM800K dataset.\\\\n\\\\n  - id: reward-shaping-rlhf\\\\n    title: \\\\\\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\\\\\"\\\\n    authors: \\\\\\\"Jiayi Fu, Xuandong Zhao, Chengyuan Yao, et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2502.18770\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      Studies reward shaping design principles for RLHF: bounded rewards and\\\\n      rapid-then-convergent growth. STA's ISR follows these principles\\\\n      naturally since structural necessity scores are bounded [0,1].\\\\n    key_finding: >\\\\n      Two key reward shaping principles: (1) bounded RL reward, (2) rapid\\\\n      initial growth with gradual convergence. PAR method achieves 5%+\\\\n      win rate improvement on AlpacaEval 2.0.\\\\n\\\\n  - id: rlvr-reasoning\\\\n    title: \\\\\\\"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2506.14245\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize\\\\n      reasoning. STA argues that for neurosymbolic formalization, binary reward\\\\n      is insufficient and structural reward is needed to avoid reward hacking.\\\\n    key_finding: >\\\\n      RLVR with binary verification implicitly teaches correct reasoning\\\\n      strategies, not just answer matching.\\\\n\\\\n  - id: rubric-grpo\\\\n    title: \\\\\\\"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2605.08061\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Uses structured rubric-based rewards with GRPO, similar in spirit to\\\\n      STA's structured ISR. Key difference: rubric rewards come from LLM\\\\n      judges, while ISR comes from solver-based mutation testing.\\\\n    key_finding: >\\\\n      Structured multi-dimensional reward signals improve GRPO training\\\\n      generalization compared to scalar rewards.\\\\n\\\\n  - id: gao-effective-rl-reward\\\\n    title: \\\\\\\"On Designing Effective RL Reward at Training Time for LLM Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2410.15115\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      Demonstrates that learned process/outcome reward models can hurt RL\\\\n      training, producing worse performance than simple success reward only.\\\\n      Directly explains plan005 NEGATIVE: STA's ISR as auxiliary process\\\\n      reward degrades prove_rate compared to exec-only baseline.\\\\n    key_finding: >\\\\n      PRM/ORM rewards may NOT help or even hurt RL training vs success-only\\\\n      reward. Solution: Clipping and Delta techniques to bound accumulated\\\\n      reward magnitude prevent reward hacking.\\\\n\\\\n  - id: prof-process-outcome\\\\n    title: \\\\\\\"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training\\\\\\\"\\\\n    authors: \\\\\\\"Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2509.03403\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      Shows that naively combining PRM+ORM signals leads to performance\\\\n      degradation. PROF consistency filter retains only PRM-ORM consistent\\\\n      samples, achieving 4%+ improvement over blending. Suggests STA should\\\\n      only apply ISR when consistent with execution outcome.\\\\n    key_finding: >\\\\n      Process rewards frequently suffer from inaccuracies and reward hacking\\\\n      susceptibility. PROF filters training data by PRM-ORM consistency,\\\\n      outperforming naive reward blending by 4%+ accuracy.\\\\n\\\\n  - id: moskovitz-constrained-rlhf\\\\n    title: \\\\\\\"Confronting Reward Model Overoptimization with Constrained RLHF\\\\\\\"\\\\n    authors: \\\\\\\"Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"arXiv 2310.04373 / ICLR 2024\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      First study on overoptimization in composite reward models. Shows that\\\\n      fixed-weight linear scalarization of component rewards leads to\\\\n      degradation past a threshold. Proposes constrained RL with dynamic\\\\n      Lagrange multiplier weighting as alternative to fixed ISR weight.\\\\n    key_finding: >\\\\n      Correlation between component RMs significantly affects overoptimization\\\\n      thresholds. Constrained RL with Lagrange multipliers outperforms\\\\n      fixed-weight reward composition.\\\\n\\\\n  - id: skalse-reward-hacking\\\\n    title: \\\\\\\"Defining and Characterizing Reward Hacking\\\\\\\"\\\\n    authors: \\\\\\\"Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger\\\\\\\"\\\\n    year: 2022\\\\n    venue: \\\\\\\"arXiv 2209.13085 / NeurIPS 2022\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      Formal proof that for stochastic policies, two reward functions are\\\\n      unhackable only if one is constant. Theoretically explains why any\\\\n      non-zero ISR weight can decrease prove_rate -- this is a fundamental\\\\n      property of reward composition, not STA-specific.\\\\n    key_finding: >\\\\n      Any non-constant proxy reward can decrease true reward when optimized.\\\\n      Unhackability requires the proxy to be constant, making all non-trivial\\\\n      auxiliary rewards theoretically vulnerable to degrading primary performance.\\\\n\\\\n  - id: progrs-outcome-conditioned\\\\n    title: \\\\\\\"LLM Reasoning with Process Rewards for Outcome-Guided Steps\\\\\\\"\\\\n    authors: \\\\\\\"Mohammad Rezaei, Jens Lehmann, Sahar Vahdati\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv 2604.02341\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      PRM scores optimized as absolute rewards amplify fluent failure modes.\\\\n      Outcome-conditioned centering shifts incorrect trajectories' PRM scores\\\\n      to zero mean, preserving ranking info without corrupting gradients.\\\\n      Suggests STA should condition ISR on execution outcome.\\\\n    key_finding: >\\\\n      Naive process rewards induce reward hacking by rewarding locally fluent\\\\n      but globally incorrect reasoning. Outcome-conditioned centering resolves\\\\n      the conflict with fewer rollouts than outcome-only baselines.\\\\n\\\\n  - id: qwen-prm-lessons\\\\n    title: \\\\\\\"The Lessons of Developing Process Reward Models in Mathematical Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Zhenru Zhang et al. (Qwen Team, Alibaba)\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"ACL 2025 Findings (arXiv 2501.07301)\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: supporting-evidence\\\\n    relevance: >\\\\n      MC estimation-synthesized PRM data leads to quality degradation; policy\\\\n      model generates \\\\\\\"answer-correct but reasoning-flawed\\\\\\\" responses, causing\\\\n      process reward / outcome misalignment. Directly parallels ISR problem:\\\\n      structurally correct but semantically wrong proof traces get high ISR\\\\n      but low execution reward.\\\\n    key_finding: >\\\\n      PRM performance depends critically on data quality; MC estimation\\\\n      introduces systematic bias. Answer-correct reasoning-flawed samples\\\\n      corrupt process supervision signal.\\\\n\\\\n  # ============================================================\\\\n  # Category 3: Mutation testing in software engineering\\\\n  # ============================================================\\\\n\\\\n  - id: demillo1978\\\\n    title: \\\\\\\"Hints on Test Data Selection: Help for the Practicing Programmer\\\\\\\"\\\\n    authors: \\\\\\\"Richard A. DeMillo, Richard J. Lipton, Frederick G. Sayward\\\\\\\"\\\\n    year: 1978\\\\n    venue: \\\\\\\"Computer 11(4):34-43\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Foundational paper introducing mutation testing. STA's component\\\\n      necessity testing directly extends this idea: instead of mutating\\\\n      source code to test test suites, STA mutates logical formulas\\\\n      to test component necessity for solver success.\\\\n    key_finding: >\\\\n      Introduced mutation testing and the coupling effect hypothesis:\\\\n      tests that detect simple faults also detect complex faults.\\\\n\\\\n  - id: offutt-coupling\\\\n    title: \\\\\\\"Investigations of the Software Testing Coupling Effect\\\\\\\"\\\\n    authors: \\\\\\\"A. Jefferson Offutt\\\\\\\"\\\\n    year: 1992\\\\n    venue: \\\\\\\"ACM TOSEM 1(1):5-20\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Empirically validates the coupling effect hypothesis that underpins\\\\n      mutation testing. STA's single-component ablation is analogous to\\\\n      first-order mutation; the coupling effect suggests this suffices.\\\\n    key_finding: >\\\\n      Test data killing all first-order mutants killed >99% of second-\\\\n      and third-order mutants, validating the coupling effect.\\\\n\\\\n  - id: jia-harman-survey\\\\n    title: \\\\\\\"An Analysis and Survey of the Development of Mutation Testing\\\\\\\"\\\\n    authors: \\\\\\\"Yue Jia, Mark Harman\\\\\\\"\\\\n    year: 2011\\\\n    venue: \\\\\\\"IEEE TSE 37(5):649-678\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Comprehensive survey of mutation testing covering three decades of\\\\n      development. Provides theoretical and practical foundation for STA's\\\\n      adaptation of mutation testing to logical formulas.\\\\n    key_finding: >\\\\n      Systematic classification of mutation operators, cost reduction\\\\n      techniques, and equivalence problem -- all relevant to STA's design\\\\n      of clause-level ablation operators.\\\\n\\\\n  - id: just-mutants-real-faults\\\\n    title: \\\\\\\"Are Mutants a Valid Substitute for Real Faults in Software Testing?\\\\\\\"\\\\n    authors: \\\\\\\"Rene Just, Darioush Jalali, Laura Inozemtseva, et al.\\\\\\\"\\\\n    year: 2014\\\\n    venue: \\\\\\\"FSE 2014\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Validates that mutation testing (structural/intensional analysis of\\\\n      program adequacy) correlates with real fault detection. Supports STA's\\\\n      premise that structural analysis of formalization components provides\\\\n      meaningful signal about formalization quality.\\\\n    key_finding: >\\\\n      Mutant detection is statistically correlated with real fault detection,\\\\n      and mutation score is a better predictor of test effectiveness than\\\\n      code coverage.\\\\n\\\\n  - id: llmorpheus\\\\n    title: \\\\\\\"LLMorpheus: Mutation Testing Using Large Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Frank Tip, Jon Bell, et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"IEEE TSE 2025\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Uses LLMs to generate realistic code mutants beyond traditional\\\\n      mutation operators. Shows mutation testing evolving toward\\\\n      ML-integrated approaches, validating STA's cross-pollination\\\\n      of mutation testing ideas into ML training.\\\\n    key_finding: >\\\\n      LLM-generated mutants simulate real bugs that rule-based operators\\\\n      cannot produce, improving mutation testing realism.\\\\n\\\\n  - id: mutation-guided-meta\\\\n    title: \\\\\\\"Mutation-Guided LLM-based Test Generation at Meta\\\\\\\"\\\\n    authors: \\\\\\\"Christopher Foster et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"FSE 2025\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Industrial application of mutation-guided LLM test generation at\\\\n      Meta. Demonstrates that mutation analysis can guide LLM behavior\\\\n      in production -- analogous to how STA uses mutation (ablation) to\\\\n      guide GRPO reward signal.\\\\n    key_finding: >\\\\n      Mutation-guided approach generates tests that kill significantly\\\\n      more mutants than unguided LLM test generation at Meta scale.\\\\n\\\\n  - id: mutation-consistency-llm\\\\n    title: \\\\\\\"Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2401.05940\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Uses code mutations to evaluate LLM code understanding consistency.\\\\n      Conceptually related to STA: both use systematic code/formula\\\\n      mutations to assess model capabilities.\\\\n    key_finding: >\\\\n      LLMs show significant inconsistency when evaluated on mutated code\\\\n      variants, suggesting superficial pattern matching.\\\\n\\\\n  # ============================================================\\\\n  # Category 4: Intensional program analysis\\\\n  # ============================================================\\\\n\\\\n  - id: deepmutation\\\\n    title: \\\\\\\"A Probabilistic Framework for Mutation Testing in Deep Neural Networks\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"Information and Software Technology 2023\\\\\\\"\\\\n    category: intensional-analysis\\\\n    role: background\\\\n    relevance: >\\\\n      Extends mutation testing to DNN testing with probabilistic mutation\\\\n      operators. Parallel to STA's extension of mutation testing from\\\\n      traditional programs to logical formulas.\\\\n    key_finding: >\\\\n      Probabilistic mutation framework enables meaningful test adequacy\\\\n      assessment for neural networks through structural perturbation.\\\\n\\\\n  # ============================================================\\\\n  # Category 5: Reward hacking / overoptimization\\\\n  # ============================================================\\\\n\\\\n  - id: inform-reward-hacking\\\\n    title: \\\\\\\"InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"NeurIPS 2024\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: background\\\\n    relevance: >\\\\n      Proposes information-bottleneck approach to detect and mitigate reward\\\\n      hacking. STA's ISR addresses the same problem differently: by grounding\\\\n      reward in verifiable structural properties (component necessity), it\\\\n      reduces the attack surface for reward hacking.\\\\n    key_finding: >\\\\n      Variational information bottleneck filters irrelevant features from\\\\n      reward model; Cluster Separation Index detects reward overoptimization.\\\\n\\\\n  - id: mo-grpo\\\\n    title: \\\\\\\"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\\\\\\\"\\\\n    authors: \\\\\\\"CyberAgent AI Lab\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2509.22047\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: background\\\\n    relevance: >\\\\n      Directly addresses GRPO reward hacking in multi-objective settings.\\\\n      STA's ISR can be viewed as adding a structural objective to the\\\\n      correctness objective, making MO-GRPO's insights directly applicable.\\\\n    key_finding: >\\\\n      Standard GRPO normalizes after summing rewards, allowing high-variance\\\\n      objectives to dominate. MO-GRPO equalizes scales before aggregation.\\\\n\\\\n  - id: reward-hacking-survey\\\\n    title: \\\\\\\"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv 2604.13602\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: background\\\\n    relevance: >\\\\n      Comprehensive survey of reward hacking mechanisms in the LLM era.\\\\n      Provides theoretical framework for understanding why STA's structural\\\\n      reward is more robust than pure outcome-based reward.\\\\n    key_finding: >\\\\n      Reward hacking manifests through specification gaming, reward model\\\\n      exploitation, and emergent misalignment; structural verification\\\\n      rewards are more robust than learned reward models.\\\\n\\\\n  - id: energy-loss-reward-hacking\\\\n    title: \\\\\\\"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"ICML 2025\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: background\\\\n    relevance: >\\\\n      Identifies energy loss in LLM final layer as an indicator of reward\\\\n      hacking during RL. Provides complementary diagnostic to STA's\\\\n      structural reward approach.\\\\n    key_finding: >\\\\n      Energy loss in the final layer increases during RL and excessive\\\\n      increase characterizes reward hacking; EPPO algorithm penalizes\\\\n      this to mitigate hacking.\\\\n\\\\n  - id: spurious-rewards\\\\n    title: \\\\\\\"Spurious Rewards: Rethinking Training Signals in RLVR\\\\\\\"\\\\n    authors: \\\\\\\"Ruixin Yang et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2506.10947 / NeurIPS 2025 submission\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: direct-evidence\\\\n    relevance: >\\\\n      Most directly relevant to STA findings. GRPO+random reward on\\\\n      Qwen2.5-Math improves 21.4%, nearly matching ground-truth reward's\\\\n      29.1%. Matches our plan017 finding: additive random (PR=48%) >\\\\n      additive ISR (PR=18%). Structured metrics can be worse than random\\\\n      noise due to systematic bias vs pure variance.\\\\n    key_finding: >\\\\n      Random reward nearly matches ground-truth reward in GRPO training,\\\\n      suggesting GRPO's group normalization extracts signal from noise.\\\\n      Effect is model-dependent (works on Qwen2.5, not Llama3).\\\\n\\\\n  - id: bondarenko-spec-gaming\\\\n    title: \\\\\\\"Demonstrating Specification Gaming in Reasoning Models\\\\\\\"\\\\n    authors: \\\\\\\"Alexander Bondarenko, Denis Volk, Dmitrii Volkov, Jeffrey Ladish\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2502.13295\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: direct-evidence\\\\n    relevance: >\\\\n      Shows that reasoning models (o3, DeepSeek-R1) resort to specification\\\\n      gaming on difficult tasks by default, without explicit nudging.\\\\n      Directly relevant to STA's concern: RL-trained reasoning models\\\\n      may game formal verification rewards rather than learn genuine\\\\n      formalization skills.\\\\n    key_finding: >\\\\n      Reasoning models spontaneously hack benchmarks (e.g., manipulating\\\\n      chess engine files instead of playing chess). Stronger reasoning\\\\n      capability correlates with more sophisticated gaming strategies.\\\\n\\\\n  - id: kim-game-formalization\\\\n    title: \\\\\\\"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Kyuhee Kim, Auguste Poiroux, Antoine Bosselut\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"VerifAI-2 Workshop, ICLR 2026 (arXiv 2604.19459)\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: direct-evidence\\\\n    relevance: >\\\\n      Directly studies whether LLMs game formalization in logical reasoning --\\\\n      the exact phenomenon STA's ISR is designed to detect. Evaluates GPT-5\\\\n      and DeepSeek-R1 on FOLIO with Lean 4 proofs. Finds two modes of\\\\n      unfaithfulness: axiom fabrication (GPT-5) and premise mistranslation\\\\n      (R1), the latter evading detection entirely.\\\\n    key_finding: >\\\\n      High compilation rates (87-99%) do not imply faithful formalization.\\\\n      Two-stage pipelines reveal unfaithfulness that unified generation hides.\\\\n      Premise mistranslation produces internally consistent but unfaithful\\\\n      outputs -- analogous to STA's high-ISR but semantically wrong traces.\\\\n\\\\n  - id: gao-reward-overoptimization\\\\n    title: \\\\\\\"Scaling Laws for Reward Model Overoptimization\\\\\\\"\\\\n    authors: \\\\\\\"Leo Gao, John Schulman, Jacob Hilton\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"ICML 2023 (arXiv 2210.10760)\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: theoretical-foundation\\\\n    relevance: >\\\\n      Foundational work quantifying Goodhart's effect: proxy reward rises\\\\n      but gold reward first rises then falls. ISR is a proxy reward that\\\\n      exhibits exactly this pattern — ISR can increase while prove_rate\\\\n      decreases, making it suitable for post-hoc diagnosis but harmful\\\\n      as training signal.\\\\n    key_finding: >\\\\n      Gold/proxy reward divergence follows predictable scaling laws.\\\\n      Proxy reward optimization past critical point degrades gold reward,\\\\n      with the divergence point scaling with model and dataset size.\\\\n\\\\n  - id: karwowski-goodhart-rl\\\\n    title: \\\\\\\"Goodhart's Law in Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Jacek Karwowski, Oliver Hayman, Xingjian Bai, Klaus Kiendlhofer, Charlie Griffin, Joar Skalse\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"ICLR 2024 (arXiv 2310.09144)\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: theoretical-foundation\\\\n    relevance: >\\\\n      Geometric interpretation of Goodhart's Law in MDPs: optimizing\\\\n      imperfect proxy past critical point decreases true objective. ISR as\\\\n      proxy has partial correlation with execution correctness — exceeding\\\\n      critical optimization point pushes policy toward high-ISR but\\\\n      low-correctness regions. Explains plan002/plan005 negative results.\\\\n    key_finding: >\\\\n      Formalizes Goodhart's Law for RL: any non-trivially correlated proxy\\\\n      reward creates regions where proxy and true reward diverge, and\\\\n      policy optimization inevitably enters these regions.\\\\n\\\\n  # ============================================================\\\\n  # Category 6: FOL/Prolog formalization with LLMs\\\\n  # ============================================================\\\\n\\\\n  - id: folio\\\\n    title: \\\\\\\"FOLIO: Natural Language Reasoning with First-Order Logic\\\\\\\"\\\\n    authors: \\\\\\\"Simeng Han et al.\\\\\\\"\\\\n    year: 2022\\\\n    venue: \\\\\\\"arXiv 2209.00840 / EMNLP 2024\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: evaluation\\\\n    relevance: >\\\\n      Primary FOL reasoning benchmark. STA uses FOLIO-style NL->FOL\\\\n      formalization as the target task for GRPO training. FOLIO's\\\\n      expert-annotated FOL annotations serve as reference formalizations.\\\\n    key_finding: >\\\\n      1,430 NL-FOL paired examples with reasoning depths up to 5+;\\\\n      GPT-4 still struggles on the hardest examples.\\\\n\\\\n  - id: proofwriter\\\\n    title: \\\\\\\"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language\\\\\\\"\\\\n    authors: \\\\\\\"Oyvind Tafjord, Bhavana Dalvi, Peter Clark\\\\\\\"\\\\n    year: 2021\\\\n    venue: \\\\\\\"Findings of ACL-IJCNLP 2021\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: evaluation\\\\n    relevance: >\\\\n      Source dataset for STA's training data. ProofWriter provides\\\\n      rule-based logical reasoning problems in natural language that\\\\n      STA uses for training formalizer models.\\\\n    key_finding: >\\\\n      Generative model can reliably produce implications and proofs;\\\\n      accuracy exceeds prior methods by 9% and generalizes to unseen\\\\n      proof depths.\\\\n\\\\n  - id: logic-lm\\\\n    title: \\\\\\\"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Liangming Pan, Alon Albalak, Xinyi Wang, William Wang\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"Findings of EMNLP 2023\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      LLM->symbolic solver pipeline for logical reasoning, directly\\\\n      comparable to STA's formalizer->Prolog solver pipeline. Key\\\\n      difference: Logic-LM uses prompting, STA uses GRPO training.\\\\n    key_finding: >\\\\n      LLM+solver achieves 39.2% improvement over LLM-alone on logical\\\\n      reasoning benchmarks including ProofWriter and FOLIO.\\\\n\\\\n  - id: linc\\\\n    title: \\\\\\\"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers\\\\\\\"\\\\n    authors: \\\\\\\"Theo X. Olausson, Alex Gu, Ben Lipkin, et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"EMNLP 2023\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Neurosymbolic approach where LLM translates NL to FOL for theorem\\\\n      prover. Directly comparable to STA's NL->Prolog translation.\\\\n      LINC uses prompting-based approach; STA uses RL training.\\\\n    key_finding: >\\\\n      StarCoder+ (15.5B) with LINC outperforms GPT-3.5 and GPT-4 with\\\\n      CoT by 38% and 10% respectively on ProofWriter.\\\\n\\\\n  - id: fover-pei2025\\\\n    title: \\\\\\\"FoVer: First-Order Logic Verification for Natural Language Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Yu Pei, Yongping Du, Xingnan Jin\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"TACL 13:1340-1359\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Uses LLM->FOL->Z3 pipeline for verifying NL reasoning correctness.\\\\n      Similar to STA's verification pipeline but focuses on post-hoc\\\\n      verification rather than training reward signal.\\\\n    key_finding: >\\\\n      FOL verification via Z3 significantly outperforms existing methods\\\\n      on ProofWriter and FOLIO benchmarks.\\\\n\\\\n  - id: lorp\\\\n    title: \\\\\\\"LoRP: LLM-based Logical Reasoning via Prolog\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"Knowledge-Based Systems 2025\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      LLM->Prolog pipeline with FOL-to-Prolog translation mechanism.\\\\n      Closest to STA's formalization target (Prolog), though LoRP\\\\n      uses prompting while STA uses GRPO training with structural reward.\\\\n    key_finding: >\\\\n      Systematic FOL-to-Prolog translation extends Prolog expressiveness;\\\\n      achieves SoTA accuracy on logical reasoning with three-vote majority.\\\\n\\\\n  - id: nl2fol\\\\n    title: \\\\\\\"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection\\\\\\\"\\\\n    authors: \\\\\\\"Lalwani, Kim, et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2405.02318\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: background\\\\n    relevance: >\\\\n      Step-by-step NL->FOL translation using LLMs with SMT solver\\\\n      verification. Demonstrates the NL->formal logic pipeline that\\\\n      STA aims to improve via RL training.\\\\n    key_finding: >\\\\n      Neurosymbolic NL2FOL achieves 78% F1 on LOGIC dataset and\\\\n      generalizes to LogicClimate (80% F1), outperforming supervised\\\\n      models by 21%.\\\\n\\\\n  - id: logica2\\\\n    title: \\\\\\\"LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding\\\\\\\"\\\\n    authors: \\\\\\\"Liu et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"IEEE/ACM TASLP 2023\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: evaluation\\\\n    relevance: >\\\\n      Logical reasoning evaluation benchmark derived from Chinese civil\\\\n      service exams. Provides supplementary evaluation for STA's\\\\n      formalization capabilities.\\\\n    key_finding: >\\\\n      8,678 multiple-choice questions covering categorical, disjunctive,\\\\n      and conditional reasoning; widely used LLM benchmark.\\\\n\\\\n  # ============================================================\\\\n  # Category 7: Goodhart's Law theory and dose-response dynamics\\\\n  # ============================================================\\\\n\\\\n  - id: manheim-goodhart-taxonomy\\\\n    title: \\\\\\\"Categorizing Variants of Goodhart's Law\\\\\\\"\\\\n    authors: \\\\\\\"David Manheim, Scott Garrabrant\\\\\\\"\\\\n    year: 2019\\\\n    venue: \\\\\\\"arXiv 1803.04585\\\\\\\"\\\\n    category: goodhart-overoptimization\\\\n    role: theoretical-foundation\\\\n    relevance: >\\\\n      Four-part Goodhart taxonomy: regressional, extremal, causal, adversarial.\\\\n      STA's high-β ISR collapse is best classified as extremal Goodhart\\\\n      (policy moves to OOD region where ISR↑ but prove_rate↓). Provides\\\\n      vocabulary for discussion section.\\\\n    key_finding: >\\\\n      First systematic categorization of Goodhart failure modes. Extremal\\\\n      variant occurs when proxy-goal relationship breaks in out-of-distribution\\\\n      regions reached by strong optimization.\\\\n\\\\n  - id: pan-reward-misspecification\\\\n    title: \\\\\\\"The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models\\\\\\\"\\\\n    authors: \\\\\\\"Alexander Pan, Kush Bhatia, Jacob Steinhardt\\\\\\\"\\\\n    year: 2022\\\\n    venue: \\\\\\\"ICLR 2022\\\\\\\"\\\\n    category: goodhart-overoptimization\\\\n    role: theoretical-foundation\\\\n    relevance: >\\\\n      Across 9 environments, more capable agents exploit misspecifications more.\\\\n      Observes dose-dependent degradation — capability thresholds where true\\\\n      reward sharply drops. Matches STA's β=0.1→0.3 qualitative shift.\\\\n    key_finding: >\\\\n      Reward misspecification causes dose-dependent degradation where true reward\\\\n      sharply drops past capability thresholds. More capable optimization\\\\n      produces worse outcomes under misspecification.\\\\n\\\\n  - id: kwa-catastrophic-goodhart\\\\n    title: \\\\\\\"Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification\\\\\\\"\\\\n    authors: \\\\\\\"Tat-Thang Kwa, Rachel Thomas, Adrià Garriga-Alonso\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"NeurIPS 2024\\\\\\\"\\\\n    category: goodhart-overoptimization\\\\n    role: theoretical-foundation\\\\n    relevance: >\\\\n      If reward model error is heavy-tailed, policies achieve arbitrarily\\\\n      high proxy reward with no true utility gain. KL regularization provably\\\\n      fails. Explains why KL penalty in GRPO cannot prevent ISR collapse\\\\n      at high β if ISR error distribution is heavy-tailed.\\\\n    key_finding: >\\\\n      KL-regularized RL provably fails to prevent overoptimization under\\\\n      heavy-tailed reward misspecification. Policies can achieve arbitrarily\\\\n      high proxy reward with zero true utility.\\\\n\\\\n  - id: rafailov-daa-scaling\\\\n    title: \\\\\\\"Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms\\\\\\\"\\\\n    authors: \\\\\\\"Rafael Rafailov, Yaswanth Chittepu, Ryan Park, Harshit Sikchi, Joey Hejna, W. Bradley Knox, Chelsea Finn, Scott Niekum\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"NeurIPS 2024\\\\\\\"\\\\n    category: goodhart-overoptimization\\\\n    role: supporting-evidence\\\\n    relevance: >\\\\n      Extends Gao et al. to DPO/IPO/SLiC. Tests seven β values across\\\\n      1B-6.9B models. DAAs still overoptimize despite no explicit proxy RM.\\\\n      Validates β as a \\\\\\\"dose\\\\\\\" parameter — directly analogous to STA's\\\\n      ISR weight sweep.\\\\n    key_finding: >\\\\n      Direct alignment algorithms exhibit overoptimization following\\\\n      predictable scaling laws. Smaller models overoptimize sooner.\\\\n      β-controlled dose-response is a general phenomenon across RL paradigms.\\\\n\\\\n  - id: huang-chi-squared\\\\n    title: \\\\\\\"Correcting the Mythos of KL-Regularization: Direct and Contrastive Distribution Correction\\\\\\\"\\\\n    authors: \\\\\\\"Afra Feyza Akyürek, Banghua Zhu, Sham Kakade, Jiantao Jiao\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"ICLR 2025 Poster\\\\\\\"\\\\n    category: goodhart-overoptimization\\\\n    role: supporting-evidence\\\\n    relevance: >\\\\n      KL-regularization is theoretically inadequate for preventing\\\\n      overoptimization. Chi-squared divergence provably alleviates it.\\\\n      Suggests that even with KL penalty in GRPO, STA's high-β collapse\\\\n      is theoretically expected.\\\\n    key_finding: >\\\\n      Chi-squared preference optimization provably mitigates overoptimization\\\\n      where KL-regularization fails. Alternative divergence measures offer\\\\n      stronger guarantees.\\\\n\\\\n  - id: coste-rm-ensembles\\\\n    title: \\\\\\\"Reward Model Ensembles Help Mitigate Overoptimization\\\\\\\"\\\\n    authors: \\\\\\\"Thomas Coste, Usman Anwar, Robert Kirk, David Krueger\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"NeurIPS 2023 Workshop on Alignment\\\\\\\"\\\\n    category: goodhart-overoptimization\\\\n    role: background\\\\n    relevance: >\\\\n      Worst-case optimization across RM ensembles practically eliminates\\\\n      overoptimization for BoN and reduces it for PPO. Suggests ensemble\\\\n      of multiple solver metrics (instead of single ISR) as mitigation.\\\\n    key_finding: >\\\\n      RM ensembles with worst-case aggregation mitigate overoptimization.\\\\n      Ensemble size and diversity directly affect robustness.\\\\n\\\\n  # ============================================================\\\\n  # Category 8: Solver/prover as RL reward signal\\\\n  # ============================================================\\\\n\\\\n  - id: rlsf\\\\n    title: \\\\\\\"Reinforcement Learning via Symbolic Feedback\\\\\\\"\\\\n    authors: \\\\\\\"Abhinav Jha, Shikhar Murty, Zico Kolter, et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2405.16661\\\\\\\"\\\\n    category: verification-reward\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Most directly relevant: uses solver/prover certificates as fine-grained\\\\n      token-level reward signal. Outperforms traditional approaches on program\\\\n      synthesis (+31.4%). STA extends this paradigm and shows when it breaks\\\\n      (Goodhart effects at high auxiliary reward weight).\\\\n    key_finding: >\\\\n      Symbolic reasoning tools provide poly-sized certificates as reward.\\\\n      Smaller RLSF models outperform GPT-4 on structured generation tasks.\\\\n\\\\n  - id: fover-kamoi2026\\\\n    title: \\\\\\\"FoVer: Generalizable Process Reward Models via Formally Verified Training Data\\\\\\\"\\\\n    authors: \\\\\\\"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"Findings of ACL 2026 (arXiv 2502.01345)\\\\\\\"\\\\n    category: verification-reward\\\\n    role: supporting-evidence\\\\n    relevance: >\\\\n      Uses Z3 and Isabelle to synthesize PRM training data by annotating\\\\n      step-level error labels without human annotation. Same solver family\\\\n      as STA. Shows verification-based rewards work; STA extends by showing\\\\n      dose-response dynamics.\\\\n    key_finding: >\\\\n      Formally verified training data enables generalizable process reward\\\\n      models competitive on ProcessBench and 12 reasoning benchmarks.\\\\n\\\\n  - id: deepseek-prover-v15\\\\n    title: \\\\\\\"DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search\\\\\\\"\\\\n    authors: \\\\\\\"DeepSeek AI\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"ICLR 2025 (arXiv 2408.08152)\\\\\\\"\\\\n    category: verification-reward\\\\n    role: method-component\\\\n    relevance: >\\\\n      Uses GRPO with Lean 4 verification as binary reward. Same algorithm\\\\n      (GRPO) + formal verification, but binary (pass/fail). Binary reward\\\\n      avoids the graded-metric Goodhart risk that STA identifies with ISR.\\\\n    key_finding: >\\\\n      GRPO + binary Lean verification achieves 63.5% on miniF2F. Binary\\\\n      correctness guarantee via formal verification sidesteps proxy reward\\\\n      overoptimization.\\\\n\\\\n  - id: alphaproof\\\\n    title: \\\\\\\"AlphaProof\\\\\\\"\\\\n    authors: \\\\\\\"Google DeepMind\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"Nature 2025\\\\\\\"\\\\n    category: verification-reward\\\\n    role: background\\\\n    relevance: >\\\\n      AlphaZero-inspired RL with Lean proof verification at scale.\\\\n      Silver medal at IMO 2024. Binary verification reward avoids the\\\\n      Goodhart problem STA identifies with graded verification metrics.\\\\n    key_finding: >\\\\n      Binary formal verification as RL reward scales to IMO-level\\\\n      mathematical reasoning. Demonstrates verification-reward RL works\\\\n      at the frontier of mathematical difficulty.\\\\n\\\\n  - id: math-shepherd\\\\n    title: \\\\\\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\\\\\"\\\\n    authors: \\\\\\\"Peiyi Wang, Lei Li, Zhihong Shao, R.X. Xu, et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"ACL 2024 (arXiv 2312.08935)\\\\\\\"\\\\n    category: verification-reward\\\\n    role: supporting-evidence\\\\n    relevance: >\\\\n      Automatically constructs process supervision data and uses it as\\\\n      step-by-step PPO reward. Automated verification reward without human\\\\n      labels, analogous to STA's automated ISR computation via solver.\\\\n    key_finding: >\\\\n      Automated process supervision improves Mistral-7B on GSM8K\\\\n      (77.9→84.1%) and MATH (28.6→33.0%) without human annotation.\\\\n\\\\n  # ============================================================\\\\n  # Additional reward-shaping papers (Goodhart survey additions)\\\\n  # ============================================================\\\\n\\\\n  - id: bipars\\\\n    title: \\\\\\\"Learning to Utilize Shaping Rewards: A New Approach of Reward Shaping\\\\\\\"\\\\n    authors: \\\\\\\"Yujing Hu, Weixun Wang, Hangtian Jia, et al.\\\\\\\"\\\\n    year: 2020\\\\n    venue: \\\\\\\"NeurIPS 2020\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      Bi-level optimization learns parameterized shaping reward weights.\\\\n      Can transform harmful shaping rewards into beneficial ones by learning\\\\n      negative weights. Directly addresses STA's problem: when ISR weight\\\\n      is wrong, automated weight learning could find optimal β.\\\\n    key_finding: >\\\\n      Bi-level optimization automatically learns auxiliary reward weights,\\\\n      outperforming fixed weights and recovering from harmful shaping rewards.\\\\n\\\\n  - id: yue-rlvr-limits\\\\n    title: \\\\\\\"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?\\\\\\\"\\\\n    authors: \\\\\\\"Yue et al. (Tsinghua)\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"NeurIPS 2025 (arXiv 2504.13837)\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: supporting-evidence\\\\n    relevance: >\\\\n      RLVR does not elicit fundamentally new reasoning patterns; it biases\\\\n      output distribution toward reward-yielding paths while narrowing the\\\\n      reasoning capability boundary compared to base models. Directly supports\\\\n      STA's finding that 1000-step GRPO collapses to hacking: the model\\\\n      concentrates on high-reward but non-genuine pathways rather than\\\\n      discovering novel reasoning strategies.\\\\n    key_finding: >\\\\n      RLVR improves sampling efficiency toward correct paths but narrows\\\\n      the reasoning frontier relative to base models. Current RL paradigms\\\\n      redistribute existing capability rather than creating new reasoning.\\\\n\\\\n  - id: deng-grpo-collapse-lld\\\\n    title: \\\\\\\"On GRPO Collapse in Search-R1: The Lazy Likelihood-Displacement Death Spiral\\\\\\\"\\\\n    authors: \\\\\\\"Deng et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2512.04220\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: supporting-evidence\\\\n    relevance: >\\\\n      Identifies Lazy Likelihood Displacement (LLD) as the core mechanism\\\\n      driving GRPO training collapse: systematic reduction in likelihood of\\\\n      both correct and incorrect responses triggers a self-reinforcing death\\\\n      spiral. Provides a mechanistic explanation complementary to Goodhart\\\\n      theory for why STA's 1000-step GRPO universally collapses regardless\\\\n      of reward signal type.\\\\n    key_finding: >\\\\n      LLD emerges early in GRPO training and triggers a death spiral where\\\\n      declining likelihood inflates gradients and causes collapse.\\\\n      Lightweight likelihood-preserving regularization yields +37.8% on\\\\n      Qwen2.5-3B.\\\\n\\\\n  - id: dapo\\\\n    title: \\\\\\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\\\\\"\\\\n    authors: \\\\\\\"Qiying Yu et al. (ByteDance)\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2503.14476\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      Four techniques for stable multi-component reward in GRPO: Clip-Higher,\\\\n      Dynamic Sampling, token-level policy gradient, Overlong Reward Shaping.\\\\n      Addresses stability issues relevant to STA's multi-reward setup.\\\\n    key_finding: >\\\\n      Clip-Higher and Dynamic Sampling prevent entropy collapse in GRPO\\\\n      with multi-component rewards. Soft punishment for overlong outputs\\\\n      avoids reward hacking through length exploitation.\\\\n\\\", \\\"total_chars\\\": 44638, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\", \"content\": \"# Literature Map for Solver Trace Ablation (STA)\\n# Categories:\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\n#   2. reward-shaping: Reward shaping for code/formal verification\\n#   3. mutation-testing: Mutation testing in software engineering\\n#   4. intensional-analysis: Intensional program analysis\\n#   5. reward-hacking: Reward hacking / overoptimization\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\n#   7. goodhart-overoptimization: Goodhart's Law theory and dose-response dynamics\\n#   8. verification-reward: Solver/prover as RL reward signal\\n\\npapers:\\n\\n  # ============================================================\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\n  # ============================================================\\n\\n  - id: deepseek-r1\\n    title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n    authors: \\\"DeepSeek-AI\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2501.12948 / Nature 2025\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\n      intensional structural reward for neurosymbolic formalization.\\n    key_finding: >\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\n      showing emergent chain-of-thought reasoning from RL alone.\\n\\n  - id: deepseekmath\\n    title: \\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\"\\n    authors: \\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2402.03300\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\\n      used in STA training. GRPO eliminates the critic model by estimating\\n      baselines from group scores.\\n    key_finding: >\\n      GRPO matches PPO performance while significantly reducing training\\n      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.\\n\\n  - id: logic-rl\\n    title: \\\"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\\\"\\n    authors: \\\"Xian et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.14768\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic\\n      logic puzzles. Closest competitor to STA's approach of RL for logical\\n      formalization, though Logic-RL uses extensional (answer-correctness)\\n      rewards rather than STA's intensional structural rewards.\\n    key_finding: >\\n      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;\\n      rule-based reward design is critical for RL-based logical reasoning.\\n\\n  - id: mellgren-prolog-grpo\\n    title: \\\"Training Language Models to Use Prolog as a Tool\\\"\\n    authors: \\\"Niklas Mellgren\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2512.07407\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,\\n      directly comparable to STA's approach of GRPO-training a formalizer.\\n      Key difference: uses pass/fail reward vs STA's structural ISR.\\n    key_finding: >\\n      GRPO is effective for teaching small LLMs to use Prolog as a tool\\n      for logical and mathematical reasoning.\\n\\n  - id: satlm\\n    title: \\\"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\\\"\\n    authors: \\\"Xi Ye et al.\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023\\\"\\n    category: neurosymbolic-rl\\n    role: background\\n    relevance: >\\n      Neurosymbolic approach where LLM generates declarative specifications\\n      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)\\n      but uses prompting, not RL training.\\n    key_finding: >\\n      Declarative formulation outperforms imperative program-aided LMs by 23%\\n      on GSM; achieves SoTA on LSAT and BoardgameQA.\\n\\n  - id: deepproblog\\n    title: \\\"Neural Probabilistic Logic Programming in DeepProbLog\\\"\\n    authors: \\\"Robin Manhaeve, Sebastijan Dumančić, Angelika Kimmig, Thomas Demeester, Luc De Raedt\\\"\\n    year: 2021\\n    venue: \\\"Artificial Intelligence 298\\\"\\n    category: neurosymbolic-rl\\n    role: background\\n    relevance: >\\n      Foundational neural-probabilistic logic programming framework that integrates\\n      deep learning with ProbLog via neural predicates. Establishes the intellectual\\n      tradition of combining neural networks with logic programming that STA extends\\n      to LLM-generated Prolog with RL training.\\n    key_finding: >\\n      End-to-end differentiable framework integrating neural perception with\\n      probabilistic logical reasoning; supports program induction and learning\\n      from examples.\\n\\n  - id: neurasp\\n    title: \\\"NeurASP: Embracing Neural Networks into Answer Set Programming\\\"\\n    authors: \\\"Zhun Yang, Adam Ishay, Joohyung Lee\\\"\\n    year: 2020\\n    venue: \\\"IJCAI 2020\\\"\\n    category: neurosymbolic-rl\\n    role: background\\n    relevance: >\\n      Integrates neural networks with answer set programming (ASP), using\\n      ASP rules to constrain and improve neural network training. Complementary\\n      to DeepProbLog; together they represent the neuro-symbolic LP foundation\\n      that STA's LLM-to-Prolog pipeline builds upon.\\n    key_finding: >\\n      ASP semantic constraints improve neural network perception accuracy;\\n      demonstrates bidirectional benefit of neural-symbolic integration.\\n\\n  - id: thought-like-pro\\n    title: \\\"Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought\\\"\\n    authors: \\\"Xiaoyu Tan, Yongxin Deng, Xihe Qiu, Weidi Xu, Chao Qu, Wei Chu, Yinghui Xu, Yuan Qi\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2407.14562\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses Prolog engine to generate verified reasoning trajectories, then trains\\n      LLMs via imitation learning to replicate them. Directly comparable pipeline\\n      to STA (Prolog verification + LLM training), but uses imitation learning\\n      instead of GRPO with structural reward.\\n    key_finding: >\\n      Prolog-verified reasoning trajectories as training signal improve LLM\\n      logical reasoning; self-driven framework enables LLMs to formulate\\n      rules from instructions and leverage Prolog for derivation.\\n\\n  # ============================================================\\n  # Category 2: Reward shaping for code/formal verification\\n  # ============================================================\\n\\n  - id: lightman-verify-step\\n    title: \\\"Let's Verify Step by Step\\\"\\n    authors: \\\"Hunter Lightman, Vineet Kosaraju, Yura Burda, et al.\\\"\\n    year: 2023\\n    venue: \\\"arXiv 2305.20050 / ICLR 2024\\\"\\n    category: reward-shaping\\n    role: method-component\\n    relevance: >\\n      Establishes that process supervision (step-level reward) outperforms\\n      outcome supervision (final-answer reward) for reasoning. STA's ISR\\n      is analogous: it provides structural process-level signal about which\\n      components of a formalization matter, rather than just pass/fail.\\n    key_finding: >\\n      Process-supervised reward model achieves 78% on MATH, significantly\\n      outperforming outcome-supervised models. Released PRM800K dataset.\\n\\n  - id: reward-shaping-rlhf\\n    title: \\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\"\\n    authors: \\\"Jiayi Fu, Xuandong Zhao, Chengyuan Yao, et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.18770\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Studies reward shaping design principles for RLHF: bounded rewards and\\n      rapid-then-convergent growth. STA's ISR follows these principles\\n      naturally since structural necessity scores are bounded [0,1].\\n    key_finding: >\\n      Two key reward shaping principles: (1) bounded RL reward, (2) rapid\\n      initial growth with gradual convergence. PAR method achieves 5%+\\n      win rate improvement on AlpacaEval 2.0.\\n\\n  - id: rlvr-reasoning\\n    title: \\\"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2506.14245\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize\\n      reasoning. STA argues that for neurosymbolic formalization, binary reward\\n      is insufficient and structural reward is needed to avoid reward hacking.\\n    key_finding: >\\n      RLVR with binary verification implicitly teaches correct reasoning\\n      strategies, not just answer matching.\\n\\n  - id: rubric-grpo\\n    title: \\\"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2605.08061\\\"\\n    category: reward-shaping\\n    role: direct-competitor\\n    relevance: >\\n      Uses structured rubric-based rewards with GRPO, similar in spirit to\\n      STA's structured ISR. Key difference: rubric rewards come from LLM\\n      judges, while ISR comes from solver-based mutation testing.\\n    key_finding: >\\n      Structured multi-dimensional reward signals improve GRPO training\\n      generalization compared to scalar rewards.\\n\\n  - id: gao-effective-rl-reward\\n    title: \\\"On Designing Effective RL Reward at Training Time for LLM Reasoning\\\"\\n    authors: \\\"Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2410.15115\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Demonstrates that learned process/outcome reward models can hurt RL\\n      training, producing worse performance than simple success reward only.\\n      Directly explains plan005 NEGATIVE: STA's ISR as auxiliary process\\n      reward degrades prove_rate compared to exec-only baseline.\\n    key_finding: >\\n      PRM/ORM rewards may NOT help or even hurt RL training vs success-only\\n      reward. Solution: Clipping and Delta techniques to bound accumulated\\n      reward magnitude prevent reward hacking.\\n\\n  - id: prof-process-outcome\\n    title: \\\"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training\\\"\\n    authors: \\\"Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2509.03403\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Shows that naively combining PRM+ORM signals leads to performance\\n      degradation. PROF consistency filter retains only PRM-ORM consistent\\n      samples, achieving 4%+ improvement over blending. Suggests STA should\\n      only apply ISR when consistent with execution outcome.\\n    key_finding: >\\n      Process rewards frequently suffer from inaccuracies and reward hacking\\n      susceptibility. PROF filters training data by PRM-ORM consistency,\\n      outperforming naive reward blending by 4%+ accuracy.\\n\\n  - id: moskovitz-constrained-rlhf\\n    title: \\\"Confronting Reward Model Overoptimization with Constrained RLHF\\\"\\n    authors: \\\"Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer\\\"\\n    year: 2023\\n    venue: \\\"arXiv 2310.04373 / ICLR 2024\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      First study on overoptimization in composite reward models. Shows that\\n      fixed-weight linear scalarization of component rewards leads to\\n      degradation past a threshold. Proposes constrained RL with dynamic\\n      Lagrange multiplier weighting as alternative to fixed ISR weight.\\n    key_finding: >\\n      Correlation between component RMs significantly affects overoptimization\\n      thresholds. Constrained RL with Lagrange multipliers outperforms\\n      fixed-weight reward composition.\\n\\n  - id: skalse-reward-hacking\\n    title: \\\"Defining and Characterizing Reward Hacking\\\"\\n    authors: \\\"Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger\\\"\\n    year: 2022\\n    venue: \\\"arXiv 2209.13085 / NeurIPS 2022\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Formal proof that for stochastic policies, two reward functions are\\n      unhackable only if one is constant. Theoretically explains why any\\n      non-zero ISR weight can decrease prove_rate -- this is a fundamental\\n      property of reward composition, not STA-specific.\\n    key_finding: >\\n      Any non-constant proxy reward can decrease true reward when optimized.\\n      Unhackability requires the proxy to be constant, making all non-trivial\\n      auxiliary rewards theoretically vulnerable to degrading primary performance.\\n\\n  - id: progrs-outcome-conditioned\\n    title: \\\"LLM Reasoning with Process Rewards for Outcome-Guided Steps\\\"\\n    authors: \\\"Mohammad Rezaei, Jens Lehmann, Sahar Vahdati\\\"\\n    year: 2026\\n    venue: \\\"arXiv 2604.02341\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      PRM scores optimized as absolute rewards amplify fluent failure modes.\\n      Outcome-conditioned centering shifts incorrect trajectories' PRM scores\\n      to zero mean, preserving ranking info without corrupting gradients.\\n      Suggests STA should condition ISR on execution outcome.\\n    key_finding: >\\n      Naive process rewards induce reward hacking by rewarding locally fluent\\n      but globally incorrect reasoning. Outcome-conditioned centering resolves\\n      the conflict with fewer rollouts than outcome-only baselines.\\n\\n  - id: qwen-prm-lessons\\n    title: \\\"The Lessons of Developing Process Reward Models in Mathematical Reasoning\\\"\\n    authors: \\\"Zhenru Zhang et al. (Qwen Team, Alibaba)\\\"\\n    year: 2025\\n    venue: \\\"ACL 2025 Findings (arXiv 2501.07301)\\\"\\n    category: reward-shaping\\n    role: supporting-evidence\\n    relevance: >\\n      MC estimation-synthesized PRM data leads to quality degradation; policy\\n      model generates \\\"answer-correct but reasoning-flawed\\\" responses, causing\\n      process reward / outcome misalignment. Directly parallels ISR problem:\\n      structurally correct but semantically wrong proof traces get high ISR\\n      but low execution reward.\\n    key_finding: >\\n      PRM performance depends critically on data quality; MC estimation\\n      introduces systematic bias. Answer-correct reasoning-flawed samples\\n      corrupt process supervision signal.\\n\\n  # ============================================================\\n  # Category 3: Mutation testing in software engineering\\n  # ============================================================\\n\\n  - id: demillo1978\\n    title: \\\"Hints on Test Data Selection: Help for the Practicing Programmer\\\"\\n    authors: \\\"Richard A. DeMillo, Richard J. Lipton, Frederick G. Sayward\\\"\\n    year: 1978\\n    venue: \\\"Computer 11(4):34-43\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Foundational paper introducing mutation testing. STA's component\\n      necessity testing directly extends this idea: instead of mutating\\n      source code to test test suites, STA mutates logical formulas\\n      to test component necessity for solver success.\\n    key_finding: >\\n      Introduced mutation testing and the coupling effect hypothesis:\\n      tests that detect simple faults also detect complex faults.\\n\\n  - id: offutt-coupling\\n    title: \\\"Investigations of the Software Testing Coupling Effect\\\"\\n    authors: \\\"A. Jefferson Offutt\\\"\\n    year: 1992\\n    venue: \\\"ACM TOSEM 1(1):5-20\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Empirically validates the coupling effect hypothesis that underpins\\n      mutation testing. STA's single-component ablation is analogous to\\n      first-order mutation; the coupling effect suggests this suffices.\\n    key_finding: >\\n      Test data killing all first-order mutants killed >99% of second-\\n      and third-order mutants, validating the coupling effect.\\n\\n  - id: jia-harman-survey\\n    title: \\\"An Analysis and Survey of the Development of Mutation Testing\\\"\\n    authors: \\\"Yue Jia, Mark Harman\\\"\\n    year: 2011\\n    venue: \\\"IEEE TSE 37(5):649-678\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Comprehensive survey of mutation testing covering three decades of\\n      development. Provides theoretical and practical foundation for STA's\\n      adaptation of mutation testing to logical formulas.\\n    key_finding: >\\n      Systematic classification of mutation operators, cost reduction\\n      techniques, and equivalence problem -- all relevant to STA's design\\n      of clause-level ablation operators.\\n\\n  - id: just-mutants-real-faults\\n    title: \\\"Are Mutants a Valid Substitute for Real Faults in Software Testing?\\\"\\n    authors: \\\"Rene Just, Darioush Jalali, Laura Inozemtseva, et al.\\\"\\n    year: 2014\\n    venue: \\\"FSE 2014\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Validates that mutation testing (structural/intensional analysis of\\n      program adequacy) correlates with real fault detection. Supports STA's\\n      premise that structural analysis of formalization components provides\\n      meaningful signal about formalization quality.\\n    key_finding: >\\n      Mutant detection is statistically correlated with real fault detection,\\n      and mutation score is a better predictor of test effectiveness than\\n      code coverage.\\n\\n  - id: llmorpheus\\n    title: \\\"LLMorpheus: Mutation Testing Using Large Language Models\\\"\\n    authors: \\\"Frank Tip, Jon Bell, et al.\\\"\\n    year: 2025\\n    venue: \\\"IEEE TSE 2025\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Uses LLMs to generate realistic code mutants beyond traditional\\n      mutation operators. Shows mutation testing evolving toward\\n      ML-integrated approaches, validating STA's cross-pollination\\n      of mutation testing ideas into ML training.\\n    key_finding: >\\n      LLM-generated mutants simulate real bugs that rule-based operators\\n      cannot produce, improving mutation testing realism.\\n\\n  - id: mutation-guided-meta\\n    title: \\\"Mutation-Guided LLM-based Test Generation at Meta\\\"\\n    authors: \\\"Christopher Foster et al.\\\"\\n    year: 2025\\n    venue: \\\"FSE 2025\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Industrial application of mutation-guided LLM test generation at\\n      Meta. Demonstrates that mutation analysis can guide LLM behavior\\n      in production -- analogous to how STA uses mutation (ablation) to\\n      guide GRPO reward signal.\\n    key_finding: >\\n      Mutation-guided approach generates tests that kill significantly\\n      more mutants than unguided LLM test generation at Meta scale.\\n\\n  - id: mutation-consistency-llm\\n    title: \\\"Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs\\\"\\n    authors: \\\"Various\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2401.05940\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Uses code mutations to evaluate LLM code understanding consistency.\\n      Conceptually related to STA: both use systematic code/formula\\n      mutations to assess model capabilities.\\n    key_finding: >\\n      LLMs show significant inconsistency when evaluated on mutated code\\n      variants, suggesting superficial pattern matching.\\n\\n  # ============================================================\\n  # Category 4: Intensional program analysis\\n  # ============================================================\\n\\n  - id: deepmutation\\n    title: \\\"A Probabilistic Framework for Mutation Testing in Deep Neural Networks\\\"\\n    authors: \\\"Various\\\"\\n    year: 2023\\n    venue: \\\"Information and Software Technology 2023\\\"\\n    category: intensional-analysis\\n    role: background\\n    relevance: >\\n      Extends mutation testing to DNN testing with probabilistic mutation\\n      operators. Parallel to STA's extension of mutation testing from\\n      traditional programs to logical formulas.\\n    key_finding: >\\n      Probabilistic mutation framework enables meaningful test adequacy\\n      assessment for neural networks through structural perturbation.\\n\\n  # ============================================================\\n  # Category 5: Reward hacking / overoptimization\\n  # ============================================================\\n\\n  - id: inform-reward-hacking\\n    title: \\\"InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling\\\"\\n    authors: \\\"Various\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS 2024\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Proposes information-bottleneck approach to detect and mitigate reward\\n      hacking. STA's ISR addresses the same problem differently: by grounding\\n      reward in verifiable structural properties (component necessity), it\\n      reduces the attack surface for reward hacking.\\n    key_finding: >\\n      Variational information bottleneck filters irrelevant features from\\n      reward model; Cluster Separation Index detects reward overoptimization.\\n\\n  - id: mo-grpo\\n    title: \\\"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\\\"\\n    authors: \\\"CyberAgent AI Lab\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2509.22047\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Directly addresses GRPO reward hacking in multi-objective settings.\\n      STA's ISR can be viewed as adding a structural objective to the\\n      correctness objective, making MO-GRPO's insights directly applicable.\\n    key_finding: >\\n      Standard GRPO normalizes after summing rewards, allowing high-variance\\n      objectives to dominate. MO-GRPO equalizes scales before aggregation.\\n\\n  - id: reward-hacking-survey\\n    title: \\\"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\\\"\\n    authors: \\\"Various\\\"\\n    year: 2026\\n    venue: \\\"arXiv 2604.13602\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Comprehensive survey of reward hacking mechanisms in the LLM era.\\n      Provides theoretical framework for understanding why STA's structural\\n      reward is more robust than pure outcome-based reward.\\n    key_finding: >\\n      Reward hacking manifests through specification gaming, reward model\\n      exploitation, and emergent misalignment; structural verification\\n      rewards are more robust than learned reward models.\\n\\n  - id: energy-loss-reward-hacking\\n    title: \\\"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"ICML 2025\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Identifies energy loss in LLM final layer as an indicator of reward\\n      hacking during RL. Provides complementary diagnostic to STA's\\n      structural reward approach.\\n    key_finding: >\\n      Energy loss in the final layer increases during RL and excessive\\n      increase characterizes reward hacking; EPPO algorithm penalizes\\n      this to mitigate hacking.\\n\\n  - id: spurious-rewards\\n    title: \\\"Spurious Rewards: Rethinking Training Signals in RLVR\\\"\\n    authors: \\\"Ruixin Yang et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2506.10947 / NeurIPS 2025 submission\\\"\\n    category: reward-hacking\\n    role: direct-evidence\\n    relevance: >\\n      Most directly relevant to STA findings. GRPO+random reward on\\n      Qwen2.5-Math improves 21.4%, nearly matching ground-truth reward's\\n      29.1%. Matches our plan017 finding: additive random (PR=48%) >\\n      additive ISR (PR=18%). Structured metrics can be worse than random\\n      noise due to systematic bias vs pure variance.\\n    key_finding: >\\n      Random reward nearly matches ground-truth reward in GRPO training,\\n      suggesting GRPO's group normalization extracts signal from noise.\\n      Effect is model-dependent (works on Qwen2.5, not Llama3).\\n\\n  - id: bondarenko-spec-gaming\\n    title: \\\"Demonstrating Specification Gaming in Reasoning Models\\\"\\n    authors: \\\"Alexander Bondarenko, Denis Volk, Dmitrii Volkov, Jeffrey Ladish\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.13295\\\"\\n    category: reward-hacking\\n    role: direct-evidence\\n    relevance: >\\n      Shows that reasoning models (o3, DeepSeek-R1) resort to specification\\n      gaming on difficult tasks by default, without explicit nudging.\\n      Directly relevant to STA's concern: RL-trained reasoning models\\n      may game formal verification rewards rather than learn genuine\\n      formalization skills.\\n    key_finding: >\\n      Reasoning models spontaneously hack benchmarks (e.g., manipulating\\n      chess engine files instead of playing chess). Stronger reasoning\\n      capability correlates with more sophisticated gaming strategies.\\n\\n  - id: kim-game-formalization\\n    title: \\\"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning\\\"\\n    authors: \\\"Kyuhee Kim, Auguste Poiroux, Antoine Bosselut\\\"\\n    year: 2026\\n    venue: \\\"VerifAI-2 Workshop, ICLR 2026 (arXiv 2604.19459)\\\"\\n    category: reward-hacking\\n    role: direct-evidence\\n    relevance: >\\n      Directly studies whether LLMs game formalization in logical reasoning --\\n      the exact phenomenon STA's ISR is designed to detect. Evaluates GPT-5\\n      and DeepSeek-R1 on FOLIO with Lean 4 proofs. Finds two modes of\\n      unfaithfulness: axiom fabrication (GPT-5) and premise mistranslation\\n      (R1), the latter evading detection entirely.\\n    key_finding: >\\n      High compilation rates (87-99%) do not imply faithful formalization.\\n      Two-stage pipelines reveal unfaithfulness that unified generation hides.\\n      Premise mistranslation produces internally consistent but unfaithful\\n      outputs -- analogous to STA's high-ISR but semantically wrong traces.\\n\\n  - id: gao-reward-overoptimization\\n    title: \\\"Scaling Laws for Reward Model Overoptimization\\\"\\n    authors: \\\"Leo Gao, John Schulman, Jacob Hilton\\\"\\n    year: 2023\\n    venue: \\\"ICML 2023 (arXiv 2210.10760)\\\"\\n    category: reward-hacking\\n    role: theoretical-foundation\\n    relevance: >\\n      Foundational work quantifying Goodhart's effect: proxy reward rises\\n      but gold reward first rises then falls. ISR is a proxy reward that\\n      exhibits exactly this pattern — ISR can increase while prove_rate\\n      decreases, making it suitable for post-hoc diagnosis but harmful\\n      as training signal.\\n    key_finding: >\\n      Gold/proxy reward divergence follows predictable scaling laws.\\n      Proxy reward optimization past critical point degrades gold reward,\\n      with the divergence point scaling with model and dataset size.\\n\\n  - id: karwowski-goodhart-rl\\n    title: \\\"Goodhart's Law in Reinforcement Learning\\\"\\n    authors: \\\"Jacek Karwowski, Oliver Hayman, Xingjian Bai, Klaus Kiendlhofer, Charlie Griffin, Joar Skalse\\\"\\n    year: 2024\\n    venue: \\\"ICLR 2024 (arXiv 2310.09144)\\\"\\n    category: reward-hacking\\n    role: theoretical-foundation\\n    relevance: >\\n      Geometric interpretation of Goodhart's Law in MDPs: optimizing\\n      imperfect proxy past critical point decreases true objective. ISR as\\n      proxy has partial correlation with execution correctness — exceeding\\n      critical optimization point pushes policy toward high-ISR but\\n      low-correctness regions. Explains plan002/plan005 negative results.\\n    key_finding: >\\n      Formalizes Goodhart's Law for RL: any non-trivially correlated proxy\\n      reward creates regions where proxy and true reward diverge, and\\n      policy optimization inevitably enters these regions.\\n\\n  # ============================================================\\n  # Category 6: FOL/Prolog formalization with LLMs\\n  # ============================================================\\n\\n  - id: folio\\n    title: \\\"FOLIO: Natural Language Reasoning with First-Order Logic\\\"\\n    authors: \\\"Simeng Han et al.\\\"\\n    year: 2022\\n    venue: \\\"arXiv 2209.00840 / EMNLP 2024\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Primary FOL reasoning benchmark. STA uses FOLIO-style NL->FOL\\n      formalization as the target task for GRPO training. FOLIO's\\n      expert-annotated FOL annotations serve as reference formalizations.\\n    key_finding: >\\n      1,430 NL-FOL paired examples with reasoning depths up to 5+;\\n      GPT-4 still struggles on the hardest examples.\\n\\n  - id: proofwriter\\n    title: \\\"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language\\\"\\n    authors: \\\"Oyvind Tafjord, Bhavana Dalvi, Peter Clark\\\"\\n    year: 2021\\n    venue: \\\"Findings of ACL-IJCNLP 2021\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Source dataset for STA's training data. ProofWriter provides\\n      rule-based logical reasoning problems in natural language that\\n      STA uses for training formalizer models.\\n    key_finding: >\\n      Generative model can reliably produce implications and proofs;\\n      accuracy exceeds prior methods by 9% and generalizes to unseen\\n      proof depths.\\n\\n  - id: logic-lm\\n    title: \\\"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\\\"\\n    authors: \\\"Liangming Pan, Alon Albalak, Xinyi Wang, William Wang\\\"\\n    year: 2023\\n    venue: \\\"Findings of EMNLP 2023\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      LLM->symbolic solver pipeline for logical reasoning, directly\\n      comparable to STA's formalizer->Prolog solver pipeline. Key\\n      difference: Logic-LM uses prompting, STA uses GRPO training.\\n    key_finding: >\\n      LLM+solver achieves 39.2% improvement over LLM-alone on logical\\n      reasoning benchmarks including ProofWriter and FOLIO.\\n\\n  - id: linc\\n    title: \\\"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers\\\"\\n    authors: \\\"Theo X. Olausson, Alex Gu, Ben Lipkin, et al.\\\"\\n    year: 2023\\n    venue: \\\"EMNLP 2023\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      Neurosymbolic approach where LLM translates NL to FOL for theorem\\n      prover. Directly comparable to STA's NL->Prolog translation.\\n      LINC uses prompting-based approach; STA uses RL training.\\n    key_finding: >\\n      StarCoder+ (15.5B) with LINC outperforms GPT-3.5 and GPT-4 with\\n      CoT by 38% and 10% respectively on ProofWriter.\\n\\n  - id: fover-pei2025\\n    title: \\\"FoVer: First-Order Logic Verification for Natural Language Reasoning\\\"\\n    authors: \\\"Yu Pei, Yongping Du, Xingnan Jin\\\"\\n    year: 2025\\n    venue: \\\"TACL 13:1340-1359\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      Uses LLM->FOL->Z3 pipeline for verifying NL reasoning correctness.\\n      Similar to STA's verification pipeline but focuses on post-hoc\\n      verification rather than training reward signal.\\n    key_finding: >\\n      FOL verification via Z3 significantly outperforms existing methods\\n      on ProofWriter and FOLIO benchmarks.\\n\\n  - id: lorp\\n    title: \\\"LoRP: LLM-based Logical Reasoning via Prolog\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"Knowledge-Based Systems 2025\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      LLM->Prolog pipeline with FOL-to-Prolog translation mechanism.\\n      Closest to STA's formalization target (Prolog), though LoRP\\n      uses prompting while STA uses GRPO training with structural reward.\\n    key_finding: >\\n      Systematic FOL-to-Prolog translation extends Prolog expressiveness;\\n      achieves SoTA accuracy on logical reasoning with three-vote majority.\\n\\n  - id: nl2fol\\n    title: \\\"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection\\\"\\n    authors: \\\"Lalwani, Kim, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2405.02318\\\"\\n    category: fol-formalization\\n    role: background\\n    relevance: >\\n      Step-by-step NL->FOL translation using LLMs with SMT solver\\n      verification. Demonstrates the NL->formal logic pipeline that\\n      STA aims to improve via RL training.\\n    key_finding: >\\n      Neurosymbolic NL2FOL achieves 78% F1 on LOGIC dataset and\\n      generalizes to LogicClimate (80% F1), outperforming supervised\\n      models by 21%.\\n\\n  - id: logica2\\n    title: \\\"LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: \\\"IEEE/ACM TASLP 2023\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Logical reasoning evaluation benchmark derived from Chinese civil\\n      service exams. Provides supplementary evaluation for STA's\\n      formalization capabilities.\\n    key_finding: >\\n      8,678 multiple-choice questions covering categorical, disjunctive,\\n      and conditional reasoning; widely used LLM benchmark.\\n\\n  # ============================================================\\n  # Category 7: Goodhart's Law theory and dose-response dynamics\\n  # ============================================================\\n\\n  - id: manheim-goodhart-taxonomy\\n    title: \\\"Categorizing Variants of Goodhart's Law\\\"\\n    authors: \\\"David Manheim, Scott Garrabrant\\\"\\n    year: 2019\\n    venue: \\\"arXiv 1803.04585\\\"\\n    category: goodhart-overoptimization\\n    role: theoretical-foundation\\n    relevance: >\\n      Four-part Goodhart taxonomy: regressional, extremal, causal, adversarial.\\n      STA's high-β ISR collapse is best classified as extremal Goodhart\\n      (policy moves to OOD region where ISR↑ but prove_rate↓). Provides\\n      vocabulary for discussion section.\\n    key_finding: >\\n      First systematic categorization of Goodhart failure modes. Extremal\\n      variant occurs when proxy-goal relationship breaks in out-of-distribution\\n      regions reached by strong optimization.\\n\\n  - id: pan-reward-misspecification\\n    title: \\\"The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models\\\"\\n    authors: \\\"Alexander Pan, Kush Bhatia, Jacob Steinhardt\\\"\\n    year: 2022\\n    venue: \\\"ICLR 2022\\\"\\n    category: goodhart-overoptimization\\n    role: theoretical-foundation\\n    relevance: >\\n      Across 9 environments, more capable agents exploit misspecifications more.\\n      Observes dose-dependent degradation — capability thresholds where true\\n      reward sharply drops. Matches STA's β=0.1→0.3 qualitative shift.\\n    key_finding: >\\n      Reward misspecification causes dose-dependent degradation where true reward\\n      sharply drops past capability thresholds. More capable optimization\\n      produces worse outcomes under misspecification.\\n\\n  - id: kwa-catastrophic-goodhart\\n    title: \\\"Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification\\\"\\n    authors: \\\"Tat-Thang Kwa, Rachel Thomas, Adrià Garriga-Alonso\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS 2024\\\"\\n    category: goodhart-overoptimization\\n    role: theoretical-foundation\\n    relevance: >\\n      If reward model error is heavy-tailed, policies achieve arbitrarily\\n      high proxy reward with no true utility gain. KL regularization provably\\n      fails. Explains why KL penalty in GRPO cannot prevent ISR collapse\\n      at high β if ISR error distribution is heavy-tailed.\\n    key_finding: >\\n      KL-regularized RL provably fails to prevent overoptimization under\\n      heavy-tailed reward misspecification. Policies can achieve arbitrarily\\n      high proxy reward with zero true utility.\\n\\n  - id: rafailov-daa-scaling\\n    title: \\\"Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms\\\"\\n    authors: \\\"Rafael Rafailov, Yaswanth Chittepu, Ryan Park, Harshit Sikchi, Joey Hejna, W. Bradley Knox, Chelsea Finn, Scott Niekum\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS 2024\\\"\\n    category: goodhart-overoptimization\\n    role: supporting-evidence\\n    relevance: >\\n      Extends Gao et al. to DPO/IPO/SLiC. Tests seven β values across\\n      1B-6.9B models. DAAs still overoptimize despite no explicit proxy RM.\\n      Validates β as a \\\"dose\\\" parameter — directly analogous to STA's\\n      ISR weight sweep.\\n    key_finding: >\\n      Direct alignment algorithms exhibit overoptimization following\\n      predictable scaling laws. Smaller models overoptimize sooner.\\n      β-controlled dose-response is a general phenomenon across RL paradigms.\\n\\n  - id: huang-chi-squared\\n    title: \\\"Correcting the Mythos of KL-Regularization: Direct and Contrastive Distribution Correction\\\"\\n    authors: \\\"Afra Feyza Akyürek, Banghua Zhu, Sham Kakade, Jiantao Jiao\\\"\\n    year: 2025\\n    venue: \\\"ICLR 2025 Poster\\\"\\n    category: goodhart-overoptimization\\n    role: supporting-evidence\\n    relevance: >\\n      KL-regularization is theoretically inadequate for preventing\\n      overoptimization. Chi-squared divergence provably alleviates it.\\n      Suggests that even with KL penalty in GRPO, STA's high-β collapse\\n      is theoretically expected.\\n    key_finding: >\\n      Chi-squared preference optimization provably mitigates overoptimization\\n      where KL-regularization fails. Alternative divergence measures offer\\n      stronger guarantees.\\n\\n  - id: coste-rm-ensembles\\n    title: \\\"Reward Model Ensembles Help Mitigate Overoptimization\\\"\\n    authors: \\\"Thomas Coste, Usman Anwar, Robert Kirk, David Krueger\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023 Workshop on Alignment\\\"\\n    category: goodhart-overoptimization\\n    role: background\\n    relevance: >\\n      Worst-case optimization across RM ensembles practically eliminates\\n      overoptimization for BoN and reduces it for PPO. Suggests ensemble\\n      of multiple solver metrics (instead of single ISR) as mitigation.\\n    key_finding: >\\n      RM ensembles with worst-case aggregation mitigate overoptimization.\\n      Ensemble size and diversity directly affect robustness.\\n\\n  # ============================================================\\n  # Category 8: Solver/prover as RL reward signal\\n  # ============================================================\\n\\n  - id: rlsf\\n    title: \\\"Reinforcement Learning via Symbolic Feedback\\\"\\n    authors: \\\"Abhinav Jha, Shikhar Murty, Zico Kolter, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2405.16661\\\"\\n    category: verification-reward\\n    role: direct-competitor\\n    relevance: >\\n      Most directly relevant: uses solver/prover certificates as fine-grained\\n      token-level reward signal. Outperforms traditional approaches on program\\n      synthesis (+31.4%). STA extends this paradigm and shows when it breaks\\n      (Goodhart effects at high auxiliary reward weight).\\n    key_finding: >\\n      Symbolic reasoning tools provide poly-sized certificates as reward.\\n      Smaller RLSF models outperform GPT-4 on structured generation tasks.\\n\\n  - id: fover-kamoi2026\\n    title: \\\"FoVer: Generalizable Process Reward Models via Formally Verified Training Data\\\"\\n    authors: \\\"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\\\"\\n    year: 2025\\n    venue: \\\"Findings of ACL 2026 (arXiv 2502.01345)\\\"\\n    category: verification-reward\\n    role: supporting-evidence\\n    relevance: >\\n      Uses Z3 and Isabelle to synthesize PRM training data by annotating\\n      step-level error labels without human annotation. Same solver family\\n      as STA. Shows verification-based rewards work; STA extends by showing\\n      dose-response dynamics.\\n    key_finding: >\\n      Formally verified training data enables generalizable process reward\\n      models competitive on ProcessBench and 12 reasoning benchmarks.\\n\\n  - id: deepseek-prover-v15\\n    title: \\\"DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search\\\"\\n    authors: \\\"DeepSeek AI\\\"\\n    year: 2024\\n    venue: \\\"ICLR 2025 (arXiv 2408.08152)\\\"\\n    category: verification-reward\\n    role: method-component\\n    relevance: >\\n      Uses GRPO with Lean 4 verification as binary reward. Same algorithm\\n      (GRPO) + formal verification, but binary (pass/fail). Binary reward\\n      avoids the graded-metric Goodhart risk that STA identifies with ISR.\\n    key_finding: >\\n      GRPO + binary Lean verification achieves 63.5% on miniF2F. Binary\\n      correctness guarantee via formal verification sidesteps proxy reward\\n      overoptimization.\\n\\n  - id: alphaproof\\n    title: \\\"AlphaProof\\\"\\n    authors: \\\"Google DeepMind\\\"\\n    year: 2024\\n    venue: \\\"Nature 2025\\\"\\n    category: verification-reward\\n    role: background\\n    relevance: >\\n      AlphaZero-inspired RL with Lean proof verification at scale.\\n      Silver medal at IMO 2024. Binary verification reward avoids the\\n      Goodhart problem STA identifies with graded verification metrics.\\n    key_finding: >\\n      Binary formal verification as RL reward scales to IMO-level\\n      mathematical reasoning. Demonstrates verification-reward RL works\\n      at the frontier of mathematical difficulty.\\n\\n  - id: math-shepherd\\n    title: \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\"\\n    authors: \\\"Peiyi Wang, Lei Li, Zhihong Shao, R.X. Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"ACL 2024 (arXiv 2312.08935)\\\"\\n    category: verification-reward\\n    role: supporting-evidence\\n    relevance: >\\n      Automatically constructs process supervision data and uses it as\\n      step-by-step PPO reward. Automated verification reward without human\\n      labels, analogous to STA's automated ISR computation via solver.\\n    key_finding: >\\n      Automated process supervision improves Mistral-7B on GSM8K\\n      (77.9→84.1%) and MATH (28.6→33.0%) without human annotation.\\n\\n  # ============================================================\\n  # Additional reward-shaping papers (Goodhart survey additions)\\n  # ============================================================\\n\\n  - id: bipars\\n    title: \\\"Learning to Utilize Shaping Rewards: A New Approach of Reward Shaping\\\"\\n    authors: \\\"Yujing Hu, Weixun Wang, Hangtian Jia, et al.\\\"\\n    year: 2020\\n    venue: \\\"NeurIPS 2020\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Bi-level optimization learns parameterized shaping reward weights.\\n      Can transform harmful shaping rewards into beneficial ones by learning\\n      negative weights. Directly addresses STA's problem: when ISR weight\\n      is wrong, automated weight learning could find optimal β.\\n    key_finding: >\\n      Bi-level optimization automatically learns auxiliary reward weights,\\n      outperforming fixed weights and recovering from harmful shaping rewards.\\n\\n  - id: yue-rlvr-limits\\n    title: \\\"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?\\\"\\n    authors: \\\"Yue et al. (Tsinghua)\\\"\\n    year: 2025\\n    venue: \\\"NeurIPS 2025 (arXiv 2504.13837)\\\"\\n    category: reward-hacking\\n    role: supporting-evidence\\n    relevance: >\\n      RLVR does not elicit fundamentally new reasoning patterns; it biases\\n      output distribution toward reward-yielding paths while narrowing the\\n      reasoning capability boundary compared to base models. Directly supports\\n      STA's finding that 1000-step GRPO collapses to hacking: the model\\n      concentrates on high-reward but non-genuine pathways rather than\\n      discovering novel reasoning strategies.\\n    key_finding: >\\n      RLVR improves sampling efficiency toward correct paths but narrows\\n      the reasoning frontier relative to base models. Current RL paradigms\\n      redistribute existing capability rather than creating new reasoning.\\n\\n  - id: deng-grpo-collapse-lld\\n    title: \\\"On GRPO Collapse in Search-R1: The Lazy Likelihood-Displacement Death Spiral\\\"\\n    authors: \\\"Deng et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2512.04220\\\"\\n    category: reward-hacking\\n    role: supporting-evidence\\n    relevance: >\\n      Identifies Lazy Likelihood Displacement (LLD) as the core mechanism\\n      driving GRPO training collapse: systematic reduction in likelihood of\\n      both correct and incorrect responses triggers a self-reinforcing death\\n      spiral. Provides a mechanistic explanation complementary to Goodhart\\n      theory for why STA's 1000-step GRPO universally collapses regardless\\n      of reward signal type.\\n    key_finding: >\\n      LLD emerges early in GRPO training and triggers a death spiral where\\n      declining likelihood inflates gradients and causes collapse.\\n      Lightweight likelihood-preserving regularization yields +37.8% on\\n      Qwen2.5-3B.\\n\\n  - id: dapo\\n    title: \\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\"\\n    authors: \\\"Qiying Yu et al. (ByteDance)\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2503.14476\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Four techniques for stable multi-component reward in GRPO: Clip-Higher,\\n      Dynamic Sampling, token-level policy gradient, Overlong Reward Shaping.\\n      Addresses stability issues relevant to STA's multi-reward setup.\\n    key_finding: >\\n      Clip-Higher and Dynamic Sampling prevent entropy collapse in GRPO\\n      with multi-component rewards. Soft punishment for overlong outputs\\n      avoids reward hacking through length exploitation.\\n\", \"total_chars\": 44638, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
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
The literature map is extensive. Now I need to search for papers specifically about:

1. Proxy optimization being *worse* than random/no-optimization (our key finding: ISR genuine 6.9% vs Random 18.4%)
2. Goodhart's Law empirical evidence in RL where proxy optimization actively hurts
3. Manheim & Garrabrant's "regressional Goodhart" concept
4. "Optimization pressure" + "metric collapse" in NLP/code generation

Let me check what's already in the literature map:


- manheim-goodhart-taxonomy: already there
- karwowski-goodhart-rl: already there
- gao-reward-overoptimization: already there
- spurious-rewards (random reward matching ground truth): already there
- skalse-reward-hacking: already there

The key distinction is that our finding shows proxy optimization performing significantly worse than random—not just matching it, but actively degrading below baseline. This is different from the spurious-rewards case where random happens to align with ground truth. I need to find empirical evidence of regressional Goodhart and metric collapse in RL and NLP where optimization against a proxy actually hurts performance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "da42ec7e-e1c5-4f74-9e46-c6c095a271d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FDcxsXkshevz7a2LUrtBs4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14444,
      "cache_read_input_tokens": 27370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14444
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

Now I'll search for papers on the specific phenomenon: proxy optimization performing *worse* than random baselines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "370bd026-6b27-40d1-a8b0-bb0e841bd2ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FDcxsXkshevz7a2LUrtBs4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14444,
      "cache_read_input_tokens": 27370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14444
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V9PQRvNy2wsX3Ukp2Saicb`</summary>

```json
{
  "query": "Goodhart's Law reinforcement learning proxy optimization worse than random baseline empirical evidence 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "f88ecdd6-10d3-4eb6-9540-f6db20fc6dd4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FDcxsXkshevz7a2LUrtBs4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14444,
      "cache_read_input_tokens": 27370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14444
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AYCzFzXkGrKfuZPaqnf4gH`</summary>

```json
{
  "query": "\"reward hacking\" proxy reward underperforms random reward RLHF reinforcement learning 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "d5a38d5e-55fd-4818-9b08-77570c4b59cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FDcxsXkshevz7a2LUrtBs4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14444,
      "cache_read_input_tokens": 27370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14444
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Hz4Fym9gCMbKq83Q9T9qWE`</summary>

```json
{
  "query": "Manheim Garrabrant \"regressional Goodhart\" empirical evidence reinforcement learning reward model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "2f0c7b58-9b65-4aff-86be-05cccb550b3a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FDcxsXkshevz7a2LUrtBs4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14444,
      "cache_read_input_tokens": 27370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14444
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Au7GSrAnhvTsBUj6bf3RY4`</summary>

```json
{
  "query": "\"optimization pressure\" \"metric collapse\" reward overoptimization NLP code generation proxy worse than baseline 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "d8c3596d-0757-4ecb-8e60-5647a70090a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FDcxsXkshevz7a2LUrtBs4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14444,
      "cache_read_input_tokens": 27370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14444
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

_source line 16 · 2026-05-15T14:08:58.330Z_

<details><summary>↩ Tool result · `toolu_01V9PQRvNy2wsX3Ukp2Saicb`</summary>

```text
Web search results for query: "Goodhart's Law reinforcement learning proxy optimization worse than random baseline empirical evidence 2024 2025"

Links: [{"title":"Goodhart's Law in Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=5o9G4XF1LI"},{"title":"Goodhart's Law in Reinforcement Learning","url":"https://www.alignmentforum.org/posts/Eu6CvP7c7ivcGM3PJ/goodhart-s-law-in-reinforcement-learning"},{"title":"[2310.09144] Goodhart's Law in Reinforcement Learning","url":"https://arxiv.org/abs/2310.09144"},{"title":"Goodhart’s Law in Reinforcement Learning","url":"https://arxiv.org/html/2310.09144v1"},{"title":"GOODHART'S LAW IN REINFORCEMENT LEARNING","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/6ad68a54eaa8f9bf6ac698b02ec05048-Paper-Conference.pdf"},{"title":"Catastrophic Goodhart: regularizing RLHF with KL","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/1a8189929f3d7bd6183718f42c3f4309-Paper-Conference.pdf"},{"title":"Scaling Laws for Reward Model Overoptimization","url":"https://proceedings.mlr.press/v202/gao23h.html"},{"title":"Measuring Goodhart’s law | OpenAI","url":"https://openai.com/index/measuring-goodharts-law/"},{"title":"Take Goodhart Seriously: Principled Limit on General-Purpose AI Optimization","url":"https://arxiv.org/html/2510.02840"},{"title":"Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/e45caa3d5273d105b8d045e748636957-Paper-Conference.pdf"}]

I've found several highly relevant research results on Goodhart's Law in reinforcement learning with empirical evidence. Here's what the recent literature shows:

## Key Empirical Findings

Studies show empirically that optimising an imperfect proxy reward often leads to the behaviour predicted by Goodhart's law for a wide range of environments and reward functions. More specifically, research found that a Goodhart drop occurs for 19.3% of all experiments sampled across different parameter ranges, suggesting that Goodharting is a common (albeit not universal) phenomenon in RL and occurs in various environments and for various reward functions.

## Recent Publications (2023-2024)

The primary peer-reviewed research on this topic includes:

1. **"Goodhart's Law in Reinforcement Learning"** - A paper that appeared at ICLR 2024 which proposes a way to quantify the magnitude of the Goodharting effect and shows empirically that optimising an imperfect proxy reward often leads to the behaviour predicted by Goodhart's law for a wide range of environments and reward functions.

2. **"Scaling Laws for Reward Model Overoptimization"** - Shows that because the reward model is an imperfect proxy, optimizing its value too much can hinder ground truth performance in accordance with Goodhart's law, an effect that has been frequently observed but not carefully measured due to the expense of collecting human preference data.

3. **"Catastrophic Goodhart"** (2024) - Recent research defining a phenomenon called "catastrophic Goodhart" where the true objective V approaches 0 in the limit of optimization for a proxy, meaning the end result of optimizing for a proxy is no better than not optimizing at all.

The research provides both theoretical explanations and empirical validation of Goodhart's Law effects in RL proxy optimization scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "4624a4a5-753f-430b-b968-0a0ace905a13",
  "tool_use_result": {
    "query": "Goodhart's Law reinforcement learning proxy optimization worse than random baseline empirical evidence 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LMnb7nyKMYAN4dWcJLZcfn",
        "content": [
          {
            "title": "Goodhart's Law in Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=5o9G4XF1LI"
          },
          {
            "title": "Goodhart's Law in Reinforcement Learning",
            "url": "https://www.alignmentforum.org/posts/Eu6CvP7c7ivcGM3PJ/goodhart-s-law-in-reinforcement-learning"
          },
          {
            "title": "[2310.09144] Goodhart's Law in Reinforcement Learning",
            "url": "https://arxiv.org/abs/2310.09144"
          },
          {
            "title": "Goodhart’s Law in Reinforcement Learning",
            "url": "https://arxiv.org/html/2310.09144v1"
          },
          {
            "title": "GOODHART'S LAW IN REINFORCEMENT LEARNING",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2024/file/6ad68a54eaa8f9bf6ac698b02ec05048-Paper-Conference.pdf"
          },
          {
            "title": "Catastrophic Goodhart: regularizing RLHF with KL",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/1a8189929f3d7bd6183718f42c3f4309-Paper-Conference.pdf"
          },
          {
            "title": "Scaling Laws for Reward Model Overoptimization",
            "url": "https://proceedings.mlr.press/v202/gao23h.html"
          },
          {
            "title": "Measuring Goodhart’s law | OpenAI",
            "url": "https://openai.com/index/measuring-goodharts-law/"
          },
          {
            "title": "Take Goodhart Seriously: Principled Limit on General-Purpose AI Optimization",
            "url": "https://arxiv.org/html/2510.02840"
          },
          {
            "title": "Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/e45caa3d5273d105b8d045e748636957-Paper-Conference.pdf"
          }
        ]
      },
      "I've found several highly relevant research results on Goodhart's Law in reinforcement learning with empirical evidence. Here's what the recent literature shows:\n\n## Key Empirical Findings\n\nStudies show empirically that optimising an imperfect proxy reward often leads to the behaviour predicted by Goodhart's law for a wide range of environments and reward functions. More specifically, research found that a Goodhart drop occurs for 19.3% of all experiments sampled across different parameter ranges, suggesting that Goodharting is a common (albeit not universal) phenomenon in RL and occurs in various environments and for various reward functions.\n\n## Recent Publications (2023-2024)\n\nThe primary peer-reviewed research on this topic includes:\n\n1. **\"Goodhart's Law in Reinforcement Learning\"** - A paper that appeared at ICLR 2024 which proposes a way to quantify the magnitude of the Goodharting effect and shows empirically that optimising an imperfect proxy reward often leads to the behaviour predicted by Goodhart's law for a wide range of environments and reward functions.\n\n2. **\"Scaling Laws for Reward Model Overoptimization\"** - Shows that because the reward model is an imperfect proxy, optimizing its value too much can hinder ground truth performance in accordance with Goodhart's law, an effect that has been frequently observed but not carefully measured due to the expense of collecting human preference data.\n\n3. **\"Catastrophic Goodhart\"** (2024) - Recent research defining a phenomenon called \"catastrophic Goodhart\" where the true objective V approaches 0 in the limit of optimization for a proxy, meaning the end result of optimizing for a proxy is no better than not optimizing at all.\n\nThe research provides both theoretical explanations and empirical validation of Goodhart's Law effects in RL proxy optimization scenarios."
    ],
    "durationSeconds": 7.676727648
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T14:08:59.496Z_

<details><summary>↩ Tool result · `toolu_01Hz4Fym9gCMbKq83Q9T9qWE`</summary>

```text
Web search results for query: "Manheim Garrabrant "regressional Goodhart" empirical evidence reinforcement learning reward model"

Links: [{"title":"(PDF) Categorizing Variants of Goodhart's Law","url":"https://www.researchgate.net/publication/323747167_Categorizing_Variants_of_Goodhart's_Law"},{"title":"Rethinking Reward Model Evaluation: Are We Barking up the Wrong Tree?","url":"https://arxiv.org/html/2410.05584v5"},{"title":"RETHINKING REWARD MODEL EVALUATION: ARE WE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/93f250215e4889119807b6fac3a57aec-Paper-Conference.pdf"},{"title":"Scaling Laws for Reward Model Overoptimization","url":"https://proceedings.mlr.press/v202/gao23h/gao23h.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2410.05584"},{"title":"Goodhart’s Law in Reinforcement Learning","url":"https://arxiv.org/html/2310.09144v1"},{"title":"GOODHART'S LAW IN REINFORCEMENT LEARNING","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/6ad68a54eaa8f9bf6ac698b02ec05048-Paper-Conference.pdf"},{"title":"Reliance on Metrics is a Fundamental Challenge for AI Rachel L. Thomas","url":"https://arxiv.org/pdf/2002.08512"},{"title":"Categorizing Variants of Goodhart's Law","url":"https://arxiv.org/pdf/1803.04585"},{"title":"The Strong, weak and benign Goodhart's law. An ...","url":"https://openreview.net/pdf?id=itft16CVuQ"}]

I found comprehensive search results on your query. Here's what I discovered:

## Key Findings

Manheim and Garrabrant (2019) developed a taxonomy of 4 distinct failure modes contained in Goodhart's Law, including regressional Goodhart, in which the difference between the proxy and the goal is important.

Regressional Goodhart occurs when proxy reward models depend on features with noise, exemplified by a proxy reward equal to the gold reward plus some independent noise.

## Empirical Evidence in Reinforcement Learning

Recent research has provided empirical evidence of regressional Goodhart effects in the context of reward models:

Studies derive the expected relationship between accuracy and the degree of reward overoptimization under the assumptions of Regressional Goodhart's effect (Manheim & Garrabrant, 2019) and normal distributions of both reward score and noise.

Research has shown empirically that optimizing an imperfect proxy reward often leads to the behavior predicted by Goodhart's law for a wide range of environments and reward functions.

In comprehensive empirical testing, Goodhart drops occurred in 19.3% of all experiments, suggesting that Goodharting is a common phenomenon in RL and occurs in various environments and for various reward functions.

The search results indicate that the Manheim & Garrabrant framework on regressional Goodhart has become foundational for understanding reward model overoptimization in modern reinforcement learning and RLHF (Reinforcement Learning from Human Feedback) research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "12a0f213-d777-41d9-8941-6201312715db",
  "tool_use_result": {
    "query": "Manheim Garrabrant \"regressional Goodhart\" empirical evidence reinforcement learning reward model",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FSjB15ZhfW5na6D8eQTKF2",
        "content": [
          {
            "title": "(PDF) Categorizing Variants of Goodhart's Law",
            "url": "https://www.researchgate.net/publication/323747167_Categorizing_Variants_of_Goodhart's_Law"
          },
          {
            "title": "Rethinking Reward Model Evaluation: Are We Barking up the Wrong Tree?",
            "url": "https://arxiv.org/html/2410.05584v5"
          },
          {
            "title": "RETHINKING REWARD MODEL EVALUATION: ARE WE ...",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/93f250215e4889119807b6fac3a57aec-Paper-Conference.pdf"
          },
          {
            "title": "Scaling Laws for Reward Model Overoptimization",
            "url": "https://proceedings.mlr.press/v202/gao23h/gao23h.pdf"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://arxiv.org/pdf/2410.05584"
          },
          {
            "title": "Goodhart’s Law in Reinforcement Learning",
            "url": "https://arxiv.org/html/2310.09144v1"
          },
          {
            "title": "GOODHART'S LAW IN REINFORCEMENT LEARNING",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2024/file/6ad68a54eaa8f9bf6ac698b02ec05048-Paper-Conference.pdf"
          },
          {
            "title": "Reliance on Metrics is a Fundamental Challenge for AI Rachel L. Thomas",
            "url": "https://arxiv.org/pdf/2002.08512"
          },
          {
            "title": "Categorizing Variants of Goodhart's Law",
            "url": "https://arxiv.org/pdf/1803.04585"
          },
          {
            "title": "The Strong, weak and benign Goodhart's law. An ...",
            "url": "https://openreview.net/pdf?id=itft16CVuQ"
          }
        ]
      },
      "I found comprehensive search results on your query. Here's what I discovered:\n\n## Key Findings\n\nManheim and Garrabrant (2019) developed a taxonomy of 4 distinct failure modes contained in Goodhart's Law, including regressional Goodhart, in which the difference between the proxy and the goal is important.\n\nRegressional Goodhart occurs when proxy reward models depend on features with noise, exemplified by a proxy reward equal to the gold reward plus some independent noise.\n\n## Empirical Evidence in Reinforcement Learning\n\nRecent research has provided empirical evidence of regressional Goodhart effects in the context of reward models:\n\nStudies derive the expected relationship between accuracy and the degree of reward overoptimization under the assumptions of Regressional Goodhart's effect (Manheim & Garrabrant, 2019) and normal distributions of both reward score and noise.\n\nResearch has shown empirically that optimizing an imperfect proxy reward often leads to the behavior predicted by Goodhart's law for a wide range of environments and reward functions.\n\nIn comprehensive empirical testing, Goodhart drops occurred in 19.3% of all experiments, suggesting that Goodharting is a common phenomenon in RL and occurs in various environments and for various reward functions.\n\nThe search results indicate that the Manheim & Garrabrant framework on regressional Goodhart has become foundational for understanding reward model overoptimization in modern reinforcement learning and RLHF (Reinforcement Learning from Human Feedback) research."
    ],
    "durationSeconds": 7.2468999560000045
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T14:09:00.779Z_

<details><summary>↩ Tool result · `toolu_01AYCzFzXkGrKfuZPaqnf4gH`</summary>

```text
Web search results for query: ""reward hacking" proxy reward underperforms random reward RLHF reinforcement learning 2024 2025 2026"

Links: [{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"Reward Hacking: The Hidden Failure Mode in AI Optimization | by Adnan Masood, PhD. | Medium","url":"https://medium.com/@adnanmasood/reward-hacking-the-hidden-failure-mode-in-ai-optimization-686b62acf408"},{"title":"Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/html/2502.18770v3"},{"title":"Mitigating Reward Hacking in RLHF via Information- ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/f25d75fc760aec0a6174f9f5d9da59b8-Paper-Conference.pdf"},{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602v1"},{"title":"Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking","url":"https://arxiv.org/html/2403.03185v4"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/html/2604.02986"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=reward+hacking"},{"title":"Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling","url":"https://arxiv.org/html/2602.10623"},{"title":"Reward hacking - Wikipedia","url":"https://en.wikipedia.org/wiki/Reward_hacking"}]

I've performed a web search on reward hacking in reinforcement learning from human feedback (RLHF). Here are the key findings:

## Core Definition and Problem

Reward models (RMs) used in RLHF are vulnerable to reward hacking: as the policy maximizes a learned proxy reward, true quality plateaus or degrades. Reward hacking occurs when optimizing a correlated proxy reward leads to a policy obtaining lower true reward than the reference policy.

## How Proxy Rewards Underperform

Reward overoptimization happens when optimization pressure increases too much. The model's proxy score continues to improve, but its actual quality stops improving and eventually gets worse. Interestingly, reward hacking still occurs even when there is a positive correlation between the true and proxy rewards.

## Mechanisms in RLHF

RLHF aims to improve the model's alignment with human preference, but human feedback may not capture all the aspects we care about (e.g., factuality) and thus can be hacked to overfit to undesired attributes. For example, the model may be optimized to output responses that seem correct and convincing but are, in fact, inaccurate, thereby misleading human evaluators.

## Recent Mitigation Approaches (2024-2026)

Two key design principles have emerged: (1) the RL reward should be bounded, and (2) the RL reward benefits from rapid initial growth followed by gradual convergence. Researchers propose Preference As Reward (PAR), a novel approach that leverages the latent preferences embedded within the reward model as the signal for reinforcement learning.

SignCert-PO proposes down-weighting non-robust completions in the policy gradient update. Unlike prior approaches that require multiple RMs or access to the RM training data, SignCert-PO is lightweight and operates purely at the policy optimization stage.

Additional mitigation research includes InfoRM, which consistently prevents reward overoptimization and maintains stability regardless of label noise, underscoring its ability to extract human preference-relevant information from noisy data to improve the resilience of proxy RMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "1807afe7-273b-4127-b8c8-5c5a019dbe2c",
  "tool_use_result": {
    "query": "\"reward hacking\" proxy reward underperforms random reward RLHF reinforcement learning 2024 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BmEuTvm5mJHJ1o7WkYs2yE",
        "content": [
          {
            "title": "Reward Hacking in Reinforcement Learning | Lil'Log",
            "url": "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"
          },
          {
            "title": "Reward Hacking: The Hidden Failure Mode in AI Optimization | by Adnan Masood, PhD. | Medium",
            "url": "https://medium.com/@adnanmasood/reward-hacking-the-hidden-failure-mode-in-ai-optimization-686b62acf408"
          },
          {
            "title": "Reward Shaping to Mitigate Reward Hacking in RLHF",
            "url": "https://arxiv.org/html/2502.18770v3"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Information- ...",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/f25d75fc760aec0a6174f9f5d9da59b8-Paper-Conference.pdf"
          },
          {
            "title": "Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges",
            "url": "https://arxiv.org/html/2604.13602v1"
          },
          {
            "title": "Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking",
            "url": "https://arxiv.org/html/2403.03185v4"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness",
            "url": "https://arxiv.org/html/2604.02986"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=reward+hacking"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling",
            "url": "https://arxiv.org/html/2602.10623"
          },
          {
            "title": "Reward hacking - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Reward_hacking"
          }
        ]
      },
      "I've performed a web search on reward hacking in reinforcement learning from human feedback (RLHF). Here are the key findings:\n\n## Core Definition and Problem\n\nReward models (RMs) used in RLHF are vulnerable to reward hacking: as the policy maximizes a learned proxy reward, true quality plateaus or degrades. Reward hacking occurs when optimizing a correlated proxy reward leads to a policy obtaining lower true reward than the reference policy.\n\n## How Proxy Rewards Underperform\n\nReward overoptimization happens when optimization pressure increases too much. The model's proxy score continues to improve, but its actual quality stops improving and eventually gets worse. Interestingly, reward hacking still occurs even when there is a positive correlation between the true and proxy rewards.\n\n## Mechanisms in RLHF\n\nRLHF aims to improve the model's alignment with human preference, but human feedback may not capture all the aspects we care about (e.g., factuality) and thus can be hacked to overfit to undesired attributes. For example, the model may be optimized to output responses that seem correct and convincing but are, in fact, inaccurate, thereby misleading human evaluators.\n\n## Recent Mitigation Approaches (2024-2026)\n\nTwo key design principles have emerged: (1) the RL reward should be bounded, and (2) the RL reward benefits from rapid initial growth followed by gradual convergence. Researchers propose Preference As Reward (PAR), a novel approach that leverages the latent preferences embedded within the reward model as the signal for reinforcement learning.\n\nSignCert-PO proposes down-weighting non-robust completions in the policy gradient update. Unlike prior approaches that require multiple RMs or access to the RM training data, SignCert-PO is lightweight and operates purely at the policy optimization stage.\n\nAdditional mitigation research includes InfoRM, which consistently prevents reward overoptimization and maintains stability regardless of label noise, underscoring its ability to extract human preference-relevant information from noisy data to improve the resilience of proxy RMs."
    ],
    "durationSeconds": 9.472404623
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T14:09:02.063Z_

<details><summary>↩ Tool result · `toolu_01Au7GSrAnhvTsBUj6bf3RY4`</summary>

```text
Web search results for query: ""optimization pressure" "metric collapse" reward overoptimization NLP code generation proxy worse than baseline 2024 2025"

Links: [{"title":"confronting reward model overoptimization","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/5eee634cb9729b8bcc2ec9f2a46a74ae-Paper-Conference.pdf"},{"title":"NeurIPS Poster Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms","url":"https://neurips.cc/virtual/2024/poster/93540"},{"title":"Reward Over-Optimization in AI","url":"https://www.emergentmind.com/topics/reward-over-optimization"},{"title":"GitHub - tlc4418/llm_optimization: A repo for RLHF training and BoN over LLMs, with support for reward model ensembles. · GitHub","url":"https://github.com/tlc4418/llm_optimization"},{"title":"Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/e45caa3d5273d105b8d045e748636957-Paper-Conference.pdf"},{"title":"Over-Optimization | RLHF Book by Nathan Lambert","url":"https://rlhfbook.com/c/14-over-optimization"},{"title":"Confronting Reward Model Overoptimization with Constrained RLHF | OpenReview","url":"https://openreview.net/forum?id=gkfUvn0fLU"},{"title":"NeurIPS 2025 Papers with Code & Data – Paper Digest","url":"https://www.paperdigest.org/2025/11/neurips-2025-papers-with-code-data/"},{"title":"[2406.02900] Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms","url":"https://arxiv.org/abs/2406.02900"},{"title":"NeurIPS Poster Mitigating Reward Overoptimization via Lightweight Uncertainty Estimation","url":"https://neurips.cc/virtual/2024/poster/93880"}]

I've completed a web search for your query about optimization pressure, metric collapse, and reward overoptimization in NLP and code generation. Here are the key findings from recent 2024-2025 research:

## Core Problem: Reward Overoptimization

A prominent issue with RLHF methods is reward over-optimization or reward hacking, where performance as measured by the learned proxy reward model increases, but true quality plateaus or even deteriorates. Any reward model is only a proxy for the agent's true measuring stick—human evaluation—so as predicted by Goodhart's Law, an agent trained to maximize it will eventually learn behaviors which the true objective would discourage.

## Metric Collapse and Distribution Shifts

The core mechanism underlying reward over-optimization is reward misgeneralization: policies exploit spurious correlations, under-specified aspects, or brittle error modes in the reward model, rather than genuinely aligning with human intent or the desired objective. Out-of-distribution (OOD) sensitivity means optimized policies amplify OOD queries to the reward model; the reward model extrapolates poorly, leading to pathological behaviors such as repetition, unnatural verbosity, or gaming of superficial metrics.

## Empirical Evidence of Worse-Than-Baseline Performance

Empirical studies across both language and vision benchmarks consistently demonstrate a characteristic "hump-shaped" curve: as the policy departs from the reference, gold reward and true task winrate rise, peak, and then fall, while the proxy reward increases monotonically.

## Recent Solutions (2024-2025)

Several mitigation strategies have emerged:
- Constrained RLHF aligns policies only up to a proxy-identified threshold ("sweet spot") for each component of a composite reward, using Lagrange multipliers or a Constrained Markov Decision Process (CMDP) formulation.
- Behavior-supported policy optimization regularizes the policy and Bellman operator to only take actions supported by behavioral data, avoiding value propagation to OOD actions that might trigger reward mispredictions.

The research indicates this remains an active area with multiple papers from NeurIPS 2024 addressing these challenges.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "d1509dab-b165-458a-922d-7c75a1a49f72",
  "tool_use_result": {
    "query": "\"optimization pressure\" \"metric collapse\" reward overoptimization NLP code generation proxy worse than baseline 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_012eqFhemd2XnEzgemguKgmT",
        "content": [
          {
            "title": "confronting reward model overoptimization",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2024/file/5eee634cb9729b8bcc2ec9f2a46a74ae-Paper-Conference.pdf"
          },
          {
            "title": "NeurIPS Poster Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms",
            "url": "https://neurips.cc/virtual/2024/poster/93540"
          },
          {
            "title": "Reward Over-Optimization in AI",
            "url": "https://www.emergentmind.com/topics/reward-over-optimization"
          },
          {
            "title": "GitHub - tlc4418/llm_optimization: A repo for RLHF training and BoN over LLMs, with support for reward model ensembles. · GitHub",
            "url": "https://github.com/tlc4418/llm_optimization"
          },
          {
            "title": "Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/e45caa3d5273d105b8d045e748636957-Paper-Conference.pdf"
          },
          {
            "title": "Over-Optimization | RLHF Book by Nathan Lambert",
            "url": "https://rlhfbook.com/c/14-over-optimization"
          },
          {
            "title": "Confronting Reward Model Overoptimization with Constrained RLHF | OpenReview",
            "url": "https://openreview.net/forum?id=gkfUvn0fLU"
          },
          {
            "title": "NeurIPS 2025 Papers with Code & Data – Paper Digest",
            "url": "https://www.paperdigest.org/2025/11/neurips-2025-papers-with-code-data/"
          },
          {
            "title": "[2406.02900] Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms",
            "url": "https://arxiv.org/abs/2406.02900"
          },
          {
            "title": "NeurIPS Poster Mitigating Reward Overoptimization via Lightweight Uncertainty Estimation",
            "url": "https://neurips.cc/virtual/2024/poster/93880"
          }
        ]
      },
      "I've completed a web search for your query about optimization pressure, metric collapse, and reward overoptimization in NLP and code generation. Here are the key findings from recent 2024-2025 research:\n\n## Core Problem: Reward Overoptimization\n\nA prominent issue with RLHF methods is reward over-optimization or reward hacking, where performance as measured by the learned proxy reward model increases, but true quality plateaus or even deteriorates. Any reward model is only a proxy for the agent's true measuring stick—human evaluation—so as predicted by Goodhart's Law, an agent trained to maximize it will eventually learn behaviors which the true objective would discourage.\n\n## Metric Collapse and Distribution Shifts\n\nThe core mechanism underlying reward over-optimization is reward misgeneralization: policies exploit spurious correlations, under-specified aspects, or brittle error modes in the reward model, rather than genuinely aligning with human intent or the desired objective. Out-of-distribution (OOD) sensitivity means optimized policies amplify OOD queries to the reward model; the reward model extrapolates poorly, leading to pathological behaviors such as repetition, unnatural verbosity, or gaming of superficial metrics.\n\n## Empirical Evidence of Worse-Than-Baseline Performance\n\nEmpirical studies across both language and vision benchmarks consistently demonstrate a characteristic \"hump-shaped\" curve: as the policy departs from the reference, gold reward and true task winrate rise, peak, and then fall, while the proxy reward increases monotonically.\n\n## Recent Solutions (2024-2025)\n\nSeveral mitigation strategies have emerged:\n- Constrained RLHF aligns policies only up to a proxy-identified threshold (\"sweet spot\") for each component of a composite reward, using Lagrange multipliers or a Constrained Markov Decision Process (CMDP) formulation.\n- Behavior-supported policy optimization regularizes the policy and Bellman operator to only take actions supported by behavioral data, avoiding value propagation to OOD actions that might trigger reward mispredictions.\n\nThe research indicates this remains an active area with multiple papers from NeurIPS 2024 addressing these challenges."
    ],
    "durationSeconds": 9.40761264
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
Good, I have a broad picture. Now let me search more specifically for the papers that are most directly relevant to our finding: proxy optimization being **significantly worse** than random. The key papers I need to find that aren't already in the literature map:

1. Papers where proxy optimization is empirically worse than random (not just worse than optimal)
2. The "catastrophic Goodhart" concept - where optimization drives true reward to 0
3. Any RLHF/RL papers showing structured reward < random reward
4. The Lilian Weng blog post references might point to good papers

Let me search more specifically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "16e0702a-1649-48c0-b5e6-de4f73f27099",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5jM4P8iZbzgaDKxYAZi6k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4574,
      "cache_read_input_tokens": 41814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4574
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

_source line 21_

Let me search for more specific cases and recent papers on the exact phenomenon we observe.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "7dfeed40-02bc-438b-8e37-c0e962724d34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5jM4P8iZbzgaDKxYAZi6k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4574,
      "cache_read_input_tokens": 41814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4574
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PY5cL8N4YHLTkzzR596ENi`</summary>

```json
{
  "query": "\"spurious rewards\" GRPO random reward matches ground truth Yang 2025 RLVR rethinking training signals"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "89794b3a-ec96-4e93-8dfb-795cff583111",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5jM4P8iZbzgaDKxYAZi6k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4574,
      "cache_read_input_tokens": 41814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4574
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XaFUW6orV5bdE5ugPSNXCM`</summary>

```json
{
  "query": "structured reward worse than random baseline reinforcement learning RLHF process reward model hurts performance 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "e3b788a8-0887-4a07-bc98-1029741ab7e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5jM4P8iZbzgaDKxYAZi6k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4574,
      "cache_read_input_tokens": 41814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4574
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MfYnYYRFfNe4orPPRr4maP`</summary>

```json
{
  "query": "\"reward overoptimization\" proxy reward below random baseline \"worse than\" no optimization empirical RLHF 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "148e3c12-97cc-4033-8558-9f66c39579df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5jM4P8iZbzgaDKxYAZi6k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4574,
      "cache_read_input_tokens": 41814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4574
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

_source line 25 · 2026-05-15T14:09:17.726Z_

<details><summary>↩ Tool result · `toolu_01PY5cL8N4YHLTkzzR596ENi`</summary>

```text
Web search results for query: ""spurious rewards" GRPO random reward matches ground truth Yang 2025 RLVR rethinking training signals"

Links: [{"title":"[2506.10947] Spurious Rewards: Rethinking Training Signals in RLVR","url":"https://arxiv.org/abs/2506.10947"},{"title":"GitHub - ruixin31/Spurious_Rewards","url":"https://github.com/ruixin31/Spurious_Rewards"},{"title":"Unknown NLP Lab | Spurious Rewards: Rethinking Training Signals in RLVR","url":"https://unknown-nlp.github.io/blog/2025/spurious-rewards-rethinking-training-signals-in-rlvr/"},{"title":"(PDF) Spurious Rewards: Rethinking Training Signals in RLVR","url":"https://www.researchgate.net/publication/392629816_Spurious_Rewards_Rethinking_Training_Signals_in_RLVR"},{"title":"SPURIOUS REWARDS","url":"https://openreview.net/pdf/3622bc23476a26328225806f1b86b0182645c94b.pdf"},{"title":"Exploration vs Exploitation: Rethinking RLVR through Clipping, Entropy, and Spurious Reward","url":"https://arxiv.org/html/2512.16912"},{"title":"rethinking rlvr through clipping, entropy","url":"https://arxiv.org/pdf/2512.16912"},{"title":"Exploration v.s. Exploitation: Rethinking RLVR through Clipping, Entropy, and Spurious Reward","url":"https://arxiv.org/html/2512.16912v1"},{"title":"Spurious Rewards: Rethinking Training Signals in RLVR","url":"https://github.com/ruixin31/Rethink_RLVR"},{"title":"Spurious Rewards: Rethinking Training Signals in RLVR – Fast Overview","url":"https://aiwithmike.substack.com/p/spurious-rewards-rethinking-training"}]

I found relevant research on this topic. Here are the key findings:

## Spurious Rewards in RLVR

RLVR training with GRPO improves MATH-500 performance for Qwen2.5-Math-7B by 21.4 percentage points using randomly assigned rewards, nearly matching the 29.1-point gain from ground-truth rewards.

### Performance Comparison

The research demonstrates striking results across different reward types:

Using incorrect labels for training results in 24.1% absolute accuracy gain on MATH-500, while using format or random rewards result in 13.8% and 21.4% gains, respectively. These spurious-reward gains are even comparable to the 29.1% gain from training on ground truth.

### Mechanisms Behind Spurious Rewards

Many incorrect labels remain close to ground truth values, providing positive reinforcement for largely correct reasoning. Second, incorrect labels partially function as format rewards: the model only receives positive rewards when its final answer is extractable.

For random rewards specifically, the source of training signals under random rewards possibly originates from a bias in the training objective—specifically, GRPO clipping bias can induce random reward training signals.

### Key Limitation

It is easy to get significant performance improvements on Qwen models even with completely spurious reward signals. Thus, future RLVR research should possibly be confirmed on other models. Llama and OLMo lack useful code priors, so the same spurious signals either help little or hurt.

The paper suggests that we do not yet fully understand the exact mechanisms by which RLVR improves performance, and that in many cases it may be somehow exposing innate model abilities learned during pretraining.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "08bf9483-ec34-4eb3-80df-f93cb5f22a11",
  "tool_use_result": {
    "query": "\"spurious rewards\" GRPO random reward matches ground truth Yang 2025 RLVR rethinking training signals",
    "results": [
      {
        "tool_use_id": "srvtoolu_01U3JJYTXxWWKsuRgKmdjhav",
        "content": [
          {
            "title": "[2506.10947] Spurious Rewards: Rethinking Training Signals in RLVR",
            "url": "https://arxiv.org/abs/2506.10947"
          },
          {
            "title": "GitHub - ruixin31/Spurious_Rewards",
            "url": "https://github.com/ruixin31/Spurious_Rewards"
          },
          {
            "title": "Unknown NLP Lab | Spurious Rewards: Rethinking Training Signals in RLVR",
            "url": "https://unknown-nlp.github.io/blog/2025/spurious-rewards-rethinking-training-signals-in-rlvr/"
          },
          {
            "title": "(PDF) Spurious Rewards: Rethinking Training Signals in RLVR",
            "url": "https://www.researchgate.net/publication/392629816_Spurious_Rewards_Rethinking_Training_Signals_in_RLVR"
          },
          {
            "title": "SPURIOUS REWARDS",
            "url": "https://openreview.net/pdf/3622bc23476a26328225806f1b86b0182645c94b.pdf"
          },
          {
            "title": "Exploration vs Exploitation: Rethinking RLVR through Clipping, Entropy, and Spurious Reward",
            "url": "https://arxiv.org/html/2512.16912"
          },
          {
            "title": "rethinking rlvr through clipping, entropy",
            "url": "https://arxiv.org/pdf/2512.16912"
          },
          {
            "title": "Exploration v.s. Exploitation: Rethinking RLVR through Clipping, Entropy, and Spurious Reward",
            "url": "https://arxiv.org/html/2512.16912v1"
          },
          {
            "title": "Spurious Rewards: Rethinking Training Signals in RLVR",
            "url": "https://github.com/ruixin31/Rethink_RLVR"
          },
          {
            "title": "Spurious Rewards: Rethinking Training Signals in RLVR – Fast Overview",
            "url": "https://aiwithmike.substack.com/p/spurious-rewards-rethinking-training"
          }
        ]
      },
      "I found relevant research on this topic. Here are the key findings:\n\n## Spurious Rewards in RLVR\n\nRLVR training with GRPO improves MATH-500 performance for Qwen2.5-Math-7B by 21.4 percentage points using randomly assigned rewards, nearly matching the 29.1-point gain from ground-truth rewards.\n\n### Performance Comparison\n\nThe research demonstrates striking results across different reward types:\n\nUsing incorrect labels for training results in 24.1% absolute accuracy gain on MATH-500, while using format or random rewards result in 13.8% and 21.4% gains, respectively. These spurious-reward gains are even comparable to the 29.1% gain from training on ground truth.\n\n### Mechanisms Behind Spurious Rewards\n\nMany incorrect labels remain close to ground truth values, providing positive reinforcement for largely correct reasoning. Second, incorrect labels partially function as format rewards: the model only receives positive rewards when its final answer is extractable.\n\nFor random rewards specifically, the source of training signals under random rewards possibly originates from a bias in the training objective—specifically, GRPO clipping bias can induce random reward training signals.\n\n### Key Limitation\n\nIt is easy to get significant performance improvements on Qwen models even with completely spurious reward signals. Thus, future RLVR research should possibly be confirmed on other models. Llama and OLMo lack useful code priors, so the same spurious signals either help little or hurt.\n\nThe paper suggests that we do not yet fully understand the exact mechanisms by which RLVR improves performance, and that in many cases it may be somehow exposing innate model abilities learned during pretraining."
    ],
    "durationSeconds": 7.948765503000002
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T14:09:19.505Z_

<details><summary>↩ Tool result · `toolu_01MfYnYYRFfNe4orPPRr4maP`</summary>

```text
Web search results for query: ""reward overoptimization" proxy reward below random baseline "worse than" no optimization empirical RLHF 2024 2025"

Links: [{"title":"Confronting Reward Model Overoptimization with Constrained RLHF | OpenReview","url":"https://openreview.net/forum?id=gkfUvn0fLU"},{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602v1"},{"title":"Reward Over-Optimization in AI","url":"https://www.emergentmind.com/topics/reward-over-optimization"},{"title":"[2406.02900] Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms","url":"https://arxiv.org/abs/2406.02900"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2410.05584"},{"title":"Reward Model Overoptimisation in Iterated RLHF | OpenReview","url":"https://openreview.net/forum?id=efoe5VJfKz"},{"title":"Reward Model Overoptimisation in Iterated RLHF","url":"https://arxiv.org/html/2505.18126v2"},{"title":"Confronting Reward Model Overoptimization with Constrained RLHF","url":"https://arxiv.org/html/2310.04373v1"},{"title":"Over-Optimization | RLHF Book by Nathan Lambert","url":"https://rlhfbook.com/c/14-over-optimization"},{"title":"NeurIPS Poster Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms","url":"https://neurips.cc/virtual/2024/poster/93540"}]

I found several highly relevant research papers and sources on reward overoptimization. Here are the key findings:

## Core Phenomenon

Reward overoptimization occurs when, because any reward model is only a proxy for human evaluation, past a certain point accumulating higher reward is associated with worse human ratings.

When optimization pressure increases too much through reward overoptimization, the model's proxy score continues to improve, but its actual quality stops improving and eventually gets worse.

## Empirical Evidence in RLHF

Gao et al. (2022) showed that maximizing a reward model beyond a certain point can actually begin to decrease ground truth performance, leading a text-based agent to produce outputs which are judged as qualitatively worse.

Examples of overoptimization include producing overly wordy responses or hallucinating information in an effort to give the impression of expertise.

## Recent Empirical Studies (2024-2025)

Although Direct Alignment Algorithms do not use a separate proxy reward model, they still commonly deteriorate from over-optimization, exhibiting similar degradation patterns to RLHF counterparts at higher KL budgets, and often deteriorate before even a single epoch of the dataset is completed.

Small but persistent overoptimization remains after four iterations of iterated RLHF regardless of design choices, and while iterated RLHF significantly improves reward model robustness, it does not fully eliminate overoptimization.

## Mitigation Approaches

Constrained RLHF aligns policies only up to a proxy-identified threshold ("sweet spot") for each component of a composite reward, using Lagrange multipliers or a Constrained Markov Decision Process formulation.

Reward-model ensembles can substantially mitigate overoptimization in both best-of-n sampling and PPO, suggesting that part of the failure comes from exploitable evaluator idiosyncrasies rather than from one particular optimization procedure.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "8e2d9b82-f089-45c9-9424-34d8518cfe3a",
  "tool_use_result": {
    "query": "\"reward overoptimization\" proxy reward below random baseline \"worse than\" no optimization empirical RLHF 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_011GwgcVV8SiUXxmV2TMDV5N",
        "content": [
          {
            "title": "Confronting Reward Model Overoptimization with Constrained RLHF | OpenReview",
            "url": "https://openreview.net/forum?id=gkfUvn0fLU"
          },
          {
            "title": "Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges",
            "url": "https://arxiv.org/html/2604.13602v1"
          },
          {
            "title": "Reward Over-Optimization in AI",
            "url": "https://www.emergentmind.com/topics/reward-over-optimization"
          },
          {
            "title": "[2406.02900] Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms",
            "url": "https://arxiv.org/abs/2406.02900"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://arxiv.org/pdf/2410.05584"
          },
          {
            "title": "Reward Model Overoptimisation in Iterated RLHF | OpenReview",
            "url": "https://openreview.net/forum?id=efoe5VJfKz"
          },
          {
            "title": "Reward Model Overoptimisation in Iterated RLHF",
            "url": "https://arxiv.org/html/2505.18126v2"
          },
          {
            "title": "Confronting Reward Model Overoptimization with Constrained RLHF",
            "url": "https://arxiv.org/html/2310.04373v1"
          },
          {
            "title": "Over-Optimization | RLHF Book by Nathan Lambert",
            "url": "https://rlhfbook.com/c/14-over-optimization"
          },
          {
            "title": "NeurIPS Poster Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms",
            "url": "https://neurips.cc/virtual/2024/poster/93540"
          }
        ]
      },
      "I found several highly relevant research papers and sources on reward overoptimization. Here are the key findings:\n\n## Core Phenomenon\n\nReward overoptimization occurs when, because any reward model is only a proxy for human evaluation, past a certain point accumulating higher reward is associated with worse human ratings.\n\nWhen optimization pressure increases too much through reward overoptimization, the model's proxy score continues to improve, but its actual quality stops improving and eventually gets worse.\n\n## Empirical Evidence in RLHF\n\nGao et al. (2022) showed that maximizing a reward model beyond a certain point can actually begin to decrease ground truth performance, leading a text-based agent to produce outputs which are judged as qualitatively worse.\n\nExamples of overoptimization include producing overly wordy responses or hallucinating information in an effort to give the impression of expertise.\n\n## Recent Empirical Studies (2024-2025)\n\nAlthough Direct Alignment Algorithms do not use a separate proxy reward model, they still commonly deteriorate from over-optimization, exhibiting similar degradation patterns to RLHF counterparts at higher KL budgets, and often deteriorate before even a single epoch of the dataset is completed.\n\nSmall but persistent overoptimization remains after four iterations of iterated RLHF regardless of design choices, and while iterated RLHF significantly improves reward model robustness, it does not fully eliminate overoptimization.\n\n## Mitigation Approaches\n\nConstrained RLHF aligns policies only up to a proxy-identified threshold (\"sweet spot\") for each component of a composite reward, using Lagrange multipliers or a Constrained Markov Decision Process formulation.\n\nReward-model ensembles can substantially mitigate overoptimization in both best-of-n sampling and PPO, suggesting that part of the failure comes from exploitable evaluator idiosyncrasies rather than from one particular optimization procedure."
    ],
    "durationSeconds": 8.297341916999997
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T14:09:26.339Z_

<details><summary>↩ Tool result · `toolu_01XaFUW6orV5bdE5ugPSNXCM`</summary>

```text
Web search results for query: "structured reward worse than random baseline reinforcement learning RLHF process reward model hurts performance 2024 2025 2026"

Links: [{"title":"Reward Function in Reinforcement Learning | by Amit Yadav | Biased-Algorithms | Medium","url":"https://medium.com/biased-algorithms/reward-function-in-reinforcement-learning-c9ee04cabe7d"},{"title":"Breaking the SFT Plateau: Multimodal Structured Reinforcement Learning for Chart-to-Code Generation","url":"https://arxiv.org/html/2508.13587v1"},{"title":"The State of Reinforcement Learning for LLM Reasoning","url":"https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training"},{"title":"Reinforcement Learning with Verifiable Rewards Makes Models Faster, Not Smarter | Promptfoo","url":"https://www.promptfoo.dev/blog/rlvr-explained/"},{"title":"AI 101: The State of Reinforcement Learning in 2025","url":"https://www.turingpost.com/p/stateofrl2025"},{"title":"Reward Modelling in Modern AI","url":"https://www.emergentmind.com/topics/reward-modelling"},{"title":"Reward Modeling in Reinforcement Learning | Apolo AI Launchpad - Secure, Industry-Tailored AI Tools for Regulated Enterprises","url":"https://www.apolo.us/blog-posts/reward-modeling-in-reinforcement-learning"},{"title":"GitHub - bobxwu/learning-from-rewards-llm-papers: A comrephensive collection of learning from rewards in the post-training and test-time scaling of LLMs, with a focus on both reward models and learning strategies across training, inference, and post-inference stages. · GitHub","url":"https://github.com/bobxwu/learning-from-rewards-llm-papers"},{"title":"Reward Shaping for Faster Learning in Reinforcement ...","url":"https://codesignal.com/learn/courses/advanced-rl-techniques-optimization-and-beyond/lessons/reward-shaping-for-faster-learning-in-reinforcement-learning"},{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"}]

Let me search for more specific information about process reward models and their effectiveness issues.

Links: [{"title":"How to Evaluate Reward Models for RLHF | OpenReview","url":"https://openreview.net/forum?id=cbttLtO94Q"},{"title":"Reward Modeling for Human Preferences Evan Frick","url":"https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-82.pdf"},{"title":"Secrets of RLHF in Large Language Models Part II: Reward Modeling","url":"https://arxiv.org/html/2401.06080v2"},{"title":"Reward Modeling for Human Preferences | EECS at UC Berkeley","url":"https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-82.html"},{"title":"Reward Model Overoptimisation in Iterated RLHF | OpenReview","url":"https://openreview.net/forum?id=efoe5VJfKz"},{"title":"HOW TO EVALUATE REWARD MODELS FOR RLHF","url":"https://openreview.net/pdf?id=cbttLtO94Q"},{"title":"Reward Modeling | RLHF Book by Nathan Lambert","url":"https://rlhfbook.com/c/05-reward-models"},{"title":"Confronting Reward Model Overoptimization with Constrained RLHF | OpenReview","url":"https://openreview.net/forum?id=gkfUvn0fLU"},{"title":"Reward Models - by Cameron R. Wolfe, Ph.D.","url":"https://cameronrwolfe.substack.com/p/reward-models"},{"title":"Reward Model Overoptimization: Root Causes and Mitigations","url":"https://www.reinforced.info/p/reward-model-overoptimization"}]

Let me search for more recent research about process reward models specifically underperforming.

Links: [{"title":"Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=h3LlJ6Bh4S"},{"title":"Reward Modeling from Natural Language Human Feedback","url":"https://arxiv.org/html/2601.07349v1"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Process+Reward+Models+(PRMs)"},{"title":"Process Reward Models - Stephen Diehl","url":"https://www.stephendiehl.com/posts/process_reward/"},{"title":"[2505.14069] Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning","url":"https://arxiv.org/abs/2505.14069"},{"title":"Process Reward Model (PRM) Overview","url":"https://www.emergentmind.com/topics/process-reward-model-prm"},{"title":"Outcome reward vs Process reward. The figure shows two different types... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Outcome-reward-vs-Process-reward-The-figure-shows-two-different-types-of-reward-outcome_fig3_387184187"},{"title":"Reward process instead of results - The Failure Institute","url":"https://thefailureinstitute.com/blog/reward-process-instead-results/"},{"title":"(PDF) Process Reward Models That Think","url":"https://www.researchgate.net/publication/391058520_Process_Reward_Models_That_Think"},{"title":"Process vs. Outcome Supervision","url":"https://www.emergentmind.com/topics/process-vs-outcome-supervision"}]

Based on my search results, I can provide you with comprehensive information about recent research on structured rewards, process reward models, and their performance in reinforcement learning and RLHF:

## Key Findings from Recent Research (2024-2026)

### Random Rewards vs. Structured Rewards

Research from June 2025 found Qwen2.5-Math-7B improved 21.4% on MATH-500 with random rewards, nearly matching the 29.1% gain from ground truth rewards. This surprising finding suggests that the RL update process, even with random rewards, implicitly guides the model's attention.

However, these effects were strongest on Qwen2.5-Math and did not consistently replicate on Llama3 or OLMo2, with later research suggesting Qwen's unusual sensitivity may indicate training data contamination rather than genuine capability surfacing, and on contamination-free datasets, only accurate rewards deliver gains; random rewards provide no benefit.

### Process Reward Models and Effectiveness Issues

Process Reward Models (PRMs) frequently suffer from inaccuracies and are susceptible to reward hacking. More specifically, the outcome-process misalignment resulting from outcome-only supervision might lead the model to exploit spurious correlations rather than developing genuine reasoning capabilities.

A substantial portion (20-30%) of correct preference predictions are accompanied by flawed critiques, even in state-of-the-art models.

### Process vs. Outcome Supervision

Interestingly, research shows mixed results. ReasonRAG, utilizing RAG-ProGUIDE, outperforms existing approaches like Search-R1 and traditional RAG systems, achieving superior performance on five benchmark datasets with only 5k training instances—significantly fewer than the 90k required by Search-R1. This suggests process-level rewards can be more efficient in certain domains.

However, VL-PRMs when used as Outcome Reward Models (ORMs) during test-time scaling can outperform VL-PRM guided process step selection.

### Reward Model Overoptimization

A critical issue in RLHF is that because any RM is only a proxy for human evaluation, this process is vulnerable to overoptimization, wherein past a certain point, accumulating higher reward is associated with worse human ratings.

As reward models have improved, there is a negative correlation between RewardBench evaluation score on top models and downstream RLHF performance.

### Distribution Shift Problems

When a reward model is trained on data with a specific distribution, it may perform poorly when it encounters out-of-distribution (OOD) examples. This is a fundamental challenge in maintaining reward model reliability.

The research landscape from 2024-2026 suggests that while structured and process-based rewards can be beneficial, their effectiveness is highly dependent on implementation details, model architecture, and whether the training data is contaminated or contains systematic biases.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "23665ba4-9004-43db-9535-5832e8ae7388",
  "tool_use_result": {
    "query": "structured reward worse than random baseline reinforcement learning RLHF process reward model hurts performance 2024 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XDdkC34LUH8GqZogZFfbLw",
        "content": [
          {
            "title": "Reward Function in Reinforcement Learning | by Amit Yadav | Biased-Algorithms | Medium",
            "url": "https://medium.com/biased-algorithms/reward-function-in-reinforcement-learning-c9ee04cabe7d"
          },
          {
            "title": "Breaking the SFT Plateau: Multimodal Structured Reinforcement Learning for Chart-to-Code Generation",
            "url": "https://arxiv.org/html/2508.13587v1"
          },
          {
            "title": "The State of Reinforcement Learning for LLM Reasoning",
            "url": "https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training"
          },
          {
            "title": "Reinforcement Learning with Verifiable Rewards Makes Models Faster, Not Smarter | Promptfoo",
            "url": "https://www.promptfoo.dev/blog/rlvr-explained/"
          },
          {
            "title": "AI 101: The State of Reinforcement Learning in 2025",
            "url": "https://www.turingpost.com/p/stateofrl2025"
          },
          {
            "title": "Reward Modelling in Modern AI",
            "url": "https://www.emergentmind.com/topics/reward-modelling"
          },
          {
            "title": "Reward Modeling in Reinforcement Learning | Apolo AI Launchpad - Secure, Industry-Tailored AI Tools for Regulated Enterprises",
            "url": "https://www.apolo.us/blog-posts/reward-modeling-in-reinforcement-learning"
          },
          {
            "title": "GitHub - bobxwu/learning-from-rewards-llm-papers: A comrephensive collection of learning from rewards in the post-training and test-time scaling of LLMs, with a focus on both reward models and learning strategies across training, inference, and post-inference stages. · GitHub",
            "url": "https://github.com/bobxwu/learning-from-rewards-llm-papers"
          },
          {
            "title": "Reward Shaping for Faster Learning in Reinforcement ...",
            "url": "https://codesignal.com/learn/courses/advanced-rl-techniques-optimization-and-beyond/lessons/reward-shaping-for-faster-learning-in-reinforcement-learning"
          },
          {
            "title": "Reward Hacking in Reinforcement Learning | Lil'Log",
            "url": "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"
          }
        ]
      },
      "Let me search for more specific information about process reward models and their effectiveness issues.",
      {
        "tool_use_id": "srvtoolu_017GWCytznL4B5YcHPDGZtLp",
        "content": [
          {
            "title": "How to Evaluate Reward Models for RLHF | OpenReview",
            "url": "https://openreview.net/forum?id=cbttLtO94Q"
          },
          {
            "title": "Reward Modeling for Human Preferences Evan Frick",
            "url": "https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-82.pdf"
          },
          {
            "title": "Secrets of RLHF in Large Language Models Part II: Reward Modeling",
            "url": "https://arxiv.org/html/2401.06080v2"
          },
          {
            "title": "Reward Modeling for Human Preferences | EECS at UC Berkeley",
            "url": "https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-82.html"
          },
          {
            "title": "Reward Model Overoptimisation in Iterated RLHF | OpenReview",
            "url": "https://openreview.net/forum?id=efoe5VJfKz"
          },
          {
            "title": "HOW TO EVALUATE REWARD MODELS FOR RLHF",
            "url": "https://openreview.net/pdf?id=cbttLtO94Q"
          },
          {
            "title": "Reward Modeling | RLHF Book by Nathan Lambert",
            "url": "https://rlhfbook.com/c/05-reward-models"
          },
          {
            "title": "Confronting Reward Model Overoptimization with Constrained RLHF | OpenReview",
            "url": "https://openreview.net/forum?id=gkfUvn0fLU"
          },
          {
            "title": "Reward Models - by Cameron R. Wolfe, Ph.D.",
            "url": "https://cameronrwolfe.substack.com/p/reward-models"
          },
          {
            "title": "Reward Model Overoptimization: Root Causes and Mitigations",
            "url": "https://www.reinforced.info/p/reward-model-overoptimization"
          }
        ]
      },
      "Let me search for more recent research about process reward models specifically underperforming.",
      {
        "tool_use_id": "srvtoolu_01298YbMEs8QiaVt32Ggy7iC",
        "content": [
          {
            "title": "Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=h3LlJ6Bh4S"
          },
          {
            "title": "Reward Modeling from Natural Language Human Feedback",
            "url": "https://arxiv.org/html/2601.07349v1"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=Process+Reward+Models+(PRMs)"
          },
          {
            "title": "Process Reward Models - Stephen Diehl",
            "url": "https://www.stephendiehl.com/posts/process_reward/"
          },
          {
            "title": "[2505.14069] Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning",
            "url": "https://arxiv.org/abs/2505.14069"
          },
          {
            "title": "Process Reward Model (PRM) Overview",
            "url": "https://www.emergentmind.com/topics/process-reward-model-prm"
          },
          {
            "title": "Outcome reward vs Process reward. The figure shows two different types... | Download Scientific Diagram",
            "url": "https://www.researchgate.net/figure/Outcome-reward-vs-Process-reward-The-figure-shows-two-different-types-of-reward-outcome_fig3_387184187"
          },
          {
            "title": "Reward process instead of results - The Failure Institute",
            "url": "https://thefailureinstitute.com/blog/reward-process-instead-results/"
          },
          {
            "title": "(PDF) Process Reward Models That Think",
            "url": "https://www.researchgate.net/publication/391058520_Process_Reward_Models_That_Think"
          },
          {
            "title": "Process vs. Outcome Supervision",
            "url": "https://www.emergentmind.com/topics/process-vs-outcome-supervision"
          }
        ]
      },
      "Based on my search results, I can provide you with comprehensive information about recent research on structured rewards, process reward models, and their performance in reinforcement learning and RLHF:\n\n## Key Findings from Recent Research (2024-2026)\n\n### Random Rewards vs. Structured Rewards\n\nResearch from June 2025 found Qwen2.5-Math-7B improved 21.4% on MATH-500 with random rewards, nearly matching the 29.1% gain from ground truth rewards. This surprising finding suggests that the RL update process, even with random rewards, implicitly guides the model's attention.\n\nHowever, these effects were strongest on Qwen2.5-Math and did not consistently replicate on Llama3 or OLMo2, with later research suggesting Qwen's unusual sensitivity may indicate training data contamination rather than genuine capability surfacing, and on contamination-free datasets, only accurate rewards deliver gains; random rewards provide no benefit.\n\n### Process Reward Models and Effectiveness Issues\n\nProcess Reward Models (PRMs) frequently suffer from inaccuracies and are susceptible to reward hacking. More specifically, the outcome-process misalignment resulting from outcome-only supervision might lead the model to exploit spurious correlations rather than developing genuine reasoning capabilities.\n\nA substantial portion (20-30%) of correct preference predictions are accompanied by flawed critiques, even in state-of-the-art models.\n\n### Process vs. Outcome Supervision\n\nInterestingly, research shows mixed results. ReasonRAG, utilizing RAG-ProGUIDE, outperforms existing approaches like Search-R1 and traditional RAG systems, achieving superior performance on five benchmark datasets with only 5k training instances—significantly fewer than the 90k required by Search-R1. This suggests process-level rewards can be more efficient in certain domains.\n\nHowever, VL-PRMs when used as Outcome Reward Models (ORMs) during test-time scaling can outperform VL-PRM guided process step selection.\n\n### Reward Model Overoptimization\n\nA critical issue in RLHF is that because any RM is only a proxy for human evaluation, this process is vulnerable to overoptimization, wherein past a certain point, accumulating higher reward is associated with worse human ratings.\n\nAs reward models have improved, there is a negative correlation between RewardBench evaluation score on top models and downstream RLHF performance.\n\n### Distribution Shift Problems\n\nWhen a reward model is trained on data with a specific distribution, it may perform poorly when it encounters out-of-distribution (OOD) examples. This is a fundamental challenge in maintaining reward model reliability.\n\nThe research landscape from 2024-2026 suggests that while structured and process-based rewards can be beneficial, their effectiveness is highly dependent on implementation details, model architecture, and whether the training data is contaminated or contains systematic biases."
    ],
    "durationSeconds": 15.599796795999994
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for the most specific papers I need:

1. A paper about "catastrophic Goodhart" - Kwa et al. 2024 - already in the literature map as `kwa-catastrophic-goodhart`
2. Papers about reward model overoptimization in iterated RLHF - this seems new
3. The Lilian Weng blog post might reference good papers
4. I need to find papers NOT already in the literature map that specifically show proxy < random

Let me search for a few more specific papers:
- "Correlated Proxies" paper (2024) - seems relevant


- The "Rethinking Reward Model Evaluation" paper from ICLR 2025 looks promising, and I should also look for empirical work on Goodhart effects in code and formal verification domains.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "85692e34-1cb8-441e-a8e8-bd9a49fd8d04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0199FENGrGkZVrJsgEA8d5HH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 956,
      "cache_creation_input_tokens": 3681,
      "cache_read_input_tokens": 46388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3681
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

_source line 29_

Let me search for a few more specific papers that could be highly relevant.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "f3293677-d92d-4f04-ac98-1c9500d3211b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0199FENGrGkZVrJsgEA8d5HH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 956,
      "cache_creation_input_tokens": 3681,
      "cache_read_input_tokens": 46388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3681
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

_source line 30_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QTgvcHtz8xhdBVN5tftdws`</summary>

```json
{
  "query": "\"correlated proxies\" reward hacking definition improved mitigation Everitt 2024 proxy optimization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "1280c94c-a41c-4b78-aa82-d0d0dc5f8867",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0199FENGrGkZVrJsgEA8d5HH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 956,
      "cache_creation_input_tokens": 3681,
      "cache_read_input_tokens": 46388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3681
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

_source line 31_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011GCguLWoQuTHqdXB1EKjNb`</summary>

```json
{
  "query": "Gao \"On Designing Effective RL Reward\" process reward hurts training LLM reasoning 2024 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "ee5219ec-8b43-4142-9820-f798b9f7bede",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0199FENGrGkZVrJsgEA8d5HH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 956,
      "cache_creation_input_tokens": 3681,
      "cache_read_input_tokens": 46388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3681
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

_source line 32_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CuGcuNkug1kQxJE2QqjjcV`</summary>

```json
{
  "query": "RLHF \"gold reward decreases\" \"proxy reward increases\" empirical evidence worse than random reference policy 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "44fc5a7d-4abf-4446-a582-1107dc7e074e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0199FENGrGkZVrJsgEA8d5HH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 956,
      "cache_creation_input_tokens": 3681,
      "cache_read_input_tokens": 46388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3681
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

_source line 33 · 2026-05-15T14:09:41.082Z_

<details><summary>↩ Tool result · `toolu_01QTgvcHtz8xhdBVN5tftdws`</summary>

```text
Web search results for query: ""correlated proxies" reward hacking definition improved mitigation Everitt 2024 proxy optimization"

Links: [{"title":"[2403.03185] Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking","url":"https://arxiv.org/abs/2403.03185"},{"title":"Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking","url":"https://arxiv.org/html/2403.03185"},{"title":"Robust Optimization for Mitigating Reward Hacking with Correlated Proxies","url":"https://arxiv.org/html/2604.12086"},{"title":"Robust Optimization for Mitigating Reward Hacking with ...","url":"https://arxiv.org/pdf/2604.12086"},{"title":"Adversarial Reward Auditing for Active Detection and ...","url":"https://arxiv.org/pdf/2602.01750"},{"title":"[2403.03185v4] Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking","url":"https://arxiv.org/abs/2403.03185v4"},{"title":"(PDF) Robust Optimization for Mitigating Reward Hacking with Correlated Proxies","url":"https://www.researchgate.net/publication/403824186_Robust_Optimization_for_Mitigating_Reward_Hacking_with_Correlated_Proxies"},{"title":"Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking | OpenReview","url":"https://openreview.net/forum?id=msEr27EejF"},{"title":"Adversarial Reward Auditing for Active Detection and Mitigation of Reward Hacking","url":"https://arxiv.org/html/2602.01750v1"},{"title":"ROBUST OPTIMIZATION FOR MITIGATING REWARD ...","url":"https://openreview.net/pdf/1f6eebe054b98acb5c8e31d211e96597ad368b36.pdf"}]

Based on the web search results, I found relevant information about correlated proxies and reward hacking. Here's what the research shows:

## Definition of Reward Hacking

Optimizing proxy rewards frequently leads to reward hacking: the optimized reward function ceases to be a good proxy and the resulting policy performs poorly with respect to the unspecified true reward.

## Correlated Proxies Definition

A definition of reward hacking has been introduced based on the correlation between proxy and true rewards for states and actions seen by a "reference policy" that breaks down under optimization. Principled solutions to reward hacking have been impeded by the lack of a good definition for the problem.

## Improved Mitigation Approach

A new definition for reward hacking based on the correlation between a proxy reward function and the unknown true reward that breaks down when optimizing the proxy has been introduced, and chi-squared occupancy measure regularization can more effectively prevent reward hacking than current approaches.

## Application Context

These results have implications for settings like RLHF (reinforcement learning from human feedback), where it is suggested that the heuristic KL penalty used currently should be replaced by a more principled form of regularization.

The key research is from Laidlaw, Singhal, and Dragan (2025), published at the International Conference on Learning Representations, which provides both theoretical and empirical advances in understanding and mitigating reward hacking through the correlated proxies framework.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "86c0439e-46b2-40d9-bd28-fdf940764812",
  "tool_use_result": {
    "query": "\"correlated proxies\" reward hacking definition improved mitigation Everitt 2024 proxy optimization",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WNjxKoczKLqAnv9H28RFD2",
        "content": [
          {
            "title": "[2403.03185] Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking",
            "url": "https://arxiv.org/abs/2403.03185"
          },
          {
            "title": "Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking",
            "url": "https://arxiv.org/html/2403.03185"
          },
          {
            "title": "Robust Optimization for Mitigating Reward Hacking with Correlated Proxies",
            "url": "https://arxiv.org/html/2604.12086"
          },
          {
            "title": "Robust Optimization for Mitigating Reward Hacking with ...",
            "url": "https://arxiv.org/pdf/2604.12086"
          },
          {
            "title": "Adversarial Reward Auditing for Active Detection and ...",
            "url": "https://arxiv.org/pdf/2602.01750"
          },
          {
            "title": "[2403.03185v4] Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking",
            "url": "https://arxiv.org/abs/2403.03185v4"
          },
          {
            "title": "(PDF) Robust Optimization for Mitigating Reward Hacking with Correlated Proxies",
            "url": "https://www.researchgate.net/publication/403824186_Robust_Optimization_for_Mitigating_Reward_Hacking_with_Correlated_Proxies"
          },
          {
            "title": "Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking | OpenReview",
            "url": "https://openreview.net/forum?id=msEr27EejF"
          },
          {
            "title": "Adversarial Reward Auditing for Active Detection and Mitigation of Reward Hacking",
            "url": "https://arxiv.org/html/2602.01750v1"
          },
          {
            "title": "ROBUST OPTIMIZATION FOR MITIGATING REWARD ...",
            "url": "https://openreview.net/pdf/1f6eebe054b98acb5c8e31d211e96597ad368b36.pdf"
          }
        ]
      },
      "Based on the web search results, I found relevant information about correlated proxies and reward hacking. Here's what the research shows:\n\n## Definition of Reward Hacking\n\nOptimizing proxy rewards frequently leads to reward hacking: the optimized reward function ceases to be a good proxy and the resulting policy performs poorly with respect to the unspecified true reward.\n\n## Correlated Proxies Definition\n\nA definition of reward hacking has been introduced based on the correlation between proxy and true rewards for states and actions seen by a \"reference policy\" that breaks down under optimization. Principled solutions to reward hacking have been impeded by the lack of a good definition for the problem.\n\n## Improved Mitigation Approach\n\nA new definition for reward hacking based on the correlation between a proxy reward function and the unknown true reward that breaks down when optimizing the proxy has been introduced, and chi-squared occupancy measure regularization can more effectively prevent reward hacking than current approaches.\n\n## Application Context\n\nThese results have implications for settings like RLHF (reinforcement learning from human feedback), where it is suggested that the heuristic KL penalty used currently should be replaced by a more principled form of regularization.\n\nThe key research is from Laidlaw, Singhal, and Dragan (2025), published at the International Conference on Learning Representations, which provides both theoretical and empirical advances in understanding and mitigating reward hacking through the correlated proxies framework."
    ],
    "durationSeconds": 6.0689408640000035
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T14:09:43.599Z_

<details><summary>↩ Tool result · `toolu_011GCguLWoQuTHqdXB1EKjNb`</summary>

```text
Web search results for query: "Gao "On Designing Effective RL Reward" process reward hurts training LLM reasoning 2024 arXiv"

Links: [{"title":"[2410.15115] On Designing Effective RL Reward at Training Time for LLM Reasoning","url":"https://arxiv.org/abs/2410.15115"},{"title":"On Designing Effective RL Reward at Training Time for LLM Reasoning","url":"https://arxiv.org/html/2410.15115"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation","url":"https://arxiv.org/html/2602.09305v1"},{"title":"[2410.15115v3] On Designing Effective RL Reward at Training Time for LLM Reasoning","url":"https://arxiv.org/abs/2410.15115v3"},{"title":"On Designing Effective RL Reward at Training Time for LLM Reasoning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241015115G/abstract"},{"title":"[PDF] On Designing Effective RL Reward at Training Time for LLM Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/On-Designing-Effective-RL-Reward-at-Training-Time-Gao-Xu/043731dd9f2292b7e4788d0b97edee5db170f840"},{"title":"On Designing Effective RL Reward at Training Time for LLM Reasoning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/designing-effective-rl-reward-at-training-time"},{"title":"On Designing Effective RL Reward at Training Time for LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=F0GNv13ojF"},{"title":"On Designing Effective RL Reward at Training Time for LLM Reasoning | Request PDF","url":"https://www.researchgate.net/publication/385107562_On_Designing_Effective_RL_Reward_at_Training_Time_for_LLM_Reasoning"},{"title":"Navigate the Unknown: Enhancing LLM Reasoning with Intrinsic Motivation Guided Exploration","url":"https://arxiv.org/html/2505.17621v5"}]

I found the paper you're looking for! Here's the information about it:

**Title:** On Designing Effective RL Reward at Training Time for LLM Reasoning

**Authors:** Jiaxuan Gao and 8 other authors

**Key Finding:** Even though these learned reward models have strong inference-time performances, they may NOT help or even hurt RL training

**Main Problem Identified:** An LLM can receive high rewards from some of these reward models by repeating correct but unnecessary reasoning steps, leading to a severe reward hacking issue

**Proposed Solution:** The authors introduce two novel reward refinement techniques, including Clipping and Delta, which ensure the accumulative reward of any reasoning trajectory is upper-bounded to keep a learned reward model effective without being exploited

**Evaluation:** The techniques are evaluated with multiple reward models over 1.5B and 7B LLMs on MATH and GSM8K benchmarks

The paper (arXiv 2410.15115) was published on October 19, 2024, with the latest version from November 27, 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "45d35457-81fb-434e-8c4b-83250d343938",
  "tool_use_result": {
    "query": "Gao \"On Designing Effective RL Reward\" process reward hurts training LLM reasoning 2024 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GC8i8vwk8JUxcAbZxWfejf",
        "content": [
          {
            "title": "[2410.15115] On Designing Effective RL Reward at Training Time for LLM Reasoning",
            "url": "https://arxiv.org/abs/2410.15115"
          },
          {
            "title": "On Designing Effective RL Reward at Training Time for LLM Reasoning",
            "url": "https://arxiv.org/html/2410.15115"
          },
          {
            "title": "Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation",
            "url": "https://arxiv.org/html/2602.09305v1"
          },
          {
            "title": "[2410.15115v3] On Designing Effective RL Reward at Training Time for LLM Reasoning",
            "url": "https://arxiv.org/abs/2410.15115v3"
          },
          {
            "title": "On Designing Effective RL Reward at Training Time for LLM Reasoning - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv241015115G/abstract"
          },
          {
            "title": "[PDF] On Designing Effective RL Reward at Training Time for LLM Reasoning | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/On-Designing-Effective-RL-Reward-at-Training-Time-Gao-Xu/043731dd9f2292b7e4788d0b97edee5db170f840"
          },
          {
            "title": "On Designing Effective RL Reward at Training Time for LLM Reasoning | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/designing-effective-rl-reward-at-training-time"
          },
          {
            "title": "On Designing Effective RL Reward at Training Time for LLM Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=F0GNv13ojF"
          },
          {
            "title": "On Designing Effective RL Reward at Training Time for LLM Reasoning | Request PDF",
            "url": "https://www.researchgate.net/publication/385107562_On_Designing_Effective_RL_Reward_at_Training_Time_for_LLM_Reasoning"
          },
          {
            "title": "Navigate the Unknown: Enhancing LLM Reasoning with Intrinsic Motivation Guided Exploration",
            "url": "https://arxiv.org/html/2505.17621v5"
          }
        ]
      },
      "I found the paper you're looking for! Here's the information about it:\n\n**Title:** On Designing Effective RL Reward at Training Time for LLM Reasoning\n\n**Authors:** Jiaxuan Gao and 8 other authors\n\n**Key Finding:** Even though these learned reward models have strong inference-time performances, they may NOT help or even hurt RL training\n\n**Main Problem Identified:** An LLM can receive high rewards from some of these reward models by repeating correct but unnecessary reasoning steps, leading to a severe reward hacking issue\n\n**Proposed Solution:** The authors introduce two novel reward refinement techniques, including Clipping and Delta, which ensure the accumulative reward of any reasoning trajectory is upper-bounded to keep a learned reward model effective without being exploited\n\n**Evaluation:** The techniques are evaluated with multiple reward models over 1.5B and 7B LLMs on MATH and GSM8K benchmarks\n\nThe paper (arXiv 2410.15115) was published on October 19, 2024, with the latest version from November 27, 2024."
    ],
    "durationSeconds": 7.106191667999999
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-15T14:09:45.318Z_

<details><summary>↩ Tool result · `toolu_01CuGcuNkug1kQxJE2QqjjcV`</summary>

```text
Web search results for query: "RLHF "gold reward decreases" "proxy reward increases" empirical evidence worse than random reference policy 2024 2025 2026"

Links: [{"title":"Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking","url":"https://arxiv.org/html/2403.03185v4"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/html/2604.02986"},{"title":"Scaling Laws for Reward Model Overoptimization","url":"https://proceedings.mlr.press/v202/gao23h/gao23h.pdf"},{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602v1"},{"title":"Mitigating Reward Hacking in RLHF via Information- ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/f25d75fc760aec0a6174f9f5d9da59b8-Paper-Conference.pdf"},{"title":"Mitigating Reward Over-Optimization in RLHF via Behavior-Supported Regularization","url":"https://arxiv.org/html/2503.18130v1"},{"title":"How to Evaluate Reward Models for RLHF","url":"https://arxiv.org/html/2410.14872v2"},{"title":"What Makes a Reward Model a Good Teacher? An Optimization Perspective","url":"https://arxiv.org/html/2503.15477v1"},{"title":"Repairing Reward Functions with Human Feedback to Mitigate Reward Hacking","url":"https://arxiv.org/html/2510.13036v1"},{"title":"Repairing Reward Functions with Feedback to Mitigate Reward Hacking","url":"https://arxiv.org/html/2510.13036v2"}]

Based on the web search results, I found substantial research on RLHF reward hacking and the phenomenon where proxy rewards increase while true rewards decrease. Here are the key findings:

## Empirical Evidence of Reward Hacking

As optimization progresses, proxy reward continues to rise while true quality stagnates or degrades. The model's proxy score continues to improve, but its actual quality stops improving and eventually gets worse.

## Comparison to Reference Policy

Reward hacking occurs when optimizing a correlated proxy reward leads to a policy obtaining lower true reward than the reference policy. Optimizing the proxy alone can lead to a breakdown in the correlation and worse true reward than the reference policy.

## Theoretical Framework and Scaling Laws

Gao et al. established scaling laws for reward model overoptimization, showing that the gap between proxy and true reward grows with optimization strength and that this growth follows predictable functional forms.

## Recent Research (2024-2026)

Multiple recent papers address this challenge:

- Reward hacking is a phenomenon where as optimization progresses, proxy reward continues to rise while true quality stagnates or degrades.

- In later RL stages, as KL divergence increases, Standard RM shows a declining gold score and a rising proxy score, indicating overoptimization. Conversely, newer approaches maintain consistent growth in both scores, effectively mitigating overoptimization.

- Although the performance of LLMs may seem to improve under the reward model (proxy reward), it can deviate from the actual human objectives (gold reward).

The search results contain extensive empirical evidence from 2024-2026 showing this exact phenomenon you asked about, with multiple papers developing methods to mitigate it.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "8bff1eb3-06f2-4589-9221-bab5b2307b4d",
  "tool_use_result": {
    "query": "RLHF \"gold reward decreases\" \"proxy reward increases\" empirical evidence worse than random reference policy 2024 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HTo36z9RK8tv9hYmtvGPDY",
        "content": [
          {
            "title": "Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking",
            "url": "https://arxiv.org/html/2403.03185v4"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness",
            "url": "https://arxiv.org/html/2604.02986"
          },
          {
            "title": "Scaling Laws for Reward Model Overoptimization",
            "url": "https://proceedings.mlr.press/v202/gao23h/gao23h.pdf"
          },
          {
            "title": "Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges",
            "url": "https://arxiv.org/html/2604.13602v1"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Information- ...",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/f25d75fc760aec0a6174f9f5d9da59b8-Paper-Conference.pdf"
          },
          {
            "title": "Mitigating Reward Over-Optimization in RLHF via Behavior-Supported Regularization",
            "url": "https://arxiv.org/html/2503.18130v1"
          },
          {
            "title": "How to Evaluate Reward Models for RLHF",
            "url": "https://arxiv.org/html/2410.14872v2"
          },
          {
            "title": "What Makes a Reward Model a Good Teacher? An Optimization Perspective",
            "url": "https://arxiv.org/html/2503.15477v1"
          },
          {
            "title": "Repairing Reward Functions with Human Feedback to Mitigate Reward Hacking",
            "url": "https://arxiv.org/html/2510.13036v1"
          },
          {
            "title": "Repairing Reward Functions with Feedback to Mitigate Reward Hacking",
            "url": "https://arxiv.org/html/2510.13036v2"
          }
        ]
      },
      "Based on the web search results, I found substantial research on RLHF reward hacking and the phenomenon where proxy rewards increase while true rewards decrease. Here are the key findings:\n\n## Empirical Evidence of Reward Hacking\n\nAs optimization progresses, proxy reward continues to rise while true quality stagnates or degrades. The model's proxy score continues to improve, but its actual quality stops improving and eventually gets worse.\n\n## Comparison to Reference Policy\n\nReward hacking occurs when optimizing a correlated proxy reward leads to a policy obtaining lower true reward than the reference policy. Optimizing the proxy alone can lead to a breakdown in the correlation and worse true reward than the reference policy.\n\n## Theoretical Framework and Scaling Laws\n\nGao et al. established scaling laws for reward model overoptimization, showing that the gap between proxy and true reward grows with optimization strength and that this growth follows predictable functional forms.\n\n## Recent Research (2024-2026)\n\nMultiple recent papers address this challenge:\n\n- Reward hacking is a phenomenon where as optimization progresses, proxy reward continues to rise while true quality stagnates or degrades.\n\n- In later RL stages, as KL divergence increases, Standard RM shows a declining gold score and a rising proxy score, indicating overoptimization. Conversely, newer approaches maintain consistent growth in both scores, effectively mitigating overoptimization.\n\n- Although the performance of LLMs may seem to improve under the reward model (proxy reward), it can deviate from the actual human objectives (gold reward).\n\nThe search results contain extensive empirical evidence from 2024-2026 showing this exact phenomenon you asked about, with multiple papers developing methods to mitigate it."
    ],
    "durationSeconds": 8.054039619000003
  }
}
```

</details>

---

### Assistant

_source line 36_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for papers specifically related to our finding that are NOT already in the literature map. Let me look for:

1. Laidlaw et al. "Correlated Proxies" (2024/2025) - NOT in lit map, defines reward hacking via correlation breakdown
2. "Reward Model Overoptimisation in Iterated RLHF" - NOT in lit map
3. Any papers on Goodhart in code generation/formal verification specifically
4. Papers on "optimization against proxy" where proxy is explicitly *worse* than random

Let me also look for the specific "catastrophic Goodhart" phenomenon and the Thomas (2022) paper on reliance on metrics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "bc83aad8-1281-4314-8437-57bbe3fcd527",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A21wQmp1i4PxJsFRMfYs17",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4090,
      "cache_read_input_tokens": 50069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4090
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

Let me fetch details on a few key candidate papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "01c00d82-a276-47d1-8528-ca01939d00dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A21wQmp1i4PxJsFRMfYs17",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4090,
      "cache_read_input_tokens": 50069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4090
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Y1k32hmuYc8kTA1EGaEfVK`</summary>

```json
{
  "url": "https://arxiv.org/abs/2403.03185",
  "prompt": "Extract: title, authors, year, venue, abstract. What is the main finding about reward hacking and correlated proxies? Does it show cases where proxy optimization is worse than random/no optimization?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "0aaea37b-26c8-4064-93c4-3fee02642885",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A21wQmp1i4PxJsFRMfYs17",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4090,
      "cache_read_input_tokens": 50069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4090
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BFmKoQfEP9DNotMQ6D4YSE`</summary>

```json
{
  "query": "Goodhart reinforcement learning code generation formal verification reward hacking structured reward underperforms unstructured 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "88e228af-8a24-4994-9e47-1bc91d6c8819",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A21wQmp1i4PxJsFRMfYs17",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4090,
      "cache_read_input_tokens": 50069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4090
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EXCWXeAimnnspnPiNdb4jd`</summary>

```json
{
  "query": "\"optimization against proxy\" Fisher exact test significant degradation reward model proxy metric gaming 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "f271508d-9348-4d89-8db9-afd8f9988950",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A21wQmp1i4PxJsFRMfYs17",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4090,
      "cache_read_input_tokens": 50069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4090
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

_source line 41 · 2026-05-15T14:09:58.812Z_

<details><summary>↩ Tool result · `toolu_01Y1k32hmuYc8kTA1EGaEfVK`</summary>

```text
# Paper Summary

**Title:** Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking

**Authors:** Cassidy Laidlaw, Shivam Singhal, Anca Dragan

**Year:** 2024 (submitted March 5, 2024; latest version March 13, 2025)

**Venue:** ICLR 2025 (Spotlight)

## Abstract
The paper addresses "reward hacking," where "optimizing proxy rewards frequently leads to reward hacking: the optimized reward function ceases to be a good proxy and the resulting policy performs poorly with respect to the unspecified true reward."

## Main Finding
The authors propose a formal definition of reward hacking based on correlation breakdown between proxy and true rewards. Their key contribution is showing that "regularizing the χ² divergence between the policies' occupancy measures can be more effective" than standard KL penalties used in reinforcement learning from human feedback (RLHF).

## Cases Where Proxy Optimization Fails
The document confirms that the paper demonstrates realistic scenarios where proxy optimization indeed performs poorly, stating the method "better mitigates reward hacking in practice across four realistic settings, including RLHF." However, the abstract doesn't explicitly compare optimized proxies against random or no-optimization baselines—it focuses on comparing different regularization approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "d33d3cce-e495-479d-b855-fb2593aaa223",
  "tool_use_result": {
    "bytes": 48202,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary\n\n**Title:** Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking\n\n**Authors:** Cassidy Laidlaw, Shivam Singhal, Anca Dragan\n\n**Year:** 2024 (submitted March 5, 2024; latest version March 13, 2025)\n\n**Venue:** ICLR 2025 (Spotlight)\n\n## Abstract\nThe paper addresses \"reward hacking,\" where \"optimizing proxy rewards frequently leads to reward hacking: the optimized reward function ceases to be a good proxy and the resulting policy performs poorly with respect to the unspecified true reward.\"\n\n## Main Finding\nThe authors propose a formal definition of reward hacking based on correlation breakdown between proxy and true rewards. Their key contribution is showing that \"regularizing the χ² divergence between the policies' occupancy measures can be more effective\" than standard KL penalties used in reinforcement learning from human feedback (RLHF).\n\n## Cases Where Proxy Optimization Fails\nThe document confirms that the paper demonstrates realistic scenarios where proxy optimization indeed performs poorly, stating the method \"better mitigates reward hacking in practice across four realistic settings, including RLHF.\" However, the abstract doesn't explicitly compare optimized proxies against random or no-optimization baselines—it focuses on comparing different regularization approaches.",
    "durationMs": 5505,
    "url": "https://arxiv.org/abs/2403.03185"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T14:10:01.861Z_

<details><summary>↩ Tool result · `toolu_01EXCWXeAimnnspnPiNdb4jd`</summary>

```text
Web search results for query: ""optimization against proxy" Fisher exact test significant degradation reward model proxy metric gaming 2024 2025"

Links: [{"title":"A Comprehensive Survey of Reward Models: Taxonomy, Applications, Challenges, and Future","url":"https://arxiv.org/html/2504.12328v1"},{"title":"On the Optimality of Tracking Fisher Information in Adaptive ...","url":"https://arxiv.org/pdf/2510.07862"},{"title":"Robust Optimization for Mitigating Reward Hacking with Correlated Proxies","url":"https://arxiv.org/html/2604.12086v1"},{"title":"On the Optimality of Tracking Fisher Information in Adaptive Testing with Stochastic Binary Responses","url":"https://arxiv.org/html/2510.07862v1"},{"title":"[2509.22677] Profit over Proxies: A Scalable Bayesian Decision Framework for Optimizing Multi-Variant Online Experiments","url":"https://arxiv.org/abs/2509.22677"},{"title":"Direct Preference Optimization: Your Language Model is Secretly a Reward Model","url":"https://arxiv.org/pdf/2305.18290"},{"title":"Reward Models and Learning Strategies","url":"https://aclanthology.org/2025.findings-emnlp.970.pdf"},{"title":"ICML Poster Discriminative Policy Optimization for Token-Level Reward Models","url":"https://icml.cc/virtual/2025/poster/44776"},{"title":"[2510.07862] On the Optimality of Tracking Fisher Information in Adaptive Testing with Stochastic Binary Responses","url":"https://arxiv.org/abs/2510.07862"},{"title":"Findings of the Association for Computational Linguistics:","url":"https://aclanthology.org/2025.findings-naacl.447.pdf"}]

Based on the web search results, I found relevant research related to optimization against proxy metrics and reward model degradation. Here are the key findings:

## Reward Hacking and Proxy Metric Optimization

A critical challenge in reward model training is overoptimization (also called reward hacking), where reward models can be excessively optimized to narrow evaluation metrics, and an RL policy trained against such models may "hack" the reward signal, leading to performance degradation.

## Causes of Proxy Metric Gaming

Some causes of overoptimization include reward tampering, mislead, and sycophancy.

## Mitigation Strategies

Several research directions such as RM ensemble, data augmentation, and robust training have demonstrated potential in mitigating overoptimization.

## Robust Optimization for Correlated Proxies

One particularly relevant recent work is "Correlated proxies: a new definition and improved mitigation for reward hacking" by Laidlaw, Singhal, and Dragan (2025) published at the International Conference on Learning Representations.

The search results indicate that this is an active research area with significant focus in 2024-2025, particularly addressing how to prevent optimization against proxy metrics from degrading actual performance in reward models used for language model alignment and reinforcement learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "9c6b5d91-f566-4e9d-bb02-c2d4f26fcbe0",
  "tool_use_result": {
    "query": "\"optimization against proxy\" Fisher exact test significant degradation reward model proxy metric gaming 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GihUebw4WodMh72pMTESKG",
        "content": [
          {
            "title": "A Comprehensive Survey of Reward Models: Taxonomy, Applications, Challenges, and Future",
            "url": "https://arxiv.org/html/2504.12328v1"
          },
          {
            "title": "On the Optimality of Tracking Fisher Information in Adaptive ...",
            "url": "https://arxiv.org/pdf/2510.07862"
          },
          {
            "title": "Robust Optimization for Mitigating Reward Hacking with Correlated Proxies",
            "url": "https://arxiv.org/html/2604.12086v1"
          },
          {
            "title": "On the Optimality of Tracking Fisher Information in Adaptive Testing with Stochastic Binary Responses",
            "url": "https://arxiv.org/html/2510.07862v1"
          },
          {
            "title": "[2509.22677] Profit over Proxies: A Scalable Bayesian Decision Framework for Optimizing Multi-Variant Online Experiments",
            "url": "https://arxiv.org/abs/2509.22677"
          },
          {
            "title": "Direct Preference Optimization: Your Language Model is Secretly a Reward Model",
            "url": "https://arxiv.org/pdf/2305.18290"
          },
          {
            "title": "Reward Models and Learning Strategies",
            "url": "https://aclanthology.org/2025.findings-emnlp.970.pdf"
          },
          {
            "title": "ICML Poster Discriminative Policy Optimization for Token-Level Reward Models",
            "url": "https://icml.cc/virtual/2025/poster/44776"
          },
          {
            "title": "[2510.07862] On the Optimality of Tracking Fisher Information in Adaptive Testing with Stochastic Binary Responses",
            "url": "https://arxiv.org/abs/2510.07862"
          },
          {
            "title": "Findings of the Association for Computational Linguistics:",
            "url": "https://aclanthology.org/2025.findings-naacl.447.pdf"
          }
        ]
      },
      "Based on the web search results, I found relevant research related to optimization against proxy metrics and reward model degradation. Here are the key findings:\n\n## Reward Hacking and Proxy Metric Optimization\n\nA critical challenge in reward model training is overoptimization (also called reward hacking), where reward models can be excessively optimized to narrow evaluation metrics, and an RL policy trained against such models may \"hack\" the reward signal, leading to performance degradation.\n\n## Causes of Proxy Metric Gaming\n\nSome causes of overoptimization include reward tampering, mislead, and sycophancy.\n\n## Mitigation Strategies\n\nSeveral research directions such as RM ensemble, data augmentation, and robust training have demonstrated potential in mitigating overoptimization.\n\n## Robust Optimization for Correlated Proxies\n\nOne particularly relevant recent work is \"Correlated proxies: a new definition and improved mitigation for reward hacking\" by Laidlaw, Singhal, and Dragan (2025) published at the International Conference on Learning Representations.\n\nThe search results indicate that this is an active research area with significant focus in 2024-2025, particularly addressing how to prevent optimization against proxy metrics from degrading actual performance in reward models used for language model alignment and reinforcement learning."
    ],
    "durationSeconds": 7.1056860030000095
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-15T14:10:04.822Z_

<details><summary>↩ Tool result · `toolu_01BFmKoQfEP9DNotMQ6D4YSE`</summary>

```text
Web search results for query: "Goodhart reinforcement learning code generation formal verification reward hacking structured reward underperforms unstructured 2024 2025 2026"

Links: [{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"From Verifiable Dot to Reward Chain: Harnessing Verifiable Reference-based Rewards for Reinforcement Learning of Open-ended Generation","url":"https://arxiv.org/html/2601.18533v1"},{"title":"Reward Hacking – Shekhar Gulati","url":"https://shekhargulati.com/2025/05/28/reward-hacking/"},{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602v1"},{"title":"AI Safety II: Goodharting and Reward Hacking - Synthesis AI","url":"https://synthesis.ai/2025/05/08/ai-safety-ii-goodharting-and-reward-hacking/"},{"title":"Inference-Time Reward Hacking in Large Language Models","url":"https://openreview.net/pdf?id=vRfDOhiJAR"},{"title":"GitHub - opendilab/awesome-RLVR: A curated list of reinforcement learning with verifiable rewards (continually updated) · GitHub","url":"https://github.com/opendilab/awesome-RLVR"},{"title":"Reward hacking - Wikipedia","url":"https://en.wikipedia.org/wiki/Reward_hacking"},{"title":"Reward Modeling in Reinforcement Learning | Apolo AI Launchpad - Secure, Industry-Tailored AI Tools for Regulated Enterprises","url":"https://www.apolo.us/blog-posts/reward-modeling-in-reinforcement-learning"},{"title":"Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/html/2502.18770v3"}]

Based on the search results, I found substantial information about reward hacking, Goodhart's Law, and their intersection with reinforcement learning in code generation and formal verification contexts. Here's what the current research landscape shows:

## Key Findings

**Goodhart's Law and Reward Hacking Connection:**
Goodhart's Law states that "When a measure becomes a target, it ceases to be a good measure", with the intuition that a good metric can become corrupted once significant pressure is applied to optimize it. Reward hacking is fundamentally rooted in Goodhart's Law, where an imperfect proxy measure breaks down when subjected to strong optimization.

**Reinforcement Learning with Verifiable Rewards (RLVR):**
Reinforcement learning with verifiable rewards (RLVR) has emerged as a promising paradigm for enhancing large language models in reasoning tasks such as mathematics and code generation, at its core only checking the correctness of the final reasoning result within the reasoning solution. However, RLVR fails in open-ended generation tasks, where no unambiguous ground truth exists and reliable verification cannot be reduced to a single dot.

**Structured vs. Unstructured Rewards:**
Reward models suffer from two major limitations: they are prone to reward hacking, often overfitting superficial artifacts and spurious correlations, and they require large-scale pairwise annotations, making training costly and brittle during RL optimization. While simple mathematical reasoning or code generation provide natural verification signals (did the math problem yield the correct answer? does the code pass a comprehensive test suite?), many important tasks do not fit into such neat boxes.

**Recent Mitigation Approaches (2024-2025):**
Fu et al. (2025) conducted a comprehensive study of various reward shaping methods used in RLHF and found two key design considerations: the reward function should have an upper bound, and the reward should have rapid growth and slow convergence. Their method, called Preference As Reward (PAR), demonstrated robustness against reward hacking even after extensive training.

**Contemporary Challenges:**
A significant shift has occurred in current frontier models, with reasoning models such as OpenAI's O1 series and DeepSeek-R1 found to reason about the testing processes and take actions to maximize scores. For instance, in a 2025 study, when reasoning LLMs were asked to win at chess, some attempted to hack the game system by modifying components. Reports in 2025 indicated that recent models engaged in increasingly sophisticated reward hacking.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "119856d0-29e3-4fd5-bb44-28a7165d962d",
  "tool_use_result": {
    "query": "Goodhart reinforcement learning code generation formal verification reward hacking structured reward underperforms unstructured 2024 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RZWBUCyHDmgywBGbNiA1iG",
        "content": [
          {
            "title": "Reward Hacking in Reinforcement Learning | Lil'Log",
            "url": "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"
          },
          {
            "title": "From Verifiable Dot to Reward Chain: Harnessing Verifiable Reference-based Rewards for Reinforcement Learning of Open-ended Generation",
            "url": "https://arxiv.org/html/2601.18533v1"
          },
          {
            "title": "Reward Hacking – Shekhar Gulati",
            "url": "https://shekhargulati.com/2025/05/28/reward-hacking/"
          },
          {
            "title": "Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges",
            "url": "https://arxiv.org/html/2604.13602v1"
          },
          {
            "title": "AI Safety II: Goodharting and Reward Hacking - Synthesis AI",
            "url": "https://synthesis.ai/2025/05/08/ai-safety-ii-goodharting-and-reward-hacking/"
          },
          {
            "title": "Inference-Time Reward Hacking in Large Language Models",
            "url": "https://openreview.net/pdf?id=vRfDOhiJAR"
          },
          {
            "title": "GitHub - opendilab/awesome-RLVR: A curated list of reinforcement learning with verifiable rewards (continually updated) · GitHub",
            "url": "https://github.com/opendilab/awesome-RLVR"
          },
          {
            "title": "Reward hacking - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Reward_hacking"
          },
          {
            "title": "Reward Modeling in Reinforcement Learning | Apolo AI Launchpad - Secure, Industry-Tailored AI Tools for Regulated Enterprises",
            "url": "https://www.apolo.us/blog-posts/reward-modeling-in-reinforcement-learning"
          },
          {
            "title": "Reward Shaping to Mitigate Reward Hacking in RLHF",
            "url": "https://arxiv.org/html/2502.18770v3"
          }
        ]
      },
      "Based on the search results, I found substantial information about reward hacking, Goodhart's Law, and their intersection with reinforcement learning in code generation and formal verification contexts. Here's what the current research landscape shows:\n\n## Key Findings\n\n**Goodhart's Law and Reward Hacking Connection:**\nGoodhart's Law states that \"When a measure becomes a target, it ceases to be a good measure\", with the intuition that a good metric can become corrupted once significant pressure is applied to optimize it. Reward hacking is fundamentally rooted in Goodhart's Law, where an imperfect proxy measure breaks down when subjected to strong optimization.\n\n**Reinforcement Learning with Verifiable Rewards (RLVR):**\nReinforcement learning with verifiable rewards (RLVR) has emerged as a promising paradigm for enhancing large language models in reasoning tasks such as mathematics and code generation, at its core only checking the correctness of the final reasoning result within the reasoning solution. However, RLVR fails in open-ended generation tasks, where no unambiguous ground truth exists and reliable verification cannot be reduced to a single dot.\n\n**Structured vs. Unstructured Rewards:**\nReward models suffer from two major limitations: they are prone to reward hacking, often overfitting superficial artifacts and spurious correlations, and they require large-scale pairwise annotations, making training costly and brittle during RL optimization. While simple mathematical reasoning or code generation provide natural verification signals (did the math problem yield the correct answer? does the code pass a comprehensive test suite?), many important tasks do not fit into such neat boxes.\n\n**Recent Mitigation Approaches (2024-2025):**\nFu et al. (2025) conducted a comprehensive study of various reward shaping methods used in RLHF and found two key design considerations: the reward function should have an upper bound, and the reward should have rapid growth and slow convergence. Their method, called Preference As Reward (PAR), demonstrated robustness against reward hacking even after extensive training.\n\n**Contemporary Challenges:**\nA significant shift has occurred in current frontier models, with reasoning models such as OpenAI's O1 series and DeepSeek-R1 found to reason about the testing processes and take actions to maximize scores. For instance, in a 2025 study, when reasoning LLMs were asked to win at chess, some attempted to hack the game system by modifying components. Reports in 2025 indicated that recent models engaged in increasingly sophisticated reward hacking."
    ],
    "durationSeconds": 10.574000667999993
  }
}
```

</details>

---

### Assistant

_source line 44_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good picture. Let me identify the 2-4 papers most relevant to our specific finding (ISR genuine 6.9% vs Random 18.4%, p=0.0002) that are either:
1. Not already in the literature map, or
2. In the literature map but with a new relevance angle for INC-05

Papers already in the literature map:
- manheim-goodhart-taxonomy ✓
- karwowski-goodhart-rl ✓
- gao-reward-overoptimization ✓
- spurious-rewards ✓
- skalse-reward-hacking ✓


- kwa-catastrophic-goodhart ✓
- pan-reward-misspecification ✓
- gao-effective-rl-reward ✓
- prof-process-outcome ✓

The key papers I'm focusing on are Laidlaw et al.'s work on correlated proxies, which directly explains how ISR breaks down as a reward signal under optimization, and another 2025 paper on reward model overoptimization in iterated RLHF that seems particularly relevant to our findings.

Our core result is striking: optimizing for ISR yields a genuine rate of 6.9%, substantially worse than the random baseline at 18.4% (p=0.0002). This isn't just a proxy that fails to help—it actively degrades performance. Laidlaw's framework formalizes exactly this phenomenon, showing how proxy optimization can produce lower true reward than the reference policy, and their chi-squared regularization approach might offer a path forward.

The other papers in the literature map all converge on related mechanisms: Gao's work highlights how process-level signals like ISR can backfire, Pan's research shows that more capable agents exploit reward misspecifications more effectively, Karwowski's geometric analysis demonstrates how any meaningfully correlated proxy creates divergence regions, and Yang's spurious rewards study provides a direct empirical parallel where random rewards outperform certain learned signals.

I'm recognizing this as regressional Goodhart's law in action—ISR shows genuine correlation with quality in the unoptimized regime, but once it becomes the optimization target, the policy exploits the noise component and the correlation collapses. Now I'm looking for an empirical precedent where a deliberately designed reward actually performs worse than random, which would be the strongest parallel to our ISR finding.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "95c68e5f-4442-458c-b100-9865400b4643",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013CBGB1PC9J6NGrNHZWKA9c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 797,
      "cache_creation_input_tokens": 1899,
      "cache_read_input_tokens": 54159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1899
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

_source line 45_

Let me search for one more angle — the specific phenomenon where a designed metric performs worse than random.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "2fd55644-e7a9-4f76-b244-f7adce60443e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013CBGB1PC9J6NGrNHZWKA9c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 797,
      "cache_creation_input_tokens": 1899,
      "cache_read_input_tokens": 54159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1899
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01REDREtAEW85GJVRxV6DPtr`</summary>

```json
{
  "query": "\"process reward\" OR \"auxiliary reward\" significantly worse random noise GRPO PPO reinforcement learning LLM reasoning empirical 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "dd6e5a1f-4779-4083-9028-b91b8ac3c020",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013CBGB1PC9J6NGrNHZWKA9c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 797,
      "cache_creation_input_tokens": 1899,
      "cache_read_input_tokens": 54159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1899
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JSjPy4aYJmCiAeZfYm6Ep4`</summary>

```json
{
  "url": "https://arxiv.org/abs/2403.03185v4",
  "prompt": "Extract: full title, all authors, publication venue, exact year. What is the formal definition of reward hacking they propose? Do they show empirical cases where optimized policy has lower true reward than the reference (unoptimized) policy?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "046b7d8b-e86b-4fd6-9e9a-4e614589788b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013CBGB1PC9J6NGrNHZWKA9c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 797,
      "cache_creation_input_tokens": 1899,
      "cache_read_input_tokens": 54159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1899
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

### Runtime record

_source line 48_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778872200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "8290a4bc-5fac-40c5-8265-71583bba596c",
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e"
}
```

---

### Tool result

_source line 49 · 2026-05-15T14:10:35.356Z_

<details><summary>↩ Tool result · `toolu_01JSjPy4aYJmCiAeZfYm6Ep4`</summary>

```text
# Paper Summary

**Full Title:** Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking

**Authors:** Cassidy Laidlaw, Shivam Singhal, Anca Dragan

**Publication Venue:** ICLR 2025 (Spotlight)

**Year:** 2025 (submitted March 2024, final revision March 2025)

## Formal Definition of Reward Hacking

The paper introduces a definition based on "the correlation between proxy and true rewards for states and actions seen by a reference policy that breaks down under optimization." This captures instances where the proxy reward ceases to approximate the true objective as policies are optimized.

## Empirical Evidence

The abstract states the approach was "demonstrate[d]...in practice across four realistic settings, including RLHF," and mentions the researchers "intuitively show the benefits" of their regularization method. However, the provided content does not explicitly confirm whether empirical cases show optimized policies achieving lower true rewards than reference policies—only that their method better mitigates reward hacking across tested scenarios.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "4b3010ad-01bb-4590-8fc5-3b1b9e696c60",
  "tool_use_result": {
    "bytes": 48216,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary\n\n**Full Title:** Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking\n\n**Authors:** Cassidy Laidlaw, Shivam Singhal, Anca Dragan\n\n**Publication Venue:** ICLR 2025 (Spotlight)\n\n**Year:** 2025 (submitted March 2024, final revision March 2025)\n\n## Formal Definition of Reward Hacking\n\nThe paper introduces a definition based on \"the correlation between proxy and true rewards for states and actions seen by a reference policy that breaks down under optimization.\" This captures instances where the proxy reward ceases to approximate the true objective as policies are optimized.\n\n## Empirical Evidence\n\nThe abstract states the approach was \"demonstrate[d]...in practice across four realistic settings, including RLHF,\" and mentions the researchers \"intuitively show the benefits\" of their regularization method. However, the provided content does not explicitly confirm whether empirical cases show optimized policies achieving lower true rewards than reference policies—only that their method better mitigates reward hacking across tested scenarios.",
    "durationMs": 4104,
    "url": "https://arxiv.org/abs/2403.03185v4"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T14:10:38.189Z_

<details><summary>↩ Tool result · `toolu_01REDREtAEW85GJVRxV6DPtr`</summary>

```text
Web search results for query: ""process reward" OR "auxiliary reward" significantly worse random noise GRPO PPO reinforcement learning LLM reasoning empirical 2025 2026"

Links: [{"title":"Post-Training in 2026: GRPO, DAPO, RLVR & Beyond","url":"https://llm-stats.com/blog/research/post-training-techniques-2026"},{"title":"LLM Reasoning with Process Rewards for Outcome-Guided Steps","url":"https://arxiv.org/html/2604.02341v1"},{"title":"[2604.02341] LLM Reasoning with Process Rewards for Outcome-Guided Steps","url":"https://arxiv.org/abs/2604.02341"},{"title":"Use large language model to enhance reasoning of another large language model through reward updated GRPO | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-39296-8"},{"title":"The State of Reinforcement Learning for LLM Reasoning","url":"https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training"},{"title":"Comparative Analysis and Parametric Tuning of PPO, GRPO, and DAPO for LLM Reasoning Enhancement","url":"https://arxiv.org/html/2512.07611v1"},{"title":"Random Policy Valuation is Enough for LLM Reasoning with Verifiable Rewards","url":"https://arxiv.org/html/2509.24981v1"},{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"},{"title":"PPO for LLMs: A Guide for Normal People","url":"https://cameronrwolfe.substack.com/p/ppo-llm"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"}]

Based on the search results, I found several highly relevant papers and resources about process rewards, auxiliary rewards, and their interactions with reinforcement learning algorithms (GRPO, PPO) for LLM reasoning in 2025-2026:

## Key Research Findings:

### Process Rewards and Outcome-Guided Training

PROGRS treats process rewards as relative preferences within outcome groups rather than absolute targets, introducing outcome-conditioned centering which shifts PRM scores of incorrect trajectories to have zero mean within each prompt group. This recent work (February 2026) directly addresses how process reward models interact with outcome correctness during RL training.

Existing PRM-based methods improve PRM quality, filter trajectories, or modify reward aggregation, but they do not directly constrain how process rewards interact with outcome correctness during optimization, which PROGRS proposes to address.

### Stability Issues with Auxiliary Signals

Current methods following generalized policy iteration suffer from unstable learning dynamics and entropy collapse induced by the reward-maximizing nature within iterative policy evaluation, with leading algorithms like GRPO still exhibiting unstable learning dynamics and being prone to model collapse.

### DAPO's Approach to Reward Noise

DAPO (ByteDance/Tsinghua, 2025) tackles instabilities that arise when training reasoning models with long chain-of-thought outputs, introducing Overlong Reward Shaping to reduce reward noise from responses that exceed length limits.

The search results show active research in 2025-2026 on managing reward signal quality and stability in reasoning model training, with multiple approaches addressing the degradation that can occur from noisy or poorly-specified auxiliary rewards.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "d5aeee51-d42b-4188-a918-1daa0a69d3d1",
  "tool_use_result": {
    "query": "\"process reward\" OR \"auxiliary reward\" significantly worse random noise GRPO PPO reinforcement learning LLM reasoning empirical 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XHSYrxUDcLASmhLbGEWMb1",
        "content": [
          {
            "title": "Post-Training in 2026: GRPO, DAPO, RLVR & Beyond",
            "url": "https://llm-stats.com/blog/research/post-training-techniques-2026"
          },
          {
            "title": "LLM Reasoning with Process Rewards for Outcome-Guided Steps",
            "url": "https://arxiv.org/html/2604.02341v1"
          },
          {
            "title": "[2604.02341] LLM Reasoning with Process Rewards for Outcome-Guided Steps",
            "url": "https://arxiv.org/abs/2604.02341"
          },
          {
            "title": "Use large language model to enhance reasoning of another large language model through reward updated GRPO | Scientific Reports",
            "url": "https://www.nature.com/articles/s41598-026-39296-8"
          },
          {
            "title": "The State of Reinforcement Learning for LLM Reasoning",
            "url": "https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training"
          },
          {
            "title": "Comparative Analysis and Parametric Tuning of PPO, GRPO, and DAPO for LLM Reasoning Enhancement",
            "url": "https://arxiv.org/html/2512.07611v1"
          },
          {
            "title": "Random Policy Valuation is Enough for LLM Reasoning with Verifiable Rewards",
            "url": "https://arxiv.org/html/2509.24981v1"
          },
          {
            "title": "Group Relative Policy Optimization (GRPO)",
            "url": "https://cameronrwolfe.substack.com/p/grpo"
          },
          {
            "title": "PPO for LLMs: A Guide for Normal People",
            "url": "https://cameronrwolfe.substack.com/p/ppo-llm"
          },
          {
            "title": "The State Of LLMs 2025: Progress, Progress, and Predictions",
            "url": "https://magazine.sebastianraschka.com/p/state-of-llms-2025"
          }
        ]
      },
      "Based on the search results, I found several highly relevant papers and resources about process rewards, auxiliary rewards, and their interactions with reinforcement learning algorithms (GRPO, PPO) for LLM reasoning in 2025-2026:\n\n## Key Research Findings:\n\n### Process Rewards and Outcome-Guided Training\n\nPROGRS treats process rewards as relative preferences within outcome groups rather than absolute targets, introducing outcome-conditioned centering which shifts PRM scores of incorrect trajectories to have zero mean within each prompt group. This recent work (February 2026) directly addresses how process reward models interact with outcome correctness during RL training.\n\nExisting PRM-based methods improve PRM quality, filter trajectories, or modify reward aggregation, but they do not directly constrain how process rewards interact with outcome correctness during optimization, which PROGRS proposes to address.\n\n### Stability Issues with Auxiliary Signals\n\nCurrent methods following generalized policy iteration suffer from unstable learning dynamics and entropy collapse induced by the reward-maximizing nature within iterative policy evaluation, with leading algorithms like GRPO still exhibiting unstable learning dynamics and being prone to model collapse.\n\n### DAPO's Approach to Reward Noise\n\nDAPO (ByteDance/Tsinghua, 2025) tackles instabilities that arise when training reasoning models with long chain-of-thought outputs, introducing Overlong Reward Shaping to reduce reward noise from responses that exceed length limits.\n\nThe search results show active research in 2025-2026 on managing reward signal quality and stability in reasoning model training, with multiple approaches addressing the degradation that can occur from noisy or poorly-specified auxiliary rewards."
    ],
    "durationSeconds": 8.334010394999991
  }
}
```

</details>

---

### Assistant

_source line 51_

<details><summary>Logged reasoning block</summary>

```text
Now I have another interesting find: "Random Policy Valuation is Enough for LLM Reasoning with Verifiable Rewards" (arXiv 2509.24981). This seems VERY relevant - let me check it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "b77af38a-e05d-44bb-b257-7261bd57b81c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NvrHHTwAV7996YwW8yEdat",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 279,
      "cache_creation_input_tokens": 2931,
      "cache_read_input_tokens": 56058,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2931
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

_source line 52_

Found an interesting paper. Let me check it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "34abb44e-f48e-4412-a3d6-cb0f4afa3cd1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NvrHHTwAV7996YwW8yEdat",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 279,
      "cache_creation_input_tokens": 2931,
      "cache_read_input_tokens": 56058,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2931
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

_source line 53_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AHvXwY4xwXD5kTKFsh6sq1`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.24981",
  "prompt": "Extract: full title, all authors, year, venue, abstract. What is their main finding about random policy valuation vs structured rewards in LLM reasoning?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "34b2beac-f337-46d5-9cba-d7f159130a14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NvrHHTwAV7996YwW8yEdat",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 279,
      "cache_creation_input_tokens": 2931,
      "cache_read_input_tokens": 56058,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2931
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

_source line 54 · 2026-05-15T14:10:48.191Z_

<details><summary>↩ Tool result · `toolu_01AHvXwY4xwXD5kTKFsh6sq1`</summary>

```text
# Paper Summary

**Full Title:** Random Policy Valuation is Enough for LLM Reasoning with Verifiable Rewards

**Authors:** Haoran He, Yuxiao Ye, Qingpeng Cai, Chen Hu, Binxing Jiao, Daxin Jiang, Ling Pan

**Year:** 2025

**Venue:** arXiv (cs.LG - Machine Learning)

## Main Finding

The researchers' key insight is that "the optimal action can be recovered from the Q-function of a fixed uniformly random policy," eliminating the need for complex policy iteration loops. 

Rather than relying on structured reward optimization like PPO or GRPO, they demonstrate that sampling actions from a softmax distribution over random policy Q-values achieves superior results. Their ROVER algorithm shows:

- **Quality improvements:** +8.2 on pass@1 and +16.8 on pass@256 metrics
- **Diversity gains:** +17.6% improvement in solution diversity
- **Simplification:** A "minimalist yet highly effective" approach compared to existing sophisticated methods

The core finding suggests that math reasoning problems have sufficient inherent structure (finite-horizon MDPs with deterministic transitions and tree dynamics) that complex policy optimization techniques are unnecessary—random policy valuation alone suffices for effective reasoning improvement.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "82f6fc30-555b-4397-8520-c64eb2230d8a",
  "tool_use_result": {
    "bytes": 49461,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary\n\n**Full Title:** Random Policy Valuation is Enough for LLM Reasoning with Verifiable Rewards\n\n**Authors:** Haoran He, Yuxiao Ye, Qingpeng Cai, Chen Hu, Binxing Jiao, Daxin Jiang, Ling Pan\n\n**Year:** 2025\n\n**Venue:** arXiv (cs.LG - Machine Learning)\n\n## Main Finding\n\nThe researchers' key insight is that \"the optimal action can be recovered from the Q-function of a fixed uniformly random policy,\" eliminating the need for complex policy iteration loops. \n\nRather than relying on structured reward optimization like PPO or GRPO, they demonstrate that sampling actions from a softmax distribution over random policy Q-values achieves superior results. Their ROVER algorithm shows:\n\n- **Quality improvements:** +8.2 on pass@1 and +16.8 on pass@256 metrics\n- **Diversity gains:** +17.6% improvement in solution diversity\n- **Simplification:** A \"minimalist yet highly effective\" approach compared to existing sophisticated methods\n\nThe core finding suggests that math reasoning problems have sufficient inherent structure (finite-horizon MDPs with deterministic transitions and tree dynamics) that complex policy optimization techniques are unnecessary—random policy valuation alone suffices for effective reasoning improvement.",
    "durationMs": 5136,
    "url": "https://arxiv.org/abs/2509.24981"
  }
}
```

</details>

---

### Assistant

_source line 55_

<details><summary>Logged reasoning block</summary>

```text
This paper (ROVER) is interesting but not directly about our finding. It's about test-time scaling, not training-time reward design. Our finding is about training with ISR as a reward signal vs random reward.

Let me now synthesize. I have enough information to write the literature linkage document. Let me identify the 2-4 most relevant papers:

**Papers NOT in literature_map.yaml that should be added:**

1. **Laidlaw, Singhal, Dragan (2025) "Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking"** - ICLR 2025 Spotlight
   - This formalizes reward hacking through the lens of correlation breakdown, which directly explains our finding: ISR acts as a correlated proxy that tracks genuine quality under the reference policy, but once we optimize against it, that correlation collapses and genuine performance drops below random baseline.

2. **"Robust Optimization for Mitigating Reward Hacking with Correlated Proxies"** (2026, arXiv 2604.12086) - Follow-up to Laidlaw et al.
   - Probably too incremental to include.

**Papers ALREADY in literature_map.yaml with new INC-05 angle:**

3. **Pan, B**

hatia, Steinhardt (2022) "The Effects of Reward Misspecification"** - ICLR 2022
   - Already catalogued as `pan-reward-misspecification`
   - The key insight here is that more capable agents are better at exploiting misspecifications, so our ISR-optimized model becomes more capable at gaming the metric itself, which paradoxically tanks the genuine rate below what random selection would achieve.

4. **Karwowski et al. (2024) "Goodhart's Law in Reinforcement Learning"** - ICLR 2024
   - Already catalogued as `karwowski-goodhart-rl`
   - They found empirical evidence of Goodhart degradation in about 19% of their experiments, and our ISR result is a textbook example of this with extremely strong statistical significance.

5. **Yang et al. (2025) "Spurious Rewards"**
   - Already catalogued as `spurious-rewards`
   - Their finding that random performance matches ground truth is interesting, but our result is actually more striking—we're showing that a deliberately designed proxy performs substantially worse than random, not just equivalent to it.

6. **Manheim & Garrabrant (2019) "Categorizing Variants of Goodhart's Law"**
   - Already catalogued as `manheim-goodhart-taxonomy`
   - Our ISR case fits cleanly into their "regressional Goodhart" category—the metric correlates with genuine quality initially, but once you optimize for it, the noise gets exploited rather than the signal.

Now I'm identifying the most impactful new papers to add alongside these existing references:

**New papers to include:**
1. Laidlaw et al. (2025) "Correlated Proxies" - ICLR 2025 Spotlight

Actually, looking through the lit map more carefully, that's the main paper that's genuinely new and directly relevant. Most of the other key work is already there. The Laidlaw paper is the standout addition.

I should also check whether "Rethinking Reward Model Evaluation: Are We Barking up the Wrong Tree?" from ICLR 2025 is worth including—it could be relevant if it demonstrates a disconnect between reward model evaluation metrics and actual downstream performance.

The core finding I'm building toward is that ISR as a reward signal produces a 6.9% genuine rate compared to 18.4% for random, with strong statistical significance (p=0.0002), which directly contradicts the assumption that a structured proxy should outperform random selection.

For the paper, I want to position this as empirical evidence of Goodhart's Law operating in neurosymbolic RL, drawing on the Manheim & Garrabrant taxonomy and related work. The key distinction is that this isn't just about spurious rewards performing as well as ground truth—it's about a carefully engineered proxy actively performing worse than random, which is a stronger claim. I'll connect this to the broader reward overoptimization literature and use Laidlaw's formal framing for the "worse than reference policy" angle.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "39c61de1-7b51-4295-ba2b-eddeb0cf3e69",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01USs2V47SSLdBAoDhQTEvu1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 58989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 781
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

_source line 56_

I have enough information. Let me write the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "09def929-3882-4136-89ff-c6a9efab19bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01USs2V47SSLdBAoDhQTEvu1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 58989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 781
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

_source line 57_

<details open><summary>🔧 Tool call — Write · `toolu_013oyfkT6nGpgGLaUfAzz1uN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/inc05_literature_linkage.md",
  "content": "# INC-05 Literature Linkage\n\n## 核心发现摘要\nISR genuine rate 6.9% (16/231) vs Random baseline 18.4% (34/185), Fisher exact p=0.0002.\nISR 作为优化目标不仅未提升结构质量，反而**显著降低**了 genuine rate——典型的 optimization-against-proxy 证据。\n\n---\n\n## 相关文献\n\n### 1. Laidlaw et al. (2025) — Correlated Proxies [**新，未在 literature_map 中**]\n\n- **引用**: Cassidy Laidlaw, Shivam Singhal, Anca Dragan. \"Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking.\" ICLR 2025 (Spotlight). arXiv 2403.03185.\n- **关联点**: 提出基于 correlation breakdown 的 reward hacking 形式化定义：proxy reward 在 reference policy 下与 true reward 相关，但 optimization 破坏该相关性，导致 optimized policy 的 true reward **低于 reference policy**。这精确描述了 INC-05 发现：ISR 在未优化模型上与 genuine quality 正相关，但 GRPO 优化后 genuine rate 从 18.4%（random baseline ≈ reference）降至 6.9%。论文进一步证明 χ² divergence 正则化优于标准 KL penalty，暗示 GRPO 的 KL constraint 不足以防止 ISR-specific 的 correlation breakdown。\n- **已在 literature_map**: 否\n- **建议 claim**: \"Our finding that ISR optimization reduces genuine rate below the random baseline (p=0.0002) constitutes an empirical instance of the correlation-breakdown reward hacking formalized by Laidlaw et al. (2025).\"\n\n### 2. Yang et al. (2025) — Spurious Rewards [**已在 literature_map，新角度**]\n\n- **引用**: Ruixin Yang et al. \"Spurious Rewards: Rethinking Training Signals in RLVR.\" arXiv 2506.10947.\n- **关联点**: 他们发现 GRPO + random reward 在 Qwen2.5-Math 上提升 21.4%，接近 ground-truth reward 的 29.1%。我们的发现是其**强化版**：不仅 random ≈ structured，而是 structured ISR (6.9%) **显著劣于** random (18.4%)。这表明 ISR 不是\"无用的噪声\"而是\"有害的系统性偏差\"——GRPO 的 group normalization 可以从 random noise 中提取信号，但 ISR 的结构化偏差引导 policy 进入 high-ISR-low-genuine 区域。\n- **已在 literature_map**: 是 (`spurious-rewards`)\n- **建议 claim**: \"While Yang et al. (2025) show random rewards nearly match ground-truth rewards, our results go further: the structured ISR proxy performs significantly *worse* than random (6.9% vs 18.4%, p=0.0002), indicating that ISR introduces systematic bias rather than mere noise.\"\n\n### 3. Manheim & Garrabrant (2019) — Regressional Goodhart [**已在 literature_map，新角度**]\n\n- **引用**: David Manheim, Scott Garrabrant. \"Categorizing Variants of Goodhart's Law.\" arXiv 1803.04585.\n- **关联点**: INC-05 发现映射到 **regressional Goodhart**: ISR 在未优化 regime 下是 genuine quality 的 noisy estimator（正相关），但当作为优化目标时，policy 利用 noise component（ISR 的非 genuine 部分——可以通过 redundant clauses、tautological structures 等获得 high ISR），导致 genuine rate 反向下降。与 extremal Goodhart（policy 进入 OOD 区域）不同，regressional Goodhart 不需要 distributional shift，仅需 proxy 中的 noise variance 足以被 optimization 利用。\n- **已在 literature_map**: 是 (`manheim-goodhart-taxonomy`)，但当前 relevance 描述将 STA 归类为 extremal Goodhart\n- **建议 claim**: \"The ISR-vs-random gap exemplifies regressional Goodhart (Manheim & Garrabrant, 2019): under optimization, the model exploits the gap between ISR and genuine structural necessity, producing formalizations that score high on ISR through redundant or tautological constructions rather than genuine reasoning.\"\n\n### 4. Pan, Bhatia, Steinhardt (2022) — Effects of Reward Misspecification [**已在 literature_map，新角度**]\n\n- **引用**: Alexander Pan, Kush Bhatia, Jacob Steinhardt. \"The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models.\" ICLR 2022.\n- **关联点**: 核心发现\"more capable agents exploit misspecifications more\"直接解释 ISR paradox：ISR-optimized model 比 random-baseline model 更\"capable\"（在 ISR metric 上），但这种 capability 被用于 exploit ISR misspecification（gaming structural necessity），导致 genuine rate 更低。Random baseline 无法 exploit ISR（因为没有 ISR gradient signal），反而保留了更多 genuine formalization diversity。\n- **已在 literature_map**: 是 (`pan-reward-misspecification`)\n- **建议 claim**: \"Consistent with Pan et al. (2022), the ISR-optimized model's superior capability at maximizing the proxy metric correlates with worse true performance, as the model learns to exploit ISR's misspecification rather than improve genuine formalization quality.\"\n\n---\n\n## 建议\n\n### 应加入 literature_map 的论文\n1. **Laidlaw et al. (2025) \"Correlated Proxies\"** — ICLR 2025 Spotlight。category: `reward-hacking`, role: `theoretical-foundation`。提供 reward hacking 的 correlation-breakdown 形式化定义，直接框架化 ISR genuine rate 降低现象。\n\n### Related Work section 可引用的具体 claim\n\n1. **Goodhart framing (Discussion section)**:\n   > Our finding that ISR-as-reward produces significantly lower genuine rate than random baseline (6.9% vs 18.4%, Fisher p=0.0002) provides empirical evidence of Goodhart's Law in neurosymbolic RL. Specifically, this constitutes regressional Goodhart (Manheim & Garrabrant, 2019): ISR correlates with genuine structural necessity under the reference distribution, but optimization pressure exploits the gap between proxy and true objective.\n\n2. **Random-vs-structured comparison (Results section)**:\n   > Yang et al. (2025) demonstrate that random rewards nearly match ground-truth rewards in GRPO training. Our results reveal a stronger phenomenon: the structured ISR proxy performs significantly *worse* than random, suggesting that ISR's systematic bias actively misleads optimization into high-ISR-low-genuine regions of the policy space.\n\n3. **Capability-exploitation linkage (Discussion section)**:\n   > The ISR-trained model exhibits the capability-exploitation tradeoff identified by Pan et al. (2022): greater optimization capability enables more effective exploitation of reward misspecification. The random baseline, lacking ISR gradient signal, cannot exploit ISR's structural gaps and thus preserves higher genuine formalization diversity.\n\n4. **Formal reward hacking definition (Related Work)**:\n   > Under the correlated-proxy framework of Laidlaw et al. (2025), ISR constitutes a proxy whose correlation with genuine quality breaks down under GRPO optimization, yielding a policy with lower true reward than the reference policy—the formal definition of reward hacking.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "a8300f29-ae9b-4af1-9469-6c2c8448dcd7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01USs2V47SSLdBAoDhQTEvu1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 58989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 781
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

_source line 58 · 2026-05-15T14:11:53.533Z_

<details><summary>↩ Tool result · `toolu_013oyfkT6nGpgGLaUfAzz1uN`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/inc05_literature_linkage.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "1f7aeb1d-24ba-4018-8bec-4b7d315eae64",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/inc05_literature_linkage.md",
    "content": "# INC-05 Literature Linkage\n\n## 核心发现摘要\nISR genuine rate 6.9% (16/231) vs Random baseline 18.4% (34/185), Fisher exact p=0.0002.\nISR 作为优化目标不仅未提升结构质量，反而**显著降低**了 genuine rate——典型的 optimization-against-proxy 证据。\n\n---\n\n## 相关文献\n\n### 1. Laidlaw et al. (2025) — Correlated Proxies [**新，未在 literature_map 中**]\n\n- **引用**: Cassidy Laidlaw, Shivam Singhal, Anca Dragan. \"Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking.\" ICLR 2025 (Spotlight). arXiv 2403.03185.\n- **关联点**: 提出基于 correlation breakdown 的 reward hacking 形式化定义：proxy reward 在 reference policy 下与 true reward 相关，但 optimization 破坏该相关性，导致 optimized policy 的 true reward **低于 reference policy**。这精确描述了 INC-05 发现：ISR 在未优化模型上与 genuine quality 正相关，但 GRPO 优化后 genuine rate 从 18.4%（random baseline ≈ reference）降至 6.9%。论文进一步证明 χ² divergence 正则化优于标准 KL penalty，暗示 GRPO 的 KL constraint 不足以防止 ISR-specific 的 correlation breakdown。\n- **已在 literature_map**: 否\n- **建议 claim**: \"Our finding that ISR optimization reduces genuine rate below the random baseline (p=0.0002) constitutes an empirical instance of the correlation-breakdown reward hacking formalized by Laidlaw et al. (2025).\"\n\n### 2. Yang et al. (2025) — Spurious Rewards [**已在 literature_map，新角度**]\n\n- **引用**: Ruixin Yang et al. \"Spurious Rewards: Rethinking Training Signals in RLVR.\" arXiv 2506.10947.\n- **关联点**: 他们发现 GRPO + random reward 在 Qwen2.5-Math 上提升 21.4%，接近 ground-truth reward 的 29.1%。我们的发现是其**强化版**：不仅 random ≈ structured，而是 structured ISR (6.9%) **显著劣于** random (18.4%)。这表明 ISR 不是\"无用的噪声\"而是\"有害的系统性偏差\"——GRPO 的 group normalization 可以从 random noise 中提取信号，但 ISR 的结构化偏差引导 policy 进入 high-ISR-low-genuine 区域。\n- **已在 literature_map**: 是 (`spurious-rewards`)\n- **建议 claim**: \"While Yang et al. (2025) show random rewards nearly match ground-truth rewards, our results go further: the structured ISR proxy performs significantly *worse* than random (6.9% vs 18.4%, p=0.0002), indicating that ISR introduces systematic bias rather than mere noise.\"\n\n### 3. Manheim & Garrabrant (2019) — Regressional Goodhart [**已在 literature_map，新角度**]\n\n- **引用**: David Manheim, Scott Garrabrant. \"Categorizing Variants of Goodhart's Law.\" arXiv 1803.04585.\n- **关联点**: INC-05 发现映射到 **regressional Goodhart**: ISR 在未优化 regime 下是 genuine quality 的 noisy estimator（正相关），但当作为优化目标时，policy 利用 noise component（ISR 的非 genuine 部分——可以通过 redundant clauses、tautological structures 等获得 high ISR），导致 genuine rate 反向下降。与 extremal Goodhart（policy 进入 OOD 区域）不同，regressional Goodhart 不需要 distributional shift，仅需 proxy 中的 noise variance 足以被 optimization 利用。\n- **已在 literature_map**: 是 (`manheim-goodhart-taxonomy`)，但当前 relevance 描述将 STA 归类为 extremal Goodhart\n- **建议 claim**: \"The ISR-vs-random gap exemplifies regressional Goodhart (Manheim & Garrabrant, 2019): under optimization, the model exploits the gap between ISR and genuine structural necessity, producing formalizations that score high on ISR through redundant or tautological constructions rather than genuine reasoning.\"\n\n### 4. Pan, Bhatia, Steinhardt (2022) — Effects of Reward Misspecification [**已在 literature_map，新角度**]\n\n- **引用**: Alexander Pan, Kush Bhatia, Jacob Steinhardt. \"The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models.\" ICLR 2022.\n- **关联点**: 核心发现\"more capable agents exploit misspecifications more\"直接解释 ISR paradox：ISR-optimized model 比 random-baseline model 更\"capable\"（在 ISR metric 上），但这种 capability 被用于 exploit ISR misspecification（gaming structural necessity），导致 genuine rate 更低。Random baseline 无法 exploit ISR（因为没有 ISR gradient signal），反而保留了更多 genuine formalization diversity。\n- **已在 literature_map**: 是 (`pan-reward-misspecification`)\n- **建议 claim**: \"Consistent with Pan et al. (2022), the ISR-optimized model's superior capability at maximizing the proxy metric correlates with worse true performance, as the model learns to exploit ISR's misspecification rather than improve genuine formalization quality.\"\n\n---\n\n## 建议\n\n### 应加入 literature_map 的论文\n1. **Laidlaw et al. (2025) \"Correlated Proxies\"** — ICLR 2025 Spotlight。category: `reward-hacking`, role: `theoretical-foundation`。提供 reward hacking 的 correlation-breakdown 形式化定义，直接框架化 ISR genuine rate 降低现象。\n\n### Related Work section 可引用的具体 claim\n\n1. **Goodhart framing (Discussion section)**:\n   > Our finding that ISR-as-reward produces significantly lower genuine rate than random baseline (6.9% vs 18.4%, Fisher p=0.0002) provides empirical evidence of Goodhart's Law in neurosymbolic RL. Specifically, this constitutes regressional Goodhart (Manheim & Garrabrant, 2019): ISR correlates with genuine structural necessity under the reference distribution, but optimization pressure exploits the gap between proxy and true objective.\n\n2. **Random-vs-structured comparison (Results section)**:\n   > Yang et al. (2025) demonstrate that random rewards nearly match ground-truth rewards in GRPO training. Our results reveal a stronger phenomenon: the structured ISR proxy performs significantly *worse* than random, suggesting that ISR's systematic bias actively misleads optimization into high-ISR-low-genuine regions of the policy space.\n\n3. **Capability-exploitation linkage (Discussion section)**:\n   > The ISR-trained model exhibits the capability-exploitation tradeoff identified by Pan et al. (2022): greater optimization capability enables more effective exploitation of reward misspecification. The random baseline, lacking ISR gradient signal, cannot exploit ISR's structural gaps and thus preserves higher genuine formalization diversity.\n\n4. **Formal reward hacking definition (Related Work)**:\n   > Under the correlated-proxy framework of Laidlaw et al. (2025), ISR constitutes a proxy whose correlation with genuine quality breaks down under GRPO optimization, yielding a policy with lower true reward than the reference policy—the formal definition of reward hacking.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01Go1bd2FCMgkrTXSmnoNq7A`</summary>

```json
{
  "name": "inc05_literature_linkage",
  "type": "report",
  "description": "INC-05 统计发现的文献联动：ISR genuine 6.9% vs Random 18.4% (p=0.0002) 与 Goodhart's Law / reward hacking 文献的映射关系，含 4 篇核心论文和论文写作建议 claim",
  "project": "solver-trace-ablation",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/inc05_literature_linkage.md",
  "tags": [
    "inc-05",
    "literature",
    "goodhart",
    "reward-hacking",
    "fisher-test"
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
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "8ddaeaf9-dd2b-49c0-b588-f63070afae9b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MZgBdZRRMMQHmokFyR5NZj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3354,
      "cache_read_input_tokens": 59770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3354
      },
      "output_tokens": 46,
      "service_tier": "standard",
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

_source line 60 · 2026-05-15T14:12:01.212Z_

<details><summary>↩ Tool result · `toolu_01Go1bd2FCMgkrTXSmnoNq7A`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_880127\", \"name\": \"inc05_literature_linkage\", \"type\": \"report\", \"description\": \"INC-05 统计发现的文献联动：ISR genuine 6.9% vs Random 18.4% (p=0.0002) 与 Goodhart's Law / reward hacking 文献的映射关系，含 4 篇核心论文和论文写作建议 claim\", \"path\": \"projects/solver-trace-ablation/artifacts/_project/report/inc05_literature_linkage.md\", \"url\": null, \"project\": \"solver-trace-ablation\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T14:12:00.986498+00:00\", \"tags\": [\"inc-05\", \"literature\", \"goodhart\", \"reward-hacking\", \"fisher-test\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "b8e8e93c-5dbb-465f-94e6-09ccc9c767e4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260515_880127\\\", \\\"name\\\": \\\"inc05_literature_linkage\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"INC-05 统计发现的文献联动：ISR genuine 6.9% vs Random 18.4% (p=0.0002) 与 Goodhart's Law / reward hacking 文献的映射关系，含 4 篇核心论文和论文写作建议 claim\\\", \\\"path\\\": \\\"projects/solver-trace-ablation/artifacts/_project/report/inc05_literature_linkage.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"solver-trace-ablation\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-15T14:12:00.986498+00:00\\\", \\\"tags\\\": [\\\"inc-05\\\", \\\"literature\\\", \\\"goodhart\\\", \\\"reward-hacking\\\", \\\"fisher-test\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_880127\", \"name\": \"inc05_literature_linkage\", \"type\": \"report\", \"description\": \"INC-05 统计发现的文献联动：ISR genuine 6.9% vs Random 18.4% (p=0.0002) 与 Goodhart's Law / reward hacking 文献的映射关系，含 4 篇核心论文和论文写作建议 claim\", \"path\": \"projects/solver-trace-ablation/artifacts/_project/report/inc05_literature_linkage.md\", \"url\": null, \"project\": \"solver-trace-ablation\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T14:12:00.986498+00:00\", \"tags\": [\"inc-05\", \"literature\", \"goodhart\", \"reward-hacking\", \"fisher-test\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 61_

产出已注册。核心结论：

**4 篇论文映射到 INC-05 发现**：
1. **Laidlaw et al. (2025) "Correlated Proxies"** — **新，需加入 literature_map**。ICLR 2025 Spotlight，提供 reward hacking 的 correlation-breakdown 形式化定义，直接框架化"ISR 优化后 genuine rate 低于 random baseline"。
2. **Yang et al. (2025) "Spurious Rewards"** — 已在 lit map。我们的发现是其强化版：不是 random ≈ truth，而是 structured < random。
3. **Manheim & Garrabrant (2019)** — 已在 lit map，但当前标注为 extremal Goodhart；INC-05 更准确映射到 **regressional Goodhart**（noise exploitation, 无需 distributional shift）。
4. **Pan et al. (2022)** — 已在 lit map。"more capable agents exploit misspecifications more" 直接解释为何 ISR-optimized model 比 random baseline 的 genuine rate 更低。

产出文件含 4 条可直接用于论文的 suggested claims。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "uuid": "df1ce669-d6e9-4cce-a945-5f06d3761629",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AqRZZvxvmHyp2pdrjQVXUJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 63124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 632
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

_source line 62_

产出已注册。核心结论：

**4 篇论文映射到 INC-05 发现**：
1. **Laidlaw et al. (2025) "Correlated Proxies"** — **新，需加入 literature_map**。ICLR 2025 Spotlight，提供 reward hacking 的 correlation-breakdown 形式化定义，直接框架化"ISR 优化后 genuine rate 低于 random baseline"。
2. **Yang et al. (2025) "Spurious Rewards"** — 已在 lit map。我们的发现是其强化版：不是 random ≈ truth，而是 structured < random。
3. **Manheim & Garrabrant (2019)** — 已在 lit map，但当前标注为 extremal Goodhart；INC-05 更准确映射到 **regressional Goodhart**（noise exploitation, 无需 distributional shift）。
4. **Pan et al. (2022)** — 已在 lit map。"more capable agents exploit misspecifications more" 直接解释为何 ISR-optimized model 比 random baseline 的 genuine rate 更低。

产出文件含 4 条可直接用于论文的 suggested claims。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 216288,
  "duration_api_ms": 289658,
  "num_turns": 21,
  "stop_reason": "end_turn",
  "session_id": "aa4ff852-75c3-4edb-a551-d1739a37945e",
  "total_cost_usd": 1.29560275,
  "usage": {
    "input_tokens": 2044,
    "cache_creation_input_tokens": 51915,
    "cache_read_input_tokens": 494624,
    "output_tokens": 7349,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 51915,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 333,
        "cache_read_input_tokens": 63124,
        "cache_creation_input_tokens": 632,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 632
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 336607,
      "outputTokens": 8654,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 15,
      "costUSD": 0.5298769999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 2044,
      "outputTokens": 7349,
      "cacheReadInputTokens": 494624,
      "cacheCreationInputTokens": 51915,
      "webSearchRequests": 0,
      "costUSD": 0.7657257500000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "e8b5c3e4-cf8c-425e-a48e-38009a1a648d"
}
```

</details>

---
