# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-27 (UTC).** ## Original idea { "tit

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/c61f05f5-597a-4fa1-8ef1-d83c1f03bb02.jsonl`
- **Structured JSON:** [`b41080ce8f589075b421.json`](../../sessions/b4/b41080ce8f589075b421.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T17:51:21.326Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T17:51:21.326Z",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-27 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Verifier-Certified Progress Rewards via Sorry-Driven Decomposition\",\n  \"core_problem\": \"RL training for theorem provers relies on binary success/fail rewards, creating severe reward sparsity on hard problems where the model makes substantial partial progress but receives zero signal. Can we use the Lean compiler itself to provide exact, dense progress measurements?\",\n  \"opportunity\": \"Mechanic (March 2026) demonstrated that sorry-driven fault isolation can precisely identify which subgoals in a proof are solved vs. unsolved while preserving verified proof structure. Meanwhile, ProD (NeurIPS 2024) showed that rewarding intermediate lemma correctness improves decomposition learning, and LeanProgress (TMLR 2025) validated that dense progress signals improve proof search. However, no system combines sorry-verified subgoal completion ratios as RL reward — ProD rewards individual lemmas without measuring progress on the original problem, and LeanProgress uses a learned (noisy) step predictor rather than exact compiler verification. The sorry mechanism provides a unique, compiler-certified 'fraction-of-problem-solved' signal that is both exact and structurally faithful.\",\n  \"landscape\": \"Current RL for theorem proving uses binary reward: Lean compiler accepts the full proof (reward=1) or rejects it (reward=0). DeepSeek-Prover-V2 uses GRPO with binary reward plus a consistency bonus. Goedel-Prover-V2 and Kimina-Prover similarly use binary verification reward. LeanProgress (2025) predicts remaining proof steps via a learned model (75.8% accuracy, MAE 3.15), providing approximate dense signal. ProD (NeurIPS 2024) rewards correct intermediate lemmas but doesn't measure progress on the original theorem. FormalRewardBench (May 2026) benchmarks reward models for theorem proving but focuses on learned verifiers, not compiler-derived signals. Process-Verified RL (NeurIPS 2025) uses Lean's tactic-level elaboration as a process reward oracle, providing dense credit at the individual tactic granularity — related but fundamentally different from subgoal-level progress measurement. Milestones over Outcome (SGVR, January 2026) applies sub-goal verifiable reward ratios to geometric reasoning via GRPO, achieving +9.7% on geometry benchmarks — conceptually analogous but operates on numeric sub-goals in geometry, not sorry-verified formal proof subgoals. SorryDB (March 2026) curates sorry-bearing theorems from real Lean repositories, providing a natural evaluation testbed. The sorry-driven approach is fundamentally different from all of the above: decompose via sorry → count compiler-verified solved subgoals → reward = verified_subgoals / total_subgoals. This is exact (no model error), structurally grounded (respects proof dependencies), and naturally curriculum-calibrated (harder problems decompose into more subgoals).\",\n  \"inspired_by\": \"Field guide gap 'Scaling laws for iterative self-correction are unknown' + pattern 'Verifier-as-Swiss-Army-Knife' (using verifier as reward signal AND curriculum generator) + pattern 'Subgoal decomposition as data synthesis strategy' (decomposition generates both training signal and training data) + Mechanic system (sorry-driven isolation, March 2026)\",\n  \"approach\": \"We implement a Sorry-Progress Reward (SPR) for GRPO-style RL training of formal theorem provers. Given a model-generated proof attempt for theorem T, a sorrifier module (adapted from Mechanic) decomposes it into k subgoals with sorry placeholders for unresolved parts; the Lean 4 compiler then type-checks the structure, yielding reward = verified_subgoals / total_subgoals in [0,1]. This compiler-certified fractional reward replaces the standard binary verification signal, providing exact dense feedback without any learned approximation. We train Goedel-Prover-V2-8B (current strongest open-source 8B prover, 84.6% pass@32 on MiniF2F) using the open-source Kimina-Prover-RL pipeline with Verl/GRPO, comparing SPR against binary reward, Process-Verified RL tactic-level reward, and LeanProgress on MiniF2F-test and PutnamBench, with particular focus on sample efficiency gains on hard problems where binary reward yields near-zero signal. We additionally explore sorry-weighted rewards (weighting subgoals by proof-tree depth) and sorry-driven curriculum scheduling (training first on problems where the model resolves most subgoals, then gradually increasing difficulty).\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"2000-3000 H100-hours (sorry-reward wrapper + sorrifier integration: 500h dev/debug on GPU; RL training of 8B model across 4 ablations × ~500h each; evaluation sweeps ~200h)\",\n      \"timeline\": \"10-12 weeks (3 weeks sorry-reward + Lean API integration, 2 weeks RL infra on Kimina-Prover-RL/Verl, 4 weeks training + ablations, 2 weeks evaluation + paper)\",\n      \"estimated_gpu_cost\": \"$5,000-$7,500 (at $2.50/H100-hour spot pricing, May 2026 market rate)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"2000-2500 H100-hours (same training budget, reduced debugging via Claude-assisted Lean4 code generation)\",\n      \"timeline\": \"7-9 weeks (Claude accelerates sorrifier integration and GRPO reward-shaping implementation by ~40%)\",\n      \"claude_api_cost\": \"$250-400 (implementation assistance, experiment analysis, paper drafting)\",\n      \"estimated_gpu_cost\": \"$5,000-$6,250\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"2500-3500 H100-hours (additional automated hyperparameter exploration and ablation sweeps)\",\n      \"timeline\": \"5-7 weeks (parallel experiment orchestration, automated evaluation pipelines)\",\n      \"claude_api_cost\": \"$500-800 (code generation, experiment orchestration, automated paper drafting)\",\n      \"estimated_gpu_cost\": \"$6,250-$8,750\",\n      \"speed_bottleneck\": \"Lean 4 compilation latency (~2-5s per sorry-verification call) during RL rollouts; each GRPO group of 8-16 samples requires sequential Lean type-checking, creating a verification throughput ceiling of ~300-700 verifications/GPU-hour that dominates wall-clock time over model forward passes\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (abstract: July 21, 2026; full paper: July 28, 2026 — confirmed)\",\n    \"ICLR 2027 (predicted ~October 2026 based on ICLR 2026 September 24 pattern — not yet announced)\",\n    \"ICML 2027 (predicted ~January 2027 based on ICML 2026 January 23/28 pattern — not yet announced)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Mechanic: Sorrifier-Driven Formal Decomposition Workflow for Automated Theorem Proving (arXiv 2026)\",\n    \"Formal Theorem Proving by Rewarding LLMs to Decompose Proofs Hierarchically [ProD] (NeurIPS 2024)\",\n    \"LeanProgress: Guiding Search for Neural Theorem Proving via Proof Progress Prediction (TMLR 2025)\",\n    \"FormalRewardBench: A Benchmark for Formal Theorem Proving Reward Models (arXiv 2026)\",\n    \"DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition (arXiv 2025)\",\n    \"Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction (arXiv 2025)\",\n    \"Kimina-Prover Preview: Towards Large Formal Reasoning Models with Reinforcement Learning (arXiv 2025)\",\n    \"Process-Verified Reinforcement Learning for Theorem Proving via Lean (NeurIPS 2025)\",\n    \"Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward (arXiv 2026)\",\n    \"SorryDB: Can AI Provers Complete Real-World Lean Theorems? (arXiv 2026)\"\n  ],\n  \"description\": \"We propose Sorry-Progress Reward (SPR), a dense RL reward signal for training formal theorem provers that uses the Lean 4 compiler's sorry mechanism to provide exact, verifier-certified measurements of partial proof progress. Current RL training relies on binary success/fail rewards, creating severe sparsity on hard problems. SPR addresses this by decomposing proof attempts via sorry-driven isolation (following Mechanic's sorrifier): each attempt yields k subgoals, and the Lean compiler verifies which are resolved, producing reward = verified_subgoals / total_subgoals. Unlike learned progress predictors (LeanProgress, 75.8% accuracy) or individual lemma rewards (ProD), SPR is exact (zero model error), structurally faithful (respects proof dependencies), and naturally curriculum-calibrated (harder problems yield more subgoals). Unlike Process-Verified RL's tactic-level credit, SPR measures meaningful mathematical progress on the original theorem. We integrate SPR into GRPO training of Goedel-Prover-V2-8B via the open-source Kimina-Prover-RL pipeline, benchmarking on MiniF2F-test and PutnamBench with focus on hard-problem sample efficiency where binary reward provides near-zero learning signal.\",\n  \"project_name\": \"sorry_progress_reward\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 1)\nIssues: [\"CRITICAL: Does not address user's requirement for 'Autoformalization' — the idea is purely about RL reward shaping for formal proof generation, not bridging informal and formal mathematical reasoning\", \"Process-Verified RL venue error: published at ICLR 2026 (Poster), NOT NeurIPS 2025 as cited\", \"ProD is a NeurIPS 2024 MATH-AI Workshop paper, not a main-track NeurIPS paper — citation is misleading\", \"Missing critical reference: Hilbert (ICLR 2026) — uses sorry-based recursive decomposition at inference time, achieves 99.2% on miniF2F and 70.0% on PutnamBench. Most closely related work using sorry for formal proof decomposition\", \"Missing critical reference: AlphaProof (Nature, Feb 2025) — handles multi-subgoal returns in formal RL (min-over-subgoals rather than mean), directly relevant to reward design choices\", \"Missing reference: Proof-Verifier (ICLR 2026) — addresses same problem (dense reward for theorem proving RL) via learned verifier, achieving 93% verification accuracy\", \"Missing reference: VeRPO (arXiv Jan 2026) — conceptually analogous partial-completion ratio reward for code generation RL\", \"Mechanic's sorrifier is NOT available as a modularized component (paper explicitly states this is future work), creating a major implementation dependency risk\", \"Novelty over SGVR is thin: SGVR already implements skeleton_rate = verified_subgoals/total_subgoals as GRPO reward; SPR is essentially 'SGVR for formal proofs' with compiler verification\", \"MiniF2F benchmark saturation: Hilbert 99.2%, BFS-Prover-V2 95.08%, Seed-Prover saturates it — this reduces the evaluation value of MiniF2F as a primary metric\"]\nFeedback: The core technical idea (sorry-verified subgoal completion ratio as dense RL reward) has genuine merit but needs significant revisions: (1) Most critically, reframe or extend to address autoformalization — e.g., use SPR to train models that bridge informal proof sketches to formal proofs, connecting to Hilbert's paradigm. (2) Add and discuss Hilbert, AlphaProof, VeRPO, and Proof-Verifier as related work — you must articulate why SPR's subgoal-level signal is superior to Process-Verified RL's tactic-level signal and how it differs from SGVR beyond the domain. (3) Fix the venue errors (Process-Verified RL → ICLR 2026; ProD → NeurIPS 2024 Workshop). (4) Address the sorrifier availability risk — either confirm code access from the Mechanic authors or plan to reimplement the sorrifier from scratch (add time/cost). (5) Consider replacing MiniF2F as primary benchmark with harder benchmarks (PutnamBench, SorryDB, ProofNet) where reward sparsity actually matters. (6) Strengthen the novelty argument by emphasizing what sorry-level progress measurement provides over tactic-level (Process-Verified RL): mathematical meaningfulness, structural faithfulness to proof dependencies, and natural curriculum calibration.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.\n- Address each issue specifically.\n\n## 深度调研要求\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。\n3. **深度思考**：\n   - 核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach？\n4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。\n\n## 针对 Review 意见的定向搜索\n\n1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点\n2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline\n3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现\n4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot\n\n- You have full freedom: minor fix, major revision, or pivot.\n- Include a \"change_type\" field: \"minor\", \"major\", or \"pivot\".\n- Output a COMPLETE JSON object with ALL fields."
}
```

---

### Runtime record

_source line 2 · 2026-05-27T17:51:21.329Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T17:51:21.329Z",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02"
}
```

---

## Round 1

38 recorded events

### User

_source line 3 · 2026-05-27T17:51:21.342Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-27 (UTC).**

## Original idea
{
  "title": "Verifier-Certified Progress Rewards via Sorry-Driven Decomposition",
  "core_problem": "RL training for theorem provers relies on binary success/fail rewards, creating severe reward sparsity on hard problems where the model makes substantial partial progress but receives zero signal. Can we use the Lean compiler itself to provide exact, dense progress measurements?",
  "opportunity": "Mechanic (March 2026) demonstrated that sorry-driven fault isolation can precisely identify which subgoals in a proof are solved vs. unsolved while preserving verified proof structure. Meanwhile, ProD (NeurIPS 2024) showed that rewarding intermediate lemma correctness improves decomposition learning, and LeanProgress (TMLR 2025) validated that dense progress signals improve proof search. However, no system combines sorry-verified subgoal completion ratios as RL reward — ProD rewards individual lemmas without measuring progress on the original problem, and LeanProgress uses a learned (noisy) step predictor rather than exact compiler verification. The sorry mechanism provides a unique, compiler-certified 'fraction-of-problem-solved' signal that is both exact and structurally faithful.",
  "landscape": "Current RL for theorem proving uses binary reward: Lean compiler accepts the full proof (reward=1) or rejects it (reward=0). DeepSeek-Prover-V2 uses GRPO with binary reward plus a consistency bonus. Goedel-Prover-V2 and Kimina-Prover similarly use binary verification reward. LeanProgress (2025) predicts remaining proof steps via a learned model (75.8% accuracy, MAE 3.15), providing approximate dense signal. ProD (NeurIPS 2024) rewards correct intermediate lemmas but doesn't measure progress on the original theorem. FormalRewardBench (May 2026) benchmarks reward models for theorem proving but focuses on learned verifiers, not compiler-derived signals. Process-Verified RL (NeurIPS 2025) uses Lean's tactic-level elaboration as a process reward oracle, providing dense credit at the individual tactic granularity — related but fundamentally different from subgoal-level progress measurement. Milestones over Outcome (SGVR, January 2026) applies sub-goal verifiable reward ratios to geometric reasoning via GRPO, achieving +9.7% on geometry benchmarks — conceptually analogous but operates on numeric sub-goals in geometry, not sorry-verified formal proof subgoals. SorryDB (March 2026) curates sorry-bearing theorems from real Lean repositories, providing a natural evaluation testbed. The sorry-driven approach is fundamentally different from all of the above: decompose via sorry → count compiler-verified solved subgoals → reward = verified_subgoals / total_subgoals. This is exact (no model error), structurally grounded (respects proof dependencies), and naturally curriculum-calibrated (harder problems decompose into more subgoals).",
  "inspired_by": "Field guide gap 'Scaling laws for iterative self-correction are unknown' + pattern 'Verifier-as-Swiss-Army-Knife' (using verifier as reward signal AND curriculum generator) + pattern 'Subgoal decomposition as data synthesis strategy' (decomposition generates both training signal and training data) + Mechanic system (sorry-driven isolation, March 2026)",
  "approach": "We implement a Sorry-Progress Reward (SPR) for GRPO-style RL training of formal theorem provers. Given a model-generated proof attempt for theorem T, a sorrifier module (adapted from Mechanic) decomposes it into k subgoals with sorry placeholders for unresolved parts; the Lean 4 compiler then type-checks the structure, yielding reward = verified_subgoals / total_subgoals in [0,1]. This compiler-certified fractional reward replaces the standard binary verification signal, providing exact dense feedback without any learned approximation. We train Goedel-Prover-V2-8B (current strongest open-source 8B prover, 84.6% pass@32 on MiniF2F) using the open-source Kimina-Prover-RL pipeline with Verl/GRPO, comparing SPR against binary reward, Process-Verified RL tactic-level reward, and LeanProgress on MiniF2F-test and PutnamBench, with particular focus on sample efficiency gains on hard problems where binary reward yields near-zero signal. We additionally explore sorry-weighted rewards (weighting subgoals by proof-tree depth) and sorry-driven curriculum scheduling (training first on problems where the model resolves most subgoals, then gradually increasing difficulty).",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "2000-3000 H100-hours (sorry-reward wrapper + sorrifier integration: 500h dev/debug on GPU; RL training of 8B model across 4 ablations × ~500h each; evaluation sweeps ~200h)",
      "timeline": "10-12 weeks (3 weeks sorry-reward + Lean API integration, 2 weeks RL infra on Kimina-Prover-RL/Verl, 4 weeks training + ablations, 2 weeks evaluation + paper)",
      "estimated_gpu_cost": "$5,000-$7,500 (at $2.50/H100-hour spot pricing, May 2026 market rate)"
    },
    "human_in_loop": {
      "gpu_hours": "2000-2500 H100-hours (same training budget, reduced debugging via Claude-assisted Lean4 code generation)",
      "timeline": "7-9 weeks (Claude accelerates sorrifier integration and GRPO reward-shaping implementation by ~40%)",
      "claude_api_cost": "$250-400 (implementation assistance, experiment analysis, paper drafting)",
      "estimated_gpu_cost": "$5,000-$6,250"
    },
    "auto_research": {
      "gpu_hours": "2500-3500 H100-hours (additional automated hyperparameter exploration and ablation sweeps)",
      "timeline": "5-7 weeks (parallel experiment orchestration, automated evaluation pipelines)",
      "claude_api_cost": "$500-800 (code generation, experiment orchestration, automated paper drafting)",
      "estimated_gpu_cost": "$6,250-$8,750",
      "speed_bottleneck": "Lean 4 compilation latency (~2-5s per sorry-verification call) during RL rollouts; each GRPO group of 8-16 samples requires sequential Lean type-checking, creating a verification throughput ceiling of ~300-700 verifications/GPU-hour that dominates wall-clock time over model forward passes"
    }
  },
  "target_venues": [
    "AAAI 2027 (abstract: July 21, 2026; full paper: July 28, 2026 — confirmed)",
    "ICLR 2027 (predicted ~October 2026 based on ICLR 2026 September 24 pattern — not yet announced)",
    "ICML 2027 (predicted ~January 2027 based on ICML 2026 January 23/28 pattern — not yet announced)"
  ],
  "level": "solid",
  "key_references": [
    "Mechanic: Sorrifier-Driven Formal Decomposition Workflow for Automated Theorem Proving (arXiv 2026)",
    "Formal Theorem Proving by Rewarding LLMs to Decompose Proofs Hierarchically [ProD] (NeurIPS 2024)",
    "LeanProgress: Guiding Search for Neural Theorem Proving via Proof Progress Prediction (TMLR 2025)",
    "FormalRewardBench: A Benchmark for Formal Theorem Proving Reward Models (arXiv 2026)",
    "DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition (arXiv 2025)",
    "Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction (arXiv 2025)",
    "Kimina-Prover Preview: Towards Large Formal Reasoning Models with Reinforcement Learning (arXiv 2025)",
    "Process-Verified Reinforcement Learning for Theorem Proving via Lean (NeurIPS 2025)",
    "Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward (arXiv 2026)",
    "SorryDB: Can AI Provers Complete Real-World Lean Theorems? (arXiv 2026)"
  ],
  "description": "We propose Sorry-Progress Reward (SPR), a dense RL reward signal for training formal theorem provers that uses the Lean 4 compiler's sorry mechanism to provide exact, verifier-certified measurements of partial proof progress. Current RL training relies on binary success/fail rewards, creating severe sparsity on hard problems. SPR addresses this by decomposing proof attempts via sorry-driven isolation (following Mechanic's sorrifier): each attempt yields k subgoals, and the Lean compiler verifies which are resolved, producing reward = verified_subgoals / total_subgoals. Unlike learned progress predictors (LeanProgress, 75.8% accuracy) or individual lemma rewards (ProD), SPR is exact (zero model error), structurally faithful (respects proof dependencies), and naturally curriculum-calibrated (harder problems yield more subgoals). Unlike Process-Verified RL's tactic-level credit, SPR measures meaningful mathematical progress on the original theorem. We integrate SPR into GRPO training of Goedel-Prover-V2-8B via the open-source Kimina-Prover-RL pipeline, benchmarking on MiniF2F-test and PutnamBench with focus on hard-problem sample efficiency where binary reward provides near-zero learning signal.",
  "project_name": "sorry_progress_reward",
  "source": "web_research"
}

## Reviewer feedback (round 1)
Issues: ["CRITICAL: Does not address user's requirement for 'Autoformalization' — the idea is purely about RL reward shaping for formal proof generation, not bridging informal and formal mathematical reasoning", "Process-Verified RL venue error: published at ICLR 2026 (Poster), NOT NeurIPS 2025 as cited", "ProD is a NeurIPS 2024 MATH-AI Workshop paper, not a main-track NeurIPS paper — citation is misleading", "Missing critical reference: Hilbert (ICLR 2026) — uses sorry-based recursive decomposition at inference time, achieves 99.2% on miniF2F and 70.0% on PutnamBench. Most closely related work using sorry for formal proof decomposition", "Missing critical reference: AlphaProof (Nature, Feb 2025) — handles multi-subgoal returns in formal RL (min-over-subgoals rather than mean), directly relevant to reward design choices", "Missing reference: Proof-Verifier (ICLR 2026) — addresses same problem (dense reward for theorem proving RL) via learned verifier, achieving 93% verification accuracy", "Missing reference: VeRPO (arXiv Jan 2026) — conceptually analogous partial-completion ratio reward for code generation RL", "Mechanic's sorrifier is NOT available as a modularized component (paper explicitly states this is future work), creating a major implementation dependency risk", "Novelty over SGVR is thin: SGVR already implements skeleton_rate = verified_subgoals/total_subgoals as GRPO reward; SPR is essentially 'SGVR for formal proofs' with compiler verification", "MiniF2F benchmark saturation: Hilbert 99.2%, BFS-Prover-V2 95.08%, Seed-Prover saturates it — this reduces the evaluation value of MiniF2F as a primary metric"]
Feedback: The core technical idea (sorry-verified subgoal completion ratio as dense RL reward) has genuine merit but needs significant revisions: (1) Most critically, reframe or extend to address autoformalization — e.g., use SPR to train models that bridge informal proof sketches to formal proofs, connecting to Hilbert's paradigm. (2) Add and discuss Hilbert, AlphaProof, VeRPO, and Proof-Verifier as related work — you must articulate why SPR's subgoal-level signal is superior to Process-Verified RL's tactic-level signal and how it differs from SGVR beyond the domain. (3) Fix the venue errors (Process-Verified RL → ICLR 2026; ProD → NeurIPS 2024 Workshop). (4) Address the sorrifier availability risk — either confirm code access from the Mechanic authors or plan to reimplement the sorrifier from scratch (add time/cost). (5) Consider replacing MiniF2F as primary benchmark with harder benchmarks (PutnamBench, SorryDB, ProofNet) where reward sparsity actually matters. (6) Strengthen the novelty argument by emphasizing what sorry-level progress measurement provides over tactic-level (Process-Verified RL): mathematical meaningfulness, structural faithfulness to proof dependencies, and natural curriculum calibration.

## Instructions
- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.
- Address each issue specifically.

## 深度调研要求

不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。

1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。
2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。
3. **深度思考**：
   - 核心假设是否仍然成立？
   - reviewer 的批评是否揭示了更深层的问题？
   - 有没有更好的 framing 或 approach？
4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。

## 针对 Review 意见的定向搜索

1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点
2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline
3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现
4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot

- You have full freedom: minor fix, major revision, or pivot.
- Include a "change_type" field: "minor", "major", or "pivot".
- Output a COMPLETE JSON object with ALL fields.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "c8f8bb74-4b57-4255-9fe8-15c0a5831ab6",
  "type": "user",
  "uuid": "045f8b6f-bc11-4aba-a44c-231af79d9e3e",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T17:51:21.341Z_

```json
{
  "parentUuid": "045f8b6f-bc11-4aba-a44c-231af79d9e3e",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "92f41d60-1d10-4360-9325-8d0452ce6da4",
  "timestamp": "2026-05-27T17:51:21.341Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T17:51:21.341Z_

```json
{
  "parentUuid": "92f41d60-1d10-4360-9325-8d0452ce6da4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "afd8aac8-a64d-4fb7-8a63-d8c44c97397e",
  "timestamp": "2026-05-27T17:51:21.341Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise sorry-progress reward to address autoformalization gap",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02"
}
```

---

### Assistant

_source line 7 · 2026-05-27T17:51:30.823Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully and plan my research accordingly. The key issues are:

1. **CRITICAL**: Need to address autoformalization - bridging informal and formal mathematical reasoning
2. **Venue errors**: Process-Verified RL → ICLR 2026; ProD → NeurIPS 2024 Workshop
3. **Missing references**: Hilbert, AlphaProof, Proof-Verifier, VeRPO
4. **Sorrifier availability risk**: Mechanic's sorrifier not modularized
5. **MiniF2F saturation**: Need harder benchmarks


6. **Novelty over SGVR**: Need stronger differentiation
7. **Novelty over Process-Verified RL**: Need to articulate why subgoal-level > tactic-level

I need to dive into the literature on these specific papers - Hilbert's sorry-based recursive decomposition, AlphaProof's multi-subgoal returns, Proof-Verifier, and VeRPO - to understand how they relate to my work and where I can establish clearer differentiation.

I should also investigate autoformalization with sorry mechanisms, check what the current SOTA is on MiniF2F and other benchmarks, and see what the sorrifier implementation looks like. Let me spin up parallel research agents to tackle these simultaneously.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afd8aac8-a64d-4fb7-8a63-d8c44c97397e",
  "isSidechain": false,
  "requestId": "req_011CbTVrJMzb8HsDU135rF2Z",
  "type": "assistant",
  "uuid": "82064276-0545-4791-813c-59dd80ea7fab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019AndjdiEQjnZviJQPhvBj3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5060,
      "cache_read_input_tokens": 11014,
      "output_tokens": 456,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5060,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 456,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 5060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5060
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-27T17:51:30.825Z_

I'll conduct deep research on each reviewer concern in parallel before revising the idea. Let me launch multiple research agents simultaneously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82064276-0545-4791-813c-59dd80ea7fab",
  "isSidechain": false,
  "requestId": "req_011CbTVrJMzb8HsDU135rF2Z",
  "type": "assistant",
  "uuid": "1bc91920-24a2-4764-a7c2-3f26f90572eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019AndjdiEQjnZviJQPhvBj3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5060,
      "cache_read_input_tokens": 11014,
      "output_tokens": 456,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5060,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 456,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 5060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5060
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-27T17:51:31.242Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DMedpSZV5imiguo7L5B68p`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bc91920-24a2-4764-a7c2-3f26f90572eb",
  "isSidechain": false,
  "requestId": "req_011CbTVrJMzb8HsDU135rF2Z",
  "type": "assistant",
  "uuid": "c43fa063-4044-4216-8aea-f7f1b6d362d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019AndjdiEQjnZviJQPhvBj3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5060,
      "cache_read_input_tokens": 11014,
      "output_tokens": 456,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5060,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 456,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 5060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5060
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-27T17:51:31.250Z_

<details><summary>↩ Tool result · `toolu_01DMedpSZV5imiguo7L5B68p`</summary>

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
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c43fa063-4044-4216-8aea-f7f1b6d362d1",
  "isSidechain": false,
  "promptId": "c8f8bb74-4b57-4255-9fe8-15c0a5831ab6",
  "type": "user",
  "uuid": "ef12164f-df35-410b-8e43-4fa654a154a6",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "c43fa063-4044-4216-8aea-f7f1b6d362d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Verifier-Certified Progress Rewards via Sorry-Driven Decomposition\",…",
  "leafUuid": "ef12164f-df35-410b-8e43-4fa654a154a6",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise sorry-progress reward to address autoformalization gap",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02"
}
```

---

### Assistant

_source line 13 · 2026-05-27T17:51:34.713Z_

Now let me launch parallel research agents to investigate each major reviewer concern deeply.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef12164f-df35-410b-8e43-4fa654a154a6",
  "isSidechain": false,
  "requestId": "req_011CbTVs2qNg2uSwBLtXytXo",
  "type": "assistant",
  "uuid": "e68afe1f-5fd0-4b2c-8d18-e0037a662fe3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QeoRdHrEAxhk3T1vASoH5P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1476,
      "cache_read_input_tokens": 16074,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 363,
          "cache_read_input_tokens": 16074,
          "cache_creation_input_tokens": 1476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1476
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-27T17:51:42.984Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01FLmFxaGQqBB8T9n6EUhenw`</summary>

```json
{
  "description": "Research Hilbert ICLR 2026",
  "prompt": "I need to deeply research the paper \"Hilbert\" published at ICLR 2026 that uses sorry-based recursive decomposition for theorem proving and achieves 99.2% on miniF2F and 70.0% on PutnamBench.\n\nPlease:\n1. Search for \"Hilbert ICLR 2026 sorry decomposition theorem proving\" and related queries\n2. Fetch and read the actual paper (arXiv or OpenReview)\n3. Extract:\n   - Full title and authors\n   - How exactly they use sorry for decomposition\n   - Their approach (inference-time? training-time? both?)\n   - Key results (miniF2F, PutnamBench, other benchmarks)\n   - How they handle subgoal verification\n   - Whether they do any RL training or just inference-time search\n   - Their relation to Mechanic's sorrifier\n   - Any discussion of using sorry-completion as RL reward signal\n   - GitHub repo availability and code status\n\nReport in detail (500+ words). This is critical for positioning our work.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e68afe1f-5fd0-4b2c-8d18-e0037a662fe3",
  "isSidechain": false,
  "requestId": "req_011CbTVs2qNg2uSwBLtXytXo",
  "type": "assistant",
  "uuid": "aa12feb2-f97b-4776-a35b-9959f251a287",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QeoRdHrEAxhk3T1vASoH5P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1476,
      "cache_read_input_tokens": 16074,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 363,
          "cache_read_input_tokens": 16074,
          "cache_creation_input_tokens": 1476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1476
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-27T17:54:51.764Z_

<details><summary>↩ Tool result · `toolu_01FLmFxaGQqBB8T9n6EUhenw`</summary>

```text
I now have comprehensive information. Here is the detailed report.

---

## Hilbert: Recursively Building Formal Proofs with Informal Reasoning -- Detailed Research Report

### Full Title and Authors

**Title:** "Hilbert: Recursively Building Formal Proofs with Informal Reasoning"

**Authors:** Sumanth Varambally, Thomas Voice, Yanchao Sun, Zhifeng Chen, Rose Yu, Ke Ye

**Affiliations:** UC San Diego (Varambally, Rose Yu) and Apple (Voice, Sun, Chen, Ke Ye)

**Publication:** ICLR 2026 (also appeared at MATH-AI Workshop at NeurIPS 2025). arXiv: 2509.22819 (submitted September 2025, revised March 2026).

---

### How Sorry Is Used for Decomposition

Hilbert's core mechanism is **recursive sorry-based subgoal decomposition** in Lean 4. The process works as follows:

1. **Proof sketch generation:** The Reasoner LLM (Gemini 2.5 Pro or Flash) first generates a natural-language step-by-step proof. It then translates this into a Lean 4 proof sketch consisting of `have` statements, where each subgoal's proof body is filled with `sorry` -- Lean's placeholder keyword that the type-checker temporarily accepts as a valid proof of any proposition. The prompts explicitly instruct: "Use `sorry` for all subgoal proofs -- focus on structure, not implementation" and "Do NOT use `sorry` for the main goal proof -- use your subgoals to prove it."

2. **Sketch compilation and correction:** The sorry-laden sketch is compiled against the Lean verifier. Because `sorry` is accepted by Lean, this validates the *logical structure* (that the subgoals, if proven, would actually prove the main theorem) without requiring the subgoals themselves to be proven yet. If compilation fails, error messages are fed back to the Reasoner for iterative correction (up to 4 attempts).

3. **Subgoal extraction:** Each `have` statement with a `sorry` placeholder is extracted as an independent theorem statement.

4. **Assembly:** Once subgoal theorems are proven, the Reasoner produces an assembled proof replacing each `sorry` placeholder with calls to the corresponding subgoal theorem.

5. **Recursive application:** If a subgoal cannot be proven directly, it is itself decomposed using the same sorry-sketch process, up to a maximum recursion depth D=5.

This is distinct from prior approaches (DSP, LEGO-Prover) which could decompose once but not recursively decompose subgoals that remained too difficult.

---

### Approach: Inference-Time Only (No RL Training)

**Hilbert is purely an inference-time system.** There is no reinforcement learning training, no fine-tuning, and no reward signals. The system orchestrates four pre-existing components at inference time:

1. **Reasoner:** Gemini 2.5 Flash or Pro (general-purpose LLM for informal math reasoning, sketch generation, assembly)
2. **Prover:** DeepSeek-Prover-V2-7B or Goedel-Prover-V2-32B (specialized Lean 4 tactic generation model)
3. **Verifier:** Kimina Lean Server (Lean v4.15.0 with Mathlib v4.15.0)
4. **Retriever:** Sentence-transformer-based semantic search over Mathlib theorems (all-mpnet-base-v2 embeddings)

The paper explicitly notes that future work could use "proofs and reasoning traces generated by Hilbert to train better Prover and Reasoner models," creating a "virtuous cycle" -- but this is stated as future direction, not something they did. **There is no RL reward signal, no sorry-completion reward, and no training loop in the current system.**

---

### Subgoal Verification Process

For each extracted subgoal, Hilbert applies a cascading four-stage strategy:

1. **Direct prover attempt:** The Prover LLM generates 4 candidate proofs; if any compiles, the subgoal is done.
2. **Mathematical correctness check:** The Reasoner evaluates whether the subgoal is mathematically sound (to avoid wasting compute on ill-formed subgoals).
3. **Shallow solve:** The Reasoner writes short proofs (max 30 lines) using retrieved Mathlib theorems, with iterative refinement from verifier error feedback (up to 6 correction passes).
4. **Recursive decomposition:** If all above fail and depth < D, the subgoal is itself decomposed via the same sorry-sketch process.

---

### Key Results

**miniF2F-Test (244 problems):**
- Hilbert + Gemini 2.5 Pro + Goedel-Prover-V2-32B: **99.2%** (6.6 percentage points above best prior public method)
- Hilbert + Gemini 2.5 Flash + DeepSeek-Prover-V2-7B: **96.7%** (+35.4% over pass@4 baseline of the prover alone)
- Standalone prover at D=0 (no decomposition): 75%

**PutnamBench (660 problems):**
- Hilbert: **462/660 (70.0%)**
- SeedProver (proprietary): 50.4%
- Best prior public baseline: ~13.4%
- This is a **422% improvement** over the best publicly available baseline

**Ablation findings:**
- Recursion depth D=3 achieves near-optimal performance (98.7% on miniF2F); diminishing returns beyond that
- Theorem retrieval reduces both compute and improves accuracy (98.4% vs 97.1% with DeepSeek Prover)
- Best configuration: ~4.5K reasoner calls and 11.3K total LLM calls per problem (substantially fewer than DeltaProver's 16,384 calls with the same reasoner)

---

### Relation to Mechanic's Sorrifier

Hilbert and Mechanic (Qiu et al., 2026, arXiv: 2603.24465) both use `sorry` for decomposition but differ fundamentally in their approach:

- **Hilbert uses "informal decomposition":** The Reasoner generates a sorry-sketch *proactively* from an informal proof plan. When a proof fails entirely, Hilbert discards the formal proof and regenerates a new informal sketch from scratch.
- **Mechanic uses "formal decomposition" via a Sorrifier:** When a proof attempt *fails compilation*, Mechanic's Sorrifier surgically replaces only the innermost failing code block with `sorry`, iteratively recompiling until the proof compiles. This preserves verified structure and extracts only the truly unresolved subgoals, avoiding redundant re-analysis.

Mechanic benchmarks against Hilbert as a baseline. On Putnam 2025 (12 problems), Mechanic solved 11 with better efficiency (114 min avg vs. higher for other systems). Mechanic's key claim is that formal decomposition is more efficient for complex problems because it does not discard valid proof segments.

---

### Sorry-Completion as RL Reward Signal

**Neither Hilbert nor Mechanic discusses using sorry-completion as an RL reward signal.** Hilbert's paper mentions the possibility of using generated proofs to train better models as future work, but does not formalize this as a reward signal. This appears to be an open research direction that neither paper has explored.

---

### Code Availability

**GitHub repository:** [https://github.com/apple/ml-hilbert](https://github.com/apple/ml-hilbert) (Apple's official release)

**Active fork:** [https://github.com/Rose-STL-Lab/ml-hilbert](https://github.com/Rose-STL-Lab/ml-hilbert) (maintained by primary author Varambally)

The Apple repo has 18 stars, 9 forks, 2 commits, and is described as "not in active development" with the active fork at Rose-STL-Lab. The code includes inference pipeline code (`src/`), config files, and requires kimina-lean-server, sentence-transformers, and OpenAI-compatible LLM endpoints. It is inference-only code -- no training code is included. Licensed under CC BY 4.0.

---

### Key Takeaways for Positioning

1. Hilbert is inference-time only with no RL -- the sorry-completion-as-reward-signal idea is entirely unexplored territory that could differentiate your work.
2. Hilbert's sorry usage is "proactive" (plan-then-sorry), while Mechanic's is "reactive" (fail-then-sorrify). A training-time approach using sorry as reward signal would be a third, distinct paradigm.
3. The 99.2% miniF2F and 70.0% PutnamBench numbers are the current SOTA to beat or compare against.
4. Hilbert explicitly flags training on its own traces as future work -- if your approach does this, you are directly addressing their stated open problem.
5. Code is available but minimal (18 stars), suggesting the community has not yet deeply engaged with reproducing or extending this work.

Sources:
- [Hilbert paper on arXiv](https://arxiv.org/abs/2509.22819)
- [Hilbert HTML version](https://arxiv.org/html/2509.22819v1)
- [Hilbert on OpenReview (ICLR 2026)](https://openreview.net/forum?id=GN8OdkTo3B)
- [Apple ML Research page](https://machinelearning.apple.com/research/hilbert)
- [GitHub: apple/ml-hilbert](https://github.com/apple/ml-hilbert)
- [GitHub: Rose-STL-Lab/ml-hilbert (active fork)](https://github.com/Rose-STL-Lab/ml-hilbert)
- [Mechanic paper (arXiv)](https://arxiv.org/html/2603.24465)
- [Hilbert Quick Review on Liner](https://liner.com/review/hilbert-recursively-building-formal-proofs-with-informal-reasoning)

agentId: a0f2d98692977fe44 (use SendMessage with to: 'a0f2d98692977fe44' to continue this agent)
&lt;usage>total_tokens: 23989
tool_uses: 14
duration_ms: 188773&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa12feb2-f97b-4776-a35b-9959f251a287",
  "isSidechain": false,
  "promptId": "c8f8bb74-4b57-4255-9fe8-15c0a5831ab6",
  "type": "user",
  "uuid": "352722f1-259c-4e2b-9a81-7cfba56f2ebf",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to deeply research the paper \"Hilbert\" published at ICLR 2026 that uses sorry-based recursive decomposition for theorem proving and achieves 99.2% on miniF2F and 70.0% on PutnamBench.\n\nPlease:\n1. Search for \"Hilbert ICLR 2026 sorry decomposition theorem proving\" and related queries\n2. Fetch and read the actual paper (arXiv or OpenReview)\n3. Extract:\n   - Full title and authors\n   - How exactly they use sorry for decomposition\n   - Their approach (inference-time? training-time? both?)\n   - Key results (miniF2F, PutnamBench, other benchmarks)\n   - How they handle subgoal verification\n   - Whether they do any RL training or just inference-time search\n   - Their relation to Mechanic's sorrifier\n   - Any discussion of using sorry-completion as RL reward signal\n   - GitHub repo availability and code status\n\nReport in detail (500+ words). This is critical for positioning our work.",
    "agentId": "a0f2d98692977fe44",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information. Here is the detailed report.\n\n---\n\n## Hilbert: Recursively Building Formal Proofs with Informal Reasoning -- Detailed Research Report\n\n### Full Title and Authors\n\n**Title:** \"Hilbert: Recursively Building Formal Proofs with Informal Reasoning\"\n\n**Authors:** Sumanth Varambally, Thomas Voice, Yanchao Sun, Zhifeng Chen, Rose Yu, Ke Ye\n\n**Affiliations:** UC San Diego (Varambally, Rose Yu) and Apple (Voice, Sun, Chen, Ke Ye)\n\n**Publication:** ICLR 2026 (also appeared at MATH-AI Workshop at NeurIPS 2025). arXiv: 2509.22819 (submitted September 2025, revised March 2026).\n\n---\n\n### How Sorry Is Used for Decomposition\n\nHilbert's core mechanism is **recursive sorry-based subgoal decomposition** in Lean 4. The process works as follows:\n\n1. **Proof sketch generation:** The Reasoner LLM (Gemini 2.5 Pro or Flash) first generates a natural-language step-by-step proof. It then translates this into a Lean 4 proof sketch consisting of `have` statements, where each subgoal's proof body is filled with `sorry` -- Lean's placeholder keyword that the type-checker temporarily accepts as a valid proof of any proposition. The prompts explicitly instruct: \"Use `sorry` for all subgoal proofs -- focus on structure, not implementation\" and \"Do NOT use `sorry` for the main goal proof -- use your subgoals to prove it.\"\n\n2. **Sketch compilation and correction:** The sorry-laden sketch is compiled against the Lean verifier. Because `sorry` is accepted by Lean, this validates the *logical structure* (that the subgoals, if proven, would actually prove the main theorem) without requiring the subgoals themselves to be proven yet. If compilation fails, error messages are fed back to the Reasoner for iterative correction (up to 4 attempts).\n\n3. **Subgoal extraction:** Each `have` statement with a `sorry` placeholder is extracted as an independent theorem statement.\n\n4. **Assembly:** Once subgoal theorems are proven, the Reasoner produces an assembled proof replacing each `sorry` placeholder with calls to the corresponding subgoal theorem.\n\n5. **Recursive application:** If a subgoal cannot be proven directly, it is itself decomposed using the same sorry-sketch process, up to a maximum recursion depth D=5.\n\nThis is distinct from prior approaches (DSP, LEGO-Prover) which could decompose once but not recursively decompose subgoals that remained too difficult.\n\n---\n\n### Approach: Inference-Time Only (No RL Training)\n\n**Hilbert is purely an inference-time system.** There is no reinforcement learning training, no fine-tuning, and no reward signals. The system orchestrates four pre-existing components at inference time:\n\n1. **Reasoner:** Gemini 2.5 Flash or Pro (general-purpose LLM for informal math reasoning, sketch generation, assembly)\n2. **Prover:** DeepSeek-Prover-V2-7B or Goedel-Prover-V2-32B (specialized Lean 4 tactic generation model)\n3. **Verifier:** Kimina Lean Server (Lean v4.15.0 with Mathlib v4.15.0)\n4. **Retriever:** Sentence-transformer-based semantic search over Mathlib theorems (all-mpnet-base-v2 embeddings)\n\nThe paper explicitly notes that future work could use \"proofs and reasoning traces generated by Hilbert to train better Prover and Reasoner models,\" creating a \"virtuous cycle\" -- but this is stated as future direction, not something they did. **There is no RL reward signal, no sorry-completion reward, and no training loop in the current system.**\n\n---\n\n### Subgoal Verification Process\n\nFor each extracted subgoal, Hilbert applies a cascading four-stage strategy:\n\n1. **Direct prover attempt:** The Prover LLM generates 4 candidate proofs; if any compiles, the subgoal is done.\n2. **Mathematical correctness check:** The Reasoner evaluates whether the subgoal is mathematically sound (to avoid wasting compute on ill-formed subgoals).\n3. **Shallow solve:** The Reasoner writes short proofs (max 30 lines) using retrieved Mathlib theorems, with iterative refinement from verifier error feedback (up to 6 correction passes).\n4. **Recursive decomposition:** If all above fail and depth < D, the subgoal is itself decomposed via the same sorry-sketch process.\n\n---\n\n### Key Results\n\n**miniF2F-Test (244 problems):**\n- Hilbert + Gemini 2.5 Pro + Goedel-Prover-V2-32B: **99.2%** (6.6 percentage points above best prior public method)\n- Hilbert + Gemini 2.5 Flash + DeepSeek-Prover-V2-7B: **96.7%** (+35.4% over pass@4 baseline of the prover alone)\n- Standalone prover at D=0 (no decomposition): 75%\n\n**PutnamBench (660 problems):**\n- Hilbert: **462/660 (70.0%)**\n- SeedProver (proprietary): 50.4%\n- Best prior public baseline: ~13.4%\n- This is a **422% improvement** over the best publicly available baseline\n\n**Ablation findings:**\n- Recursion depth D=3 achieves near-optimal performance (98.7% on miniF2F); diminishing returns beyond that\n- Theorem retrieval reduces both compute and improves accuracy (98.4% vs 97.1% with DeepSeek Prover)\n- Best configuration: ~4.5K reasoner calls and 11.3K total LLM calls per problem (substantially fewer than DeltaProver's 16,384 calls with the same reasoner)\n\n---\n\n### Relation to Mechanic's Sorrifier\n\nHilbert and Mechanic (Qiu et al., 2026, arXiv: 2603.24465) both use `sorry` for decomposition but differ fundamentally in their approach:\n\n- **Hilbert uses \"informal decomposition\":** The Reasoner generates a sorry-sketch *proactively* from an informal proof plan. When a proof fails entirely, Hilbert discards the formal proof and regenerates a new informal sketch from scratch.\n- **Mechanic uses \"formal decomposition\" via a Sorrifier:** When a proof attempt *fails compilation*, Mechanic's Sorrifier surgically replaces only the innermost failing code block with `sorry`, iteratively recompiling until the proof compiles. This preserves verified structure and extracts only the truly unresolved subgoals, avoiding redundant re-analysis.\n\nMechanic benchmarks against Hilbert as a baseline. On Putnam 2025 (12 problems), Mechanic solved 11 with better efficiency (114 min avg vs. higher for other systems). Mechanic's key claim is that formal decomposition is more efficient for complex problems because it does not discard valid proof segments.\n\n---\n\n### Sorry-Completion as RL Reward Signal\n\n**Neither Hilbert nor Mechanic discusses using sorry-completion as an RL reward signal.** Hilbert's paper mentions the possibility of using generated proofs to train better models as future work, but does not formalize this as a reward signal. This appears to be an open research direction that neither paper has explored.\n\n---\n\n### Code Availability\n\n**GitHub repository:** [https://github.com/apple/ml-hilbert](https://github.com/apple/ml-hilbert) (Apple's official release)\n\n**Active fork:** [https://github.com/Rose-STL-Lab/ml-hilbert](https://github.com/Rose-STL-Lab/ml-hilbert) (maintained by primary author Varambally)\n\nThe Apple repo has 18 stars, 9 forks, 2 commits, and is described as \"not in active development\" with the active fork at Rose-STL-Lab. The code includes inference pipeline code (`src/`), config files, and requires kimina-lean-server, sentence-transformers, and OpenAI-compatible LLM endpoints. It is inference-only code -- no training code is included. Licensed under CC BY 4.0.\n\n---\n\n### Key Takeaways for Positioning\n\n1. Hilbert is inference-time only with no RL -- the sorry-completion-as-reward-signal idea is entirely unexplored territory that could differentiate your work.\n2. Hilbert's sorry usage is \"proactive\" (plan-then-sorry), while Mechanic's is \"reactive\" (fail-then-sorrify). A training-time approach using sorry as reward signal would be a third, distinct paradigm.\n3. The 99.2% miniF2F and 70.0% PutnamBench numbers are the current SOTA to beat or compare against.\n4. Hilbert explicitly flags training on its own traces as future work -- if your approach does this, you are directly addressing their stated open problem.\n5. Code is available but minimal (18 stars), suggesting the community has not yet deeply engaged with reproducing or extending this work.\n\nSources:\n- [Hilbert paper on arXiv](https://arxiv.org/abs/2509.22819)\n- [Hilbert HTML version](https://arxiv.org/html/2509.22819v1)\n- [Hilbert on OpenReview (ICLR 2026)](https://openreview.net/forum?id=GN8OdkTo3B)\n- [Apple ML Research page](https://machinelearning.apple.com/research/hilbert)\n- [GitHub: apple/ml-hilbert](https://github.com/apple/ml-hilbert)\n- [GitHub: Rose-STL-Lab/ml-hilbert (active fork)](https://github.com/Rose-STL-Lab/ml-hilbert)\n- [Mechanic paper (arXiv)](https://arxiv.org/html/2603.24465)\n- [Hilbert Quick Review on Liner](https://liner.com/review/hilbert-recursively-building-formal-proofs-with-informal-reasoning)"
      }
    ],
    "totalDurationMs": 188773,
    "totalTokens": 23989,
    "totalToolUseCount": 14,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 21516,
      "output_tokens": 2472,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2472,
          "cache_read_input_tokens": 21516,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 14
    }
  },
  "sourceToolAssistantUUID": "aa12feb2-f97b-4776-a35b-9959f251a287",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-27T17:55:01.395Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01HyMLVsGGsSJ8cLCB9h3Uth`</summary>

```json
{
  "description": "Research AlphaProof and VeRPO",
  "prompt": "I need to deeply research two papers:\n\n1. **AlphaProof (Nature, Feb 2025)** - DeepMind's system for formal mathematical reasoning. I need to understand:\n   - How it handles multi-subgoal returns in formal RL\n   - Their reward design (min-over-subgoals vs mean)\n   - The AlphaProof training loop (AlphaZero-style?)\n   - Key results and benchmarks\n   - Any connection to sorry-based decomposition\n\n2. **VeRPO (arXiv, Jan 2026)** - Partial-completion ratio reward for code generation RL. I need:\n   - Full title and authors\n   - How they compute partial completion ratios\n   - Their reward formulation\n   - How it compares to binary pass/fail reward\n   - Results showing improvement\n   - Whether this is analogous to verified_subgoals/total_subgoals\n\nPlease search for both papers using multiple queries, fetch and read them, and report detailed findings (400+ words each). Include exact citations and key technical details.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "352722f1-259c-4e2b-9a81-7cfba56f2ebf",
  "isSidechain": false,
  "requestId": "req_011CbTW7otB6MH85rha4vnKn",
  "type": "assistant",
  "uuid": "14a07d87-d396-499d-b536-207b3b69f66e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ZoUNpJwdXLstUJFb8i9uo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2913,
      "cache_read_input_tokens": 17550,
      "output_tokens": 347,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2913,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 347,
          "cache_read_input_tokens": 17550,
          "cache_creation_input_tokens": 2913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2913
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-27T18:02:48.873Z_

<details><summary>↩ Tool result · `toolu_01HyMLVsGGsSJ8cLCB9h3Uth`</summary>

```text
I now have comprehensive information on both papers. Let me compile the detailed findings.

---

## Paper 1: AlphaProof -- Olympiad-Level Formal Mathematical Reasoning with Reinforcement Learning

**Full Citation:** Thomas Hubert, Rishi Mehta, Laurent Sartran, Miklos Z. Horvath, Goran Zuzic, Eric Wieser, Aja Huang, Julian Schrittwieser, Yannick Schroecker, Hussain Masoom, Ottavia Bertolli, Tom Zahavy, Amol Mandhane, Jessica Yung, Iuliya Beloshapka, Borja Ibarz, Vivek Veeriah, Lei Yu, Oliver Nash, Paul Lezeau, Salvatore Mercuri, Calle Sonne, Bhavik Mehta, Alex Davies, Daniel Zheng, Fabian Pedregosa, Yin Li, Ingrid von Glehn, Mark Rowland, Samuel Albanie, Ameya Velingker, Simon Schmitt, Edward Lockhart, Edward Hughes, Henryk Michalewski, Nicolas Sonnerat, Demis Hassabis, Pushmeet Kohli, and David Silver. "Olympiad-level formal mathematical reasoning with reinforcement learning." *Nature* (2025). Google DeepMind, London, UK.

### Architecture and Training Loop

AlphaProof couples a **pretrained encoder-decoder transformer** with an **AlphaZero-style reinforcement learning** algorithm. The transformer backbone was pretrained for 50 epochs on a mix of code and mathematical data, processing 12 trillion tokens on the encoder side. The system operates in the **Lean 4** formal proof assistant environment.

The training loop is a self-improving cycle analogous to AlphaZero in games: the agent iteratively attempts to prove formal theorems, and every verified proof is fed back into the training data, updating the model's weights so similar reasoning steps become easier to discover on future problems. This directly bootstraps on its own discoveries. The RL loop uses **Monte Carlo Tree Search (MCTS)** with a neural network providing both a policy head (to rank candidate tactics) and a value head (to estimate likelihood of eventual proof completion).

### Reward Design: rt = -1 per Tactic, Min-over-Subgoals

The reward signal is elegantly simple: **r_t = -1 for each tactic applied**. This incentivizes the agent to find short proofs (fewer tactics = higher cumulative return). The return G_t from a state s_t is the sum of these rewards until termination.

The critical design choice concerns **multi-subgoal returns**. In Lean, a single tactic application can split one goal into multiple independent subgoals (e.g., via induction, producing a base case and inductive step). AlphaProof introduces **product nodes** (also called **AND nodes**) into the search tree to represent this branching. For such nodes, the return is defined as the **minimum return over all subgoals** (corresponding to the longest/hardest proof branch), rather than the sum or mean of returns. The reasoning is that the difficulty of completing a proof is determined by the hardest sub-statement that must be proved. The naming "product node" derives from the Curry-Howard correspondence between logical conjunction (AND) and product types.

This min-over-subgoals formulation is a principled choice: since all subgoals must be solved for the proof to succeed, the bottleneck subgoal determines the effective difficulty. Using a sum would conflate proof length with proof difficulty; using a mean would dilute the signal from hard subgoals.

### AND-OR Tree Search

The MCTS operates on an **AND-OR tree** structure:
- **OR nodes** represent proof states where the agent chooses among candidate tactics (standard MCTS choice nodes).
- **AND nodes** (product nodes) represent states where a tactic has decomposed the goal into multiple independent subgoals, all of which must be solved.

Backpropagation through AND nodes uses the value of the hardest branch. Proven subgoals are **marked as solved and not revisited**, allowing search effort to concentrate on what remains unsolved. The system typically uses **400 MCTS simulations** per search step, bounded by a hard RPC timeout.

### Autoformalization Pipeline

A **Gemini model** was fine-tuned to translate natural language mathematical problem statements into formal Lean statements. This pipeline generated **80 million distinct Lean statements** from approximately 1 million natural language theorems, through stochastic sampling and intentional prompt randomization. This massive corpus of auto-formalized problems serves as the training curriculum for the RL loop.

### Test-Time RL

For the most difficult problems (notably IMO problems), AlphaProof deploys **Test-Time RL**: at inference time, the LLM generates millions of related problem variants that serve as a "natural curriculum" -- easier stepping stones that build toward solving the target problem. The system trains on these variants during the contest itself, performing deep, problem-specific adaptation. This was used during the 2024 IMO.

### Sorry-Based Decomposition

AlphaProof itself does not employ sorry-based decomposition as a strategy. However, the `sorry` keyword in Lean is relevant: AlphaProof requires that for a tactic application to be considered successful, **the resulting proof term must not employ the `sorry` placeholder** (used for incomplete proofs) and must be type-correct. The `sorry` keyword thus serves as a negative validity check -- its presence indicates an incomplete proof.

A separate, related work called **Mechanic** (arXiv:2603.24465) does implement a "sorrifier-driven formal decomposition workflow" that explicitly uses `sorry` placeholders to isolate unresolved subgoals while preserving surrounding verified proof structure, extracting each failed sub-problem into a clean, self-contained context. This is conceptually related but is not part of AlphaProof itself.

### Key Benchmark Results

| Benchmark | Result |
|-----------|--------|
| **IMO 2024** | Solved P1, P2, P6 (3 of 5 non-geometry problems); P6 was solved by only 5 of 609 human participants |
| **Combined with AlphaGeometry 2** | 28/42 points = silver medal equivalent (4 of 6 total problems) |
| **miniF2F** | **Saturated** the benchmark (effectively solved it) |
| **PutnamBench** | **56%** solve rate |

The miniF2F saturation is particularly notable as it indicates the benchmark is no longer discriminative for systems at AlphaProof's level.

---

## Paper 2: VeRPO -- Verifiable Dense Reward Policy Optimization for Code Generation

**Full Citation:** Longwen Wang, Yirui Liu, Xuan'er Wu, Xiaohui Hu, Yuankai Fan, Kaidong Yu, Qizhen Weng, Wei Xi, and Xuelong Li. "VeRPO: Verifiable Dense Reward Policy Optimization for Code Generation." arXiv:2601.03525 (January 7, 2026).

### Core Problem and Motivation

Standard RL for code generation uses **binary pass/fail outcome rewards** (does the generated code pass all unit tests?). This creates severe **reward sparsity**: most generated code either fully passes or fully fails, providing no gradient signal for partial progress. External learned Reward Models (RMs) can provide denser supervision but suffer from **reward misalignment** and high computational cost. VeRPO bridges this gap by constructing dense rewards entirely from **verifiable execution feedback** -- no learned reward model needed.

### Partial Completion Ratio: Weighted Partial Success

VeRPO's core innovation is computing a **weighted partial success** score rather than a binary outcome. The turn-level reward is:

**R^turn(tau_i, t) = sum_{j=1}^{|U_x|} w'_j * p_{t,i}^(j)**

where p_{t,i}^(j) = 1 if test j passes at turn t, else 0, and w'_j are normalized difficulty weights.

### Dynamic Difficulty Weight Estimation (Three Steps)

1. **Empirical Pass Rate:** rho_j = (number of passes of test j across all turns) / (total turn count). Tests that are rarely passed get low rho_j.

2. **Inverse Pass-Rate Weight:** w_j = exp(-alpha * rho_j), where alpha > 0 (default 2.0) controls sensitivity. Harder tests (low pass rate) get exponentially higher weight.

3. **Density Normalization via Gaussian KDE:** To prevent clusters of similarly-difficult trivial tests from dominating:
   - rho_hat_j = sum exp(-(rho_j - rho_j')^2 / 2*sigma^2) (kernel density estimate)
   - sigma = std({rho_j}) / 2 (adaptive bandwidth)
   - w'_j = w_j / (rho_hat_j + epsilon) (penalizes redundant trivial tests)

This dynamic weighting is recalculated each training iteration based on the **current policy's** execution statistics, so weights adapt as the model improves.

### Global Execution Outcome Anchoring

To maintain alignment with end-to-end functional correctness, VeRPO anchors the dense turn-level signal with a **trajectory-level binary reward**:

**R_tilde^traj(tau_i) = R^traj(tau_i) * gamma^|tau_i|**

where R^traj = 1 if ALL tests pass, 0 otherwise; gamma in (0,1] (default 0.95) is an efficiency decay penalizing longer trajectories.

### Combined Advantage (Dual-Level)

VeRPO uses a **GRPO variant** (Group Relative Policy Optimization) with dual-level advantages:

- **Turn-level advantage:** A^turn(tau_i, t) = [R^turn - mean(turn-level rewards)] / F_norm
- **Trajectory-level advantage:** A^traj(tau_i) = [R_tilde^traj - mean(trajectory rewards)] / F_norm
- **Combined:** A(tau_i, t) = A^traj(tau_i) + beta * A^turn(tau_i, t) (beta=1.0)

Critically, **F_norm = 1** (constant normalization), not standard deviation. This avoids task-difficulty bias where hard problems would artificially inflate advantages.

### Comparison to Binary Pass/Fail Reward

The key problem with binary rewards is the **degenerate group ratio** -- the fraction of training groups where all samples receive identical reward (all pass or all fail), yielding zero advantage and zero gradient signal. Standard outcome-driven GRPO exhibits a **60-70% degenerate group ratio** persistently throughout training. VeRPO reduces this to **below 25%** with a downward trend, meaning the model receives useful learning signal on far more training examples.

### Benchmark Results (Qwen3-8B backbone)

| Benchmark | GRPO (Multi-Turn) | VeRPO (Multi-Turn) | Improvement |
|-----------|-------------------|---------------------|-------------|
| HumanEval Plus | 96.41% | 97.87% | +1.46% |
| BigCodeBench Full | 60.91% | 62.52% | +1.61% |
| BigCodeBench Hard | 43.32% | 45.69% | +2.37% |
| LiveCodeBench V6 | 30.50% | 33.07% | +2.57% |
| Codeforces CodeElo | 31.61% | 40.44% | **+8.83%** |
| **Average** | **58.99%** | **62.12%** | **+3.13%** |

The improvement is most pronounced on harder benchmarks (Codeforces), where partial progress signals matter most because binary success is rare. AceCoder (a learned RM baseline) suffered **training collapse** in the multi-turn setting, while VeRPO remained stable.

### Training Details

- **Base model:** Qwen3-8B
- **Rollout batch:** 32 problems, 10 responses per problem
- **Max length:** 16,384 tokens, temperature 1.0
- **Learning rate:** 1e-6, PPO-style clipping (epsilon_low=0.2, epsilon_high=0.28)
- **No KL penalty** to foster exploration
- **Hardware:** 8x NVIDIA H800 GPUs
- **Computational overhead:** <0.02% additional time; zero GPU memory overhead (no external RM)

### Analogy to verified_subgoals / total_subgoals

VeRPO's reward is **directly analogous** to a verified_subgoals / total_subgoals formulation, but with important refinements:

- Each unit test is analogous to a "subgoal"
- The partial pass ratio (tests_passed / total_tests) is the basic version
- VeRPO improves on this by **weighting subgoals by difficulty** -- a hard test that is rarely passed counts more than a trivial one
- The KDE-based normalization further prevents clusters of easy tests from dominating

So rather than a simple ratio, VeRPO computes **sum(difficulty_weight_j * passed_j) / sum(difficulty_weight_j)** (after normalization), which is a sophisticiated, dynamically-weighted version of the subgoal completion ratio.

---

## Cross-Paper Comparison

Both papers address the same fundamental problem: **how to provide dense, informative reward signals in domains where the final outcome is binary** (proof complete vs. incomplete; all tests pass vs. not). Their solutions are structurally parallel:

| Dimension | AlphaProof | VeRPO |
|-----------|-----------|-------|
| Domain | Formal theorem proving (Lean) | Code generation (unit tests) |
| Subgoal unit | Proof subgoals (from tactic decomposition) | Unit tests |
| Reward per step | -1 per tactic (incentivize brevity) | Weighted partial test passage |
| Multi-subgoal aggregation | **min** over subgoals (bottleneck) | **weighted sum** over tests |
| Verification | Lean type checker (100% sound) | Test execution (empirically sound) |
| RL algorithm | AlphaZero + MCTS | GRPO (no value network) |
| Key insight | Hardest subgoal determines difficulty | Difficulty-weighted partial credit |

Sources:
- [Olympiad-level formal mathematical reasoning with reinforcement learning | Nature](https://www.nature.com/articles/s41586-025-09833-y)
- [AlphaProof PubMed entry with full author list](https://pubmed.ncbi.nlm.nih.gov/41225005/)
- [AlphaProof Paper analysis by Julian Schrittwieser](https://www.julian.ac/blog/2025/11/13/alphaproof-paper/)
- [AlphaProof system proves its worth at the Math Olympiad](https://www.startuphub.ai/ai-news/ai-research/2025/alphaproof-system-proves-its-worth-at-the-math-olympiad/)
- [AlphaProof: AI for Formal Mathematics - EmergentMind](https://www.emergentmind.com/topics/alphaproof)
- [Thomas Hubert's AlphaProof presentation slides (Berkeley)](https://rdi.berkeley.edu/adv-llm-agents/slides/alphaproof.pdf)
- [Major Breakthroughs in Lean 4-Based Auto-Formalized Mathematics (UVA course)](https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html)
- [A Minimal Agent for Automated Theorem Proving (citing AlphaProof benchmarks)](https://arxiv.org/html/2602.24273v1)
- [Mechanic: Sorrifier-Driven Formal Decomposition Workflow](https://arxiv.org/pdf/2603.24465)
- [VeRPO: Verifiable Dense Reward Policy Optimization for Code Generation (arXiv)](https://arxiv.org/abs/2601.03525)
- [VeRPO full paper HTML](https://arxiv.org/html/2601.03525v1)
- [VeRPO - EmergentMind](https://www.emergentmind.com/papers/2601.03525)

agentId: a0162e44957860730 (use SendMessage with to: 'a0162e44957860730' to continue this agent)
&lt;usage>total_tokens: 35717
tool_uses: 30
duration_ms: 467469&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14a07d87-d396-499d-b536-207b3b69f66e",
  "isSidechain": false,
  "promptId": "c8f8bb74-4b57-4255-9fe8-15c0a5831ab6",
  "type": "user",
  "uuid": "3a70060c-a1a8-4cc2-aa8a-1e91d3d521de",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to deeply research two papers:\n\n1. **AlphaProof (Nature, Feb 2025)** - DeepMind's system for formal mathematical reasoning. I need to understand:\n   - How it handles multi-subgoal returns in formal RL\n   - Their reward design (min-over-subgoals vs mean)\n   - The AlphaProof training loop (AlphaZero-style?)\n   - Key results and benchmarks\n   - Any connection to sorry-based decomposition\n\n2. **VeRPO (arXiv, Jan 2026)** - Partial-completion ratio reward for code generation RL. I need:\n   - Full title and authors\n   - How they compute partial completion ratios\n   - Their reward formulation\n   - How it compares to binary pass/fail reward\n   - Results showing improvement\n   - Whether this is analogous to verified_subgoals/total_subgoals\n\nPlease search for both papers using multiple queries, fetch and read them, and report detailed findings (400+ words each). Include exact citations and key technical details.",
    "agentId": "a0162e44957860730",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information on both papers. Let me compile the detailed findings.\n\n---\n\n## Paper 1: AlphaProof -- Olympiad-Level Formal Mathematical Reasoning with Reinforcement Learning\n\n**Full Citation:** Thomas Hubert, Rishi Mehta, Laurent Sartran, Miklos Z. Horvath, Goran Zuzic, Eric Wieser, Aja Huang, Julian Schrittwieser, Yannick Schroecker, Hussain Masoom, Ottavia Bertolli, Tom Zahavy, Amol Mandhane, Jessica Yung, Iuliya Beloshapka, Borja Ibarz, Vivek Veeriah, Lei Yu, Oliver Nash, Paul Lezeau, Salvatore Mercuri, Calle Sonne, Bhavik Mehta, Alex Davies, Daniel Zheng, Fabian Pedregosa, Yin Li, Ingrid von Glehn, Mark Rowland, Samuel Albanie, Ameya Velingker, Simon Schmitt, Edward Lockhart, Edward Hughes, Henryk Michalewski, Nicolas Sonnerat, Demis Hassabis, Pushmeet Kohli, and David Silver. \"Olympiad-level formal mathematical reasoning with reinforcement learning.\" *Nature* (2025). Google DeepMind, London, UK.\n\n### Architecture and Training Loop\n\nAlphaProof couples a **pretrained encoder-decoder transformer** with an **AlphaZero-style reinforcement learning** algorithm. The transformer backbone was pretrained for 50 epochs on a mix of code and mathematical data, processing 12 trillion tokens on the encoder side. The system operates in the **Lean 4** formal proof assistant environment.\n\nThe training loop is a self-improving cycle analogous to AlphaZero in games: the agent iteratively attempts to prove formal theorems, and every verified proof is fed back into the training data, updating the model's weights so similar reasoning steps become easier to discover on future problems. This directly bootstraps on its own discoveries. The RL loop uses **Monte Carlo Tree Search (MCTS)** with a neural network providing both a policy head (to rank candidate tactics) and a value head (to estimate likelihood of eventual proof completion).\n\n### Reward Design: rt = -1 per Tactic, Min-over-Subgoals\n\nThe reward signal is elegantly simple: **r_t = -1 for each tactic applied**. This incentivizes the agent to find short proofs (fewer tactics = higher cumulative return). The return G_t from a state s_t is the sum of these rewards until termination.\n\nThe critical design choice concerns **multi-subgoal returns**. In Lean, a single tactic application can split one goal into multiple independent subgoals (e.g., via induction, producing a base case and inductive step). AlphaProof introduces **product nodes** (also called **AND nodes**) into the search tree to represent this branching. For such nodes, the return is defined as the **minimum return over all subgoals** (corresponding to the longest/hardest proof branch), rather than the sum or mean of returns. The reasoning is that the difficulty of completing a proof is determined by the hardest sub-statement that must be proved. The naming \"product node\" derives from the Curry-Howard correspondence between logical conjunction (AND) and product types.\n\nThis min-over-subgoals formulation is a principled choice: since all subgoals must be solved for the proof to succeed, the bottleneck subgoal determines the effective difficulty. Using a sum would conflate proof length with proof difficulty; using a mean would dilute the signal from hard subgoals.\n\n### AND-OR Tree Search\n\nThe MCTS operates on an **AND-OR tree** structure:\n- **OR nodes** represent proof states where the agent chooses among candidate tactics (standard MCTS choice nodes).\n- **AND nodes** (product nodes) represent states where a tactic has decomposed the goal into multiple independent subgoals, all of which must be solved.\n\nBackpropagation through AND nodes uses the value of the hardest branch. Proven subgoals are **marked as solved and not revisited**, allowing search effort to concentrate on what remains unsolved. The system typically uses **400 MCTS simulations** per search step, bounded by a hard RPC timeout.\n\n### Autoformalization Pipeline\n\nA **Gemini model** was fine-tuned to translate natural language mathematical problem statements into formal Lean statements. This pipeline generated **80 million distinct Lean statements** from approximately 1 million natural language theorems, through stochastic sampling and intentional prompt randomization. This massive corpus of auto-formalized problems serves as the training curriculum for the RL loop.\n\n### Test-Time RL\n\nFor the most difficult problems (notably IMO problems), AlphaProof deploys **Test-Time RL**: at inference time, the LLM generates millions of related problem variants that serve as a \"natural curriculum\" -- easier stepping stones that build toward solving the target problem. The system trains on these variants during the contest itself, performing deep, problem-specific adaptation. This was used during the 2024 IMO.\n\n### Sorry-Based Decomposition\n\nAlphaProof itself does not employ sorry-based decomposition as a strategy. However, the `sorry` keyword in Lean is relevant: AlphaProof requires that for a tactic application to be considered successful, **the resulting proof term must not employ the `sorry` placeholder** (used for incomplete proofs) and must be type-correct. The `sorry` keyword thus serves as a negative validity check -- its presence indicates an incomplete proof.\n\nA separate, related work called **Mechanic** (arXiv:2603.24465) does implement a \"sorrifier-driven formal decomposition workflow\" that explicitly uses `sorry` placeholders to isolate unresolved subgoals while preserving surrounding verified proof structure, extracting each failed sub-problem into a clean, self-contained context. This is conceptually related but is not part of AlphaProof itself.\n\n### Key Benchmark Results\n\n| Benchmark | Result |\n|-----------|--------|\n| **IMO 2024** | Solved P1, P2, P6 (3 of 5 non-geometry problems); P6 was solved by only 5 of 609 human participants |\n| **Combined with AlphaGeometry 2** | 28/42 points = silver medal equivalent (4 of 6 total problems) |\n| **miniF2F** | **Saturated** the benchmark (effectively solved it) |\n| **PutnamBench** | **56%** solve rate |\n\nThe miniF2F saturation is particularly notable as it indicates the benchmark is no longer discriminative for systems at AlphaProof's level.\n\n---\n\n## Paper 2: VeRPO -- Verifiable Dense Reward Policy Optimization for Code Generation\n\n**Full Citation:** Longwen Wang, Yirui Liu, Xuan'er Wu, Xiaohui Hu, Yuankai Fan, Kaidong Yu, Qizhen Weng, Wei Xi, and Xuelong Li. \"VeRPO: Verifiable Dense Reward Policy Optimization for Code Generation.\" arXiv:2601.03525 (January 7, 2026).\n\n### Core Problem and Motivation\n\nStandard RL for code generation uses **binary pass/fail outcome rewards** (does the generated code pass all unit tests?). This creates severe **reward sparsity**: most generated code either fully passes or fully fails, providing no gradient signal for partial progress. External learned Reward Models (RMs) can provide denser supervision but suffer from **reward misalignment** and high computational cost. VeRPO bridges this gap by constructing dense rewards entirely from **verifiable execution feedback** -- no learned reward model needed.\n\n### Partial Completion Ratio: Weighted Partial Success\n\nVeRPO's core innovation is computing a **weighted partial success** score rather than a binary outcome. The turn-level reward is:\n\n**R^turn(tau_i, t) = sum_{j=1}^{|U_x|} w'_j * p_{t,i}^(j)**\n\nwhere p_{t,i}^(j) = 1 if test j passes at turn t, else 0, and w'_j are normalized difficulty weights.\n\n### Dynamic Difficulty Weight Estimation (Three Steps)\n\n1. **Empirical Pass Rate:** rho_j = (number of passes of test j across all turns) / (total turn count). Tests that are rarely passed get low rho_j.\n\n2. **Inverse Pass-Rate Weight:** w_j = exp(-alpha * rho_j), where alpha > 0 (default 2.0) controls sensitivity. Harder tests (low pass rate) get exponentially higher weight.\n\n3. **Density Normalization via Gaussian KDE:** To prevent clusters of similarly-difficult trivial tests from dominating:\n   - rho_hat_j = sum exp(-(rho_j - rho_j')^2 / 2*sigma^2) (kernel density estimate)\n   - sigma = std({rho_j}) / 2 (adaptive bandwidth)\n   - w'_j = w_j / (rho_hat_j + epsilon) (penalizes redundant trivial tests)\n\nThis dynamic weighting is recalculated each training iteration based on the **current policy's** execution statistics, so weights adapt as the model improves.\n\n### Global Execution Outcome Anchoring\n\nTo maintain alignment with end-to-end functional correctness, VeRPO anchors the dense turn-level signal with a **trajectory-level binary reward**:\n\n**R_tilde^traj(tau_i) = R^traj(tau_i) * gamma^|tau_i|**\n\nwhere R^traj = 1 if ALL tests pass, 0 otherwise; gamma in (0,1] (default 0.95) is an efficiency decay penalizing longer trajectories.\n\n### Combined Advantage (Dual-Level)\n\nVeRPO uses a **GRPO variant** (Group Relative Policy Optimization) with dual-level advantages:\n\n- **Turn-level advantage:** A^turn(tau_i, t) = [R^turn - mean(turn-level rewards)] / F_norm\n- **Trajectory-level advantage:** A^traj(tau_i) = [R_tilde^traj - mean(trajectory rewards)] / F_norm\n- **Combined:** A(tau_i, t) = A^traj(tau_i) + beta * A^turn(tau_i, t) (beta=1.0)\n\nCritically, **F_norm = 1** (constant normalization), not standard deviation. This avoids task-difficulty bias where hard problems would artificially inflate advantages.\n\n### Comparison to Binary Pass/Fail Reward\n\nThe key problem with binary rewards is the **degenerate group ratio** -- the fraction of training groups where all samples receive identical reward (all pass or all fail), yielding zero advantage and zero gradient signal. Standard outcome-driven GRPO exhibits a **60-70% degenerate group ratio** persistently throughout training. VeRPO reduces this to **below 25%** with a downward trend, meaning the model receives useful learning signal on far more training examples.\n\n### Benchmark Results (Qwen3-8B backbone)\n\n| Benchmark | GRPO (Multi-Turn) | VeRPO (Multi-Turn) | Improvement |\n|-----------|-------------------|---------------------|-------------|\n| HumanEval Plus | 96.41% | 97.87% | +1.46% |\n| BigCodeBench Full | 60.91% | 62.52% | +1.61% |\n| BigCodeBench Hard | 43.32% | 45.69% | +2.37% |\n| LiveCodeBench V6 | 30.50% | 33.07% | +2.57% |\n| Codeforces CodeElo | 31.61% | 40.44% | **+8.83%** |\n| **Average** | **58.99%** | **62.12%** | **+3.13%** |\n\nThe improvement is most pronounced on harder benchmarks (Codeforces), where partial progress signals matter most because binary success is rare. AceCoder (a learned RM baseline) suffered **training collapse** in the multi-turn setting, while VeRPO remained stable.\n\n### Training Details\n\n- **Base model:** Qwen3-8B\n- **Rollout batch:** 32 problems, 10 responses per problem\n- **Max length:** 16,384 tokens, temperature 1.0\n- **Learning rate:** 1e-6, PPO-style clipping (epsilon_low=0.2, epsilon_high=0.28)\n- **No KL penalty** to foster exploration\n- **Hardware:** 8x NVIDIA H800 GPUs\n- **Computational overhead:** <0.02% additional time; zero GPU memory overhead (no external RM)\n\n### Analogy to verified_subgoals / total_subgoals\n\nVeRPO's reward is **directly analogous** to a verified_subgoals / total_subgoals formulation, but with important refinements:\n\n- Each unit test is analogous to a \"subgoal\"\n- The partial pass ratio (tests_passed / total_tests) is the basic version\n- VeRPO improves on this by **weighting subgoals by difficulty** -- a hard test that is rarely passed counts more than a trivial one\n- The KDE-based normalization further prevents clusters of easy tests from dominating\n\nSo rather than a simple ratio, VeRPO computes **sum(difficulty_weight_j * passed_j) / sum(difficulty_weight_j)** (after normalization), which is a sophisticiated, dynamically-weighted version of the subgoal completion ratio.\n\n---\n\n## Cross-Paper Comparison\n\nBoth papers address the same fundamental problem: **how to provide dense, informative reward signals in domains where the final outcome is binary** (proof complete vs. incomplete; all tests pass vs. not). Their solutions are structurally parallel:\n\n| Dimension | AlphaProof | VeRPO |\n|-----------|-----------|-------|\n| Domain | Formal theorem proving (Lean) | Code generation (unit tests) |\n| Subgoal unit | Proof subgoals (from tactic decomposition) | Unit tests |\n| Reward per step | -1 per tactic (incentivize brevity) | Weighted partial test passage |\n| Multi-subgoal aggregation | **min** over subgoals (bottleneck) | **weighted sum** over tests |\n| Verification | Lean type checker (100% sound) | Test execution (empirically sound) |\n| RL algorithm | AlphaZero + MCTS | GRPO (no value network) |\n| Key insight | Hardest subgoal determines difficulty | Difficulty-weighted partial credit |\n\nSources:\n- [Olympiad-level formal mathematical reasoning with reinforcement learning | Nature](https://www.nature.com/articles/s41586-025-09833-y)\n- [AlphaProof PubMed entry with full author list](https://pubmed.ncbi.nlm.nih.gov/41225005/)\n- [AlphaProof Paper analysis by Julian Schrittwieser](https://www.julian.ac/blog/2025/11/13/alphaproof-paper/)\n- [AlphaProof system proves its worth at the Math Olympiad](https://www.startuphub.ai/ai-news/ai-research/2025/alphaproof-system-proves-its-worth-at-the-math-olympiad/)\n- [AlphaProof: AI for Formal Mathematics - EmergentMind](https://www.emergentmind.com/topics/alphaproof)\n- [Thomas Hubert's AlphaProof presentation slides (Berkeley)](https://rdi.berkeley.edu/adv-llm-agents/slides/alphaproof.pdf)\n- [Major Breakthroughs in Lean 4-Based Auto-Formalized Mathematics (UVA course)](https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html)\n- [A Minimal Agent for Automated Theorem Proving (citing AlphaProof benchmarks)](https://arxiv.org/html/2602.24273v1)\n- [Mechanic: Sorrifier-Driven Formal Decomposition Workflow](https://arxiv.org/pdf/2603.24465)\n- [VeRPO: Verifiable Dense Reward Policy Optimization for Code Generation (arXiv)](https://arxiv.org/abs/2601.03525)\n- [VeRPO full paper HTML](https://arxiv.org/html/2601.03525v1)\n- [VeRPO - EmergentMind](https://www.emergentmind.com/papers/2601.03525)"
      }
    ],
    "totalDurationMs": 467469,
    "totalTokens": 35717,
    "totalToolUseCount": 30,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 857,
      "cache_read_input_tokens": 30809,
      "output_tokens": 4050,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 857
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4050,
          "cache_read_input_tokens": 30809,
          "cache_creation_input_tokens": 857,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 857,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 30
    }
  },
  "sourceToolAssistantUUID": "14a07d87-d396-499d-b536-207b3b69f66e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Verifier-Certified Progress Rewards via Sorry-Driven Decomposition\",…",
  "leafUuid": "3a70060c-a1a8-4cc2-aa8a-1e91d3d521de",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise sorry-progress reward to address autoformalization gap",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02"
}
```

---

### Tool call

_source line 20 · 2026-05-27T18:03:00.102Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01UQCpPhZBysJiRw8VQZEkMY`</summary>

```json
{
  "description": "Research Proof-Verifier and autoformalization",
  "prompt": "I need to deeply research two topics:\n\n1. **Proof-Verifier (ICLR 2026)** - A paper that addresses dense reward for theorem proving RL via a learned verifier, achieving 93% verification accuracy. Search for:\n   - \"Proof-Verifier ICLR 2026 dense reward theorem proving\"\n   - \"learned verifier theorem proving RL reward ICLR 2026\"\n   - Extract full title, authors, approach, how their learned verifier works, results, and how it compares to compiler-based verification\n\n2. **Autoformalization + sorry mechanisms** - I need to understand the current state of autoformalization (bridging informal/natural language math to formal proofs) and how sorry-based decomposition could connect to it. Search for:\n   - \"autoformalization theorem proving 2025 2026\"\n   - \"informal to formal proof translation sorry\"\n   - \"autoformalization Lean survey 2025 2026\"\n   - \"Hilbert autoformalization informal reasoning formal proofs\"\n   Key questions: How does Hilbert connect informal reasoning to formal proofs? What is the current SOTA in autoformalization? How could sorry-based RL reward training improve autoformalization?\n\nPlease fetch and read actual papers. Report detailed findings (400+ words per topic).",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a70060c-a1a8-4cc2-aa8a-1e91d3d521de",
  "isSidechain": false,
  "requestId": "req_011CbTWiyohvVd8SmCiTH4ck",
  "type": "assistant",
  "uuid": "c323f52c-ca9e-4431-bbef-e91b07f0b25e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WRFuEZY62K4MwPB5bTfGVH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4470,
      "cache_read_input_tokens": 20463,
      "output_tokens": 402,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4470,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 402,
          "cache_read_input_tokens": 20463,
          "cache_creation_input_tokens": 4470,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4470
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-27T18:06:37.286Z_

<details><summary>↩ Tool result · `toolu_01UQCpPhZBysJiRw8VQZEkMY`</summary>

```text
Now I have comprehensive information on both topics. Let me compile the detailed findings.

---

## Topic 1: Proof-Verifier (ICLR 2026)

**Full Title:** "Proof-Verifier: Enabling Reinforcement Learning from Verifiable Rewards for Mathematical Theorem Proving"

**Authors:** Zhiyuan Fan, Dadi Guo, Zhitao He, Elias Stengel-Eskin, Mohit Bansal, Yi R. Fung

**The Problem.** Reinforcement Learning from Verifiable Rewards (RLVR) has proven highly effective for mathematical tasks with clear numerical answers, but extending it to theorem proving faces a fundamental "verification bottleneck." Unlike arithmetic or algebra where answers can be checked against a ground truth, theorem proving generates entire reasoning processes -- complete proofs -- that lack reliable automated verification. Current automated theorem provers (ATPs) and formal compilers provide only coarse-grained binary labels (correct/incorrect) and cannot distinguish between a minor computational error and a fundamental logical flaw. Both receive the same "incorrect" label, offering no gradient of useful feedback for RL training.

**Approach: The Learned Generative Verifier.** Proof-Verifier is the first generative verifier specifically designed for RLVR in theorem proving. Unlike a compiler that outputs pass/fail, Proof-Verifier generates a comprehensive verification trajectory containing: (1) detailed error analysis, (2) evaluation scores on a continuous scale, (3) actionable feedback explaining what went wrong, and (4) final verification labels. This provides the dense, fine-grained reward signal that RL training needs.

**Two-Stage Coarse-to-Fine Reward Modeling.** Training the verifier uses a novel two-stage mechanism. Stage 1 (coarse-grained) trains the model on binary correct/incorrect judgments to build a broad understanding of proof validity. Stage 2 (fine-grained) refines the model to produce detailed, continuous-valued assessments that distinguish severity of errors, provide localized feedback, and score proof quality along multiple dimensions.

**Formal-to-Informal Translation Pipeline.** To generate high-quality training data, the authors developed a pipeline that translates formal proofs (from Lean/Isabelle-style formal corpora) into natural language equivalents. This produces synthetic paired data of proofs and their verification judgments, allowing training on both formal and informal proofs -- a key distinction, since most real-world theorem proving by LLMs produces natural language proofs rather than formal tactic sequences.

**Results.**
- 93% verification accuracy on proof correctness judgments
- 79% win rate in best-of-N sampling (test-time scaling), meaning the verifier reliably selects correct proofs from multiple candidates
- 32% improvement in multi-turn proof refinement, where the verifier's feedback guides iterative proof correction
- Successful single-turn and multi-turn RLVR training with consistent improvements to LLM theorem proving performance

**Comparison to Compiler-Based Verification.** The core thesis of Proof-Verifier is that compiler-based verification (e.g., Lean type-checker) is insufficient for RL reward signals in theorem proving. Compilers provide binary pass/fail, cannot handle natural language proofs at all, and give no partial credit or diagnostic information. Proof-Verifier addresses all three limitations: it works on informal proofs, provides continuous reward scores, and generates actionable feedback. However, compiler-based verification remains the gold standard for formal correctness -- Proof-Verifier complements rather than replaces it by enabling RL training on the much larger space of informal proofs.

---

## Topic 2: Autoformalization and Sorry-Based Decomposition

### Current State of Autoformalization

Autoformalization -- automatically translating informal mathematics into formal, verifiable representations -- has seen dramatic progress in 2025-2026. The comprehensive survey "Autoformalization in the Era of Large Language Models" (Weng, Du, Li et al., May 2025) maps the landscape across two paradigms:

**Rule-based approaches** use explicit logical/syntactic transformations, including controlled natural language systems (Mizar, NaProche) and grammar-based frameworks like GF. These are precise but require extensive manual rule development.

**LLM-based approaches** exploit few-shot learning and can translate between informal and formal mathematical statements with fewer than 5 examples. Key systems include DeepSeek-Prover-V2, Goedel-Prover, InternLM2.5-StepProver, and LLEMMA. Performance varies sharply by difficulty: informal competition-level problems achieve roughly 70% accuracy, but formal translation of the same problems drops to about 30%. On MiniF2F, state-of-the-art systems reach 57.6-88.9% pass rates.

A critical asymmetry exists: translating from formal to informal (informalization) is significantly easier and higher quality than the reverse direction. This asymmetry is exploited for synthetic data generation.

**Key challenges remain:** data scarcity (parallel informal-formal corpora are rare), semantic gaps (informal language is ambiguous and omits implicit knowledge), scalability to research-level mathematics (GPT-O3 solves only 25.2% of Frontier Math problems), and the distinction between syntactic correctness (type-checking) and semantic correctness (the formalization actually captures the intended meaning).

### Hilbert: Bridging Informal Reasoning and Formal Proofs

**Hilbert** (Varambally, Voice et al.; Apple ML Research; NeurIPS 2025 MATH-AI Workshop) is an agentic framework that directly bridges the informal-formal gap through recursive sorry-based decomposition. It orchestrates four components:

1. **Reasoner** (Gemini 2.5 Pro): A general-purpose LLM for informal mathematical reasoning and generating proof sketches
2. **Prover** (DeepSeek/Goedel-Prover): Specialized model for generating Lean 4 tactics
3. **Verifier**: The Lean 4 compiler via Kimina Lean Server for automated correctness checking
4. **Retriever**: A semantic search engine using sentence transformer embeddings against Mathlib's informal descriptions

**How sorry-based decomposition works:** When direct proof fails, the Reasoner generates a "formal proof sketch" using `have` statements with `sorry` placeholders -- Lean's keyword that temporarily accepts an unproven statement. This allows structural validation of the overall proof architecture before any subgoal is solved. If subgoals resist standard solving, the algorithm recursively decomposes up to depth D=5, creating nested levels of progressively simpler problems.

**Results:** Hilbert achieves 99.2% on miniF2F (6.6 points above the best publicly available method) and solves 462/660 PutnamBench problems (70.0%), a 422% improvement over the best public baseline. This dramatically narrows the gap between informal reasoning ability (Gemini solves ~83% of PutnamBench informally) and formal proof success.

### DeepSeek-Prover-V2: RL for Subgoal Decomposition

DeepSeek-Prover-V2 uses a closely related sorry-based approach. DeepSeek-V3 generates an informal chain-of-thought alongside a Lean sketch with `sorry` placeholders for unresolved subgoals. A specialized 7B prover recursively solves each subgoal. The complete proof is then paired with the original informal reasoning, creating supervised training data for formal-informal alignment. The 671B model achieves 88.9% on MiniF2F-test.

### Mechanic: The Sorrifier-Driven Workflow

**Mechanic** (March 2026, Chinese Academy of Sciences) introduces the "Sorrifier" -- a tool that systematically replaces erroneous proof blocks with `sorry` until the code compiles. It targets the innermost reported error, replaces it with `sorry`, recompiles, and repeats. Each sorry location is then extracted into a clean, self-contained subproblem with relevant hypotheses. Results: 11/12 Putnam 2025 problems solved, 4/4 IMO 2025 problems, with substantially shorter proofs (avg 656 lines vs. 1,161 for Seed-Prover) and lower cost ($18.5 vs. $72.7 for Numina per proof).

### RL Reward Training for Autoformalization

Two key works address RL reward signals for autoformalization directly:

**FormaRL** (Huang, Jin et al.) uses GRPO with a composite reward combining Lean compiler type-checking (syntactic) with LLM-based consistency checking (semantic). Using only 859 unlabeled data samples, it improved ProofNet pass@1 from 4.04% to 26.15% -- a 6.5x improvement -- demonstrating that RL can dramatically improve autoformalization even without labeled data.

**Online RL for Autoformalization** (NeurIPS 2025 MAR Workshop) identifies a critical failure mode: using type-check success alone as a reward produces syntactically valid but semantically vacuous outputs (reward hacking). The solution is composite rewards combining: (i) exact-match metrics (BEq/BEq+) when ground-truth exists, and (ii) continuous embedding-based similarity rewards requiring no paired data.

### How Sorry-Based RL Reward Could Improve Autoformalization

The connection between sorry-based decomposition and autoformalization improvement is becoming increasingly clear:

1. **Dense intermediate rewards:** Instead of a binary "does the whole proof compile?" signal, sorry-based decomposition creates multiple verification checkpoints. Each successfully filled sorry yields a partial reward, providing the dense signal that RL training requires.

2. **Compositional autoformalization:** Rather than translating an entire informal proof at once, sorry-based methods decompose into subgoals that can be autoformalized independently -- reducing the difficulty of each translation step.

3. **Curriculum learning via sorry depth:** The recursive decomposition naturally creates a difficulty hierarchy. RL agents can be trained first on shallow, simple subgoals and progressively tackle deeper decompositions.

4. **Hybrid reward signals:** Combining compiler feedback (does the sorry-free subgoal compile?) with semantic similarity rewards (does the formal statement match the informal intent?) addresses both the syntactic and semantic challenges identified in the autoformalization literature.

---

### Sources

- [Proof-Verifier: Enabling RLVR for Mathematical Theorem Proving (OpenReview)](https://openreview.net/forum?id=FAe9Gts2Qd)
- [Proof-Verifier PDF](https://openreview.net/pdf?id=FAe9Gts2Qd)
- [Autoformalization in the Era of Large Language Models: A Survey](https://arxiv.org/abs/2505.23486v2)
- [Autoformalization Survey HTML](https://arxiv.org/html/2505.23486v1)
- [Hilbert: Recursively Building Formal Proofs with Informal Reasoning](https://arxiv.org/abs/2509.22819)
- [Hilbert - Apple ML Research](https://machinelearning.apple.com/research/hilbert)
- [ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings](https://arxiv.org/abs/2510.15681)
- [DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via RL for Subgoal Decomposition](https://arxiv.org/abs/2504.21801)
- [Mechanic: Sorrifier-Driven Formal Decomposition Workflow for ATP](https://arxiv.org/abs/2603.24465)
- [FormaRL: Enhancing Autoformalization with no Labeled Data](https://arxiv.org/abs/2508.18914)
- [Online Reinforcement Learning for Autoformalization (ResearchGate)](https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization)
- [Process-Driven Autoformalization in Lean 4 (OpenReview)](https://openreview.net/forum?id=k8KsI84Ds7)
- [Major Breakthroughs in Lean 4-Based Auto-Formalized Mathematics](https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html)
- [RLVR Beyond Math and Code: The Verifier Problem (Subhadip Mitra)](https://subhadipmitra.com/blog/2026/rlvr-beyond-math-code/)
- [Awesome-RLVR (GitHub)](https://github.com/opendilab/awesome-RLVR)

agentId: ae143030d110626ae (use SendMessage with to: 'ae143030d110626ae' to continue this agent)
&lt;usage>total_tokens: 31110
tool_uses: 26
duration_ms: 217177&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c323f52c-ca9e-4431-bbef-e91b07f0b25e",
  "isSidechain": false,
  "promptId": "c8f8bb74-4b57-4255-9fe8-15c0a5831ab6",
  "type": "user",
  "uuid": "6a5d92ce-425d-48d4-afc1-c1ac33b6a241",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to deeply research two topics:\n\n1. **Proof-Verifier (ICLR 2026)** - A paper that addresses dense reward for theorem proving RL via a learned verifier, achieving 93% verification accuracy. Search for:\n   - \"Proof-Verifier ICLR 2026 dense reward theorem proving\"\n   - \"learned verifier theorem proving RL reward ICLR 2026\"\n   - Extract full title, authors, approach, how their learned verifier works, results, and how it compares to compiler-based verification\n\n2. **Autoformalization + sorry mechanisms** - I need to understand the current state of autoformalization (bridging informal/natural language math to formal proofs) and how sorry-based decomposition could connect to it. Search for:\n   - \"autoformalization theorem proving 2025 2026\"\n   - \"informal to formal proof translation sorry\"\n   - \"autoformalization Lean survey 2025 2026\"\n   - \"Hilbert autoformalization informal reasoning formal proofs\"\n   Key questions: How does Hilbert connect informal reasoning to formal proofs? What is the current SOTA in autoformalization? How could sorry-based RL reward training improve autoformalization?\n\nPlease fetch and read actual papers. Report detailed findings (400+ words per topic).",
    "agentId": "ae143030d110626ae",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information on both topics. Let me compile the detailed findings.\n\n---\n\n## Topic 1: Proof-Verifier (ICLR 2026)\n\n**Full Title:** \"Proof-Verifier: Enabling Reinforcement Learning from Verifiable Rewards for Mathematical Theorem Proving\"\n\n**Authors:** Zhiyuan Fan, Dadi Guo, Zhitao He, Elias Stengel-Eskin, Mohit Bansal, Yi R. Fung\n\n**The Problem.** Reinforcement Learning from Verifiable Rewards (RLVR) has proven highly effective for mathematical tasks with clear numerical answers, but extending it to theorem proving faces a fundamental \"verification bottleneck.\" Unlike arithmetic or algebra where answers can be checked against a ground truth, theorem proving generates entire reasoning processes -- complete proofs -- that lack reliable automated verification. Current automated theorem provers (ATPs) and formal compilers provide only coarse-grained binary labels (correct/incorrect) and cannot distinguish between a minor computational error and a fundamental logical flaw. Both receive the same \"incorrect\" label, offering no gradient of useful feedback for RL training.\n\n**Approach: The Learned Generative Verifier.** Proof-Verifier is the first generative verifier specifically designed for RLVR in theorem proving. Unlike a compiler that outputs pass/fail, Proof-Verifier generates a comprehensive verification trajectory containing: (1) detailed error analysis, (2) evaluation scores on a continuous scale, (3) actionable feedback explaining what went wrong, and (4) final verification labels. This provides the dense, fine-grained reward signal that RL training needs.\n\n**Two-Stage Coarse-to-Fine Reward Modeling.** Training the verifier uses a novel two-stage mechanism. Stage 1 (coarse-grained) trains the model on binary correct/incorrect judgments to build a broad understanding of proof validity. Stage 2 (fine-grained) refines the model to produce detailed, continuous-valued assessments that distinguish severity of errors, provide localized feedback, and score proof quality along multiple dimensions.\n\n**Formal-to-Informal Translation Pipeline.** To generate high-quality training data, the authors developed a pipeline that translates formal proofs (from Lean/Isabelle-style formal corpora) into natural language equivalents. This produces synthetic paired data of proofs and their verification judgments, allowing training on both formal and informal proofs -- a key distinction, since most real-world theorem proving by LLMs produces natural language proofs rather than formal tactic sequences.\n\n**Results.**\n- 93% verification accuracy on proof correctness judgments\n- 79% win rate in best-of-N sampling (test-time scaling), meaning the verifier reliably selects correct proofs from multiple candidates\n- 32% improvement in multi-turn proof refinement, where the verifier's feedback guides iterative proof correction\n- Successful single-turn and multi-turn RLVR training with consistent improvements to LLM theorem proving performance\n\n**Comparison to Compiler-Based Verification.** The core thesis of Proof-Verifier is that compiler-based verification (e.g., Lean type-checker) is insufficient for RL reward signals in theorem proving. Compilers provide binary pass/fail, cannot handle natural language proofs at all, and give no partial credit or diagnostic information. Proof-Verifier addresses all three limitations: it works on informal proofs, provides continuous reward scores, and generates actionable feedback. However, compiler-based verification remains the gold standard for formal correctness -- Proof-Verifier complements rather than replaces it by enabling RL training on the much larger space of informal proofs.\n\n---\n\n## Topic 2: Autoformalization and Sorry-Based Decomposition\n\n### Current State of Autoformalization\n\nAutoformalization -- automatically translating informal mathematics into formal, verifiable representations -- has seen dramatic progress in 2025-2026. The comprehensive survey \"Autoformalization in the Era of Large Language Models\" (Weng, Du, Li et al., May 2025) maps the landscape across two paradigms:\n\n**Rule-based approaches** use explicit logical/syntactic transformations, including controlled natural language systems (Mizar, NaProche) and grammar-based frameworks like GF. These are precise but require extensive manual rule development.\n\n**LLM-based approaches** exploit few-shot learning and can translate between informal and formal mathematical statements with fewer than 5 examples. Key systems include DeepSeek-Prover-V2, Goedel-Prover, InternLM2.5-StepProver, and LLEMMA. Performance varies sharply by difficulty: informal competition-level problems achieve roughly 70% accuracy, but formal translation of the same problems drops to about 30%. On MiniF2F, state-of-the-art systems reach 57.6-88.9% pass rates.\n\nA critical asymmetry exists: translating from formal to informal (informalization) is significantly easier and higher quality than the reverse direction. This asymmetry is exploited for synthetic data generation.\n\n**Key challenges remain:** data scarcity (parallel informal-formal corpora are rare), semantic gaps (informal language is ambiguous and omits implicit knowledge), scalability to research-level mathematics (GPT-O3 solves only 25.2% of Frontier Math problems), and the distinction between syntactic correctness (type-checking) and semantic correctness (the formalization actually captures the intended meaning).\n\n### Hilbert: Bridging Informal Reasoning and Formal Proofs\n\n**Hilbert** (Varambally, Voice et al.; Apple ML Research; NeurIPS 2025 MATH-AI Workshop) is an agentic framework that directly bridges the informal-formal gap through recursive sorry-based decomposition. It orchestrates four components:\n\n1. **Reasoner** (Gemini 2.5 Pro): A general-purpose LLM for informal mathematical reasoning and generating proof sketches\n2. **Prover** (DeepSeek/Goedel-Prover): Specialized model for generating Lean 4 tactics\n3. **Verifier**: The Lean 4 compiler via Kimina Lean Server for automated correctness checking\n4. **Retriever**: A semantic search engine using sentence transformer embeddings against Mathlib's informal descriptions\n\n**How sorry-based decomposition works:** When direct proof fails, the Reasoner generates a \"formal proof sketch\" using `have` statements with `sorry` placeholders -- Lean's keyword that temporarily accepts an unproven statement. This allows structural validation of the overall proof architecture before any subgoal is solved. If subgoals resist standard solving, the algorithm recursively decomposes up to depth D=5, creating nested levels of progressively simpler problems.\n\n**Results:** Hilbert achieves 99.2% on miniF2F (6.6 points above the best publicly available method) and solves 462/660 PutnamBench problems (70.0%), a 422% improvement over the best public baseline. This dramatically narrows the gap between informal reasoning ability (Gemini solves ~83% of PutnamBench informally) and formal proof success.\n\n### DeepSeek-Prover-V2: RL for Subgoal Decomposition\n\nDeepSeek-Prover-V2 uses a closely related sorry-based approach. DeepSeek-V3 generates an informal chain-of-thought alongside a Lean sketch with `sorry` placeholders for unresolved subgoals. A specialized 7B prover recursively solves each subgoal. The complete proof is then paired with the original informal reasoning, creating supervised training data for formal-informal alignment. The 671B model achieves 88.9% on MiniF2F-test.\n\n### Mechanic: The Sorrifier-Driven Workflow\n\n**Mechanic** (March 2026, Chinese Academy of Sciences) introduces the \"Sorrifier\" -- a tool that systematically replaces erroneous proof blocks with `sorry` until the code compiles. It targets the innermost reported error, replaces it with `sorry`, recompiles, and repeats. Each sorry location is then extracted into a clean, self-contained subproblem with relevant hypotheses. Results: 11/12 Putnam 2025 problems solved, 4/4 IMO 2025 problems, with substantially shorter proofs (avg 656 lines vs. 1,161 for Seed-Prover) and lower cost ($18.5 vs. $72.7 for Numina per proof).\n\n### RL Reward Training for Autoformalization\n\nTwo key works address RL reward signals for autoformalization directly:\n\n**FormaRL** (Huang, Jin et al.) uses GRPO with a composite reward combining Lean compiler type-checking (syntactic) with LLM-based consistency checking (semantic). Using only 859 unlabeled data samples, it improved ProofNet pass@1 from 4.04% to 26.15% -- a 6.5x improvement -- demonstrating that RL can dramatically improve autoformalization even without labeled data.\n\n**Online RL for Autoformalization** (NeurIPS 2025 MAR Workshop) identifies a critical failure mode: using type-check success alone as a reward produces syntactically valid but semantically vacuous outputs (reward hacking). The solution is composite rewards combining: (i) exact-match metrics (BEq/BEq+) when ground-truth exists, and (ii) continuous embedding-based similarity rewards requiring no paired data.\n\n### How Sorry-Based RL Reward Could Improve Autoformalization\n\nThe connection between sorry-based decomposition and autoformalization improvement is becoming increasingly clear:\n\n1. **Dense intermediate rewards:** Instead of a binary \"does the whole proof compile?\" signal, sorry-based decomposition creates multiple verification checkpoints. Each successfully filled sorry yields a partial reward, providing the dense signal that RL training requires.\n\n2. **Compositional autoformalization:** Rather than translating an entire informal proof at once, sorry-based methods decompose into subgoals that can be autoformalized independently -- reducing the difficulty of each translation step.\n\n3. **Curriculum learning via sorry depth:** The recursive decomposition naturally creates a difficulty hierarchy. RL agents can be trained first on shallow, simple subgoals and progressively tackle deeper decompositions.\n\n4. **Hybrid reward signals:** Combining compiler feedback (does the sorry-free subgoal compile?) with semantic similarity rewards (does the formal statement match the informal intent?) addresses both the syntactic and semantic challenges identified in the autoformalization literature.\n\n---\n\n### Sources\n\n- [Proof-Verifier: Enabling RLVR for Mathematical Theorem Proving (OpenReview)](https://openreview.net/forum?id=FAe9Gts2Qd)\n- [Proof-Verifier PDF](https://openreview.net/pdf?id=FAe9Gts2Qd)\n- [Autoformalization in the Era of Large Language Models: A Survey](https://arxiv.org/abs/2505.23486v2)\n- [Autoformalization Survey HTML](https://arxiv.org/html/2505.23486v1)\n- [Hilbert: Recursively Building Formal Proofs with Informal Reasoning](https://arxiv.org/abs/2509.22819)\n- [Hilbert - Apple ML Research](https://machinelearning.apple.com/research/hilbert)\n- [ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings](https://arxiv.org/abs/2510.15681)\n- [DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via RL for Subgoal Decomposition](https://arxiv.org/abs/2504.21801)\n- [Mechanic: Sorrifier-Driven Formal Decomposition Workflow for ATP](https://arxiv.org/abs/2603.24465)\n- [FormaRL: Enhancing Autoformalization with no Labeled Data](https://arxiv.org/abs/2508.18914)\n- [Online Reinforcement Learning for Autoformalization (ResearchGate)](https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization)\n- [Process-Driven Autoformalization in Lean 4 (OpenReview)](https://openreview.net/forum?id=k8KsI84Ds7)\n- [Major Breakthroughs in Lean 4-Based Auto-Formalized Mathematics](https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html)\n- [RLVR Beyond Math and Code: The Verifier Problem (Subhadip Mitra)](https://subhadipmitra.com/blog/2026/rlvr-beyond-math-code/)\n- [Awesome-RLVR (GitHub)](https://github.com/opendilab/awesome-RLVR)"
      }
    ],
    "totalDurationMs": 217177,
    "totalTokens": 31110,
    "totalToolUseCount": 26,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1481,
      "cache_read_input_tokens": 26549,
      "output_tokens": 3079,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1481
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3079,
          "cache_read_input_tokens": 26549,
          "cache_creation_input_tokens": 1481,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1481,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 26
    }
  },
  "sourceToolAssistantUUID": "c323f52c-ca9e-4431-bbef-e91b07f0b25e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-27T18:06:52.092Z_

<details open><summary>🔧 Tool call — Agent · `toolu_015TmmrjXM3Ga2HVgWnYPQd2`</summary>

```json
{
  "description": "Research SGVR, Process-RL, benchmarks",
  "prompt": "I need to deeply research three topics:\n\n1. **SGVR (Sub-Goal Verifiable Reward, January 2026)** - \"Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward\". I need:\n   - Exact formulation of skeleton_rate = verified_subgoals/total_subgoals\n   - How they implement this in GRPO\n   - Their results (+9.7% on geometry)\n   - What differentiates this from applying the same idea in formal theorem proving\n   - Authors and venue\n\n2. **Process-Verified RL for Theorem Proving** - The reviewer says this was published at ICLR 2026 (NOT NeurIPS 2025 as we cited). Search for:\n   - \"Process-Verified Reinforcement Learning Theorem Proving Lean ICLR 2026\"\n   - Confirm the venue\n   - Their tactic-level process reward approach\n   - How tactic-level differs from subgoal-level\n   - Full title and authors\n\n3. **Current theorem proving benchmarks and SOTA (May 2026)**:\n   - MiniF2F current SOTA (is it really saturated? what are the top scores?)\n   - PutnamBench SOTA\n   - SorryDB as evaluation\n   - ProofNet benchmark\n   - Any newer harder benchmarks\n   - Search \"theorem proving benchmark SOTA 2026\" and \"PutnamBench leaderboard 2026\"\n\nReport detailed findings for each topic (300+ words each).",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a5d92ce-425d-48d4-afc1-c1ac33b6a241",
  "isSidechain": false,
  "requestId": "req_011CbTX1pHC4GuAqban1peui",
  "type": "assistant",
  "uuid": "db6f7384-af8c-42e8-8123-12438d8964ce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014tRtkVPKmbXCHfbVfbyZhB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3551,
      "cache_read_input_tokens": 24933,
      "output_tokens": 467,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3551,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 467,
          "cache_read_input_tokens": 24933,
          "cache_creation_input_tokens": 3551,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3551
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-27T18:10:39.050Z_

<details><summary>↩ Tool result · `toolu_015TmmrjXM3Ga2HVgWnYPQd2`</summary>

```text
Now I have comprehensive information on all three topics. Here is the detailed report:

---

## Topic 1: SGVR (Sub-Goal Verifiable Reward, January 2026)

**Full Title:** "Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward"

**Authors:** Jianlong Chen, Daocheng Fu, Shengze Xu, Jiawei Chen, Yuan Feng, Yue Yang, Junchi Yan, Hongyuan Zha, and Renqiu Xia

**Affiliations:** The Chinese University of Hong Kong, Shenzhen (CUHKSZ); Shanghai Jiao Tong University (SJTU); Fudan University; The Chinese University of Hong Kong; University of Science and Technology Beijing

**Venue:** arXiv preprint (arXiv:2601.05073), submitted January 8, 2026. No confirmed peer-reviewed venue at this time. Code repository at [GitHub: FrontierX-Lab/SGVR](https://github.com/FrontierX-Lab/SGVR).

### Skeleton Rate Formulation

The Skeleton Rate (SR) measures average step-wise correctness across sub-goals. The exact formulation is:

**SR = (1/N) * sum_{i=1}^{N} (1/n_i) * sum_{t=1}^{n_i} I(y_hat_{i,t} = y_{i,t})**

Where for instance i with n_i sub-goals, it computes the fraction of correctly predicted intermediate values compared to ground truth. The indicator function I returns 1 when predicted value matches ground truth, 0 otherwise. This produces a normalized score between 0 and 1 representing the percentage of intermediate steps solved correctly.

Two companion metrics exist:
- **Skeleton Completion (SC):** Requires ALL sub-goals to be correct: SC = (1/N) * sum_i prod_t I(y_hat_{i,t} = y_{i,t}). This captures end-to-end consistency.
- **Consistency Ratio (CR):** CR = SC_dataset / SR_dataset. A low CR reveals that models solve many individual sub-goals correctly yet fail to maintain end-to-end consistency.

### GRPO Integration

The reward function replaces the sparse binary outcome signal with the granular skeleton rate:

**R(y) = SR_i = (1/n_i) * sum_{t=1}^{n_i} I(y_hat_{i,t} = y_{i,t})**

Rather than assigning 0 or 1 based solely on final answer correctness, trajectories correctly solving 80% of sub-goals receive substantially higher rewards than those solving only 20%. The paper describes this as "providing step-by-step supervision that guides the model to incrementally improve its reasoning process."

The GRPO optimizer then computes group-relative advantages: **A_i = (r_i - mean({r_1,...,r_G})) / (std({r_1,...,r_G}) + epsilon)**. This is the standard GRPO formulation, but now r_i is the dense skeleton-rate reward rather than a binary outcome.

### GeoGoal Benchmark

The benchmark (GeoGoal) comprises 256 training and 256 test instances, constructed via three steps: (1) Formal skeleton generation via TrustGeoGen engine producing verified logical chains, (2) Decomposition into atomic reasoning steps mapped to numeric sub-goals, (3) Sequential organization with the final sub-goal corresponding to the original problem's answer.

### Results

- **Geometric reasoning:** SR improved from 50.2% to 87.7% (+37.5%) on GeoGoal; external geometry benchmarks averaged +4.0% improvement; GeoPQA-Test: +6.4% (7B model), +7.2% (3B model). The headline figure of "+9.7% on geometry" is the aggregated improvement.
- **Cross-domain transfer:** General mathematics (AMC): +12.1% (7B), +6.0% (3B). LiveBench-Reasoning: +3.5% (7B), +7.0% (3B). Overall reported as "+8.0% on general math, +2.8% on general reasoning."

### Differentiation from Formal Theorem Proving

The key distinction is the nature of the verification. In formal theorem proving (e.g., Lean-based approaches), each tactic step is verified via type-checking -- the proof assistant serves as a symbolic process oracle verifying that each step preserves logical soundness within a formal type theory. In SGVR, sub-goals are automatically verifiable *numeric* values (intermediate geometric computation results), not formally verified logical proof states. The paper explicitly notes that "outcome accuracy alone is not a faithful proxy for step-wise reasoning reliability" -- models can achieve correct final answers despite flawed intermediate steps. This is a problem that formal theorem proving inherently avoids since each tactic must type-check. SGVR's approach is designed for informal mathematical reasoning (natural language geometry problem solving by MLLMs), where no formal proof assistant exists, and the "verification" is matching predicted numeric sub-goal values against ground truth rather than type-theoretic checking.

---

## Topic 2: Process-Verified RL for Theorem Proving

**Full Title:** "Process-Verified Reinforcement Learning for Theorem Proving via Lean"

**Authors:** Minsu Kim and Se-Young Yun (KAIST)

**Venue:** This is a critical finding. The paper appeared at **NeurIPS 2025 as a workshop paper** (MATH-AI: The 5th Workshop on Mathematical Reasoning and AI), and was subsequently **published as a conference paper at ICLR 2026**. The OpenReview page ([link](https://openreview.net/forum?id=P00k4DFaXF)) and the published PDF both confirm "Published as a conference paper at ICLR 2026." So the reviewer's claim that it was published at ICLR 2026 (not NeurIPS 2025) is **correct** -- the NeurIPS 2025 appearance was only a workshop version, and the full conference publication is ICLR 2026.

### Tactic-Level Process Reward Approach

The core insight is that Lean's proof assistant itself serves as a "symbolic process oracle" providing both outcome-level and fine-grained tactic-level verified feedback during training. The approach works as follows:

1. **Tactic-level parsing:** Proof attempts are parsed into tactic sequences. Lean's elaboration engine marks both locally sound steps (tactics that successfully modify the proof state) and the earliest failing step.
2. **Dense credit signals:** This yields verifier-grounded credit signals rooted in type theory. Unlike binary outcome verification (proof compiles or not), each individual tactic gets a verified signal.
3. **First-error propagation:** Rewards propagate from the first erroneous tactic forward. Once Lean identifies the earliest failing step, subsequent tactics are also penalized, reflecting that errors compound in proof construction.
4. **First-token credit:** Credit is assigned at the first token of each tactic, providing a precise signal for which part of the generated sequence the reward pertains to.
5. **GRPO-style objective:** These structured signals are incorporated into a GRPO-style reinforcement learning objective that balances outcome-level and process-level advantages.

### Tactic-Level vs. Subgoal-Level (Key Distinction)

Tactic-level feedback operates at the granularity of individual proof commands (e.g., `apply`, `rw`, `simp`, `ring`) -- each tactic is checked by Lean's type-checker for local soundness. This is fundamentally different from SGVR's subgoal-level approach:

- **Granularity:** Tactics are individual proof steps (often one per line); sub-goals in SGVR are intermediate numeric computation results that may span multiple reasoning steps.
- **Verification mechanism:** Tactic verification uses formal type-checking (sound by construction); SGVR verification uses numeric value matching (empirical correctness).
- **Error semantics:** A failed tactic means the proof state is invalid (type error); a failed sub-goal in SGVR means an incorrect intermediate number but the model can still proceed (and even get the final answer right by luck).
- **Domain:** Tactic-level is specific to formal theorem proving in proof assistants; subgoal-level is designed for informal mathematical reasoning.

### Results

The paper demonstrates improvements on MiniF2F and ProofNet benchmarks, tested on models like STP-Lean and DeepSeek-Prover-V1.5. The paper shows that "tactic-level supervision outperforms outcome-only baselines in most settings."

---

## Topic 3: Current Theorem Proving Benchmarks and SOTA (May 2026)

### MiniF2F -- Effectively Saturated

MiniF2F consists of 488 manually curated Olympiad-style problems formalized in Lean (and other proof assistants). As of mid-2026, it is essentially saturated:

- **HILBERT** (Apple): **99.2%** on miniF2F -- fails on only 2 problems (AMC 12A 2020 Problem 25 and IMO Shortlist 2007 Problem A6). Uses Gemini 2.5 Pro + Goedel-Prover-V2-32B in an agentic framework with recursive decomposition. Published at ICLR 2026.
- **Seed-Prover** (ByteDance): **100.0% on MiniF2F-valid, 99.6% on MiniF2F-test** using medium inference. Uses a three-tiered inference strategy for deep and broad thinking.
- **AlphaProof** (DeepMind): Also saturated MiniF2F.
- **Goedel-Prover-V2-32B**: 88.1% at pass@32 standard mode, 90.4% with self-correction. Published at ICLR 2026.
- Previous SOTA: DeepSeek-Prover-V2 at 90.6%, Kimina-Prover at 92.2%.

**Conclusion: MiniF2F is indeed saturated.** Multiple systems achieve 99%+ and the benchmark no longer discriminates between top systems. The community paper "miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward" explicitly addresses this.

### PutnamBench

PutnamBench formalizes 640-672 problems (depending on the proof assistant) from the William Lowell Putnam Mathematical Competition across algebra, analysis, number theory, geometry, combinatorics, probability, and set theory. Available in Lean (672 problems), Isabelle (640), and Coq (412).

Current leaders:
- **Aleph** (Logical Intelligence): **668/672 (99.4%)** -- announced January 21, 2026. Uses an agentic orchestration layer with GPT-5.2 performing planning, proving, and refining. Also identified and corrected ~15 problematic formalizations in the benchmark itself. Comfortably tops the leaderboard ahead of ByteDance and Apple.
- **HILBERT** (Apple): **70.0%** -- nearly 20 percentage points above previous methods at time of publication.
- **Seed-Prover**: >50% on PutnamBench.
- **Goedel-Prover-V2-32B**: 86 problems solved at pass@184, surpassing DeepSeek-Prover-V2-671B's 47 problems at pass@1024.

Leaderboard: [PutnamBench Leaderboard](https://trishullab.github.io/PutnamBench/leaderboard.html)

### SorryDB

**Full title:** "SorryDB: Can AI Provers Complete Real-World Lean Theorems?"

**Authors:** Austin Letson, Leopoldo Sarra, Auguste Poiroux, Oliver Dressler, Paul Lezeau, Dhyan Aranha, Frederick Pu, Aaron Hill, Miguel Corredera Hidalgo, Julian Berman, George Tsoukalas, and Lenny Taelman. Published March 2026 (arXiv:2603.02668).

SorryDB is a dynamically-updating benchmark of open Lean tasks drawn from 78 real-world formalization projects on GitHub. It extracts theorems marked with `sorry` (unproven) from open-source Lean repositories. The January 2026 snapshot contains 1,000 tasks. Key advantages over static benchmarks:
- **Not saturated:** Current approaches solve only a fraction.
- **Mitigates contamination:** Continuously updated stream of new tasks.
- **Practical alignment:** "Hillclimbing the SorryDB benchmark will yield tools aligned to community needs and more usable by mathematicians."
- **Complementary models:** An agentic approach based on Gemini Flash was the most performant but was not strictly better than other off-the-shelf LLMs and specialized provers.

### ProofNet

ProofNet consists of 371 examples with formal statements in Lean 3, covering undergraduate pure mathematics (real/complex analysis, linear algebra, abstract algebra, topology). Current SOTA: **BFS-Prover-V2 at 41.4%** (as of late 2025). This benchmark remains unsaturated and challenging.

### FormalProofBench

**Full title:** "FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?"

**Authors:** Nikil Ravi, Kexing Ying, Vasilii Nesterov, Rayan Krishnan, Elif Uskuplu, Bingyu Xia, Janitha Aswedige, Langston Nashold. Published March 2026 (arXiv:2603.26996). Accepted at ICLR 2026 Workshop (VerifAI-2).

Targets advanced undergraduate and graduate mathematics from qualifying exams and textbooks, using Lean 4. Best model achieves only **33.5% accuracy**, with rapid performance dropoff. Topics: analysis, algebra, probability, logic.

### Newer/Harder Benchmarks

Several newer benchmarks have emerged to address MiniF2F saturation:

1. **FormalMATH**: Large-scale Lean 4 benchmark with 5,560 formally verified statements across algebra, geometry, calculus, number theory, with multiple difficulty levels.
2. **FATE**: Focuses on abstract and commutative algebra reflecting modern mathematics research. FATE-M is ~50% solvable; FATE-H at ~3%; FATE-X at 0% solved.
3. **miniCTX**: Addresses the ability to use long contexts in theorem proving, offering more realistic evaluation.
4. **TaoBench**: "Do Automated Theorem Prover LLMs Generalize Beyond MathLib?" -- tests generalization to non-standard libraries.
5. **VeriBench-FTP**: Another formal theorem proving benchmark submitted to venues in 2026.

---

Sources:
- [SGVR Paper (arXiv)](https://arxiv.org/abs/2601.05073)
- [SGVR HTML Version](https://arxiv.org/html/2601.05073v1)
- [SGVR GitHub Repository](https://github.com/FrontierX-Lab/SGVR)
- [SGVR Hugging Face Page](https://huggingface.co/papers/2601.05073)
- [Process-Verified RL OpenReview (ICLR 2026)](https://openreview.net/forum?id=P00k4DFaXF)
- [Process-Verified RL NeurIPS 2025 Workshop](https://neurips.cc/virtual/2025/131058)
- [Aleph Solves PutnamBench (99.4%)](https://logicalintelligence.com/blog/aleph-solves-putnambench)
- [PutnamBench Leaderboard](https://trishullab.github.io/PutnamBench/leaderboard.html)
- [HILBERT (Apple) - ICLR 2026](https://arxiv.org/abs/2509.22819)
- [Seed-Prover](https://arxiv.org/abs/2507.23726)
- [Goedel-Prover-V2 (ICLR 2026)](https://arxiv.org/abs/2508.03613)
- [SorryDB (arXiv)](https://arxiv.org/abs/2603.02668)
- [FormalProofBench (arXiv)](https://arxiv.org/abs/2603.26996)
- [ProofNet](https://huggingface.co/papers/2302.12433)
- [MiniF2F Revisited](https://arxiv.org/pdf/2511.03108)
- [FormalMATH](https://arxiv.org/pdf/2505.02735)
- [TaoBench](https://arxiv.org/html/2603.12744)

agentId: aa24e789d008980c4 (use SendMessage with to: 'aa24e789d008980c4' to continue this agent)
&lt;usage>total_tokens: 34056
tool_uses: 28
duration_ms: 226951&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db6f7384-af8c-42e8-8123-12438d8964ce",
  "isSidechain": false,
  "promptId": "c8f8bb74-4b57-4255-9fe8-15c0a5831ab6",
  "type": "user",
  "uuid": "e95eb0f0-a971-4ee7-b9c3-3df08bc6ba6c",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to deeply research three topics:\n\n1. **SGVR (Sub-Goal Verifiable Reward, January 2026)** - \"Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward\". I need:\n   - Exact formulation of skeleton_rate = verified_subgoals/total_subgoals\n   - How they implement this in GRPO\n   - Their results (+9.7% on geometry)\n   - What differentiates this from applying the same idea in formal theorem proving\n   - Authors and venue\n\n2. **Process-Verified RL for Theorem Proving** - The reviewer says this was published at ICLR 2026 (NOT NeurIPS 2025 as we cited). Search for:\n   - \"Process-Verified Reinforcement Learning Theorem Proving Lean ICLR 2026\"\n   - Confirm the venue\n   - Their tactic-level process reward approach\n   - How tactic-level differs from subgoal-level\n   - Full title and authors\n\n3. **Current theorem proving benchmarks and SOTA (May 2026)**:\n   - MiniF2F current SOTA (is it really saturated? what are the top scores?)\n   - PutnamBench SOTA\n   - SorryDB as evaluation\n   - ProofNet benchmark\n   - Any newer harder benchmarks\n   - Search \"theorem proving benchmark SOTA 2026\" and \"PutnamBench leaderboard 2026\"\n\nReport detailed findings for each topic (300+ words each).",
    "agentId": "aa24e789d008980c4",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information on all three topics. Here is the detailed report:\n\n---\n\n## Topic 1: SGVR (Sub-Goal Verifiable Reward, January 2026)\n\n**Full Title:** \"Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward\"\n\n**Authors:** Jianlong Chen, Daocheng Fu, Shengze Xu, Jiawei Chen, Yuan Feng, Yue Yang, Junchi Yan, Hongyuan Zha, and Renqiu Xia\n\n**Affiliations:** The Chinese University of Hong Kong, Shenzhen (CUHKSZ); Shanghai Jiao Tong University (SJTU); Fudan University; The Chinese University of Hong Kong; University of Science and Technology Beijing\n\n**Venue:** arXiv preprint (arXiv:2601.05073), submitted January 8, 2026. No confirmed peer-reviewed venue at this time. Code repository at [GitHub: FrontierX-Lab/SGVR](https://github.com/FrontierX-Lab/SGVR).\n\n### Skeleton Rate Formulation\n\nThe Skeleton Rate (SR) measures average step-wise correctness across sub-goals. The exact formulation is:\n\n**SR = (1/N) * sum_{i=1}^{N} (1/n_i) * sum_{t=1}^{n_i} I(y_hat_{i,t} = y_{i,t})**\n\nWhere for instance i with n_i sub-goals, it computes the fraction of correctly predicted intermediate values compared to ground truth. The indicator function I returns 1 when predicted value matches ground truth, 0 otherwise. This produces a normalized score between 0 and 1 representing the percentage of intermediate steps solved correctly.\n\nTwo companion metrics exist:\n- **Skeleton Completion (SC):** Requires ALL sub-goals to be correct: SC = (1/N) * sum_i prod_t I(y_hat_{i,t} = y_{i,t}). This captures end-to-end consistency.\n- **Consistency Ratio (CR):** CR = SC_dataset / SR_dataset. A low CR reveals that models solve many individual sub-goals correctly yet fail to maintain end-to-end consistency.\n\n### GRPO Integration\n\nThe reward function replaces the sparse binary outcome signal with the granular skeleton rate:\n\n**R(y) = SR_i = (1/n_i) * sum_{t=1}^{n_i} I(y_hat_{i,t} = y_{i,t})**\n\nRather than assigning 0 or 1 based solely on final answer correctness, trajectories correctly solving 80% of sub-goals receive substantially higher rewards than those solving only 20%. The paper describes this as \"providing step-by-step supervision that guides the model to incrementally improve its reasoning process.\"\n\nThe GRPO optimizer then computes group-relative advantages: **A_i = (r_i - mean({r_1,...,r_G})) / (std({r_1,...,r_G}) + epsilon)**. This is the standard GRPO formulation, but now r_i is the dense skeleton-rate reward rather than a binary outcome.\n\n### GeoGoal Benchmark\n\nThe benchmark (GeoGoal) comprises 256 training and 256 test instances, constructed via three steps: (1) Formal skeleton generation via TrustGeoGen engine producing verified logical chains, (2) Decomposition into atomic reasoning steps mapped to numeric sub-goals, (3) Sequential organization with the final sub-goal corresponding to the original problem's answer.\n\n### Results\n\n- **Geometric reasoning:** SR improved from 50.2% to 87.7% (+37.5%) on GeoGoal; external geometry benchmarks averaged +4.0% improvement; GeoPQA-Test: +6.4% (7B model), +7.2% (3B model). The headline figure of \"+9.7% on geometry\" is the aggregated improvement.\n- **Cross-domain transfer:** General mathematics (AMC): +12.1% (7B), +6.0% (3B). LiveBench-Reasoning: +3.5% (7B), +7.0% (3B). Overall reported as \"+8.0% on general math, +2.8% on general reasoning.\"\n\n### Differentiation from Formal Theorem Proving\n\nThe key distinction is the nature of the verification. In formal theorem proving (e.g., Lean-based approaches), each tactic step is verified via type-checking -- the proof assistant serves as a symbolic process oracle verifying that each step preserves logical soundness within a formal type theory. In SGVR, sub-goals are automatically verifiable *numeric* values (intermediate geometric computation results), not formally verified logical proof states. The paper explicitly notes that \"outcome accuracy alone is not a faithful proxy for step-wise reasoning reliability\" -- models can achieve correct final answers despite flawed intermediate steps. This is a problem that formal theorem proving inherently avoids since each tactic must type-check. SGVR's approach is designed for informal mathematical reasoning (natural language geometry problem solving by MLLMs), where no formal proof assistant exists, and the \"verification\" is matching predicted numeric sub-goal values against ground truth rather than type-theoretic checking.\n\n---\n\n## Topic 2: Process-Verified RL for Theorem Proving\n\n**Full Title:** \"Process-Verified Reinforcement Learning for Theorem Proving via Lean\"\n\n**Authors:** Minsu Kim and Se-Young Yun (KAIST)\n\n**Venue:** This is a critical finding. The paper appeared at **NeurIPS 2025 as a workshop paper** (MATH-AI: The 5th Workshop on Mathematical Reasoning and AI), and was subsequently **published as a conference paper at ICLR 2026**. The OpenReview page ([link](https://openreview.net/forum?id=P00k4DFaXF)) and the published PDF both confirm \"Published as a conference paper at ICLR 2026.\" So the reviewer's claim that it was published at ICLR 2026 (not NeurIPS 2025) is **correct** -- the NeurIPS 2025 appearance was only a workshop version, and the full conference publication is ICLR 2026.\n\n### Tactic-Level Process Reward Approach\n\nThe core insight is that Lean's proof assistant itself serves as a \"symbolic process oracle\" providing both outcome-level and fine-grained tactic-level verified feedback during training. The approach works as follows:\n\n1. **Tactic-level parsing:** Proof attempts are parsed into tactic sequences. Lean's elaboration engine marks both locally sound steps (tactics that successfully modify the proof state) and the earliest failing step.\n2. **Dense credit signals:** This yields verifier-grounded credit signals rooted in type theory. Unlike binary outcome verification (proof compiles or not), each individual tactic gets a verified signal.\n3. **First-error propagation:** Rewards propagate from the first erroneous tactic forward. Once Lean identifies the earliest failing step, subsequent tactics are also penalized, reflecting that errors compound in proof construction.\n4. **First-token credit:** Credit is assigned at the first token of each tactic, providing a precise signal for which part of the generated sequence the reward pertains to.\n5. **GRPO-style objective:** These structured signals are incorporated into a GRPO-style reinforcement learning objective that balances outcome-level and process-level advantages.\n\n### Tactic-Level vs. Subgoal-Level (Key Distinction)\n\nTactic-level feedback operates at the granularity of individual proof commands (e.g., `apply`, `rw`, `simp`, `ring`) -- each tactic is checked by Lean's type-checker for local soundness. This is fundamentally different from SGVR's subgoal-level approach:\n\n- **Granularity:** Tactics are individual proof steps (often one per line); sub-goals in SGVR are intermediate numeric computation results that may span multiple reasoning steps.\n- **Verification mechanism:** Tactic verification uses formal type-checking (sound by construction); SGVR verification uses numeric value matching (empirical correctness).\n- **Error semantics:** A failed tactic means the proof state is invalid (type error); a failed sub-goal in SGVR means an incorrect intermediate number but the model can still proceed (and even get the final answer right by luck).\n- **Domain:** Tactic-level is specific to formal theorem proving in proof assistants; subgoal-level is designed for informal mathematical reasoning.\n\n### Results\n\nThe paper demonstrates improvements on MiniF2F and ProofNet benchmarks, tested on models like STP-Lean and DeepSeek-Prover-V1.5. The paper shows that \"tactic-level supervision outperforms outcome-only baselines in most settings.\"\n\n---\n\n## Topic 3: Current Theorem Proving Benchmarks and SOTA (May 2026)\n\n### MiniF2F -- Effectively Saturated\n\nMiniF2F consists of 488 manually curated Olympiad-style problems formalized in Lean (and other proof assistants). As of mid-2026, it is essentially saturated:\n\n- **HILBERT** (Apple): **99.2%** on miniF2F -- fails on only 2 problems (AMC 12A 2020 Problem 25 and IMO Shortlist 2007 Problem A6). Uses Gemini 2.5 Pro + Goedel-Prover-V2-32B in an agentic framework with recursive decomposition. Published at ICLR 2026.\n- **Seed-Prover** (ByteDance): **100.0% on MiniF2F-valid, 99.6% on MiniF2F-test** using medium inference. Uses a three-tiered inference strategy for deep and broad thinking.\n- **AlphaProof** (DeepMind): Also saturated MiniF2F.\n- **Goedel-Prover-V2-32B**: 88.1% at pass@32 standard mode, 90.4% with self-correction. Published at ICLR 2026.\n- Previous SOTA: DeepSeek-Prover-V2 at 90.6%, Kimina-Prover at 92.2%.\n\n**Conclusion: MiniF2F is indeed saturated.** Multiple systems achieve 99%+ and the benchmark no longer discriminates between top systems. The community paper \"miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward\" explicitly addresses this.\n\n### PutnamBench\n\nPutnamBench formalizes 640-672 problems (depending on the proof assistant) from the William Lowell Putnam Mathematical Competition across algebra, analysis, number theory, geometry, combinatorics, probability, and set theory. Available in Lean (672 problems), Isabelle (640), and Coq (412).\n\nCurrent leaders:\n- **Aleph** (Logical Intelligence): **668/672 (99.4%)** -- announced January 21, 2026. Uses an agentic orchestration layer with GPT-5.2 performing planning, proving, and refining. Also identified and corrected ~15 problematic formalizations in the benchmark itself. Comfortably tops the leaderboard ahead of ByteDance and Apple.\n- **HILBERT** (Apple): **70.0%** -- nearly 20 percentage points above previous methods at time of publication.\n- **Seed-Prover**: >50% on PutnamBench.\n- **Goedel-Prover-V2-32B**: 86 problems solved at pass@184, surpassing DeepSeek-Prover-V2-671B's 47 problems at pass@1024.\n\nLeaderboard: [PutnamBench Leaderboard](https://trishullab.github.io/PutnamBench/leaderboard.html)\n\n### SorryDB\n\n**Full title:** \"SorryDB: Can AI Provers Complete Real-World Lean Theorems?\"\n\n**Authors:** Austin Letson, Leopoldo Sarra, Auguste Poiroux, Oliver Dressler, Paul Lezeau, Dhyan Aranha, Frederick Pu, Aaron Hill, Miguel Corredera Hidalgo, Julian Berman, George Tsoukalas, and Lenny Taelman. Published March 2026 (arXiv:2603.02668).\n\nSorryDB is a dynamically-updating benchmark of open Lean tasks drawn from 78 real-world formalization projects on GitHub. It extracts theorems marked with `sorry` (unproven) from open-source Lean repositories. The January 2026 snapshot contains 1,000 tasks. Key advantages over static benchmarks:\n- **Not saturated:** Current approaches solve only a fraction.\n- **Mitigates contamination:** Continuously updated stream of new tasks.\n- **Practical alignment:** \"Hillclimbing the SorryDB benchmark will yield tools aligned to community needs and more usable by mathematicians.\"\n- **Complementary models:** An agentic approach based on Gemini Flash was the most performant but was not strictly better than other off-the-shelf LLMs and specialized provers.\n\n### ProofNet\n\nProofNet consists of 371 examples with formal statements in Lean 3, covering undergraduate pure mathematics (real/complex analysis, linear algebra, abstract algebra, topology). Current SOTA: **BFS-Prover-V2 at 41.4%** (as of late 2025). This benchmark remains unsaturated and challenging.\n\n### FormalProofBench\n\n**Full title:** \"FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?\"\n\n**Authors:** Nikil Ravi, Kexing Ying, Vasilii Nesterov, Rayan Krishnan, Elif Uskuplu, Bingyu Xia, Janitha Aswedige, Langston Nashold. Published March 2026 (arXiv:2603.26996). Accepted at ICLR 2026 Workshop (VerifAI-2).\n\nTargets advanced undergraduate and graduate mathematics from qualifying exams and textbooks, using Lean 4. Best model achieves only **33.5% accuracy**, with rapid performance dropoff. Topics: analysis, algebra, probability, logic.\n\n### Newer/Harder Benchmarks\n\nSeveral newer benchmarks have emerged to address MiniF2F saturation:\n\n1. **FormalMATH**: Large-scale Lean 4 benchmark with 5,560 formally verified statements across algebra, geometry, calculus, number theory, with multiple difficulty levels.\n2. **FATE**: Focuses on abstract and commutative algebra reflecting modern mathematics research. FATE-M is ~50% solvable; FATE-H at ~3%; FATE-X at 0% solved.\n3. **miniCTX**: Addresses the ability to use long contexts in theorem proving, offering more realistic evaluation.\n4. **TaoBench**: \"Do Automated Theorem Prover LLMs Generalize Beyond MathLib?\" -- tests generalization to non-standard libraries.\n5. **VeriBench-FTP**: Another formal theorem proving benchmark submitted to venues in 2026.\n\n---\n\nSources:\n- [SGVR Paper (arXiv)](https://arxiv.org/abs/2601.05073)\n- [SGVR HTML Version](https://arxiv.org/html/2601.05073v1)\n- [SGVR GitHub Repository](https://github.com/FrontierX-Lab/SGVR)\n- [SGVR Hugging Face Page](https://huggingface.co/papers/2601.05073)\n- [Process-Verified RL OpenReview (ICLR 2026)](https://openreview.net/forum?id=P00k4DFaXF)\n- [Process-Verified RL NeurIPS 2025 Workshop](https://neurips.cc/virtual/2025/131058)\n- [Aleph Solves PutnamBench (99.4%)](https://logicalintelligence.com/blog/aleph-solves-putnambench)\n- [PutnamBench Leaderboard](https://trishullab.github.io/PutnamBench/leaderboard.html)\n- [HILBERT (Apple) - ICLR 2026](https://arxiv.org/abs/2509.22819)\n- [Seed-Prover](https://arxiv.org/abs/2507.23726)\n- [Goedel-Prover-V2 (ICLR 2026)](https://arxiv.org/abs/2508.03613)\n- [SorryDB (arXiv)](https://arxiv.org/abs/2603.02668)\n- [FormalProofBench (arXiv)](https://arxiv.org/abs/2603.26996)\n- [ProofNet](https://huggingface.co/papers/2302.12433)\n- [MiniF2F Revisited](https://arxiv.org/pdf/2511.03108)\n- [FormalMATH](https://arxiv.org/pdf/2505.02735)\n- [TaoBench](https://arxiv.org/html/2603.12744)"
      }
    ],
    "totalDurationMs": 226951,
    "totalTokens": 34056,
    "totalToolUseCount": 28,
    "usage": {
      "input_tokens": 668,
      "cache_creation_input_tokens": 1013,
      "cache_read_input_tokens": 28228,
      "output_tokens": 4147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1013
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 668,
          "output_tokens": 4147,
          "cache_read_input_tokens": 28228,
          "cache_creation_input_tokens": 1013,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1013,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 28
    }
  },
  "sourceToolAssistantUUID": "db6f7384-af8c-42e8-8123-12438d8964ce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Verifier-Certified Progress Rewards via Sorry-Driven Decomposition\",…",
  "leafUuid": "e95eb0f0-a971-4ee7-b9c3-3df08bc6ba6c",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise sorry-progress reward to address autoformalization gap",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02"
}
```

---

### Tool call

_source line 26 · 2026-05-27T18:10:51.720Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01SGjdKsJeDFLBeCXCgo4udN`</summary>

```json
{
  "description": "Research sorrifier availability and FormaRL",
  "prompt": "I need to research two specific topics:\n\n1. **Mechanic's sorrifier implementation availability**: The reviewer flagged that Mechanic's sorrifier is NOT available as a modularized component (the paper states this is future work). I need to:\n   - Search for \"Mechanic sorrifier GitHub code implementation\" and \"Mechanic theorem proving sorry isolation code 2026\"\n   - Check if there's any open-source implementation\n   - Assess how hard it would be to reimplement from scratch based on the paper's description\n   - Look for alternative sorry-manipulation tools in the Lean ecosystem (e.g., does Lean 4's API natively support sorry insertion/extraction?)\n   - Search for \"Lean 4 sorry API metaprogramming\" and \"sorry extraction Lean 4\"\n\n2. **FormaRL** - A paper about using GRPO with composite reward for autoformalization. Search for:\n   - \"FormaRL autoformalization GRPO Lean 2025 2026\"\n   - How they combine Lean compiler type-checking with LLM-based consistency checking\n   - Their ProofNet results (4.04% → 26.15%)\n   - How this relates to our sorry-based reward idea\n\nReport detailed findings (300+ words per topic).",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e95eb0f0-a971-4ee7-b9c3-3df08bc6ba6c",
  "isSidechain": false,
  "requestId": "req_011CbTXKe1JgTEoP9Pazsifv",
  "type": "assistant",
  "uuid": "bbad86c5-4892-436f-88b6-2b3487788fe8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FmWzkmRiypWXrWZTj35CiG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4689,
      "cache_read_input_tokens": 28484,
      "output_tokens": 392,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4689,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 392,
          "cache_read_input_tokens": 28484,
          "cache_creation_input_tokens": 4689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4689
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-27T18:14:52.029Z_

<details><summary>↩ Tool result · `toolu_01SGjdKsJeDFLBeCXCgo4udN`</summary>

```text
Now I have comprehensive information on both topics. Let me compile the findings.

---

## Research Findings

### 1. Mechanic's Sorrifier Implementation Availability

**Paper and concept overview:** Mechanic (arXiv [2603.24465](https://arxiv.org/abs/2603.24465), March 2026) is an agent system that uses a "sorrifier-driven formal decomposition" strategy for automated theorem proving. The sorrifier works by repeatedly substituting incorrect/failing proof blocks with `sorry` placeholders until the full proof compiles in Lean 4. Once the proof compiles with sorries, each sorry is extracted as a self-contained subgoal with its local context, and an LLM independently resolves each subgoal. Once all subgoals are proven, they are reassembled into the original proof. This avoids both full regeneration from scratch and the excessive context of iterative repair.

**Code availability: No open-source implementation exists.** My searches across GitHub and the broader web found zero code repositories for the Mechanic sorrifier. The paper itself explicitly states: *"In future work, the sorrifier will be modularized as a standalone component integrated into the code agent."* This confirms the reviewer's flag -- the sorrifier is currently not available as a modularized, reusable component. It exists only as an internal part of the Mechanic agent described in the paper.

**Feasibility of reimplementation:** Reimplementing a basic sorrifier from scratch is plausible, though non-trivial, because Lean 4 already provides significant native API support for sorry manipulation:

- **`Lean.Meta.Sorry` module** ([API docs](https://lean-lang.org/doc/api/Lean/Meta/Sorry.html)): Provides core functions for creating and recognizing `sorryAx` terms. Key functions include constructing labeled sorries with source position metadata, and `forEachSorryM` which iterates over every sorry in an expression -- enabling programmatic discovery of all sorry locations.

- **`Lean.Elab.admitGoal`** ([source](https://github.com/leanprover/lean4/blob/master/src/Lean/Elab/Tactic/Basic.lean)): Assigns `mvarId := sorry`, effectively inserting a sorry to close a tactic goal programmatically. Takes an `MVarId` and an optional `synthetic` flag.

- **leanprover-community REPL** ([GitHub](https://github.com/leanprover-community/repl)): A REPL for Lean 4 that returns structured information about errors and sorries. When sorry appears in tactic mode, the response includes `proofState` identifiers for the goal at each sorry. The `CommandResponse` structure includes `env`, `messages`, `sorries`, and `tactics` fields, making it straightforward to extract sorry goals programmatically.

- **Pantograph** ([arXiv 2410.16429](https://arxiv.org/pdf/2410.16429)): Supports sorry-extraction where it finds all occurrences of sorry in a proof/definition and converts them to goals with their full context.

- **SorryDB** ([GitHub](https://github.com/SorryDB/SorryDB)): A dynamically-updating benchmark that scrapes sorry statements from 78+ real-world Lean formalization projects. It uses the Lean REPL to locate and analyze sorries, and provides template agents and a verifier. This infrastructure demonstrates that sorry extraction at scale is already working in practice.

**Assessment:** The core sorrifier algorithm (replace failing blocks with sorry, compile, extract subgoals) could be reimplemented using the leanprover-community REPL + `Lean.Meta.Sorry` API. The hardest part is the "error localization" step -- determining which specific proof blocks to replace with sorry when compilation fails. This requires heuristic or LLM-guided parsing of Lean error messages to identify the minimal failing region. A basic version could use line-level error locations from the compiler; a sophisticated version would need AST-level analysis. Estimated effort: a basic prototype in 1-2 weeks for someone familiar with Lean 4 metaprogramming; a robust version matching the paper's quality would take longer.

---

### 2. FormaRL: RL-Driven Autoformalization

**Paper overview:** FormaRL ([arXiv 2508.18914](https://arxiv.org/abs/2508.18914), August 2025) is a reinforcement learning framework for autoformalization -- translating natural language mathematics into Lean 4 formal statements -- that requires only a small amount of **unlabeled** data. It was authored by Huang, Jin, and collaborators.

**Core method -- Composite reward with GRPO:**

FormaRL's key innovation is its composite reward function used with GRPO (Group Relative Policy Optimization):

1. **Lean compiler syntax/type check (R_syntax):** Each candidate formalization is compiled in Lean 4. If it compiles without errors, it passes the syntax check. This is a binary signal -- the Lean compiler either accepts the output or rejects it. This checks syntactic correctness and type-level well-formedness.

2. **LLM-based consistency check (R_consistency):** A separate LLM is prompted to compare the original natural language problem against the formal Lean output. It evaluates whether the essence -- conditions, variables, conclusions -- matches faithfully. This addresses the semantic gap that syntax checking alone cannot catch (e.g., a formalization that compiles but states a different theorem).

3. **Composite reward:** The final reward combines both signals, ensuring that the formalizer produces outputs that are both formally valid (accepted by Lean) and semantically faithful (confirmed by LLM comparison).

**GRPO specifics:** FormaRL uses GRPO rather than PPO. GRPO estimates advantages using Monte Carlo rollouts rather than a learned critic model, and applies whitening (mean/variance normalization) to the advantage function. Statistics are estimated from a "group" of rollouts for each input query. This eliminates the need for a separate value network, simplifying training.

**ProofNet results:** FormaRL achieved dramatic improvements on the ProofNet benchmark: **pass@1 accuracy went from 4.04% to 26.15%** using Qwen2.5-Coder-7B-Instruct as the base model, a roughly **6.5x improvement**. On their custom uproof dataset (undergraduate-level math), they achieved 2.4% to 9.6% (pass@1) and 24.4% to 33.6% (pass@16). All of this was achieved with merely **859 unlabeled** mathematical problems -- no human-annotated formal/informal pairs were needed.

**Relation to sorry-based reward ideas:** FormaRL's approach is conceptually adjacent but distinct from a sorry-based reward:

- **FormaRL's compiler check** is a binary pass/fail on whether the entire formalization compiles. It does not use sorry for partial credit -- a formalization either fully compiles or it doesn't.
- **A sorry-based reward** would be more granular: insert sorry where the proof/formalization fails, count how many sorries remain, and use (1 - sorry_count/total_goals) as a partial reward signal. This gives credit for "almost correct" formalizations that get most of the structure right but fail on specific subgoals.
- **The key gap FormaRL does not address** is partial credit for partially correct formalizations. Their binary compiler check means a formalization that is 90% correct but has one type error gets the same reward (0) as a completely wrong formalization. A sorry-based reward would distinguish these cases, potentially enabling more effective RL training by providing richer gradient signal.
- **FormaRL's LLM consistency check** is orthogonal to sorry-based rewards and could be combined with them. You could have a three-part reward: (1) sorry-based partial compilation score, (2) LLM consistency score, and (3) full compilation bonus.

In summary, FormaRL validates the general paradigm of using compiler feedback + RL for autoformalization, and its impressive ProofNet results demonstrate the approach works. A sorry-based reward signal would be a natural extension that adds partial-credit granularity to their binary compiler reward, potentially enabling even stronger results.

---

Sources:
- [Mechanic: Sorrifier-Driven Formal Decomposition (arXiv)](https://arxiv.org/abs/2603.24465)
- [Mechanic paper HTML](https://arxiv.org/html/2603.24465)
- [SorryDB GitHub](https://github.com/SorryDB/SorryDB)
- [SorryDB paper](https://arxiv.org/html/2603.02668v1)
- [Lean.Meta.Sorry API](https://lean-lang.org/doc/api/Lean/Meta/Sorry.html)
- [leanprover-community REPL](https://github.com/leanprover-community/repl)
- [Lean 4 Metaprogramming Book - Tactics](https://leanprover-community.github.io/lean4-metaprogramming-book/main/09_tactics.html)
- [Lean 4 Metaprogramming Book - MetaM](https://leanprover-community.github.io/lean4-metaprogramming-book/main/04_metam.html)
- [Pantograph paper](https://arxiv.org/pdf/2410.16429)
- [FormaRL (arXiv)](https://arxiv.org/abs/2508.18914)
- [FormaRL PDF](https://arxiv.org/pdf/2508.18914)
- [FormaRL on EmergentMind](https://www.emergentmind.com/topics/formarl)
- [FormaRL OpenReview](https://openreview.net/forum?id=Z2El1U94bq)
- [Lean 4 Tactic Basic source](https://github.com/leanprover/lean4/blob/master/src/Lean/Elab/Tactic/Basic.lean)

agentId: a8d26970cbcbccc26 (use SendMessage with to: 'a8d26970cbcbccc26' to continue this agent)
&lt;usage>total_tokens: 25689
tool_uses: 18
duration_ms: 240304&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbad86c5-4892-436f-88b6-2b3487788fe8",
  "isSidechain": false,
  "promptId": "c8f8bb74-4b57-4255-9fe8-15c0a5831ab6",
  "type": "user",
  "uuid": "ed9f077e-5ca0-428f-b883-91e400896e1d",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to research two specific topics:\n\n1. **Mechanic's sorrifier implementation availability**: The reviewer flagged that Mechanic's sorrifier is NOT available as a modularized component (the paper states this is future work). I need to:\n   - Search for \"Mechanic sorrifier GitHub code implementation\" and \"Mechanic theorem proving sorry isolation code 2026\"\n   - Check if there's any open-source implementation\n   - Assess how hard it would be to reimplement from scratch based on the paper's description\n   - Look for alternative sorry-manipulation tools in the Lean ecosystem (e.g., does Lean 4's API natively support sorry insertion/extraction?)\n   - Search for \"Lean 4 sorry API metaprogramming\" and \"sorry extraction Lean 4\"\n\n2. **FormaRL** - A paper about using GRPO with composite reward for autoformalization. Search for:\n   - \"FormaRL autoformalization GRPO Lean 2025 2026\"\n   - How they combine Lean compiler type-checking with LLM-based consistency checking\n   - Their ProofNet results (4.04% → 26.15%)\n   - How this relates to our sorry-based reward idea\n\nReport detailed findings (300+ words per topic).",
    "agentId": "a8d26970cbcbccc26",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information on both topics. Let me compile the findings.\n\n---\n\n## Research Findings\n\n### 1. Mechanic's Sorrifier Implementation Availability\n\n**Paper and concept overview:** Mechanic (arXiv [2603.24465](https://arxiv.org/abs/2603.24465), March 2026) is an agent system that uses a \"sorrifier-driven formal decomposition\" strategy for automated theorem proving. The sorrifier works by repeatedly substituting incorrect/failing proof blocks with `sorry` placeholders until the full proof compiles in Lean 4. Once the proof compiles with sorries, each sorry is extracted as a self-contained subgoal with its local context, and an LLM independently resolves each subgoal. Once all subgoals are proven, they are reassembled into the original proof. This avoids both full regeneration from scratch and the excessive context of iterative repair.\n\n**Code availability: No open-source implementation exists.** My searches across GitHub and the broader web found zero code repositories for the Mechanic sorrifier. The paper itself explicitly states: *\"In future work, the sorrifier will be modularized as a standalone component integrated into the code agent.\"* This confirms the reviewer's flag -- the sorrifier is currently not available as a modularized, reusable component. It exists only as an internal part of the Mechanic agent described in the paper.\n\n**Feasibility of reimplementation:** Reimplementing a basic sorrifier from scratch is plausible, though non-trivial, because Lean 4 already provides significant native API support for sorry manipulation:\n\n- **`Lean.Meta.Sorry` module** ([API docs](https://lean-lang.org/doc/api/Lean/Meta/Sorry.html)): Provides core functions for creating and recognizing `sorryAx` terms. Key functions include constructing labeled sorries with source position metadata, and `forEachSorryM` which iterates over every sorry in an expression -- enabling programmatic discovery of all sorry locations.\n\n- **`Lean.Elab.admitGoal`** ([source](https://github.com/leanprover/lean4/blob/master/src/Lean/Elab/Tactic/Basic.lean)): Assigns `mvarId := sorry`, effectively inserting a sorry to close a tactic goal programmatically. Takes an `MVarId` and an optional `synthetic` flag.\n\n- **leanprover-community REPL** ([GitHub](https://github.com/leanprover-community/repl)): A REPL for Lean 4 that returns structured information about errors and sorries. When sorry appears in tactic mode, the response includes `proofState` identifiers for the goal at each sorry. The `CommandResponse` structure includes `env`, `messages`, `sorries`, and `tactics` fields, making it straightforward to extract sorry goals programmatically.\n\n- **Pantograph** ([arXiv 2410.16429](https://arxiv.org/pdf/2410.16429)): Supports sorry-extraction where it finds all occurrences of sorry in a proof/definition and converts them to goals with their full context.\n\n- **SorryDB** ([GitHub](https://github.com/SorryDB/SorryDB)): A dynamically-updating benchmark that scrapes sorry statements from 78+ real-world Lean formalization projects. It uses the Lean REPL to locate and analyze sorries, and provides template agents and a verifier. This infrastructure demonstrates that sorry extraction at scale is already working in practice.\n\n**Assessment:** The core sorrifier algorithm (replace failing blocks with sorry, compile, extract subgoals) could be reimplemented using the leanprover-community REPL + `Lean.Meta.Sorry` API. The hardest part is the \"error localization\" step -- determining which specific proof blocks to replace with sorry when compilation fails. This requires heuristic or LLM-guided parsing of Lean error messages to identify the minimal failing region. A basic version could use line-level error locations from the compiler; a sophisticated version would need AST-level analysis. Estimated effort: a basic prototype in 1-2 weeks for someone familiar with Lean 4 metaprogramming; a robust version matching the paper's quality would take longer.\n\n---\n\n### 2. FormaRL: RL-Driven Autoformalization\n\n**Paper overview:** FormaRL ([arXiv 2508.18914](https://arxiv.org/abs/2508.18914), August 2025) is a reinforcement learning framework for autoformalization -- translating natural language mathematics into Lean 4 formal statements -- that requires only a small amount of **unlabeled** data. It was authored by Huang, Jin, and collaborators.\n\n**Core method -- Composite reward with GRPO:**\n\nFormaRL's key innovation is its composite reward function used with GRPO (Group Relative Policy Optimization):\n\n1. **Lean compiler syntax/type check (R_syntax):** Each candidate formalization is compiled in Lean 4. If it compiles without errors, it passes the syntax check. This is a binary signal -- the Lean compiler either accepts the output or rejects it. This checks syntactic correctness and type-level well-formedness.\n\n2. **LLM-based consistency check (R_consistency):** A separate LLM is prompted to compare the original natural language problem against the formal Lean output. It evaluates whether the essence -- conditions, variables, conclusions -- matches faithfully. This addresses the semantic gap that syntax checking alone cannot catch (e.g., a formalization that compiles but states a different theorem).\n\n3. **Composite reward:** The final reward combines both signals, ensuring that the formalizer produces outputs that are both formally valid (accepted by Lean) and semantically faithful (confirmed by LLM comparison).\n\n**GRPO specifics:** FormaRL uses GRPO rather than PPO. GRPO estimates advantages using Monte Carlo rollouts rather than a learned critic model, and applies whitening (mean/variance normalization) to the advantage function. Statistics are estimated from a \"group\" of rollouts for each input query. This eliminates the need for a separate value network, simplifying training.\n\n**ProofNet results:** FormaRL achieved dramatic improvements on the ProofNet benchmark: **pass@1 accuracy went from 4.04% to 26.15%** using Qwen2.5-Coder-7B-Instruct as the base model, a roughly **6.5x improvement**. On their custom uproof dataset (undergraduate-level math), they achieved 2.4% to 9.6% (pass@1) and 24.4% to 33.6% (pass@16). All of this was achieved with merely **859 unlabeled** mathematical problems -- no human-annotated formal/informal pairs were needed.\n\n**Relation to sorry-based reward ideas:** FormaRL's approach is conceptually adjacent but distinct from a sorry-based reward:\n\n- **FormaRL's compiler check** is a binary pass/fail on whether the entire formalization compiles. It does not use sorry for partial credit -- a formalization either fully compiles or it doesn't.\n- **A sorry-based reward** would be more granular: insert sorry where the proof/formalization fails, count how many sorries remain, and use (1 - sorry_count/total_goals) as a partial reward signal. This gives credit for \"almost correct\" formalizations that get most of the structure right but fail on specific subgoals.\n- **The key gap FormaRL does not address** is partial credit for partially correct formalizations. Their binary compiler check means a formalization that is 90% correct but has one type error gets the same reward (0) as a completely wrong formalization. A sorry-based reward would distinguish these cases, potentially enabling more effective RL training by providing richer gradient signal.\n- **FormaRL's LLM consistency check** is orthogonal to sorry-based rewards and could be combined with them. You could have a three-part reward: (1) sorry-based partial compilation score, (2) LLM consistency score, and (3) full compilation bonus.\n\nIn summary, FormaRL validates the general paradigm of using compiler feedback + RL for autoformalization, and its impressive ProofNet results demonstrate the approach works. A sorry-based reward signal would be a natural extension that adds partial-credit granularity to their binary compiler reward, potentially enabling even stronger results.\n\n---\n\nSources:\n- [Mechanic: Sorrifier-Driven Formal Decomposition (arXiv)](https://arxiv.org/abs/2603.24465)\n- [Mechanic paper HTML](https://arxiv.org/html/2603.24465)\n- [SorryDB GitHub](https://github.com/SorryDB/SorryDB)\n- [SorryDB paper](https://arxiv.org/html/2603.02668v1)\n- [Lean.Meta.Sorry API](https://lean-lang.org/doc/api/Lean/Meta/Sorry.html)\n- [leanprover-community REPL](https://github.com/leanprover-community/repl)\n- [Lean 4 Metaprogramming Book - Tactics](https://leanprover-community.github.io/lean4-metaprogramming-book/main/09_tactics.html)\n- [Lean 4 Metaprogramming Book - MetaM](https://leanprover-community.github.io/lean4-metaprogramming-book/main/04_metam.html)\n- [Pantograph paper](https://arxiv.org/pdf/2410.16429)\n- [FormaRL (arXiv)](https://arxiv.org/abs/2508.18914)\n- [FormaRL PDF](https://arxiv.org/pdf/2508.18914)\n- [FormaRL on EmergentMind](https://www.emergentmind.com/topics/formarl)\n- [FormaRL OpenReview](https://openreview.net/forum?id=Z2El1U94bq)\n- [Lean 4 Tactic Basic source](https://github.com/leanprover/lean4/blob/master/src/Lean/Elab/Tactic/Basic.lean)"
      }
    ],
    "totalDurationMs": 240304,
    "totalTokens": 25689,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 22478,
      "output_tokens": 2409,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 801
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2409,
          "cache_read_input_tokens": 22478,
          "cache_creation_input_tokens": 801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 801,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 18
    }
  },
  "sourceToolAssistantUUID": "bbad86c5-4892-436f-88b6-2b3487788fe8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-27T18:18:39.279Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive research on all the key areas. Let me synthesize the findings and produce a deeply revised research idea. Let me think through the key issues:

## Key findings from research:

### 1. Autoformalization requirement (CRITICAL)
The reviewer's most critical concern: the idea must address autoformalization. Looking at the research:
- **Hilbert** bridges informal→formal using sorry-based decomposition at inference time
- **FormaRL** uses GRPO + compiler feedback for autoformalization training (4.04% → 26.15% on ProofNet)
- **DeepSeek-Prover-V2** generates informal chain-of-thought alongside Lean sketches with sorry


- The key insight: sorry-based RL rewards could train models to better translate informal proof sketches into formal proofs, extending Hilbert's inference-time approach into the training loop itself.

### 2. Missing references (now thoroughly researched)
- **Hilbert (ICLR 2026)**: Sorry-based recursive decomposition, inference-

only, achieves 99.2% on miniF2F and 70% on PutnamBench without RL training.
- **AlphaProof (Nature 2025)**: Uses min-over-subgoals reward with MCTS and RL, saturates miniF2F but doesn't employ sorry-based decomposition.
- **Proof-Verifier (ICLR 2026)**: Learned generative verifier that works on informal proofs and provides continuous reward scores.
- **VeRPO (arXiv Jan 2026)**: Applies weighted partial completion ratios for code RL with dynamic difficulty weighting.
- **FormaRL**: Combines GRPO with compiler and LLM consistency for autoformalization, showing 6.5x improvement on ProofNet.
- **Process-Verified RL (ICLR 2026)**: Tactic-level verification approach...

I'm clarifying the venue details—Process-Verified RL is confirmed for ICLR 2026, while ProD appeared at the NeurIPS 2024 MATH-AI Workshop rather than the main track. For the sorry-based decomposition approach, there's no existing open-source implementation, but Lean 4's native APIs and the SorryDB infrastructure demonstrate that reimplementing this would be feasible within a couple of weeks using available tools.

The benchmark landscape has shifted significantly—MiniF2F is essentially saturated across multiple systems (Hilbert at 99.2%, Prover at 99.6%, AlphaProof, and Aleph at 99.4% on PutnamBench), so I need to pivot toward fresher benchmarks like SorryDB, ProofNet, FormalProofBench, FATE, and PutnamBench.

On the novelty front, I'm distinguishing this work from SGVR by highlighting that while both use a verified subgoals ratio as a reward signal, the key differences lie in the verification mechanism (type-checker versus numeric matching), the domain (formal proofs versus informal geometry), and structural faithfulness (proof dependencies versus independent steps). The reviewer has a point that the core reward structure shares similarities, but the approach diverges meaningfully in execution. For Process-Verified RL, the distinction is that their method operates at the tactic level while this work targets a different granularity.

Given these considerations, I'm committing to a major revision that reframes the entire contribution. Instead of positioning this as just another formal prover, I'm repositioning it as a method for bridging informal mathematical reasoning to formal proofs through autoformalization. The insight is that Hilbert demonstrates sorry-decomposition works exceptionally well for informal-to-formal translation, FormaRL shows RL can dramatically improve autoformalization outcomes, but FormaRL relies on binary compiler rewards with no partial credit—this work fills that gap by providing dense, compiler-certified partial credit signals for autoformalization training. The new direction focuses on training models to translate informal proof sketches into formal Lean proofs using sorry-based rewards.

For benchmarks, I'm shifting to ProofNet as the primary focus since it directly targets autoformalization with unsaturated problems around 41.4% SOTA, keeping SorryDB for real-world validation, and dropping MiniF2F as primary. The differentiation becomes clearer: versus Hilbert, this applies RL rewards during training rather than inference search; versus FormaRL, it uses sorry-based partial credit instead of binary compilation signals; versus other approaches, it targets subgoal-level mathematical progress rather than tactic-level syntax or numeric matching.

For implementation, I'm planning to use Lean's REPL with Pantograph and the Lean.Meta.Sorry API to build a lightweight sorrifier—simpler than Mechanic's full agent and achievable in 2-3 weeks with existing tools.

The reviewer's suggestion about reframing toward autoformalization is hitting on something important: using SPR to train models that bridge informal proof sketches to formal proofs, which connects directly to Hilbert's paradigm and addresses the core challenge. is:
1. Hilbert uses informal reasoning (Gemini) to generate sorry-laden formal sketches, then fills in sorries
2. The sorry completion rate is a natural measure of how well the informal→formal translation worked
3. Training with SPR reward would teach models to produce formal sketches where MORE sorries get filled
4. This is autoformalization: the model learns to translate informal reasoning into better formal proof structures

So the reframing is: **SPR for Autoformalization-Guided Theorem Proving**

The model takes an informal proof sketch and produces a formal Lean proof. SPR rewards how much of the formal proof is compiler-verified, using sorry as the measurement mechanism.

Let me also think about the resource estimate. The new approach adds:
- Sorrifier reimplementation: 2-3 weeks
- FormaRL-style composite reward integration: 1 week
- The training is similar

Now I'm refining the framing further. The key insight is that by measuring sorry completion rates, I get dense, compiler-verified reward signals at the subgoal level—much richer than FormaRL's binary outcomes or Process-Verified RL's tactic-level feedback. The informal proof sketch becomes the input, and the model learns to translate it into formal Lean code where the compiler itself validates correctness. This bridges the gap between informal mathematical reasoning and formal verification in a way that's both mathematically meaningful and practically measurable. The sorrifier works by taking a proof attempt, iteratively replacing failing blocks with sorry statements, compiling to check what verifies, and extracting the fraction of the proof that's actually complete. For the reward signal, I'm using a basic sorry-progress metric (verified subgoals divided by total), but also exploring a weighted version that gives more credit for proving deeper subgoals since they're harder, plus a composite reward for autoformalization that combines sorry progress with semantic consistency checks and a bonus for full compilation. The training setup splits into two modes: one for formal proof generation where I reward progress on theorem-to-proof pairs, and another approach I'm still working through.

For evaluation, I'm targeting ProofNet for autoformalization benchmarks, SorryDB for real-world theorems with incomplete proofs, FormalProofBench for graduate-level problems, and PutnamBench for competition math—though I should note Aleph already hits 99.4% there. I'm leaning toward Goedel-Prover-V2-8B or Qwen2.5-Math-7B as the base model. One key decision I'm still weighing: whether to use the minimum across subgoals like AlphaProof does, or the mean instead—AlphaProof's approach makes sense when you need every subgoal solved, but mean gives smoother gradients for RL training, so I should probably ablate both.

Now I need to go through the references systematically and fix the venues and add the missing papers—Process-Verified RL goes to ICLR 2026, ProD to the NeurIPS 2024 MATH-AI Workshop, and I need to add Hilbert, AlphaProof, Proof-Verifier, VeRPO, and FormaRL while keeping the core references like Mechanic, SGVR, SorryDB, and FormalRewardBench.

I'm also reconsidering the Aleph claim about 99.4% on PutnamBench—it's from a commercial announcement in January 2026, not peer-reviewed, so I should be cautious. The PutnamBench leaderboard is public though, so I can verify it there. I'll stick with Hilbert's well-documented 70% and note that several systems have pushed higher rather than relying on unverified claims.

Since both MiniF2F and PutnamBench appear to be saturating, this actually strengthens the argument for harder benchmarks like SorryDB (which is continuously updated and can't saturate), ProofNet (only 41.4% SOTA), and FormalProofBench (33.5% SOTA).

For autoformalization specifically, ProofNet is the critical benchmark—FormaRL improved from 4.04% to 26.15% pass@1, so there's clear room for improvement with our approach.

I'm considering how to frame the title and core contribution. The key insight is that this work addresses two interconnected problems: the autoformalization quality gap (informal-to-formal translation is weak) and the reward sparsity problem in RL for theorem proving. The approach elegantly solves both by providing dense rewards for training while ensuring those rewards directly measure progress toward valid formal proofs.

Now I need to tackle the novelty concern head-on. The reviewer noted that SGVR already uses a similar skeleton_rate metric, so I need to clarify what fundamentally distinguishes this work. The critical differences are the verification mechanism—using Lean's type-checker for sound, error-free verification versus numeric answer matching—the domain shift from geometry to formal theorem proving with autoformalization, and the structural complexity where proof subgoals have dependencies rather than being independent computations.

Beyond that, I'm measuring the quality of informal-to-formal translation, which SGVR doesn't address, and exploring different aggregation strategies (min, mean, weighted) to understand what best captures proof difficulty. The sorry count naturally provides a curriculum signal that SGVR lacks. While the core formula is admittedly the same, the novelty really comes from applying it to autoformalization, leveraging compiler-certified verification, handling proof dependencies properly, designing composite rewards that track both sorry progress and semantic consistency, and studying difficulty-weighted variants inspired by VeRPO.

Now I'm ready to restructure the paper—shifting the title to emphasize the autoformalization angle, reframing the core problem around both autoformalization quality and reward sparsity, and highlighting how this differs fundamentally from prior work like Hilbert and FormaRL in terms of verification mechanisms and proof structure.

I need to decide between three training approaches: either training a formal prover on informal sketches with partial credit, training an autoformalization model on theorem statements, or combining both to handle the full informal-to-formal pipeline end-to-end.

Option A stands out as the most novel contribution — using sorry-based partial credit to train models on informal proof sketches directly, which neither Hilbert nor FormaRL have done before. The dense reward signal from SPR should help with this harder task.

For the paper, I'm framing this around autoformalization of mathematical proofs as the core challenge, with the key insight being that current approaches struggle because the translation is extremely difficult and sparse feedback makes training inefficient.

Now I'm working through the full proposal structure and resource estimates, accounting for the sorrifier implementation and adjusted GPU requirements for the autoformalization experiments.

For the base model, I'm weighing options between Goedel-Prover-V2-8B for its strong formal reasoning capabilities, versus more balanced models like Qwen2.5-Math or DeepSeek-Prover that might handle informal reasoning better. I think sticking with Goedel-Prover-V2-8B makes sense since it's the strongest open 8B prover available, and I can compensate for informal reasoning through the input format by including informal sketches as context.

Actually, for autoformalization specifically, I need a model that can handle both informal math and generate formal Lean code. FormaRL used Qwen2.5-Coder-7B-Instruct, so I could use that for a fair comparison. The most compelling approach would be running the autoformalization task with Qwen2.5-Coder-7B-Instruct and the theorem proving task with Goedel-Prover-V2-8B, then comparing SPR rewards against binary rewards on both to show the method's broader applicability.

I need to stop deliberating and actually start writing this. I should also check the AAAI 2027 deadline—it's July 21 or 28, 2026.

The timeline is tight with only about 8 weeks until AAAI, especially given the complexity of reimplementing the sorrifier and running autoformalization experiments. ICLR 2027 in October 2026 would be more realistic, but AAAI is still feasible if resources are available, so I'll keep both as targets.

Writing the full project JSON now... FormaRL showed that RL training can boost autoformalization performance significantly on ProofNet, but it's constrained by binary compiler rewards that miss partial progress signals. The Lean 4 ecosystem now has mature APIs for programmatic sorry insertion and subgoal extraction, creating an opening to combine sorry-verified partial-credit rewards with RL training — something no existing system does. SPR bridges this gap by providing compiler-certified dense feedback that measures exactly how much of an informal proof sketch translates to verified formal structure.

Looking at the broader landscape, current approaches each have limitations. Binary reward systems like DeepSeek-Prover-V2 and FormaRL achieve strong results but offer no credit for partially-correct formalizations. Tactic-level process rewards provide granular feedback but measure syntactic proof progress rather than mathematical progress on the original theorem. Learned verifiers like Proof-Verifier offer continuous reward scores and diagnostic feedback, though their 7% error rate introduces noise into the training signal.

Other domains have explored subgoal-level rewards with mixed results—SGVR uses verified subgoals for geometric reasoning and VeRPO uses test-passage ratios for code generation, both showing promise but relying on domain-specific or unsound verification methods. Meanwhile, inference-time approaches like Hilbert use sorry-driven recursive decomposition to achieve strong performance on miniF2F and PutnamBench.

What sets our approach apart is that we're combining compiler-certified verification with subgoal-level rewards that respect proof structure, unlike prior work that either verifies at the tactic level or treats subgoals independently. The sorry mechanism gives us a unique signal—the fraction of proof successfully autoformalized—that measures both translation quality and provides training feedback simultaneously.

We're building Sorry-Progress Reward (SPR) for GRPO-style RL training, drawing inspiration from how sorry-decomposition works at inference time but extending it to training. The system has four main components, starting with a lightweight sorrifier module that we'll implement from scratch using mature Lean libraries rather than relying on existing unmodularized implementations.

The sorrifier uses Pantograph for extracting sorrys with full context, the leanprover-community REPL for structured compilation feedback, and Lean's Meta.Sorry API to programmatically manipulate sorrys. When a proof attempt fails, it iteratively replaces failing blocks with sorry placeholders guided by Lean error locations, recompiles until type-checking succeeds, and extracts each sorry as a self-contained subgoal with its relevant hypotheses. This is more straightforward than existing approaches but still sufficient for computing rewards.

The SPR reward module then takes a model-generated proof attempt and decomposes it into subgoals with sorry placeholders, using the Lean compiler to type-check the structure and compute a base reward from the ratio of verified subgoals to total subgoals, plus a depth-weighted variant that accounts for proof complexity.

For training, I'm setting up two complementary tracks: one focused on proof autoformalization that takes an informal sketch and formal theorem statement and outputs a Lean proof, and another track that I'm still defining. The curriculum starts with easier problems where the model already resolves most subgoals, then gradually increases difficulty as performance improves—this self-calibrates naturally since harder problems have more subgoals to complete. I'm also planning several ablations to test different reward formulations, verification methods, curriculum strategies, and training configurations, plus different ways to aggregate subgoal performance. For resources, I'm estimating around 2500-3500 H100-hours total, including development time for the sorrifier and Lean integration plus the actual RL training across both tracks and ablation variants. Looking at the cost breakdown for the human-in-loop and auto-research approaches—the auto-research path requires more GPU hours and API costs due to parallel experiment orchestration and automated hyperparameter tuning, but the real constraint is Lean 4 compilation latency during RL rollouts, where each verification step adds overhead to the training loop.

For venues, I'm targeting ICLR 2027 as the primary submission since it gives the most time for full experimental validation, with AAAI and ICML as fallback options depending on how the timeline plays out.

Now I'm reviewing the key references that ground this work—recent papers on formal theorem proving with RL, verifiable rewards, and autoformalization that directly inform the approach. I'm looking at more papers on formal theorem proving and autoformalization, then reconsidering the project title—"Sorry-Progress Reward for Proof Autoformalization" feels a bit unwieldy, so I'm exploring shorter alternatives.

After weighing a few options, I'm settling on "Compiler-Certified Progress Rewards for Proof Autoformalization via Sorry-Driven Decomposition" since it keeps autoformalization central while making the technical approach clear. Now I need to write a concise description for the project, though I'm also thinking about feedback that the novelty over existing work might be thin.

Actually, the autoformalization framing does create meaningful differentiation—SGVR works with geometry and numeric subgoals without any formal proof component, while my approach uses compiler-verified subgoals specifically for translating informal proofs to formal ones, with fundamentally different verification mechanisms and proof dependencies that create novel composite rewards with semantic consistency checking.

For benchmarks, I'm moving away from MiniF2F since it's saturated, instead using ProofNet as the primary autoformalization benchmark where there's still significant room for improvement, SorryDB for real-world unsaturated data, FormalProofBench and PutnamBench for harder evaluation, and keeping MiniF2F only as a secondary reference point.

I should also note that Goedel-Prover-V2 was published at ICLR 2026, not just arXiv. With the stronger positioning around autoformalization, more comprehensive related work, better benchmark selection, clearer novelty differentiation, and the feasible sorrifier reimplementation path, this feels like it's moved from solid to solid-plus territory.

The core technical contribution—using sorry-based partial credit as an RL reward—is relatively straightforward, but the combination of being the first system to apply this to autoformalization, the compiler-certified versus learned reward distinction, the comprehensive ablation study of reward aggregation strategies, and the sorry-driven curriculum learning approach together make this a solid contribution. I'll stick with "solid" as the assessment, though it could push toward "strong" if the autoformalization results are particularly compelling.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed9f077e-5ca0-428f-b883-91e400896e1d",
  "isSidechain": false,
  "requestId": "req_011CbTXeHXXwSCJEvd5UJeM2",
  "type": "assistant",
  "uuid": "373f20c4-bb18-4ea2-bc12-26d1c0fd510f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMpk9qUTsfLEnmx8xHWysc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2880,
      "cache_read_input_tokens": 33173,
      "output_tokens": 9914,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2880,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9914,
          "cache_read_input_tokens": 33173,
          "cache_creation_input_tokens": 2880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2880
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-27T18:18:39.418Z_

Now let me synthesize all research findings into a comprehensive revised idea. Let me think through the key insights carefully before writing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "373f20c4-bb18-4ea2-bc12-26d1c0fd510f",
  "isSidechain": false,
  "requestId": "req_011CbTXeHXXwSCJEvd5UJeM2",
  "type": "assistant",
  "uuid": "e4bea615-89aa-47a5-ad1f-c9c5c62338dc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMpk9qUTsfLEnmx8xHWysc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2880,
      "cache_read_input_tokens": 33173,
      "output_tokens": 9914,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2880,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9914,
          "cache_read_input_tokens": 33173,
          "cache_creation_input_tokens": 2880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2880
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-27T18:18:45.518Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01T4szAeeUYMpDqMXEgi85HV`</summary>

```json
{
  "description": "Verify latest benchmark SOTA details",
  "prompt": "I need to verify a few specific claims from my research before finalizing a revised research idea. Please search for and verify:\n\n1. **ProofNet SOTA**: Search \"ProofNet benchmark theorem proving SOTA 2026\" — is the current SOTA really ~41.4% (BFS-Prover-V2)?\n2. **Goedel-Prover-V2 venue**: Search \"Goedel-Prover-V2 ICLR 2026\" — was it published at ICLR 2026 or just arXiv?\n3. **Aleph PutnamBench 99.4%**: Search \"Aleph Logical Intelligence PutnamBench\" — is this claim real? What's the actual PutnamBench SOTA?\n4. **FormaRL venue**: Search \"FormaRL autoformalization venue\" — was this published at any conference or just arXiv?\n5. **Pantograph sorry extraction**: Search \"Pantograph Lean 4 sorry extraction\" — confirm this tool supports sorry-to-goal extraction\n\nReport brief findings (100 words each).",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4bea615-89aa-47a5-ad1f-c9c5c62338dc",
  "isSidechain": false,
  "requestId": "req_011CbTXeHXXwSCJEvd5UJeM2",
  "type": "assistant",
  "uuid": "d646063b-c3fb-4a97-8bda-eab119d46cb6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMpk9qUTsfLEnmx8xHWysc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2880,
      "cache_read_input_tokens": 33173,
      "output_tokens": 9914,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2880,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9914,
          "cache_read_input_tokens": 33173,
          "cache_creation_input_tokens": 2880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2880
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Verifier-Certified Progress Rewards via Sorry-Driven Decomposition\",…",
  "leafUuid": "d646063b-c3fb-4a97-8bda-eab119d46cb6",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise sorry-progress reward to address autoformalization gap",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02"
}
```

---

### Tool result

_source line 33 · 2026-05-27T18:19:47.974Z_

<details><summary>↩ Tool result · `toolu_01T4szAeeUYMpDqMXEgi85HV`</summary>

```text
Here are the findings for each claim:

---

**1. ProofNet SOTA -- BFS-Prover-V2 at ~41.4%: CONFIRMED**

BFS-Prover-V2 (ByteDance) achieves 41.4% on the ProofNet validation/test set, which is the current state-of-the-art. It also achieves 95.08% on miniF2F-test. The system uses multi-stage expert iteration with adaptive tactic-level data filtering at training time, and planner-enhanced multi-agent tree search at inference time. The paper is available on OpenReview and the model is open-source on Hugging Face.

Sources:
- [BFS-Prover-V2 on Emergent Mind](https://www.emergentmind.com/topics/bfs-prover-v2)
- [BFS-Prover-V2 on OpenReview](https://openreview.net/pdf/28f1ecf5ea53fbeae0fabf505fffa07d27abed83.pdf)
- [BFS-Prover-V2 on Hugging Face](https://huggingface.co/ByteDance-Seed/BFS-Prover-V2-32B)

---

**2. Goedel-Prover-V2 venue -- ICLR 2026: CONFIRMED**

Goedel-Prover-V2 was published as a conference paper at ICLR 2026. It was presented as a poster on Thursday, April 23, 2026. The arXiv PDF itself states "Published as a conference paper at ICLR 2026." It is not merely an arXiv preprint -- it has a full ICLR acceptance. Your claim is accurate.

Sources:
- [ICLR 2026 Virtual Poster](https://iclr.cc/virtual/2026/poster/10007912)
- [OpenReview page](https://openreview.net/forum?id=j4C0nALrgK)
- [arXiv (stating ICLR 2026)](https://arxiv.org/pdf/2509.22819)

---

**3. Aleph PutnamBench 99.4%: CONFIRMED**

Logical Intelligence's Aleph agent scored 668/672 (99.4%) on PutnamBench, which consists of 672 formally stated problems from 50+ years of the William Lowell Putnam Mathematical Competition. Aleph is #1 on the PutnamBench leaderboard, ahead of ByteDance and Apple. This is a dramatic jump from less than 2% SOTA as recently as mid-2025. The system is powered by GPT-5.2 and uses a language-free, mathematically grounded approach. The claim is real and well-documented through official press releases and the company's own blog.

Sources:
- [Logical Intelligence blog post](https://logicalintelligence.com/blog/aleph-solves-putnambench)
- [Yahoo Finance coverage](https://finance.yahoo.com/sectors/technology/articles/logical-intelligence-tops-leading-ai-153000376.html)
- [BusinessWire press release](https://www.businesswire.com/news/home/20251202089385/en/Logical-Intelligence-Achieves-76-Percent-on-Putnam-Benchmark-Highlighting-Shift-Beyond-Large-Language-Models-to-Language-free-Mathematically-Grounded-Models)

---

**4. FormaRL venue: UNDER REVIEW (not yet published at a conference)**

FormaRL (arXiv 2508.18914, August 2025) appears to be under review at COLM 2026 based on its OpenReview submission page. It has not yet been published as a conference paper. If your research draft cites it as a published venue paper, that should be corrected -- it is currently an arXiv preprint under review. The paper proposes using GRPO-based RL with syntax and consistency rewards for autoformalization, achieving 4-6x improvements on ProofNet pass@1 with Qwen2.5-Coder-7B.

Sources:
- [arXiv page](https://arxiv.org/abs/2508.18914)
- [OpenReview submission](https://openreview.net/forum?id=Z2El1U94bq)
- [Semantic Scholar](https://www.semanticscholar.org/paper/FormaRL:-Enhancing-Autoformalization-with-no-Data-Huang-Jin/b430d8ac9cf1236314a1273dc7e8fb9769ebae70)

---

**5. Pantograph sorry-to-goal extraction: CONFIRMED**

Pantograph explicitly supports "sorry extraction" -- it finds all occurrences of `sorry` in a Lean 4 proof or definition and converts them into goals. This is a core feature designed for ML agents implementing the "Draft-Sketch-Prove" paradigm: an LLM outputs a proof skeleton with `sorry` placeholders, Pantograph extracts the corresponding goals, and a proof search tool fills them in. The tool was published at TACAS (part of Springer LNCS) and has an open-source Python binding (PyPantograph) from Stanford.

Sources:
- [Pantograph paper (Springer)](https://link.springer.com/chapter/10.1007/978-3-031-90643-5_6)
- [arXiv version](https://arxiv.org/abs/2410.16429)
- [PyPantograph on GitHub](https://github.com/stanford-centaur/PyPantograph)

agentId: af8ca305ec442763b (use SendMessage with to: 'af8ca305ec442763b' to continue this agent)
&lt;usage>total_tokens: 16037
tool_uses: 7
duration_ms: 62450&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d646063b-c3fb-4a97-8bda-eab119d46cb6",
  "isSidechain": false,
  "promptId": "c8f8bb74-4b57-4255-9fe8-15c0a5831ab6",
  "type": "user",
  "uuid": "85827a40-2481-4cd0-9981-1438a6ad3e09",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify a few specific claims from my research before finalizing a revised research idea. Please search for and verify:\n\n1. **ProofNet SOTA**: Search \"ProofNet benchmark theorem proving SOTA 2026\" — is the current SOTA really ~41.4% (BFS-Prover-V2)?\n2. **Goedel-Prover-V2 venue**: Search \"Goedel-Prover-V2 ICLR 2026\" — was it published at ICLR 2026 or just arXiv?\n3. **Aleph PutnamBench 99.4%**: Search \"Aleph Logical Intelligence PutnamBench\" — is this claim real? What's the actual PutnamBench SOTA?\n4. **FormaRL venue**: Search \"FormaRL autoformalization venue\" — was this published at any conference or just arXiv?\n5. **Pantograph sorry extraction**: Search \"Pantograph Lean 4 sorry extraction\" — confirm this tool supports sorry-to-goal extraction\n\nReport brief findings (100 words each).",
    "agentId": "af8ca305ec442763b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the findings for each claim:\n\n---\n\n**1. ProofNet SOTA -- BFS-Prover-V2 at ~41.4%: CONFIRMED**\n\nBFS-Prover-V2 (ByteDance) achieves 41.4% on the ProofNet validation/test set, which is the current state-of-the-art. It also achieves 95.08% on miniF2F-test. The system uses multi-stage expert iteration with adaptive tactic-level data filtering at training time, and planner-enhanced multi-agent tree search at inference time. The paper is available on OpenReview and the model is open-source on Hugging Face.\n\nSources:\n- [BFS-Prover-V2 on Emergent Mind](https://www.emergentmind.com/topics/bfs-prover-v2)\n- [BFS-Prover-V2 on OpenReview](https://openreview.net/pdf/28f1ecf5ea53fbeae0fabf505fffa07d27abed83.pdf)\n- [BFS-Prover-V2 on Hugging Face](https://huggingface.co/ByteDance-Seed/BFS-Prover-V2-32B)\n\n---\n\n**2. Goedel-Prover-V2 venue -- ICLR 2026: CONFIRMED**\n\nGoedel-Prover-V2 was published as a conference paper at ICLR 2026. It was presented as a poster on Thursday, April 23, 2026. The arXiv PDF itself states \"Published as a conference paper at ICLR 2026.\" It is not merely an arXiv preprint -- it has a full ICLR acceptance. Your claim is accurate.\n\nSources:\n- [ICLR 2026 Virtual Poster](https://iclr.cc/virtual/2026/poster/10007912)\n- [OpenReview page](https://openreview.net/forum?id=j4C0nALrgK)\n- [arXiv (stating ICLR 2026)](https://arxiv.org/pdf/2509.22819)\n\n---\n\n**3. Aleph PutnamBench 99.4%: CONFIRMED**\n\nLogical Intelligence's Aleph agent scored 668/672 (99.4%) on PutnamBench, which consists of 672 formally stated problems from 50+ years of the William Lowell Putnam Mathematical Competition. Aleph is #1 on the PutnamBench leaderboard, ahead of ByteDance and Apple. This is a dramatic jump from less than 2% SOTA as recently as mid-2025. The system is powered by GPT-5.2 and uses a language-free, mathematically grounded approach. The claim is real and well-documented through official press releases and the company's own blog.\n\nSources:\n- [Logical Intelligence blog post](https://logicalintelligence.com/blog/aleph-solves-putnambench)\n- [Yahoo Finance coverage](https://finance.yahoo.com/sectors/technology/articles/logical-intelligence-tops-leading-ai-153000376.html)\n- [BusinessWire press release](https://www.businesswire.com/news/home/20251202089385/en/Logical-Intelligence-Achieves-76-Percent-on-Putnam-Benchmark-Highlighting-Shift-Beyond-Large-Language-Models-to-Language-free-Mathematically-Grounded-Models)\n\n---\n\n**4. FormaRL venue: UNDER REVIEW (not yet published at a conference)**\n\nFormaRL (arXiv 2508.18914, August 2025) appears to be under review at COLM 2026 based on its OpenReview submission page. It has not yet been published as a conference paper. If your research draft cites it as a published venue paper, that should be corrected -- it is currently an arXiv preprint under review. The paper proposes using GRPO-based RL with syntax and consistency rewards for autoformalization, achieving 4-6x improvements on ProofNet pass@1 with Qwen2.5-Coder-7B.\n\nSources:\n- [arXiv page](https://arxiv.org/abs/2508.18914)\n- [OpenReview submission](https://openreview.net/forum?id=Z2El1U94bq)\n- [Semantic Scholar](https://www.semanticscholar.org/paper/FormaRL:-Enhancing-Autoformalization-with-no-Data-Huang-Jin/b430d8ac9cf1236314a1273dc7e8fb9769ebae70)\n\n---\n\n**5. Pantograph sorry-to-goal extraction: CONFIRMED**\n\nPantograph explicitly supports \"sorry extraction\" -- it finds all occurrences of `sorry` in a Lean 4 proof or definition and converts them into goals. This is a core feature designed for ML agents implementing the \"Draft-Sketch-Prove\" paradigm: an LLM outputs a proof skeleton with `sorry` placeholders, Pantograph extracts the corresponding goals, and a proof search tool fills them in. The tool was published at TACAS (part of Springer LNCS) and has an open-source Python binding (PyPantograph) from Stanford.\n\nSources:\n- [Pantograph paper (Springer)](https://link.springer.com/chapter/10.1007/978-3-031-90643-5_6)\n- [arXiv version](https://arxiv.org/abs/2410.16429)\n- [PyPantograph on GitHub](https://github.com/stanford-centaur/PyPantograph)"
      }
    ],
    "totalDurationMs": 62450,
    "totalTokens": 16037,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 821,
      "cache_read_input_tokens": 13842,
      "output_tokens": 1373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 821
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1373,
          "cache_read_input_tokens": 13842,
          "cache_creation_input_tokens": 821,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 821,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 7
    }
  },
  "sourceToolAssistantUUID": "d646063b-c3fb-4a97-8bda-eab119d46cb6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34 · 2026-05-27T18:19:47.987Z_

```json
{
  "parentUuid": "85827a40-2481-4cd0-9981-1438a6ad3e09",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "93d56fe2-de90-4cec-8d53-76e3e8beb3bb",
  "timestamp": "2026-05-27T18:19:47.987Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 35 · 2026-05-27T18:20:04.225Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the research I need. Let me synthesize everything and write the complete revised JSON. Let me carefully address each reviewer concern:

1. **CRITICAL: Autoformalization** → Reframed around autoformalization (informal→formal proof translation)
2. **Process-Verified RL venue** → Fixed to ICLR 2026
3. **ProD venue** → Fixed to NeurIPS 2024 MATH-AI Workshop
4. **Hilbert** → Added as key related work, positioned as inference-only (we add training)
5. **AlphaProof** → Added, min-over-subgoals reward design discussed


6. **Proof-Verifier** → Added, positioned as learned (93% accuracy) vs our exact (100%)
7. **VeRPO** → Added, difficulty-weighted partial completion inspires our weighted SPR
8. **Sorrifier availability** → Reimplementation plan using Pantograph + REPL + Lean.Meta.Sorry
9. **SGVR novelty** → Strengthened differentiation via autoformalization angle + compiler verification + proof dependencies
10. **MiniF2F saturation** → Replaced with ProofNet, SorryDB, FormalProofBench as primary benchmarks

This is a major revision with the same core mechanism but significantly strengthened positioning and related work coverage.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93d56fe2-de90-4cec-8d53-76e3e8beb3bb",
  "isSidechain": false,
  "requestId": "req_011CbTY26sSzBQkA1gpLGvrf",
  "type": "assistant",
  "uuid": "60c3f44a-2a23-4604-9712-ee9cd1ca7675",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QV2m9X824Lj9yBZaZbwk8P",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11460,
      "cache_read_input_tokens": 36053,
      "output_tokens": 7019,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11460,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 7019,
          "cache_read_input_tokens": 36053,
          "cache_creation_input_tokens": 11460,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11460
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-27T18:22:42.243Z_

Now I have comprehensive research findings on all reviewer concerns. Let me synthesize everything and produce the complete revised idea.

**Research synthesis summary:**

1. **Hilbert (ICLR 2026)**: Inference-only sorry-based recursive decomposition, 99.2% miniF2F, 70% PutnamBench. No RL training. Explicitly flags training on its own traces as future work. Code available (Apple GitHub).

2. **AlphaProof (Nature 2025)**: Uses min-over-subgoals return (bottleneck signal) in AND-OR MCTS with RL. Saturated miniF2F. Reward is -1/tactic (incentivize short proofs). No sorry-based decomposition.

3. **Proof-Verifier (ICLR 2026)**: Learned generative verifier, 93% accuracy, provides continuous reward + diagnostic feedback. Works on informal proofs. Complements but doesn't replace compiler verification.

4. **VeRPO (arXiv Jan 2026)**: Difficulty-weighted partial test-passage ratio for code RL. Dynamic weights via inverse pass-rate + KDE normalization. +3.13% average, +8.83% on hardest benchmark. Directly analogous to our weighted SPR.

5. **FormaRL (arXiv 2025, under review)**: GRPO + binary compiler + LLM consistency for autoformalization. 4.04%→26.15% on ProofNet. No partial credit via sorry.

6. **Process-Verified RL**: Confirmed ICLR 2026 (not NeurIPS 2025). Tactic-level process reward.

7. **SGVR**: skeleton_rate = verified_subgoals/total_subgoals for geometry. Numeric sub-goal matching, not compiler verification.

8. **Sorrifier**: No open-source code. But Pantograph (TACAS, Stanford) confirms sorry-to-goal extraction. Lean REPL provides structured sorry info. Reimplementation feasible in 2-3 weeks.

9. **Benchmarks**: MiniF2F saturated (99.2%+). PutnamBench near-saturated (Aleph 99.4%). ProofNet unsaturated (SOTA 41.4%). SorryDB dynamic. FormalProofBench hard (SOTA 33.5%).

Here is the complete revised idea:

```json
{
  "title": "Compiler-Certified Progress Rewards for Proof Autoformalization via Sorry-Driven Decomposition",
  "change_type": "major",

  "core_problem": "Autoformalization of mathematical proofs — translating informal human reasoning into compiler-verified formal proofs in Lean 4 — remains a major open challenge (ProofNet SOTA ~41%, FormalProofBench ~34%). RL training for this task compounds the difficulty: binary compilation reward (the full proof compiles or not) provides zero gradient signal for partial progress, creating severe reward sparsity precisely on the hard problems where autoformalization matters most. Can we leverage Lean 4's sorry mechanism to provide exact, dense measurements of how much informal reasoning successfully transfers to verified formal structure?",

  "opportunity": "Three recent advances create a convergent opportunity that no existing system exploits. First, Hilbert (ICLR 2026) demonstrated that sorry-based recursive decomposition brilliantly bridges informal reasoning to formal proofs at inference time — achieving 99.2% on miniF2F and 70% on PutnamBench — but it orchestrates frozen pretrained models and never trains for this capability; its authors explicitly flag training on generated traces as future work. Second, FormaRL (2025) showed that GRPO-based RL training can improve autoformalization 6.5× on ProofNet (4.04% → 26.15%), but relies on binary compiler reward that treats a 90%-correct formalization the same as a completely wrong one. Third, the Lean 4 ecosystem now provides mature sorry-manipulation infrastructure — Pantograph's sorry-to-goal extraction (TACAS), the leanprover-community REPL's structured sorry reporting, and the Lean.Meta.Sorry API — enabling reliable programmatic sorry insertion and subgoal extraction at scale. The gap: no system combines sorry-verified partial-credit rewards with RL training for proof autoformalization. SPR fills this gap — providing compiler-certified dense feedback that measures exactly how much of an informal proof sketch successfully translates to verified formal structure, without any learned approximation error.",

  "landscape": "Current approaches to RL for theorem proving and autoformalization span several paradigms, each with distinct limitations that SPR addresses:\n\n**Binary reward systems.** DeepSeek-Prover-V2 uses GRPO with binary verification plus consistency bonus. Goedel-Prover-V2 (ICLR 2026) and Kimina-Prover similarly use binary Lean compilation reward. FormaRL applies GRPO with binary compiler check + LLM semantic consistency for autoformalization, achieving 6.5× improvement on ProofNet but offering zero partial credit for partially-correct formalizations — a formalization that correctly captures 90% of the proof structure receives the same reward (0) as a completely wrong one.\n\n**Tactic-level process rewards.** Process-Verified RL (Kim & Yun, ICLR 2026) uses Lean's tactic-level elaboration as a process reward oracle, providing dense credit at individual tactic granularity with first-error propagation. While exact and sound, tactic-level credit measures syntactic proof progress (did this tactic type-check?) rather than mathematical progress on the original theorem — a proof may execute many valid tactics without making meaningful mathematical headway on the problem.\n\n**Learned verifiers.** Proof-Verifier (Fan et al., ICLR 2026) trains a generative verifier achieving 93% verification accuracy with continuous reward scores and diagnostic feedback for theorem proving RLVR. While it handles informal proofs and provides rich signal, its 7% error rate introduces reward noise that can mislead RL training on edge cases, and training the verifier itself requires expensive formal-to-informal data generation.\n\n**Subgoal-level rewards in adjacent domains.** SGVR (Chen et al., 2026) implements skeleton_rate = verified_subgoals/total_subgoals as GRPO reward for geometric reasoning, achieving +9.7% on geometry benchmarks. VeRPO (Wang et al., 2026) uses difficulty-weighted partial test-passage ratios for code generation RL, achieving +8.83% on the hardest coding benchmark with dynamic weight recalibration. Both validate subgoal-level dense reward, but SGVR verifies by numeric answer matching (approximate, geometry-specific), and VeRPO verifies via test execution (empirical, not sound).\n\n**Sorry-based decomposition at inference time.** Hilbert (Varambally et al., ICLR 2026) achieves SOTA by recursively decomposing proofs via sorry-laden sketches generated from informal reasoning, then filling each sorry independently — but purely at inference with frozen models. Mechanic (2026) implements a sorrifier for fault isolation in failed proofs. AlphaProof (Hubert et al., Nature 2025) uses min-over-subgoals return in AND-OR MCTS tree search with RL, but does not employ sorry-based decomposition. SorryDB (2026) curates sorry-bearing theorems from 78 real Lean projects, providing a natural evaluation testbed.\n\n**SPR's unique position.** We combine: (1) compiler-certified verification — exact with zero model error, unlike Proof-Verifier's 93% accuracy; (2) subgoal-level mathematical meaningfulness — measuring progress on the original theorem, unlike Process-Verified RL's tactic-level syntactic signal; (3) structural faithfulness respecting proof dependencies — unlike SGVR's independent numeric sub-goals, later sorry-goals may depend on earlier ones; (4) application to autoformalization — the sorry-completion ratio directly measures how much informal reasoning successfully formalized, unlike pure proof generation; and (5) difficulty-aware weighting inspired by VeRPO and aggregation strategies from AlphaProof (min-over-subgoals for bottleneck identification).",

  "inspired_by": "Hilbert's inference-time sorry-decomposition paradigm (extend from inference to training time) + FormaRL's RL-for-autoformalization approach (add sorry-based partial credit to binary reward) + VeRPO's difficulty-weighted partial completion ratios (adapt from code tests to proof subgoals) + AlphaProof's min-over-subgoals aggregation (bottleneck-aware reward design) + SGVR's skeleton_rate formulation (generalize from numeric geometry to compiler-verified formal proofs) + Pantograph/REPL infrastructure (enabling practical sorrifier construction)",

  "approach": "We implement Sorry-Progress Reward (SPR), a dense RL reward signal for training proof autoformalization models that uses Lean 4's sorry mechanism to provide exact, compiler-certified measurements of partial proof progress. The system has four components:\n\n**1. Lightweight Sorrifier Module (weeks 1-3).** Rather than depending on Mechanic's unmodularized sorrifier (the paper explicitly states modularization is future work), we build our own using mature Lean 4 infrastructure: Pantograph (TACAS) for sorry-to-goal extraction with full hypothesis context, the leanprover-community REPL for structured compilation feedback (returns sorries with proof states), and Lean.Meta.Sorry API for programmatic sorry manipulation. Given a failed proof attempt, our sorrifier: (a) identifies failing blocks via Lean error locations, (b) iteratively replaces minimal failing regions with sorry, (c) recompiles until the overall structure type-checks, and (d) extracts each sorry as a self-contained subgoal. This is narrower in scope than Mechanic's full agent workflow but sufficient and robust for reward computation.\n\n**2. SPR Reward Variants (weeks 3-4).** Given a model-generated proof attempt (potentially guided by an informal proof sketch), the sorrifier decomposes it into k subgoals with sorry placeholders. The Lean 4 compiler type-checks the structure, yielding multiple reward formulations we ablate:\n- Base SPR: R_base = verified_subgoals / total_subgoals ∈ [0,1]\n- Depth-Weighted SPR: R_depth = Σ(d_i · v_i) / Σ(d_i), weighting subgoals by proof-tree depth (deeper = harder = more weight), inspired by VeRPO's difficulty weighting\n- Pass-Rate-Weighted SPR: R_pr = Σ(w_i · v_i) / Σ(w_i), with w_i = exp(-α · ρ_i) where ρ_i is the empirical pass rate of subgoal i across the rollout group, directly adapting VeRPO's dynamic difficulty estimation to proof subgoals\n- Min-SPR: R_min = min(v_i) across all subgoals (AlphaProof-inspired bottleneck signal, capturing that the hardest subgoal determines proof difficulty)\n- Composite Autoformalization Reward: R_auto = α·R_spr + β·R_consistency + γ·R_full, where R_consistency is an LLM semantic faithfulness check measuring whether the formal proof captures the intent of the informal sketch (following FormaRL), and R_full is a binary full-compilation bonus anchoring to end-to-end correctness\n\n**3. Two-Track RL Training (weeks 4-9).** We train on two complementary tasks using GRPO via the Kimina-Prover-RL/Verl pipeline:\n- Track A — Proof Autoformalization: Input = informal proof sketch + formal theorem statement → Output = formal Lean 4 proof. Base model: Qwen2.5-Coder-7B-Instruct (FormaRL's baseline for fair comparison). Reward: R_auto. Training data: ProofNet (371 undergraduate math theorems with informal/formal pairs) + Mathlib docstring-theorem pairs + synthetically generated informal sketches via informalization (formal→informal is high-quality per the autoformalization survey).\n- Track B — Formal Proof Generation: Input = formal theorem statement → Output = formal Lean 4 proof. Base model: Goedel-Prover-V2-8B (strongest open 8B prover, 84.6% pass@32 on miniF2F). Reward: R_base, R_depth, or R_pr. Training data: SorryDB theorems + PutnamBench + ProofNet formal statements.\nTrack B serves as a controlled comparison isolating SPR's impact on pure proof generation without the autoformalization variable.\n\n**4. Sorry-Driven Curriculum (concurrent with training).** We implement curriculum scheduling based on sorry-completion statistics from the base model's initial rollouts: start training on problems where the base model resolves >60% of subgoals (warm zone), gradually decrease the threshold as the model improves. This is naturally calibrated — harder problems decompose into more subgoals, and the sorry-completion rate directly measures the model's readiness for each difficulty tier. This extends SGVR's insight that sub-goal progress enables curriculum design, but uses compiler-verified rather than numeric-match calibration.\n\n**Key Ablations:** (1) R_base vs R_depth vs R_pr vs R_min vs R_auto vs binary reward; (2) SPR vs Process-Verified RL tactic-level reward vs Proof-Verifier learned reward; (3) with vs without sorry-driven curriculum; (4) Track A (autoformalization) vs Track B (proof generation) vs joint training; (5) subgoal aggregation: mean vs min vs difficulty-weighted; (6) composite reward coefficient sensitivity (α, β, γ).\n\n**Evaluation.** Primary benchmarks: ProofNet (autoformalization, SOTA 41.4%, ample headroom), SorryDB (real-world sorry-bearing theorems, dynamic/unsaturated). Secondary benchmarks: FormalProofBench (graduate-level, SOTA ~34%), PutnamBench. MiniF2F is used only as a sanity check given saturation (Hilbert 99.2%, Seed-Prover 99.6%). Key metrics: pass@1 and pass@32 on all benchmarks; sample efficiency curves on hard problems (where binary reward yields near-zero signal); sorry-completion rate progression during training; degenerate-group ratio (fraction of GRPO groups with zero advantage, following VeRPO's analysis).",

  "resource_estimate": {
    "manual": {
      "gpu_hours": "2500-3500 H100-hours (sorrifier dev/debug on GPU: 500h; Track A training 4 reward ablations × ~350h: 1400h; Track B training 3 ablations × ~350h: 1050h; evaluation sweeps: 300h)",
      "timeline": "12-14 weeks (3 weeks sorrifier reimplementation using Pantograph + REPL, 1 week SPR reward module integration, 2 weeks RL infra setup + data preparation with informal sketch synthesis, 4-5 weeks training + ablations across both tracks, 2-3 weeks evaluation on ProofNet/SorryDB/FormalProofBench + paper writing)",
      "estimated_gpu_cost": "$6,250-$8,750 (at $2.50/H100-hour spot pricing, May 2026 market rate)"
    },
    "human_in_loop": {
      "gpu_hours": "2500-3000 H100-hours (same training budget, reduced sorrifier debugging via Claude-assisted Lean 4 metaprogramming)",
      "timeline": "9-11 weeks (Claude accelerates Pantograph/REPL-based sorrifier implementation and GRPO reward integration by ~35%; automates informal sketch synthesis pipeline)",
      "claude_api_cost": "$400-600 (sorrifier implementation assistance, Lean 4 metaprogramming, experiment analysis, paper drafting)",
      "estimated_gpu_cost": "$6,250-$7,500"
    },
    "auto_research": {
      "gpu_hours": "3000-4000 H100-hours (additional automated hyperparameter search over reward coefficients α/β/γ, curriculum threshold sweep, aggregation strategy exploration)",
      "timeline": "7-9 weeks (parallel experiment orchestration across both tracks, automated evaluation pipeline on all benchmarks)",
      "claude_api_cost": "$700-1000 (code generation, experiment orchestration, automated evaluation analysis, paper drafting)",
      "estimated_gpu_cost": "$7,500-$10,000",
      "speed_bottleneck": "Lean 4 compilation latency (~2-5s per sorry-verification call) during RL rollouts; each GRPO group of 8-16 samples requires Lean type-checking via the sorrifier, creating a verification throughput ceiling of ~300-700 verifications/GPU-hour. Mitigations: (a) batch sorry-verification across rollout groups using Pantograph's async API, (b) cache sorrifier results for structurally identical proof attempts, (c) pre-filter obviously broken proofs via fast syntax check before full sorrification."
    }
  },

  "target_venues": [
    "ICLR 2027 (predicted ~October 2026 based on ICLR 2026 September 24 pattern — primary target, allows full experimental validation across both tracks)",
    "AAAI 2027 (abstract: July 21, 2026; full paper: July 28, 2026 — stretch target feasible only with human-in-loop timeline and prioritizing Track A results)",
    "ICML 2027 (predicted ~January 2027 — fallback with maximum ablation coverage)"
  ],

  "level": "solid",

  "key_references": [
    "Hilbert: Recursively Building Formal Proofs with Informal Reasoning (Varambally et al., ICLR 2026)",
    "Olympiad-Level Formal Mathematical Reasoning with Reinforcement Learning [AlphaProof] (Hubert et al., Nature 2025)",
    "Proof-Verifier: Enabling Reinforcement Learning from Verifiable Rewards for Mathematical Theorem Proving (Fan et al., ICLR 2026)",
    "Process-Verified Reinforcement Learning for Theorem Proving via Lean (Kim & Yun, ICLR 2026)",
    "VeRPO: Verifiable Dense Reward Policy Optimization for Code Generation (Wang et al., arXiv 2026)",
    "Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward [SGVR] (Chen et al., arXiv 2026)",
    "FormaRL: Enhancing Autoformalization with No Labeled Data (Huang & Jin et al., arXiv 2025)",
    "Mechanic: Sorrifier-Driven Formal Decomposition Workflow for Automated Theorem Proving (Qiu et al., arXiv 2026)",
    "Formal Theorem Proving by Rewarding LLMs to Decompose Proofs Hierarchically [ProD] (Dong et al., NeurIPS 2024 MATH-AI Workshop)",
    "LeanProgress: Guiding Search for Neural Theorem Proving via Proof Progress Prediction (TMLR 2025)",
    "FormalRewardBench: A Benchmark for Formal Theorem Proving Reward Models (arXiv 2026)",
    "DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition (arXiv 2025)",
    "Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction (ICLR 2026)",
    "Kimina-Prover Preview: Towards Large Formal Reasoning Models with Reinforcement Learning (arXiv 2025)",
    "SorryDB: Can AI Provers Complete Real-World Lean Theorems? (Letson et al., arXiv 2026)",
    "FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified? (Ravi et al., arXiv 2026)",
    "Autoformalization in the Era of Large Language Models: A Survey (Weng et al., arXiv 2025)",
    "Pantograph: A Machine-to-Machine Interaction Interface for Advanced Theorem Proving (Aniva et al., TACAS 2025)"
  ],

  "description": "We propose Sorry-Progress Reward (SPR), a dense RL reward signal for training proof autoformalization models that uses Lean 4's sorry mechanism to provide exact, compiler-certified measurements of how much informal mathematical reasoning successfully translates to verified formal proof structure. Current RL training for autoformalization relies on binary reward (full proof compiles or not), while the best alternative (FormaRL) achieves 6.5× improvement on ProofNet but still offers zero partial credit for partially-correct formalizations. Meanwhile, Hilbert demonstrates that sorry-based decomposition brilliantly bridges informal and formal reasoning at inference time (99.2% miniF2F) but never trains models for this capability. SPR bridges this gap: given a proof attempt (optionally guided by an informal sketch), a lightweight sorrifier built on Pantograph and the Lean REPL decomposes it into k subgoals, and the Lean compiler verifies which are resolved, producing reward = verified_subgoals/total_subgoals. Unlike learned verifiers (Proof-Verifier, 93% accuracy), SPR is exact with zero model error. Unlike tactic-level process rewards (Process-Verified RL, ICLR 2026), SPR measures mathematically meaningful subgoal-level progress. Unlike SGVR's numeric sub-goal matching for geometry, SPR uses compiler-certified verification respecting proof dependencies. We train on two tracks — proof autoformalization (Qwen2.5-Coder-7B, composite SPR + semantic consistency reward) and formal proof generation (Goedel-Prover-V2-8B, weighted SPR) — using GRPO via Kimina-Prover-RL/Verl, with sorry-driven curriculum scheduling. We ablate five reward variants including difficulty-weighted (VeRPO-inspired) and min-over-subgoals (AlphaProof-inspired) aggregation. Evaluation targets unsaturated benchmarks: ProofNet (autoformalization, SOTA 41.4%), SorryDB (real-world), and FormalProofBench (graduate-level), with particular focus on sample efficiency gains on hard problems where binary reward yields near-zero learning signal.",

  "project_name": "sorry_progress_autoformalization",
  "source": "web_research"
}
```

---

### Issue-by-Issue Resolution Summary

| # | Reviewer Issue | Resolution |
|---|---|---|
| 1 | **CRITICAL: Must address autoformalization** | **Major reframing.** SPR is now positioned as a reward for training proof autoformalization models that bridge informal→formal proofs, directly extending Hilbert's inference-time paradigm to training time and improving on FormaRL's binary reward. Two-track design: Track A (autoformalization) + Track B (proof generation). |
| 2 | **Process-Verified RL venue error** | **Fixed.** Corrected to ICLR 2026 (confirmed via OpenReview). |
| 3 | **ProD venue misleading** | **Fixed.** Corrected to NeurIPS 2024 MATH-AI Workshop (not main track). |
| 4 | **Missing: Hilbert (ICLR 2026)** | **Added as primary related work.** Key positioning: Hilbert proves sorry-decomposition works brilliantly for informal→formal bridging but only at inference time with frozen models. SPR makes this a training objective. Hilbert's authors explicitly flag training as future work — we address their open problem. |
| 5 | **Missing: AlphaProof (Nature 2025)** | **Added.** Min-over-subgoals return design adopted as one of our ablated reward variants (R_min). Differentiated: AlphaProof uses MCTS+RL without sorry decomposition; we use sorry-completion as the reward itself. |
| 6 | **Missing: Proof-Verifier (ICLR 2026)** | **Added as key baseline.** Positioning: learned verifier (93% accuracy, provides diagnostics) vs. our compiler-certified signal (100% accuracy, zero model error). SPR and Proof-Verifier are complementary — SPR provides exact signal for formal proofs; Proof-Verifier handles informal proofs. |
| 7 | **Missing: VeRPO (arXiv 2026)** | **Added.** VeRPO's difficulty-weighted partial completion ratio directly inspires our Pass-Rate-Weighted SPR variant (R_pr) and the degenerate-group ratio analysis we adopt for evaluation. |
| 8 | **Sorrifier availability risk** | **Resolved with concrete implementation plan.** We build our own lightweight sorrifier using three mature tools: (a) Pantograph (TACAS, Stanford) for sorry-to-goal extraction, (b) leanprover-community REPL for structured sorry reporting, (c) Lean.Meta.Sorry API. This is narrower than Mechanic's full agent but sufficient for reward computation. SorryDB's infrastructure demonstrates sorry extraction at scale already works. Added 1 week to timeline. |
| 9 | **Novelty over SGVR is thin** | **Substantially strengthened.** Five differentiators: (1) compiler-verified vs. numeric-match verification, (2) autoformalization application (new domain), (3) proof dependency structure (later subgoals depend on earlier ones, unlike SGVR's independent numeric steps), (4) composite reward with semantic consistency for autoformalization, (5) multiple aggregation strategies (mean/min/difficulty-weighted) studied systematically. |
| 10 | **MiniF2F benchmark saturation** | **Replaced primary benchmarks.** New primaries: ProofNet (autoformalization, SOTA 41.4%), SorryDB (real-world, dynamic/unsaturated). Secondaries: FormalProofBench (graduate-level, SOTA ~34%), PutnamBench. MiniF2F retained only as sanity check. |

### Additional improvements beyond reviewer requests:
- **Added FormaRL** as key autoformalization baseline (discovered during research) — enables direct comparison of SPR's partial-credit reward vs. FormaRL's binary reward for autoformalization
- **Added FormalProofBench and Pantograph** to references
- **Five reward variants** now systematically ablated (base, depth-weighted, pass-rate-weighted, min, composite), drawing on insights from AlphaProof, VeRPO, and SGVR
- **Degenerate-group ratio analysis** borrowed from VeRPO to quantify reward signal density improvement
- **Sorry-driven curriculum** now better motivated and connected to SGVR's insight about sub-goal progress enabling curriculum design
- **Reordered target venues** — ICLR 2027 is now primary (more realistic timeline), AAAI 2027 is stretch target

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60c3f44a-2a23-4604-9712-ee9cd1ca7675",
  "isSidechain": false,
  "requestId": "req_011CbTY26sSzBQkA1gpLGvrf",
  "type": "assistant",
  "uuid": "2a946b42-493f-401f-ad55-4520baa0baea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QV2m9X824Lj9yBZaZbwk8P",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11460,
      "cache_read_input_tokens": 36053,
      "output_tokens": 7019,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11460,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 7019,
          "cache_read_input_tokens": 36053,
          "cache_creation_input_tokens": 11460,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11460
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Verifier-Certified Progress Rewards via Sorry-Driven Decomposition\",…",
  "leafUuid": "2a946b42-493f-401f-ad55-4520baa0baea",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise sorry-progress reward to address autoformalization gap",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Verifier-Certified Progress Rewards via Sorry-Driven Decomposition\",…",
  "leafUuid": "2a946b42-493f-401f-ad55-4520baa0baea",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise sorry-progress reward to address autoformalization gap",
  "sessionId": "c61f05f5-597a-4fa1-8ef1-d83c1f03bb02"
}
```

---
