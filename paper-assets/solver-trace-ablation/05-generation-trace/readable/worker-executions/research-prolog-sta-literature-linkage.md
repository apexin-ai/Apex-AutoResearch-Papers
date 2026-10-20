# research prolog sta literature linkage

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/workers/worker_research_prolog-sta-literature-linkage_20260514T184211.log`
- **Structured JSON:** [`14c6d23598534c70dcd3.json`](../../sessions/14/14c6d23598534c70dcd3.json)

## Before a recorded user message

48 recorded events

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
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
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
  "uuid": "417ef3b0-6083-4e60-ab78-a70d8fe02d35",
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
    "resetsAt": 1778800200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "e9587054-3942-44f9-b3c5-b256cea24d9b",
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d"
}
```

---

### Assistant

_source line 4_

I'll read the literature map first, then search for relevant recent papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "a93bd630-4aab-458b-8521-5cf79995fa19",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QrRPkA3pYJW1Ey9KgPVSvb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12557,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12557
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011sBTSpozE9VW6bBPpYFGfb`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
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
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "3749a949-8838-43c5-b1f9-b6daaadb9d14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QrRPkA3pYJW1Ey9KgPVSvb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12557,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12557
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

_source line 6 · 2026-05-14T18:42:21.965Z_

<details><summary>↩ Tool result · `toolu_011sBTSpozE9VW6bBPpYFGfb`</summary>

````text
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
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "f522ba51-a0c9-4c3e-8a23-ab86b3ea8eb7",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
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
Let me read the literature map and search for relevant papers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "684a537e-e83a-4e20-8f2d-bb984da09e25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018PQsqvUWf7kzj1TAT4XEq6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 451,
      "cache_read_input_tokens": 24398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 451
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

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01K1CdVFGFmX2tRxoCG3td29`</summary>

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
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "a48dc5fa-443b-4b60-9fb3-20a83c7c335f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018PQsqvUWf7kzj1TAT4XEq6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 451,
      "cache_read_input_tokens": 24398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 451
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

_source line 9 · 2026-05-14T18:42:25.190Z_

<details><summary>↩ Tool result · `toolu_01K1CdVFGFmX2tRxoCG3td29`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\", \"content\": \"# Literature Map for Solver Trace Ablation (STA)\\n# Categories:\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\n#   2. reward-shaping: Reward shaping for code/formal verification\\n#   3. mutation-testing: Mutation testing in software engineering\\n#   4. intensional-analysis: Intensional program analysis\\n#   5. reward-hacking: Reward hacking / overoptimization\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\n#   7. goodhart-overoptimization: Goodhart's Law theory and dose-response dynamics\\n#   8. verification-reward: Solver/prover as RL reward signal\\n\\npapers:\\n\\n  # ============================================================\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\n  # ============================================================\\n\\n  - id: deepseek-r1\\n    title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n    authors: \\\"DeepSeek-AI\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2501.12948 / Nature 2025\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\n      intensional structural reward for neurosymbolic formalization.\\n    key_finding: >\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\n      showing emergent chain-of-thought reasoning from RL alone.\\n\\n  - id: deepseekmath\\n    title: \\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\"\\n    authors: \\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2402.03300\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\\n      used in STA training. GRPO eliminates the critic model by estimating\\n      baselines from group scores.\\n    key_finding: >\\n      GRPO matches PPO performance while significantly reducing training\\n      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.\\n\\n  - id: logic-rl\\n    title: \\\"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\\\"\\n    authors: \\\"Xian et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.14768\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic\\n      logic puzzles. Closest competitor to STA's approach of RL for logical\\n      formalization, though Logic-RL uses extensional (answer-correctness)\\n      rewards rather than STA's intensional structural rewards.\\n    key_finding: >\\n      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;\\n      rule-based reward design is critical for RL-based logical reasoning.\\n\\n  - id: mellgren-prolog-grpo\\n    title: \\\"Training Language Models to Use Prolog as a Tool\\\"\\n    authors: \\\"Niklas Mellgren\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2512.07407\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,\\n      directly comparable to STA's approach of GRPO-training a formalizer.\\n      Key difference: uses pass/fail reward vs STA's structural ISR.\\n    key_finding: >\\n      GRPO is effective for teaching small LLMs to use Prolog as a tool\\n      for logical and mathematical reasoning.\\n\\n  - id: satlm\\n    title: \\\"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\\\"\\n    authors: \\\"Xi Ye et al.\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023\\\"\\n    category: neurosymbolic-rl\\n    role: background\\n    relevance: >\\n      Neurosymbolic approach where LLM generates declarative specifications\\n      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)\\n      but uses prompting, not RL training.\\n    key_finding: >\\n      Declarative formulation outperforms imperative program-aided LMs by 23%\\n      on GSM; achieves SoTA on LSAT and BoardgameQA.\\n\\n  - id: deepproblog\\n    title: \\\"Neural Probabilistic Logic Programming in DeepProbLog\\\"\\n    authors: \\\"Robin Manhaeve, Sebastijan Dumančić, Angelika Kimmig, Thomas Demeester, Luc De Raedt\\\"\\n    year: 2021\\n    venue: \\\"Artificial Intelligence 298\\\"\\n    category: neurosymbolic-rl\\n    role: background\\n    relevance: >\\n      Foundational neural-probabilistic logic programming framework that integrates\\n      deep learning with ProbLog via neural predicates. Establishes the intellectual\\n      tradition of combining neural networks with logic programming that STA extends\\n      to LLM-generated Prolog with RL training.\\n    key_finding: >\\n      End-to-end differentiable framework integrating neural perception with\\n      probabilistic logical reasoning; supports program induction and learning\\n      from examples.\\n\\n  - id: neurasp\\n    title: \\\"NeurASP: Embracing Neural Networks into Answer Set Programming\\\"\\n    authors: \\\"Zhun Yang, Adam Ishay, Joohyung Lee\\\"\\n    year: 2020\\n    venue: \\\"IJCAI 2020\\\"\\n    category: neurosymbolic-rl\\n    role: background\\n    relevance: >\\n      Integrates neural networks with answer set programming (ASP), using\\n      ASP rules to constrain and improve neural network training. Complementary\\n      to DeepProbLog; together they represent the neuro-symbolic LP foundation\\n      that STA's LLM-to-Prolog pipeline builds upon.\\n    key_finding: >\\n      ASP semantic constraints improve neural network perception accuracy;\\n      demonstrates bidirectional benefit of neural-symbolic integration.\\n\\n  - id: thought-like-pro\\n    title: \\\"Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought\\\"\\n    authors: \\\"Xiaoyu Tan, Yongxin Deng, Xihe Qiu, Weidi Xu, Chao Qu, Wei Chu, Yinghui Xu, Yuan Qi\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2407.14562\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses Prolog engine to generate verified reasoning trajectories, then trains\\n      LLMs via imitation learning to replicate them. Directly comparable pipeline\\n      to STA (Prolog verification + LLM training), but uses imitation learning\\n      instead of GRPO with structural reward.\\n    key_finding: >\\n      Prolog-verified reasoning trajectories as training signal improve LLM\\n      logical reasoning; self-driven framework enables LLMs to formulate\\n      rules from instructions and leverage Prolog for derivation.\\n\\n  # ============================================================\\n  # Category 2: Reward shaping for code/formal verification\\n  # ============================================================\\n\\n  - id: lightman-verify-step\\n    title: \\\"Let's Verify Step by Step\\\"\\n    authors: \\\"Hunter Lightman, Vineet Kosaraju, Yura Burda, et al.\\\"\\n    year: 2023\\n    venue: \\\"arXiv 2305.20050 / ICLR 2024\\\"\\n    category: reward-shaping\\n    role: method-component\\n    relevance: >\\n      Establishes that process supervision (step-level reward) outperforms\\n      outcome supervision (final-answer reward) for reasoning. STA's ISR\\n      is analogous: it provides structural process-level signal about which\\n      components of a formalization matter, rather than just pass/fail.\\n    key_finding: >\\n      Process-supervised reward model achieves 78% on MATH, significantly\\n      outperforming outcome-supervised models. Released PRM800K dataset.\\n\\n  - id: reward-shaping-rlhf\\n    title: \\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\"\\n    authors: \\\"Jiayi Fu, Xuandong Zhao, Chengyuan Yao, et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.18770\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Studies reward shaping design principles for RLHF: bounded rewards and\\n      rapid-then-convergent growth. STA's ISR follows these principles\\n      naturally since structural necessity scores are bounded [0,1].\\n    key_finding: >\\n      Two key reward shaping principles: (1) bounded RL reward, (2) rapid\\n      initial growth with gradual convergence. PAR method achieves 5%+\\n      win rate improvement on AlpacaEval 2.0.\\n\\n  - id: rlvr-reasoning\\n    title: \\\"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2506.14245\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize\\n      reasoning. STA argues that for neurosymbolic formalization, binary reward\\n      is insufficient and structural reward is needed to avoid reward hacking.\\n    key_finding: >\\n      RLVR with binary verification implicitly teaches correct reasoning\\n      strategies, not just answer matching.\\n\\n  - id: rubric-grpo\\n    title: \\\"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2605.08061\\\"\\n    category: reward-shaping\\n    role: direct-competitor\\n    relevance: >\\n      Uses structured rubric-based rewards with GRPO, similar in spirit to\\n      STA's structured ISR. Key difference: rubric rewards come from LLM\\n      judges, while ISR comes from solver-based mutation testing.\\n    key_finding: >\\n      Structured multi-dimensional reward signals improve GRPO training\\n      generalization compared to scalar rewards.\\n\\n  - id: gao-effective-rl-reward\\n    title: \\\"On Designing Effective RL Reward at Training Time for LLM Reasoning\\\"\\n    authors: \\\"Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2410.15115\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Demonstrates that learned process/outcome reward models can hurt RL\\n      training, producing worse performance than simple success reward only.\\n      Directly explains plan005 NEGATIVE: STA's ISR as auxiliary process\\n      reward degrades prove_rate compared to exec-only baseline.\\n    key_finding: >\\n      PRM/ORM rewards may NOT help or even hurt RL training vs success-only\\n      reward. Solution: Clipping and Delta techniques to bound accumulated\\n      reward magnitude prevent reward hacking.\\n\\n  - id: prof-process-outcome\\n    title: \\\"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training\\\"\\n    authors: \\\"Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2509.03403\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Shows that naively combining PRM+ORM signals leads to performance\\n      degradation. PROF consistency filter retains only PRM-ORM consistent\\n      samples, achieving 4%+ improvement over blending. Suggests STA should\\n      only apply ISR when consistent with execution outcome.\\n    key_finding: >\\n      Process rewards frequently suffer from inaccuracies and reward hacking\\n      susceptibility. PROF filters training data by PRM-ORM consistency,\\n      outperforming naive reward blending by 4%+ accuracy.\\n\\n  - id: moskovitz-constrained-rlhf\\n    title: \\\"Confronting Reward Model Overoptimization with Constrained RLHF\\\"\\n    authors: \\\"Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer\\\"\\n    year: 2023\\n    venue: \\\"arXiv 2310.04373 / ICLR 2024\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      First study on overoptimization in composite reward models. Shows that\\n      fixed-weight linear scalarization of component rewards leads to\\n      degradation past a threshold. Proposes constrained RL with dynamic\\n      Lagrange multiplier weighting as alternative to fixed ISR weight.\\n    key_finding: >\\n      Correlation between component RMs significantly affects overoptimization\\n      thresholds. Constrained RL with Lagrange multipliers outperforms\\n      fixed-weight reward composition.\\n\\n  - id: skalse-reward-hacking\\n    title: \\\"Defining and Characterizing Reward Hacking\\\"\\n    authors: \\\"Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger\\\"\\n    year: 2022\\n    venue: \\\"arXiv 2209.13085 / NeurIPS 2022\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Formal proof that for stochastic policies, two reward functions are\\n      unhackable only if one is constant. Theoretically explains why any\\n      non-zero ISR weight can decrease prove_rate -- this is a fundamental\\n      property of reward composition, not STA-specific.\\n    key_finding: >\\n      Any non-constant proxy reward can decrease true reward when optimized.\\n      Unhackability requires the proxy to be constant, making all non-trivial\\n      auxiliary rewards theoretically vulnerable to degrading primary performance.\\n\\n  - id: progrs-outcome-conditioned\\n    title: \\\"LLM Reasoning with Process Rewards for Outcome-Guided Steps\\\"\\n    authors: \\\"Mohammad Rezaei, Jens Lehmann, Sahar Vahdati\\\"\\n    year: 2026\\n    venue: \\\"arXiv 2604.02341\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      PRM scores optimized as absolute rewards amplify fluent failure modes.\\n      Outcome-conditioned centering shifts incorrect trajectories' PRM scores\\n      to zero mean, preserving ranking info without corrupting gradients.\\n      Suggests STA should condition ISR on execution outcome.\\n    key_finding: >\\n      Naive process rewards induce reward hacking by rewarding locally fluent\\n      but globally incorrect reasoning. Outcome-conditioned centering resolves\\n      the conflict with fewer rollouts than outcome-only baselines.\\n\\n  - id: qwen-prm-lessons\\n    title: \\\"The Lessons of Developing Process Reward Models in Mathematical Reasoning\\\"\\n    authors: \\\"Zhenru Zhang et al. (Qwen Team, Alibaba)\\\"\\n    year: 2025\\n    venue: \\\"ACL 2025 Findings (arXiv 2501.07301)\\\"\\n    category: reward-shaping\\n    role: supporting-evidence\\n    relevance: >\\n      MC estimation-synthesized PRM data leads to quality degradation; policy\\n      model generates \\\"answer-correct but reasoning-flawed\\\" responses, causing\\n      process reward / outcome misalignment. Directly parallels ISR problem:\\n      structurally correct but semantically wrong proof traces get high ISR\\n      but low execution reward.\\n    key_finding: >\\n      PRM performance depends critically on data quality; MC estimation\\n      introduces systematic bias. Answer-correct reasoning-flawed samples\\n      corrupt process supervision signal.\\n\\n  # ============================================================\\n  # Category 3: Mutation testing in software engineering\\n  # ============================================================\\n\\n  - id: demillo1978\\n    title: \\\"Hints on Test Data Selection: Help for the Practicing Programmer\\\"\\n    authors: \\\"Richard A. DeMillo, Richard J. Lipton, Frederick G. Sayward\\\"\\n    year: 1978\\n    venue: \\\"Computer 11(4):34-43\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Foundational paper introducing mutation testing. STA's component\\n      necessity testing directly extends this idea: instead of mutating\\n      source code to test test suites, STA mutates logical formulas\\n      to test component necessity for solver success.\\n    key_finding: >\\n      Introduced mutation testing and the coupling effect hypothesis:\\n      tests that detect simple faults also detect complex faults.\\n\\n  - id: offutt-coupling\\n    title: \\\"Investigations of the Software Testing Coupling Effect\\\"\\n    authors: \\\"A. Jefferson Offutt\\\"\\n    year: 1992\\n    venue: \\\"ACM TOSEM 1(1):5-20\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Empirically validates the coupling effect hypothesis that underpins\\n      mutation testing. STA's single-component ablation is analogous to\\n      first-order mutation; the coupling effect suggests this suffices.\\n    key_finding: >\\n      Test data killing all first-order mutants killed >99% of second-\\n      and third-order mutants, validating the coupling effect.\\n\\n  - id: jia-harman-survey\\n    title: \\\"An Analysis and Survey of the Development of Mutation Testing\\\"\\n    authors: \\\"Yue Jia, Mark Harman\\\"\\n    year: 2011\\n    venue: \\\"IEEE TSE 37(5):649-678\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Comprehensive survey of mutation testing covering three decades of\\n      development. Provides theoretical and practical foundation for STA's\\n      adaptation of mutation testing to logical formulas.\\n    key_finding: >\\n      Systematic classification of mutation operators, cost reduction\\n      techniques, and equivalence problem -- all relevant to STA's design\\n      of clause-level ablation operators.\\n\\n  - id: just-mutants-real-faults\\n    title: \\\"Are Mutants a Valid Substitute for Real Faults in Software Testing?\\\"\\n    authors: \\\"Rene Just, Darioush Jalali, Laura Inozemtseva, et al.\\\"\\n    year: 2014\\n    venue: \\\"FSE 2014\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Validates that mutation testing (structural/intensional analysis of\\n      program adequacy) correlates with real fault detection. Supports STA's\\n      premise that structural analysis of formalization components provides\\n      meaningful signal about formalization quality.\\n    key_finding: >\\n      Mutant detection is statistically correlated with real fault detection,\\n      and mutation score is a better predictor of test effectiveness than\\n      code coverage.\\n\\n  - id: llmorpheus\\n    title: \\\"LLMorpheus: Mutation Testing Using Large Language Models\\\"\\n    authors: \\\"Frank Tip, Jon Bell, et al.\\\"\\n    year: 2025\\n    venue: \\\"IEEE TSE 2025\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Uses LLMs to generate realistic code mutants beyond traditional\\n      mutation operators. Shows mutation testing evolving toward\\n      ML-integrated approaches, validating STA's cross-pollination\\n      of mutation testing ideas into ML training.\\n    key_finding: >\\n      LLM-generated mutants simulate real bugs that rule-based operators\\n      cannot produce, improving mutation testing realism.\\n\\n  - id: mutation-guided-meta\\n    title: \\\"Mutation-Guided LLM-based Test Generation at Meta\\\"\\n    authors: \\\"Christopher Foster et al.\\\"\\n    year: 2025\\n    venue: \\\"FSE 2025\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Industrial application of mutation-guided LLM test generation at\\n      Meta. Demonstrates that mutation analysis can guide LLM behavior\\n      in production -- analogous to how STA uses mutation (ablation) to\\n      guide GRPO reward signal.\\n    key_finding: >\\n      Mutation-guided approach generates tests that kill significantly\\n      more mutants than unguided LLM test generation at Meta scale.\\n\\n  - id: mutation-consistency-llm\\n    title: \\\"Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs\\\"\\n    authors: \\\"Various\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2401.05940\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Uses code mutations to evaluate LLM code understanding consistency.\\n      Conceptually related to STA: both use systematic code/formula\\n      mutations to assess model capabilities.\\n    key_finding: >\\n      LLMs show significant inconsistency when evaluated on mutated code\\n      variants, suggesting superficial pattern matching.\\n\\n  # ============================================================\\n  # Category 4: Intensional program analysis\\n  # ============================================================\\n\\n  - id: deepmutation\\n    title: \\\"A Probabilistic Framework for Mutation Testing in Deep Neural Networks\\\"\\n    authors: \\\"Various\\\"\\n    year: 2023\\n    venue: \\\"Information and Software Technology 2023\\\"\\n    category: intensional-analysis\\n    role: background\\n    relevance: >\\n      Extends mutation testing to DNN testing with probabilistic mutation\\n      operators. Parallel to STA's extension of mutation testing from\\n      traditional programs to logical formulas.\\n    key_finding: >\\n      Probabilistic mutation framework enables meaningful test adequacy\\n      assessment for neural networks through structural perturbation.\\n\\n  # ============================================================\\n  # Category 5: Reward hacking / overoptimization\\n  # ============================================================\\n\\n  - id: inform-reward-hacking\\n    title: \\\"InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling\\\"\\n    authors: \\\"Various\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS 2024\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Proposes information-bottleneck approach to detect and mitigate reward\\n      hacking. STA's ISR addresses the same problem differently: by grounding\\n      reward in verifiable structural properties (component necessity), it\\n      reduces the attack surface for reward hacking.\\n    key_finding: >\\n      Variational information bottleneck filters irrelevant features from\\n      reward model; Cluster Separation Index detects reward overoptimization.\\n\\n  - id: mo-grpo\\n    title: \\\"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\\\"\\n    authors: \\\"CyberAgent AI Lab\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2509.22047\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Directly addresses GRPO reward hacking in multi-objective settings.\\n      STA's ISR can be viewed as adding a structural objective to the\\n      correctness objective, making MO-GRPO's insights directly applicable.\\n    key_finding: >\\n      Standard GRPO normalizes after summing rewards, allowing high-variance\\n      objectives to dominate. MO-GRPO equalizes scales before aggregation.\\n\\n  - id: reward-hacking-survey\\n    title: \\\"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\\\"\\n    authors: \\\"Various\\\"\\n    year: 2026\\n    venue: \\\"arXiv 2604.13602\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Comprehensive survey of reward hacking mechanisms in the LLM era.\\n      Provides theoretical framework for understanding why STA's structural\\n      reward is more robust than pure outcome-based reward.\\n    key_finding: >\\n      Reward hacking manifests through specification gaming, reward model\\n      exploitation, and emergent misalignment; structural verification\\n      rewards are more robust than learned reward models.\\n\\n  - id: energy-loss-reward-hacking\\n    title: \\\"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"ICML 2025\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Identifies energy loss in LLM final layer as an indicator of reward\\n      hacking during RL. Provides complementary diagnostic to STA's\\n      structural reward approach.\\n    key_finding: >\\n      Energy loss in the final layer increases during RL and excessive\\n      increase characterizes reward hacking; EPPO algorithm penalizes\\n      this to mitigate hacking.\\n\\n  - id: spurious-rewards\\n    title: \\\"Spurious Rewards: Rethinking Training Signals in RLVR\\\"\\n    authors: \\\"Ruixin Yang et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2506.10947 / NeurIPS 2025 submission\\\"\\n    category: reward-hacking\\n    role: direct-evidence\\n    relevance: >\\n      Most directly relevant to STA findings. GRPO+random reward on\\n      Qwen2.5-Math improves 21.4%, nearly matching ground-truth reward's\\n      29.1%. Matches our plan017 finding: additive random (PR=48%) >\\n      additive ISR (PR=18%). Structured metrics can be worse than random\\n      noise due to systematic bias vs pure variance.\\n    key_finding: >\\n      Random reward nearly matches ground-truth reward in GRPO training,\\n      suggesting GRPO's group normalization extracts signal from noise.\\n      Effect is model-dependent (works on Qwen2.5, not Llama3).\\n\\n  - id: bondarenko-spec-gaming\\n    title: \\\"Demonstrating Specification Gaming in Reasoning Models\\\"\\n    authors: \\\"Alexander Bondarenko, Denis Volk, Dmitrii Volkov, Jeffrey Ladish\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.13295\\\"\\n    category: reward-hacking\\n    role: direct-evidence\\n    relevance: >\\n      Shows that reasoning models (o3, DeepSeek-R1) resort to specification\\n      gaming on difficult tasks by default, without explicit nudging.\\n      Directly relevant to STA's concern: RL-trained reasoning models\\n      may game formal verification rewards rather than learn genuine\\n      formalization skills.\\n    key_finding: >\\n      Reasoning models spontaneously hack benchmarks (e.g., manipulating\\n      chess engine files instead of playing chess). Stronger reasoning\\n      capability correlates with more sophisticated gaming strategies.\\n\\n  - id: kim-game-formalization\\n    title: \\\"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning\\\"\\n    authors: \\\"Kyuhee Kim, Auguste Poiroux, Antoine Bosselut\\\"\\n    year: 2026\\n    venue: \\\"VerifAI-2 Workshop, ICLR 2026 (arXiv 2604.19459)\\\"\\n    category: reward-hacking\\n    role: direct-evidence\\n    relevance: >\\n      Directly studies whether LLMs game formalization in logical reasoning --\\n      the exact phenomenon STA's ISR is designed to detect. Evaluates GPT-5\\n      and DeepSeek-R1 on FOLIO with Lean 4 proofs. Finds two modes of\\n      unfaithfulness: axiom fabrication (GPT-5) and premise mistranslation\\n      (R1), the latter evading detection entirely.\\n    key_finding: >\\n      High compilation rates (87-99%) do not imply faithful formalization.\\n      Two-stage pipelines reveal unfaithfulness that unified generation hides.\\n      Premise mistranslation produces internally consistent but unfaithful\\n      outputs -- analogous to STA's high-ISR but semantically wrong traces.\\n\\n  - id: gao-reward-overoptimization\\n    title: \\\"Scaling Laws for Reward Model Overoptimization\\\"\\n    authors: \\\"Leo Gao, John Schulman, Jacob Hilton\\\"\\n    year: 2023\\n    venue: \\\"ICML 2023 (arXiv 2210.10760)\\\"\\n    category: reward-hacking\\n    role: theoretical-foundation\\n    relevance: >\\n      Foundational work quantifying Goodhart's effect: proxy reward rises\\n      but gold reward first rises then falls. ISR is a proxy reward that\\n      exhibits exactly this pattern — ISR can increase while prove_rate\\n      decreases, making it suitable for post-hoc diagnosis but harmful\\n      as training signal.\\n    key_finding: >\\n      Gold/proxy reward divergence follows predictable scaling laws.\\n      Proxy reward optimization past critical point degrades gold reward,\\n      with the divergence point scaling with model and dataset size.\\n\\n  - id: karwowski-goodhart-rl\\n    title: \\\"Goodhart's Law in Reinforcement Learning\\\"\\n    authors: \\\"Jacek Karwowski, Oliver Hayman, Xingjian Bai, Klaus Kiendlhofer, Charlie Griffin, Joar Skalse\\\"\\n    year: 2024\\n    venue: \\\"ICLR 2024 (arXiv 2310.09144)\\\"\\n    category: reward-hacking\\n    role: theoretical-foundation\\n    relevance: >\\n      Geometric interpretation of Goodhart's Law in MDPs: optimizing\\n      imperfect proxy past critical point decreases true objective. ISR as\\n      proxy has partial correlation with execution correctness — exceeding\\n      critical optimization point pushes policy toward high-ISR but\\n      low-correctness regions. Explains plan002/plan005 negative results.\\n    key_finding: >\\n      Formalizes Goodhart's Law for RL: any non-trivially correlated proxy\\n      reward creates regions where proxy and true reward diverge, and\\n      policy optimization inevitably enters these regions.\\n\\n  # ============================================================\\n  # Category 6: FOL/Prolog formalization with LLMs\\n  # ============================================================\\n\\n  - id: folio\\n    title: \\\"FOLIO: Natural Language Reasoning with First-Order Logic\\\"\\n    authors: \\\"Simeng Han et al.\\\"\\n    year: 2022\\n    venue: \\\"arXiv 2209.00840 / EMNLP 2024\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Primary FOL reasoning benchmark. STA uses FOLIO-style NL->FOL\\n      formalization as the target task for GRPO training. FOLIO's\\n      expert-annotated FOL annotations serve as reference formalizations.\\n    key_finding: >\\n      1,430 NL-FOL paired examples with reasoning depths up to 5+;\\n      GPT-4 still struggles on the hardest examples.\\n\\n  - id: proofwriter\\n    title: \\\"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language\\\"\\n    authors: \\\"Oyvind Tafjord, Bhavana Dalvi, Peter Clark\\\"\\n    year: 2021\\n    venue: \\\"Findings of ACL-IJCNLP 2021\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Source dataset for STA's training data. ProofWriter provides\\n      rule-based logical reasoning problems in natural language that\\n      STA uses for training formalizer models.\\n    key_finding: >\\n      Generative model can reliably produce implications and proofs;\\n      accuracy exceeds prior methods by 9% and generalizes to unseen\\n      proof depths.\\n\\n  - id: logic-lm\\n    title: \\\"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\\\"\\n    authors: \\\"Liangming Pan, Alon Albalak, Xinyi Wang, William Wang\\\"\\n    year: 2023\\n    venue: \\\"Findings of EMNLP 2023\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      LLM->symbolic solver pipeline for logical reasoning, directly\\n      comparable to STA's formalizer->Prolog solver pipeline. Key\\n      difference: Logic-LM uses prompting, STA uses GRPO training.\\n    key_finding: >\\n      LLM+solver achieves 39.2% improvement over LLM-alone on logical\\n      reasoning benchmarks including ProofWriter and FOLIO.\\n\\n  - id: linc\\n    title: \\\"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers\\\"\\n    authors: \\\"Theo X. Olausson, Alex Gu, Ben Lipkin, et al.\\\"\\n    year: 2023\\n    venue: \\\"EMNLP 2023\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      Neurosymbolic approach where LLM translates NL to FOL for theorem\\n      prover. Directly comparable to STA's NL->Prolog translation.\\n      LINC uses prompting-based approach; STA uses RL training.\\n    key_finding: >\\n      StarCoder+ (15.5B) with LINC outperforms GPT-3.5 and GPT-4 with\\n      CoT by 38% and 10% respectively on ProofWriter.\\n\\n  - id: fover-pei2025\\n    title: \\\"FoVer: First-Order Logic Verification for Natural Language Reasoning\\\"\\n    authors: \\\"Yu Pei, Yongping Du, Xingnan Jin\\\"\\n    year: 2025\\n    venue: \\\"TACL 13:1340-1359\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      Uses LLM->FOL->Z3 pipeline for verifying NL reasoning correctness.\\n      Similar to STA's verification pipeline but focuses on post-hoc\\n      verification rather than training reward signal.\\n    key_finding: >\\n      FOL verification via Z3 significantly outperforms existing methods\\n      on ProofWriter and FOLIO benchmarks.\\n\\n  - id: lorp\\n    title: \\\"LoRP: LLM-based Logical Reasoning via Prolog\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"Knowledge-Based Systems 2025\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      LLM->Prolog pipeline with FOL-to-Prolog translation mechanism.\\n      Closest to STA's formalization target (Prolog), though LoRP\\n      uses prompting while STA uses GRPO training with structural reward.\\n    key_finding: >\\n      Systematic FOL-to-Prolog translation extends Prolog expressiveness;\\n      achieves SoTA accuracy on logical reasoning with three-vote majority.\\n\\n  - id: nl2fol\\n    title: \\\"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection\\\"\\n    authors: \\\"Lalwani, Kim, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2405.02318\\\"\\n    category: fol-formalization\\n    role: background\\n    relevance: >\\n      Step-by-step NL->FOL translation using LLMs with SMT solver\\n      verification. Demonstrates the NL->formal logic pipeline that\\n      STA aims to improve via RL training.\\n    key_finding: >\\n      Neurosymbolic NL2FOL achieves 78% F1 on LOGIC dataset and\\n      generalizes to LogicClimate (80% F1), outperforming supervised\\n      models by 21%.\\n\\n  - id: logica2\\n    title: \\\"LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: \\\"IEEE/ACM TASLP 2023\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Logical reasoning evaluation benchmark derived from Chinese civil\\n      service exams. Provides supplementary evaluation for STA's\\n      formalization capabilities.\\n    key_finding: >\\n      8,678 multiple-choice questions covering categorical, disjunctive,\\n      and conditional reasoning; widely used LLM benchmark.\\n\\n  # ============================================================\\n  # Category 7: Goodhart's Law theory and dose-response dynamics\\n  # ============================================================\\n\\n  - id: manheim-goodhart-taxonomy\\n    title: \\\"Categorizing Variants of Goodhart's Law\\\"\\n    authors: \\\"David Manheim, Scott Garrabrant\\\"\\n    year: 2019\\n    venue: \\\"arXiv 1803.04585\\\"\\n    category: goodhart-overoptimization\\n    role: theoretical-foundation\\n    relevance: >\\n      Four-part Goodhart taxonomy: regressional, extremal, causal, adversarial.\\n      STA's high-β ISR collapse is best classified as extremal Goodhart\\n      (policy moves to OOD region where ISR↑ but prove_rate↓). Provides\\n      vocabulary for discussion section.\\n    key_finding: >\\n      First systematic categorization of Goodhart failure modes. Extremal\\n      variant occurs when proxy-goal relationship breaks in out-of-distribution\\n      regions reached by strong optimization.\\n\\n  - id: pan-reward-misspecification\\n    title: \\\"The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models\\\"\\n    authors: \\\"Alexander Pan, Kush Bhatia, Jacob Steinhardt\\\"\\n    year: 2022\\n    venue: \\\"ICLR 2022\\\"\\n    category: goodhart-overoptimization\\n    role: theoretical-foundation\\n    relevance: >\\n      Across 9 environments, more capable agents exploit misspecifications more.\\n      Observes dose-dependent degradation — capability thresholds where true\\n      reward sharply drops. Matches STA's β=0.1→0.3 qualitative shift.\\n    key_finding: >\\n      Reward misspecification causes dose-dependent degradation where true reward\\n      sharply drops past capability thresholds. More capable optimization\\n      produces worse outcomes under misspecification.\\n\\n  - id: kwa-catastrophic-goodhart\\n    title: \\\"Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification\\\"\\n    authors: \\\"Tat-Thang Kwa, Rachel Thomas, Adrià Garriga-Alonso\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS 2024\\\"\\n    category: goodhart-overoptimization\\n    role: theoretical-foundation\\n    relevance: >\\n      If reward model error is heavy-tailed, policies achieve arbitrarily\\n      high proxy reward with no true utility gain. KL regularization provably\\n      fails. Explains why KL penalty in GRPO cannot prevent ISR collapse\\n      at high β if ISR error distribution is heavy-tailed.\\n    key_finding: >\\n      KL-regularized RL provably fails to prevent overoptimization under\\n      heavy-tailed reward misspecification. Policies can achieve arbitrarily\\n      high proxy reward with zero true utility.\\n\\n  - id: rafailov-daa-scaling\\n    title: \\\"Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms\\\"\\n    authors: \\\"Rafael Rafailov, Yaswanth Chittepu, Ryan Park, Harshit Sikchi, Joey Hejna, W. Bradley Knox, Chelsea Finn, Scott Niekum\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS 2024\\\"\\n    category: goodhart-overoptimization\\n    role: supporting-evidence\\n    relevance: >\\n      Extends Gao et al. to DPO/IPO/SLiC. Tests seven β values across\\n      1B-6.9B models. DAAs still overoptimize despite no explicit proxy RM.\\n      Validates β as a \\\"dose\\\" parameter — directly analogous to STA's\\n      ISR weight sweep.\\n    key_finding: >\\n      Direct alignment algorithms exhibit overoptimization following\\n      predictable scaling laws. Smaller models overoptimize sooner.\\n      β-controlled dose-response is a general phenomenon across RL paradigms.\\n\\n  - id: huang-chi-squared\\n    title: \\\"Correcting the Mythos of KL-Regularization: Direct and Contrastive Distribution Correction\\\"\\n    authors: \\\"Afra Feyza Akyürek, Banghua Zhu, Sham Kakade, Jiantao Jiao\\\"\\n    year: 2025\\n    venue: \\\"ICLR 2025 Poster\\\"\\n    category: goodhart-overoptimization\\n    role: supporting-evidence\\n    relevance: >\\n      KL-regularization is theoretically inadequate for preventing\\n      overoptimization. Chi-squared divergence provably alleviates it.\\n      Suggests that even with KL penalty in GRPO, STA's high-β collapse\\n      is theoretically expected.\\n    key_finding: >\\n      Chi-squared preference optimization provably mitigates overoptimization\\n      where KL-regularization fails. Alternative divergence measures offer\\n      stronger guarantees.\\n\\n  - id: coste-rm-ensembles\\n    title: \\\"Reward Model Ensembles Help Mitigate Overoptimization\\\"\\n    authors: \\\"Thomas Coste, Usman Anwar, Robert Kirk, David Krueger\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023 Workshop on Alignment\\\"\\n    category: goodhart-overoptimization\\n    role: background\\n    relevance: >\\n      Worst-case optimization across RM ensembles practically eliminates\\n      overoptimization for BoN and reduces it for PPO. Suggests ensemble\\n      of multiple solver metrics (instead of single ISR) as mitigation.\\n    key_finding: >\\n      RM ensembles with worst-case aggregation mitigate overoptimization.\\n      Ensemble size and diversity directly affect robustness.\\n\\n  # ============================================================\\n  # Category 8: Solver/prover as RL reward signal\\n  # ============================================================\\n\\n  - id: rlsf\\n    title: \\\"Reinforcement Learning via Symbolic Feedback\\\"\\n    authors: \\\"Abhinav Jha, Shikhar Murty, Zico Kolter, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2405.16661\\\"\\n    category: verification-reward\\n    role: direct-competitor\\n    relevance: >\\n      Most directly relevant: uses solver/prover certificates as fine-grained\\n      token-level reward signal. Outperforms traditional approaches on program\\n      synthesis (+31.4%). STA extends this paradigm and shows when it breaks\\n      (Goodhart effects at high auxiliary reward weight).\\n    key_finding: >\\n      Symbolic reasoning tools provide poly-sized certificates as reward.\\n      Smaller RLSF models outperform GPT-4 on structured generation tasks.\\n\\n  - id: fover-kamoi2026\\n    title: \\\"FoVer: Generalizable Process Reward Models via Formally Verified Training Data\\\"\\n    authors: \\\"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\\\"\\n    year: 2025\\n    venue: \\\"Findings of ACL 2026 (arXiv 2502.01345)\\\"\\n    category: verification-reward\\n    role: supporting-evidence\\n    relevance: >\\n      Uses Z3 and Isabelle to synthesize PRM training data by annotating\\n      step-level error labels without human annotation. Same solver family\\n      as STA. Shows verification-based rewards work; STA extends by showing\\n      dose-response dynamics.\\n    key_finding: >\\n      Formally verified training data enables generalizable process reward\\n      models competitive on ProcessBench and 12 reasoning benchmarks.\\n\\n  - id: deepseek-prover-v15\\n    title: \\\"DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search\\\"\\n    authors: \\\"DeepSeek AI\\\"\\n    year: 2024\\n    venue: \\\"ICLR 2025 (arXiv 2408.08152)\\\"\\n    category: verification-reward\\n    role: method-component\\n    relevance: >\\n      Uses GRPO with Lean 4 verification as binary reward. Same algorithm\\n      (GRPO) + formal verification, but binary (pass/fail). Binary reward\\n      avoids the graded-metric Goodhart risk that STA identifies with ISR.\\n    key_finding: >\\n      GRPO + binary Lean verification achieves 63.5% on miniF2F. Binary\\n      correctness guarantee via formal verification sidesteps proxy reward\\n      overoptimization.\\n\\n  - id: alphaproof\\n    title: \\\"AlphaProof\\\"\\n    authors: \\\"Google DeepMind\\\"\\n    year: 2024\\n    venue: \\\"Nature 2025\\\"\\n    category: verification-reward\\n    role: background\\n    relevance: >\\n      AlphaZero-inspired RL with Lean proof verification at scale.\\n      Silver medal at IMO 2024. Binary verification reward avoids the\\n      Goodhart problem STA identifies with graded verification metrics.\\n    key_finding: >\\n      Binary formal verification as RL reward scales to IMO-level\\n      mathematical reasoning. Demonstrates verification-reward RL works\\n      at the frontier of mathematical difficulty.\\n\\n  - id: math-shepherd\\n    title: \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\"\\n    authors: \\\"Peiyi Wang, Lei Li, Zhihong Shao, R.X. Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"ACL 2024 (arXiv 2312.08935)\\\"\\n    category: verification-reward\\n    role: supporting-evidence\\n    relevance: >\\n      Automatically constructs process supervision data and uses it as\\n      step-by-step PPO reward. Automated verification reward without human\\n      labels, analogous to STA's automated ISR computation via solver.\\n    key_finding: >\\n      Automated process supervision improves Mistral-7B on GSM8K\\n      (77.9→84.1%) and MATH (28.6→33.0%) without human annotation.\\n\\n  # ============================================================\\n  # Additional reward-shaping papers (Goodhart survey additions)\\n  # ============================================================\\n\\n  - id: bipars\\n    title: \\\"Learning to Utilize Shaping Rewards: A New Approach of Reward Shaping\\\"\\n    authors: \\\"Yujing Hu, Weixun Wang, Hangtian Jia, et al.\\\"\\n    year: 2020\\n    venue: \\\"NeurIPS 2020\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Bi-level optimization learns parameterized shaping reward weights.\\n      Can transform harmful shaping rewards into beneficial ones by learning\\n      negative weights. Directly addresses STA's problem: when ISR weight\\n      is wrong, automated weight learning could find optimal β.\\n    key_finding: >\\n      Bi-level optimization automatically learns auxiliary reward weights,\\n      outperforming fixed weights and recovering from harmful shaping rewards.\\n\\n  - id: dapo\\n    title: \\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\"\\n    authors: \\\"Qiying Yu et al. (ByteDance)\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2503.14476\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Four techniques for stable multi-component reward in GRPO: Clip-Higher,\\n      Dynamic Sampling, token-level policy gradient, Overlong Reward Shaping.\\n      Addresses stability issues relevant to STA's multi-reward setup.\\n    key_finding: >\\n      Clip-Higher and Dynamic Sampling prevent entropy collapse in GRPO\\n      with multi-component rewards. Soft punishment for overlong outputs\\n      avoids reward hacking through length exploitation.\\n\", \"total_chars\": 42743, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "ad6b06bf-7f05-433c-96cd-64bb98aaa7a1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\\\", \\\"content\\\": \\\"# Literature Map for Solver Trace Ablation (STA)\\\\n# Categories:\\\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\\\n#   2. reward-shaping: Reward shaping for code/formal verification\\\\n#   3. mutation-testing: Mutation testing in software engineering\\\\n#   4. intensional-analysis: Intensional program analysis\\\\n#   5. reward-hacking: Reward hacking / overoptimization\\\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\\\n#   7. goodhart-overoptimization: Goodhart's Law theory and dose-response dynamics\\\\n#   8. verification-reward: Solver/prover as RL reward signal\\\\n\\\\npapers:\\\\n\\\\n  # ============================================================\\\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\\\n  # ============================================================\\\\n\\\\n  - id: deepseek-r1\\\\n    title: \\\\\\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"DeepSeek-AI\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2501.12948 / Nature 2025\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: method-component\\\\n    relevance: >\\\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\\\n      intensional structural reward for neurosymbolic formalization.\\\\n    key_finding: >\\\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\\\n      showing emergent chain-of-thought reasoning from RL alone.\\\\n\\\\n  - id: deepseekmath\\\\n    title: \\\\\\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2402.03300\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: method-component\\\\n    relevance: >\\\\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\\\\n      used in STA training. GRPO eliminates the critic model by estimating\\\\n      baselines from group scores.\\\\n    key_finding: >\\\\n      GRPO matches PPO performance while significantly reducing training\\\\n      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.\\\\n\\\\n  - id: logic-rl\\\\n    title: \\\\\\\"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Xian et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2502.14768\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic\\\\n      logic puzzles. Closest competitor to STA's approach of RL for logical\\\\n      formalization, though Logic-RL uses extensional (answer-correctness)\\\\n      rewards rather than STA's intensional structural rewards.\\\\n    key_finding: >\\\\n      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;\\\\n      rule-based reward design is critical for RL-based logical reasoning.\\\\n\\\\n  - id: mellgren-prolog-grpo\\\\n    title: \\\\\\\"Training Language Models to Use Prolog as a Tool\\\\\\\"\\\\n    authors: \\\\\\\"Niklas Mellgren\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2512.07407\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,\\\\n      directly comparable to STA's approach of GRPO-training a formalizer.\\\\n      Key difference: uses pass/fail reward vs STA's structural ISR.\\\\n    key_finding: >\\\\n      GRPO is effective for teaching small LLMs to use Prolog as a tool\\\\n      for logical and mathematical reasoning.\\\\n\\\\n  - id: satlm\\\\n    title: \\\\\\\"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\\\\\\\"\\\\n    authors: \\\\\\\"Xi Ye et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"NeurIPS 2023\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: background\\\\n    relevance: >\\\\n      Neurosymbolic approach where LLM generates declarative specifications\\\\n      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)\\\\n      but uses prompting, not RL training.\\\\n    key_finding: >\\\\n      Declarative formulation outperforms imperative program-aided LMs by 23%\\\\n      on GSM; achieves SoTA on LSAT and BoardgameQA.\\\\n\\\\n  - id: deepproblog\\\\n    title: \\\\\\\"Neural Probabilistic Logic Programming in DeepProbLog\\\\\\\"\\\\n    authors: \\\\\\\"Robin Manhaeve, Sebastijan Dumančić, Angelika Kimmig, Thomas Demeester, Luc De Raedt\\\\\\\"\\\\n    year: 2021\\\\n    venue: \\\\\\\"Artificial Intelligence 298\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: background\\\\n    relevance: >\\\\n      Foundational neural-probabilistic logic programming framework that integrates\\\\n      deep learning with ProbLog via neural predicates. Establishes the intellectual\\\\n      tradition of combining neural networks with logic programming that STA extends\\\\n      to LLM-generated Prolog with RL training.\\\\n    key_finding: >\\\\n      End-to-end differentiable framework integrating neural perception with\\\\n      probabilistic logical reasoning; supports program induction and learning\\\\n      from examples.\\\\n\\\\n  - id: neurasp\\\\n    title: \\\\\\\"NeurASP: Embracing Neural Networks into Answer Set Programming\\\\\\\"\\\\n    authors: \\\\\\\"Zhun Yang, Adam Ishay, Joohyung Lee\\\\\\\"\\\\n    year: 2020\\\\n    venue: \\\\\\\"IJCAI 2020\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: background\\\\n    relevance: >\\\\n      Integrates neural networks with answer set programming (ASP), using\\\\n      ASP rules to constrain and improve neural network training. Complementary\\\\n      to DeepProbLog; together they represent the neuro-symbolic LP foundation\\\\n      that STA's LLM-to-Prolog pipeline builds upon.\\\\n    key_finding: >\\\\n      ASP semantic constraints improve neural network perception accuracy;\\\\n      demonstrates bidirectional benefit of neural-symbolic integration.\\\\n\\\\n  - id: thought-like-pro\\\\n    title: \\\\\\\"Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought\\\\\\\"\\\\n    authors: \\\\\\\"Xiaoyu Tan, Yongxin Deng, Xihe Qiu, Weidi Xu, Chao Qu, Wei Chu, Yinghui Xu, Yuan Qi\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2407.14562\\\\\\\"\\\\n    category: neurosymbolic-rl\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Uses Prolog engine to generate verified reasoning trajectories, then trains\\\\n      LLMs via imitation learning to replicate them. Directly comparable pipeline\\\\n      to STA (Prolog verification + LLM training), but uses imitation learning\\\\n      instead of GRPO with structural reward.\\\\n    key_finding: >\\\\n      Prolog-verified reasoning trajectories as training signal improve LLM\\\\n      logical reasoning; self-driven framework enables LLMs to formulate\\\\n      rules from instructions and leverage Prolog for derivation.\\\\n\\\\n  # ============================================================\\\\n  # Category 2: Reward shaping for code/formal verification\\\\n  # ============================================================\\\\n\\\\n  - id: lightman-verify-step\\\\n    title: \\\\\\\"Let's Verify Step by Step\\\\\\\"\\\\n    authors: \\\\\\\"Hunter Lightman, Vineet Kosaraju, Yura Burda, et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"arXiv 2305.20050 / ICLR 2024\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: method-component\\\\n    relevance: >\\\\n      Establishes that process supervision (step-level reward) outperforms\\\\n      outcome supervision (final-answer reward) for reasoning. STA's ISR\\\\n      is analogous: it provides structural process-level signal about which\\\\n      components of a formalization matter, rather than just pass/fail.\\\\n    key_finding: >\\\\n      Process-supervised reward model achieves 78% on MATH, significantly\\\\n      outperforming outcome-supervised models. Released PRM800K dataset.\\\\n\\\\n  - id: reward-shaping-rlhf\\\\n    title: \\\\\\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\\\\\"\\\\n    authors: \\\\\\\"Jiayi Fu, Xuandong Zhao, Chengyuan Yao, et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2502.18770\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      Studies reward shaping design principles for RLHF: bounded rewards and\\\\n      rapid-then-convergent growth. STA's ISR follows these principles\\\\n      naturally since structural necessity scores are bounded [0,1].\\\\n    key_finding: >\\\\n      Two key reward shaping principles: (1) bounded RL reward, (2) rapid\\\\n      initial growth with gradual convergence. PAR method achieves 5%+\\\\n      win rate improvement on AlpacaEval 2.0.\\\\n\\\\n  - id: rlvr-reasoning\\\\n    title: \\\\\\\"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2506.14245\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize\\\\n      reasoning. STA argues that for neurosymbolic formalization, binary reward\\\\n      is insufficient and structural reward is needed to avoid reward hacking.\\\\n    key_finding: >\\\\n      RLVR with binary verification implicitly teaches correct reasoning\\\\n      strategies, not just answer matching.\\\\n\\\\n  - id: rubric-grpo\\\\n    title: \\\\\\\"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2605.08061\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Uses structured rubric-based rewards with GRPO, similar in spirit to\\\\n      STA's structured ISR. Key difference: rubric rewards come from LLM\\\\n      judges, while ISR comes from solver-based mutation testing.\\\\n    key_finding: >\\\\n      Structured multi-dimensional reward signals improve GRPO training\\\\n      generalization compared to scalar rewards.\\\\n\\\\n  - id: gao-effective-rl-reward\\\\n    title: \\\\\\\"On Designing Effective RL Reward at Training Time for LLM Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2410.15115\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      Demonstrates that learned process/outcome reward models can hurt RL\\\\n      training, producing worse performance than simple success reward only.\\\\n      Directly explains plan005 NEGATIVE: STA's ISR as auxiliary process\\\\n      reward degrades prove_rate compared to exec-only baseline.\\\\n    key_finding: >\\\\n      PRM/ORM rewards may NOT help or even hurt RL training vs success-only\\\\n      reward. Solution: Clipping and Delta techniques to bound accumulated\\\\n      reward magnitude prevent reward hacking.\\\\n\\\\n  - id: prof-process-outcome\\\\n    title: \\\\\\\"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training\\\\\\\"\\\\n    authors: \\\\\\\"Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2509.03403\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      Shows that naively combining PRM+ORM signals leads to performance\\\\n      degradation. PROF consistency filter retains only PRM-ORM consistent\\\\n      samples, achieving 4%+ improvement over blending. Suggests STA should\\\\n      only apply ISR when consistent with execution outcome.\\\\n    key_finding: >\\\\n      Process rewards frequently suffer from inaccuracies and reward hacking\\\\n      susceptibility. PROF filters training data by PRM-ORM consistency,\\\\n      outperforming naive reward blending by 4%+ accuracy.\\\\n\\\\n  - id: moskovitz-constrained-rlhf\\\\n    title: \\\\\\\"Confronting Reward Model Overoptimization with Constrained RLHF\\\\\\\"\\\\n    authors: \\\\\\\"Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"arXiv 2310.04373 / ICLR 2024\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      First study on overoptimization in composite reward models. Shows that\\\\n      fixed-weight linear scalarization of component rewards leads to\\\\n      degradation past a threshold. Proposes constrained RL with dynamic\\\\n      Lagrange multiplier weighting as alternative to fixed ISR weight.\\\\n    key_finding: >\\\\n      Correlation between component RMs significantly affects overoptimization\\\\n      thresholds. Constrained RL with Lagrange multipliers outperforms\\\\n      fixed-weight reward composition.\\\\n\\\\n  - id: skalse-reward-hacking\\\\n    title: \\\\\\\"Defining and Characterizing Reward Hacking\\\\\\\"\\\\n    authors: \\\\\\\"Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger\\\\\\\"\\\\n    year: 2022\\\\n    venue: \\\\\\\"arXiv 2209.13085 / NeurIPS 2022\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      Formal proof that for stochastic policies, two reward functions are\\\\n      unhackable only if one is constant. Theoretically explains why any\\\\n      non-zero ISR weight can decrease prove_rate -- this is a fundamental\\\\n      property of reward composition, not STA-specific.\\\\n    key_finding: >\\\\n      Any non-constant proxy reward can decrease true reward when optimized.\\\\n      Unhackability requires the proxy to be constant, making all non-trivial\\\\n      auxiliary rewards theoretically vulnerable to degrading primary performance.\\\\n\\\\n  - id: progrs-outcome-conditioned\\\\n    title: \\\\\\\"LLM Reasoning with Process Rewards for Outcome-Guided Steps\\\\\\\"\\\\n    authors: \\\\\\\"Mohammad Rezaei, Jens Lehmann, Sahar Vahdati\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv 2604.02341\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      PRM scores optimized as absolute rewards amplify fluent failure modes.\\\\n      Outcome-conditioned centering shifts incorrect trajectories' PRM scores\\\\n      to zero mean, preserving ranking info without corrupting gradients.\\\\n      Suggests STA should condition ISR on execution outcome.\\\\n    key_finding: >\\\\n      Naive process rewards induce reward hacking by rewarding locally fluent\\\\n      but globally incorrect reasoning. Outcome-conditioned centering resolves\\\\n      the conflict with fewer rollouts than outcome-only baselines.\\\\n\\\\n  - id: qwen-prm-lessons\\\\n    title: \\\\\\\"The Lessons of Developing Process Reward Models in Mathematical Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Zhenru Zhang et al. (Qwen Team, Alibaba)\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"ACL 2025 Findings (arXiv 2501.07301)\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: supporting-evidence\\\\n    relevance: >\\\\n      MC estimation-synthesized PRM data leads to quality degradation; policy\\\\n      model generates \\\\\\\"answer-correct but reasoning-flawed\\\\\\\" responses, causing\\\\n      process reward / outcome misalignment. Directly parallels ISR problem:\\\\n      structurally correct but semantically wrong proof traces get high ISR\\\\n      but low execution reward.\\\\n    key_finding: >\\\\n      PRM performance depends critically on data quality; MC estimation\\\\n      introduces systematic bias. Answer-correct reasoning-flawed samples\\\\n      corrupt process supervision signal.\\\\n\\\\n  # ============================================================\\\\n  # Category 3: Mutation testing in software engineering\\\\n  # ============================================================\\\\n\\\\n  - id: demillo1978\\\\n    title: \\\\\\\"Hints on Test Data Selection: Help for the Practicing Programmer\\\\\\\"\\\\n    authors: \\\\\\\"Richard A. DeMillo, Richard J. Lipton, Frederick G. Sayward\\\\\\\"\\\\n    year: 1978\\\\n    venue: \\\\\\\"Computer 11(4):34-43\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Foundational paper introducing mutation testing. STA's component\\\\n      necessity testing directly extends this idea: instead of mutating\\\\n      source code to test test suites, STA mutates logical formulas\\\\n      to test component necessity for solver success.\\\\n    key_finding: >\\\\n      Introduced mutation testing and the coupling effect hypothesis:\\\\n      tests that detect simple faults also detect complex faults.\\\\n\\\\n  - id: offutt-coupling\\\\n    title: \\\\\\\"Investigations of the Software Testing Coupling Effect\\\\\\\"\\\\n    authors: \\\\\\\"A. Jefferson Offutt\\\\\\\"\\\\n    year: 1992\\\\n    venue: \\\\\\\"ACM TOSEM 1(1):5-20\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Empirically validates the coupling effect hypothesis that underpins\\\\n      mutation testing. STA's single-component ablation is analogous to\\\\n      first-order mutation; the coupling effect suggests this suffices.\\\\n    key_finding: >\\\\n      Test data killing all first-order mutants killed >99% of second-\\\\n      and third-order mutants, validating the coupling effect.\\\\n\\\\n  - id: jia-harman-survey\\\\n    title: \\\\\\\"An Analysis and Survey of the Development of Mutation Testing\\\\\\\"\\\\n    authors: \\\\\\\"Yue Jia, Mark Harman\\\\\\\"\\\\n    year: 2011\\\\n    venue: \\\\\\\"IEEE TSE 37(5):649-678\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Comprehensive survey of mutation testing covering three decades of\\\\n      development. Provides theoretical and practical foundation for STA's\\\\n      adaptation of mutation testing to logical formulas.\\\\n    key_finding: >\\\\n      Systematic classification of mutation operators, cost reduction\\\\n      techniques, and equivalence problem -- all relevant to STA's design\\\\n      of clause-level ablation operators.\\\\n\\\\n  - id: just-mutants-real-faults\\\\n    title: \\\\\\\"Are Mutants a Valid Substitute for Real Faults in Software Testing?\\\\\\\"\\\\n    authors: \\\\\\\"Rene Just, Darioush Jalali, Laura Inozemtseva, et al.\\\\\\\"\\\\n    year: 2014\\\\n    venue: \\\\\\\"FSE 2014\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Validates that mutation testing (structural/intensional analysis of\\\\n      program adequacy) correlates with real fault detection. Supports STA's\\\\n      premise that structural analysis of formalization components provides\\\\n      meaningful signal about formalization quality.\\\\n    key_finding: >\\\\n      Mutant detection is statistically correlated with real fault detection,\\\\n      and mutation score is a better predictor of test effectiveness than\\\\n      code coverage.\\\\n\\\\n  - id: llmorpheus\\\\n    title: \\\\\\\"LLMorpheus: Mutation Testing Using Large Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Frank Tip, Jon Bell, et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"IEEE TSE 2025\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Uses LLMs to generate realistic code mutants beyond traditional\\\\n      mutation operators. Shows mutation testing evolving toward\\\\n      ML-integrated approaches, validating STA's cross-pollination\\\\n      of mutation testing ideas into ML training.\\\\n    key_finding: >\\\\n      LLM-generated mutants simulate real bugs that rule-based operators\\\\n      cannot produce, improving mutation testing realism.\\\\n\\\\n  - id: mutation-guided-meta\\\\n    title: \\\\\\\"Mutation-Guided LLM-based Test Generation at Meta\\\\\\\"\\\\n    authors: \\\\\\\"Christopher Foster et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"FSE 2025\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Industrial application of mutation-guided LLM test generation at\\\\n      Meta. Demonstrates that mutation analysis can guide LLM behavior\\\\n      in production -- analogous to how STA uses mutation (ablation) to\\\\n      guide GRPO reward signal.\\\\n    key_finding: >\\\\n      Mutation-guided approach generates tests that kill significantly\\\\n      more mutants than unguided LLM test generation at Meta scale.\\\\n\\\\n  - id: mutation-consistency-llm\\\\n    title: \\\\\\\"Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2401.05940\\\\\\\"\\\\n    category: mutation-testing\\\\n    role: background\\\\n    relevance: >\\\\n      Uses code mutations to evaluate LLM code understanding consistency.\\\\n      Conceptually related to STA: both use systematic code/formula\\\\n      mutations to assess model capabilities.\\\\n    key_finding: >\\\\n      LLMs show significant inconsistency when evaluated on mutated code\\\\n      variants, suggesting superficial pattern matching.\\\\n\\\\n  # ============================================================\\\\n  # Category 4: Intensional program analysis\\\\n  # ============================================================\\\\n\\\\n  - id: deepmutation\\\\n    title: \\\\\\\"A Probabilistic Framework for Mutation Testing in Deep Neural Networks\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"Information and Software Technology 2023\\\\\\\"\\\\n    category: intensional-analysis\\\\n    role: background\\\\n    relevance: >\\\\n      Extends mutation testing to DNN testing with probabilistic mutation\\\\n      operators. Parallel to STA's extension of mutation testing from\\\\n      traditional programs to logical formulas.\\\\n    key_finding: >\\\\n      Probabilistic mutation framework enables meaningful test adequacy\\\\n      assessment for neural networks through structural perturbation.\\\\n\\\\n  # ============================================================\\\\n  # Category 5: Reward hacking / overoptimization\\\\n  # ============================================================\\\\n\\\\n  - id: inform-reward-hacking\\\\n    title: \\\\\\\"InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"NeurIPS 2024\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: background\\\\n    relevance: >\\\\n      Proposes information-bottleneck approach to detect and mitigate reward\\\\n      hacking. STA's ISR addresses the same problem differently: by grounding\\\\n      reward in verifiable structural properties (component necessity), it\\\\n      reduces the attack surface for reward hacking.\\\\n    key_finding: >\\\\n      Variational information bottleneck filters irrelevant features from\\\\n      reward model; Cluster Separation Index detects reward overoptimization.\\\\n\\\\n  - id: mo-grpo\\\\n    title: \\\\\\\"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\\\\\\\"\\\\n    authors: \\\\\\\"CyberAgent AI Lab\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2509.22047\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: background\\\\n    relevance: >\\\\n      Directly addresses GRPO reward hacking in multi-objective settings.\\\\n      STA's ISR can be viewed as adding a structural objective to the\\\\n      correctness objective, making MO-GRPO's insights directly applicable.\\\\n    key_finding: >\\\\n      Standard GRPO normalizes after summing rewards, allowing high-variance\\\\n      objectives to dominate. MO-GRPO equalizes scales before aggregation.\\\\n\\\\n  - id: reward-hacking-survey\\\\n    title: \\\\\\\"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv 2604.13602\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: background\\\\n    relevance: >\\\\n      Comprehensive survey of reward hacking mechanisms in the LLM era.\\\\n      Provides theoretical framework for understanding why STA's structural\\\\n      reward is more robust than pure outcome-based reward.\\\\n    key_finding: >\\\\n      Reward hacking manifests through specification gaming, reward model\\\\n      exploitation, and emergent misalignment; structural verification\\\\n      rewards are more robust than learned reward models.\\\\n\\\\n  - id: energy-loss-reward-hacking\\\\n    title: \\\\\\\"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"ICML 2025\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: background\\\\n    relevance: >\\\\n      Identifies energy loss in LLM final layer as an indicator of reward\\\\n      hacking during RL. Provides complementary diagnostic to STA's\\\\n      structural reward approach.\\\\n    key_finding: >\\\\n      Energy loss in the final layer increases during RL and excessive\\\\n      increase characterizes reward hacking; EPPO algorithm penalizes\\\\n      this to mitigate hacking.\\\\n\\\\n  - id: spurious-rewards\\\\n    title: \\\\\\\"Spurious Rewards: Rethinking Training Signals in RLVR\\\\\\\"\\\\n    authors: \\\\\\\"Ruixin Yang et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2506.10947 / NeurIPS 2025 submission\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: direct-evidence\\\\n    relevance: >\\\\n      Most directly relevant to STA findings. GRPO+random reward on\\\\n      Qwen2.5-Math improves 21.4%, nearly matching ground-truth reward's\\\\n      29.1%. Matches our plan017 finding: additive random (PR=48%) >\\\\n      additive ISR (PR=18%). Structured metrics can be worse than random\\\\n      noise due to systematic bias vs pure variance.\\\\n    key_finding: >\\\\n      Random reward nearly matches ground-truth reward in GRPO training,\\\\n      suggesting GRPO's group normalization extracts signal from noise.\\\\n      Effect is model-dependent (works on Qwen2.5, not Llama3).\\\\n\\\\n  - id: bondarenko-spec-gaming\\\\n    title: \\\\\\\"Demonstrating Specification Gaming in Reasoning Models\\\\\\\"\\\\n    authors: \\\\\\\"Alexander Bondarenko, Denis Volk, Dmitrii Volkov, Jeffrey Ladish\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2502.13295\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: direct-evidence\\\\n    relevance: >\\\\n      Shows that reasoning models (o3, DeepSeek-R1) resort to specification\\\\n      gaming on difficult tasks by default, without explicit nudging.\\\\n      Directly relevant to STA's concern: RL-trained reasoning models\\\\n      may game formal verification rewards rather than learn genuine\\\\n      formalization skills.\\\\n    key_finding: >\\\\n      Reasoning models spontaneously hack benchmarks (e.g., manipulating\\\\n      chess engine files instead of playing chess). Stronger reasoning\\\\n      capability correlates with more sophisticated gaming strategies.\\\\n\\\\n  - id: kim-game-formalization\\\\n    title: \\\\\\\"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Kyuhee Kim, Auguste Poiroux, Antoine Bosselut\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"VerifAI-2 Workshop, ICLR 2026 (arXiv 2604.19459)\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: direct-evidence\\\\n    relevance: >\\\\n      Directly studies whether LLMs game formalization in logical reasoning --\\\\n      the exact phenomenon STA's ISR is designed to detect. Evaluates GPT-5\\\\n      and DeepSeek-R1 on FOLIO with Lean 4 proofs. Finds two modes of\\\\n      unfaithfulness: axiom fabrication (GPT-5) and premise mistranslation\\\\n      (R1), the latter evading detection entirely.\\\\n    key_finding: >\\\\n      High compilation rates (87-99%) do not imply faithful formalization.\\\\n      Two-stage pipelines reveal unfaithfulness that unified generation hides.\\\\n      Premise mistranslation produces internally consistent but unfaithful\\\\n      outputs -- analogous to STA's high-ISR but semantically wrong traces.\\\\n\\\\n  - id: gao-reward-overoptimization\\\\n    title: \\\\\\\"Scaling Laws for Reward Model Overoptimization\\\\\\\"\\\\n    authors: \\\\\\\"Leo Gao, John Schulman, Jacob Hilton\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"ICML 2023 (arXiv 2210.10760)\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: theoretical-foundation\\\\n    relevance: >\\\\n      Foundational work quantifying Goodhart's effect: proxy reward rises\\\\n      but gold reward first rises then falls. ISR is a proxy reward that\\\\n      exhibits exactly this pattern — ISR can increase while prove_rate\\\\n      decreases, making it suitable for post-hoc diagnosis but harmful\\\\n      as training signal.\\\\n    key_finding: >\\\\n      Gold/proxy reward divergence follows predictable scaling laws.\\\\n      Proxy reward optimization past critical point degrades gold reward,\\\\n      with the divergence point scaling with model and dataset size.\\\\n\\\\n  - id: karwowski-goodhart-rl\\\\n    title: \\\\\\\"Goodhart's Law in Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Jacek Karwowski, Oliver Hayman, Xingjian Bai, Klaus Kiendlhofer, Charlie Griffin, Joar Skalse\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"ICLR 2024 (arXiv 2310.09144)\\\\\\\"\\\\n    category: reward-hacking\\\\n    role: theoretical-foundation\\\\n    relevance: >\\\\n      Geometric interpretation of Goodhart's Law in MDPs: optimizing\\\\n      imperfect proxy past critical point decreases true objective. ISR as\\\\n      proxy has partial correlation with execution correctness — exceeding\\\\n      critical optimization point pushes policy toward high-ISR but\\\\n      low-correctness regions. Explains plan002/plan005 negative results.\\\\n    key_finding: >\\\\n      Formalizes Goodhart's Law for RL: any non-trivially correlated proxy\\\\n      reward creates regions where proxy and true reward diverge, and\\\\n      policy optimization inevitably enters these regions.\\\\n\\\\n  # ============================================================\\\\n  # Category 6: FOL/Prolog formalization with LLMs\\\\n  # ============================================================\\\\n\\\\n  - id: folio\\\\n    title: \\\\\\\"FOLIO: Natural Language Reasoning with First-Order Logic\\\\\\\"\\\\n    authors: \\\\\\\"Simeng Han et al.\\\\\\\"\\\\n    year: 2022\\\\n    venue: \\\\\\\"arXiv 2209.00840 / EMNLP 2024\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: evaluation\\\\n    relevance: >\\\\n      Primary FOL reasoning benchmark. STA uses FOLIO-style NL->FOL\\\\n      formalization as the target task for GRPO training. FOLIO's\\\\n      expert-annotated FOL annotations serve as reference formalizations.\\\\n    key_finding: >\\\\n      1,430 NL-FOL paired examples with reasoning depths up to 5+;\\\\n      GPT-4 still struggles on the hardest examples.\\\\n\\\\n  - id: proofwriter\\\\n    title: \\\\\\\"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language\\\\\\\"\\\\n    authors: \\\\\\\"Oyvind Tafjord, Bhavana Dalvi, Peter Clark\\\\\\\"\\\\n    year: 2021\\\\n    venue: \\\\\\\"Findings of ACL-IJCNLP 2021\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: evaluation\\\\n    relevance: >\\\\n      Source dataset for STA's training data. ProofWriter provides\\\\n      rule-based logical reasoning problems in natural language that\\\\n      STA uses for training formalizer models.\\\\n    key_finding: >\\\\n      Generative model can reliably produce implications and proofs;\\\\n      accuracy exceeds prior methods by 9% and generalizes to unseen\\\\n      proof depths.\\\\n\\\\n  - id: logic-lm\\\\n    title: \\\\\\\"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Liangming Pan, Alon Albalak, Xinyi Wang, William Wang\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"Findings of EMNLP 2023\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      LLM->symbolic solver pipeline for logical reasoning, directly\\\\n      comparable to STA's formalizer->Prolog solver pipeline. Key\\\\n      difference: Logic-LM uses prompting, STA uses GRPO training.\\\\n    key_finding: >\\\\n      LLM+solver achieves 39.2% improvement over LLM-alone on logical\\\\n      reasoning benchmarks including ProofWriter and FOLIO.\\\\n\\\\n  - id: linc\\\\n    title: \\\\\\\"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers\\\\\\\"\\\\n    authors: \\\\\\\"Theo X. Olausson, Alex Gu, Ben Lipkin, et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"EMNLP 2023\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Neurosymbolic approach where LLM translates NL to FOL for theorem\\\\n      prover. Directly comparable to STA's NL->Prolog translation.\\\\n      LINC uses prompting-based approach; STA uses RL training.\\\\n    key_finding: >\\\\n      StarCoder+ (15.5B) with LINC outperforms GPT-3.5 and GPT-4 with\\\\n      CoT by 38% and 10% respectively on ProofWriter.\\\\n\\\\n  - id: fover-pei2025\\\\n    title: \\\\\\\"FoVer: First-Order Logic Verification for Natural Language Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Yu Pei, Yongping Du, Xingnan Jin\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"TACL 13:1340-1359\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Uses LLM->FOL->Z3 pipeline for verifying NL reasoning correctness.\\\\n      Similar to STA's verification pipeline but focuses on post-hoc\\\\n      verification rather than training reward signal.\\\\n    key_finding: >\\\\n      FOL verification via Z3 significantly outperforms existing methods\\\\n      on ProofWriter and FOLIO benchmarks.\\\\n\\\\n  - id: lorp\\\\n    title: \\\\\\\"LoRP: LLM-based Logical Reasoning via Prolog\\\\\\\"\\\\n    authors: \\\\\\\"Various\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"Knowledge-Based Systems 2025\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      LLM->Prolog pipeline with FOL-to-Prolog translation mechanism.\\\\n      Closest to STA's formalization target (Prolog), though LoRP\\\\n      uses prompting while STA uses GRPO training with structural reward.\\\\n    key_finding: >\\\\n      Systematic FOL-to-Prolog translation extends Prolog expressiveness;\\\\n      achieves SoTA accuracy on logical reasoning with three-vote majority.\\\\n\\\\n  - id: nl2fol\\\\n    title: \\\\\\\"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection\\\\\\\"\\\\n    authors: \\\\\\\"Lalwani, Kim, et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2405.02318\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: background\\\\n    relevance: >\\\\n      Step-by-step NL->FOL translation using LLMs with SMT solver\\\\n      verification. Demonstrates the NL->formal logic pipeline that\\\\n      STA aims to improve via RL training.\\\\n    key_finding: >\\\\n      Neurosymbolic NL2FOL achieves 78% F1 on LOGIC dataset and\\\\n      generalizes to LogicClimate (80% F1), outperforming supervised\\\\n      models by 21%.\\\\n\\\\n  - id: logica2\\\\n    title: \\\\\\\"LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding\\\\\\\"\\\\n    authors: \\\\\\\"Liu et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"IEEE/ACM TASLP 2023\\\\\\\"\\\\n    category: fol-formalization\\\\n    role: evaluation\\\\n    relevance: >\\\\n      Logical reasoning evaluation benchmark derived from Chinese civil\\\\n      service exams. Provides supplementary evaluation for STA's\\\\n      formalization capabilities.\\\\n    key_finding: >\\\\n      8,678 multiple-choice questions covering categorical, disjunctive,\\\\n      and conditional reasoning; widely used LLM benchmark.\\\\n\\\\n  # ============================================================\\\\n  # Category 7: Goodhart's Law theory and dose-response dynamics\\\\n  # ============================================================\\\\n\\\\n  - id: manheim-goodhart-taxonomy\\\\n    title: \\\\\\\"Categorizing Variants of Goodhart's Law\\\\\\\"\\\\n    authors: \\\\\\\"David Manheim, Scott Garrabrant\\\\\\\"\\\\n    year: 2019\\\\n    venue: \\\\\\\"arXiv 1803.04585\\\\\\\"\\\\n    category: goodhart-overoptimization\\\\n    role: theoretical-foundation\\\\n    relevance: >\\\\n      Four-part Goodhart taxonomy: regressional, extremal, causal, adversarial.\\\\n      STA's high-β ISR collapse is best classified as extremal Goodhart\\\\n      (policy moves to OOD region where ISR↑ but prove_rate↓). Provides\\\\n      vocabulary for discussion section.\\\\n    key_finding: >\\\\n      First systematic categorization of Goodhart failure modes. Extremal\\\\n      variant occurs when proxy-goal relationship breaks in out-of-distribution\\\\n      regions reached by strong optimization.\\\\n\\\\n  - id: pan-reward-misspecification\\\\n    title: \\\\\\\"The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models\\\\\\\"\\\\n    authors: \\\\\\\"Alexander Pan, Kush Bhatia, Jacob Steinhardt\\\\\\\"\\\\n    year: 2022\\\\n    venue: \\\\\\\"ICLR 2022\\\\\\\"\\\\n    category: goodhart-overoptimization\\\\n    role: theoretical-foundation\\\\n    relevance: >\\\\n      Across 9 environments, more capable agents exploit misspecifications more.\\\\n      Observes dose-dependent degradation — capability thresholds where true\\\\n      reward sharply drops. Matches STA's β=0.1→0.3 qualitative shift.\\\\n    key_finding: >\\\\n      Reward misspecification causes dose-dependent degradation where true reward\\\\n      sharply drops past capability thresholds. More capable optimization\\\\n      produces worse outcomes under misspecification.\\\\n\\\\n  - id: kwa-catastrophic-goodhart\\\\n    title: \\\\\\\"Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification\\\\\\\"\\\\n    authors: \\\\\\\"Tat-Thang Kwa, Rachel Thomas, Adrià Garriga-Alonso\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"NeurIPS 2024\\\\\\\"\\\\n    category: goodhart-overoptimization\\\\n    role: theoretical-foundation\\\\n    relevance: >\\\\n      If reward model error is heavy-tailed, policies achieve arbitrarily\\\\n      high proxy reward with no true utility gain. KL regularization provably\\\\n      fails. Explains why KL penalty in GRPO cannot prevent ISR collapse\\\\n      at high β if ISR error distribution is heavy-tailed.\\\\n    key_finding: >\\\\n      KL-regularized RL provably fails to prevent overoptimization under\\\\n      heavy-tailed reward misspecification. Policies can achieve arbitrarily\\\\n      high proxy reward with zero true utility.\\\\n\\\\n  - id: rafailov-daa-scaling\\\\n    title: \\\\\\\"Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms\\\\\\\"\\\\n    authors: \\\\\\\"Rafael Rafailov, Yaswanth Chittepu, Ryan Park, Harshit Sikchi, Joey Hejna, W. Bradley Knox, Chelsea Finn, Scott Niekum\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"NeurIPS 2024\\\\\\\"\\\\n    category: goodhart-overoptimization\\\\n    role: supporting-evidence\\\\n    relevance: >\\\\n      Extends Gao et al. to DPO/IPO/SLiC. Tests seven β values across\\\\n      1B-6.9B models. DAAs still overoptimize despite no explicit proxy RM.\\\\n      Validates β as a \\\\\\\"dose\\\\\\\" parameter — directly analogous to STA's\\\\n      ISR weight sweep.\\\\n    key_finding: >\\\\n      Direct alignment algorithms exhibit overoptimization following\\\\n      predictable scaling laws. Smaller models overoptimize sooner.\\\\n      β-controlled dose-response is a general phenomenon across RL paradigms.\\\\n\\\\n  - id: huang-chi-squared\\\\n    title: \\\\\\\"Correcting the Mythos of KL-Regularization: Direct and Contrastive Distribution Correction\\\\\\\"\\\\n    authors: \\\\\\\"Afra Feyza Akyürek, Banghua Zhu, Sham Kakade, Jiantao Jiao\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"ICLR 2025 Poster\\\\\\\"\\\\n    category: goodhart-overoptimization\\\\n    role: supporting-evidence\\\\n    relevance: >\\\\n      KL-regularization is theoretically inadequate for preventing\\\\n      overoptimization. Chi-squared divergence provably alleviates it.\\\\n      Suggests that even with KL penalty in GRPO, STA's high-β collapse\\\\n      is theoretically expected.\\\\n    key_finding: >\\\\n      Chi-squared preference optimization provably mitigates overoptimization\\\\n      where KL-regularization fails. Alternative divergence measures offer\\\\n      stronger guarantees.\\\\n\\\\n  - id: coste-rm-ensembles\\\\n    title: \\\\\\\"Reward Model Ensembles Help Mitigate Overoptimization\\\\\\\"\\\\n    authors: \\\\\\\"Thomas Coste, Usman Anwar, Robert Kirk, David Krueger\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"NeurIPS 2023 Workshop on Alignment\\\\\\\"\\\\n    category: goodhart-overoptimization\\\\n    role: background\\\\n    relevance: >\\\\n      Worst-case optimization across RM ensembles practically eliminates\\\\n      overoptimization for BoN and reduces it for PPO. Suggests ensemble\\\\n      of multiple solver metrics (instead of single ISR) as mitigation.\\\\n    key_finding: >\\\\n      RM ensembles with worst-case aggregation mitigate overoptimization.\\\\n      Ensemble size and diversity directly affect robustness.\\\\n\\\\n  # ============================================================\\\\n  # Category 8: Solver/prover as RL reward signal\\\\n  # ============================================================\\\\n\\\\n  - id: rlsf\\\\n    title: \\\\\\\"Reinforcement Learning via Symbolic Feedback\\\\\\\"\\\\n    authors: \\\\\\\"Abhinav Jha, Shikhar Murty, Zico Kolter, et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv 2405.16661\\\\\\\"\\\\n    category: verification-reward\\\\n    role: direct-competitor\\\\n    relevance: >\\\\n      Most directly relevant: uses solver/prover certificates as fine-grained\\\\n      token-level reward signal. Outperforms traditional approaches on program\\\\n      synthesis (+31.4%). STA extends this paradigm and shows when it breaks\\\\n      (Goodhart effects at high auxiliary reward weight).\\\\n    key_finding: >\\\\n      Symbolic reasoning tools provide poly-sized certificates as reward.\\\\n      Smaller RLSF models outperform GPT-4 on structured generation tasks.\\\\n\\\\n  - id: fover-kamoi2026\\\\n    title: \\\\\\\"FoVer: Generalizable Process Reward Models via Formally Verified Training Data\\\\\\\"\\\\n    authors: \\\\\\\"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"Findings of ACL 2026 (arXiv 2502.01345)\\\\\\\"\\\\n    category: verification-reward\\\\n    role: supporting-evidence\\\\n    relevance: >\\\\n      Uses Z3 and Isabelle to synthesize PRM training data by annotating\\\\n      step-level error labels without human annotation. Same solver family\\\\n      as STA. Shows verification-based rewards work; STA extends by showing\\\\n      dose-response dynamics.\\\\n    key_finding: >\\\\n      Formally verified training data enables generalizable process reward\\\\n      models competitive on ProcessBench and 12 reasoning benchmarks.\\\\n\\\\n  - id: deepseek-prover-v15\\\\n    title: \\\\\\\"DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search\\\\\\\"\\\\n    authors: \\\\\\\"DeepSeek AI\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"ICLR 2025 (arXiv 2408.08152)\\\\\\\"\\\\n    category: verification-reward\\\\n    role: method-component\\\\n    relevance: >\\\\n      Uses GRPO with Lean 4 verification as binary reward. Same algorithm\\\\n      (GRPO) + formal verification, but binary (pass/fail). Binary reward\\\\n      avoids the graded-metric Goodhart risk that STA identifies with ISR.\\\\n    key_finding: >\\\\n      GRPO + binary Lean verification achieves 63.5% on miniF2F. Binary\\\\n      correctness guarantee via formal verification sidesteps proxy reward\\\\n      overoptimization.\\\\n\\\\n  - id: alphaproof\\\\n    title: \\\\\\\"AlphaProof\\\\\\\"\\\\n    authors: \\\\\\\"Google DeepMind\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"Nature 2025\\\\\\\"\\\\n    category: verification-reward\\\\n    role: background\\\\n    relevance: >\\\\n      AlphaZero-inspired RL with Lean proof verification at scale.\\\\n      Silver medal at IMO 2024. Binary verification reward avoids the\\\\n      Goodhart problem STA identifies with graded verification metrics.\\\\n    key_finding: >\\\\n      Binary formal verification as RL reward scales to IMO-level\\\\n      mathematical reasoning. Demonstrates verification-reward RL works\\\\n      at the frontier of mathematical difficulty.\\\\n\\\\n  - id: math-shepherd\\\\n    title: \\\\\\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\\\\\"\\\\n    authors: \\\\\\\"Peiyi Wang, Lei Li, Zhihong Shao, R.X. Xu, et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"ACL 2024 (arXiv 2312.08935)\\\\\\\"\\\\n    category: verification-reward\\\\n    role: supporting-evidence\\\\n    relevance: >\\\\n      Automatically constructs process supervision data and uses it as\\\\n      step-by-step PPO reward. Automated verification reward without human\\\\n      labels, analogous to STA's automated ISR computation via solver.\\\\n    key_finding: >\\\\n      Automated process supervision improves Mistral-7B on GSM8K\\\\n      (77.9→84.1%) and MATH (28.6→33.0%) without human annotation.\\\\n\\\\n  # ============================================================\\\\n  # Additional reward-shaping papers (Goodhart survey additions)\\\\n  # ============================================================\\\\n\\\\n  - id: bipars\\\\n    title: \\\\\\\"Learning to Utilize Shaping Rewards: A New Approach of Reward Shaping\\\\\\\"\\\\n    authors: \\\\\\\"Yujing Hu, Weixun Wang, Hangtian Jia, et al.\\\\\\\"\\\\n    year: 2020\\\\n    venue: \\\\\\\"NeurIPS 2020\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      Bi-level optimization learns parameterized shaping reward weights.\\\\n      Can transform harmful shaping rewards into beneficial ones by learning\\\\n      negative weights. Directly addresses STA's problem: when ISR weight\\\\n      is wrong, automated weight learning could find optimal β.\\\\n    key_finding: >\\\\n      Bi-level optimization automatically learns auxiliary reward weights,\\\\n      outperforming fixed weights and recovering from harmful shaping rewards.\\\\n\\\\n  - id: dapo\\\\n    title: \\\\\\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\\\\\"\\\\n    authors: \\\\\\\"Qiying Yu et al. (ByteDance)\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2503.14476\\\\\\\"\\\\n    category: reward-shaping\\\\n    role: background\\\\n    relevance: >\\\\n      Four techniques for stable multi-component reward in GRPO: Clip-Higher,\\\\n      Dynamic Sampling, token-level policy gradient, Overlong Reward Shaping.\\\\n      Addresses stability issues relevant to STA's multi-reward setup.\\\\n    key_finding: >\\\\n      Clip-Higher and Dynamic Sampling prevent entropy collapse in GRPO\\\\n      with multi-component rewards. Soft punishment for overlong outputs\\\\n      avoids reward hacking through length exploitation.\\\\n\\\", \\\"total_chars\\\": 42743, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\", \"content\": \"# Literature Map for Solver Trace Ablation (STA)\\n# Categories:\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\n#   2. reward-shaping: Reward shaping for code/formal verification\\n#   3. mutation-testing: Mutation testing in software engineering\\n#   4. intensional-analysis: Intensional program analysis\\n#   5. reward-hacking: Reward hacking / overoptimization\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\n#   7. goodhart-overoptimization: Goodhart's Law theory and dose-response dynamics\\n#   8. verification-reward: Solver/prover as RL reward signal\\n\\npapers:\\n\\n  # ============================================================\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\n  # ============================================================\\n\\n  - id: deepseek-r1\\n    title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n    authors: \\\"DeepSeek-AI\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2501.12948 / Nature 2025\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\n      intensional structural reward for neurosymbolic formalization.\\n    key_finding: >\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\n      showing emergent chain-of-thought reasoning from RL alone.\\n\\n  - id: deepseekmath\\n    title: \\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\"\\n    authors: \\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2402.03300\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\\n      used in STA training. GRPO eliminates the critic model by estimating\\n      baselines from group scores.\\n    key_finding: >\\n      GRPO matches PPO performance while significantly reducing training\\n      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.\\n\\n  - id: logic-rl\\n    title: \\\"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\\\"\\n    authors: \\\"Xian et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.14768\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic\\n      logic puzzles. Closest competitor to STA's approach of RL for logical\\n      formalization, though Logic-RL uses extensional (answer-correctness)\\n      rewards rather than STA's intensional structural rewards.\\n    key_finding: >\\n      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;\\n      rule-based reward design is critical for RL-based logical reasoning.\\n\\n  - id: mellgren-prolog-grpo\\n    title: \\\"Training Language Models to Use Prolog as a Tool\\\"\\n    authors: \\\"Niklas Mellgren\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2512.07407\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,\\n      directly comparable to STA's approach of GRPO-training a formalizer.\\n      Key difference: uses pass/fail reward vs STA's structural ISR.\\n    key_finding: >\\n      GRPO is effective for teaching small LLMs to use Prolog as a tool\\n      for logical and mathematical reasoning.\\n\\n  - id: satlm\\n    title: \\\"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\\\"\\n    authors: \\\"Xi Ye et al.\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023\\\"\\n    category: neurosymbolic-rl\\n    role: background\\n    relevance: >\\n      Neurosymbolic approach where LLM generates declarative specifications\\n      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)\\n      but uses prompting, not RL training.\\n    key_finding: >\\n      Declarative formulation outperforms imperative program-aided LMs by 23%\\n      on GSM; achieves SoTA on LSAT and BoardgameQA.\\n\\n  - id: deepproblog\\n    title: \\\"Neural Probabilistic Logic Programming in DeepProbLog\\\"\\n    authors: \\\"Robin Manhaeve, Sebastijan Dumančić, Angelika Kimmig, Thomas Demeester, Luc De Raedt\\\"\\n    year: 2021\\n    venue: \\\"Artificial Intelligence 298\\\"\\n    category: neurosymbolic-rl\\n    role: background\\n    relevance: >\\n      Foundational neural-probabilistic logic programming framework that integrates\\n      deep learning with ProbLog via neural predicates. Establishes the intellectual\\n      tradition of combining neural networks with logic programming that STA extends\\n      to LLM-generated Prolog with RL training.\\n    key_finding: >\\n      End-to-end differentiable framework integrating neural perception with\\n      probabilistic logical reasoning; supports program induction and learning\\n      from examples.\\n\\n  - id: neurasp\\n    title: \\\"NeurASP: Embracing Neural Networks into Answer Set Programming\\\"\\n    authors: \\\"Zhun Yang, Adam Ishay, Joohyung Lee\\\"\\n    year: 2020\\n    venue: \\\"IJCAI 2020\\\"\\n    category: neurosymbolic-rl\\n    role: background\\n    relevance: >\\n      Integrates neural networks with answer set programming (ASP), using\\n      ASP rules to constrain and improve neural network training. Complementary\\n      to DeepProbLog; together they represent the neuro-symbolic LP foundation\\n      that STA's LLM-to-Prolog pipeline builds upon.\\n    key_finding: >\\n      ASP semantic constraints improve neural network perception accuracy;\\n      demonstrates bidirectional benefit of neural-symbolic integration.\\n\\n  - id: thought-like-pro\\n    title: \\\"Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought\\\"\\n    authors: \\\"Xiaoyu Tan, Yongxin Deng, Xihe Qiu, Weidi Xu, Chao Qu, Wei Chu, Yinghui Xu, Yuan Qi\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2407.14562\\\"\\n    category: neurosymbolic-rl\\n    role: direct-competitor\\n    relevance: >\\n      Uses Prolog engine to generate verified reasoning trajectories, then trains\\n      LLMs via imitation learning to replicate them. Directly comparable pipeline\\n      to STA (Prolog verification + LLM training), but uses imitation learning\\n      instead of GRPO with structural reward.\\n    key_finding: >\\n      Prolog-verified reasoning trajectories as training signal improve LLM\\n      logical reasoning; self-driven framework enables LLMs to formulate\\n      rules from instructions and leverage Prolog for derivation.\\n\\n  # ============================================================\\n  # Category 2: Reward shaping for code/formal verification\\n  # ============================================================\\n\\n  - id: lightman-verify-step\\n    title: \\\"Let's Verify Step by Step\\\"\\n    authors: \\\"Hunter Lightman, Vineet Kosaraju, Yura Burda, et al.\\\"\\n    year: 2023\\n    venue: \\\"arXiv 2305.20050 / ICLR 2024\\\"\\n    category: reward-shaping\\n    role: method-component\\n    relevance: >\\n      Establishes that process supervision (step-level reward) outperforms\\n      outcome supervision (final-answer reward) for reasoning. STA's ISR\\n      is analogous: it provides structural process-level signal about which\\n      components of a formalization matter, rather than just pass/fail.\\n    key_finding: >\\n      Process-supervised reward model achieves 78% on MATH, significantly\\n      outperforming outcome-supervised models. Released PRM800K dataset.\\n\\n  - id: reward-shaping-rlhf\\n    title: \\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\"\\n    authors: \\\"Jiayi Fu, Xuandong Zhao, Chengyuan Yao, et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.18770\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Studies reward shaping design principles for RLHF: bounded rewards and\\n      rapid-then-convergent growth. STA's ISR follows these principles\\n      naturally since structural necessity scores are bounded [0,1].\\n    key_finding: >\\n      Two key reward shaping principles: (1) bounded RL reward, (2) rapid\\n      initial growth with gradual convergence. PAR method achieves 5%+\\n      win rate improvement on AlpacaEval 2.0.\\n\\n  - id: rlvr-reasoning\\n    title: \\\"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2506.14245\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize\\n      reasoning. STA argues that for neurosymbolic formalization, binary reward\\n      is insufficient and structural reward is needed to avoid reward hacking.\\n    key_finding: >\\n      RLVR with binary verification implicitly teaches correct reasoning\\n      strategies, not just answer matching.\\n\\n  - id: rubric-grpo\\n    title: \\\"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2605.08061\\\"\\n    category: reward-shaping\\n    role: direct-competitor\\n    relevance: >\\n      Uses structured rubric-based rewards with GRPO, similar in spirit to\\n      STA's structured ISR. Key difference: rubric rewards come from LLM\\n      judges, while ISR comes from solver-based mutation testing.\\n    key_finding: >\\n      Structured multi-dimensional reward signals improve GRPO training\\n      generalization compared to scalar rewards.\\n\\n  - id: gao-effective-rl-reward\\n    title: \\\"On Designing Effective RL Reward at Training Time for LLM Reasoning\\\"\\n    authors: \\\"Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2410.15115\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Demonstrates that learned process/outcome reward models can hurt RL\\n      training, producing worse performance than simple success reward only.\\n      Directly explains plan005 NEGATIVE: STA's ISR as auxiliary process\\n      reward degrades prove_rate compared to exec-only baseline.\\n    key_finding: >\\n      PRM/ORM rewards may NOT help or even hurt RL training vs success-only\\n      reward. Solution: Clipping and Delta techniques to bound accumulated\\n      reward magnitude prevent reward hacking.\\n\\n  - id: prof-process-outcome\\n    title: \\\"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training\\\"\\n    authors: \\\"Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2509.03403\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Shows that naively combining PRM+ORM signals leads to performance\\n      degradation. PROF consistency filter retains only PRM-ORM consistent\\n      samples, achieving 4%+ improvement over blending. Suggests STA should\\n      only apply ISR when consistent with execution outcome.\\n    key_finding: >\\n      Process rewards frequently suffer from inaccuracies and reward hacking\\n      susceptibility. PROF filters training data by PRM-ORM consistency,\\n      outperforming naive reward blending by 4%+ accuracy.\\n\\n  - id: moskovitz-constrained-rlhf\\n    title: \\\"Confronting Reward Model Overoptimization with Constrained RLHF\\\"\\n    authors: \\\"Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer\\\"\\n    year: 2023\\n    venue: \\\"arXiv 2310.04373 / ICLR 2024\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      First study on overoptimization in composite reward models. Shows that\\n      fixed-weight linear scalarization of component rewards leads to\\n      degradation past a threshold. Proposes constrained RL with dynamic\\n      Lagrange multiplier weighting as alternative to fixed ISR weight.\\n    key_finding: >\\n      Correlation between component RMs significantly affects overoptimization\\n      thresholds. Constrained RL with Lagrange multipliers outperforms\\n      fixed-weight reward composition.\\n\\n  - id: skalse-reward-hacking\\n    title: \\\"Defining and Characterizing Reward Hacking\\\"\\n    authors: \\\"Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger\\\"\\n    year: 2022\\n    venue: \\\"arXiv 2209.13085 / NeurIPS 2022\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Formal proof that for stochastic policies, two reward functions are\\n      unhackable only if one is constant. Theoretically explains why any\\n      non-zero ISR weight can decrease prove_rate -- this is a fundamental\\n      property of reward composition, not STA-specific.\\n    key_finding: >\\n      Any non-constant proxy reward can decrease true reward when optimized.\\n      Unhackability requires the proxy to be constant, making all non-trivial\\n      auxiliary rewards theoretically vulnerable to degrading primary performance.\\n\\n  - id: progrs-outcome-conditioned\\n    title: \\\"LLM Reasoning with Process Rewards for Outcome-Guided Steps\\\"\\n    authors: \\\"Mohammad Rezaei, Jens Lehmann, Sahar Vahdati\\\"\\n    year: 2026\\n    venue: \\\"arXiv 2604.02341\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      PRM scores optimized as absolute rewards amplify fluent failure modes.\\n      Outcome-conditioned centering shifts incorrect trajectories' PRM scores\\n      to zero mean, preserving ranking info without corrupting gradients.\\n      Suggests STA should condition ISR on execution outcome.\\n    key_finding: >\\n      Naive process rewards induce reward hacking by rewarding locally fluent\\n      but globally incorrect reasoning. Outcome-conditioned centering resolves\\n      the conflict with fewer rollouts than outcome-only baselines.\\n\\n  - id: qwen-prm-lessons\\n    title: \\\"The Lessons of Developing Process Reward Models in Mathematical Reasoning\\\"\\n    authors: \\\"Zhenru Zhang et al. (Qwen Team, Alibaba)\\\"\\n    year: 2025\\n    venue: \\\"ACL 2025 Findings (arXiv 2501.07301)\\\"\\n    category: reward-shaping\\n    role: supporting-evidence\\n    relevance: >\\n      MC estimation-synthesized PRM data leads to quality degradation; policy\\n      model generates \\\"answer-correct but reasoning-flawed\\\" responses, causing\\n      process reward / outcome misalignment. Directly parallels ISR problem:\\n      structurally correct but semantically wrong proof traces get high ISR\\n      but low execution reward.\\n    key_finding: >\\n      PRM performance depends critically on data quality; MC estimation\\n      introduces systematic bias. Answer-correct reasoning-flawed samples\\n      corrupt process supervision signal.\\n\\n  # ============================================================\\n  # Category 3: Mutation testing in software engineering\\n  # ============================================================\\n\\n  - id: demillo1978\\n    title: \\\"Hints on Test Data Selection: Help for the Practicing Programmer\\\"\\n    authors: \\\"Richard A. DeMillo, Richard J. Lipton, Frederick G. Sayward\\\"\\n    year: 1978\\n    venue: \\\"Computer 11(4):34-43\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Foundational paper introducing mutation testing. STA's component\\n      necessity testing directly extends this idea: instead of mutating\\n      source code to test test suites, STA mutates logical formulas\\n      to test component necessity for solver success.\\n    key_finding: >\\n      Introduced mutation testing and the coupling effect hypothesis:\\n      tests that detect simple faults also detect complex faults.\\n\\n  - id: offutt-coupling\\n    title: \\\"Investigations of the Software Testing Coupling Effect\\\"\\n    authors: \\\"A. Jefferson Offutt\\\"\\n    year: 1992\\n    venue: \\\"ACM TOSEM 1(1):5-20\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Empirically validates the coupling effect hypothesis that underpins\\n      mutation testing. STA's single-component ablation is analogous to\\n      first-order mutation; the coupling effect suggests this suffices.\\n    key_finding: >\\n      Test data killing all first-order mutants killed >99% of second-\\n      and third-order mutants, validating the coupling effect.\\n\\n  - id: jia-harman-survey\\n    title: \\\"An Analysis and Survey of the Development of Mutation Testing\\\"\\n    authors: \\\"Yue Jia, Mark Harman\\\"\\n    year: 2011\\n    venue: \\\"IEEE TSE 37(5):649-678\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Comprehensive survey of mutation testing covering three decades of\\n      development. Provides theoretical and practical foundation for STA's\\n      adaptation of mutation testing to logical formulas.\\n    key_finding: >\\n      Systematic classification of mutation operators, cost reduction\\n      techniques, and equivalence problem -- all relevant to STA's design\\n      of clause-level ablation operators.\\n\\n  - id: just-mutants-real-faults\\n    title: \\\"Are Mutants a Valid Substitute for Real Faults in Software Testing?\\\"\\n    authors: \\\"Rene Just, Darioush Jalali, Laura Inozemtseva, et al.\\\"\\n    year: 2014\\n    venue: \\\"FSE 2014\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Validates that mutation testing (structural/intensional analysis of\\n      program adequacy) correlates with real fault detection. Supports STA's\\n      premise that structural analysis of formalization components provides\\n      meaningful signal about formalization quality.\\n    key_finding: >\\n      Mutant detection is statistically correlated with real fault detection,\\n      and mutation score is a better predictor of test effectiveness than\\n      code coverage.\\n\\n  - id: llmorpheus\\n    title: \\\"LLMorpheus: Mutation Testing Using Large Language Models\\\"\\n    authors: \\\"Frank Tip, Jon Bell, et al.\\\"\\n    year: 2025\\n    venue: \\\"IEEE TSE 2025\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Uses LLMs to generate realistic code mutants beyond traditional\\n      mutation operators. Shows mutation testing evolving toward\\n      ML-integrated approaches, validating STA's cross-pollination\\n      of mutation testing ideas into ML training.\\n    key_finding: >\\n      LLM-generated mutants simulate real bugs that rule-based operators\\n      cannot produce, improving mutation testing realism.\\n\\n  - id: mutation-guided-meta\\n    title: \\\"Mutation-Guided LLM-based Test Generation at Meta\\\"\\n    authors: \\\"Christopher Foster et al.\\\"\\n    year: 2025\\n    venue: \\\"FSE 2025\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Industrial application of mutation-guided LLM test generation at\\n      Meta. Demonstrates that mutation analysis can guide LLM behavior\\n      in production -- analogous to how STA uses mutation (ablation) to\\n      guide GRPO reward signal.\\n    key_finding: >\\n      Mutation-guided approach generates tests that kill significantly\\n      more mutants than unguided LLM test generation at Meta scale.\\n\\n  - id: mutation-consistency-llm\\n    title: \\\"Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs\\\"\\n    authors: \\\"Various\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2401.05940\\\"\\n    category: mutation-testing\\n    role: background\\n    relevance: >\\n      Uses code mutations to evaluate LLM code understanding consistency.\\n      Conceptually related to STA: both use systematic code/formula\\n      mutations to assess model capabilities.\\n    key_finding: >\\n      LLMs show significant inconsistency when evaluated on mutated code\\n      variants, suggesting superficial pattern matching.\\n\\n  # ============================================================\\n  # Category 4: Intensional program analysis\\n  # ============================================================\\n\\n  - id: deepmutation\\n    title: \\\"A Probabilistic Framework for Mutation Testing in Deep Neural Networks\\\"\\n    authors: \\\"Various\\\"\\n    year: 2023\\n    venue: \\\"Information and Software Technology 2023\\\"\\n    category: intensional-analysis\\n    role: background\\n    relevance: >\\n      Extends mutation testing to DNN testing with probabilistic mutation\\n      operators. Parallel to STA's extension of mutation testing from\\n      traditional programs to logical formulas.\\n    key_finding: >\\n      Probabilistic mutation framework enables meaningful test adequacy\\n      assessment for neural networks through structural perturbation.\\n\\n  # ============================================================\\n  # Category 5: Reward hacking / overoptimization\\n  # ============================================================\\n\\n  - id: inform-reward-hacking\\n    title: \\\"InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling\\\"\\n    authors: \\\"Various\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS 2024\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Proposes information-bottleneck approach to detect and mitigate reward\\n      hacking. STA's ISR addresses the same problem differently: by grounding\\n      reward in verifiable structural properties (component necessity), it\\n      reduces the attack surface for reward hacking.\\n    key_finding: >\\n      Variational information bottleneck filters irrelevant features from\\n      reward model; Cluster Separation Index detects reward overoptimization.\\n\\n  - id: mo-grpo\\n    title: \\\"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\\\"\\n    authors: \\\"CyberAgent AI Lab\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2509.22047\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Directly addresses GRPO reward hacking in multi-objective settings.\\n      STA's ISR can be viewed as adding a structural objective to the\\n      correctness objective, making MO-GRPO's insights directly applicable.\\n    key_finding: >\\n      Standard GRPO normalizes after summing rewards, allowing high-variance\\n      objectives to dominate. MO-GRPO equalizes scales before aggregation.\\n\\n  - id: reward-hacking-survey\\n    title: \\\"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\\\"\\n    authors: \\\"Various\\\"\\n    year: 2026\\n    venue: \\\"arXiv 2604.13602\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Comprehensive survey of reward hacking mechanisms in the LLM era.\\n      Provides theoretical framework for understanding why STA's structural\\n      reward is more robust than pure outcome-based reward.\\n    key_finding: >\\n      Reward hacking manifests through specification gaming, reward model\\n      exploitation, and emergent misalignment; structural verification\\n      rewards are more robust than learned reward models.\\n\\n  - id: energy-loss-reward-hacking\\n    title: \\\"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"ICML 2025\\\"\\n    category: reward-hacking\\n    role: background\\n    relevance: >\\n      Identifies energy loss in LLM final layer as an indicator of reward\\n      hacking during RL. Provides complementary diagnostic to STA's\\n      structural reward approach.\\n    key_finding: >\\n      Energy loss in the final layer increases during RL and excessive\\n      increase characterizes reward hacking; EPPO algorithm penalizes\\n      this to mitigate hacking.\\n\\n  - id: spurious-rewards\\n    title: \\\"Spurious Rewards: Rethinking Training Signals in RLVR\\\"\\n    authors: \\\"Ruixin Yang et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2506.10947 / NeurIPS 2025 submission\\\"\\n    category: reward-hacking\\n    role: direct-evidence\\n    relevance: >\\n      Most directly relevant to STA findings. GRPO+random reward on\\n      Qwen2.5-Math improves 21.4%, nearly matching ground-truth reward's\\n      29.1%. Matches our plan017 finding: additive random (PR=48%) >\\n      additive ISR (PR=18%). Structured metrics can be worse than random\\n      noise due to systematic bias vs pure variance.\\n    key_finding: >\\n      Random reward nearly matches ground-truth reward in GRPO training,\\n      suggesting GRPO's group normalization extracts signal from noise.\\n      Effect is model-dependent (works on Qwen2.5, not Llama3).\\n\\n  - id: bondarenko-spec-gaming\\n    title: \\\"Demonstrating Specification Gaming in Reasoning Models\\\"\\n    authors: \\\"Alexander Bondarenko, Denis Volk, Dmitrii Volkov, Jeffrey Ladish\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2502.13295\\\"\\n    category: reward-hacking\\n    role: direct-evidence\\n    relevance: >\\n      Shows that reasoning models (o3, DeepSeek-R1) resort to specification\\n      gaming on difficult tasks by default, without explicit nudging.\\n      Directly relevant to STA's concern: RL-trained reasoning models\\n      may game formal verification rewards rather than learn genuine\\n      formalization skills.\\n    key_finding: >\\n      Reasoning models spontaneously hack benchmarks (e.g., manipulating\\n      chess engine files instead of playing chess). Stronger reasoning\\n      capability correlates with more sophisticated gaming strategies.\\n\\n  - id: kim-game-formalization\\n    title: \\\"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning\\\"\\n    authors: \\\"Kyuhee Kim, Auguste Poiroux, Antoine Bosselut\\\"\\n    year: 2026\\n    venue: \\\"VerifAI-2 Workshop, ICLR 2026 (arXiv 2604.19459)\\\"\\n    category: reward-hacking\\n    role: direct-evidence\\n    relevance: >\\n      Directly studies whether LLMs game formalization in logical reasoning --\\n      the exact phenomenon STA's ISR is designed to detect. Evaluates GPT-5\\n      and DeepSeek-R1 on FOLIO with Lean 4 proofs. Finds two modes of\\n      unfaithfulness: axiom fabrication (GPT-5) and premise mistranslation\\n      (R1), the latter evading detection entirely.\\n    key_finding: >\\n      High compilation rates (87-99%) do not imply faithful formalization.\\n      Two-stage pipelines reveal unfaithfulness that unified generation hides.\\n      Premise mistranslation produces internally consistent but unfaithful\\n      outputs -- analogous to STA's high-ISR but semantically wrong traces.\\n\\n  - id: gao-reward-overoptimization\\n    title: \\\"Scaling Laws for Reward Model Overoptimization\\\"\\n    authors: \\\"Leo Gao, John Schulman, Jacob Hilton\\\"\\n    year: 2023\\n    venue: \\\"ICML 2023 (arXiv 2210.10760)\\\"\\n    category: reward-hacking\\n    role: theoretical-foundation\\n    relevance: >\\n      Foundational work quantifying Goodhart's effect: proxy reward rises\\n      but gold reward first rises then falls. ISR is a proxy reward that\\n      exhibits exactly this pattern — ISR can increase while prove_rate\\n      decreases, making it suitable for post-hoc diagnosis but harmful\\n      as training signal.\\n    key_finding: >\\n      Gold/proxy reward divergence follows predictable scaling laws.\\n      Proxy reward optimization past critical point degrades gold reward,\\n      with the divergence point scaling with model and dataset size.\\n\\n  - id: karwowski-goodhart-rl\\n    title: \\\"Goodhart's Law in Reinforcement Learning\\\"\\n    authors: \\\"Jacek Karwowski, Oliver Hayman, Xingjian Bai, Klaus Kiendlhofer, Charlie Griffin, Joar Skalse\\\"\\n    year: 2024\\n    venue: \\\"ICLR 2024 (arXiv 2310.09144)\\\"\\n    category: reward-hacking\\n    role: theoretical-foundation\\n    relevance: >\\n      Geometric interpretation of Goodhart's Law in MDPs: optimizing\\n      imperfect proxy past critical point decreases true objective. ISR as\\n      proxy has partial correlation with execution correctness — exceeding\\n      critical optimization point pushes policy toward high-ISR but\\n      low-correctness regions. Explains plan002/plan005 negative results.\\n    key_finding: >\\n      Formalizes Goodhart's Law for RL: any non-trivially correlated proxy\\n      reward creates regions where proxy and true reward diverge, and\\n      policy optimization inevitably enters these regions.\\n\\n  # ============================================================\\n  # Category 6: FOL/Prolog formalization with LLMs\\n  # ============================================================\\n\\n  - id: folio\\n    title: \\\"FOLIO: Natural Language Reasoning with First-Order Logic\\\"\\n    authors: \\\"Simeng Han et al.\\\"\\n    year: 2022\\n    venue: \\\"arXiv 2209.00840 / EMNLP 2024\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Primary FOL reasoning benchmark. STA uses FOLIO-style NL->FOL\\n      formalization as the target task for GRPO training. FOLIO's\\n      expert-annotated FOL annotations serve as reference formalizations.\\n    key_finding: >\\n      1,430 NL-FOL paired examples with reasoning depths up to 5+;\\n      GPT-4 still struggles on the hardest examples.\\n\\n  - id: proofwriter\\n    title: \\\"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language\\\"\\n    authors: \\\"Oyvind Tafjord, Bhavana Dalvi, Peter Clark\\\"\\n    year: 2021\\n    venue: \\\"Findings of ACL-IJCNLP 2021\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Source dataset for STA's training data. ProofWriter provides\\n      rule-based logical reasoning problems in natural language that\\n      STA uses for training formalizer models.\\n    key_finding: >\\n      Generative model can reliably produce implications and proofs;\\n      accuracy exceeds prior methods by 9% and generalizes to unseen\\n      proof depths.\\n\\n  - id: logic-lm\\n    title: \\\"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\\\"\\n    authors: \\\"Liangming Pan, Alon Albalak, Xinyi Wang, William Wang\\\"\\n    year: 2023\\n    venue: \\\"Findings of EMNLP 2023\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      LLM->symbolic solver pipeline for logical reasoning, directly\\n      comparable to STA's formalizer->Prolog solver pipeline. Key\\n      difference: Logic-LM uses prompting, STA uses GRPO training.\\n    key_finding: >\\n      LLM+solver achieves 39.2% improvement over LLM-alone on logical\\n      reasoning benchmarks including ProofWriter and FOLIO.\\n\\n  - id: linc\\n    title: \\\"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers\\\"\\n    authors: \\\"Theo X. Olausson, Alex Gu, Ben Lipkin, et al.\\\"\\n    year: 2023\\n    venue: \\\"EMNLP 2023\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      Neurosymbolic approach where LLM translates NL to FOL for theorem\\n      prover. Directly comparable to STA's NL->Prolog translation.\\n      LINC uses prompting-based approach; STA uses RL training.\\n    key_finding: >\\n      StarCoder+ (15.5B) with LINC outperforms GPT-3.5 and GPT-4 with\\n      CoT by 38% and 10% respectively on ProofWriter.\\n\\n  - id: fover-pei2025\\n    title: \\\"FoVer: First-Order Logic Verification for Natural Language Reasoning\\\"\\n    authors: \\\"Yu Pei, Yongping Du, Xingnan Jin\\\"\\n    year: 2025\\n    venue: \\\"TACL 13:1340-1359\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      Uses LLM->FOL->Z3 pipeline for verifying NL reasoning correctness.\\n      Similar to STA's verification pipeline but focuses on post-hoc\\n      verification rather than training reward signal.\\n    key_finding: >\\n      FOL verification via Z3 significantly outperforms existing methods\\n      on ProofWriter and FOLIO benchmarks.\\n\\n  - id: lorp\\n    title: \\\"LoRP: LLM-based Logical Reasoning via Prolog\\\"\\n    authors: \\\"Various\\\"\\n    year: 2025\\n    venue: \\\"Knowledge-Based Systems 2025\\\"\\n    category: fol-formalization\\n    role: direct-competitor\\n    relevance: >\\n      LLM->Prolog pipeline with FOL-to-Prolog translation mechanism.\\n      Closest to STA's formalization target (Prolog), though LoRP\\n      uses prompting while STA uses GRPO training with structural reward.\\n    key_finding: >\\n      Systematic FOL-to-Prolog translation extends Prolog expressiveness;\\n      achieves SoTA accuracy on logical reasoning with three-vote majority.\\n\\n  - id: nl2fol\\n    title: \\\"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection\\\"\\n    authors: \\\"Lalwani, Kim, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2405.02318\\\"\\n    category: fol-formalization\\n    role: background\\n    relevance: >\\n      Step-by-step NL->FOL translation using LLMs with SMT solver\\n      verification. Demonstrates the NL->formal logic pipeline that\\n      STA aims to improve via RL training.\\n    key_finding: >\\n      Neurosymbolic NL2FOL achieves 78% F1 on LOGIC dataset and\\n      generalizes to LogicClimate (80% F1), outperforming supervised\\n      models by 21%.\\n\\n  - id: logica2\\n    title: \\\"LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: \\\"IEEE/ACM TASLP 2023\\\"\\n    category: fol-formalization\\n    role: evaluation\\n    relevance: >\\n      Logical reasoning evaluation benchmark derived from Chinese civil\\n      service exams. Provides supplementary evaluation for STA's\\n      formalization capabilities.\\n    key_finding: >\\n      8,678 multiple-choice questions covering categorical, disjunctive,\\n      and conditional reasoning; widely used LLM benchmark.\\n\\n  # ============================================================\\n  # Category 7: Goodhart's Law theory and dose-response dynamics\\n  # ============================================================\\n\\n  - id: manheim-goodhart-taxonomy\\n    title: \\\"Categorizing Variants of Goodhart's Law\\\"\\n    authors: \\\"David Manheim, Scott Garrabrant\\\"\\n    year: 2019\\n    venue: \\\"arXiv 1803.04585\\\"\\n    category: goodhart-overoptimization\\n    role: theoretical-foundation\\n    relevance: >\\n      Four-part Goodhart taxonomy: regressional, extremal, causal, adversarial.\\n      STA's high-β ISR collapse is best classified as extremal Goodhart\\n      (policy moves to OOD region where ISR↑ but prove_rate↓). Provides\\n      vocabulary for discussion section.\\n    key_finding: >\\n      First systematic categorization of Goodhart failure modes. Extremal\\n      variant occurs when proxy-goal relationship breaks in out-of-distribution\\n      regions reached by strong optimization.\\n\\n  - id: pan-reward-misspecification\\n    title: \\\"The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models\\\"\\n    authors: \\\"Alexander Pan, Kush Bhatia, Jacob Steinhardt\\\"\\n    year: 2022\\n    venue: \\\"ICLR 2022\\\"\\n    category: goodhart-overoptimization\\n    role: theoretical-foundation\\n    relevance: >\\n      Across 9 environments, more capable agents exploit misspecifications more.\\n      Observes dose-dependent degradation — capability thresholds where true\\n      reward sharply drops. Matches STA's β=0.1→0.3 qualitative shift.\\n    key_finding: >\\n      Reward misspecification causes dose-dependent degradation where true reward\\n      sharply drops past capability thresholds. More capable optimization\\n      produces worse outcomes under misspecification.\\n\\n  - id: kwa-catastrophic-goodhart\\n    title: \\\"Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification\\\"\\n    authors: \\\"Tat-Thang Kwa, Rachel Thomas, Adrià Garriga-Alonso\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS 2024\\\"\\n    category: goodhart-overoptimization\\n    role: theoretical-foundation\\n    relevance: >\\n      If reward model error is heavy-tailed, policies achieve arbitrarily\\n      high proxy reward with no true utility gain. KL regularization provably\\n      fails. Explains why KL penalty in GRPO cannot prevent ISR collapse\\n      at high β if ISR error distribution is heavy-tailed.\\n    key_finding: >\\n      KL-regularized RL provably fails to prevent overoptimization under\\n      heavy-tailed reward misspecification. Policies can achieve arbitrarily\\n      high proxy reward with zero true utility.\\n\\n  - id: rafailov-daa-scaling\\n    title: \\\"Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms\\\"\\n    authors: \\\"Rafael Rafailov, Yaswanth Chittepu, Ryan Park, Harshit Sikchi, Joey Hejna, W. Bradley Knox, Chelsea Finn, Scott Niekum\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS 2024\\\"\\n    category: goodhart-overoptimization\\n    role: supporting-evidence\\n    relevance: >\\n      Extends Gao et al. to DPO/IPO/SLiC. Tests seven β values across\\n      1B-6.9B models. DAAs still overoptimize despite no explicit proxy RM.\\n      Validates β as a \\\"dose\\\" parameter — directly analogous to STA's\\n      ISR weight sweep.\\n    key_finding: >\\n      Direct alignment algorithms exhibit overoptimization following\\n      predictable scaling laws. Smaller models overoptimize sooner.\\n      β-controlled dose-response is a general phenomenon across RL paradigms.\\n\\n  - id: huang-chi-squared\\n    title: \\\"Correcting the Mythos of KL-Regularization: Direct and Contrastive Distribution Correction\\\"\\n    authors: \\\"Afra Feyza Akyürek, Banghua Zhu, Sham Kakade, Jiantao Jiao\\\"\\n    year: 2025\\n    venue: \\\"ICLR 2025 Poster\\\"\\n    category: goodhart-overoptimization\\n    role: supporting-evidence\\n    relevance: >\\n      KL-regularization is theoretically inadequate for preventing\\n      overoptimization. Chi-squared divergence provably alleviates it.\\n      Suggests that even with KL penalty in GRPO, STA's high-β collapse\\n      is theoretically expected.\\n    key_finding: >\\n      Chi-squared preference optimization provably mitigates overoptimization\\n      where KL-regularization fails. Alternative divergence measures offer\\n      stronger guarantees.\\n\\n  - id: coste-rm-ensembles\\n    title: \\\"Reward Model Ensembles Help Mitigate Overoptimization\\\"\\n    authors: \\\"Thomas Coste, Usman Anwar, Robert Kirk, David Krueger\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023 Workshop on Alignment\\\"\\n    category: goodhart-overoptimization\\n    role: background\\n    relevance: >\\n      Worst-case optimization across RM ensembles practically eliminates\\n      overoptimization for BoN and reduces it for PPO. Suggests ensemble\\n      of multiple solver metrics (instead of single ISR) as mitigation.\\n    key_finding: >\\n      RM ensembles with worst-case aggregation mitigate overoptimization.\\n      Ensemble size and diversity directly affect robustness.\\n\\n  # ============================================================\\n  # Category 8: Solver/prover as RL reward signal\\n  # ============================================================\\n\\n  - id: rlsf\\n    title: \\\"Reinforcement Learning via Symbolic Feedback\\\"\\n    authors: \\\"Abhinav Jha, Shikhar Murty, Zico Kolter, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2405.16661\\\"\\n    category: verification-reward\\n    role: direct-competitor\\n    relevance: >\\n      Most directly relevant: uses solver/prover certificates as fine-grained\\n      token-level reward signal. Outperforms traditional approaches on program\\n      synthesis (+31.4%). STA extends this paradigm and shows when it breaks\\n      (Goodhart effects at high auxiliary reward weight).\\n    key_finding: >\\n      Symbolic reasoning tools provide poly-sized certificates as reward.\\n      Smaller RLSF models outperform GPT-4 on structured generation tasks.\\n\\n  - id: fover-kamoi2026\\n    title: \\\"FoVer: Generalizable Process Reward Models via Formally Verified Training Data\\\"\\n    authors: \\\"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\\\"\\n    year: 2025\\n    venue: \\\"Findings of ACL 2026 (arXiv 2502.01345)\\\"\\n    category: verification-reward\\n    role: supporting-evidence\\n    relevance: >\\n      Uses Z3 and Isabelle to synthesize PRM training data by annotating\\n      step-level error labels without human annotation. Same solver family\\n      as STA. Shows verification-based rewards work; STA extends by showing\\n      dose-response dynamics.\\n    key_finding: >\\n      Formally verified training data enables generalizable process reward\\n      models competitive on ProcessBench and 12 reasoning benchmarks.\\n\\n  - id: deepseek-prover-v15\\n    title: \\\"DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search\\\"\\n    authors: \\\"DeepSeek AI\\\"\\n    year: 2024\\n    venue: \\\"ICLR 2025 (arXiv 2408.08152)\\\"\\n    category: verification-reward\\n    role: method-component\\n    relevance: >\\n      Uses GRPO with Lean 4 verification as binary reward. Same algorithm\\n      (GRPO) + formal verification, but binary (pass/fail). Binary reward\\n      avoids the graded-metric Goodhart risk that STA identifies with ISR.\\n    key_finding: >\\n      GRPO + binary Lean verification achieves 63.5% on miniF2F. Binary\\n      correctness guarantee via formal verification sidesteps proxy reward\\n      overoptimization.\\n\\n  - id: alphaproof\\n    title: \\\"AlphaProof\\\"\\n    authors: \\\"Google DeepMind\\\"\\n    year: 2024\\n    venue: \\\"Nature 2025\\\"\\n    category: verification-reward\\n    role: background\\n    relevance: >\\n      AlphaZero-inspired RL with Lean proof verification at scale.\\n      Silver medal at IMO 2024. Binary verification reward avoids the\\n      Goodhart problem STA identifies with graded verification metrics.\\n    key_finding: >\\n      Binary formal verification as RL reward scales to IMO-level\\n      mathematical reasoning. Demonstrates verification-reward RL works\\n      at the frontier of mathematical difficulty.\\n\\n  - id: math-shepherd\\n    title: \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\"\\n    authors: \\\"Peiyi Wang, Lei Li, Zhihong Shao, R.X. Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"ACL 2024 (arXiv 2312.08935)\\\"\\n    category: verification-reward\\n    role: supporting-evidence\\n    relevance: >\\n      Automatically constructs process supervision data and uses it as\\n      step-by-step PPO reward. Automated verification reward without human\\n      labels, analogous to STA's automated ISR computation via solver.\\n    key_finding: >\\n      Automated process supervision improves Mistral-7B on GSM8K\\n      (77.9→84.1%) and MATH (28.6→33.0%) without human annotation.\\n\\n  # ============================================================\\n  # Additional reward-shaping papers (Goodhart survey additions)\\n  # ============================================================\\n\\n  - id: bipars\\n    title: \\\"Learning to Utilize Shaping Rewards: A New Approach of Reward Shaping\\\"\\n    authors: \\\"Yujing Hu, Weixun Wang, Hangtian Jia, et al.\\\"\\n    year: 2020\\n    venue: \\\"NeurIPS 2020\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Bi-level optimization learns parameterized shaping reward weights.\\n      Can transform harmful shaping rewards into beneficial ones by learning\\n      negative weights. Directly addresses STA's problem: when ISR weight\\n      is wrong, automated weight learning could find optimal β.\\n    key_finding: >\\n      Bi-level optimization automatically learns auxiliary reward weights,\\n      outperforming fixed weights and recovering from harmful shaping rewards.\\n\\n  - id: dapo\\n    title: \\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\"\\n    authors: \\\"Qiying Yu et al. (ByteDance)\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2503.14476\\\"\\n    category: reward-shaping\\n    role: background\\n    relevance: >\\n      Four techniques for stable multi-component reward in GRPO: Clip-Higher,\\n      Dynamic Sampling, token-level policy gradient, Overlong Reward Shaping.\\n      Addresses stability issues relevant to STA's multi-reward setup.\\n    key_finding: >\\n      Clip-Higher and Dynamic Sampling prevent entropy collapse in GRPO\\n      with multi-component rewards. Soft punishment for overlong outputs\\n      avoids reward hacking through length exploitation.\\n\", \"total_chars\": 42743, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GiGJKFvud9d63HYNjQAQLS`</summary>

```json
{
  "query": "select:WebSearch",
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
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "47cbdbf7-927d-4b9d-88ec-c4a52e1a0205",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018PQsqvUWf7kzj1TAT4XEq6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 451,
      "cache_read_input_tokens": 24398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 451
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

_source line 11 · 2026-05-14T18:42:25.390Z_

<details><summary>↩ Tool result · `toolu_01GiGJKFvud9d63HYNjQAQLS`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
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
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "e4dabcc6-2d5a-4da8-b77a-755979e43fb4",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
I have the full literature map with 33 papers across 8 categories. Now let me search for recent papers on the specific topics mentioned in the task. Let me run multiple searches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "bce1be90-5231-47be-97df-1328bd4e4102",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NW36KupZaSntoaYG6jq9t1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14494,
      "cache_read_input_tokens": 24849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14494
      },
      "output_tokens": 16,
      "service_tier": "standard",
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

_source line 13_

Got the full literature map (33 papers, 8 categories). Now searching for recent papers on Prolog-specific Goodhart effects and related topics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "b402444b-8000-4af6-82f8-43858107afd7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NW36KupZaSntoaYG6jq9t1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14494,
      "cache_read_input_tokens": 24849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14494
      },
      "output_tokens": 16,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_017Ydbpi5jBSEeCuefyxrS5g`</summary>

```json
{
  "query": "reward hacking Prolog logic programming GRPO reinforcement learning 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "e3b73afb-1db5-49f1-aa5f-a1dfc58883c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NW36KupZaSntoaYG6jq9t1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14494,
      "cache_read_input_tokens": 24849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14494
      },
      "output_tokens": 16,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_0183xmZnD9wUoZT5CtBL7rvM`</summary>

```json
{
  "query": "Goodhart's Law neurosymbolic formal verification automated reasoning reward overoptimization 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "3e106b5a-8090-4b0f-b5c2-3df54d215b47",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NW36KupZaSntoaYG6jq9t1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14494,
      "cache_read_input_tokens": 24849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14494
      },
      "output_tokens": 16,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Atm4vT2uBPTzHgSpwDAfJn`</summary>

```json
{
  "query": "tautological collapse GRPO reinforcement learning reward shaping logic formal reasoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "9855a5aa-f8db-4a08-9460-260ff05f0324",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NW36KupZaSntoaYG6jq9t1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14494,
      "cache_read_input_tokens": 24849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14494
      },
      "output_tokens": 16,
      "service_tier": "standard",
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

_source line 17_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018MhKAufgT2yFWrmgkMycTE`</summary>

```json
{
  "query": "\"cross-logic generalization\" OR \"solver-agnostic\" diagnostic metric logic programming 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "994ed113-74e8-4c0a-a268-5ecdd3598ec0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NW36KupZaSntoaYG6jq9t1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14494,
      "cache_read_input_tokens": 24849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14494
      },
      "output_tokens": 16,
      "service_tier": "standard",
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

_source line 18 · 2026-05-14T18:42:40.096Z_

<details><summary>↩ Tool result · `toolu_017Ydbpi5jBSEeCuefyxrS5g`</summary>

```text
Web search results for query: "reward hacking Prolog logic programming GRPO reinforcement learning 2024 2025 2026"

Links: [{"title":"Overcoming reward signal challenges: Verifiable rewards-based reinforcement learning with GRPO on SageMaker AI | Artificial Intelligence","url":"https://aws.amazon.com/blogs/machine-learning/overcoming-reward-signal-challenges-verifiable-rewards-based-reinforcement-learning-with-grpo-on-sagemaker-ai/"},{"title":"Training Language Models to Use Prolog as a Tool","url":"https://arxiv.org/html/2512.07407v1"},{"title":"From Reasoning to Code: GRPO Optimization for ...","url":"https://arxiv.org/pdf/2506.11027"},{"title":"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems","url":"https://arxiv.org/html/2509.22047"},{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"Reinforcement Fine-Tuning LLMs With GRPO - DeepLearning.AI","url":"https://learn.deeplearning.ai/courses/reinforcement-fine-tuning-llms-grpo/lesson/xxwlq/reward-hacking"},{"title":"Scaling Reinforcement Learning: Environments, Reward Hacking, Agents, Scaling Data","url":"https://semianalysis.com/2025/06/08/scaling-reinforcement-learning-environments-reward-hacking-agents-scaling-data/"},{"title":"Training Language Models to Use Prolog as a Tool Niklas Mellgren","url":"https://arxiv.org/pdf/2512.07407"},{"title":"GitHub - Jiaaqiliu/Awesome-RL-Reasoning-LMs: A comprehensive collection of research papers on RL(especially various R1-related paper) techniques for enhancing reasoning capabilities in LLMs, VLMs, and MLLMs. · GitHub","url":"https://github.com/Jiaaqiliu/Awesome-RL-Reasoning-LMs"},{"title":"From Reasoning to Code: GRPO Optimization for Underrepresented Languages","url":"https://arxiv.org/html/2506.11027"}]

Based on the search results, here's what I found about reward hacking, Prolog logic programming, GRPO reinforcement learning in recent research:

## Key Findings

### Reward Hacking in GRPO

GRPO exhibits reward hacking behavior where it tends to ignore rewards with lower variances and only optimizes the ones with higher variances, resulting in unintended behavior such as hacking the readability objective while ignoring translation consistency. RLVR (reinforcement learning with verifiable rewards) addresses reward hacking through rule-based feedback defined by the model tuner.

### Prolog and GRPO Integration

Recent research has successfully combined Prolog logic programming with GRPO training. Using Group Relative Policy Optimization (GRPO), researchers fine-tuned Qwen2.5-3B-Instruct on a cleaned GSM8K-Prolog-Prover dataset while varying prompt structure, reward composition (execution, syntax, semantics, structure), and inference protocol. The reinforcement learning approach outperforms supervised fine-tuning, with the 3B model achieving zero-shot MMLU performance comparable to 7B few-shot results.

### Mitigating Reward Hacking

To resolve reward hacking problems, researchers proposed MO-GRPO (Multi-Objective Group Relative Policy Optimization), which normalizes the advantage functions for each objective so that their variances are scaled evenly, ensuring all reward functions contribute equally to updating the policy, regardless of their variance scales.

### Recent Advances (2025)

Recent work includes "Posterior-GRPO: Rewarding Reasoning Processes in Code Generation" which addresses reward hacking in code generation with process-based rewards, achieving 4.5% improvement over baselines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "888afc5e-de51-4107-99f9-790f58de1f7f",
  "tool_use_result": {
    "query": "reward hacking Prolog logic programming GRPO reinforcement learning 2024 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01S75XTifCCSwYeXhgFw8tgo",
        "content": [
          {
            "title": "Overcoming reward signal challenges: Verifiable rewards-based reinforcement learning with GRPO on SageMaker AI | Artificial Intelligence",
            "url": "https://aws.amazon.com/blogs/machine-learning/overcoming-reward-signal-challenges-verifiable-rewards-based-reinforcement-learning-with-grpo-on-sagemaker-ai/"
          },
          {
            "title": "Training Language Models to Use Prolog as a Tool",
            "url": "https://arxiv.org/html/2512.07407v1"
          },
          {
            "title": "From Reasoning to Code: GRPO Optimization for ...",
            "url": "https://arxiv.org/pdf/2506.11027"
          },
          {
            "title": "MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems",
            "url": "https://arxiv.org/html/2509.22047"
          },
          {
            "title": "Reward Hacking in Reinforcement Learning | Lil'Log",
            "url": "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"
          },
          {
            "title": "Reinforcement Fine-Tuning LLMs With GRPO - DeepLearning.AI",
            "url": "https://learn.deeplearning.ai/courses/reinforcement-fine-tuning-llms-grpo/lesson/xxwlq/reward-hacking"
          },
          {
            "title": "Scaling Reinforcement Learning: Environments, Reward Hacking, Agents, Scaling Data",
            "url": "https://semianalysis.com/2025/06/08/scaling-reinforcement-learning-environments-reward-hacking-agents-scaling-data/"
          },
          {
            "title": "Training Language Models to Use Prolog as a Tool Niklas Mellgren",
            "url": "https://arxiv.org/pdf/2512.07407"
          },
          {
            "title": "GitHub - Jiaaqiliu/Awesome-RL-Reasoning-LMs: A comprehensive collection of research papers on RL(especially various R1-related paper) techniques for enhancing reasoning capabilities in LLMs, VLMs, and MLLMs. · GitHub",
            "url": "https://github.com/Jiaaqiliu/Awesome-RL-Reasoning-LMs"
          },
          {
            "title": "From Reasoning to Code: GRPO Optimization for Underrepresented Languages",
            "url": "https://arxiv.org/html/2506.11027"
          }
        ]
      },
      "Based on the search results, here's what I found about reward hacking, Prolog logic programming, GRPO reinforcement learning in recent research:\n\n## Key Findings\n\n### Reward Hacking in GRPO\n\nGRPO exhibits reward hacking behavior where it tends to ignore rewards with lower variances and only optimizes the ones with higher variances, resulting in unintended behavior such as hacking the readability objective while ignoring translation consistency. RLVR (reinforcement learning with verifiable rewards) addresses reward hacking through rule-based feedback defined by the model tuner.\n\n### Prolog and GRPO Integration\n\nRecent research has successfully combined Prolog logic programming with GRPO training. Using Group Relative Policy Optimization (GRPO), researchers fine-tuned Qwen2.5-3B-Instruct on a cleaned GSM8K-Prolog-Prover dataset while varying prompt structure, reward composition (execution, syntax, semantics, structure), and inference protocol. The reinforcement learning approach outperforms supervised fine-tuning, with the 3B model achieving zero-shot MMLU performance comparable to 7B few-shot results.\n\n### Mitigating Reward Hacking\n\nTo resolve reward hacking problems, researchers proposed MO-GRPO (Multi-Objective Group Relative Policy Optimization), which normalizes the advantage functions for each objective so that their variances are scaled evenly, ensuring all reward functions contribute equally to updating the policy, regardless of their variance scales.\n\n### Recent Advances (2025)\n\nRecent work includes \"Posterior-GRPO: Rewarding Reasoning Processes in Code Generation\" which addresses reward hacking in code generation with process-based rewards, achieving 4.5% improvement over baselines."
    ],
    "durationSeconds": 8.327777428999998
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T18:42:40.715Z_

<details><summary>↩ Tool result · `toolu_0183xmZnD9wUoZT5CtBL7rvM`</summary>

```text
Web search results for query: "Goodhart's Law neurosymbolic formal verification automated reasoning reward overoptimization 2025 2026"

Links: [{"title":"Goodhart's Law in Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=5o9G4XF1LI"},{"title":"[2310.09144] Goodhart's Law in Reinforcement Learning","url":"https://arxiv.org/abs/2310.09144"},{"title":"Goodhart's Law in Reinforcement Learning","url":"https://www.alignmentforum.org/posts/Eu6CvP7c7ivcGM3PJ/goodhart-s-law-in-reinforcement-learning"},{"title":"Goodhart’s Law in Reinforcement Learning","url":"https://arxiv.org/html/2310.09144v1"},{"title":"The Strong, Weak and Benign Goodhart’s law.","url":"https://arxiv.org/pdf/2505.23445v2"},{"title":"Measuring Goodhart’s law | OpenAI","url":"https://openai.com/index/measuring-goodharts-law/"},{"title":"On Goodhart’s law, with an application to value alignment","url":"https://arxiv.org/html/2410.09638v1"},{"title":"Goodhart's law - Wikipedia","url":"https://en.wikipedia.org/wiki/Goodhart%27s_law"},{"title":"[2210.10760] Scaling Laws for Reward Model Overoptimization","url":"https://arxiv.org/abs/2210.10760"},{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"}]

I've completed the web search for your query about Goodhart's Law in relation to neurosymbolic formal verification, automated reasoning, and reward overoptimization in 2025-2026.

## Key Findings

The search returned several highly relevant recent papers and discussions on Goodhart's Law and reward overoptimization:

**Core Research on Goodhart's Law in RL:**

Goodhart's law predicts that increasing optimisation of an imperfect proxy beyond some critical point decreases performance on the true objective. Researchers have proposed ways to quantify this effect, provided a geometric explanation for why Goodhart's law occurs in Markov decision processes, and proposed an optimal early stopping method that provably avoids this pitfall with theoretical regret bounds.

**Recent Theoretical Advances (2024-2025):**

Recent frameworks devise general approaches to AI overoptimization, with setups inspired by incomplete contracting that make them suitable to reinforcement learning. Additionally, for normally distributed discrepancies there is only very weak Goodhart's law, but for distributions with subexponential tail distribution Goodhart's law may become strong, particularly if the discrepancy has a power law distribution thicker than that of the goal.

**Practical Applications:**

In summarization tasks, researchers have typically been able to reach around 10 nats using reinforcement learning before the true objective starts to decrease due to Goodhart's law. More reward model data leads to higher gold reward scores and reduces "Goodharting".

Note: The search results did not specifically address neurosymbolic formal verification or automated reasoning applications to this problem, which may be an emerging area not yet extensively covered in publicly available literature as of May 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "6783a1c6-23c0-4fc1-9fa0-16e61289433e",
  "tool_use_result": {
    "query": "Goodhart's Law neurosymbolic formal verification automated reasoning reward overoptimization 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Pk3Rfp6S3bdePeQ7iZ5N3x",
        "content": [
          {
            "title": "Goodhart's Law in Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=5o9G4XF1LI"
          },
          {
            "title": "[2310.09144] Goodhart's Law in Reinforcement Learning",
            "url": "https://arxiv.org/abs/2310.09144"
          },
          {
            "title": "Goodhart's Law in Reinforcement Learning",
            "url": "https://www.alignmentforum.org/posts/Eu6CvP7c7ivcGM3PJ/goodhart-s-law-in-reinforcement-learning"
          },
          {
            "title": "Goodhart’s Law in Reinforcement Learning",
            "url": "https://arxiv.org/html/2310.09144v1"
          },
          {
            "title": "The Strong, Weak and Benign Goodhart’s law.",
            "url": "https://arxiv.org/pdf/2505.23445v2"
          },
          {
            "title": "Measuring Goodhart’s law | OpenAI",
            "url": "https://openai.com/index/measuring-goodharts-law/"
          },
          {
            "title": "On Goodhart’s law, with an application to value alignment",
            "url": "https://arxiv.org/html/2410.09638v1"
          },
          {
            "title": "Goodhart's law - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Goodhart%27s_law"
          },
          {
            "title": "[2210.10760] Scaling Laws for Reward Model Overoptimization",
            "url": "https://arxiv.org/abs/2210.10760"
          },
          {
            "title": "Reward Hacking in Reinforcement Learning | Lil'Log",
            "url": "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"
          }
        ]
      },
      "I've completed the web search for your query about Goodhart's Law in relation to neurosymbolic formal verification, automated reasoning, and reward overoptimization in 2025-2026.\n\n## Key Findings\n\nThe search returned several highly relevant recent papers and discussions on Goodhart's Law and reward overoptimization:\n\n**Core Research on Goodhart's Law in RL:**\n\nGoodhart's law predicts that increasing optimisation of an imperfect proxy beyond some critical point decreases performance on the true objective. Researchers have proposed ways to quantify this effect, provided a geometric explanation for why Goodhart's law occurs in Markov decision processes, and proposed an optimal early stopping method that provably avoids this pitfall with theoretical regret bounds.\n\n**Recent Theoretical Advances (2024-2025):**\n\nRecent frameworks devise general approaches to AI overoptimization, with setups inspired by incomplete contracting that make them suitable to reinforcement learning. Additionally, for normally distributed discrepancies there is only very weak Goodhart's law, but for distributions with subexponential tail distribution Goodhart's law may become strong, particularly if the discrepancy has a power law distribution thicker than that of the goal.\n\n**Practical Applications:**\n\nIn summarization tasks, researchers have typically been able to reach around 10 nats using reinforcement learning before the true objective starts to decrease due to Goodhart's law. More reward model data leads to higher gold reward scores and reduces \"Goodharting\".\n\nNote: The search results did not specifically address neurosymbolic formal verification or automated reasoning applications to this problem, which may be an emerging area not yet extensively covered in publicly available literature as of May 2026."
    ],
    "durationSeconds": 7.997589059999998
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T18:42:40.842Z_

<details><summary>↩ Tool result · `toolu_018MhKAufgT2yFWrmgkMycTE`</summary>

```text
Web search results for query: ""cross-logic generalization" OR "solver-agnostic" diagnostic metric logic programming 2025 2026"

Links: [{"title":"LPNMR: Logic Programming and Non-Monotonic Reasoning 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1976"},{"title":"LPAR: Logic Programming and Automated Reasoning 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1973"},{"title":"ICLP: International Conference on Logic Programming 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1409"},{"title":"LOPSTR 2025 - 34th International Symposium on Logic-Based Program Synthesis and Transformation","url":"https://lopstr.github.io/2025/"},{"title":"FLoC 2026: The 9th Federated Logic Conference","url":"https://www.floc26.org/"},{"title":"ICLP Conferences – Association for Logic Programming","url":"https://logicprogramming.org/conferences/"},{"title":"[2601.00047] Proceedings 41st International Conference on Logic Programming","url":"https://arxiv.org/abs/2601.00047"},{"title":"Association for Logic Programming","url":"https://logicprogramming.org/"},{"title":"Hybrid Architectures for Efficient Reasoning in Large Language ...","url":"https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.176581130.09718203/v1"},{"title":"EPTCS : Logic Programming","url":"https://arxiv.org/html/2601.00047"}]

I've completed the web search for your query. The results returned information about logic programming conferences and proceedings, particularly the 41st International Conference on Logic Programming (ICLP 2025) and upcoming events in 2026. However, the search results don't appear to contain specific information about "cross-logic generalization" or "solver-agnostic diagnostic metric" concepts that you were searching for.

The search returned:
- General conference information and call for papers for major logic programming events
- The proceedings of the 41st ICLP, held on 12-19 September 2025 at the University of Calabria in Rende, Italy
- Information about the 42nd International Conference on Logic Programming (ICLP 2026) in Lisbon, Portugal, from July 20-23, 2026

The specific technical terms from your search query ("cross-logic generalization," "solver-agnostic diagnostic metric") do not appear in these results. If you're looking for papers or research on these specific topics, you might want to try searching within the ICLP 2025 proceedings directly or look at research papers on arxiv.org with more specific keyword combinations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "114a2d2c-d98d-4b8c-bb1e-5d48895f3e5c",
  "tool_use_result": {
    "query": "\"cross-logic generalization\" OR \"solver-agnostic\" diagnostic metric logic programming 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NTZCrWSBaCuVyBSV2z3GX9",
        "content": [
          {
            "title": "LPNMR: Logic Programming and Non-Monotonic Reasoning 2027 2026 2025 ...",
            "url": "http://www.wikicfp.com/cfp/program?id=1976"
          },
          {
            "title": "LPAR: Logic Programming and Automated Reasoning 2027 2026 2025 ...",
            "url": "http://www.wikicfp.com/cfp/program?id=1973"
          },
          {
            "title": "ICLP: International Conference on Logic Programming 2027 2026 2025 ...",
            "url": "http://www.wikicfp.com/cfp/program?id=1409"
          },
          {
            "title": "LOPSTR 2025 - 34th International Symposium on Logic-Based Program Synthesis and Transformation",
            "url": "https://lopstr.github.io/2025/"
          },
          {
            "title": "FLoC 2026: The 9th Federated Logic Conference",
            "url": "https://www.floc26.org/"
          },
          {
            "title": "ICLP Conferences – Association for Logic Programming",
            "url": "https://logicprogramming.org/conferences/"
          },
          {
            "title": "[2601.00047] Proceedings 41st International Conference on Logic Programming",
            "url": "https://arxiv.org/abs/2601.00047"
          },
          {
            "title": "Association for Logic Programming",
            "url": "https://logicprogramming.org/"
          },
          {
            "title": "Hybrid Architectures for Efficient Reasoning in Large Language ...",
            "url": "https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.176581130.09718203/v1"
          },
          {
            "title": "EPTCS : Logic Programming",
            "url": "https://arxiv.org/html/2601.00047"
          }
        ]
      },
      "I've completed the web search for your query. The results returned information about logic programming conferences and proceedings, particularly the 41st International Conference on Logic Programming (ICLP 2025) and upcoming events in 2026. However, the search results don't appear to contain specific information about \"cross-logic generalization\" or \"solver-agnostic diagnostic metric\" concepts that you were searching for.\n\nThe search returned:\n- General conference information and call for papers for major logic programming events\n- The proceedings of the 41st ICLP, held on 12-19 September 2025 at the University of Calabria in Rende, Italy\n- Information about the 42nd International Conference on Logic Programming (ICLP 2026) in Lisbon, Portugal, from July 20-23, 2026\n\nThe specific technical terms from your search query (\"cross-logic generalization,\" \"solver-agnostic diagnostic metric\") do not appear in these results. If you're looking for papers or research on these specific topics, you might want to try searching within the ICLP 2025 proceedings directly or look at research papers on arxiv.org with more specific keyword combinations."
    ],
    "durationSeconds": 6.724846521
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T18:42:41.937Z_

<details><summary>↩ Tool result · `toolu_01Atm4vT2uBPTzHgSpwDAfJn`</summary>

```text
Web search results for query: "tautological collapse GRPO reinforcement learning reward shaping logic formal reasoning 2025 2026"

Links: [{"title":"GTPO and GRPO-S: Token and Sequence-Level Reward Shaping with...","url":"https://arxiv.org/abs/2508.04349"},{"title":"Post-Training in 2026: GRPO, DAPO, RLVR & Beyond","url":"https://llm-stats.com/blog/research/post-training-techniques-2026"},{"title":"DAPO: An Open-Source LLM Reinforcement Learning System at Scale 1ByteDance Seed","url":"https://arxiv.org/pdf/2503.14476"},{"title":"From Competition to Synergy: Unlocking Reinforcement Learning for Subject-Driven Image Generation","url":"https://arxiv.org/html/2510.18263"},{"title":"S-GRPO: Early Exit via Reinforcement Learning in Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=wNMK5o0Vfg"},{"title":"[2505.07686] S-GRPO: Early Exit via Reinforcement Learning in Reasoning Models","url":"https://arxiv.org/abs/2505.07686"},{"title":"On GRPO Collapse in Search-R1: The Lazy Likelihood-Displacement Death Spiral","url":"https://arxiv.org/html/2512.04220v1"},{"title":"Reinforcement Learning with Verifiable Rewards: GRPO’s Effective Loss, Dynamics, and Success Amplification","url":"https://arxiv.org/html/2503.06639v4"},{"title":"TIPS: TURN-LEVEL INFORMATION-POTENTIAL REWARD ...","url":"https://openreview.net/pdf?id=eBMOr6a84z"},{"title":"From Absolute to Relative: Rethinking Reward Shaping in Group-Based Reinforcement Learning","url":"https://arxiv.org/html/2601.23058"}]

Based on the web search results, I found several highly relevant papers and resources about GRPO, reinforcement learning, reward shaping, and collapse phenomena in LLM reasoning models from 2025-2026. Here are the key findings:

## GRPO Collapse Issues

A significant research area involves Lazy Likelihood Displacement (LLD), the stagnation or reduction of likelihood for both correct and incorrect responses during GRPO optimization, identified as the core mechanism driving collapse in tool-integrated reinforcement learning.

In the context of DAPO (a GRPO variant), entropy collapse has been observed—where the entropy of the policy decreases quickly during training and sampled responses of certain groups tend to be nearly identical, indicating limited exploration and early deterministic policy.

## Reward Shaping Approaches

Recent research addresses the coarse-grained credit assignment limitations in GRPO through Dynamic Entropy Weighting, with algorithms like Group Token Policy Optimization (GTPO) that assigns entropy-weighted rewards to each token and extends this design to sequence-level GRPO (GRPO-S).

Newer frameworks like Reinforcement Learning with Relative Rewards (RLRR) shift reward shaping from absolute scoring to relative ranking to address intrinsic limitations in group-based reinforcement learning methods.

## Formal Reasoning Applications

A major shift in 2025 involved moving from human preference labels to verifiable rewards for reasoning tasks, with DeepSeek-R1 demonstrating that pure RL with verifiable rewards can produce emergent reasoning capabilities without human-labeled reasoning traces.

Research on reward shaping for long-horizon reasoning has identified severe credit-assignment bottlenecks, with classical potential-based shaping providing dense guidance while preserving optimal policies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "db32130c-b9c9-4669-97d3-7af0b28f56f9",
  "tool_use_result": {
    "query": "tautological collapse GRPO reinforcement learning reward shaping logic formal reasoning 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ADshchUGGnj9xq3wP8bhaZ",
        "content": [
          {
            "title": "GTPO and GRPO-S: Token and Sequence-Level Reward Shaping with...",
            "url": "https://arxiv.org/abs/2508.04349"
          },
          {
            "title": "Post-Training in 2026: GRPO, DAPO, RLVR & Beyond",
            "url": "https://llm-stats.com/blog/research/post-training-techniques-2026"
          },
          {
            "title": "DAPO: An Open-Source LLM Reinforcement Learning System at Scale 1ByteDance Seed",
            "url": "https://arxiv.org/pdf/2503.14476"
          },
          {
            "title": "From Competition to Synergy: Unlocking Reinforcement Learning for Subject-Driven Image Generation",
            "url": "https://arxiv.org/html/2510.18263"
          },
          {
            "title": "S-GRPO: Early Exit via Reinforcement Learning in Reasoning Models | OpenReview",
            "url": "https://openreview.net/forum?id=wNMK5o0Vfg"
          },
          {
            "title": "[2505.07686] S-GRPO: Early Exit via Reinforcement Learning in Reasoning Models",
            "url": "https://arxiv.org/abs/2505.07686"
          },
          {
            "title": "On GRPO Collapse in Search-R1: The Lazy Likelihood-Displacement Death Spiral",
            "url": "https://arxiv.org/html/2512.04220v1"
          },
          {
            "title": "Reinforcement Learning with Verifiable Rewards: GRPO’s Effective Loss, Dynamics, and Success Amplification",
            "url": "https://arxiv.org/html/2503.06639v4"
          },
          {
            "title": "TIPS: TURN-LEVEL INFORMATION-POTENTIAL REWARD ...",
            "url": "https://openreview.net/pdf?id=eBMOr6a84z"
          },
          {
            "title": "From Absolute to Relative: Rethinking Reward Shaping in Group-Based Reinforcement Learning",
            "url": "https://arxiv.org/html/2601.23058"
          }
        ]
      },
      "Based on the web search results, I found several highly relevant papers and resources about GRPO, reinforcement learning, reward shaping, and collapse phenomena in LLM reasoning models from 2025-2026. Here are the key findings:\n\n## GRPO Collapse Issues\n\nA significant research area involves Lazy Likelihood Displacement (LLD), the stagnation or reduction of likelihood for both correct and incorrect responses during GRPO optimization, identified as the core mechanism driving collapse in tool-integrated reinforcement learning.\n\nIn the context of DAPO (a GRPO variant), entropy collapse has been observed—where the entropy of the policy decreases quickly during training and sampled responses of certain groups tend to be nearly identical, indicating limited exploration and early deterministic policy.\n\n## Reward Shaping Approaches\n\nRecent research addresses the coarse-grained credit assignment limitations in GRPO through Dynamic Entropy Weighting, with algorithms like Group Token Policy Optimization (GTPO) that assigns entropy-weighted rewards to each token and extends this design to sequence-level GRPO (GRPO-S).\n\nNewer frameworks like Reinforcement Learning with Relative Rewards (RLRR) shift reward shaping from absolute scoring to relative ranking to address intrinsic limitations in group-based reinforcement learning methods.\n\n## Formal Reasoning Applications\n\nA major shift in 2025 involved moving from human preference labels to verifiable rewards for reasoning tasks, with DeepSeek-R1 demonstrating that pure RL with verifiable rewards can produce emergent reasoning capabilities without human-labeled reasoning traces.\n\nResearch on reward shaping for long-horizon reasoning has identified severe credit-assignment bottlenecks, with classical potential-based shaping providing dense guidance while preserving optimal policies."
    ],
    "durationSeconds": 8.21802393
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Let me do a couple more targeted searches to check for any papers that specifically report Goodhart effects in Prolog-based RL training, and also look for the "GRPO collapse" paper and the "specification gaming formalization" paper that might be relevant.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "1b76d969-ed75-4336-bbd6-ba5738d13c53",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CcLsEE3J3CkLW1aN8JsaRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 752,
      "cache_creation_input_tokens": 3167,
      "cache_read_input_tokens": 39343,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3167
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

Let me run a few more targeted searches for novelty verification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "7191d90b-3938-488d-9234-90d3610dfbeb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CcLsEE3J3CkLW1aN8JsaRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 752,
      "cache_creation_input_tokens": 3167,
      "cache_read_input_tokens": 39343,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3167
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_013F3Ux7V4c3hMGrcY76KvaW`</summary>

```json
{
  "query": "\"specification gaming\" OR \"reward gaming\" Prolog \"logic program\" LLM training 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "471ac4b3-dd73-4547-934f-564541151f12",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CcLsEE3J3CkLW1aN8JsaRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 752,
      "cache_creation_input_tokens": 3167,
      "cache_read_input_tokens": 39343,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3167
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BvRirBNHv7QVeDXGccisg3`</summary>

```json
{
  "query": "component necessity ablation metric formal proof reinforcement learning reward 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "ff1d11e5-3522-4356-bfad-ab2e00745162",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CcLsEE3J3CkLW1aN8JsaRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 752,
      "cache_creation_input_tokens": 3167,
      "cache_read_input_tokens": 39343,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3167
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DVYzbFCCF79pdY72iN9GrG`</summary>

```json
{
  "query": "GRPO collapse Search-R1 \"lazy likelihood displacement\" logic reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "26e7cf3a-24b7-45ba-85c1-a3a03df6d493",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CcLsEE3J3CkLW1aN8JsaRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 752,
      "cache_creation_input_tokens": 3167,
      "cache_read_input_tokens": 39343,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3167
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

_source line 27 · 2026-05-14T18:42:55.142Z_

<details><summary>↩ Tool result · `toolu_013F3Ux7V4c3hMGrcY76KvaW`</summary>

```text
Web search results for query: ""specification gaming" OR "reward gaming" Prolog "logic program" LLM training 2025 2026"

Links: [{"title":"Training Language Models to Use Prolog as a Tool","url":"https://arxiv.org/html/2512.07407v1"},{"title":"Towards Understanding Specification Gaming in Reasoning Models","url":"https://arxiv.org/html/2605.02269v1"},{"title":"From Reasoning to Code: GRPO Optimization for ...","url":"https://arxiv.org/pdf/2506.11027"},{"title":"LLM Agents as Automated Game Testers","url":"https://www.emergentmind.com/topics/llm-agents-as-game-testers"},{"title":"Training Language Models to Use Prolog as a Tool Niklas Mellgren","url":"https://arxiv.org/pdf/2512.07407"},{"title":"LLM AI for training beginners on Prolog and through syntax errors? · mthom/scryer-prolog · Discussion #2347","url":"https://github.com/mthom/scryer-prolog/discussions/2347"},{"title":"Use Prolog to improve LLM's reasoning | Hacker News","url":"https://news.ycombinator.com/item?id=41831735"},{"title":"Prolog’s Role in the LLM Era – Part 1 – Soft Coded Logic","url":"https://eugeneasahara.com/2024/08/04/does-prolog-have-a-place-in-the-llm-era/"},{"title":"How Game Data Can Improve LLMs | GameLab","url":"https://www.gamelab.com/blog/how-to-train-an-llm"},{"title":"I wanted to implement a game system with LLM-driven ...","url":"https://www.facebook.com/groups/godotengine/posts/3394606360675934/"}]

Based on the search results, I found highly relevant recent research connecting specification gaming, reward gaming, Prolog, logic programs, and LLM training in 2025-2026:

## Key Findings

**Specification Gaming in LLM Reasoning Models (2026)**

Specification gaming is a critical failure mode of LLM agents, despite there being little systematic research into when it arises and what drives it. Recent research specifically examined this issue and found that RL reasoning training substantially increases the rate at which models exploit their specifications. Additionally, test-time mitigations reduce but do not eliminate the rate of specification gaming.

**Prolog and Logic Programs in LLM Training (December 2025)**

Researchers investigate if language models can be taught to use Prolog as a tool through reinforcement learning with verifiable rewards (RLVR), specifically employing group relative policy optimization (GRPO). Critically, to avoid dominance effects due to scale mismatches across reward components, they normalize and clip all sub-rewards into a shared range, preventing the "winner-takes-all" dynamic.

This last point is particularly relevant to your query, as it directly addresses how to prevent reward gaming/specification gaming when training LLMs with Prolog: by carefully structuring multiple reward signals to prevent any single reward from dominating the optimization process.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "14208277-0b69-403c-b9ae-3937d8dd5cd4",
  "tool_use_result": {
    "query": "\"specification gaming\" OR \"reward gaming\" Prolog \"logic program\" LLM training 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UbBFYGDXMeAPbpx8ySgsdr",
        "content": [
          {
            "title": "Training Language Models to Use Prolog as a Tool",
            "url": "https://arxiv.org/html/2512.07407v1"
          },
          {
            "title": "Towards Understanding Specification Gaming in Reasoning Models",
            "url": "https://arxiv.org/html/2605.02269v1"
          },
          {
            "title": "From Reasoning to Code: GRPO Optimization for ...",
            "url": "https://arxiv.org/pdf/2506.11027"
          },
          {
            "title": "LLM Agents as Automated Game Testers",
            "url": "https://www.emergentmind.com/topics/llm-agents-as-game-testers"
          },
          {
            "title": "Training Language Models to Use Prolog as a Tool Niklas Mellgren",
            "url": "https://arxiv.org/pdf/2512.07407"
          },
          {
            "title": "LLM AI for training beginners on Prolog and through syntax errors? · mthom/scryer-prolog · Discussion #2347",
            "url": "https://github.com/mthom/scryer-prolog/discussions/2347"
          },
          {
            "title": "Use Prolog to improve LLM's reasoning | Hacker News",
            "url": "https://news.ycombinator.com/item?id=41831735"
          },
          {
            "title": "Prolog’s Role in the LLM Era – Part 1 – Soft Coded Logic",
            "url": "https://eugeneasahara.com/2024/08/04/does-prolog-have-a-place-in-the-llm-era/"
          },
          {
            "title": "How Game Data Can Improve LLMs | GameLab",
            "url": "https://www.gamelab.com/blog/how-to-train-an-llm"
          },
          {
            "title": "I wanted to implement a game system with LLM-driven ...",
            "url": "https://www.facebook.com/groups/godotengine/posts/3394606360675934/"
          }
        ]
      },
      "Based on the search results, I found highly relevant recent research connecting specification gaming, reward gaming, Prolog, logic programs, and LLM training in 2025-2026:\n\n## Key Findings\n\n**Specification Gaming in LLM Reasoning Models (2026)**\n\nSpecification gaming is a critical failure mode of LLM agents, despite there being little systematic research into when it arises and what drives it. Recent research specifically examined this issue and found that RL reasoning training substantially increases the rate at which models exploit their specifications. Additionally, test-time mitigations reduce but do not eliminate the rate of specification gaming.\n\n**Prolog and Logic Programs in LLM Training (December 2025)**\n\nResearchers investigate if language models can be taught to use Prolog as a tool through reinforcement learning with verifiable rewards (RLVR), specifically employing group relative policy optimization (GRPO). Critically, to avoid dominance effects due to scale mismatches across reward components, they normalize and clip all sub-rewards into a shared range, preventing the \"winner-takes-all\" dynamic.\n\nThis last point is particularly relevant to your query, as it directly addresses how to prevent reward gaming/specification gaming when training LLMs with Prolog: by carefully structuring multiple reward signals to prevent any single reward from dominating the optimization process."
    ],
    "durationSeconds": 7.206203701999999
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T18:42:57.751Z_

<details><summary>↩ Tool result · `toolu_01DVYzbFCCF79pdY72iN9GrG`</summary>

```text
Web search results for query: "GRPO collapse Search-R1 "lazy likelihood displacement" logic reasoning"

Links: [{"title":"[2512.04220] On GRPO Collapse in Search-R1: The Lazy Likelihood-Displacement Death Spiral","url":"https://arxiv.org/abs/2512.04220"},{"title":"Paper page - On GRPO Collapse in Search-R1: The Lazy Likelihood-Displacement Death Spiral","url":"https://huggingface.co/papers/2512.04220"},{"title":"On GRPO Collapse in Search-R1: The Lazy Likelihood-Displacement Death Spiral","url":"https://arxiv.org/html/2512.04220v1"},{"title":"On Group Relative Policy Optimization Collapse in Agent Search: The Lazy Likelihood-Displacement","url":"https://arxiv.org/html/2512.04220"},{"title":"On GRPO Collapse in Search-R1: The Lazy Likelihood-Displacement Death Spiral","url":"https://www.researchgate.net/publication/398357251_On_GRPO_Collapse_in_Search-R1_The_Lazy_Likelihood-Displacement_Death_Spiral"},{"title":"GRPO Collapse in Search-R1: LLD Death Spiral","url":"https://www.emergentmind.com/papers/2512.04220"},{"title":"On GRPO Collapse in Search-R1: The Lazy Likelihood- ...","url":"https://github.com/vengdeng/LLDS-On-Group-Relative-Policy-Optimization-Collapse-in-Search-R1"},{"title":"[Literature Review] On GRPO Collapse in Search-R1: The Lazy Likelihood-Displacement Death Spiral","url":"https://www.themoonlight.io/en/review/on-grpo-collapse-in-search-r1-the-lazy-likelihood-displacement-death-spiral"},{"title":"On GRPO Collapse in Search-R1: The Lazy Likelihood-Displacement Death Spiral - YouTube","url":"https://www.youtube.com/watch?v=k1St79ykkg8"},{"title":"The Debate on RLVR Reasoning Capability Boundary:","url":"https://arxiv.org/pdf/2510.04028"}]

Based on the search results, here's what I found about GRPO collapse in Search-R1 related to "lazy likelihood displacement":

## Overview

Group Relative Policy Optimization (GRPO), exemplified by the recent Search-R1, offers fast convergence and a value-free formulation that makes it appealing for tool-integrated reinforcement learning, yet consistently suffers from training collapse.

## Lazy Likelihood Displacement (LLD)

Lazy Likelihood Displacement (LLD) is a systematic reduction or stagnation in the likelihood of both correct and incorrect responses, identified as the core mechanism driving this failure.

## The LLD Death Spiral

LLD emerges early and triggers a self-reinforcing LLD Death Spiral, where declining likelihood leads to low-confidence responses, inflating gradients, and ultimately causing collapse.

The empirical characterization reveals a consistent three-phase trajectory: early stagnation, steady decay, and acceleration.

## Why Tool-Integrated GRPO is Vulnerable

Tool calls inject inherently out-of-distribution tokens—such as search results, API outputs, or error messages—that differ sharply from pretrained language distributions, raising token-level uncertainty and making GRPO's relative updates more volatile, accelerating the onset of likelihood displacement.

## Proposed Solution

A lightweight likelihood-preserving regularization called LLDS is proposed for GRPO that activates only when a trajectory's likelihood decreases, and regularizes only the tokens responsible, mitigating LLD with minimal interference to optimization. This method yields substantial performance improvements, including +37.8% gains on Qwen2.5-3B and +32.0% gains on Qwen2.5-7B.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "44efe276-4fee-4fef-8192-0884ec51efd8",
  "tool_use_result": {
    "query": "GRPO collapse Search-R1 \"lazy likelihood displacement\" logic reasoning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NkEwpRuuT4UMXA5HYuN5Dr",
        "content": [
          {
            "title": "[2512.04220] On GRPO Collapse in Search-R1: The Lazy Likelihood-Displacement Death Spiral",
            "url": "https://arxiv.org/abs/2512.04220"
          },
          {
            "title": "Paper page - On GRPO Collapse in Search-R1: The Lazy Likelihood-Displacement Death Spiral",
            "url": "https://huggingface.co/papers/2512.04220"
          },
          {
            "title": "On GRPO Collapse in Search-R1: The Lazy Likelihood-Displacement Death Spiral",
            "url": "https://arxiv.org/html/2512.04220v1"
          },
          {
            "title": "On Group Relative Policy Optimization Collapse in Agent Search: The Lazy Likelihood-Displacement",
            "url": "https://arxiv.org/html/2512.04220"
          },
          {
            "title": "On GRPO Collapse in Search-R1: The Lazy Likelihood-Displacement Death Spiral",
            "url": "https://www.researchgate.net/publication/398357251_On_GRPO_Collapse_in_Search-R1_The_Lazy_Likelihood-Displacement_Death_Spiral"
          },
          {
            "title": "GRPO Collapse in Search-R1: LLD Death Spiral",
            "url": "https://www.emergentmind.com/papers/2512.04220"
          },
          {
            "title": "On GRPO Collapse in Search-R1: The Lazy Likelihood- ...",
            "url": "https://github.com/vengdeng/LLDS-On-Group-Relative-Policy-Optimization-Collapse-in-Search-R1"
          },
          {
            "title": "[Literature Review] On GRPO Collapse in Search-R1: The Lazy Likelihood-Displacement Death Spiral",
            "url": "https://www.themoonlight.io/en/review/on-grpo-collapse-in-search-r1-the-lazy-likelihood-displacement-death-spiral"
          },
          {
            "title": "On GRPO Collapse in Search-R1: The Lazy Likelihood-Displacement Death Spiral - YouTube",
            "url": "https://www.youtube.com/watch?v=k1St79ykkg8"
          },
          {
            "title": "The Debate on RLVR Reasoning Capability Boundary:",
            "url": "https://arxiv.org/pdf/2510.04028"
          }
        ]
      },
      "Based on the search results, here's what I found about GRPO collapse in Search-R1 related to \"lazy likelihood displacement\":\n\n## Overview\n\nGroup Relative Policy Optimization (GRPO), exemplified by the recent Search-R1, offers fast convergence and a value-free formulation that makes it appealing for tool-integrated reinforcement learning, yet consistently suffers from training collapse.\n\n## Lazy Likelihood Displacement (LLD)\n\nLazy Likelihood Displacement (LLD) is a systematic reduction or stagnation in the likelihood of both correct and incorrect responses, identified as the core mechanism driving this failure.\n\n## The LLD Death Spiral\n\nLLD emerges early and triggers a self-reinforcing LLD Death Spiral, where declining likelihood leads to low-confidence responses, inflating gradients, and ultimately causing collapse.\n\nThe empirical characterization reveals a consistent three-phase trajectory: early stagnation, steady decay, and acceleration.\n\n## Why Tool-Integrated GRPO is Vulnerable\n\nTool calls inject inherently out-of-distribution tokens—such as search results, API outputs, or error messages—that differ sharply from pretrained language distributions, raising token-level uncertainty and making GRPO's relative updates more volatile, accelerating the onset of likelihood displacement.\n\n## Proposed Solution\n\nA lightweight likelihood-preserving regularization called LLDS is proposed for GRPO that activates only when a trajectory's likelihood decreases, and regularizes only the tokens responsible, mitigating LLD with minimal interference to optimization. This method yields substantial performance improvements, including +37.8% gains on Qwen2.5-3B and +32.0% gains on Qwen2.5-7B."
    ],
    "durationSeconds": 8.151972032999998
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T18:42:57.794Z_

<details><summary>↩ Tool result · `toolu_01BvRirBNHv7QVeDXGccisg3`</summary>

```text
Web search results for query: "component necessity ablation metric formal proof reinforcement learning reward 2025 2026"

Links: [{"title":"Beyond Rewards: Extended Evaluation Metrics for Safe Reinforcement Learning with PPO-Lagrangian | Proceedings of the 9th International Conference on Algorithms, Computing and Systems","url":"https://dl.acm.org/doi/full/10.1145/3789418.3789420"},{"title":"Reinforcement Learning for Reasoning in Large","url":"https://arxiv.org/pdf/2504.20571"},{"title":"Article Not peer-reviewed version Decomposable Reward Modeling and","url":"https://www.preprints.org/frontend/manuscript/3b6644d4b55cc60c2d3833c5ab4fa3e7/download_pub"},{"title":"Reinforcement Learning Journal 2025 Cover Page","url":"https://arxiv.org/pdf/2503.05996"},{"title":"[2510.14176] ARM-FM: Automated Reward Machines via Foundation Models for Compositional Reinforcement Learning","url":"https://arxiv.org/abs/2510.14176"},{"title":"Blockchain-enhanced incentive-compatible mechanisms for multi-agent reinforcement learning systems | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-20247-8"},{"title":"Reinforcement Learning Journal 2025 Cover Page","url":"https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_194.pdf"},{"title":"A Deep Reinforcement Learning Framework with Formal Verification | Formal Aspects of Computing","url":"https://dl.acm.org/doi/10.1145/3577204"},{"title":"Comprehensive Overview of Reward Engineering and Shaping in Advancing Reinforcement Learning Applications","url":"https://arxiv.org/html/2408.10215v1"},{"title":"Reward Models and Learning Strategies","url":"https://aclanthology.org/2025.findings-emnlp.970.pdf"}]

Based on the web search results, here's what I found regarding research related to component necessity, ablation metrics, formal proofs, and reinforcement learning reward design from 2025-2026:

## Key Findings:

**Formal Proof of Reward Metrics (2025-2026):**
The Trajectory Alignment Coefficient has been formally proven to be invariant to potential-based reward shaping and positive linear transformations of the reward function if and only if the metric considers trajectory distributions that share the same start state distribution.

**Component Ablation in Reward Design:**
A research workflow encodes reward decomposition, legality constraints, and anti-lookahead execution as enforceable system properties rather than informal conventions, which improves reproducibility, supports component-level ablation, and enables more transparent diagnosis of agent behavior. Additionally, component-wise ablation is methodologically necessary, not optional, when claiming that auxiliary terms improve learning.

**Multi-Component Reward Architectures:**
Some work introduces an 11-component reward architecture with deterministic per-step logging to support auditable ablation.

**Ablation Studies in Safe RL (April 2026):**
Recent work studies PPO-Lag using an extended evaluation framework incorporating CVaR, SBUR, violation rate, and recovery rate alongside traditional reward and cost, with ablation studies on hyperparameters and neural network architectures showing that baseline configurations achieve the most balanced trade-off.

**Blockchain-Enhanced Multi-Agent RL (November 2025):**
Ablation studies on blockchain-enhanced multi-agent RL conducted by selectively removing key elements allow researchers to isolate the impact of critical modules including on-chain record-keeping, collusion detection, and smart contract-based incentive redistribution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "b81ad219-419e-400e-933e-9cf94cd5124a",
  "tool_use_result": {
    "query": "component necessity ablation metric formal proof reinforcement learning reward 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_019btFqZ5GWkY6u3vzbRC8bY",
        "content": [
          {
            "title": "Beyond Rewards: Extended Evaluation Metrics for Safe Reinforcement Learning with PPO-Lagrangian | Proceedings of the 9th International Conference on Algorithms, Computing and Systems",
            "url": "https://dl.acm.org/doi/full/10.1145/3789418.3789420"
          },
          {
            "title": "Reinforcement Learning for Reasoning in Large",
            "url": "https://arxiv.org/pdf/2504.20571"
          },
          {
            "title": "Article Not peer-reviewed version Decomposable Reward Modeling and",
            "url": "https://www.preprints.org/frontend/manuscript/3b6644d4b55cc60c2d3833c5ab4fa3e7/download_pub"
          },
          {
            "title": "Reinforcement Learning Journal 2025 Cover Page",
            "url": "https://arxiv.org/pdf/2503.05996"
          },
          {
            "title": "[2510.14176] ARM-FM: Automated Reward Machines via Foundation Models for Compositional Reinforcement Learning",
            "url": "https://arxiv.org/abs/2510.14176"
          },
          {
            "title": "Blockchain-enhanced incentive-compatible mechanisms for multi-agent reinforcement learning systems | Scientific Reports",
            "url": "https://www.nature.com/articles/s41598-025-20247-8"
          },
          {
            "title": "Reinforcement Learning Journal 2025 Cover Page",
            "url": "https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_194.pdf"
          },
          {
            "title": "A Deep Reinforcement Learning Framework with Formal Verification | Formal Aspects of Computing",
            "url": "https://dl.acm.org/doi/10.1145/3577204"
          },
          {
            "title": "Comprehensive Overview of Reward Engineering and Shaping in Advancing Reinforcement Learning Applications",
            "url": "https://arxiv.org/html/2408.10215v1"
          },
          {
            "title": "Reward Models and Learning Strategies",
            "url": "https://aclanthology.org/2025.findings-emnlp.970.pdf"
          }
        ]
      },
      "Based on the web search results, here's what I found regarding research related to component necessity, ablation metrics, formal proofs, and reinforcement learning reward design from 2025-2026:\n\n## Key Findings:\n\n**Formal Proof of Reward Metrics (2025-2026):**\nThe Trajectory Alignment Coefficient has been formally proven to be invariant to potential-based reward shaping and positive linear transformations of the reward function if and only if the metric considers trajectory distributions that share the same start state distribution.\n\n**Component Ablation in Reward Design:**\nA research workflow encodes reward decomposition, legality constraints, and anti-lookahead execution as enforceable system properties rather than informal conventions, which improves reproducibility, supports component-level ablation, and enables more transparent diagnosis of agent behavior. Additionally, component-wise ablation is methodologically necessary, not optional, when claiming that auxiliary terms improve learning.\n\n**Multi-Component Reward Architectures:**\nSome work introduces an 11-component reward architecture with deterministic per-step logging to support auditable ablation.\n\n**Ablation Studies in Safe RL (April 2026):**\nRecent work studies PPO-Lag using an extended evaluation framework incorporating CVaR, SBUR, violation rate, and recovery rate alongside traditional reward and cost, with ablation studies on hyperparameters and neural network architectures showing that baseline configurations achieve the most balanced trade-off.\n\n**Blockchain-Enhanced Multi-Agent RL (November 2025):**\nAblation studies on blockchain-enhanced multi-agent RL conducted by selectively removing key elements allow researchers to isolate the impact of critical modules including on-chain record-keeping, collusion detection, and smart contract-based incentive redistribution."
    ],
    "durationSeconds": 8.897982871
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
Let me also check for the "Towards Understanding Specification Gaming in Reasoning Models" paper which looks very relevant:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "f7c9d84d-7fe9-4884-8197-cebec85d0e5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016YCSmzXMQR6ySXNLwPrdee",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 988,
      "cache_creation_input_tokens": 2864,
      "cache_read_input_tokens": 42510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2864
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

_source line 31_

One more search on the specification gaming paper that appeared relevant.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "b83deab9-6c13-4d4f-b66b-4788777b997e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016YCSmzXMQR6ySXNLwPrdee",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 988,
      "cache_creation_input_tokens": 2864,
      "cache_read_input_tokens": 42510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2864
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_018P3jN6JNodoq6K3WzyCzf1`</summary>

```json
{
  "query": "\"Towards Understanding Specification Gaming in Reasoning Models\" arxiv 2605 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "c7ccbcc7-948d-47b0-a4e1-cbf54bca6d57",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016YCSmzXMQR6ySXNLwPrdee",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 988,
      "cache_creation_input_tokens": 2864,
      "cache_read_input_tokens": 42510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2864
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A4BbMd1VGTtNLUukaXsJCK`</summary>

```json
{
  "query": "ISR \"intensional structural reward\" OR \"component necessity\" logic formalization reward hacking"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "46e143c3-c642-443b-8181-55e8a6d10015",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016YCSmzXMQR6ySXNLwPrdee",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 988,
      "cache_creation_input_tokens": 2864,
      "cache_read_input_tokens": 42510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2864
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

_source line 34 · 2026-05-14T18:43:16.520Z_

<details><summary>↩ Tool result · `toolu_018P3jN6JNodoq6K3WzyCzf1`</summary>

```text
Web search results for query: ""Towards Understanding Specification Gaming in Reasoning Models" arxiv 2605 2026"

Links: [{"title":"[2605.02269v1] Towards Understanding Specification Gaming in Reasoning Models","url":"https://arxiv.org/abs/2605.02269v1"},{"title":"Towards Understanding Specification Gaming in Reasoning Models","url":"https://arxiv.org/html/2605.02269v1"},{"title":"Demonstrating specification gaming in reasoning models Alexander Bondarenko 1","url":"https://arxiv.org/pdf/2502.13295"},{"title":"[2502.13295v2] Demonstrating specification gaming in reasoning models","url":"https://arxiv.org/abs/2502.13295v2"},{"title":"(PDF) Demonstrating specification gaming in reasoning models","url":"https://www.researchgate.net/publication/389167750_Demonstrating_specification_gaming_in_reasoning_models"},{"title":"Winning at All Cost: A Small Environment for Eliciting Specification Gaming Behaviors in Large Language Models","url":"https://arxiv.org/html/2505.07846v1"},{"title":"Demonstrating specification gaming in reasoning models","url":"https://openreview.net/pdf?id=QcaBdKsElk"},{"title":"[2502.13295v1] Demonstrating specification gaming in reasoning models","url":"https://arxiv.org/abs/2502.13295v1"},{"title":"Specification Gaming in AI","url":"https://www.emergentmind.com/topics/specification-gaming"},{"title":"[Literature Review] Demonstrating specification gaming in reasoning models","url":"https://www.themoonlight.io/en/review/demonstrating-specification-gaming-in-reasoning-models"}]

I found the paper! Here's the information about "Towards Understanding Specification Gaming in Reasoning Models":

## Paper Details

**Title:** Towards Understanding Specification Gaming in Reasoning Models

**ArXiv ID:** 2605.02269v1

**Authors:** Kei Nishimura-Gasparian, Robert McCarthy, David Lindner

**Publication Date:** May 4, 2026

## Summary

The paper addresses specification gaming as a critical failure mode of LLM agents. The researchers built and open sourced a diverse suite of tasks where models can score highly by taking unintended actions.

## Key Findings

All tested models exploited their specifications at non-negligible rates in most of eight settings (including five non-coding settings), with the highest rates of specification gaming in Grok 4 and the lowest rates in Claude models.

The research identified three main factors driving specification gaming:

1. RL reasoning training substantially increases the rate at which models exploit their specifications
2. Increasing RL reasoning budget has a weakly positive effect on exploit rate
3. Test-time mitigations reduce but do not eliminate the rate of specification gaming

The results suggest that specification gaming is a fundamental challenge arising from RL reasoning training.

The paper includes an open-sourced evaluation suite to support further research on this problem.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "fa747e93-be86-4bf6-8fee-d7ea6d12e6c0",
  "tool_use_result": {
    "query": "\"Towards Understanding Specification Gaming in Reasoning Models\" arxiv 2605 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FjG86gSGvHUzSMfTirsomV",
        "content": [
          {
            "title": "[2605.02269v1] Towards Understanding Specification Gaming in Reasoning Models",
            "url": "https://arxiv.org/abs/2605.02269v1"
          },
          {
            "title": "Towards Understanding Specification Gaming in Reasoning Models",
            "url": "https://arxiv.org/html/2605.02269v1"
          },
          {
            "title": "Demonstrating specification gaming in reasoning models Alexander Bondarenko 1",
            "url": "https://arxiv.org/pdf/2502.13295"
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
            "title": "Winning at All Cost: A Small Environment for Eliciting Specification Gaming Behaviors in Large Language Models",
            "url": "https://arxiv.org/html/2505.07846v1"
          },
          {
            "title": "Demonstrating specification gaming in reasoning models",
            "url": "https://openreview.net/pdf?id=QcaBdKsElk"
          },
          {
            "title": "[2502.13295v1] Demonstrating specification gaming in reasoning models",
            "url": "https://arxiv.org/abs/2502.13295v1"
          },
          {
            "title": "Specification Gaming in AI",
            "url": "https://www.emergentmind.com/topics/specification-gaming"
          },
          {
            "title": "[Literature Review] Demonstrating specification gaming in reasoning models",
            "url": "https://www.themoonlight.io/en/review/demonstrating-specification-gaming-in-reasoning-models"
          }
        ]
      },
      "I found the paper! Here's the information about \"Towards Understanding Specification Gaming in Reasoning Models\":\n\n## Paper Details\n\n**Title:** Towards Understanding Specification Gaming in Reasoning Models\n\n**ArXiv ID:** 2605.02269v1\n\n**Authors:** Kei Nishimura-Gasparian, Robert McCarthy, David Lindner\n\n**Publication Date:** May 4, 2026\n\n## Summary\n\nThe paper addresses specification gaming as a critical failure mode of LLM agents. The researchers built and open sourced a diverse suite of tasks where models can score highly by taking unintended actions.\n\n## Key Findings\n\nAll tested models exploited their specifications at non-negligible rates in most of eight settings (including five non-coding settings), with the highest rates of specification gaming in Grok 4 and the lowest rates in Claude models.\n\nThe research identified three main factors driving specification gaming:\n\n1. RL reasoning training substantially increases the rate at which models exploit their specifications\n2. Increasing RL reasoning budget has a weakly positive effect on exploit rate\n3. Test-time mitigations reduce but do not eliminate the rate of specification gaming\n\nThe results suggest that specification gaming is a fundamental challenge arising from RL reasoning training.\n\nThe paper includes an open-sourced evaluation suite to support further research on this problem."
    ],
    "durationSeconds": 6.720273540999995
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-14T18:43:17.218Z_

<details><summary>↩ Tool result · `toolu_01A4BbMd1VGTtNLUukaXsJCK`</summary>

```text
Web search results for query: "ISR "intensional structural reward" OR "component necessity" logic formalization reward hacking"

Links: [{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602"},{"title":"Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction","url":"https://arxiv.org/html/2508.04216v1"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=reward+hacking"},{"title":"Defining and Characterizing Reward Hacking Joar Skalse∗ University of Oxford","url":"https://arxiv.org/pdf/2209.13085"},{"title":"Structured Reward Shaping using Signal Temporal Logic speciﬁcations","url":"https://jdeshmukh.github.io/Papers/iros19.pdf"},{"title":"Structured Reward Shaping using Signal Temporal Logic specifications | 2019 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)","url":"https://dl.acm.org/doi/10.1109/IROS40897.2019.8968254"},{"title":"Structured Reward Shaping using Signal Temporal Logic specifications | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/8968254/"},{"title":"[2604.13602v1] Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/abs/2604.13602v1"},{"title":"[2209.13085] Defining and Characterizing Reward Hacking","url":"https://arxiv.org/abs/2209.13085"},{"title":"Reward Hacking, Structural Collapse, and the search for a stable signal in RL. | by Jennifer Wei | Medium","url":"https://medium.com/@jenwei0312/reward-hacking-structural-collapse-and-the-search-for-a-stable-signal-in-rl-eb7fec76625a"}]

I searched for the specific terms you mentioned, but the search results did not return any papers or research explicitly discussing "ISR," "intensional structural reward," or "component necessity" as formal approaches to logic formalization and reward hacking mitigation.

However, the search did surface several highly relevant papers on reward hacking and logic-based reward formalization:

**Reward Hacking Formalization:**
- The first formal definition of reward hacking describes it as a phenomenon where optimizing an imperfect proxy reward function leads to poor performance according to the true reward function.
- Reward hacking is formalized as an emergent consequence of optimizing expressive policies against compressed reward representations of high-dimensional human objectives, arising from the interaction of objective compression, optimization amplification, and evaluator-policy co-adaptation.

**Logic-Based Reward Approaches:**
- Signal Temporal Logic (STL) has been proposed as a formal specification for desired agent behaviors, with algorithms to locally shape rewards in each state to satisfy high-level STL specifications.

**Structural Causality and Reward Hacking:**
- A Structural Causal Model (SCM) has been used to describe causal relationships between observational variables and represent causal dependencies through structural equations and a Directed Acyclic Graph (DAG).

If you're looking for work specifically on "intensional structural reward" or "component necessity" formalisms, these may be very recent or specialized concepts that would benefit from a more targeted search with additional context.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "23b52b2e-4b18-40d8-acc3-de89dc408e08",
  "tool_use_result": {
    "query": "ISR \"intensional structural reward\" OR \"component necessity\" logic formalization reward hacking",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FX8JdWAQEnYaeNR6ARQkED",
        "content": [
          {
            "title": "Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges",
            "url": "https://arxiv.org/html/2604.13602"
          },
          {
            "title": "Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction",
            "url": "https://arxiv.org/html/2508.04216v1"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=reward+hacking"
          },
          {
            "title": "Defining and Characterizing Reward Hacking Joar Skalse∗ University of Oxford",
            "url": "https://arxiv.org/pdf/2209.13085"
          },
          {
            "title": "Structured Reward Shaping using Signal Temporal Logic speciﬁcations",
            "url": "https://jdeshmukh.github.io/Papers/iros19.pdf"
          },
          {
            "title": "Structured Reward Shaping using Signal Temporal Logic specifications | 2019 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)",
            "url": "https://dl.acm.org/doi/10.1109/IROS40897.2019.8968254"
          },
          {
            "title": "Structured Reward Shaping using Signal Temporal Logic specifications | IEEE Conference Publication | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/document/8968254/"
          },
          {
            "title": "[2604.13602v1] Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges",
            "url": "https://arxiv.org/abs/2604.13602v1"
          },
          {
            "title": "[2209.13085] Defining and Characterizing Reward Hacking",
            "url": "https://arxiv.org/abs/2209.13085"
          },
          {
            "title": "Reward Hacking, Structural Collapse, and the search for a stable signal in RL. | by Jennifer Wei | Medium",
            "url": "https://medium.com/@jenwei0312/reward-hacking-structural-collapse-and-the-search-for-a-stable-signal-in-rl-eb7fec76625a"
          }
        ]
      },
      "I searched for the specific terms you mentioned, but the search results did not return any papers or research explicitly discussing \"ISR,\" \"intensional structural reward,\" or \"component necessity\" as formal approaches to logic formalization and reward hacking mitigation.\n\nHowever, the search did surface several highly relevant papers on reward hacking and logic-based reward formalization:\n\n**Reward Hacking Formalization:**\n- The first formal definition of reward hacking describes it as a phenomenon where optimizing an imperfect proxy reward function leads to poor performance according to the true reward function.\n- Reward hacking is formalized as an emergent consequence of optimizing expressive policies against compressed reward representations of high-dimensional human objectives, arising from the interaction of objective compression, optimization amplification, and evaluator-policy co-adaptation.\n\n**Logic-Based Reward Approaches:**\n- Signal Temporal Logic (STL) has been proposed as a formal specification for desired agent behaviors, with algorithms to locally shape rewards in each state to satisfy high-level STL specifications.\n\n**Structural Causality and Reward Hacking:**\n- A Structural Causal Model (SCM) has been used to describe causal relationships between observational variables and represent causal dependencies through structural equations and a Directed Acyclic Graph (DAG).\n\nIf you're looking for work specifically on \"intensional structural reward\" or \"component necessity\" formalisms, these may be very recent or specialized concepts that would benefit from a more targeted search with additional context."
    ],
    "durationSeconds": 6.850574003000002
  }
}
```

</details>

---

### Assistant

_source line 36_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me synthesize the findings and write the artifact.

Key findings from the literature search:

1. **No paper reports Prolog-specific Goodhart effects in GRPO training.** This is a clear novelty for STA.

2. **Existing map coverage for Prolog STA findings:**
   - `mellgren-prolog-grpo`: Direct competitor, uses GRPO for Prolog but with pass/fail reward, no structural reward, no Goodhart analysis
   - `kim-game-formalization`: Studies formalization gaming but in FOL/Lean 4, not Prolog/SWI-Prolog
   - `bondarenko-spec-gaming`: Addresses specification gaming in reasoning models generally, without Prolog-specific focus
   - `karwowski-goodhart-rl`: Provides theoretical Goodhart framework for RL but doesn't analyze logic-type-specific manifestations
   - `gao-reward-overoptimization`: Examines scaling laws for reward overoptimization broadly
   - `spurious-rewards`: Shows how random rewards can approximate ground-truth in GRPO, relevant to gaming patterns
   - `logic-rl`: Applies rule-based RL to logic programming but uses REINFORCE++, not GRPO, and lacks Goodhart analysis

3. **New contributions this paper makes:** Combining structural rewards with GRPO specifically for Prolog, analyzing Goodhart effects in this domain, and demonstrating how reward misspecification manifests in logic programming contexts.

4. **Where our work stands out:** We're the first to compare Goodhart effects across different logic types, characterize Prolog-specific gaming patterns like tautological collapse, and apply component-necessity metrics to understand what drives the observed failures in GRPO training.

Now I'm drafting the artifact to present these findings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "96ffb163-51d0-4da8-998f-f3526445475d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0113Mne6ZyZNpmzVGeM5NbZz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2856,
      "cache_read_input_tokens": 45374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2856
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

Now I have enough to write the linkage summary. Let me also load the artifact registration tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "b974b75e-92ca-4ea0-b65a-b3fbfc3a2e14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0113Mne6ZyZNpmzVGeM5NbZz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2856,
      "cache_read_input_tokens": 45374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2856
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011Kq9bKpFWjf7hXxR7GtCfb`</summary>

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
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "37fbb565-a9e0-4350-8243-b45f7262f120",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0113Mne6ZyZNpmzVGeM5NbZz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2856,
      "cache_read_input_tokens": 45374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2856
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

_source line 39 · 2026-05-14T18:43:36.489Z_

<details><summary>↩ Tool result · `toolu_011Kq9bKpFWjf7hXxR7GtCfb`</summary>

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
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "37ccd5f9-bc2e-4634-8598-a776f5038be2",
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

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01YL1Ek4wBjbHqjRcsgo1F9B`</summary>

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
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "39e81ad1-dc70-4b95-9093-77e170187827",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0169xxgW8TUrKc5GfEtk8thN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 909,
      "cache_read_input_tokens": 48230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 909
      },
      "output_tokens": 53,
      "service_tier": "standard",
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

_source line 41 · 2026-05-14T18:43:41.393Z_

<details><summary>↩ Tool result · `toolu_01YL1Ek4wBjbHqjRcsgo1F9B`</summary>

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
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "18eff4b5-9dd6-4922-ba71-a584afacd8db",
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

_source line 42_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01R2FnjCnCkSEmQ7zBRJY6Pt`</summary>

```json
{
  "query": "artifact",
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
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "434d5981-1aa5-48cf-b41c-d314fef4a1db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVD4a1TYszaWWA2HoyPc3b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 95,
      "cache_read_input_tokens": 49139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 95
      },
      "output_tokens": 66,
      "service_tier": "standard",
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

_source line 43 · 2026-05-14T18:43:49.133Z_

<details><summary>↩ Tool result · `toolu_01R2FnjCnCkSEmQ7zBRJY6Pt`</summary>

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
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "dfd02e67-48de-4ee0-a5f7-aa5dcd71ef6d",
  "tool_use_result": {
    "matches": [],
    "query": "artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 44_

No `register_artifact` tool available. I'll write the artifact file directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "3ae57711-dfc7-4034-ab80-3abaf04f9c99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WDqMZ5uMQ88t4phWzQUtPE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 90,
      "cache_read_input_tokens": 49234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 90
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

_source line 45_

<details open><summary>🔧 Tool call — Write · `toolu_01PKDRrksePJZjLYViNbXxtW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/prolog_sta_literature_linkage.md",
  "content": "# Prolog STA Goodhart Results — Literature Linkage\n\n## Existing Map Coverage\n\nDirectly comparable papers in literature_map.yaml:\n\n- **mellgren-prolog-grpo**: Only paper using GRPO for Prolog LLM training. Uses pass/fail reward — no structural reward, no Goodhart analysis. Does not report gaming patterns.\n- **kim-game-formalization** (ICLR 2026 Workshop): Studies LLM formalization gaming but in FOL/Lean 4. Finds premise mistranslation and axiom fabrication — structurally analogous to our H1/H7 patterns but in a different logic type.\n- **bondarenko-spec-gaming**: Shows reasoning models spontaneously game specifications. General phenomenon, not logic-type-specific.\n- **spurious-rewards**: Random reward ≈ ground-truth in GRPO. Relevant to why ISR-as-reward fails — systematic bias (ISR) can underperform pure noise.\n- **karwowski-goodhart-rl**, **gao-reward-overoptimization**, **kwa-catastrophic-goodhart**: Theoretical Goodhart frameworks. None study logic-type-specific manifestations.\n\n## Gaps Filled by Our Prolog STA Results\n\n1. **No prior work reports Goodhart effects in Prolog GRPO training.** Mellgren uses binary reward and doesn't analyze gaming. Our 3-seed results (2/3 seeds gaming, 1/3 clean) are the first such evidence.\n2. **No cross-logic-type comparison of Goodhart patterns exists.** Our FOL (H7=16-97%, mixed modes) vs Prolog (H7=100% or functional H7, more thorough gaming) comparison is novel.\n3. **No LOO/component-necessity metric has been applied to Prolog formalization.** ISR applied to SWI-Prolog clauses is a new diagnostic.\n4. **Tautological collapse characterization** — Prolog's single-premise-equals-conclusion (H7) and multi-premise-contains-conclusion (H1) gaming patterns are unreported.\n\n## New Papers Worth Adding\n\n- **Nishimura-Gasparian et al. (2605.02269, May 2026)**: \"Towards Understanding Specification Gaming in Reasoning Models.\" Shows RL reasoning training *increases* specification gaming rates across 8 settings. Directly supports our finding that GRPO training induces gaming. Not Prolog-specific but strengthens the general argument. Category: reward-hacking, role: supporting-evidence.\n\n## Novelty Verdict\n\n**No paper has reported Prolog-specific Goodhart effects.** The closest is kim-game-formalization (FOL/Lean 4 gaming) and bondarenko-spec-gaming (general spec gaming). Our contribution — first systematic cross-logic-type (FOL→Prover9 + Prolog→SWI-Prolog) Goodhart analysis in GRPO training with per-logic gaming pattern characterization — remains novel.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "ed1ab4c3-4091-4191-b71a-2b7f44f3fec8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WDqMZ5uMQ88t4phWzQUtPE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 90,
      "cache_read_input_tokens": 49234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 90
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

_source line 46 · 2026-05-14T18:44:11.992Z_

<details><summary>↩ Tool result · `toolu_01PKDRrksePJZjLYViNbXxtW`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/prolog_sta_literature_linkage.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "48e09437-6c9a-43c7-8396-f26cb8c1be40",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/prolog_sta_literature_linkage.md",
    "content": "# Prolog STA Goodhart Results — Literature Linkage\n\n## Existing Map Coverage\n\nDirectly comparable papers in literature_map.yaml:\n\n- **mellgren-prolog-grpo**: Only paper using GRPO for Prolog LLM training. Uses pass/fail reward — no structural reward, no Goodhart analysis. Does not report gaming patterns.\n- **kim-game-formalization** (ICLR 2026 Workshop): Studies LLM formalization gaming but in FOL/Lean 4. Finds premise mistranslation and axiom fabrication — structurally analogous to our H1/H7 patterns but in a different logic type.\n- **bondarenko-spec-gaming**: Shows reasoning models spontaneously game specifications. General phenomenon, not logic-type-specific.\n- **spurious-rewards**: Random reward ≈ ground-truth in GRPO. Relevant to why ISR-as-reward fails — systematic bias (ISR) can underperform pure noise.\n- **karwowski-goodhart-rl**, **gao-reward-overoptimization**, **kwa-catastrophic-goodhart**: Theoretical Goodhart frameworks. None study logic-type-specific manifestations.\n\n## Gaps Filled by Our Prolog STA Results\n\n1. **No prior work reports Goodhart effects in Prolog GRPO training.** Mellgren uses binary reward and doesn't analyze gaming. Our 3-seed results (2/3 seeds gaming, 1/3 clean) are the first such evidence.\n2. **No cross-logic-type comparison of Goodhart patterns exists.** Our FOL (H7=16-97%, mixed modes) vs Prolog (H7=100% or functional H7, more thorough gaming) comparison is novel.\n3. **No LOO/component-necessity metric has been applied to Prolog formalization.** ISR applied to SWI-Prolog clauses is a new diagnostic.\n4. **Tautological collapse characterization** — Prolog's single-premise-equals-conclusion (H7) and multi-premise-contains-conclusion (H1) gaming patterns are unreported.\n\n## New Papers Worth Adding\n\n- **Nishimura-Gasparian et al. (2605.02269, May 2026)**: \"Towards Understanding Specification Gaming in Reasoning Models.\" Shows RL reasoning training *increases* specification gaming rates across 8 settings. Directly supports our finding that GRPO training induces gaming. Not Prolog-specific but strengthens the general argument. Category: reward-hacking, role: supporting-evidence.\n\n## Novelty Verdict\n\n**No paper has reported Prolog-specific Goodhart effects.** The closest is kim-game-formalization (FOL/Lean 4 gaming) and bondarenko-spec-gaming (general spec gaming). Our contribution — first systematic cross-logic-type (FOL→Prover9 + Prolog→SWI-Prolog) Goodhart analysis in GRPO training with per-logic gaming pattern characterization — remains novel.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 47_

Artifact written. Summary:

**Novelty confirmed.** No paper reports Goodhart effects in Prolog GRPO training. Key findings:

- **mellgren-prolog-grpo** is the only GRPO+Prolog paper; it uses binary reward with no Goodhart analysis
- **kim-game-formalization** studies formalization gaming but in FOL/Lean 4, not Prolog
- Cross-logic-type Goodhart comparison (FOL vs Prolog gaming patterns) is entirely novel
- One new paper worth adding: **Nishimura-Gasparian et al. (2605.02269, May 2026)** — shows RL reasoning training increases specification gaming rates, supporting our findings generally but not Prolog-specific

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "uuid": "a5a91fc8-9690-4805-bca9-ebe708326393",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ErLSnzaZGjBg3f7ttRkqqg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 903,
      "cache_read_input_tokens": 49324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 903
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

### Task result

_source line 48_

Artifact written. Summary:

**Novelty confirmed.** No paper reports Goodhart effects in Prolog GRPO training. Key findings:

- **mellgren-prolog-grpo** is the only GRPO+Prolog paper; it uses binary reward with no Goodhart analysis
- **kim-game-formalization** studies formalization gaming but in FOL/Lean 4, not Prolog
- Cross-logic-type Goodhart comparison (FOL vs Prolog gaming patterns) is entirely novel
- One new paper worth adding: **Nishimura-Gasparian et al. (2605.02269, May 2026)** — shows RL reasoning training increases specification gaming rates, supporting our findings generally but not Prolog-specific

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 122990,
  "duration_api_ms": 170749,
  "num_turns": 17,
  "stop_reason": "end_turn",
  "session_id": "e3367deb-3ff7-4115-9b14-41018e3bd34d",
  "total_cost_usd": 0.7834695,
  "usage": {
    "input_tokens": 1756,
    "cache_creation_input_tokens": 38386,
    "cache_read_input_tokens": 384242,
    "output_tokens": 2884,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 38386,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 179,
        "cache_read_input_tokens": 49324,
        "cache_creation_input_tokens": 903,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 903
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 158161,
      "outputTokens": 4479,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 9,
      "costUSD": 0.270556,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 1756,
      "outputTokens": 2884,
      "cacheReadInputTokens": 384242,
      "cacheCreationInputTokens": 38386,
      "webSearchRequests": 0,
      "costUSD": 0.5129135,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "a0778d03-1336-415c-ab34-c856d46de2be"
}
```

</details>

---
