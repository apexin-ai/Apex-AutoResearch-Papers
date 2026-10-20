# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-27 (UTC).** ## Original idea { "tit

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/048e6312-5e6d-4b84-a83d-11995bf4caaf.jsonl`
- **Structured JSON:** [`eb574a51ecdbb01d1fcb.json`](../../sessions/eb/eb574a51ecdbb01d1fcb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T17:50:11.433Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T17:50:11.433Z",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-27 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Frontier-Gap-Guided Scheduling of Distillation-RL Interleaving\",\n  \"core_problem\": \"RLVR improves sampling efficiency (pass@1) but cannot expand the reasoning frontier (pass@k), while distillation expands the frontier but is limited by teacher quality. There exists no principled framework for dynamically scheduling when to switch between these complementary phases during training.\",\n  \"opportunity\": \"The 'Sampling Efficiency Gap' (SEG = pass@k − pass@1) provides a direct, measurable signal: when SEG is large, the model has untapped potential that RL can harvest; when SEG is small but pass@k plateaus, distillation from a stronger source is needed to expand the frontier. No existing method uses this metric as a dynamic phase-switching criterion. SIRI (Sep 2025) does iterative compression-expansion but doesn't alternate distillation and RL. RLSD (Apr 2026) mixes them within a single phase rather than scheduling dynamically.\",\n  \"landscape\": \"The 'RL vs. Distillation' paper (arXiv 2505.14216) formally established that RLVR enhances pass@1 at the cost of pass@k on hard problems, while distillation with new knowledge expands capability. ProRL (NeurIPS 2025) showed prolonged RL with KL reset can find novel strategies. SIRI achieves 43.2% improvement on AIME24 via iterative length compression-expansion cycles. Self-Distilled RLVR (Apr 2026) combines RL direction with distillation magnitude in a single phase. RLAD (Feb 2026) performs selective imitation during RL via Trust Region Ratio Distillation but does not schedule discrete phases. HDPO (Mar 2026) augments GRPO with privileged self-distillation on cliff prompts but only targets zero-solve problems, not general phase scheduling. REOPOLD (Mar 2026) interprets on-policy distillation as policy optimization with an exploration-to-refinement schedule within a single distillation framework. PACED (Mar 2026) adapts distillation difficulty at the frontier of student competence. Power Distribution Bridges (May 2026) unifies sampling, self-reward RL, and self-distillation theoretically but does not propose an iterative alternation protocol. No existing work uses a pass@k-based diagnostic signal (SEG) as a dynamic criterion for when to switch between discrete distillation and RL training phases. The 'Does RL Really Incentivize Reasoning' paper explicitly calls this hybrid scheduling 'the most promising path' but notes no principled framework exists.\",\n  \"inspired_by\": \"field_gaps['Optimal interleaving of distillation and RLVR phases'] + untried_combinations[3] (iterative self-distillation RL spiral) + pattern['Diagnostic-First Method Design'] (measuring SEG before designing the method)\",\n  \"approach\": \"Define the Sampling Efficiency Gap (SEG = pass@k − pass@1, evaluated on a held-out validation set with k=64) as a phase-switching diagnostic. Start from a base model (Qwen3-8B or DeepSeek-R1-Distill-Qwen3-8B), run on-policy distillation from a strong teacher (DeepSeek-R1-0528 or Qwen3-235B) to establish the reasoning frontier, then monitor SEG every 50 training steps. When SEG exceeds a threshold τ_high (large untapped potential), switch to GRPO-based RLVR to compress sampling efficiency; when SEG drops below τ_low and pass@k growth stalls (frontier exhausted), switch back to distillation with fresh teacher rollouts to expand the frontier. Implement this as a controller atop the veRL framework, cycling through distillation→RL→distillation spirals until SEG converges. Compare against fixed-schedule baselines (SIRI-style fixed alternation, RLSD single-phase mixing, pure RLVR, pure distillation) on AIME 2024, MATH-500, and LiveCodeBench.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"1200-1500 H100-hours (5 spiral cycles × ~40h per cycle per run × 3 seeds + baselines + ablations on τ thresholds)\",\n      \"timeline\": \"14-16 weeks (4 weeks implementation, 6-8 weeks experiments, 4 weeks analysis and writing)\",\n      \"estimated_gpu_cost\": \"$2,400-3,000 at $2/H100-hr spot pricing\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"1000-1200 H100-hours (Claude assists with veRL integration, hyperparameter sweep design, and result analysis reducing dead-end runs)\",\n      \"timeline\": \"10-12 weeks (2 weeks implementation with Claude pair-programming, 5-6 weeks experiments, 3 weeks writing)\",\n      \"claude_api_cost\": \"$250-400 (extensive code generation, experiment log analysis, paper drafting assistance)\",\n      \"estimated_gpu_cost\": \"$2,000-2,400 at $2/H100-hr spot pricing\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"800-1000 H100-hours (automated experiment scheduling minimizes idle GPU time; adaptive sweep halts poor configs early)\",\n      \"timeline\": \"6-8 weeks (1 week scaffold setup, 4-5 weeks automated runs with parallel sweeps, 1-2 weeks paper generation)\",\n      \"claude_api_cost\": \"$600-900 (end-to-end pipeline orchestration, automated ablation analysis, draft writing and revision)\",\n      \"estimated_gpu_cost\": \"$1,600-2,000 at $2/H100-hr spot pricing\",\n      \"speed_bottleneck\": \"pass@64 evaluation requires 64 samples per problem per checkpoint; on AIME-sized sets this is tractable (~20 min per eval), but on MATH-500 with full k=64 sampling each evaluation checkpoint costs ~2 H100-hours, limiting monitoring frequency\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (full paper deadline: July 28, 2026)\",\n    \"ICLR 2027 (expected deadline: ~Sep-Oct 2026, based on ICLR 2026 pattern of Sep 24)\",\n    \"ARR July 2026 cycle (~July 15, 2026) for commitment to NAACL 2027 or EMNLP 2027\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Reinforcement Learning vs. Distillation: Understanding Accuracy and Capability in LLM Reasoning (arXiv 2505.14216, 2025)\",\n    \"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? (arXiv 2504.13837, 2025)\",\n    \"ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models (NeurIPS 2025)\",\n    \"SIRI: Scaling Iterative Reinforcement Learning with Interleaved Compression (arXiv 2509.25176, 2025)\",\n    \"Self-Distilled RLVR (arXiv 2604.03128, 2026)\",\n    \"Reinforcement-aware Knowledge Distillation for LLM Reasoning — RLAD (arXiv 2602.22495, 2026)\",\n    \"HDPO: Hybrid Distillation Policy Optimization via Privileged Self-Distillation (arXiv 2603.23871, 2026)\",\n    \"Scaling Reasoning Efficiently via Relaxed On-Policy Distillation — REOPOLD (arXiv 2603.11137, 2026)\",\n    \"PACED: Distillation at the Frontier of Student Competence (arXiv 2603.11178, 2026)\",\n    \"A Survey of On-Policy Distillation for Large Language Models (arXiv 2604.00626, 2026)\"\n  ],\n  \"description\": \"We propose SEG-Schedule, a principled framework for dynamically alternating between knowledge distillation and reinforcement learning with verifiable rewards (RLVR) during LLM reasoning post-training. Our key insight is that the Sampling Efficiency Gap (SEG = pass@k − pass@1), evaluated on a held-out validation set, serves as a real-time diagnostic: a large SEG signals untapped reasoning paths that RLVR can efficiently consolidate into pass@1, while a small SEG with stagnating pass@k indicates the model's reasoning frontier must be expanded via distillation from a stronger teacher. We implement a threshold-based controller atop the veRL framework that monitors SEG every 50 steps and triggers phase switches between GRPO-based RL and on-policy distillation from DeepSeek-R1-0528 or Qwen3-235B, creating an iterative spiral. Starting from Qwen3-8B, we target improvements over both pure-RLVR and pure-distillation baselines, as well as fixed-schedule and single-phase hybrid methods (RLSD, RLAD, HDPO), on AIME 2024, MATH-500, and LiveCodeBench. This is the first method to use a pass@k-derived signal as a dynamic phase-switching criterion, addressing an open problem explicitly identified in the 'RL vs. Distillation' literature.\",\n  \"project_name\": \"seg_schedule\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 1)\nIssues: [\"FABRICATED ATTRIBUTION: Neither arXiv 2505.14216 nor 2504.13837 calls hybrid scheduling 'the most promising path' — this claim must be removed or corrected with an actual source\", \"MISSING CRITICAL COMPETITOR: HPT (arXiv 2509.04419, Sep 2025) already performs adaptive switching between SFT and RL based on per-question rollout accuracy — must be cited and differentiated against\", \"MISSING RELATED WORK: Guide (2506.13923), KDRL (2506.02208), SASR (2505.13026), SRPO (2604.02288) are all uncited and directly relevant\", \"SEG SIGNAL RELIABILITY: arXiv 2511.16231 shows pass@k-pass@1 gap diminishes as policy concentrates — SEG may provide vanishing signal during successful training, creating a confound for the switching criterion\", \"THRESHOLD SENSITIVITY: τ_high and τ_low are likely task-dependent and model-dependent — the 'principled framework' claim is overstated for what is essentially a hand-tuned heuristic\", \"COST UNDERESTIMATE: Teacher rollout costs (running 235B or 671B-MoE models for distillation data) are not included in GPU estimates; pass@64 evaluation overhead at every 50 steps is substantial\", \"NOVELTY OVERCLAIMED: 'First method to use a pass@k-derived signal as a dynamic phase-switching criterion' is technically true but obscures that HPT already does metric-based phase switching and Guide already uses the pass@k compression framing\"]\nFeedback: 1) Remove the fabricated attribution about 'most promising path' — verify and cite the actual source, or rephrase as your own motivation. 2) Add HPT as a primary baseline and competitor — differentiate clearly: HPT does per-sample switching with rollout accuracy while SEG-Schedule proposes phase-level switching with pass@k gap; argue why phase-level switching with a richer metric adds value. 3) Add Guide, KDRL, SASR, SRPO to related work. 4) Address the SEG vanishing signal problem from arXiv 2511.16231 — perhaps propose a normalized SEG or relative metric that remains informative as training progresses. 5) Include an ablation comparing SEG against HPT's simpler rollout-accuracy switching criterion to justify the additional cost of pass@64 evaluation. 6) Include teacher inference costs in the resource estimate. 7) Tone down 'principled framework' language — acknowledge this is a diagnostic-guided heuristic, not a theoretically optimal scheduler.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.\n- Address each issue specifically.\n\n## 深度调研要求\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。\n3. **深度思考**：\n   - 核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach？\n4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。\n\n## 针对 Review 意见的定向搜索\n\n1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点\n2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline\n3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现\n4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot\n\n- You have full freedom: minor fix, major revision, or pivot.\n- Include a \"change_type\" field: \"minor\", \"major\", or \"pivot\".\n- Output a COMPLETE JSON object with ALL fields."
}
```

---

### Runtime record

_source line 2 · 2026-05-27T17:50:11.436Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T17:50:11.436Z",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf"
}
```

---

## Round 1

28 recorded events

### User

_source line 3 · 2026-05-27T17:50:11.468Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-27 (UTC).**

## Original idea
{
  "title": "Frontier-Gap-Guided Scheduling of Distillation-RL Interleaving",
  "core_problem": "RLVR improves sampling efficiency (pass@1) but cannot expand the reasoning frontier (pass@k), while distillation expands the frontier but is limited by teacher quality. There exists no principled framework for dynamically scheduling when to switch between these complementary phases during training.",
  "opportunity": "The 'Sampling Efficiency Gap' (SEG = pass@k − pass@1) provides a direct, measurable signal: when SEG is large, the model has untapped potential that RL can harvest; when SEG is small but pass@k plateaus, distillation from a stronger source is needed to expand the frontier. No existing method uses this metric as a dynamic phase-switching criterion. SIRI (Sep 2025) does iterative compression-expansion but doesn't alternate distillation and RL. RLSD (Apr 2026) mixes them within a single phase rather than scheduling dynamically.",
  "landscape": "The 'RL vs. Distillation' paper (arXiv 2505.14216) formally established that RLVR enhances pass@1 at the cost of pass@k on hard problems, while distillation with new knowledge expands capability. ProRL (NeurIPS 2025) showed prolonged RL with KL reset can find novel strategies. SIRI achieves 43.2% improvement on AIME24 via iterative length compression-expansion cycles. Self-Distilled RLVR (Apr 2026) combines RL direction with distillation magnitude in a single phase. RLAD (Feb 2026) performs selective imitation during RL via Trust Region Ratio Distillation but does not schedule discrete phases. HDPO (Mar 2026) augments GRPO with privileged self-distillation on cliff prompts but only targets zero-solve problems, not general phase scheduling. REOPOLD (Mar 2026) interprets on-policy distillation as policy optimization with an exploration-to-refinement schedule within a single distillation framework. PACED (Mar 2026) adapts distillation difficulty at the frontier of student competence. Power Distribution Bridges (May 2026) unifies sampling, self-reward RL, and self-distillation theoretically but does not propose an iterative alternation protocol. No existing work uses a pass@k-based diagnostic signal (SEG) as a dynamic criterion for when to switch between discrete distillation and RL training phases. The 'Does RL Really Incentivize Reasoning' paper explicitly calls this hybrid scheduling 'the most promising path' but notes no principled framework exists.",
  "inspired_by": "field_gaps['Optimal interleaving of distillation and RLVR phases'] + untried_combinations[3] (iterative self-distillation RL spiral) + pattern['Diagnostic-First Method Design'] (measuring SEG before designing the method)",
  "approach": "Define the Sampling Efficiency Gap (SEG = pass@k − pass@1, evaluated on a held-out validation set with k=64) as a phase-switching diagnostic. Start from a base model (Qwen3-8B or DeepSeek-R1-Distill-Qwen3-8B), run on-policy distillation from a strong teacher (DeepSeek-R1-0528 or Qwen3-235B) to establish the reasoning frontier, then monitor SEG every 50 training steps. When SEG exceeds a threshold τ_high (large untapped potential), switch to GRPO-based RLVR to compress sampling efficiency; when SEG drops below τ_low and pass@k growth stalls (frontier exhausted), switch back to distillation with fresh teacher rollouts to expand the frontier. Implement this as a controller atop the veRL framework, cycling through distillation→RL→distillation spirals until SEG converges. Compare against fixed-schedule baselines (SIRI-style fixed alternation, RLSD single-phase mixing, pure RLVR, pure distillation) on AIME 2024, MATH-500, and LiveCodeBench.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "1200-1500 H100-hours (5 spiral cycles × ~40h per cycle per run × 3 seeds + baselines + ablations on τ thresholds)",
      "timeline": "14-16 weeks (4 weeks implementation, 6-8 weeks experiments, 4 weeks analysis and writing)",
      "estimated_gpu_cost": "$2,400-3,000 at $2/H100-hr spot pricing"
    },
    "human_in_loop": {
      "gpu_hours": "1000-1200 H100-hours (Claude assists with veRL integration, hyperparameter sweep design, and result analysis reducing dead-end runs)",
      "timeline": "10-12 weeks (2 weeks implementation with Claude pair-programming, 5-6 weeks experiments, 3 weeks writing)",
      "claude_api_cost": "$250-400 (extensive code generation, experiment log analysis, paper drafting assistance)",
      "estimated_gpu_cost": "$2,000-2,400 at $2/H100-hr spot pricing"
    },
    "auto_research": {
      "gpu_hours": "800-1000 H100-hours (automated experiment scheduling minimizes idle GPU time; adaptive sweep halts poor configs early)",
      "timeline": "6-8 weeks (1 week scaffold setup, 4-5 weeks automated runs with parallel sweeps, 1-2 weeks paper generation)",
      "claude_api_cost": "$600-900 (end-to-end pipeline orchestration, automated ablation analysis, draft writing and revision)",
      "estimated_gpu_cost": "$1,600-2,000 at $2/H100-hr spot pricing",
      "speed_bottleneck": "pass@64 evaluation requires 64 samples per problem per checkpoint; on AIME-sized sets this is tractable (~20 min per eval), but on MATH-500 with full k=64 sampling each evaluation checkpoint costs ~2 H100-hours, limiting monitoring frequency"
    }
  },
  "target_venues": [
    "AAAI 2027 (full paper deadline: July 28, 2026)",
    "ICLR 2027 (expected deadline: ~Sep-Oct 2026, based on ICLR 2026 pattern of Sep 24)",
    "ARR July 2026 cycle (~July 15, 2026) for commitment to NAACL 2027 or EMNLP 2027"
  ],
  "level": "solid",
  "key_references": [
    "Reinforcement Learning vs. Distillation: Understanding Accuracy and Capability in LLM Reasoning (arXiv 2505.14216, 2025)",
    "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? (arXiv 2504.13837, 2025)",
    "ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models (NeurIPS 2025)",
    "SIRI: Scaling Iterative Reinforcement Learning with Interleaved Compression (arXiv 2509.25176, 2025)",
    "Self-Distilled RLVR (arXiv 2604.03128, 2026)",
    "Reinforcement-aware Knowledge Distillation for LLM Reasoning — RLAD (arXiv 2602.22495, 2026)",
    "HDPO: Hybrid Distillation Policy Optimization via Privileged Self-Distillation (arXiv 2603.23871, 2026)",
    "Scaling Reasoning Efficiently via Relaxed On-Policy Distillation — REOPOLD (arXiv 2603.11137, 2026)",
    "PACED: Distillation at the Frontier of Student Competence (arXiv 2603.11178, 2026)",
    "A Survey of On-Policy Distillation for Large Language Models (arXiv 2604.00626, 2026)"
  ],
  "description": "We propose SEG-Schedule, a principled framework for dynamically alternating between knowledge distillation and reinforcement learning with verifiable rewards (RLVR) during LLM reasoning post-training. Our key insight is that the Sampling Efficiency Gap (SEG = pass@k − pass@1), evaluated on a held-out validation set, serves as a real-time diagnostic: a large SEG signals untapped reasoning paths that RLVR can efficiently consolidate into pass@1, while a small SEG with stagnating pass@k indicates the model's reasoning frontier must be expanded via distillation from a stronger teacher. We implement a threshold-based controller atop the veRL framework that monitors SEG every 50 steps and triggers phase switches between GRPO-based RL and on-policy distillation from DeepSeek-R1-0528 or Qwen3-235B, creating an iterative spiral. Starting from Qwen3-8B, we target improvements over both pure-RLVR and pure-distillation baselines, as well as fixed-schedule and single-phase hybrid methods (RLSD, RLAD, HDPO), on AIME 2024, MATH-500, and LiveCodeBench. This is the first method to use a pass@k-derived signal as a dynamic phase-switching criterion, addressing an open problem explicitly identified in the 'RL vs. Distillation' literature.",
  "project_name": "seg_schedule",
  "source": "web_research"
}

## Reviewer feedback (round 1)
Issues: ["FABRICATED ATTRIBUTION: Neither arXiv 2505.14216 nor 2504.13837 calls hybrid scheduling 'the most promising path' — this claim must be removed or corrected with an actual source", "MISSING CRITICAL COMPETITOR: HPT (arXiv 2509.04419, Sep 2025) already performs adaptive switching between SFT and RL based on per-question rollout accuracy — must be cited and differentiated against", "MISSING RELATED WORK: Guide (2506.13923), KDRL (2506.02208), SASR (2505.13026), SRPO (2604.02288) are all uncited and directly relevant", "SEG SIGNAL RELIABILITY: arXiv 2511.16231 shows pass@k-pass@1 gap diminishes as policy concentrates — SEG may provide vanishing signal during successful training, creating a confound for the switching criterion", "THRESHOLD SENSITIVITY: τ_high and τ_low are likely task-dependent and model-dependent — the 'principled framework' claim is overstated for what is essentially a hand-tuned heuristic", "COST UNDERESTIMATE: Teacher rollout costs (running 235B or 671B-MoE models for distillation data) are not included in GPU estimates; pass@64 evaluation overhead at every 50 steps is substantial", "NOVELTY OVERCLAIMED: 'First method to use a pass@k-derived signal as a dynamic phase-switching criterion' is technically true but obscures that HPT already does metric-based phase switching and Guide already uses the pass@k compression framing"]
Feedback: 1) Remove the fabricated attribution about 'most promising path' — verify and cite the actual source, or rephrase as your own motivation. 2) Add HPT as a primary baseline and competitor — differentiate clearly: HPT does per-sample switching with rollout accuracy while SEG-Schedule proposes phase-level switching with pass@k gap; argue why phase-level switching with a richer metric adds value. 3) Add Guide, KDRL, SASR, SRPO to related work. 4) Address the SEG vanishing signal problem from arXiv 2511.16231 — perhaps propose a normalized SEG or relative metric that remains informative as training progresses. 5) Include an ablation comparing SEG against HPT's simpler rollout-accuracy switching criterion to justify the additional cost of pass@64 evaluation. 6) Include teacher inference costs in the resource estimate. 7) Tone down 'principled framework' language — acknowledge this is a diagnostic-guided heuristic, not a theoretically optimal scheduler.

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
  "promptId": "81938832-294a-4147-b0ab-ad0ff816bfdb",
  "type": "user",
  "uuid": "2a20ac77-0799-4c65-97b0-12fc6b3712d9",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T17:50:11.467Z_

```json
{
  "parentUuid": "2a20ac77-0799-4c65-97b0-12fc6b3712d9",
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
  "uuid": "8bf4d72d-0d35-4b20-b508-a639222a0b9a",
  "timestamp": "2026-05-27T17:50:11.467Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T17:50:11.467Z_

```json
{
  "parentUuid": "8bf4d72d-0d35-4b20-b508-a639222a0b9a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "bdfe1a56-d2a3-4e06-9150-37e9058f23e4",
  "timestamp": "2026-05-27T17:50:11.467Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
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
  "aiTitle": "Revise SEG-Schedule with HPT differentiation and signal reliability",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf"
}
```

---

### Assistant

_source line 7 · 2026-05-27T17:50:19.314Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully and plan my research strategy:

1. **FABRICATED ATTRIBUTION**: Need to verify what arXiv 2505.14216 and 2504.13837 actually say about hybrid scheduling
2. **MISSING CRITICAL COMPETITOR - HPT (arXiv 2509.04419)**: Need to read this paper to understand how it does adaptive switching between SFT and RL
3. **MISSING RELATED WORK**: Guide (2506.13923), KDRL (2506.02208), SASR (2505.13026), SRPO (2604.02288)


4. **SEG SIGNAL RELIABILITY**: The pass@k-pass@1 gap diminishes according to arXiv 2511.16231, which undermines the reliability of using this signal for routing decisions
5. **THRESHOLD SENSITIVITY**: The τ_high and τ_low parameters are highly task and model-dependent, making the approach less generalizable
6. **COST UNDERESTIMATE**: The analysis doesn't account for teacher rollout costs, which could significantly impact the actual efficiency gains
7. **NOVELTY OVERCLAIMED**: HPT already demonstrates metric-based phase switching, so the core contribution isn't as novel as presented

I need to launch parallel research agents to dig into these issues systematically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdfe1a56-d2a3-4e06-9150-37e9058f23e4",
  "isSidechain": false,
  "requestId": "req_011CbTVm9YXjz14AR8bWWFLj",
  "type": "assistant",
  "uuid": "d1a01c7a-b442-4e46-9d5e-5825f83eff12",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014mUD8VdJGXhAreAsmRzzkQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4826,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4826,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2213,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 4826,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4826
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

_source line 8 · 2026-05-27T17:50:19.319Z_

I'll conduct deep research on each reviewer issue in parallel before making revisions. Let me launch multiple research agents to investigate the key concerns.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1a01c7a-b442-4e46-9d5e-5825f83eff12",
  "isSidechain": false,
  "requestId": "req_011CbTVm9YXjz14AR8bWWFLj",
  "type": "assistant",
  "uuid": "ffd214fd-d2e7-4631-9b5b-e35e12f23895",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014mUD8VdJGXhAreAsmRzzkQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4826,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4826,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2213,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 4826,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4826
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

_source line 9 · 2026-05-27T17:50:24.106Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01NBAeFUWckNVR1EE2TRaZBC`</summary>

```json
{
  "description": "Research HPT paper (2509.04419)",
  "subagent_type": "general-purpose",
  "prompt": "I need to deeply research the paper HPT (arXiv 2509.04419, September 2025) which reportedly performs adaptive switching between SFT and RL based on per-question rollout accuracy. This is critical for a research idea revision.\n\nPlease:\n1. Use WebFetch to read the paper at https://arxiv.org/abs/2509.04419 \n2. Also try https://arxiv.org/pdf/2509.04419 if needed\n3. Search for \"HPT adaptive switching SFT RL rollout accuracy\" and \"HPT hybrid policy training\" to find any blog posts or discussions\n\nI need to understand:\n- What exactly is HPT's switching mechanism? Is it per-sample or per-phase?\n- What metric does HPT use to decide when to do SFT vs RL?\n- How does HPT's approach differ from using a pass@k-based signal?\n- What are HPT's limitations?\n- What benchmarks does HPT evaluate on and what results does it achieve?\n\nReport your findings in detail (500+ words). Include direct quotes from the paper where possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffd214fd-d2e7-4631-9b5b-e35e12f23895",
  "isSidechain": false,
  "requestId": "req_011CbTVm9YXjz14AR8bWWFLj",
  "type": "assistant",
  "uuid": "8ff74c5a-8091-4143-bb31-e7923036d797",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014mUD8VdJGXhAreAsmRzzkQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4826,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4826,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2213,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 4826,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4826
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

_source line 10 · 2026-05-27T17:50:29.727Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01KsK7jeJsr6T41HfxGbBF8b`</summary>

```json
{
  "description": "Research Guide, KDRL, SASR, SRPO papers",
  "subagent_type": "general-purpose",
  "prompt": "I need to research four papers that are missing from a research idea's related work section. For each paper, I need to understand what they do and how they relate to the topic of combining distillation and RL for LLM reasoning.\n\nThe papers are:\n1. Guide (arXiv 2506.13923)\n2. KDRL (arXiv 2506.02208)\n3. SASR (arXiv 2505.13026)\n4. SRPO (arXiv 2604.02288)\n\nFor each paper:\n- Use WebFetch to read the abstract and introduction from https://arxiv.org/abs/XXXX.XXXXX\n- Try to understand: What is the core method? How does it combine or relate distillation and RL? What metrics/signals does it use? What are its key results?\n\nAlso search for:\n- \"Guide distillation reinforcement learning LLM reasoning 2025\"\n- \"KDRL knowledge distillation reinforcement learning\"\n- \"SASR self-augmented self-reinforcement reasoning\"\n- \"SRPO self-refined policy optimization\"\n\nReport detailed findings for each paper (200+ words each). I need enough detail to properly cite and differentiate against them."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ff74c5a-8091-4143-bb31-e7923036d797",
  "isSidechain": false,
  "requestId": "req_011CbTVm9YXjz14AR8bWWFLj",
  "type": "assistant",
  "uuid": "c0335a95-6304-4580-b51b-b595a9558441",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014mUD8VdJGXhAreAsmRzzkQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4826,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4826,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2213,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 4826,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4826
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

_source line 11 · 2026-05-27T17:50:35.554Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01CfLpeEpK4z95b2A1dRwby4`</summary>

```json
{
  "description": "Research SEG vanishing signal issue",
  "subagent_type": "general-purpose",
  "prompt": "I need to research the problem that the pass@k - pass@1 gap (Sampling Efficiency Gap) may diminish as RL training progresses and the policy concentrates. This is a critical issue for a research idea that uses SEG as a dynamic phase-switching signal.\n\nPlease:\n1. Use WebFetch to read arXiv 2511.16231 (the paper that reportedly shows pass@k-pass@1 gap diminishes as policy concentrates). Read https://arxiv.org/abs/2511.16231\n2. Search for \"pass@k pass@1 gap RL training policy concentration\" and \"sampling efficiency gap reinforcement learning LLM\"\n3. Search for \"normalized pass@k metric\" or \"relative sampling efficiency\" to find if anyone has proposed solutions\n4. Search for \"entropy collapse RL LLM reasoning\" since policy concentration is related to entropy collapse\n\nI need to understand:\n- Exactly how and why does the pass@k-pass@1 gap diminish during training?\n- At what point in training does this become a problem?\n- Are there normalized or relative versions of this metric that remain informative?\n- What are potential solutions (e.g., temperature scaling, entropy regularization, relative SEG)?\n\nReport in detail (500+ words). This is critical for addressing a reviewer concern about signal reliability."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0335a95-6304-4580-b51b-b595a9558441",
  "isSidechain": false,
  "requestId": "req_011CbTVm9YXjz14AR8bWWFLj",
  "type": "assistant",
  "uuid": "7f8de2fe-9dc6-4c1a-a360-95476dfe98b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014mUD8VdJGXhAreAsmRzzkQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4826,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4826,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2213,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 4826,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4826
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

_source line 12 · 2026-05-27T17:50:41.705Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0126gbKf1o1ZsLGyub4t4aK1`</summary>

```json
{
  "description": "Verify fabricated attribution claim",
  "subagent_type": "general-purpose",
  "prompt": "I need to verify whether two specific papers actually call hybrid scheduling of distillation and RL \"the most promising path\" for LLM reasoning training. A reviewer flagged this as a fabricated attribution.\n\nThe papers in question:\n1. \"Reinforcement Learning vs. Distillation: Understanding Accuracy and Capability in LLM Reasoning\" (arXiv 2505.14216)\n2. \"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?\" (arXiv 2504.13837)\n\nPlease:\n1. Use WebFetch to read both papers:\n   - https://arxiv.org/abs/2505.14216\n   - https://arxiv.org/abs/2504.13837\n2. Search specifically for any mention of \"promising path\", \"hybrid scheduling\", \"alternating distillation and RL\", \"combining distillation and reinforcement\" in these papers\n3. Also search more broadly: \"hybrid distillation RL scheduling most promising\" to see if any other paper uses this language\n\nI need to know:\n- Do either paper actually use the phrase \"most promising path\" about hybrid scheduling?\n- What do these papers actually conclude/recommend about combining distillation and RL?\n- Is there any other credible source that makes this claim?\n\nBe thorough and honest. If the attribution is indeed fabricated, I need to know so I can correct it. Report exact quotes where possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f8de2fe-9dc6-4c1a-a360-95476dfe98b0",
  "isSidechain": false,
  "requestId": "req_011CbTVm9YXjz14AR8bWWFLj",
  "type": "assistant",
  "uuid": "efd51568-38f8-4de1-8f62-4aa68d2060a2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014mUD8VdJGXhAreAsmRzzkQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4826,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4826,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2213,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 4826,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4826
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

_source line 13 · 2026-05-27T17:50:48.686Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01TyccuDoB7YgqB1bGVJLtzf`</summary>

```json
{
  "description": "Research teacher inference costs",
  "subagent_type": "general-purpose",
  "prompt": "I need to estimate realistic GPU costs for running large teacher models (DeepSeek-R1-0528 at 671B MoE, Qwen3-235B) for distillation data generation, and also the cost of pass@64 evaluation.\n\nPlease search for:\n1. \"DeepSeek-R1 inference cost GPU hours\" and \"DeepSeek-R1-0528 inference requirements\"\n2. \"Qwen3-235B inference cost\" and \"Qwen3-235B GPU requirements\"\n3. \"pass@64 evaluation cost LLM reasoning\" \n4. \"veRL framework GPU requirements\" and \"GRPO training cost 8B model\"\n5. Search for any papers or blog posts discussing the actual compute costs of distillation from large teachers\n\nAlso try WebFetch on:\n- https://arxiv.org/abs/2501.12948 (DeepSeek-R1 paper for inference details)\n- Any recent blog posts about running DeepSeek-R1 inference\n\nI need realistic estimates for:\n- How many H100-hours to generate distillation data from a 671B MoE model for ~10K problems with multiple rollouts?\n- How many H100-hours for pass@64 evaluation of an 8B model on MATH-500 and AIME?\n- What is the total realistic cost including teacher inference?\n\nReport with specific numbers where possible (300+ words)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efd51568-38f8-4de1-8f62-4aa68d2060a2",
  "isSidechain": false,
  "requestId": "req_011CbTVm9YXjz14AR8bWWFLj",
  "type": "assistant",
  "uuid": "ec3dbd5e-9f48-48d8-9884-21220c74a322",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014mUD8VdJGXhAreAsmRzzkQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4826,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4826,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2213,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 4826,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4826
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

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Frontier-Gap-Guided Scheduling of Distillation-RL Interleaving\",   \"co…",
  "leafUuid": "ec3dbd5e-9f48-48d8-9884-21220c74a322",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise SEG-Schedule with HPT differentiation and signal reliability",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf"
}
```

---

### Tool result

_source line 16 · 2026-05-27T17:52:12.982Z_

<details><summary>↩ Tool result · `toolu_01KsK7jeJsr6T41HfxGbBF8b`</summary>

```text
Now I have comprehensive information on all four papers. Here is my detailed report.

---

## Detailed Findings on Four Papers

### 1. Guide (arXiv 2506.13923) — "Adaptive Guidance Accelerates Reinforcement Learning of Reasoning Models"

**Authors:** Vaskar Nath, Elaine Lau, Anisha Gunjal, Manasi Sharma, Nikhil Baharte, Sean Hendryx

**Core Method:** Guide introduces a class of online RL training algorithms that selectively inject natural-language hints into model context when all k unguided rollouts on a problem fail. Crucially, the model must still derive solutions in its own terms — the hints are pedagogically-inspired conceptual cues (generated by GPT-4o from reference solutions), not full solutions. When rollouts succeed without hints, training proceeds normally via standard GRPO or PPO. The key technical innovation is an off-policy correction mechanism: because guided trajectories are conditioned on extra context (the hint), they are off-policy relative to the unguided objective. Guide fixes this by adjusting importance sampling ratios — the denominator uses the old policy's probability conditioned on both prompt and guidance, while the numerator uses the new policy conditioned only on the prompt. This ensures gradient updates align with the plain-prompt (no-hint) objective, so the model generalizes without needing hints at test time.

**Relationship to Distillation and RL:** The paper provides an important analytical decomposition of RLVR gains. Approximately 75% of performance improvement comes from "self-distillation" — concentrating probability mass from solutions already reachable within pass@k into pass@1. The remaining ~25% is "capability gain" — genuinely solving previously unreachable problems. Guide's contribution is primarily to increase pass@k (making more solutions discoverable via hints), which then feeds into the self-distillation mechanism during subsequent unguided training. This is not traditional teacher-student distillation; rather, it is a form of curriculum-guided exploration that expands the frontier of problems the model can solve.

**Key Results:** On Qwen-2.5-Math-7B, Guide-GRPO achieved 82.68% on MATH500 vs 79.00% for vanilla GRPO, 43.11% vs 39.56% on Olympiad Bench, and 30.67% vs 26.67% on AIME 2024. The macro-average improvement is approximately 4% across math benchmarks. The 32B model showed a 3.39 percentage point macro-average improvement. Training used OpenR1-Math-220k (93.7K problems) and was tested at scales from 0.5B to 72B parameters. Results were validated across >500,000 reasoning problems spanning math, science, and code.

**Differentiation:** Guide is distinct from methods that directly distill teacher outputs. It uses hints only as exploration aids during RL training, with off-policy corrections ensuring the learned policy is independent of hints. The "distillation" here is self-distillation (pass@k to pass@1), not cross-model knowledge transfer.

---

### 2. KDRL (arXiv 2506.02208) — "KDRL: Post-Training Reasoning LLMs via Unified Knowledge Distillation and Reinforcement Learning"

**Authors:** Hongling Xu, Qi Zhu, Heyuan Deng, Jinpeng Li, Lu Hou, Yasheng Wang, Lifeng Shang, Ruifeng Xu, Fei Mi

**Core Method:** KDRL proposes a unified objective that jointly optimizes knowledge distillation from a teacher model and reinforcement learning from rule-based rewards. The combined loss is: J_KDRL(theta) = J_GRPO(theta) - beta * D_KL^k2(pi_theta || pi_T), where the first term is the standard GRPO reward-maximization objective and the second term minimizes the reverse KL divergence between student and teacher distributions. The critical theoretical insight is that reverse KL minimization can be reformulated as a REINFORCE variant using teacher log-likelihood ratios R_{i,t} = log(pi_T / pi_theta) as token-level reward signals. This allows seamless integration with GRPO's advantage-weighted policy gradients through a single policy gradient framework.

**KL Approximations Explored:** The paper systematically compares three KL estimators: (1) the k2 estimator (E[0.5 * R_{i,t}^2]), which provides unbiased gradients despite biased estimates; (2) the k3 estimator (E[exp(R_{i,t}) - R_{i,t} - 1]), which is unbiased but produces biased gradients; and (3) a Top-K approximation retaining only top-K teacher logits, which caused training instability. The k2 estimator achieved 1.4% higher accuracy on AIME24 than k3 and was adopted as default.

**Key Results:** KDRL-Annealing (with scheduled beta decay) achieved 57.2% average across 6 benchmarks, outperforming SFT by +4.7%, GRPO by +2.6%, and KD-RKL by +1.1%. On AIME24 specifically: KDRL achieved 42.9% vs 38.3% (GRPO) and 41.0% (KD-RKL). Importantly for efficiency, KDRL produced 6,000+ fewer reasoning tokens than KD-RKL while maintaining comparable accuracy, and response-level reward masking reduced output by >1,400 tokens (10%). Under equal 80-hour training budgets, KDRL consistently outperformed both baselines. The joint loss formulation proved superior to reward shaping approaches, preventing training collapse observed in earlier integration attempts.

**Differentiation:** KDRL is the most directly relevant paper for any work combining distillation and RL, as it explicitly unifies both into a single policy gradient objective. It requires a separate teacher model (unlike self-distillation approaches) and focuses on reverse KL divergence with careful estimator selection. Its key advantage is simultaneous teacher guidance and environment-driven exploration without separate training phases.

---

### 3. SASR (arXiv 2505.13026) — "Step-wise Adaptive Integration of Supervised Fine-tuning and Reinforcement Learning for Task-Specific LLMs"

**Authors:** Jack Chen, Fazhong Liu, Naruto Liu, Yuhan Luo, Erqu Qin, Harry Zheng, Tian Dong, Haojin Zhu, Yan Meng, Xiao Wang

**Core Method:** SASR (Step-wise Adaptive Supervised-Reinforcement) is a hybrid training framework that dynamically balances SFT and RL (specifically GRPO) throughout training using gradient-norm-based monitoring. The switching probability at step t is computed as: p_t = ||grad D_KL(theta)^t|| / (||grad D_KL(theta)^t|| + gamma * ||grad D_KL(theta)^0||), where the current KL divergence gradient is compared against the warm-up phase baseline. When this ratio is high (the model has drifted far from the original distribution), SFT weight increases to restore stability. When low (the model has converged tightly), GRPO weight increases to encourage exploration. The theoretical foundation establishes that the gradient norm of the SFT loss equals the gradient of KL divergence between model and data distributions, enabling this monitoring.

**Relationship to Distillation and RL:** SASR frames its combination through a curriculum learning analogy: SFT serves as "guided study using reference materials" (analogous to distillation from expert demonstrations), while RL acts as "quiz-like reinforcement that fosters generalization." Unlike KDRL which unifies both into one objective, SASR maintains them as separate training modes that are dynamically interleaved. The adaptive mechanism avoids the "forget-stagnation trade-off" where pure RL causes catastrophic forgetting while excessive SFT causes overfitting.

**Key Results:** On GSM8K, SASR achieved 80.3% vs 75.2% for pure SFT (+5.1%). On MATH, 23.0% vs 21.2% (+1.8%). Most dramatically, on the Knight-and-Knaves logic reasoning benchmark, 42% vs 28% for SFT (+14%), even outperforming GPT-4o (33%) by 9%. SASR outperformed pure SFT, pure GRPO, and static hybrid methods (SSR, SSR_cosine). Models used were Qwen2.5-1.5B and Qwen2.5-0.5B. Training required approximately 45 GPU days on NVIDIA H20 hardware.

**Differentiation:** SASR's contribution is the adaptive scheduling mechanism rather than a new objective function. It treats SFT and RL as complementary modes that need dynamic balancing based on training state, rather than fusing them into a single loss. It operates at smaller model scales (0.5B-1.5B) and focuses on task-specific fine-tuning rather than general reasoning improvement.

---

### 4. SRPO (arXiv 2604.02288) — "Unifying Group-Relative and Self-Distillation Policy Optimization via Sample Routing"

**Authors:** Gengsheng Li, Tianyu Yang, Junfeng Fang, Mingyang Song, Mao Zheng, Haiyun Guo, Dan Zhang, Jinqiao Wang, Tat-Seng Chua

**Core Method:** SRPO (Sample-Routed Policy Optimization) is a unified on-policy RL framework that routes training samples based on correctness: correct samples go to GRPO's reward-aligned reinforcement pathway, while failed samples are directed to SDPO's (Self-Distillation Policy Optimization) targeted logit-level correction. This addresses complementary weaknesses: GRPO applies coarse, uniform penalties across failed rollouts, lacking token-level precision for correcting specific deviations; SDPO provides dense logit-level supervision for rapid early improvement but collapses during prolonged training. The paper identifies two root causes of SDPO's late-stage collapse: (1) self-distillation on already-correct samples introduces optimization ambiguity, and (2) the self-teacher's signal reliability progressively degrades over time.

**Entropy-Aware Dynamic Weighting:** SRPO incorporates an entropy-aware mechanism that measures the confidence of distillation targets. High-entropy (uncertain) teacher signals are suppressed, while low-entropy (confident) signals are emphasized. This prevents the training instability that plagues SDPO in later training stages.

**Key Results:** On Qwen3-8B across five benchmarks, SRPO achieved 3.4% improvement over GRPO and 6.3% improvement over SDPO, while also reducing per-step computational cost by up to 17.2%. The method achieves SDPO's rapid early improvement combined with GRPO's long-horizon stability — getting the best of both worlds.

**Differentiation:** SRPO is fundamentally about combining two RL optimization strategies (GRPO and SDPO) through intelligent sample routing, not about combining distillation from an external teacher with RL. The "distillation" component here is self-distillation (the model distills from its own previous-step logits via SDPO), applied selectively only to failed samples. This makes it a pure RL method with a self-distillation component, distinct from teacher-student KD+RL approaches like KDRL. Its primary novelty is the routing mechanism and entropy-aware weighting rather than a new training paradigm.

---

## Summary of Key Distinctions

| Paper | KD Type | RL Type | Integration Strategy | Scale |
|-------|---------|---------|---------------------|-------|
| **Guide** | Self-distillation (pass@k to pass@1) via hint-guided exploration | GRPO/PPO with off-policy correction | Hints expand exploration; off-policy correction ensures unguided generalization | 0.5B-72B |
| **KDRL** | Teacher-student reverse KL distillation | GRPO with rule-based rewards | Single unified policy gradient objective | Not specified (reasoning LLMs) |
| **SASR** | SFT from demonstrations (implicit distillation) | GRPO with KL regularization | Dynamic interleaving via gradient-norm monitoring | 0.5B-1.5B |
| **SRPO** | Self-distillation via SDPO (logit-level, on failed samples only) | GRPO (on correct samples) | Sample routing by correctness + entropy-aware weighting | 8B (Qwen3) |

Sources:
- [Guide - arXiv 2506.13923](https://arxiv.org/abs/2506.13923)
- [KDRL - arXiv 2506.02208](https://arxiv.org/abs/2506.02208)
- [KDRL on HuggingFace Papers](https://huggingface.co/papers/2506.02208)
- [SASR - arXiv 2505.13026](https://arxiv.org/abs/2505.13026)
- [SRPO - arXiv 2604.02288](https://arxiv.org/abs/2604.02288)
- [KDRL on Semantic Scholar](https://www.semanticscholar.org/paper/KDRL:-Post-Training-Reasoning-LLMs-via-Unified-and-Xu-Zhu/f7b400cab655e820a38348fd1c933ab3036b29f9)
- [SRPO project page](https://srpo.pages.dev/)

agentId: ab118ab260224fc0d (use SendMessage with to: 'ab118ab260224fc0d' to continue this agent)
&lt;usage>total_tokens: 22188
tool_uses: 13
duration_ms: 103252&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0335a95-6304-4580-b51b-b595a9558441",
  "isSidechain": false,
  "promptId": "81938832-294a-4147-b0ab-ad0ff816bfdb",
  "type": "user",
  "uuid": "0e6b2b30-ccf0-4e37-94d8-170d46b5ccca",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to research four papers that are missing from a research idea's related work section. For each paper, I need to understand what they do and how they relate to the topic of combining distillation and RL for LLM reasoning.\n\nThe papers are:\n1. Guide (arXiv 2506.13923)\n2. KDRL (arXiv 2506.02208)\n3. SASR (arXiv 2505.13026)\n4. SRPO (arXiv 2604.02288)\n\nFor each paper:\n- Use WebFetch to read the abstract and introduction from https://arxiv.org/abs/XXXX.XXXXX\n- Try to understand: What is the core method? How does it combine or relate distillation and RL? What metrics/signals does it use? What are its key results?\n\nAlso search for:\n- \"Guide distillation reinforcement learning LLM reasoning 2025\"\n- \"KDRL knowledge distillation reinforcement learning\"\n- \"SASR self-augmented self-reinforcement reasoning\"\n- \"SRPO self-refined policy optimization\"\n\nReport detailed findings for each paper (200+ words each). I need enough detail to properly cite and differentiate against them.",
    "agentId": "ab118ab260224fc0d",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information on all four papers. Here is my detailed report.\n\n---\n\n## Detailed Findings on Four Papers\n\n### 1. Guide (arXiv 2506.13923) — \"Adaptive Guidance Accelerates Reinforcement Learning of Reasoning Models\"\n\n**Authors:** Vaskar Nath, Elaine Lau, Anisha Gunjal, Manasi Sharma, Nikhil Baharte, Sean Hendryx\n\n**Core Method:** Guide introduces a class of online RL training algorithms that selectively inject natural-language hints into model context when all k unguided rollouts on a problem fail. Crucially, the model must still derive solutions in its own terms — the hints are pedagogically-inspired conceptual cues (generated by GPT-4o from reference solutions), not full solutions. When rollouts succeed without hints, training proceeds normally via standard GRPO or PPO. The key technical innovation is an off-policy correction mechanism: because guided trajectories are conditioned on extra context (the hint), they are off-policy relative to the unguided objective. Guide fixes this by adjusting importance sampling ratios — the denominator uses the old policy's probability conditioned on both prompt and guidance, while the numerator uses the new policy conditioned only on the prompt. This ensures gradient updates align with the plain-prompt (no-hint) objective, so the model generalizes without needing hints at test time.\n\n**Relationship to Distillation and RL:** The paper provides an important analytical decomposition of RLVR gains. Approximately 75% of performance improvement comes from \"self-distillation\" — concentrating probability mass from solutions already reachable within pass@k into pass@1. The remaining ~25% is \"capability gain\" — genuinely solving previously unreachable problems. Guide's contribution is primarily to increase pass@k (making more solutions discoverable via hints), which then feeds into the self-distillation mechanism during subsequent unguided training. This is not traditional teacher-student distillation; rather, it is a form of curriculum-guided exploration that expands the frontier of problems the model can solve.\n\n**Key Results:** On Qwen-2.5-Math-7B, Guide-GRPO achieved 82.68% on MATH500 vs 79.00% for vanilla GRPO, 43.11% vs 39.56% on Olympiad Bench, and 30.67% vs 26.67% on AIME 2024. The macro-average improvement is approximately 4% across math benchmarks. The 32B model showed a 3.39 percentage point macro-average improvement. Training used OpenR1-Math-220k (93.7K problems) and was tested at scales from 0.5B to 72B parameters. Results were validated across >500,000 reasoning problems spanning math, science, and code.\n\n**Differentiation:** Guide is distinct from methods that directly distill teacher outputs. It uses hints only as exploration aids during RL training, with off-policy corrections ensuring the learned policy is independent of hints. The \"distillation\" here is self-distillation (pass@k to pass@1), not cross-model knowledge transfer.\n\n---\n\n### 2. KDRL (arXiv 2506.02208) — \"KDRL: Post-Training Reasoning LLMs via Unified Knowledge Distillation and Reinforcement Learning\"\n\n**Authors:** Hongling Xu, Qi Zhu, Heyuan Deng, Jinpeng Li, Lu Hou, Yasheng Wang, Lifeng Shang, Ruifeng Xu, Fei Mi\n\n**Core Method:** KDRL proposes a unified objective that jointly optimizes knowledge distillation from a teacher model and reinforcement learning from rule-based rewards. The combined loss is: J_KDRL(theta) = J_GRPO(theta) - beta * D_KL^k2(pi_theta || pi_T), where the first term is the standard GRPO reward-maximization objective and the second term minimizes the reverse KL divergence between student and teacher distributions. The critical theoretical insight is that reverse KL minimization can be reformulated as a REINFORCE variant using teacher log-likelihood ratios R_{i,t} = log(pi_T / pi_theta) as token-level reward signals. This allows seamless integration with GRPO's advantage-weighted policy gradients through a single policy gradient framework.\n\n**KL Approximations Explored:** The paper systematically compares three KL estimators: (1) the k2 estimator (E[0.5 * R_{i,t}^2]), which provides unbiased gradients despite biased estimates; (2) the k3 estimator (E[exp(R_{i,t}) - R_{i,t} - 1]), which is unbiased but produces biased gradients; and (3) a Top-K approximation retaining only top-K teacher logits, which caused training instability. The k2 estimator achieved 1.4% higher accuracy on AIME24 than k3 and was adopted as default.\n\n**Key Results:** KDRL-Annealing (with scheduled beta decay) achieved 57.2% average across 6 benchmarks, outperforming SFT by +4.7%, GRPO by +2.6%, and KD-RKL by +1.1%. On AIME24 specifically: KDRL achieved 42.9% vs 38.3% (GRPO) and 41.0% (KD-RKL). Importantly for efficiency, KDRL produced 6,000+ fewer reasoning tokens than KD-RKL while maintaining comparable accuracy, and response-level reward masking reduced output by >1,400 tokens (10%). Under equal 80-hour training budgets, KDRL consistently outperformed both baselines. The joint loss formulation proved superior to reward shaping approaches, preventing training collapse observed in earlier integration attempts.\n\n**Differentiation:** KDRL is the most directly relevant paper for any work combining distillation and RL, as it explicitly unifies both into a single policy gradient objective. It requires a separate teacher model (unlike self-distillation approaches) and focuses on reverse KL divergence with careful estimator selection. Its key advantage is simultaneous teacher guidance and environment-driven exploration without separate training phases.\n\n---\n\n### 3. SASR (arXiv 2505.13026) — \"Step-wise Adaptive Integration of Supervised Fine-tuning and Reinforcement Learning for Task-Specific LLMs\"\n\n**Authors:** Jack Chen, Fazhong Liu, Naruto Liu, Yuhan Luo, Erqu Qin, Harry Zheng, Tian Dong, Haojin Zhu, Yan Meng, Xiao Wang\n\n**Core Method:** SASR (Step-wise Adaptive Supervised-Reinforcement) is a hybrid training framework that dynamically balances SFT and RL (specifically GRPO) throughout training using gradient-norm-based monitoring. The switching probability at step t is computed as: p_t = ||grad D_KL(theta)^t|| / (||grad D_KL(theta)^t|| + gamma * ||grad D_KL(theta)^0||), where the current KL divergence gradient is compared against the warm-up phase baseline. When this ratio is high (the model has drifted far from the original distribution), SFT weight increases to restore stability. When low (the model has converged tightly), GRPO weight increases to encourage exploration. The theoretical foundation establishes that the gradient norm of the SFT loss equals the gradient of KL divergence between model and data distributions, enabling this monitoring.\n\n**Relationship to Distillation and RL:** SASR frames its combination through a curriculum learning analogy: SFT serves as \"guided study using reference materials\" (analogous to distillation from expert demonstrations), while RL acts as \"quiz-like reinforcement that fosters generalization.\" Unlike KDRL which unifies both into one objective, SASR maintains them as separate training modes that are dynamically interleaved. The adaptive mechanism avoids the \"forget-stagnation trade-off\" where pure RL causes catastrophic forgetting while excessive SFT causes overfitting.\n\n**Key Results:** On GSM8K, SASR achieved 80.3% vs 75.2% for pure SFT (+5.1%). On MATH, 23.0% vs 21.2% (+1.8%). Most dramatically, on the Knight-and-Knaves logic reasoning benchmark, 42% vs 28% for SFT (+14%), even outperforming GPT-4o (33%) by 9%. SASR outperformed pure SFT, pure GRPO, and static hybrid methods (SSR, SSR_cosine). Models used were Qwen2.5-1.5B and Qwen2.5-0.5B. Training required approximately 45 GPU days on NVIDIA H20 hardware.\n\n**Differentiation:** SASR's contribution is the adaptive scheduling mechanism rather than a new objective function. It treats SFT and RL as complementary modes that need dynamic balancing based on training state, rather than fusing them into a single loss. It operates at smaller model scales (0.5B-1.5B) and focuses on task-specific fine-tuning rather than general reasoning improvement.\n\n---\n\n### 4. SRPO (arXiv 2604.02288) — \"Unifying Group-Relative and Self-Distillation Policy Optimization via Sample Routing\"\n\n**Authors:** Gengsheng Li, Tianyu Yang, Junfeng Fang, Mingyang Song, Mao Zheng, Haiyun Guo, Dan Zhang, Jinqiao Wang, Tat-Seng Chua\n\n**Core Method:** SRPO (Sample-Routed Policy Optimization) is a unified on-policy RL framework that routes training samples based on correctness: correct samples go to GRPO's reward-aligned reinforcement pathway, while failed samples are directed to SDPO's (Self-Distillation Policy Optimization) targeted logit-level correction. This addresses complementary weaknesses: GRPO applies coarse, uniform penalties across failed rollouts, lacking token-level precision for correcting specific deviations; SDPO provides dense logit-level supervision for rapid early improvement but collapses during prolonged training. The paper identifies two root causes of SDPO's late-stage collapse: (1) self-distillation on already-correct samples introduces optimization ambiguity, and (2) the self-teacher's signal reliability progressively degrades over time.\n\n**Entropy-Aware Dynamic Weighting:** SRPO incorporates an entropy-aware mechanism that measures the confidence of distillation targets. High-entropy (uncertain) teacher signals are suppressed, while low-entropy (confident) signals are emphasized. This prevents the training instability that plagues SDPO in later training stages.\n\n**Key Results:** On Qwen3-8B across five benchmarks, SRPO achieved 3.4% improvement over GRPO and 6.3% improvement over SDPO, while also reducing per-step computational cost by up to 17.2%. The method achieves SDPO's rapid early improvement combined with GRPO's long-horizon stability — getting the best of both worlds.\n\n**Differentiation:** SRPO is fundamentally about combining two RL optimization strategies (GRPO and SDPO) through intelligent sample routing, not about combining distillation from an external teacher with RL. The \"distillation\" component here is self-distillation (the model distills from its own previous-step logits via SDPO), applied selectively only to failed samples. This makes it a pure RL method with a self-distillation component, distinct from teacher-student KD+RL approaches like KDRL. Its primary novelty is the routing mechanism and entropy-aware weighting rather than a new training paradigm.\n\n---\n\n## Summary of Key Distinctions\n\n| Paper | KD Type | RL Type | Integration Strategy | Scale |\n|-------|---------|---------|---------------------|-------|\n| **Guide** | Self-distillation (pass@k to pass@1) via hint-guided exploration | GRPO/PPO with off-policy correction | Hints expand exploration; off-policy correction ensures unguided generalization | 0.5B-72B |\n| **KDRL** | Teacher-student reverse KL distillation | GRPO with rule-based rewards | Single unified policy gradient objective | Not specified (reasoning LLMs) |\n| **SASR** | SFT from demonstrations (implicit distillation) | GRPO with KL regularization | Dynamic interleaving via gradient-norm monitoring | 0.5B-1.5B |\n| **SRPO** | Self-distillation via SDPO (logit-level, on failed samples only) | GRPO (on correct samples) | Sample routing by correctness + entropy-aware weighting | 8B (Qwen3) |\n\nSources:\n- [Guide - arXiv 2506.13923](https://arxiv.org/abs/2506.13923)\n- [KDRL - arXiv 2506.02208](https://arxiv.org/abs/2506.02208)\n- [KDRL on HuggingFace Papers](https://huggingface.co/papers/2506.02208)\n- [SASR - arXiv 2505.13026](https://arxiv.org/abs/2505.13026)\n- [SRPO - arXiv 2604.02288](https://arxiv.org/abs/2604.02288)\n- [KDRL on Semantic Scholar](https://www.semanticscholar.org/paper/KDRL:-Post-Training-Reasoning-LLMs-via-Unified-and-Xu-Zhu/f7b400cab655e820a38348fd1c933ab3036b29f9)\n- [SRPO project page](https://srpo.pages.dev/)"
      }
    ],
    "totalDurationMs": 103252,
    "totalTokens": 22188,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 526,
      "cache_creation_input_tokens": 4184,
      "cache_read_input_tokens": 14194,
      "output_tokens": 3284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4184
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 526,
          "output_tokens": 3284,
          "cache_read_input_tokens": 14194,
          "cache_creation_input_tokens": 4184,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4184,
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
      "otherToolCount": 13
    }
  },
  "sourceToolAssistantUUID": "c0335a95-6304-4580-b51b-b595a9558441",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-27T17:52:16.968Z_

<details><summary>↩ Tool result · `toolu_0126gbKf1o1ZsLGyub4t4aK1`</summary>

```text
I now have a comprehensive picture. Here is my thorough report.

---

## Verdict: The attribution is fabricated.

Neither paper uses the phrase "most promising path" to describe hybrid scheduling of distillation and RL. The reviewer's flag is correct.

### Paper 1: arXiv 2505.14216 ("Reinforcement Learning vs. Distillation: Understanding Accuracy and Capability in LLM Reasoning")

**Searched the full HTML text** for: "promising path", "most promising", "hybrid scheduling", "hybrid", "scheduling", "alternating", "combining distillation and reinforcement", "combine distillation", "interleave", "alternate".

**Result: NONE of these terms appear anywhere in the paper.**

The paper's actual conclusion (verbatim):

> "Recent prior work has shown that RLVR improves accuracy but often fails to improve capability, whereas distillation from a strong teacher typically improves both. In this paper, we provide explanations for these two phenomena, supported by extensive empirical experiments. In summary, the RLVR training algorithm focuses on improving the accuracy of easier problems while paying less attention to difficult ones; thus, difficult problems on the whole continue to have very low success rates, and the model's overall capability remains largely unchanged. Distillation, on the other hand, is typically performed with a strong teacher model that may include knowledge not present in the base model, which can lead to capability expansion."

The paper makes **no recommendation** about combining, alternating, or hybrid-scheduling distillation and RL. It is a diagnostic/explanatory paper, not a prescriptive one.

---

### Paper 2: arXiv 2504.13837 ("Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?")

**Searched the full HTML text** for the same terms.

**Result:** The phrase "promising path" appears **once**, in the introduction, but it refers to RLVR alone (not hybrid scheduling):

> "RLVR has been considered a **promising path** toward continuously self-evolving LLMs"

The terms "most promising", "hybrid scheduling", "hybrid", "scheduling", "alternating", "combining distillation and reinforcement", "combine distillation", and "interleave" do **NOT appear anywhere** in the paper.

The paper's actual conclusion (verbatim):

> "RLVR is widely regarded as a promising approach to enable LLMs to continuously self-improve and acquire novel reasoning capabilities. In this paper, we systematically investigate the effect of current RLVR methods on the reasoning capacity boundaries of LLMs. Surprisingly, our findings reveal that current RLVR rarely elicits fundamentally new reasoning patterns; instead, the reasoning capabilities of RLVR-trained models remain bounded by those of their base models."

The paper's forward-looking suggestions focus on **improved RL paradigms** (continual scaling, multi-turn agent-environment interaction) -- not on hybrid distillation+RL scheduling.

---

### What these papers actually say about combining distillation and RL

Neither paper proposes, recommends, or even discusses combining distillation and RL in a hybrid or alternating schedule. Both papers:

1. **Compare** distillation and RLVR as separate training methods
2. **Find** that RLVR improves accuracy (pass@1) but not capability (pass@k for large k)
3. **Find** that distillation can introduce genuinely new reasoning patterns and expand capability
4. **Do not** propose any specific hybrid training recipe

---

### Is there any other credible source for the "most promising path" + "hybrid scheduling" claim?

I ran multiple web searches combining these terms. **No paper, blog post, or credible source** attributes the phrase "most promising path" to hybrid scheduling of distillation and RL in the context of LLM reasoning training. There are recent papers exploring combinations of distillation and RL (KDRL, RLKD, RLAD), but none use this specific language, and none of them are the two papers cited.

---

### Summary

| Claim | Verified? |
|---|---|
| Papers call hybrid scheduling "the most promising path" | **No -- fabricated** |
| Paper 2504.13837 uses phrase "promising path" | Yes, but about RLVR alone, not hybrid scheduling |
| Either paper discusses hybrid scheduling of distillation + RL | **No** |
| Either paper recommends combining distillation and RL | **No** |
| Any other source makes this exact claim attributed to these papers | **No** |

**The attribution is fabricated.** The two cited papers compare distillation and RL and find distillation superior for capability expansion, but neither proposes hybrid scheduling as a path forward, let alone calls it "the most promising path." This should be corrected.

agentId: a16afc4d3e685dcfc (use SendMessage with to: 'a16afc4d3e685dcfc' to continue this agent)
&lt;usage>total_tokens: 18615
tool_uses: 11
duration_ms: 95259&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "efd51568-38f8-4de1-8f62-4aa68d2060a2",
  "isSidechain": false,
  "promptId": "81938832-294a-4147-b0ab-ad0ff816bfdb",
  "type": "user",
  "uuid": "a3894f93-7ce1-4869-9be2-8492e2131b65",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify whether two specific papers actually call hybrid scheduling of distillation and RL \"the most promising path\" for LLM reasoning training. A reviewer flagged this as a fabricated attribution.\n\nThe papers in question:\n1. \"Reinforcement Learning vs. Distillation: Understanding Accuracy and Capability in LLM Reasoning\" (arXiv 2505.14216)\n2. \"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?\" (arXiv 2504.13837)\n\nPlease:\n1. Use WebFetch to read both papers:\n   - https://arxiv.org/abs/2505.14216\n   - https://arxiv.org/abs/2504.13837\n2. Search specifically for any mention of \"promising path\", \"hybrid scheduling\", \"alternating distillation and RL\", \"combining distillation and reinforcement\" in these papers\n3. Also search more broadly: \"hybrid distillation RL scheduling most promising\" to see if any other paper uses this language\n\nI need to know:\n- Do either paper actually use the phrase \"most promising path\" about hybrid scheduling?\n- What do these papers actually conclude/recommend about combining distillation and RL?\n- Is there any other credible source that makes this claim?\n\nBe thorough and honest. If the attribution is indeed fabricated, I need to know so I can correct it. Report exact quotes where possible.",
    "agentId": "a16afc4d3e685dcfc",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have a comprehensive picture. Here is my thorough report.\n\n---\n\n## Verdict: The attribution is fabricated.\n\nNeither paper uses the phrase \"most promising path\" to describe hybrid scheduling of distillation and RL. The reviewer's flag is correct.\n\n### Paper 1: arXiv 2505.14216 (\"Reinforcement Learning vs. Distillation: Understanding Accuracy and Capability in LLM Reasoning\")\n\n**Searched the full HTML text** for: \"promising path\", \"most promising\", \"hybrid scheduling\", \"hybrid\", \"scheduling\", \"alternating\", \"combining distillation and reinforcement\", \"combine distillation\", \"interleave\", \"alternate\".\n\n**Result: NONE of these terms appear anywhere in the paper.**\n\nThe paper's actual conclusion (verbatim):\n\n> \"Recent prior work has shown that RLVR improves accuracy but often fails to improve capability, whereas distillation from a strong teacher typically improves both. In this paper, we provide explanations for these two phenomena, supported by extensive empirical experiments. In summary, the RLVR training algorithm focuses on improving the accuracy of easier problems while paying less attention to difficult ones; thus, difficult problems on the whole continue to have very low success rates, and the model's overall capability remains largely unchanged. Distillation, on the other hand, is typically performed with a strong teacher model that may include knowledge not present in the base model, which can lead to capability expansion.\"\n\nThe paper makes **no recommendation** about combining, alternating, or hybrid-scheduling distillation and RL. It is a diagnostic/explanatory paper, not a prescriptive one.\n\n---\n\n### Paper 2: arXiv 2504.13837 (\"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?\")\n\n**Searched the full HTML text** for the same terms.\n\n**Result:** The phrase \"promising path\" appears **once**, in the introduction, but it refers to RLVR alone (not hybrid scheduling):\n\n> \"RLVR has been considered a **promising path** toward continuously self-evolving LLMs\"\n\nThe terms \"most promising\", \"hybrid scheduling\", \"hybrid\", \"scheduling\", \"alternating\", \"combining distillation and reinforcement\", \"combine distillation\", and \"interleave\" do **NOT appear anywhere** in the paper.\n\nThe paper's actual conclusion (verbatim):\n\n> \"RLVR is widely regarded as a promising approach to enable LLMs to continuously self-improve and acquire novel reasoning capabilities. In this paper, we systematically investigate the effect of current RLVR methods on the reasoning capacity boundaries of LLMs. Surprisingly, our findings reveal that current RLVR rarely elicits fundamentally new reasoning patterns; instead, the reasoning capabilities of RLVR-trained models remain bounded by those of their base models.\"\n\nThe paper's forward-looking suggestions focus on **improved RL paradigms** (continual scaling, multi-turn agent-environment interaction) -- not on hybrid distillation+RL scheduling.\n\n---\n\n### What these papers actually say about combining distillation and RL\n\nNeither paper proposes, recommends, or even discusses combining distillation and RL in a hybrid or alternating schedule. Both papers:\n\n1. **Compare** distillation and RLVR as separate training methods\n2. **Find** that RLVR improves accuracy (pass@1) but not capability (pass@k for large k)\n3. **Find** that distillation can introduce genuinely new reasoning patterns and expand capability\n4. **Do not** propose any specific hybrid training recipe\n\n---\n\n### Is there any other credible source for the \"most promising path\" + \"hybrid scheduling\" claim?\n\nI ran multiple web searches combining these terms. **No paper, blog post, or credible source** attributes the phrase \"most promising path\" to hybrid scheduling of distillation and RL in the context of LLM reasoning training. There are recent papers exploring combinations of distillation and RL (KDRL, RLKD, RLAD), but none use this specific language, and none of them are the two papers cited.\n\n---\n\n### Summary\n\n| Claim | Verified? |\n|---|---|\n| Papers call hybrid scheduling \"the most promising path\" | **No -- fabricated** |\n| Paper 2504.13837 uses phrase \"promising path\" | Yes, but about RLVR alone, not hybrid scheduling |\n| Either paper discusses hybrid scheduling of distillation + RL | **No** |\n| Either paper recommends combining distillation and RL | **No** |\n| Any other source makes this exact claim attributed to these papers | **No** |\n\n**The attribution is fabricated.** The two cited papers compare distillation and RL and find distillation superior for capability expansion, but neither proposes hybrid scheduling as a path forward, let alone calls it \"the most promising path.\" This should be corrected."
      }
    ],
    "totalDurationMs": 95259,
    "totalTokens": 18615,
    "totalToolUseCount": 11,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1770,
      "cache_read_input_tokens": 15716,
      "output_tokens": 1128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1770
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1128,
          "cache_read_input_tokens": 15716,
          "cache_creation_input_tokens": 1770,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1770,
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
      "otherToolCount": 11
    }
  },
  "sourceToolAssistantUUID": "efd51568-38f8-4de1-8f62-4aa68d2060a2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Frontier-Gap-Guided Scheduling of Distillation-RL Interleaving\",   \"co…",
  "leafUuid": "a3894f93-7ce1-4869-9be2-8492e2131b65",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise SEG-Schedule with HPT differentiation and signal reliability",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf"
}
```

---

### Tool result

_source line 20 · 2026-05-27T17:52:28.208Z_

<details><summary>↩ Tool result · `toolu_01CfLpeEpK4z95b2A1dRwby4`</summary>

````text
Here is my detailed research report.

---

## The Pass@k - Pass@1 Gap Diminishment During RL Training: A Comprehensive Analysis

### 1. The Core Mathematical Problem

The definitive treatment of this issue comes from Yang Yu's paper "Pass@k Metric for RLVR: A Diagnostic Tool of Exploration, But Not an Objective" (arXiv:2511.16231). The paper proves two devastating results:

**Theorem 3.1 (Gradient Collinearity):** The gradient of pass@k is strictly collinear with that of pass@1. Given `J_k(x;theta) = 1 - (1 - J_1(x;theta))^k`, applying the chain rule yields:

```
nabla J_k(x;theta) = alpha_k(x,theta) * nabla J_1(x;theta)
```

where `alpha_k(x,theta) = k * (1 - J_1(x;theta))^{k-1}`. This means pass@k optimization introduces **no new search direction** in parameter space -- it is merely a dynamic reweighting of the pass@1 gradient.

**Theorem 3.2 (Exploration Vanishing / Gap Collapse):** Define the gap as:

```
Delta_t(k) = pass@k - pass@1 = (1 - (1-p_t)^k) - p_t
```

When the policy concentrates so that `p_t = 1 - delta` for small residual exploration delta > 0, the gap reduces to `delta - delta^k`. As `delta -> 0` through training, this gap vanishes. The paper further proves that probability **monotonically concentrates** on the discovered mode via the update `p_{t+1} >= p_t`, creating a self-reinforcing collapse.

### 2. When Does This Become a Problem?

The entropy collapse literature provides precise timing. The paper "The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models" (arXiv:2505.22617) demonstrates that:

- **First 200 gradient steps (~8% of training):** 73% of total entropy is consumed and 76% of performance gains occur.
- **First 800 steps (~33% of training):** Over 93% of performance improvements and 94% of entropy losses have already happened.
- **Remaining 2/3 of training:** Yields only marginal returns.

The relationship between entropy H and performance R follows a predictable exponential: `R = -a * exp(H) + b`. The performance ceiling at H=0 is `R = b - a`, which is fully predictable from early training dynamics (within 0.9% RMSE using only the first 15% of steps).

This means for your SEG-based phase-switching signal: **the signal will be maximally informative in very early training (first ~8-33% of steps) and will progressively lose discriminative power as training proceeds.** By the time a phase switch might be most needed (mid-to-late training), the SEG signal may already be too compressed to reliably trigger switching.

### 3. The Two Failure Modes of the Reweighting Factor

The scaling factor `alpha_k = k * (1 - J_1)^{k-1}` fails in both extremes:

| Regime | J_1 value | alpha_k behavior | Practical effect |
|--------|-----------|------------------|------------------|
| Low accuracy (early/hard problems) | ~0 | approaches k (large) | But empirical gradient is zero because no correct solutions are sampled |
| High accuracy (late/easy problems) | ~1 | approaches 0 | Learning signal vanishes entirely |

This creates a fundamental problem: the pass@k signal is uninformative precisely when it matters most.

### 4. Normalized/Relative Metrics That Remain Informative

No established "normalized SEG" metric exists in the literature under that exact name, but several alternatives address the convergence problem:

**Cover@tau (arXiv:2510.08325):** Measures the fraction of problems solved where at least tau proportion of completions are correct. Unlike pass@k, it captures reliability explicitly. The paper proves that pass@k is actually "a weighted average of Cover@tau with weights from a Beta(1,k) distribution," meaning pass@k over-emphasizes lucky hits at low reliability thresholds. Cover@tau naturally separates breadth (low tau) from depth (high tau) and does not degenerate as the policy concentrates.

**Maj@k and Cons@k:** Count a problem as solved based on majority vote (>50% correct) or mode (most frequent answer) across k samples. These remain informative because they measure consistency rather than raw probability of at least one success.

**A potential "Relative SEG" you could define:** Rather than using raw `pass@k - pass@1`, consider:
- `(pass@k - pass@1) / pass@k` -- a ratio that normalizes by the upper bound
- `(pass@k - pass@1) / H(pi)` -- normalizing by current policy entropy to account for concentration
- Or use Cover@tau at multiple thresholds to get a richer signal that does not collapse

### 5. Proposed Solutions to Preserve Signal Informativeness

**A. SimKO (Simple Pass@K Optimization, arXiv:2510.14807):** Redistributes gradient updates across the top-K candidates at high-entropy tokens rather than allowing the top-1 to dominate. Implements "top-K label smoothing" for verified-correct responses. Consistently outperforms GRPO baseline on both pass@1 and pass@256.

**B. Clip-Cov and KL-Cov (arXiv:2505.22617):** Target the covariance mechanism that drives entropy collapse. Clip-Cov detaches gradients for the ~0.02% of tokens with highest covariance between log-probability and advantage. KL-Cov applies KL penalties specifically to these high-covariance tokens. Results: 2-6.4% improvement; up to 15% on hardest benchmarks (AIME). KL-Cov maintained >10x baseline entropy levels throughout training.

**C. Difficulty-Aware Entropy Regularization (arXiv:2602.22642):** Selectively sustains exploration on hard instances while permitting aggressive compression on easy ones. This is conceptually aligned with a dynamic SEG signal -- hard problems retain high SEG longer.

**D. Temperature as Meta-Policy (arXiv:2602.11779, arXiv:2602.13035):** Learns an adaptive temperature from LLM internal states via hierarchical RL, dynamically modulating exploration. Temperature scaling alone can improve base model performance by 7.3 points on average across benchmarks, suggesting that maintaining diversity is critical.

**E. DAPO and UCPO (arXiv:2605.00365):** Uniform-Correct Policy Optimization explicitly breaks RLVR's indifference to diversity by redistributing gradient signal within the verifier-accepted set, increasing coverage over correct reasoning trajectories rather than concentrating on a single dominant mode.

### 6. Recommendations for Addressing the Reviewer Concern

For your research idea using SEG as a dynamic phase-switching signal, I would recommend a multi-pronged response:

1. **Acknowledge the issue explicitly** and cite Yu (2511.16231) and the entropy mechanism paper (2505.22617).

2. **Propose a normalized variant of SEG**, such as `SEG_rel = (pass@k - pass@1) / (1 - pass@1)`, which measures the fraction of remaining "room" that multiple sampling captures. When pass@1 approaches 1, both numerator and denominator approach 0, but the ratio can remain well-defined and informative (via L'Hopital or empirical thresholding). Alternatively, entropy-normalized SEG: `SEG_norm = (pass@k - pass@1) / H(pi)`.

3. **Use Cover@tau as a complementary or replacement signal.** The breadth-depth decomposition from arXiv:2510.08325 provides richer information than a single scalar gap.

4. **Incorporate entropy monitoring** as a co-signal: if entropy drops below a threshold (empirically, this happens within the first 8-33% of training steps), the phase switch should trigger regardless of SEG value, since SEG is no longer reliable.

5. **Apply entropy-preserving techniques** (Clip-Cov, difficulty-aware regularization) during training to slow down the collapse and extend the window in which SEG remains informative.

The key argument for your rebuttal: the SEG collapse is a real phenomenon, but it is (a) predictable in its timing, (b) addressable through normalization, and (c) can be supplemented with entropy-based co-signals to maintain a reliable phase-switching mechanism throughout training.

Sources:
- [Pass@k Metric for RLVR (Yu, 2511.16231)](https://arxiv.org/abs/2511.16231)
- [The Entropy Mechanism of RL for Reasoning LLMs (2505.22617)](https://arxiv.org/abs/2505.22617)
- [Beyond Pass@k: Breadth-Depth Metrics (2510.08325)](https://arxiv.org/html/2510.08325v2)
- [SimKO: Simple Pass@K Policy Optimization (2510.14807)](https://arxiv.org/html/2510.14807v1)
- [Rethinking Entropy Regularization in Large Reasoning Models (2509.25133)](https://arxiv.org/pdf/2509.25133)
- [Difficulty-Aware Entropy Regularization (2602.22642)](https://arxiv.org/html/2602.22642)
- [Temperature as Meta-Policy (2602.11779)](https://arxiv.org/pdf/2602.11779)
- [Uniform-Correct Policy Optimization (2605.00365)](https://arxiv.org/html/2605.00365)
- [On Entropy Control in LLM-RL Algorithms (2509.03493)](https://arxiv.org/html/2509.03493v1)
- [Rediscovering Entropy Regularization with Adaptive Coefficient (2510.10959)](https://arxiv.org/html/2510.10959v1)

agentId: a7d7b2589d7a28429 (use SendMessage with to: 'a7d7b2589d7a28429' to continue this agent)
&lt;usage>total_tokens: 23827
tool_uses: 13
duration_ms: 112650&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "7f8de2fe-9dc6-4c1a-a360-95476dfe98b0",
  "isSidechain": false,
  "promptId": "81938832-294a-4147-b0ab-ad0ff816bfdb",
  "type": "user",
  "uuid": "4fdc93f3-aa45-46b0-a8df-e6bfe45dec0c",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to research the problem that the pass@k - pass@1 gap (Sampling Efficiency Gap) may diminish as RL training progresses and the policy concentrates. This is a critical issue for a research idea that uses SEG as a dynamic phase-switching signal.\n\nPlease:\n1. Use WebFetch to read arXiv 2511.16231 (the paper that reportedly shows pass@k-pass@1 gap diminishes as policy concentrates). Read https://arxiv.org/abs/2511.16231\n2. Search for \"pass@k pass@1 gap RL training policy concentration\" and \"sampling efficiency gap reinforcement learning LLM\"\n3. Search for \"normalized pass@k metric\" or \"relative sampling efficiency\" to find if anyone has proposed solutions\n4. Search for \"entropy collapse RL LLM reasoning\" since policy concentration is related to entropy collapse\n\nI need to understand:\n- Exactly how and why does the pass@k-pass@1 gap diminish during training?\n- At what point in training does this become a problem?\n- Are there normalized or relative versions of this metric that remain informative?\n- What are potential solutions (e.g., temperature scaling, entropy regularization, relative SEG)?\n\nReport in detail (500+ words). This is critical for addressing a reviewer concern about signal reliability.",
    "agentId": "a7d7b2589d7a28429",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is my detailed research report.\n\n---\n\n## The Pass@k - Pass@1 Gap Diminishment During RL Training: A Comprehensive Analysis\n\n### 1. The Core Mathematical Problem\n\nThe definitive treatment of this issue comes from Yang Yu's paper \"Pass@k Metric for RLVR: A Diagnostic Tool of Exploration, But Not an Objective\" (arXiv:2511.16231). The paper proves two devastating results:\n\n**Theorem 3.1 (Gradient Collinearity):** The gradient of pass@k is strictly collinear with that of pass@1. Given `J_k(x;theta) = 1 - (1 - J_1(x;theta))^k`, applying the chain rule yields:\n\n```\nnabla J_k(x;theta) = alpha_k(x,theta) * nabla J_1(x;theta)\n```\n\nwhere `alpha_k(x,theta) = k * (1 - J_1(x;theta))^{k-1}`. This means pass@k optimization introduces **no new search direction** in parameter space -- it is merely a dynamic reweighting of the pass@1 gradient.\n\n**Theorem 3.2 (Exploration Vanishing / Gap Collapse):** Define the gap as:\n\n```\nDelta_t(k) = pass@k - pass@1 = (1 - (1-p_t)^k) - p_t\n```\n\nWhen the policy concentrates so that `p_t = 1 - delta` for small residual exploration delta > 0, the gap reduces to `delta - delta^k`. As `delta -> 0` through training, this gap vanishes. The paper further proves that probability **monotonically concentrates** on the discovered mode via the update `p_{t+1} >= p_t`, creating a self-reinforcing collapse.\n\n### 2. When Does This Become a Problem?\n\nThe entropy collapse literature provides precise timing. The paper \"The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models\" (arXiv:2505.22617) demonstrates that:\n\n- **First 200 gradient steps (~8% of training):** 73% of total entropy is consumed and 76% of performance gains occur.\n- **First 800 steps (~33% of training):** Over 93% of performance improvements and 94% of entropy losses have already happened.\n- **Remaining 2/3 of training:** Yields only marginal returns.\n\nThe relationship between entropy H and performance R follows a predictable exponential: `R = -a * exp(H) + b`. The performance ceiling at H=0 is `R = b - a`, which is fully predictable from early training dynamics (within 0.9% RMSE using only the first 15% of steps).\n\nThis means for your SEG-based phase-switching signal: **the signal will be maximally informative in very early training (first ~8-33% of steps) and will progressively lose discriminative power as training proceeds.** By the time a phase switch might be most needed (mid-to-late training), the SEG signal may already be too compressed to reliably trigger switching.\n\n### 3. The Two Failure Modes of the Reweighting Factor\n\nThe scaling factor `alpha_k = k * (1 - J_1)^{k-1}` fails in both extremes:\n\n| Regime | J_1 value | alpha_k behavior | Practical effect |\n|--------|-----------|------------------|------------------|\n| Low accuracy (early/hard problems) | ~0 | approaches k (large) | But empirical gradient is zero because no correct solutions are sampled |\n| High accuracy (late/easy problems) | ~1 | approaches 0 | Learning signal vanishes entirely |\n\nThis creates a fundamental problem: the pass@k signal is uninformative precisely when it matters most.\n\n### 4. Normalized/Relative Metrics That Remain Informative\n\nNo established \"normalized SEG\" metric exists in the literature under that exact name, but several alternatives address the convergence problem:\n\n**Cover@tau (arXiv:2510.08325):** Measures the fraction of problems solved where at least tau proportion of completions are correct. Unlike pass@k, it captures reliability explicitly. The paper proves that pass@k is actually \"a weighted average of Cover@tau with weights from a Beta(1,k) distribution,\" meaning pass@k over-emphasizes lucky hits at low reliability thresholds. Cover@tau naturally separates breadth (low tau) from depth (high tau) and does not degenerate as the policy concentrates.\n\n**Maj@k and Cons@k:** Count a problem as solved based on majority vote (>50% correct) or mode (most frequent answer) across k samples. These remain informative because they measure consistency rather than raw probability of at least one success.\n\n**A potential \"Relative SEG\" you could define:** Rather than using raw `pass@k - pass@1`, consider:\n- `(pass@k - pass@1) / pass@k` -- a ratio that normalizes by the upper bound\n- `(pass@k - pass@1) / H(pi)` -- normalizing by current policy entropy to account for concentration\n- Or use Cover@tau at multiple thresholds to get a richer signal that does not collapse\n\n### 5. Proposed Solutions to Preserve Signal Informativeness\n\n**A. SimKO (Simple Pass@K Optimization, arXiv:2510.14807):** Redistributes gradient updates across the top-K candidates at high-entropy tokens rather than allowing the top-1 to dominate. Implements \"top-K label smoothing\" for verified-correct responses. Consistently outperforms GRPO baseline on both pass@1 and pass@256.\n\n**B. Clip-Cov and KL-Cov (arXiv:2505.22617):** Target the covariance mechanism that drives entropy collapse. Clip-Cov detaches gradients for the ~0.02% of tokens with highest covariance between log-probability and advantage. KL-Cov applies KL penalties specifically to these high-covariance tokens. Results: 2-6.4% improvement; up to 15% on hardest benchmarks (AIME). KL-Cov maintained >10x baseline entropy levels throughout training.\n\n**C. Difficulty-Aware Entropy Regularization (arXiv:2602.22642):** Selectively sustains exploration on hard instances while permitting aggressive compression on easy ones. This is conceptually aligned with a dynamic SEG signal -- hard problems retain high SEG longer.\n\n**D. Temperature as Meta-Policy (arXiv:2602.11779, arXiv:2602.13035):** Learns an adaptive temperature from LLM internal states via hierarchical RL, dynamically modulating exploration. Temperature scaling alone can improve base model performance by 7.3 points on average across benchmarks, suggesting that maintaining diversity is critical.\n\n**E. DAPO and UCPO (arXiv:2605.00365):** Uniform-Correct Policy Optimization explicitly breaks RLVR's indifference to diversity by redistributing gradient signal within the verifier-accepted set, increasing coverage over correct reasoning trajectories rather than concentrating on a single dominant mode.\n\n### 6. Recommendations for Addressing the Reviewer Concern\n\nFor your research idea using SEG as a dynamic phase-switching signal, I would recommend a multi-pronged response:\n\n1. **Acknowledge the issue explicitly** and cite Yu (2511.16231) and the entropy mechanism paper (2505.22617).\n\n2. **Propose a normalized variant of SEG**, such as `SEG_rel = (pass@k - pass@1) / (1 - pass@1)`, which measures the fraction of remaining \"room\" that multiple sampling captures. When pass@1 approaches 1, both numerator and denominator approach 0, but the ratio can remain well-defined and informative (via L'Hopital or empirical thresholding). Alternatively, entropy-normalized SEG: `SEG_norm = (pass@k - pass@1) / H(pi)`.\n\n3. **Use Cover@tau as a complementary or replacement signal.** The breadth-depth decomposition from arXiv:2510.08325 provides richer information than a single scalar gap.\n\n4. **Incorporate entropy monitoring** as a co-signal: if entropy drops below a threshold (empirically, this happens within the first 8-33% of training steps), the phase switch should trigger regardless of SEG value, since SEG is no longer reliable.\n\n5. **Apply entropy-preserving techniques** (Clip-Cov, difficulty-aware regularization) during training to slow down the collapse and extend the window in which SEG remains informative.\n\nThe key argument for your rebuttal: the SEG collapse is a real phenomenon, but it is (a) predictable in its timing, (b) addressable through normalization, and (c) can be supplemented with entropy-based co-signals to maintain a reliable phase-switching mechanism throughout training.\n\nSources:\n- [Pass@k Metric for RLVR (Yu, 2511.16231)](https://arxiv.org/abs/2511.16231)\n- [The Entropy Mechanism of RL for Reasoning LLMs (2505.22617)](https://arxiv.org/abs/2505.22617)\n- [Beyond Pass@k: Breadth-Depth Metrics (2510.08325)](https://arxiv.org/html/2510.08325v2)\n- [SimKO: Simple Pass@K Policy Optimization (2510.14807)](https://arxiv.org/html/2510.14807v1)\n- [Rethinking Entropy Regularization in Large Reasoning Models (2509.25133)](https://arxiv.org/pdf/2509.25133)\n- [Difficulty-Aware Entropy Regularization (2602.22642)](https://arxiv.org/html/2602.22642)\n- [Temperature as Meta-Policy (2602.11779)](https://arxiv.org/pdf/2602.11779)\n- [Uniform-Correct Policy Optimization (2605.00365)](https://arxiv.org/html/2605.00365)\n- [On Entropy Control in LLM-RL Algorithms (2509.03493)](https://arxiv.org/html/2509.03493v1)\n- [Rediscovering Entropy Regularization with Adaptive Coefficient (2510.10959)](https://arxiv.org/html/2510.10959v1)"
      }
    ],
    "totalDurationMs": 112650,
    "totalTokens": 23827,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3754,
      "cache_read_input_tokens": 17594,
      "output_tokens": 2478,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3754
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2478,
          "cache_read_input_tokens": 17594,
          "cache_creation_input_tokens": 3754,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3754,
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
      "otherToolCount": 13
    }
  },
  "sourceToolAssistantUUID": "7f8de2fe-9dc6-4c1a-a360-95476dfe98b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool result

_source line 21 · 2026-05-27T17:52:40.508Z_

<details><summary>↩ Tool result · `toolu_01NBAeFUWckNVR1EE2TRaZBC`</summary>

````text
I now have comprehensive information. Let me compile the detailed research report.

---

## Detailed Research Report: HPT (Hybrid Post-Training)

**Paper:** "Towards a Unified View of Large Language Model Post-Training"
**ArXiv:** 2509.04419 (September 2025, revised January 2026)
**Authors:** Xingtai Lv, Yuxin Zuo, Youbang Sun, Hongyi Liu, Yuntian Wei, Zhekai Chen, Xuekai Zhu, Kaiyan Zhang, Bingning Wang, Ning Ding, Bowen Zhou (Tsinghua University C3I group)
**Status:** Desk-rejected at ICLR 2026 (per OpenReview)
**Code:** https://github.com/TsinghuaC3I/Unify-Post-Training

---

### 1. Theoretical Foundation: The Unified Policy Gradient Estimator

HPT rests on a theoretical contribution showing that SFT and RL are not contradictory approaches but instances of a single optimization process. The authors derive a **Unified Policy Gradient Estimator (UPGE)** that decomposes into four components: a stabilization mask, a reference policy denominator, an advantage estimate, and a likelihood gradient. The common objective is:

```
J_mu(theta) = E[r(tau|q)] - mu * KL(pi_beta(.|q) || pi_theta(.|q)),  mu >= 0
```

The gradient of this objective decomposes into "a reward + trust-region term sampled from pi_theta and a data-adherence (SFT) term sampled from pi_beta." This theoretical unification is what motivates the practical HPT algorithm.

---

### 2. HPT's Switching Mechanism: Per-Question, Not Per-Phase

This is the most critical finding for your research idea revision. **HPT operates at per-question granularity, not per-phase.** For each training question `q`, the algorithm:

1. Generates `n=8` on-policy rollouts from the current model
2. Computes a performance score: `P = (1/n) * sum(v(tau_i))` where `v(tau_i) in {0, 1}` indicates whether each rollout produced a correct answer
3. Applies a **binary gate** based on threshold gamma:

```
alpha = f(P) = { 1 if P > gamma,  0 if P <= gamma }   (RL weight)
beta  = g(P) = { 1 if P <= gamma,  0 if P > gamma }   (SFT weight)
```

The combined loss is: `L = alpha * L_RL + beta * L_SFT`

The authors state: "When the model demonstrates strong capability, it is advantageous to emphasize on-policy RL to foster exploration; conversely, when the model's competence is limited, SFT should take precedence."

**Key design choice:** The gate is binary (hard switching), not a soft mixture. For any given question at any given training step, the model receives EITHER SFT signal OR RL signal, never both simultaneously. The threshold gamma is model-dependent: gamma=0 for Qwen models (SFT only when ALL 8 rollouts fail) and gamma=2/8 for LLaMA.

---

### 3. How HPT Differs from Pass@k-Based Signals

HPT uses rollout accuracy (essentially a pass@8 computation) as a **training-time routing signal**, not merely as an evaluation metric. The key distinctions:

- **Pass@k as evaluation** measures capability breadth post-training. HPT uses the same computation **during training** to decide which gradient signal to apply.
- **HPT preserves Pass@k better than pure RL.** The authors find: "HPT achieves the highest large-k Pass@k performance overall. This indicates that Hybrid Post-Training not only delivers substantial improvements in Pass@1, but also maximally preserves and enhances the model's exploratory ability." They contrast this with RLVR findings: "While RLVR training yields a significant improvement in Pass@1, it does not lead to gains in large-k Pass@k."
- **The signal is binary, not granular.** Unlike approaches that might weight by pass@k rate, HPT collapses the signal to a binary SFT-or-RL decision. This is simpler but coarser than, say, weighting the SFT loss proportionally to (1 - pass_rate).

---

### 4. Comparison to Baselines

**On Qwen2.5-Math-7B (6-benchmark average):**

| Method | Average | AIME24 |
|---|---|---|
| SFT | 44.5 | 25.1 |
| GRPO (pure RL) | 43.1 | 19.4 |
| SFT then GRPO | 46.5 | 25.7 |
| LUFFY | 49.8 | 26.1 |
| SRFT | 44.2 | 18.4 |
| **HPT** | **52.7** | **33.0** |

HPT achieves "marked improvements over existing mixed-policy approaches such as LUFFY and SRFT, with particularly notable gains of 6.9 and 14.6 points on AIME 2024, respectively."

**On weaker/smaller models**, HPT's advantage is even more pronounced:
- LLaMA3.1-8B: HPT 18.2 vs LUFFY 13.2 (average, +37%)
- Qwen2.5-Math-1.5B: HPT 41.9 vs LUFFY 34.7 (+21%)

**Out-of-distribution** (ARC-c, GPQA): HPT 62.3 vs LUFFY 60.1, showing generalization holds.

**Key mechanism difference vs. LUFFY:** LUFFY uses "fixed coefficient, a predefined schedule, a dynamic adjustment based on entropy, or a learnable parameter" whereas HPT uses "performance feedback on questions" -- i.e., LUFFY's mixing is not conditioned on per-question difficulty.

---

### 5. Ablation Findings

**Gate threshold (gamma):** On Qwen2.5-Math-1.5B, gamma=0 (SFT only when all rollouts fail) achieves the best average of 41.9, compared to gamma=1/8 (38.7) and gamma=2/8 (39.0). This means very aggressive RL usage is preferred when the model has any capability on a question.

**Off-policy RL vs SFT for low-accuracy questions:** The paper tested replacing SFT with off-policy RL for questions where rollouts fail. Result: "The SFT/ON method achieves the best average performance (41.9), outperforming both Mix/ON (40.3) and OFF/ON (38.1). This suggests that off-policy RL may not be essential, as SFT already serves effectively."

**Training dynamics (Figure 4):** HPT's SFT proportion starts high and decreases over training as the model becomes more capable. The authors note this creates "a dynamic balance between the exploration of RL and the exploitation of SFT."

---

### 6. Limitations

The paper lacks a formal limitations section, but several emerge:

1. **Binary gating is simplistic.** The authors themselves call it a "highly streamlined experimental setup." A continuous weighting by rollout accuracy might capture more nuance.

2. **Threshold requires per-model tuning.** "The optimal degree of this gating mechanism should be adjusted according to the characteristics of the base model and the specific training data employed." Gamma=0 works for Qwen but gamma=2/8 for LLaMA.

3. **Theoretical gap for offline data.** "Neither of the two approaches is entirely theoretically justified, from an RL perspective; both require a lower bound on the state-action visitation...which can not be satisfied due to the severely limited datasets in practice."

4. **Domain-limited evaluation.** All experiments are on mathematical reasoning. The authors note "multimodal post-training is a natural next step."

5. **Computational overhead not quantified.** Each training step requires n=8 rollouts for routing, but the paper does not detail wall-clock comparisons.

6. **Desk-rejected at ICLR 2026**, suggesting reviewers/editors found significant issues (though specific reviewer comments are not publicly available).

---

### 7. Key Takeaways for Your Research Idea Revision

- HPT's switching is **per-question, binary, based on rollout accuracy (pass@8 > gamma)**. It is not a phase-level switch.
- The mechanism is extremely simple: if any rollout succeeds (gamma=0), do RL; if all fail, do SFT. This simplicity is both a strength (easy to implement) and a limitation (no nuanced weighting).
- HPT does NOT use a continuous pass@k rate as a mixing weight -- it collapses to a binary decision. There is room for more sophisticated approaches.
- The idea that SFT is better for "too-hard" questions and RL for "learnable" ones is well-supported by HPT's results but not novel to HPT alone (similar intuitions appear in curriculum RL literature).
- HPT's strongest results are on small/weak models where pure RL struggles most -- this is where the SFT fallback provides the biggest lift.

Sources:
- [arXiv abstract page](https://arxiv.org/abs/2509.04419)
- [arXiv HTML full paper](https://arxiv.org/html/2509.04419)
- [arXiv PDF](https://arxiv.org/pdf/2509.04419)
- [OpenReview submission](https://openreview.net/forum?id=3UxhlRCVgr)
- [Moonlight review](https://www.themoonlight.io/en/review/towards-a-unified-view-of-large-language-model-post-training)
- [Medium summary](https://medium.com/@huguosuo/towards-a-unified-view-of-large-language-model-post-training-0ec2557fa3a4)
- [HuggingFace paper page](https://huggingface.co/papers/2509.04419)

agentId: a86d91baac7cc3ad6 (use SendMessage with to: 'a86d91baac7cc3ad6' to continue this agent)
&lt;usage>total_tokens: 21949
tool_uses: 10
duration_ms: 136394&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "8ff74c5a-8091-4143-bb31-e7923036d797",
  "isSidechain": false,
  "promptId": "81938832-294a-4147-b0ab-ad0ff816bfdb",
  "type": "user",
  "uuid": "f1208f62-76f4-4269-8137-db820aa2e143",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to deeply research the paper HPT (arXiv 2509.04419, September 2025) which reportedly performs adaptive switching between SFT and RL based on per-question rollout accuracy. This is critical for a research idea revision.\n\nPlease:\n1. Use WebFetch to read the paper at https://arxiv.org/abs/2509.04419 \n2. Also try https://arxiv.org/pdf/2509.04419 if needed\n3. Search for \"HPT adaptive switching SFT RL rollout accuracy\" and \"HPT hybrid policy training\" to find any blog posts or discussions\n\nI need to understand:\n- What exactly is HPT's switching mechanism? Is it per-sample or per-phase?\n- What metric does HPT use to decide when to do SFT vs RL?\n- How does HPT's approach differ from using a pass@k-based signal?\n- What are HPT's limitations?\n- What benchmarks does HPT evaluate on and what results does it achieve?\n\nReport your findings in detail (500+ words). Include direct quotes from the paper where possible.",
    "agentId": "a86d91baac7cc3ad6",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information. Let me compile the detailed research report.\n\n---\n\n## Detailed Research Report: HPT (Hybrid Post-Training)\n\n**Paper:** \"Towards a Unified View of Large Language Model Post-Training\"\n**ArXiv:** 2509.04419 (September 2025, revised January 2026)\n**Authors:** Xingtai Lv, Yuxin Zuo, Youbang Sun, Hongyi Liu, Yuntian Wei, Zhekai Chen, Xuekai Zhu, Kaiyan Zhang, Bingning Wang, Ning Ding, Bowen Zhou (Tsinghua University C3I group)\n**Status:** Desk-rejected at ICLR 2026 (per OpenReview)\n**Code:** https://github.com/TsinghuaC3I/Unify-Post-Training\n\n---\n\n### 1. Theoretical Foundation: The Unified Policy Gradient Estimator\n\nHPT rests on a theoretical contribution showing that SFT and RL are not contradictory approaches but instances of a single optimization process. The authors derive a **Unified Policy Gradient Estimator (UPGE)** that decomposes into four components: a stabilization mask, a reference policy denominator, an advantage estimate, and a likelihood gradient. The common objective is:\n\n```\nJ_mu(theta) = E[r(tau|q)] - mu * KL(pi_beta(.|q) || pi_theta(.|q)),  mu >= 0\n```\n\nThe gradient of this objective decomposes into \"a reward + trust-region term sampled from pi_theta and a data-adherence (SFT) term sampled from pi_beta.\" This theoretical unification is what motivates the practical HPT algorithm.\n\n---\n\n### 2. HPT's Switching Mechanism: Per-Question, Not Per-Phase\n\nThis is the most critical finding for your research idea revision. **HPT operates at per-question granularity, not per-phase.** For each training question `q`, the algorithm:\n\n1. Generates `n=8` on-policy rollouts from the current model\n2. Computes a performance score: `P = (1/n) * sum(v(tau_i))` where `v(tau_i) in {0, 1}` indicates whether each rollout produced a correct answer\n3. Applies a **binary gate** based on threshold gamma:\n\n```\nalpha = f(P) = { 1 if P > gamma,  0 if P <= gamma }   (RL weight)\nbeta  = g(P) = { 1 if P <= gamma,  0 if P > gamma }   (SFT weight)\n```\n\nThe combined loss is: `L = alpha * L_RL + beta * L_SFT`\n\nThe authors state: \"When the model demonstrates strong capability, it is advantageous to emphasize on-policy RL to foster exploration; conversely, when the model's competence is limited, SFT should take precedence.\"\n\n**Key design choice:** The gate is binary (hard switching), not a soft mixture. For any given question at any given training step, the model receives EITHER SFT signal OR RL signal, never both simultaneously. The threshold gamma is model-dependent: gamma=0 for Qwen models (SFT only when ALL 8 rollouts fail) and gamma=2/8 for LLaMA.\n\n---\n\n### 3. How HPT Differs from Pass@k-Based Signals\n\nHPT uses rollout accuracy (essentially a pass@8 computation) as a **training-time routing signal**, not merely as an evaluation metric. The key distinctions:\n\n- **Pass@k as evaluation** measures capability breadth post-training. HPT uses the same computation **during training** to decide which gradient signal to apply.\n- **HPT preserves Pass@k better than pure RL.** The authors find: \"HPT achieves the highest large-k Pass@k performance overall. This indicates that Hybrid Post-Training not only delivers substantial improvements in Pass@1, but also maximally preserves and enhances the model's exploratory ability.\" They contrast this with RLVR findings: \"While RLVR training yields a significant improvement in Pass@1, it does not lead to gains in large-k Pass@k.\"\n- **The signal is binary, not granular.** Unlike approaches that might weight by pass@k rate, HPT collapses the signal to a binary SFT-or-RL decision. This is simpler but coarser than, say, weighting the SFT loss proportionally to (1 - pass_rate).\n\n---\n\n### 4. Comparison to Baselines\n\n**On Qwen2.5-Math-7B (6-benchmark average):**\n\n| Method | Average | AIME24 |\n|---|---|---|\n| SFT | 44.5 | 25.1 |\n| GRPO (pure RL) | 43.1 | 19.4 |\n| SFT then GRPO | 46.5 | 25.7 |\n| LUFFY | 49.8 | 26.1 |\n| SRFT | 44.2 | 18.4 |\n| **HPT** | **52.7** | **33.0** |\n\nHPT achieves \"marked improvements over existing mixed-policy approaches such as LUFFY and SRFT, with particularly notable gains of 6.9 and 14.6 points on AIME 2024, respectively.\"\n\n**On weaker/smaller models**, HPT's advantage is even more pronounced:\n- LLaMA3.1-8B: HPT 18.2 vs LUFFY 13.2 (average, +37%)\n- Qwen2.5-Math-1.5B: HPT 41.9 vs LUFFY 34.7 (+21%)\n\n**Out-of-distribution** (ARC-c, GPQA): HPT 62.3 vs LUFFY 60.1, showing generalization holds.\n\n**Key mechanism difference vs. LUFFY:** LUFFY uses \"fixed coefficient, a predefined schedule, a dynamic adjustment based on entropy, or a learnable parameter\" whereas HPT uses \"performance feedback on questions\" -- i.e., LUFFY's mixing is not conditioned on per-question difficulty.\n\n---\n\n### 5. Ablation Findings\n\n**Gate threshold (gamma):** On Qwen2.5-Math-1.5B, gamma=0 (SFT only when all rollouts fail) achieves the best average of 41.9, compared to gamma=1/8 (38.7) and gamma=2/8 (39.0). This means very aggressive RL usage is preferred when the model has any capability on a question.\n\n**Off-policy RL vs SFT for low-accuracy questions:** The paper tested replacing SFT with off-policy RL for questions where rollouts fail. Result: \"The SFT/ON method achieves the best average performance (41.9), outperforming both Mix/ON (40.3) and OFF/ON (38.1). This suggests that off-policy RL may not be essential, as SFT already serves effectively.\"\n\n**Training dynamics (Figure 4):** HPT's SFT proportion starts high and decreases over training as the model becomes more capable. The authors note this creates \"a dynamic balance between the exploration of RL and the exploitation of SFT.\"\n\n---\n\n### 6. Limitations\n\nThe paper lacks a formal limitations section, but several emerge:\n\n1. **Binary gating is simplistic.** The authors themselves call it a \"highly streamlined experimental setup.\" A continuous weighting by rollout accuracy might capture more nuance.\n\n2. **Threshold requires per-model tuning.** \"The optimal degree of this gating mechanism should be adjusted according to the characteristics of the base model and the specific training data employed.\" Gamma=0 works for Qwen but gamma=2/8 for LLaMA.\n\n3. **Theoretical gap for offline data.** \"Neither of the two approaches is entirely theoretically justified, from an RL perspective; both require a lower bound on the state-action visitation...which can not be satisfied due to the severely limited datasets in practice.\"\n\n4. **Domain-limited evaluation.** All experiments are on mathematical reasoning. The authors note \"multimodal post-training is a natural next step.\"\n\n5. **Computational overhead not quantified.** Each training step requires n=8 rollouts for routing, but the paper does not detail wall-clock comparisons.\n\n6. **Desk-rejected at ICLR 2026**, suggesting reviewers/editors found significant issues (though specific reviewer comments are not publicly available).\n\n---\n\n### 7. Key Takeaways for Your Research Idea Revision\n\n- HPT's switching is **per-question, binary, based on rollout accuracy (pass@8 > gamma)**. It is not a phase-level switch.\n- The mechanism is extremely simple: if any rollout succeeds (gamma=0), do RL; if all fail, do SFT. This simplicity is both a strength (easy to implement) and a limitation (no nuanced weighting).\n- HPT does NOT use a continuous pass@k rate as a mixing weight -- it collapses to a binary decision. There is room for more sophisticated approaches.\n- The idea that SFT is better for \"too-hard\" questions and RL for \"learnable\" ones is well-supported by HPT's results but not novel to HPT alone (similar intuitions appear in curriculum RL literature).\n- HPT's strongest results are on small/weak models where pure RL struggles most -- this is where the SFT fallback provides the biggest lift.\n\nSources:\n- [arXiv abstract page](https://arxiv.org/abs/2509.04419)\n- [arXiv HTML full paper](https://arxiv.org/html/2509.04419)\n- [arXiv PDF](https://arxiv.org/pdf/2509.04419)\n- [OpenReview submission](https://openreview.net/forum?id=3UxhlRCVgr)\n- [Moonlight review](https://www.themoonlight.io/en/review/towards-a-unified-view-of-large-language-model-post-training)\n- [Medium summary](https://medium.com/@huguosuo/towards-a-unified-view-of-large-language-model-post-training-0ec2557fa3a4)\n- [HuggingFace paper page](https://huggingface.co/papers/2509.04419)"
      }
    ],
    "totalDurationMs": 136394,
    "totalTokens": 21949,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1821,
      "cache_read_input_tokens": 17632,
      "output_tokens": 2495,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1821
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2495,
          "cache_read_input_tokens": 17632,
          "cache_creation_input_tokens": 1821,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1821,
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
      "otherToolCount": 10
    }
  },
  "sourceToolAssistantUUID": "8ff74c5a-8091-4143-bb31-e7923036d797",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Frontier-Gap-Guided Scheduling of Distillation-RL Interleaving\",   \"co…",
  "leafUuid": "f1208f62-76f4-4269-8137-db820aa2e143",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise SEG-Schedule with HPT differentiation and signal reliability",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf"
}
```

---

### Tool result

_source line 24 · 2026-05-27T17:53:26.186Z_

<details><summary>↩ Tool result · `toolu_01TyccuDoB7YgqB1bGVJLtzf`</summary>

```text
I now have enough data to compile a thorough cost estimate. Here is the report:

---

## Realistic GPU Cost Estimates for Distillation & Evaluation

### 1. Teacher Model Inference Hardware Requirements

**DeepSeek-R1-0528 (671B MoE, 37B active parameters per token):**
- Minimum deployment: 8x H100 80GB (with INT4/AWQ quantization, ~400GB VRAM consumed)
- Full precision (FP8/BF16): 16x H100 (two 8-GPU nodes) recommended for production throughput
- Single-request throughput on 8xH100: ~33 output tokens/second
- Batched throughput (concurrency ~100): ~620 output tokens/second
- Peak total throughput (input+output): ~3,000 tokens/second

**Qwen3-235B-A22B (235B MoE, 22B active parameters per token):**
- FP8 deployment: 4x H100 80GB (TP4)
- BF16 deployment: 8x H100 80GB (TP8)
- Single-request throughput on 4xH100: ~45-75 output tokens/second
- Batched throughput (concurrency 32): ~1,400 total tokens/second
- Batched throughput (concurrency 384): ~4,600 total tokens/second

### 2. Estimating Distillation Data Generation Cost (~10K Problems)

**Key parameters from the DeepSeek-R1 paper and benchmarks:**
- DeepSeek used ~800K samples for their distillation dataset (600K reasoning CoT + 200K instruction)
- DeepSeek-R1-0528 averages ~23K output tokens per AIME-level reasoning problem (up from ~12K in the original R1)
- For challenging math/code problems, reasoning traces can range from 2K to 23K+ tokens

**Scenario: 10K problems with 8 rollouts each = 80K generations using DeepSeek-R1-0528 as teacher**

Assumptions:
- Average output length per generation: ~8K tokens (mix of difficulty levels; hard competition math will be ~23K, simpler problems ~2-4K)
- Average input prompt: ~500 tokens
- Using 8xH100 with batched inference at ~620 output tokens/second throughput

Total output tokens: 80,000 generations x 8,000 tokens = 640M output tokens

Time at 620 tok/s: 640,000,000 / 620 = ~1,032,000 seconds = ~287 hours of 8xH100 wall-clock time

This translates to: **287 hours x 8 GPUs = ~2,296 H100-GPU-hours**

At cloud pricing ($2.50-3.00/H100-hour on RunPod/Lambda spot-to-on-demand):
- **Cost: $5,700 - $6,900**

If using Qwen3-235B instead (4xH100 at ~1,400 tok/s batched):
- Time: 640M / 1,400 = ~457,000 sec = ~127 hours of 4xH100
- GPU-hours: 127 x 4 = ~508 H100-GPU-hours
- **Cost: $1,270 - $1,524**

Qwen3-235B is substantially cheaper due to fewer active parameters (22B vs 37B) and fewer GPUs required.

### 3. Pass@64 Evaluation Cost (8B Student Model)

**Hardware for 8B model inference:**
- 1x H100 is sufficient (the model fits easily in a single GPU)
- Throughput: ~12,500-16,200 output tokens/second (single H100, batched, vLLM/SGLang)

**MATH-500 (500 problems, pass@64 = 32,000 generations):**
- Assume average output: ~2,000 tokens per generation (8B models produce shorter reasoning traces than 671B teachers)
- Total output tokens: 32,000 x 2,000 = 64M tokens
- Time at ~14,000 tok/s: 64M / 14,000 = ~4,571 seconds = **~1.3 hours on 1x H100**
- **Cost: ~$3-4**

**AIME 2024 (30 problems, pass@64 = 1,920 generations):**
- Assume average output: ~4,000 tokens (harder problems, longer reasoning)
- Total output tokens: 1,920 x 4,000 = 7.68M tokens
- Time: 7.68M / 14,000 = ~549 seconds = **~0.15 hours on 1x H100**
- **Cost: < $1**

**Total pass@64 evaluation: ~1.5 H100-hours, cost ~$4-5**

### 4. Total Realistic Budget Summary

| Component | H100-GPU-Hours | Est. Cost (USD) |
|---|---|---|
| **Teacher inference (DeepSeek-R1-0528, 10K problems x 8 rollouts)** | ~2,300 | $5,700 - $6,900 |
| **Teacher inference (Qwen3-235B alternative)** | ~500 | $1,270 - $1,524 |
| **Pass@64 eval on MATH-500 + AIME (8B model)** | ~1.5 | $4 - $5 |
| **GRPO/RL training (8B model, veRL, 8xH100)** | ~100-200 (est.) | $250 - $600 |
| **Total with DeepSeek-R1 teacher** | **~2,400-2,500** | **$6,000 - $7,500** |
| **Total with Qwen3-235B teacher** | **~600-700** | **$1,500 - $2,100** |

### 5. Key Caveats and Cost Reduction Strategies

- **Throughput is highly sensitive to batching**: The 620 tok/s figure for DeepSeek-R1 assumes high concurrency (~100). At low concurrency (single request), you get only ~33 tok/s, which would make costs 18x higher. Efficient batching is critical.
- **Rejection sampling amplifies cost**: If you need correct solutions only (as DeepSeek did for their 600K CoT dataset), you may need 2-5x more raw generations to filter down, potentially multiplying costs by 2-5x.
- **DeepSeek-R1-0528 is verbose**: It averages ~23K tokens per AIME problem (nearly double the original R1's ~12K). This makes teacher inference from the 0528 checkpoint significantly more expensive.
- **Spot pricing can cut costs 40-60%**: H100 spot instances are available at ~$1.03-1.50/hr vs $2.50-3.00 on-demand.
- **API alternative**: Using DeepSeek's own API at ~$2.19/M output tokens (cached) would cost roughly $1,400 for 640M output tokens -- potentially cheaper and simpler than self-hosting, though rate limits may be an issue for 80K requests.
- **The pass@64 evaluation cost is negligible** compared to teacher inference -- it represents less than 0.1% of total compute.

### Sources

- [DeepSeek-R1 671B on 8xH100 Throughput Benchmarks](https://github.com/dzhsurf/deepseek-v3-r1-deploy-and-benchmarks)
- [DeepSeek-R1 Inference on ND-H100-v5 (Microsoft)](https://techcommunity.microsoft.com/blog/azurehighperformancecomputingblog/performance-analysis-of-deepseek-r1-ai-inference-using-vllm-on-nd-h100-v5/4449351)
- [Qwen3-235B-A22B Throughput on H100 (GPUStack)](https://docs.gpustack.ai/latest/performance-lab/qwen3-235b-a22b/h100/)
- [Qwen 3 SGLang Benchmarks (Baseten)](https://www.baseten.co/blog/day-zero-benchmarks-for-qwen-3-with-sglang-on-baseten/)
- [DeepSeek-R1 paper (arXiv:2501.12948)](https://arxiv.org/abs/2501.12948)
- [DeepSeek-R1-0528 on Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528)
- [DeepSeek-R1 Distillation Details (Emergent Mind)](https://www.emergentmind.com/topics/deepseek-r1-distill-model-series)
- [Deploy Qwen3 on GPU Cloud (Spheron)](https://www.spheron.network/blog/deploy-qwen3-gpu-cloud/)
- [H100 Cloud Pricing Comparison (IntuitionLabs)](https://intuitionlabs.ai/articles/h100-rental-prices-cloud-comparison)
- [GPU Cloud Pricing 2026 (Spheron)](https://www.spheron.network/blog/gpu-cloud-pricing-comparison-2026/)
- [veRL GRPO Documentation](https://verl.readthedocs.io/en/latest/algo/grpo.html)
- [Distillation with Reasoning (Fireworks AI)](https://fireworks.ai/blog/deepseek-r1-distillation-reasoning)

agentId: a85cff59bfd2d6f3e (use SendMessage with to: 'a85cff59bfd2d6f3e' to continue this agent)
&lt;usage>total_tokens: 34429
tool_uses: 26
duration_ms: 157495&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec3dbd5e-9f48-48d8-9884-21220c74a322",
  "isSidechain": false,
  "promptId": "81938832-294a-4147-b0ab-ad0ff816bfdb",
  "type": "user",
  "uuid": "d1944023-4ff3-4974-baa9-8a57b48bbb51",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to estimate realistic GPU costs for running large teacher models (DeepSeek-R1-0528 at 671B MoE, Qwen3-235B) for distillation data generation, and also the cost of pass@64 evaluation.\n\nPlease search for:\n1. \"DeepSeek-R1 inference cost GPU hours\" and \"DeepSeek-R1-0528 inference requirements\"\n2. \"Qwen3-235B inference cost\" and \"Qwen3-235B GPU requirements\"\n3. \"pass@64 evaluation cost LLM reasoning\" \n4. \"veRL framework GPU requirements\" and \"GRPO training cost 8B model\"\n5. Search for any papers or blog posts discussing the actual compute costs of distillation from large teachers\n\nAlso try WebFetch on:\n- https://arxiv.org/abs/2501.12948 (DeepSeek-R1 paper for inference details)\n- Any recent blog posts about running DeepSeek-R1 inference\n\nI need realistic estimates for:\n- How many H100-hours to generate distillation data from a 671B MoE model for ~10K problems with multiple rollouts?\n- How many H100-hours for pass@64 evaluation of an 8B model on MATH-500 and AIME?\n- What is the total realistic cost including teacher inference?\n\nReport with specific numbers where possible (300+ words).",
    "agentId": "a85cff59bfd2d6f3e",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have enough data to compile a thorough cost estimate. Here is the report:\n\n---\n\n## Realistic GPU Cost Estimates for Distillation & Evaluation\n\n### 1. Teacher Model Inference Hardware Requirements\n\n**DeepSeek-R1-0528 (671B MoE, 37B active parameters per token):**\n- Minimum deployment: 8x H100 80GB (with INT4/AWQ quantization, ~400GB VRAM consumed)\n- Full precision (FP8/BF16): 16x H100 (two 8-GPU nodes) recommended for production throughput\n- Single-request throughput on 8xH100: ~33 output tokens/second\n- Batched throughput (concurrency ~100): ~620 output tokens/second\n- Peak total throughput (input+output): ~3,000 tokens/second\n\n**Qwen3-235B-A22B (235B MoE, 22B active parameters per token):**\n- FP8 deployment: 4x H100 80GB (TP4)\n- BF16 deployment: 8x H100 80GB (TP8)\n- Single-request throughput on 4xH100: ~45-75 output tokens/second\n- Batched throughput (concurrency 32): ~1,400 total tokens/second\n- Batched throughput (concurrency 384): ~4,600 total tokens/second\n\n### 2. Estimating Distillation Data Generation Cost (~10K Problems)\n\n**Key parameters from the DeepSeek-R1 paper and benchmarks:**\n- DeepSeek used ~800K samples for their distillation dataset (600K reasoning CoT + 200K instruction)\n- DeepSeek-R1-0528 averages ~23K output tokens per AIME-level reasoning problem (up from ~12K in the original R1)\n- For challenging math/code problems, reasoning traces can range from 2K to 23K+ tokens\n\n**Scenario: 10K problems with 8 rollouts each = 80K generations using DeepSeek-R1-0528 as teacher**\n\nAssumptions:\n- Average output length per generation: ~8K tokens (mix of difficulty levels; hard competition math will be ~23K, simpler problems ~2-4K)\n- Average input prompt: ~500 tokens\n- Using 8xH100 with batched inference at ~620 output tokens/second throughput\n\nTotal output tokens: 80,000 generations x 8,000 tokens = 640M output tokens\n\nTime at 620 tok/s: 640,000,000 / 620 = ~1,032,000 seconds = ~287 hours of 8xH100 wall-clock time\n\nThis translates to: **287 hours x 8 GPUs = ~2,296 H100-GPU-hours**\n\nAt cloud pricing ($2.50-3.00/H100-hour on RunPod/Lambda spot-to-on-demand):\n- **Cost: $5,700 - $6,900**\n\nIf using Qwen3-235B instead (4xH100 at ~1,400 tok/s batched):\n- Time: 640M / 1,400 = ~457,000 sec = ~127 hours of 4xH100\n- GPU-hours: 127 x 4 = ~508 H100-GPU-hours\n- **Cost: $1,270 - $1,524**\n\nQwen3-235B is substantially cheaper due to fewer active parameters (22B vs 37B) and fewer GPUs required.\n\n### 3. Pass@64 Evaluation Cost (8B Student Model)\n\n**Hardware for 8B model inference:**\n- 1x H100 is sufficient (the model fits easily in a single GPU)\n- Throughput: ~12,500-16,200 output tokens/second (single H100, batched, vLLM/SGLang)\n\n**MATH-500 (500 problems, pass@64 = 32,000 generations):**\n- Assume average output: ~2,000 tokens per generation (8B models produce shorter reasoning traces than 671B teachers)\n- Total output tokens: 32,000 x 2,000 = 64M tokens\n- Time at ~14,000 tok/s: 64M / 14,000 = ~4,571 seconds = **~1.3 hours on 1x H100**\n- **Cost: ~$3-4**\n\n**AIME 2024 (30 problems, pass@64 = 1,920 generations):**\n- Assume average output: ~4,000 tokens (harder problems, longer reasoning)\n- Total output tokens: 1,920 x 4,000 = 7.68M tokens\n- Time: 7.68M / 14,000 = ~549 seconds = **~0.15 hours on 1x H100**\n- **Cost: < $1**\n\n**Total pass@64 evaluation: ~1.5 H100-hours, cost ~$4-5**\n\n### 4. Total Realistic Budget Summary\n\n| Component | H100-GPU-Hours | Est. Cost (USD) |\n|---|---|---|\n| **Teacher inference (DeepSeek-R1-0528, 10K problems x 8 rollouts)** | ~2,300 | $5,700 - $6,900 |\n| **Teacher inference (Qwen3-235B alternative)** | ~500 | $1,270 - $1,524 |\n| **Pass@64 eval on MATH-500 + AIME (8B model)** | ~1.5 | $4 - $5 |\n| **GRPO/RL training (8B model, veRL, 8xH100)** | ~100-200 (est.) | $250 - $600 |\n| **Total with DeepSeek-R1 teacher** | **~2,400-2,500** | **$6,000 - $7,500** |\n| **Total with Qwen3-235B teacher** | **~600-700** | **$1,500 - $2,100** |\n\n### 5. Key Caveats and Cost Reduction Strategies\n\n- **Throughput is highly sensitive to batching**: The 620 tok/s figure for DeepSeek-R1 assumes high concurrency (~100). At low concurrency (single request), you get only ~33 tok/s, which would make costs 18x higher. Efficient batching is critical.\n- **Rejection sampling amplifies cost**: If you need correct solutions only (as DeepSeek did for their 600K CoT dataset), you may need 2-5x more raw generations to filter down, potentially multiplying costs by 2-5x.\n- **DeepSeek-R1-0528 is verbose**: It averages ~23K tokens per AIME problem (nearly double the original R1's ~12K). This makes teacher inference from the 0528 checkpoint significantly more expensive.\n- **Spot pricing can cut costs 40-60%**: H100 spot instances are available at ~$1.03-1.50/hr vs $2.50-3.00 on-demand.\n- **API alternative**: Using DeepSeek's own API at ~$2.19/M output tokens (cached) would cost roughly $1,400 for 640M output tokens -- potentially cheaper and simpler than self-hosting, though rate limits may be an issue for 80K requests.\n- **The pass@64 evaluation cost is negligible** compared to teacher inference -- it represents less than 0.1% of total compute.\n\n### Sources\n\n- [DeepSeek-R1 671B on 8xH100 Throughput Benchmarks](https://github.com/dzhsurf/deepseek-v3-r1-deploy-and-benchmarks)\n- [DeepSeek-R1 Inference on ND-H100-v5 (Microsoft)](https://techcommunity.microsoft.com/blog/azurehighperformancecomputingblog/performance-analysis-of-deepseek-r1-ai-inference-using-vllm-on-nd-h100-v5/4449351)\n- [Qwen3-235B-A22B Throughput on H100 (GPUStack)](https://docs.gpustack.ai/latest/performance-lab/qwen3-235b-a22b/h100/)\n- [Qwen 3 SGLang Benchmarks (Baseten)](https://www.baseten.co/blog/day-zero-benchmarks-for-qwen-3-with-sglang-on-baseten/)\n- [DeepSeek-R1 paper (arXiv:2501.12948)](https://arxiv.org/abs/2501.12948)\n- [DeepSeek-R1-0528 on Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528)\n- [DeepSeek-R1 Distillation Details (Emergent Mind)](https://www.emergentmind.com/topics/deepseek-r1-distill-model-series)\n- [Deploy Qwen3 on GPU Cloud (Spheron)](https://www.spheron.network/blog/deploy-qwen3-gpu-cloud/)\n- [H100 Cloud Pricing Comparison (IntuitionLabs)](https://intuitionlabs.ai/articles/h100-rental-prices-cloud-comparison)\n- [GPU Cloud Pricing 2026 (Spheron)](https://www.spheron.network/blog/gpu-cloud-pricing-comparison-2026/)\n- [veRL GRPO Documentation](https://verl.readthedocs.io/en/latest/algo/grpo.html)\n- [Distillation with Reasoning (Fireworks AI)](https://fireworks.ai/blog/deepseek-r1-distillation-reasoning)"
      }
    ],
    "totalDurationMs": 157495,
    "totalTokens": 34429,
    "totalToolUseCount": 26,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3701,
      "cache_read_input_tokens": 28319,
      "output_tokens": 2408,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3701
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2408,
          "cache_read_input_tokens": 28319,
          "cache_creation_input_tokens": 3701,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3701,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 1,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 25
    }
  },
  "sourceToolAssistantUUID": "ec3dbd5e-9f48-48d8-9884-21220c74a322",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-27T17:54:05.744Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive research on all the reviewer issues. Let me synthesize the findings and revise the research idea:

## Key Findings Summary:

### 1. Fabricated Attribution
Confirmed fabricated. Neither paper uses "most promising path" about hybrid scheduling. Paper 2504.13837 uses "promising path" about RLVR alone. Neither paper proposes combining distillation and RL.

### 2. HPT (2509.04419)
- Per-question binary switching based on rollout accuracy (pass@8 > gamma)


- If any rollout succeeds, do RL; if all fail, do SFT
- Results: 52.7% average on 6 benchmarks (Qwen2.5-Math-7B), 33.0% on AIME24
- Desk-rejected at ICLR 2026
- Key limitation: binary gating is simplistic, threshold requires per-model tuning
- **Difference from SEG-Schedule**: HPT is per-sample routing, not phase-level switching; uses binary pass@8 accuracy, not pass@k gap

### 3. Guide (2506.13923)
- Uses hints during RL to expand exploration, with off-policy correction

Most of RLVR's gains stem from self-distillation rather than actual capability improvements. KDRL takes a different approach by combining reverse KL distillation with GRPO in a single policy gradient framework, achieving 57.2% average and 42.9% on AIME24. SASR is conceptually closest to SEG-Schedule—it monitors gradient norms of KL divergence to dynamically interleave SFT and RL, though it operates at smaller scales and uses a different switching signal.

SRPO routes samples based on correctness: successful ones go to GRPO while failures use self-distillation instead of traditional teacher distillation. The vanishing signal problem in SEG is well-documented—pass@k gradients become collinear with pass@1 as the policy concentrates, with entropy collapsing in the first 8-33% of training. Normalized SEG, Cover@tau, and entropy-based co-signals can mitigate this, though Clip-Cov and KL-Cov help slow the entropy decay. For practical implementation, teacher inference costs vary significantly: DeepSeek-R1-0528 requires roughly 2,300 H100-GPU-hours for 10K problems with 8 rollouts, while Qwen3-235B is more efficient at around 500 H100-GPU-hours, with pass@64 evaluation adding another 1.5 H100-GPU-hours.

The total cost picture is substantially higher than initially estimated—DeepSeek brings the total to 2,400-2,500 H100-hours ($6,000-7,500) while Qwen3-235B lands at 600-700 H100-hours ($1,500-2,100). Looking back at the reviewer feedback, there are some fundamental concerns: SEG's mathematical foundation is shaky since the gradient signal is collinear with pass@1 and vanishes as training succeeds, which challenges the core contribution. Additionally, HPT already handles metric-based adaptive switching at the per-sample level with simpler metrics, and SASR uses gradient-norm-based interleaving, so the novelty space is getting crowded.

This calls for a substantial rethinking rather than surface-level fixes. I need to reframe the motivation as our own observation instead of relying on attribution, position HPT and SASR as clear predecessors with explicit differentiation, and replace the raw SEG signal with something more robust like entropy-normalized SEG or a multi-signal combination. I should also dial back the "principled framework" language to "diagnostic-guided heuristic," add HPT as a primary baseline with ablations comparing SEG against its rollout accuracy, include realistic cost accounting for teacher inference, expand the related work section, and address the remaining gaps in the paper.

The core viability hinges on solving the SEG vanishing signal problem. I'm considering normalized SEG that measures the fraction of improvement room covered by sampling, entropy as a co-signal to trigger distillation when it drops, or Cover@tau as a richer alternative. Testing these signals on held-out problems of varying difficulty could show whether harder problems retain the signal longer. The approach remains salvageable with these modifications, particularly by moving toward a multi-signal phase-switching criterion rather than relying on SEG alone.

Now I'm thinking through how to position this theoretically—showing why phase-level switching outperforms per-sample routing like HPT, and including a direct comparison to make that distinction clear.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1944023-4ff3-4974-baa9-8a57b48bbb51",
  "isSidechain": false,
  "requestId": "req_011CbTW1W1UcEx5qWabAnCRh",
  "type": "assistant",
  "uuid": "fe9e6b72-0752-4fb9-a5a0-abc2b75e4b93",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SmXyihJHVJUzuzQHUzmuML",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14498,
      "cache_read_input_tokens": 15840,
      "output_tokens": 7082,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14498,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7082,
          "cache_read_input_tokens": 15840,
          "cache_creation_input_tokens": 14498,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14498
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

_source line 26 · 2026-05-27T17:55:59.380Z_

Now I have comprehensive research findings from all five agents. Let me synthesize the key insights before drafting the revision:

**Key findings:**
1. **Attribution is confirmed fabricated** — neither paper uses "most promising path" about hybrid scheduling
2. **HPT** does per-question binary switching (pass@8 > γ → RL, else SFT); desk-rejected at ICLR 2026; key competitor but fundamentally different granularity
3. **SASR** is also highly relevant — uses gradient-norm-based adaptive SFT/RL interleaving (most similar in spirit)
4. **KDRL** unifies KD + GRPO in a single objective; **Guide** uses hints to expand exploration; **SRPO** routes by sample correctness
5. **SEG vanishing signal is a real mathematical problem** — Yu (2511.16231) proves pass@k gradient is collinear with pass@1, gap collapses as policy concentrates; 73% of entropy consumed in first 200 steps
6. **Teacher inference costs are massive** — DeepSeek-R1-0528 alone costs ~2,300 H100-hours for 10K problems × 8 rollouts; original estimates were 2-3x underestimated

This warrants a **major revision**. Let me now produce the complete revised idea:

```json
{
  "change_type": "major",
  "title": "Entropy-Normalized Frontier Gap as a Diagnostic for Scheduling Distillation-RL Alternation",
  "core_problem": "RLVR improves sampling efficiency (pass@1) but cannot expand the reasoning frontier (pass@k), while distillation expands the frontier but is limited by teacher quality. Existing hybrid methods either mix both signals in a single loss (KDRL, RLAD, Self-Distilled RLVR), route per-sample based on binary rollout accuracy (HPT), or use gradient-norm heuristics for scheduling (SASR). None provide an explicit, interpretable diagnostic of the model's training state that separates the 'frontier expansion needed' regime from the 'efficiency harvesting needed' regime.",
  "opportunity": "The raw Sampling Efficiency Gap (SEG = pass@k − pass@1) captures this regime distinction intuitively but suffers from a known mathematical limitation: as RL training concentrates the policy, both pass@k and pass@1 converge and the gap vanishes (Yu, 2511.16231), losing discriminative power precisely when switching decisions matter most. We propose Entropy-Normalized SEG (EN-SEG), which divides the raw gap by policy entropy, preserving the signal throughout training. Combined with a difficulty-stratified evaluation protocol, EN-SEG provides a richer, more robust phase-switching criterion than HPT's binary rollout accuracy or SASR's implicit gradient-norm monitoring. This enables principled phase-level alternation between distillation and RL — a granularity level that no existing method addresses with an explicit diagnostic.",
  "landscape": "The 'RL vs. Distillation' paper (arXiv 2505.14216) established that RLVR enhances pass@1 at the cost of pass@k on hard problems, while distillation with new knowledge expands capability. The 'Does RL Really Incentivize Reasoning' paper (arXiv 2504.13837) showed RLVR rarely elicits fundamentally new reasoning patterns beyond the base model's frontier. ProRL (NeurIPS 2025) demonstrated prolonged RL with KL reset can find novel strategies. SIRI (arXiv 2509.25176) achieves improvement via iterative length compression-expansion cycles but uses a fixed schedule without diagnostic signals. HPT (arXiv 2509.04419) provides a Unified Policy Gradient Estimator showing SFT and RL are instances of a single optimization, and implements per-question binary switching based on rollout accuracy (pass@8 > γ), achieving 52.7% average on Qwen2.5-Math-7B — but its binary gate is coarse and operates at per-sample granularity without modeling phase-level training dynamics. SASR (arXiv 2505.13026) uses gradient-norm monitoring of KL divergence to dynamically balance SFT and RL, but the signal is implicit (not directly interpretable as a frontier diagnostic) and was only tested at 0.5B-1.5B scale. KDRL (arXiv 2506.02208) unifies teacher KD and GRPO in a single reverse-KL policy gradient objective, achieving 42.9% on AIME24. Guide (arXiv 2506.13923) injects natural-language hints during RL to expand exploration, with off-policy correction for unguided generalization; it finds ~75% of RLVR gains come from self-distillation (pass@k → pass@1). SRPO (arXiv 2604.02288) routes correct samples to GRPO and failed samples to self-distillation with entropy-aware weighting. Self-Distilled RLVR (arXiv 2604.03128) combines RL direction with distillation magnitude in a single phase. RLAD (arXiv 2602.22495) performs selective imitation during RL via Trust Region Ratio Distillation. HDPO (arXiv 2603.23871) augments GRPO with privileged self-distillation on zero-solve problems. REOPOLD (arXiv 2603.11137) interprets on-policy distillation as policy optimization with an exploration-to-refinement schedule. PACED (arXiv 2603.11178) adapts distillation difficulty at the frontier of student competence. Yu (arXiv 2511.16231) proves that pass@k gradients are collinear with pass@1 and the gap vanishes as policy concentrates, establishing the mathematical challenge our EN-SEG metric addresses. The entropy mechanism paper (arXiv 2505.22617) shows 73% of entropy is consumed within the first ~200 gradient steps, motivating entropy normalization. Cover@tau (arXiv 2510.08325) provides a breadth-depth decomposition of pass@k that we use as a complementary signal. No existing work combines an explicit, entropy-normalized frontier gap diagnostic with phase-level distillation-RL alternation.",
  "inspired_by": "field_gaps['Robust diagnostic for phase-level distillation-RL scheduling'] + critique_of[HPT's binary per-sample routing and SASR's implicit gradient-norm signal] + mathematical_foundation[Yu's pass@k gradient collinearity theorem motivating entropy normalization] + pattern['Diagnostic-First Method Design']",
  "approach": "Define Entropy-Normalized SEG (EN-SEG) as the phase-switching diagnostic. Raw SEG = pass@k − pass@1 evaluated on a held-out validation set with k=64; EN-SEG = SEG / H(π), where H(π) is the policy's output entropy estimated from the same rollouts. Additionally, stratify the held-out set into difficulty tiers (based on historical solve rates) and compute per-tier EN-SEG, since hard problems retain signal longer. Start from DeepSeek-R1-Distill-Qwen3-8B (already frontier-expanded via initial distillation). Run the following spiral: (1) Monitor EN-SEG every 100 training steps (reduced from 50 to manage evaluation cost) on a compact diagnostic set (200 problems stratified by difficulty, pass@32 instead of pass@64 to cut eval cost by 2×). (2) When EN-SEG exceeds τ_high (large untapped potential relative to current entropy), switch to GRPO-based RLVR with entropy regularization (KL-Cov from arXiv 2505.22617) to harvest efficiency while preserving exploration. (3) When EN-SEG drops below τ_low on hard-tier problems and pass@k growth stalls, switch to on-policy distillation from Qwen3-235B-A22B (chosen over DeepSeek-R1-0528 for 4× lower inference cost) to expand the frontier. (4) As a co-signal, if policy entropy drops below an absolute floor ε_H, trigger distillation regardless of EN-SEG to prevent premature convergence. Implement this as a controller atop the veRL framework. Key ablations: (a) EN-SEG vs. raw SEG vs. HPT's rollout-accuracy criterion vs. SASR's gradient-norm signal — to justify the metric; (b) phase-level switching vs. per-sample routing (HPT-style) vs. single-phase mixing (KDRL-style) — to justify the scheduling granularity; (c) τ sensitivity analysis with automated grid search; (d) contribution of entropy co-signal and difficulty stratification. Compare against: HPT (per-sample switching), KDRL (single-phase unified), SASR (gradient-norm switching), SIRI (fixed-schedule alternation), pure RLVR (GRPO), pure distillation, and RLAD (selective imitation). Evaluate on AIME 2024, MATH-500, and LiveCodeBench, reporting pass@1, pass@32, Cover@0.5, and per-difficulty breakdowns.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "2800-3500 H100-hours breakdown: teacher inference from Qwen3-235B-A22B (~600 H100-hours for 10K problems × 8 rollouts across spiral cycles), GRPO training of 8B student (~400 H100-hours for 5 cycles × 3 seeds), pass@32 evaluation (~50 H100-hours for monitoring every 100 steps across all runs), baseline reproduction (~800 H100-hours for HPT, KDRL, SASR, SIRI, pure RL, pure distillation), ablations (~600 H100-hours for metric comparisons, threshold sweeps, entropy co-signal ablation)",
      "timeline": "16-18 weeks (4 weeks implementation including veRL controller + evaluation pipeline, 8-10 weeks experiments, 4 weeks analysis and writing)",
      "estimated_gpu_cost": "$5,600-7,000 at $2/H100-hr spot pricing"
    },
    "human_in_loop": {
      "gpu_hours": "2200-2800 H100-hours (Claude assists with veRL integration, automated sweep design, and early stopping of poor configs)",
      "timeline": "12-14 weeks (3 weeks implementation with Claude pair-programming, 6-7 weeks experiments, 3-4 weeks writing)",
      "claude_api_cost": "$350-500 (code generation, experiment log analysis, paper drafting)",
      "estimated_gpu_cost": "$4,400-5,600 at $2/H100-hr spot pricing"
    },
    "auto_research": {
      "gpu_hours": "1800-2200 H100-hours (automated scheduling minimizes idle time; adaptive sweep halts poor configs early; parallel baseline runs)",
      "timeline": "8-10 weeks (1-2 weeks scaffold setup, 5-6 weeks automated runs, 2 weeks paper generation)",
      "claude_api_cost": "$700-1000 (end-to-end pipeline orchestration, automated ablation analysis, draft writing)",
      "estimated_gpu_cost": "$3,600-4,400 at $2/H100-hr spot pricing",
      "speed_bottleneck": "Teacher inference from Qwen3-235B-A22B requires 4×H100 per batch; pass@32 evaluation on the compact 200-problem diagnostic set takes ~15 min per checkpoint on 1×H100, which is tractable at 100-step intervals"
    }
  },
  "target_venues": [
    "AAAI 2027 (full paper deadline: July 28, 2026)",
    "ICLR 2027 (expected deadline: ~Sep-Oct 2026)",
    "ARR July 2026 cycle (~July 15, 2026) for commitment to NAACL 2027 or EMNLP 2027"
  ],
  "level": "solid",
  "key_references": [
    "Reinforcement Learning vs. Distillation: Understanding Accuracy and Capability in LLM Reasoning (arXiv 2505.14216, 2025)",
    "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? (arXiv 2504.13837, 2025)",
    "ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models (NeurIPS 2025)",
    "SIRI: Scaling Iterative Reinforcement Learning with Interleaved Compression (arXiv 2509.25176, 2025)",
    "HPT: Towards a Unified View of Large Language Model Post-Training (arXiv 2509.04419, 2025)",
    "SASR: Step-wise Adaptive Integration of Supervised Fine-tuning and Reinforcement Learning (arXiv 2505.13026, 2025)",
    "Pass@k Metric for RLVR: A Diagnostic Tool of Exploration, But Not an Objective (arXiv 2511.16231, 2025)",
    "The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models (arXiv 2505.22617, 2025)",
    "Beyond Pass@k: Breadth-Depth Metrics for LLM Reasoning — Cover@tau (arXiv 2510.08325, 2025)",
    "Guide: Adaptive Guidance Accelerates Reinforcement Learning of Reasoning Models (arXiv 2506.13923, 2025)",
    "KDRL: Post-Training Reasoning LLMs via Unified Knowledge Distillation and Reinforcement Learning (arXiv 2506.02208, 2025)",
    "SRPO: Unifying Group-Relative and Self-Distillation Policy Optimization via Sample Routing (arXiv 2604.02288, 2026)",
    "Self-Distilled RLVR (arXiv 2604.03128, 2026)",
    "RLAD: Reinforcement-aware Knowledge Distillation for LLM Reasoning (arXiv 2602.22495, 2026)",
    "HDPO: Hybrid Distillation Policy Optimization via Privileged Self-Distillation (arXiv 2603.23871, 2026)",
    "REOPOLD: Scaling Reasoning Efficiently via Relaxed On-Policy Distillation (arXiv 2603.11137, 2026)",
    "PACED: Distillation at the Frontier of Student Competence (arXiv 2603.11178, 2026)",
    "A Survey of On-Policy Distillation for Large Language Models (arXiv 2604.00626, 2026)"
  ],
  "description": "We propose EN-SEG-Schedule, a diagnostic-guided heuristic for dynamically alternating between knowledge distillation and RLVR during LLM reasoning post-training. Our key observation is that the Sampling Efficiency Gap (SEG = pass@k − pass@1) naturally separates two training regimes — efficiency harvesting (large SEG) and frontier expansion (small SEG with stagnating pass@k) — but raw SEG suffers from a known mathematical limitation: as RL concentrates the policy, the gap vanishes regardless of the model's actual training state (Yu, 2511.16231). We address this with Entropy-Normalized SEG (EN-SEG = SEG / H(π)), which preserves discriminative power throughout training by accounting for policy concentration, and complement it with difficulty-stratified monitoring and an entropy floor co-signal. Unlike HPT's per-sample binary routing based on rollout accuracy, EN-SEG-Schedule operates at the phase level, enabling bulk training mode switches that avoid the overhead of per-question rollout evaluation during training. Unlike KDRL's single-phase unified objective, discrete phase switching allows each phase to use its optimal hyperparameters (e.g., higher learning rate for RL, lower for distillation). Unlike SASR's implicit gradient-norm criterion, EN-SEG provides a directly interpretable diagnostic of frontier state. We implement a threshold-based controller atop veRL that monitors EN-SEG every 100 steps on a compact 200-problem stratified diagnostic set using pass@32, triggering phase switches between GRPO with entropy regularization and on-policy distillation from Qwen3-235B-A22B. We include systematic ablations comparing EN-SEG against HPT's rollout accuracy, SASR's gradient norm, and raw SEG, as well as phase-level vs. per-sample switching granularity, to justify each design choice.",
  "project_name": "en_seg_schedule",
  "source": "web_research",
  "reviewer_response": {
    "issue_1_fabricated_attribution": "FIXED. Removed the fabricated claim that either arXiv 2505.14216 or 2504.13837 calls hybrid scheduling 'the most promising path.' Verified by reading both papers in full: neither discusses or recommends hybrid distillation-RL scheduling. The motivation is now stated as our own observation grounded in the empirical findings of these papers (RLVR improves pass@1 but not pass@k; distillation expands capability but is teacher-bounded).",
    "issue_2_missing_HPT": "FIXED. HPT (arXiv 2509.04419) is now cited as a primary competitor and baseline. Clear differentiation: HPT operates at per-question granularity with binary routing (pass@8 > γ → RL, else SFT), while EN-SEG-Schedule operates at the phase level with a continuous, entropy-normalized diagnostic. HPT's binary gate is coarse (threshold requires per-model tuning, γ=0 for Qwen vs γ=2/8 for LLaMA) and does not model the distinction between 'frontier exhaustion' and 'efficiency gap.' We include an explicit ablation comparing EN-SEG vs HPT's rollout-accuracy criterion.",
    "issue_3_missing_related_work": "FIXED. Added Guide (2506.13923, hint-guided exploration with off-policy correction), KDRL (2506.02208, unified KD+GRPO via reverse KL), SASR (2505.13026, gradient-norm-based adaptive SFT/RL interleaving — identified as a key predecessor for adaptive scheduling), and SRPO (2604.02288, sample routing between GRPO and self-distillation with entropy-aware weighting). Each is differentiated in the landscape and approach sections.",
    "issue_4_SEG_vanishing_signal": "FIXED with major methodological change. Acknowledged Yu (2511.16231) proving pass@k gradient collinearity and gap collapse, and the entropy mechanism paper (2505.22617) showing 73% of entropy consumed in first ~200 steps. Proposed Entropy-Normalized SEG (EN-SEG = SEG/H(π)) as the primary metric, which preserves discriminative power by normalizing for policy concentration. Added three complementary robustness mechanisms: (a) difficulty-stratified monitoring (hard problems retain signal longer), (b) entropy floor co-signal (triggers distillation when entropy drops below absolute threshold regardless of EN-SEG), (c) pass@32 on compact diagnostic set (200 problems) to make evaluation tractable. This transforms the core metric from raw SEG to EN-SEG, which is the primary reason for the 'major' revision designation.",
    "issue_5_threshold_sensitivity": "FIXED. Toned down 'principled framework' to 'diagnostic-guided heuristic.' Added explicit ablation for τ sensitivity analysis with automated grid search. Acknowledged that τ values will be task-dependent and included cross-task transfer analysis in the ablation plan. The multi-signal approach (EN-SEG + entropy floor + difficulty stratification) reduces sensitivity to any single threshold.",
    "issue_6_cost_underestimate": "FIXED. Completely revised resource estimates based on detailed cost modeling. Teacher inference from Qwen3-235B-A22B: ~600 H100-hours (4×H100 at ~1,400 tok/s batched). Switched from DeepSeek-R1-0528 (which would cost ~2,300 H100-hours due to 671B MoE requiring 8×H100) to Qwen3-235B-A22B as the default teacher (4× cheaper). Reduced evaluation overhead by using pass@32 instead of pass@64 and a compact 200-problem diagnostic set instead of full MATH-500. Total estimates now 2-3× higher than original, reflecting realistic teacher inference costs.",
    "issue_7_novelty_overclaimed": "FIXED. Removed 'first method to use a pass@k-derived signal' claim. Novelty is now positioned as: (a) EN-SEG as a mathematically motivated improvement over raw SEG that addresses the known collinearity/collapse problem, (b) phase-level scheduling (vs HPT's per-sample, KDRL's single-phase, SASR's implicit gradient-norm), (c) multi-signal diagnostic combining EN-SEG, entropy floor, and difficulty stratification. The contribution is the diagnostic framework for scheduling granularity, not the bare idea of metric-based switching."
  }
}
```

## Summary of Changes (Major Revision)

### What changed and why:

1. **Fabricated attribution removed** — Verified both papers in full; neither mentions hybrid scheduling. Motivation reframed as our own observation.

2. **HPT elevated to primary competitor** — Detailed differentiation: HPT does per-sample binary routing (pass@8 > γ), we do phase-level switching with a continuous normalized metric. Added HPT as a required baseline with explicit ablation.

3. **Four missing papers added** — Guide (hint-guided exploration), KDRL (unified KD+GRPO objective), SASR (gradient-norm scheduling — most similar predecessor), SRPO (sample routing with entropy-aware weighting).

4. **Core metric fundamentally revised** — Raw SEG replaced with **Entropy-Normalized SEG (EN-SEG = SEG/H(π))**. This addresses the mathematically proven problem that raw pass@k−pass@1 gap collapses as policy concentrates (Yu, 2511.16231). Added three robustness mechanisms: difficulty stratification, entropy floor co-signal, and compact diagnostic set.

5. **Claims toned down** — "Principled framework" → "diagnostic-guided heuristic." Removed "first method" novelty claim. Novelty repositioned around EN-SEG's mathematical motivation and phase-level scheduling granularity.

6. **Costs revised 2-3× upward** — Switched default teacher from DeepSeek-R1-0528 (8×H100, ~2,300 GPU-hours for inference alone) to Qwen3-235B-A22B (4×H100, ~600 GPU-hours). Reduced eval overhead via pass@32 on 200-problem subset. Manual estimate: $5,600-7,000 (was $2,400-3,000).

7. **Evaluation protocol strengthened** — Added Cover@0.5 and per-difficulty breakdowns alongside pass@1 and pass@32. Added systematic ablations comparing EN-SEG vs HPT's rollout accuracy vs SASR's gradient norm vs raw SEG.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe9e6b72-0752-4fb9-a5a0-abc2b75e4b93",
  "isSidechain": false,
  "requestId": "req_011CbTW1W1UcEx5qWabAnCRh",
  "type": "assistant",
  "uuid": "82d388f8-5ccf-453a-8e7d-84c835007de0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SmXyihJHVJUzuzQHUzmuML",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14498,
      "cache_read_input_tokens": 15840,
      "output_tokens": 7082,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14498,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7082,
          "cache_read_input_tokens": 15840,
          "cache_creation_input_tokens": 14498,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14498
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

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Frontier-Gap-Guided Scheduling of Distillation-RL Interleaving\",   \"co…",
  "leafUuid": "82d388f8-5ccf-453a-8e7d-84c835007de0",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise SEG-Schedule with HPT differentiation and signal reliability",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Frontier-Gap-Guided Scheduling of Distillation-RL Interleaving\",   \"co…",
  "leafUuid": "82d388f8-5ccf-453a-8e7d-84c835007de0",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise SEG-Schedule with HPT differentiation and signal reliability",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf"
}
```

---
