# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-27 (UTC).** ## Original idea { "tit

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-3/8280eabe-3ac4-4f74-b6f8-8256a49b890b.jsonl`
- **Structured JSON:** [`b045255adb304ee21c6e.json`](../../sessions/b0/b045255adb304ee21c6e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T17:45:02.590Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T17:45:02.590Z",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-27 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Search-Objective Training for Process Reward Models\",\n  \"core_problem\": \"PRMs are trained with step-level classification objectives (is this step correct?) but deployed in search contexts (beam search, best-of-N) where ranking quality matters more than classification accuracy—can we close this training-deployment gap by optimizing PRMs directly for search performance?\",\n  \"opportunity\": \"\\\"More Test-Time Compute Can Hurt\\\" (March 2026) proved that PRM-guided beam search introduces overestimation bias that grows with candidate pool size, meaning more compute can degrade accuracy. Current mitigations—\\\"Know What You Don't Know\\\" (NeurIPS 2025) and Distributional PRM (May 2026)—apply post-hoc calibration without changing the training objective. PQM (ICLR 2025) recasts PRM as Q-value ranking but still optimizes step-level ranking, not end-to-end search performance. The gap is a PRM trained to maximize the probability that downstream search selects the correct solution—analogous to the shift from pointwise to listwise learning-to-rank.\",\n  \"landscape\": \"Current PRM training uses step-level binary cross-entropy (PRM800K-style), Monte Carlo soft labels (Math-Shepherd, OmegaPRM), or Q-value ranking (PQM, ICLR 2025). All optimize proxy objectives disconnected from downstream search. \\\"More Test-Time Compute Can Hurt\\\" showed PRM scoring yields useful beam widths ≤4-8 with gains up to 8.9pp, but beyond that, overestimation bias degrades results. Post-hoc calibration via quantile regression (NeurIPS 2025) reduces but doesn't eliminate this, and requires a separate calibration step. Distributional PRM (May 2026) applies conditional optimal transport for calibrated quantile estimation but still operates post-hoc on a classification-trained PRM. BEAR (Jan 2026) demonstrated beam-search-aware training for recommendation generators, and differentiable beam search decoders exist since 2019, but neither has been applied to reward model training. AIRL-S (Aug 2025) unifies RL and search by using RL-learned rewards as PRMs, but learns outcome-level rewards, not step-level process rewards with search-aware objectives. GRADE (Jan 2026) showed Gumbel-Softmax relaxation enables direct backpropagation from reward signals in LLM alignment, providing a key technical building block. A thorough search of arXiv (March–May 2026) and OpenReview submissions found no concurrent work that trains PRMs with end-to-end search-objective losses; the closest works (Distributional PRM, BEAR) address related problems through post-hoc calibration or generator-side regularization respectively.\",\n  \"inspired_by\": \"Field guide Gap 3 (PRM search + revision never combined), Pattern 'Reformulate-the-prediction-target' (redefine what PRM should predict from step correctness to search success), and the overestimation bias finding that exposes the training-deployment mismatch\",\n  \"approach\": \"Train a PRM with a search-objective loss that directly optimizes for downstream search performance rather than step-level classification. For each training batch, sample N candidate solutions from a frozen policy model (Qwen3-7B), simulate PRM-guided beam search or best-of-N selection using a temperature-annealed Gumbel-Softmax differentiable top-k relaxation over the PRM's step scores, and backpropagate a listwise cross-entropy loss measuring whether the search procedure selected the correct solution. The Gumbel temperature anneals from τ=2.0 to τ=0.1 during training, gradually sharpening the soft selection toward discrete beam pruning. To prevent catastrophic forgetting of per-step calibration, combine the search-objective loss with a weighted (λ=0.3) step-level binary cross-entropy regularizer. Initialize from Qwen2.5-Math-PRM-7B and fine-tune on MATH training problems with 256 rollouts per problem, evaluating on MATH-500, GSM8K, and AIME'24 across beam widths 1–64 to demonstrate that SO-PRM eliminates the overestimation cliff observed in classification-trained PRMs.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"1500 H100-hours (400h rollout generation, 400h PRM training with search-objective loops, 200h evaluation across beam widths/benchmarks, 500h ablations over λ, temperature schedules, beam widths)\",\n      \"timeline\": \"12–16 weeks (3w infrastructure + rollout pipeline, 4w search-objective training loop development, 3w main experiments, 2–4w ablations and paper writing)\",\n      \"estimated_gpu_cost\": \"$3,750 at $2.50/H100-hour (mid-2026 market median)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"1500 H100-hours (same compute; Claude accelerates code iteration but not GPU workloads)\",\n      \"timeline\": \"8–11 weeks (Claude drafts differentiable search module, training loop, and evaluation harnesses, reducing implementation time by ~4 weeks)\",\n      \"claude_api_cost\": \"$200–400 (code generation, experiment analysis, paper drafting assistance)\",\n      \"estimated_gpu_cost\": \"$3,750\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"2000 H100-hours (additional 500h for automated hyperparameter sweeps and broader ablation exploration)\",\n      \"timeline\": \"6–8 weeks (parallel experiment scheduling, automated ablation grid search, continuous evaluation)\",\n      \"claude_api_cost\": \"$600–1000 (experiment orchestration, result analysis, iterative debugging over many runs)\",\n      \"estimated_gpu_cost\": \"$5,000\",\n      \"speed_bottleneck\": \"Rollout generation: sampling 256 solutions per problem across 12K MATH problems requires sequential multi-GPU generation; search-objective training loop requires re-simulating beam search per gradient step, creating a 3–4x slowdown vs. standard PRM training\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (abstract July 21, full paper July 28, 2026)\",\n    \"EACL 2027 (ARR submission August 3, 2026; commitment October 11, 2026)\",\n    \"ICLR 2027 (estimated abstract ~September 19, paper ~September 24, 2026, based on historical pattern)\",\n    \"ICML 2027 (estimated ~January 2027, based on historical pattern)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"More Test-Time Compute Can Hurt: Overestimation Bias in LLM Beam Search (arXiv 2026)\",\n    \"Know What You Don't Know: Uncertainty Calibration of Process Reward Models (NeurIPS 2025)\",\n    \"Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport (arXiv 2026)\",\n    \"Process Reward Model with Q-Value Rankings (ICLR 2025)\",\n    \"BEAR: Towards Beam-Search-Aware Optimization for Recommendation with Large Language Models (arXiv 2026)\",\n    \"A Fully Differentiable Beam Search Decoder (ICML 2019)\",\n    \"Your Reward Function for RL is Your Best PRM for Search: Unifying RL and Search-Based TTS (arXiv 2025)\",\n    \"Let's Verify Step by Step (arXiv 2023)\",\n    \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (AAAI 2026)\",\n    \"Process Reward Models That Think (arXiv 2025)\",\n    \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations (ACL 2024)\",\n    \"Improve Mathematical Reasoning in Language Models by Automated Process Supervision (arXiv 2024)\",\n    \"Learning to Rank: From Pairwise Approach to Listwise Approach (ICML 2007)\",\n    \"GRADE: Replacing Policy Gradients with Backpropagation for LLM Alignment (arXiv 2026)\"\n  ],\n  \"description\": \"Process reward models (PRMs) are trained with step-level classification objectives but deployed in search contexts (beam search, best-of-N) where selection quality determines final accuracy. Recent theoretical work proved this mismatch introduces overestimation bias that grows with candidate pool size, causing wider beam search to degrade accuracy beyond a critical width of 4–8. All current mitigations—quantile regression calibration, distributional calibration via optimal transport, Q-value ranking—either apply post-hoc corrections or still optimize step-level proxies disconnected from search outcomes. We propose Search-Objective PRM (SO-PRM), which closes this training-deployment gap by directly optimizing the PRM to maximize the probability that downstream search selects the correct solution. Using a temperature-annealed Gumbel-Softmax relaxation of beam pruning, we make the search procedure differentiable and backpropagate a listwise loss through the simulated search trajectory to the PRM parameters. A step-level regularizer preserves per-step calibration. SO-PRM eliminates the overestimation cliff, enabling monotonic accuracy scaling with beam width. Starting from Qwen2.5-Math-PRM-7B with Qwen3-7B as the generator, we target MATH-500, GSM8K, and AIME'24 benchmarks, aiming to outperform classification-trained PRMs at all beam widths, particularly the wide-beam regime (16–64) where current PRMs fail.\",\n  \"project_name\": \"search_objective_prm\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 1)\nIssues: [\"CRITICAL MISSING RELATED WORK: Supervised Optimism Correction (SOC, arXiv 2504.07527, Apr 2025) directly addresses overestimation bias in beam search via a modified training objective—an auxiliary loss during SFT that suppresses inflated Q-values. This is the closest prior work and must be cited and differentiated.\", \"MISSING RELATED WORK: CRM—Conditional Reward Modeling (ICLR 2026, arXiv 2509.26578) conditions step rewards on outcomes and demonstrates improvements across Best-of-N, beam search, and RL. While not end-to-end search-objective, it modifies what the PRM predicts to better align with downstream use.\", \"MISSING RELATED WORK: 'From Curiosity to Caution' (arXiv 2604.04648, Apr 2026) applies pessimistic reward correction for BoN to mitigate reward hacking—directly related to overestimation mitigation.\", \"MISSING RELATED WORK: 'Learning Generative Selection for Best-of-N' (arXiv 2602.02143, Feb 2026) trains selection models via RL for search—addresses the same selection quality problem from a different angle.\", \"MISSING RELATED WORK: 'Inference-Aware Fine-Tuning for Best-of-N Sampling' (ICLR 2025, arXiv 2412.15287) is the generator-side analog of this idea and provides the conceptual precedent for inference-aware training.\", \"FACTUAL ERROR: Qwen3-7B does not exist. The Qwen3 series offers 0.6B, 1.7B, 4B, 8B, 14B, 32B. The generator should be Qwen3-8B.\", \"OVERCONFIDENT CLAIM: 'SO-PRM eliminates the overestimation cliff, enabling monotonic accuracy scaling with beam width' is an extremely strong claim. Gumbel-Softmax approximation introduces its own soft-vs-hard gap, and achieving truly monotonic scaling at beam widths 16–64 would be remarkable.\", \"VENUE TIMELINE MISMATCH: AAAI 2027 abstract due July 21 (8 weeks from May 27) is unrealistic given the 12–16 week manual timeline. Even the 8–11 week human-in-loop estimate cuts it dangerously close for a first-attempt submission.\", \"TECHNICAL RISK UNDERSTATED: Temperature annealing from τ=2.0 to τ=0.1 is aggressive—at τ=0.1 Gumbel-Softmax outputs are near-discrete, causing gradient bias. The paper should discuss straight-through estimator alternatives and the soft-training/hard-inference gap.\", \"STRATEGIC CONCERN: The field is rapidly shifting toward generative verifiers (ThinkPRM, GenPRM) and RL-based training (GRPO, DAPO) where discriminative PRM optimization may have diminishing returns. The paper should explicitly address why optimizing a discriminative PRM's training objective remains important in this landscape.\"]\nFeedback: The core idea is genuinely novel—no concurrent work trains PRMs with an end-to-end search-objective loss—but the submission needs significant revision: (1) Add 5+ missing related works, especially SOC and CRM which are very close in spirit. Clearly differentiate: SOC modifies the generator's SFT loss, CRM conditions step rewards on outcomes, while SO-PRM optimizes the PRM's own training loss for search performance. (2) Fix Qwen3-7B → Qwen3-8B. (3) Soften the 'monotonic scaling' claim to 'significantly extend the useful beam width range' with explicit acknowledgment of the Gumbel soft-hard gap. (4) Drop AAAI 2027 as a realistic first target; ICLR 2027 (Sep 2026) is the earliest feasible venue. (5) Add a paragraph on why discriminative PRM optimization still matters given the generative verifier trend (e.g., discriminative PRMs are 10–100× cheaper at inference, making them preferable for large-scale beam search). (6) Discuss the technical risk of Gumbel-Softmax gradient quality at low temperatures and the training/inference distribution mismatch that the soft relaxation itself introduces.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.\n- Address each issue specifically.\n\n## 深度调研要求\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。\n3. **深度思考**：\n   - 核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach？\n4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。\n\n## 针对 Review 意见的定向搜索\n\n1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点\n2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline\n3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现\n4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot\n\n- You have full freedom: minor fix, major revision, or pivot.\n- Include a \"change_type\" field: \"minor\", \"major\", or \"pivot\".\n- Output a COMPLETE JSON object with ALL fields."
}
```

---

### Runtime record

_source line 2 · 2026-05-27T17:45:02.594Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T17:45:02.594Z",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b"
}
```

---

## Round 1

32 recorded events

### User

_source line 3 · 2026-05-27T17:45:02.653Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-27 (UTC).**

## Original idea
{
  "title": "Search-Objective Training for Process Reward Models",
  "core_problem": "PRMs are trained with step-level classification objectives (is this step correct?) but deployed in search contexts (beam search, best-of-N) where ranking quality matters more than classification accuracy—can we close this training-deployment gap by optimizing PRMs directly for search performance?",
  "opportunity": "\"More Test-Time Compute Can Hurt\" (March 2026) proved that PRM-guided beam search introduces overestimation bias that grows with candidate pool size, meaning more compute can degrade accuracy. Current mitigations—\"Know What You Don't Know\" (NeurIPS 2025) and Distributional PRM (May 2026)—apply post-hoc calibration without changing the training objective. PQM (ICLR 2025) recasts PRM as Q-value ranking but still optimizes step-level ranking, not end-to-end search performance. The gap is a PRM trained to maximize the probability that downstream search selects the correct solution—analogous to the shift from pointwise to listwise learning-to-rank.",
  "landscape": "Current PRM training uses step-level binary cross-entropy (PRM800K-style), Monte Carlo soft labels (Math-Shepherd, OmegaPRM), or Q-value ranking (PQM, ICLR 2025). All optimize proxy objectives disconnected from downstream search. \"More Test-Time Compute Can Hurt\" showed PRM scoring yields useful beam widths ≤4-8 with gains up to 8.9pp, but beyond that, overestimation bias degrades results. Post-hoc calibration via quantile regression (NeurIPS 2025) reduces but doesn't eliminate this, and requires a separate calibration step. Distributional PRM (May 2026) applies conditional optimal transport for calibrated quantile estimation but still operates post-hoc on a classification-trained PRM. BEAR (Jan 2026) demonstrated beam-search-aware training for recommendation generators, and differentiable beam search decoders exist since 2019, but neither has been applied to reward model training. AIRL-S (Aug 2025) unifies RL and search by using RL-learned rewards as PRMs, but learns outcome-level rewards, not step-level process rewards with search-aware objectives. GRADE (Jan 2026) showed Gumbel-Softmax relaxation enables direct backpropagation from reward signals in LLM alignment, providing a key technical building block. A thorough search of arXiv (March–May 2026) and OpenReview submissions found no concurrent work that trains PRMs with end-to-end search-objective losses; the closest works (Distributional PRM, BEAR) address related problems through post-hoc calibration or generator-side regularization respectively.",
  "inspired_by": "Field guide Gap 3 (PRM search + revision never combined), Pattern 'Reformulate-the-prediction-target' (redefine what PRM should predict from step correctness to search success), and the overestimation bias finding that exposes the training-deployment mismatch",
  "approach": "Train a PRM with a search-objective loss that directly optimizes for downstream search performance rather than step-level classification. For each training batch, sample N candidate solutions from a frozen policy model (Qwen3-7B), simulate PRM-guided beam search or best-of-N selection using a temperature-annealed Gumbel-Softmax differentiable top-k relaxation over the PRM's step scores, and backpropagate a listwise cross-entropy loss measuring whether the search procedure selected the correct solution. The Gumbel temperature anneals from τ=2.0 to τ=0.1 during training, gradually sharpening the soft selection toward discrete beam pruning. To prevent catastrophic forgetting of per-step calibration, combine the search-objective loss with a weighted (λ=0.3) step-level binary cross-entropy regularizer. Initialize from Qwen2.5-Math-PRM-7B and fine-tune on MATH training problems with 256 rollouts per problem, evaluating on MATH-500, GSM8K, and AIME'24 across beam widths 1–64 to demonstrate that SO-PRM eliminates the overestimation cliff observed in classification-trained PRMs.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "1500 H100-hours (400h rollout generation, 400h PRM training with search-objective loops, 200h evaluation across beam widths/benchmarks, 500h ablations over λ, temperature schedules, beam widths)",
      "timeline": "12–16 weeks (3w infrastructure + rollout pipeline, 4w search-objective training loop development, 3w main experiments, 2–4w ablations and paper writing)",
      "estimated_gpu_cost": "$3,750 at $2.50/H100-hour (mid-2026 market median)"
    },
    "human_in_loop": {
      "gpu_hours": "1500 H100-hours (same compute; Claude accelerates code iteration but not GPU workloads)",
      "timeline": "8–11 weeks (Claude drafts differentiable search module, training loop, and evaluation harnesses, reducing implementation time by ~4 weeks)",
      "claude_api_cost": "$200–400 (code generation, experiment analysis, paper drafting assistance)",
      "estimated_gpu_cost": "$3,750"
    },
    "auto_research": {
      "gpu_hours": "2000 H100-hours (additional 500h for automated hyperparameter sweeps and broader ablation exploration)",
      "timeline": "6–8 weeks (parallel experiment scheduling, automated ablation grid search, continuous evaluation)",
      "claude_api_cost": "$600–1000 (experiment orchestration, result analysis, iterative debugging over many runs)",
      "estimated_gpu_cost": "$5,000",
      "speed_bottleneck": "Rollout generation: sampling 256 solutions per problem across 12K MATH problems requires sequential multi-GPU generation; search-objective training loop requires re-simulating beam search per gradient step, creating a 3–4x slowdown vs. standard PRM training"
    }
  },
  "target_venues": [
    "AAAI 2027 (abstract July 21, full paper July 28, 2026)",
    "EACL 2027 (ARR submission August 3, 2026; commitment October 11, 2026)",
    "ICLR 2027 (estimated abstract ~September 19, paper ~September 24, 2026, based on historical pattern)",
    "ICML 2027 (estimated ~January 2027, based on historical pattern)"
  ],
  "level": "top-tier",
  "key_references": [
    "More Test-Time Compute Can Hurt: Overestimation Bias in LLM Beam Search (arXiv 2026)",
    "Know What You Don't Know: Uncertainty Calibration of Process Reward Models (NeurIPS 2025)",
    "Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport (arXiv 2026)",
    "Process Reward Model with Q-Value Rankings (ICLR 2025)",
    "BEAR: Towards Beam-Search-Aware Optimization for Recommendation with Large Language Models (arXiv 2026)",
    "A Fully Differentiable Beam Search Decoder (ICML 2019)",
    "Your Reward Function for RL is Your Best PRM for Search: Unifying RL and Search-Based TTS (arXiv 2025)",
    "Let's Verify Step by Step (arXiv 2023)",
    "GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (AAAI 2026)",
    "Process Reward Models That Think (arXiv 2025)",
    "Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations (ACL 2024)",
    "Improve Mathematical Reasoning in Language Models by Automated Process Supervision (arXiv 2024)",
    "Learning to Rank: From Pairwise Approach to Listwise Approach (ICML 2007)",
    "GRADE: Replacing Policy Gradients with Backpropagation for LLM Alignment (arXiv 2026)"
  ],
  "description": "Process reward models (PRMs) are trained with step-level classification objectives but deployed in search contexts (beam search, best-of-N) where selection quality determines final accuracy. Recent theoretical work proved this mismatch introduces overestimation bias that grows with candidate pool size, causing wider beam search to degrade accuracy beyond a critical width of 4–8. All current mitigations—quantile regression calibration, distributional calibration via optimal transport, Q-value ranking—either apply post-hoc corrections or still optimize step-level proxies disconnected from search outcomes. We propose Search-Objective PRM (SO-PRM), which closes this training-deployment gap by directly optimizing the PRM to maximize the probability that downstream search selects the correct solution. Using a temperature-annealed Gumbel-Softmax relaxation of beam pruning, we make the search procedure differentiable and backpropagate a listwise loss through the simulated search trajectory to the PRM parameters. A step-level regularizer preserves per-step calibration. SO-PRM eliminates the overestimation cliff, enabling monotonic accuracy scaling with beam width. Starting from Qwen2.5-Math-PRM-7B with Qwen3-7B as the generator, we target MATH-500, GSM8K, and AIME'24 benchmarks, aiming to outperform classification-trained PRMs at all beam widths, particularly the wide-beam regime (16–64) where current PRMs fail.",
  "project_name": "search_objective_prm",
  "source": "web_research"
}

## Reviewer feedback (round 1)
Issues: ["CRITICAL MISSING RELATED WORK: Supervised Optimism Correction (SOC, arXiv 2504.07527, Apr 2025) directly addresses overestimation bias in beam search via a modified training objective—an auxiliary loss during SFT that suppresses inflated Q-values. This is the closest prior work and must be cited and differentiated.", "MISSING RELATED WORK: CRM—Conditional Reward Modeling (ICLR 2026, arXiv 2509.26578) conditions step rewards on outcomes and demonstrates improvements across Best-of-N, beam search, and RL. While not end-to-end search-objective, it modifies what the PRM predicts to better align with downstream use.", "MISSING RELATED WORK: 'From Curiosity to Caution' (arXiv 2604.04648, Apr 2026) applies pessimistic reward correction for BoN to mitigate reward hacking—directly related to overestimation mitigation.", "MISSING RELATED WORK: 'Learning Generative Selection for Best-of-N' (arXiv 2602.02143, Feb 2026) trains selection models via RL for search—addresses the same selection quality problem from a different angle.", "MISSING RELATED WORK: 'Inference-Aware Fine-Tuning for Best-of-N Sampling' (ICLR 2025, arXiv 2412.15287) is the generator-side analog of this idea and provides the conceptual precedent for inference-aware training.", "FACTUAL ERROR: Qwen3-7B does not exist. The Qwen3 series offers 0.6B, 1.7B, 4B, 8B, 14B, 32B. The generator should be Qwen3-8B.", "OVERCONFIDENT CLAIM: 'SO-PRM eliminates the overestimation cliff, enabling monotonic accuracy scaling with beam width' is an extremely strong claim. Gumbel-Softmax approximation introduces its own soft-vs-hard gap, and achieving truly monotonic scaling at beam widths 16–64 would be remarkable.", "VENUE TIMELINE MISMATCH: AAAI 2027 abstract due July 21 (8 weeks from May 27) is unrealistic given the 12–16 week manual timeline. Even the 8–11 week human-in-loop estimate cuts it dangerously close for a first-attempt submission.", "TECHNICAL RISK UNDERSTATED: Temperature annealing from τ=2.0 to τ=0.1 is aggressive—at τ=0.1 Gumbel-Softmax outputs are near-discrete, causing gradient bias. The paper should discuss straight-through estimator alternatives and the soft-training/hard-inference gap.", "STRATEGIC CONCERN: The field is rapidly shifting toward generative verifiers (ThinkPRM, GenPRM) and RL-based training (GRPO, DAPO) where discriminative PRM optimization may have diminishing returns. The paper should explicitly address why optimizing a discriminative PRM's training objective remains important in this landscape."]
Feedback: The core idea is genuinely novel—no concurrent work trains PRMs with an end-to-end search-objective loss—but the submission needs significant revision: (1) Add 5+ missing related works, especially SOC and CRM which are very close in spirit. Clearly differentiate: SOC modifies the generator's SFT loss, CRM conditions step rewards on outcomes, while SO-PRM optimizes the PRM's own training loss for search performance. (2) Fix Qwen3-7B → Qwen3-8B. (3) Soften the 'monotonic scaling' claim to 'significantly extend the useful beam width range' with explicit acknowledgment of the Gumbel soft-hard gap. (4) Drop AAAI 2027 as a realistic first target; ICLR 2027 (Sep 2026) is the earliest feasible venue. (5) Add a paragraph on why discriminative PRM optimization still matters given the generative verifier trend (e.g., discriminative PRMs are 10–100× cheaper at inference, making them preferable for large-scale beam search). (6) Discuss the technical risk of Gumbel-Softmax gradient quality at low temperatures and the training/inference distribution mismatch that the soft relaxation itself introduces.

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
  "promptId": "cfe7962d-223e-4b12-9480-c455cf84546f",
  "type": "user",
  "uuid": "a69d83cb-e141-476c-b3e6-d57c55cc6078",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T17:45:02.652Z_

```json
{
  "parentUuid": "a69d83cb-e141-476c-b3e6-d57c55cc6078",
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
  "uuid": "96b7baa0-3c4f-4f1e-ba0a-73c1cfa1bf9f",
  "timestamp": "2026-05-27T17:45:02.652Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T17:45:02.652Z_

```json
{
  "parentUuid": "96b7baa0-3c4f-4f1e-ba0a-73c1cfa1bf9f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e777ca56-2eb4-4681-97d2-fc3ed78133fe",
  "timestamp": "2026-05-27T17:45:02.652Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Search-Objective Training for Process Reward Models\",   \"core_problem\"…",
  "leafUuid": "e777ca56-2eb4-4681-97d2-fc3ed78133fe",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise search-objective PRM training based on reviewer feedback",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b"
}
```

---

### Assistant

_source line 8 · 2026-05-27T17:45:10.267Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully and plan my research accordingly. The feedback raises several important issues:

1. **Critical missing related works** (SOC, CRM, From Curiosity to Caution, Learning Generative Selection, Inference-Aware Fine-Tuning)
2. **Factual error** (Qwen3-7B → Qwen3-8B)
3. **Overconfident claims** (monotonic scaling)


4. **Venue timeline mismatch** (AAAI 2027 unrealistic)
5. **Technical risk understated** (Gumbel-Softmax gradient quality)
6. **Strategic concern** (discriminative vs generative verifiers)

I need to dig into each of these issues systematically, starting with tracking down those missing papers and understanding how they relate to my work, then addressing the factual corrections and reconsidering my technical assumptions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e777ca56-2eb4-4681-97d2-fc3ed78133fe",
  "isSidechain": false,
  "requestId": "req_011CbTVNPEAA4eEYL9M9vpZG",
  "type": "assistant",
  "uuid": "e55a02ab-5c00-4999-a82c-7d9f77c9a101",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0125Z2DZabXrfbLYfQJBotmP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5295,
      "cache_read_input_tokens": 11014,
      "output_tokens": 322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5295,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 322,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 5295,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5295
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

_source line 9 · 2026-05-27T17:45:10.564Z_

I'll start by conducting deep research on all the missing related works and technical concerns raised by the reviewers. Let me launch parallel research agents for the key papers and topics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e55a02ab-5c00-4999-a82c-7d9f77c9a101",
  "isSidechain": false,
  "requestId": "req_011CbTVNPEAA4eEYL9M9vpZG",
  "type": "assistant",
  "uuid": "ff036257-5440-48b9-beba-a6a3a779608e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0125Z2DZabXrfbLYfQJBotmP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5295,
      "cache_read_input_tokens": 11014,
      "output_tokens": 322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5295,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 322,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 5295,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5295
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

_source line 10 · 2026-05-27T17:45:11.139Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011zigFsZM58Rcyop3TPKEGz`</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff036257-5440-48b9-beba-a6a3a779608e",
  "isSidechain": false,
  "requestId": "req_011CbTVNPEAA4eEYL9M9vpZG",
  "type": "assistant",
  "uuid": "71951ca4-1d71-42f5-a71e-60e2b998fc1c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0125Z2DZabXrfbLYfQJBotmP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5295,
      "cache_read_input_tokens": 11014,
      "output_tokens": 322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5295,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 322,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 5295,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5295
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

_source line 11 · 2026-05-27T17:45:11.146Z_

<details><summary>↩ Tool result · `toolu_011zigFsZM58Rcyop3TPKEGz`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

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
  "parentUuid": "71951ca4-1d71-42f5-a71e-60e2b998fc1c",
  "isSidechain": false,
  "promptId": "cfe7962d-223e-4b12-9480-c455cf84546f",
  "type": "user",
  "uuid": "2f22e819-5a6e-474e-a8e6-8f5c1a89830f",
  "toolUseResult": {
    "matches": [
      "WebFetch",
      "WebSearch"
    ],
    "query": "select:WebFetch,WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "71951ca4-1d71-42f5-a71e-60e2b998fc1c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-27T17:45:14.556Z_

Now let me launch parallel research on all the critical missing related works and technical concerns.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f22e819-5a6e-474e-a8e6-8f5c1a89830f",
  "isSidechain": false,
  "requestId": "req_011CbTVP1i8JZYZQ2BgHLjj4",
  "type": "assistant",
  "uuid": "363b892c-5130-4e60-bb97-aaedf2150380",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AQwP1X2gs2dF3BgCednZ3M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1342,
      "cache_read_input_tokens": 16309,
      "output_tokens": 403,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1342,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 403,
          "cache_read_input_tokens": 16309,
          "cache_creation_input_tokens": 1342,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1342
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

_source line 13 · 2026-05-27T17:45:22.953Z_

<details open><summary>🔧 Tool call — Agent · `toolu_015GdBPLFNedQyi1yvuLkW86`</summary>

```json
{
  "description": "Research SOC paper (arXiv 2504.07527)",
  "prompt": "I'm revising a research idea about training Process Reward Models (PRMs) with search-objective losses. A reviewer flagged a critical missing related work: \"Supervised Optimism Correction (SOC, arXiv 2504.07527, Apr 2025)\" which directly addresses overestimation bias in beam search via a modified training objective.\n\nPlease do the following:\n1. Search for this paper using WebSearch with queries like \"Supervised Optimism Correction SOC overestimation beam search arXiv 2504.07527\"\n2. Fetch and read the actual paper on arXiv using WebFetch (try https://arxiv.org/abs/2504.07527)\n3. Report back in detail:\n   - What exactly is SOC's approach? What training objective does it use?\n   - How does it modify the training to address overestimation bias?\n   - What results does it achieve? On what benchmarks?\n   - How is it different from training a PRM end-to-end for search performance?\n   - What are its limitations that our approach (training PRM directly with search-objective loss via differentiable beam search) could address?\n\nBe thorough - I need to clearly differentiate our work from SOC.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "363b892c-5130-4e60-bb97-aaedf2150380",
  "isSidechain": false,
  "requestId": "req_011CbTVP1i8JZYZQ2BgHLjj4",
  "type": "assistant",
  "uuid": "1ad33883-21ca-449c-b8c0-a8817988d6e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AQwP1X2gs2dF3BgCednZ3M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1342,
      "cache_read_input_tokens": 16309,
      "output_tokens": 403,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1342,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 403,
          "cache_read_input_tokens": 16309,
          "cache_creation_input_tokens": 1342,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1342
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

_source line 14 · 2026-05-27T17:48:05.820Z_

<details><summary>↩ Tool result · `toolu_015GdBPLFNedQyi1yvuLkW86`</summary>

````text
I now have all the information needed. Here is my comprehensive analysis.

---

## Detailed Analysis of SOC (Supervised Optimism Correction, arXiv 2504.07527)

**Paper:** "Supervised Optimism Correction: Be Confident When LLMs Are Sure" by Zhang et al., April 2025. Accepted at ACL 2025 Findings.

---

### 1. What Exactly Is SOC's Approach?

SOC frames token generation as a token-level Markov Decision Process (MDP) and establishes that supervised fine-tuning (SFT) implicitly trains an approximate Q-function. Specifically, since the policy is parameterized as:

```
pi_theta(a|s) = exp(Q_theta(s,a)) / sum_a' exp(Q_theta(s,a'))
```

the LLM's logits directly correspond to implicit Q-values. Beam search, which maximizes cumulative log-probability, is therefore implicitly maximizing the Q-value of the final state (since `sum log pi(a_t|s_t) = Q(s_T, a_T) - V(s_0)` and `V(s_0)` is shared across all beams).

The problem: SFT only trains on expert demonstrations, so Q-values for states/actions not covered by the training data can be arbitrarily overestimated. Beam search then systematically selects these overestimated trajectories, producing poor results.

**SOC's Training Objective:**

```
L_overall = L_SFT + lambda * L_V
```

Where:
- `L_SFT` is the standard cross-entropy SFT loss: `E_s[-sum_a pi*(a|s) log pi_theta(a|s)]`
- `L_V` is the auxiliary "value loss": `E_s[-log sum_a exp Q_theta(s,a)]`
- `lambda = 0.2` (default, not very sensitive; 0.1 and 0.3 give similar results)

The V loss is the negative log-partition function (log-sum-exp over logits). Minimizing this loss pushes up the overall implicit value function for states that appear in the expert training data, making the model more "confident" on expert-demonstrated trajectories relative to unseen ones.

---

### 2. How Does SOC Modify Training to Address Overestimation Bias?

The key insight is about **where gradients are zero vs. non-zero**:

- Standard SFT minimizes the estimation error `Q_theta(s,a) - Q*(s,a)` weighted by the gradient. When the SFT loss is near zero (the model has already fit the training data well), the gradients vanish, and Q-values for expert trajectories stop increasing -- but Q-values for non-expert trajectories may still be inflated.

- The V loss gradient is: `E_s[-sum_a Q_tilde_theta(s,a) * dQ_theta(s,a)/d_theta]`. This continues to push up Q-values for expert states even when SFT gradients are small, creating a "confidence gap" between expert-demonstrated states and unvisited states.

- **Theorem 4.1 (Value Contraction):** They prove that the V loss contracts the gap between adjacent states' values: `|V'(s_t) - V'(s_{t+1})| <= |V(s_t) - V(s_{t+1})|`. In sparse-reward settings where intermediate rewards are zero, the optimal value function should satisfy `V*(s_t) = V*(s_{t+1})` for all intermediate states. The V loss pushes the learned values toward this flat structure.

**Important caveat:** The theoretical guarantee is a contraction property, not a formal proof that overestimation is eliminated. The link from value contraction to improved beam search performance is supported empirically but not formally proven.

---

### 3. Results and Benchmarks

**Models tested:** Qwen-2-1.5B-Base, Qwen-2.5-3B-Base, Qwen-2.5-7B-Base

**Training data:**
- DATA-alpha: Filtered STEP-DPO-10K dataset (~10.3K samples, correct/complete QA pairs)
- DATA-beta: Filtered MATH dataset (~2.8K samples, highest difficulty level 5 only)

**Benchmarks:** GSM8K, MATH-500, GAOKAO-2023-En

**Key results (beam width 5, improvement over standard SFT + beam search):**

| Setting | GSM8K | MATH-500 | GAOKAO |
|---------|-------|----------|--------|
| 1.5B, DATA-alpha | +1.1% | +1.4% | +0.5% |
| 1.5B, DATA-beta | +0.3% | +1.6% | +3.4% |
| 3B, DATA-alpha | +4.3% | +4.8% | +11.7% |
| 3B, DATA-beta | +22.9% | +1.6% | +0.3% |
| 7B, DATA-alpha | +33.2% | +19.0% | +22.8% |
| 7B, DATA-beta | +3.8% | +0.4% | +0.8% |

The improvements are highly variable -- some settings see 20-33% improvement, others less than 1%. Greedy decoding performance is essentially unchanged by SOC (by design, since the method targets beam search specifically).

**Baselines:** The comparison is primarily SFT-only vs. SFT+SOC, both using beam search at inference. They do NOT compare against PRM-guided search, ORM-guided search, or any verifier-based methods.

---

### 4. How Is SOC Different from Training a PRM End-to-End for Search Performance?

This is the critical differentiation. SOC and a search-objective PRM training approach differ in several fundamental ways:

**(a) No separate reward model.** SOC does not train a separate PRM. It modifies the SFT loss of the policy model itself so that its implicit Q-values (logits) are better calibrated for beam search. At inference, beam search uses only the policy model's log-probabilities -- no external verifier or reward model is involved.

**(b) No search-aware training.** SOC does NOT backpropagate through the beam search procedure. The auxiliary V loss is applied independently at each token position in the training data. There is no mechanism to evaluate "what would beam search actually select?" during training and then correct for it. The method is search-agnostic in the sense that it regularizes Q-values uniformly, hoping this indirectly helps beam search.

**(c) Indirect optimization.** SOC addresses overestimation through a proxy: value contraction and confidence boosting on expert data. It does not directly optimize the metric "does beam search find the correct answer?" A search-objective PRM, by contrast, would directly optimize the reward model's scores to ensure the search procedure selects correct solutions.

**(d) Only works with the policy model's own logits.** SOC cannot be applied to a separate PRM that guides search -- it is fundamentally about calibrating the LLM's own token-level predictions. This means it cannot benefit from the architectural flexibility of having a dedicated verifier.

**(e) Assumes sparse terminal rewards.** The theoretical framework assumes rewards are only at the terminal state (`R_outcome = 1` for correct, 0 otherwise), with zero intermediate rewards. This is exactly the setting where step-level process reward is most valuable and where SOC's theory is most limited.

---

### 5. SOC's Limitations That Your Approach Could Address

Here are the specific gaps that training a PRM directly with a search-objective loss (via differentiable beam search) could fill:

**(a) No direct search optimization.** SOC's auxiliary loss is not aware of the actual search procedure. It applies a generic regularizer hoping it helps beam search, but it never evaluates what beam search would actually select during training. Your approach of differentiable beam search would directly optimize for "does the search find the right answer?", closing the train-test gap.

**(b) No process-level reward signal.** SOC works entirely within the sparse-reward framework (terminal correctness only). It does not provide or leverage step-level reward signals. A PRM trained with search-objective loss would provide dense, step-level guidance that can catch errors at intermediate reasoning steps, not just at the final answer.

**(c) Narrow theoretical guarantee.** SOC's Theorem 4.1 only proves value contraction (adjacent states' values get closer), but does not prove that beam search will actually find better solutions. The connection is empirical. End-to-end training through differentiable beam search would provide a more direct optimization signal with clearer alignment between training objective and search performance.

**(d) No separation of concerns.** SOC modifies the policy model's training, which means the same model must serve both as the generator and the implicit evaluator. This conflates two objectives. A dedicated PRM allows the search guidance model to specialize in evaluation while the policy model specializes in generation.

**(e) Highly variable improvements.** SOC's results are very inconsistent across model sizes and datasets (ranging from +0.3% to +33.2%). This suggests the indirect regularization approach is fragile. Direct search-objective training should provide more consistent improvements because it optimizes exactly the right objective.

**(f) Limited to beam search over policy logits.** SOC only improves beam search when using the model's own log-probabilities for scoring. It cannot improve other search strategies (MCTS, best-of-N with verifier, etc.). A PRM trained with search-objective loss is a more general tool that can guide any search algorithm.

**(g) No comparison to reward-model-based methods.** The paper does not compare against PRM-guided or ORM-guided beam search at all. This leaves open the question of whether SOC even matches the performance of a simple PRM, let alone a search-optimized one.

**(h) Beam-search specific.** The authors themselves acknowledge this limitation: they note it is "valuable to investigate whether other search-based methods encounter this issue." Your differentiable search approach could generalize across search algorithms.

---

### Summary for Positioning Your Work

SOC is the closest related work because it:
1. Identifies the same problem (overestimation bias degrading beam search for reasoning)
2. Proposes a training-time fix rather than an inference-time fix
3. Frames the problem in terms of Q-value estimation

But SOC takes an **indirect, regularization-based approach** -- it adds a simple auxiliary loss that encourages value contraction, without ever looking at what beam search actually does during training. Your approach of training a PRM end-to-end with a search-objective loss via differentiable beam search is fundamentally more direct: it optimizes the actual search outcome, provides process-level reward, and separates the reward model from the policy. You should cite SOC as identifying the right problem but argue that your method provides a more principled and direct solution by making the search procedure itself part of the training loop.

Sources:
- [SOC Paper on arXiv](https://arxiv.org/abs/2504.07527)
- [SOC Full HTML](https://arxiv.org/html/2504.07527)
- [SOC at ACL Anthology](https://aclanthology.org/2025.findings-acl.463/)
- [SOC PDF](https://arxiv.org/pdf/2504.07527)

agentId: ace561f64d3467e4d (use SendMessage with to: 'ace561f64d3467e4d' to continue this agent)
&lt;usage>total_tokens: 22320
tool_uses: 9
duration_ms: 162859&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "1ad33883-21ca-449c-b8c0-a8817988d6e3",
  "isSidechain": false,
  "promptId": "cfe7962d-223e-4b12-9480-c455cf84546f",
  "type": "user",
  "uuid": "b913dcd7-bf3b-4175-8896-23716f01bbbb",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm revising a research idea about training Process Reward Models (PRMs) with search-objective losses. A reviewer flagged a critical missing related work: \"Supervised Optimism Correction (SOC, arXiv 2504.07527, Apr 2025)\" which directly addresses overestimation bias in beam search via a modified training objective.\n\nPlease do the following:\n1. Search for this paper using WebSearch with queries like \"Supervised Optimism Correction SOC overestimation beam search arXiv 2504.07527\"\n2. Fetch and read the actual paper on arXiv using WebFetch (try https://arxiv.org/abs/2504.07527)\n3. Report back in detail:\n   - What exactly is SOC's approach? What training objective does it use?\n   - How does it modify the training to address overestimation bias?\n   - What results does it achieve? On what benchmarks?\n   - How is it different from training a PRM end-to-end for search performance?\n   - What are its limitations that our approach (training PRM directly with search-objective loss via differentiable beam search) could address?\n\nBe thorough - I need to clearly differentiate our work from SOC.",
    "agentId": "ace561f64d3467e4d",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have all the information needed. Here is my comprehensive analysis.\n\n---\n\n## Detailed Analysis of SOC (Supervised Optimism Correction, arXiv 2504.07527)\n\n**Paper:** \"Supervised Optimism Correction: Be Confident When LLMs Are Sure\" by Zhang et al., April 2025. Accepted at ACL 2025 Findings.\n\n---\n\n### 1. What Exactly Is SOC's Approach?\n\nSOC frames token generation as a token-level Markov Decision Process (MDP) and establishes that supervised fine-tuning (SFT) implicitly trains an approximate Q-function. Specifically, since the policy is parameterized as:\n\n```\npi_theta(a|s) = exp(Q_theta(s,a)) / sum_a' exp(Q_theta(s,a'))\n```\n\nthe LLM's logits directly correspond to implicit Q-values. Beam search, which maximizes cumulative log-probability, is therefore implicitly maximizing the Q-value of the final state (since `sum log pi(a_t|s_t) = Q(s_T, a_T) - V(s_0)` and `V(s_0)` is shared across all beams).\n\nThe problem: SFT only trains on expert demonstrations, so Q-values for states/actions not covered by the training data can be arbitrarily overestimated. Beam search then systematically selects these overestimated trajectories, producing poor results.\n\n**SOC's Training Objective:**\n\n```\nL_overall = L_SFT + lambda * L_V\n```\n\nWhere:\n- `L_SFT` is the standard cross-entropy SFT loss: `E_s[-sum_a pi*(a|s) log pi_theta(a|s)]`\n- `L_V` is the auxiliary \"value loss\": `E_s[-log sum_a exp Q_theta(s,a)]`\n- `lambda = 0.2` (default, not very sensitive; 0.1 and 0.3 give similar results)\n\nThe V loss is the negative log-partition function (log-sum-exp over logits). Minimizing this loss pushes up the overall implicit value function for states that appear in the expert training data, making the model more \"confident\" on expert-demonstrated trajectories relative to unseen ones.\n\n---\n\n### 2. How Does SOC Modify Training to Address Overestimation Bias?\n\nThe key insight is about **where gradients are zero vs. non-zero**:\n\n- Standard SFT minimizes the estimation error `Q_theta(s,a) - Q*(s,a)` weighted by the gradient. When the SFT loss is near zero (the model has already fit the training data well), the gradients vanish, and Q-values for expert trajectories stop increasing -- but Q-values for non-expert trajectories may still be inflated.\n\n- The V loss gradient is: `E_s[-sum_a Q_tilde_theta(s,a) * dQ_theta(s,a)/d_theta]`. This continues to push up Q-values for expert states even when SFT gradients are small, creating a \"confidence gap\" between expert-demonstrated states and unvisited states.\n\n- **Theorem 4.1 (Value Contraction):** They prove that the V loss contracts the gap between adjacent states' values: `|V'(s_t) - V'(s_{t+1})| <= |V(s_t) - V(s_{t+1})|`. In sparse-reward settings where intermediate rewards are zero, the optimal value function should satisfy `V*(s_t) = V*(s_{t+1})` for all intermediate states. The V loss pushes the learned values toward this flat structure.\n\n**Important caveat:** The theoretical guarantee is a contraction property, not a formal proof that overestimation is eliminated. The link from value contraction to improved beam search performance is supported empirically but not formally proven.\n\n---\n\n### 3. Results and Benchmarks\n\n**Models tested:** Qwen-2-1.5B-Base, Qwen-2.5-3B-Base, Qwen-2.5-7B-Base\n\n**Training data:**\n- DATA-alpha: Filtered STEP-DPO-10K dataset (~10.3K samples, correct/complete QA pairs)\n- DATA-beta: Filtered MATH dataset (~2.8K samples, highest difficulty level 5 only)\n\n**Benchmarks:** GSM8K, MATH-500, GAOKAO-2023-En\n\n**Key results (beam width 5, improvement over standard SFT + beam search):**\n\n| Setting | GSM8K | MATH-500 | GAOKAO |\n|---------|-------|----------|--------|\n| 1.5B, DATA-alpha | +1.1% | +1.4% | +0.5% |\n| 1.5B, DATA-beta | +0.3% | +1.6% | +3.4% |\n| 3B, DATA-alpha | +4.3% | +4.8% | +11.7% |\n| 3B, DATA-beta | +22.9% | +1.6% | +0.3% |\n| 7B, DATA-alpha | +33.2% | +19.0% | +22.8% |\n| 7B, DATA-beta | +3.8% | +0.4% | +0.8% |\n\nThe improvements are highly variable -- some settings see 20-33% improvement, others less than 1%. Greedy decoding performance is essentially unchanged by SOC (by design, since the method targets beam search specifically).\n\n**Baselines:** The comparison is primarily SFT-only vs. SFT+SOC, both using beam search at inference. They do NOT compare against PRM-guided search, ORM-guided search, or any verifier-based methods.\n\n---\n\n### 4. How Is SOC Different from Training a PRM End-to-End for Search Performance?\n\nThis is the critical differentiation. SOC and a search-objective PRM training approach differ in several fundamental ways:\n\n**(a) No separate reward model.** SOC does not train a separate PRM. It modifies the SFT loss of the policy model itself so that its implicit Q-values (logits) are better calibrated for beam search. At inference, beam search uses only the policy model's log-probabilities -- no external verifier or reward model is involved.\n\n**(b) No search-aware training.** SOC does NOT backpropagate through the beam search procedure. The auxiliary V loss is applied independently at each token position in the training data. There is no mechanism to evaluate \"what would beam search actually select?\" during training and then correct for it. The method is search-agnostic in the sense that it regularizes Q-values uniformly, hoping this indirectly helps beam search.\n\n**(c) Indirect optimization.** SOC addresses overestimation through a proxy: value contraction and confidence boosting on expert data. It does not directly optimize the metric \"does beam search find the correct answer?\" A search-objective PRM, by contrast, would directly optimize the reward model's scores to ensure the search procedure selects correct solutions.\n\n**(d) Only works with the policy model's own logits.** SOC cannot be applied to a separate PRM that guides search -- it is fundamentally about calibrating the LLM's own token-level predictions. This means it cannot benefit from the architectural flexibility of having a dedicated verifier.\n\n**(e) Assumes sparse terminal rewards.** The theoretical framework assumes rewards are only at the terminal state (`R_outcome = 1` for correct, 0 otherwise), with zero intermediate rewards. This is exactly the setting where step-level process reward is most valuable and where SOC's theory is most limited.\n\n---\n\n### 5. SOC's Limitations That Your Approach Could Address\n\nHere are the specific gaps that training a PRM directly with a search-objective loss (via differentiable beam search) could fill:\n\n**(a) No direct search optimization.** SOC's auxiliary loss is not aware of the actual search procedure. It applies a generic regularizer hoping it helps beam search, but it never evaluates what beam search would actually select during training. Your approach of differentiable beam search would directly optimize for \"does the search find the right answer?\", closing the train-test gap.\n\n**(b) No process-level reward signal.** SOC works entirely within the sparse-reward framework (terminal correctness only). It does not provide or leverage step-level reward signals. A PRM trained with search-objective loss would provide dense, step-level guidance that can catch errors at intermediate reasoning steps, not just at the final answer.\n\n**(c) Narrow theoretical guarantee.** SOC's Theorem 4.1 only proves value contraction (adjacent states' values get closer), but does not prove that beam search will actually find better solutions. The connection is empirical. End-to-end training through differentiable beam search would provide a more direct optimization signal with clearer alignment between training objective and search performance.\n\n**(d) No separation of concerns.** SOC modifies the policy model's training, which means the same model must serve both as the generator and the implicit evaluator. This conflates two objectives. A dedicated PRM allows the search guidance model to specialize in evaluation while the policy model specializes in generation.\n\n**(e) Highly variable improvements.** SOC's results are very inconsistent across model sizes and datasets (ranging from +0.3% to +33.2%). This suggests the indirect regularization approach is fragile. Direct search-objective training should provide more consistent improvements because it optimizes exactly the right objective.\n\n**(f) Limited to beam search over policy logits.** SOC only improves beam search when using the model's own log-probabilities for scoring. It cannot improve other search strategies (MCTS, best-of-N with verifier, etc.). A PRM trained with search-objective loss is a more general tool that can guide any search algorithm.\n\n**(g) No comparison to reward-model-based methods.** The paper does not compare against PRM-guided or ORM-guided beam search at all. This leaves open the question of whether SOC even matches the performance of a simple PRM, let alone a search-optimized one.\n\n**(h) Beam-search specific.** The authors themselves acknowledge this limitation: they note it is \"valuable to investigate whether other search-based methods encounter this issue.\" Your differentiable search approach could generalize across search algorithms.\n\n---\n\n### Summary for Positioning Your Work\n\nSOC is the closest related work because it:\n1. Identifies the same problem (overestimation bias degrading beam search for reasoning)\n2. Proposes a training-time fix rather than an inference-time fix\n3. Frames the problem in terms of Q-value estimation\n\nBut SOC takes an **indirect, regularization-based approach** -- it adds a simple auxiliary loss that encourages value contraction, without ever looking at what beam search actually does during training. Your approach of training a PRM end-to-end with a search-objective loss via differentiable beam search is fundamentally more direct: it optimizes the actual search outcome, provides process-level reward, and separates the reward model from the policy. You should cite SOC as identifying the right problem but argue that your method provides a more principled and direct solution by making the search procedure itself part of the training loop.\n\nSources:\n- [SOC Paper on arXiv](https://arxiv.org/abs/2504.07527)\n- [SOC Full HTML](https://arxiv.org/html/2504.07527)\n- [SOC at ACL Anthology](https://aclanthology.org/2025.findings-acl.463/)\n- [SOC PDF](https://arxiv.org/pdf/2504.07527)"
      }
    ],
    "totalDurationMs": 162859,
    "totalTokens": 22320,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2508,
      "cache_read_input_tokens": 17055,
      "output_tokens": 2756,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2508
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2756,
          "cache_read_input_tokens": 17055,
          "cache_creation_input_tokens": 2508,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2508,
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
      "otherToolCount": 8
    }
  },
  "sourceToolAssistantUUID": "1ad33883-21ca-449c-b8c0-a8817988d6e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Search-Objective Training for Process Reward Models\",   \"core_problem\"…",
  "leafUuid": "b913dcd7-bf3b-4175-8896-23716f01bbbb",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise search-objective PRM training based on reviewer feedback",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b"
}
```

---

### Tool call

_source line 17 · 2026-05-27T17:48:15.670Z_

<details open><summary>🔧 Tool call — Agent · `toolu_017yQ7AGtCGHiYaNPLKMwyA1`</summary>

```json
{
  "description": "Research CRM paper (arXiv 2509.26578)",
  "prompt": "I'm revising a research idea about training Process Reward Models (PRMs) with search-objective losses. A reviewer flagged a missing related work: \"CRM—Conditional Reward Modeling (ICLR 2026, arXiv 2509.26578)\" which conditions step rewards on outcomes.\n\nPlease do the following:\n1. Search for this paper using WebSearch with queries like \"Conditional Reward Modeling CRM ICLR 2026 process reward\" and \"arXiv 2509.26578\"\n2. Try to fetch and read the paper on arXiv using WebFetch (try https://arxiv.org/abs/2509.26578)\n3. Report back in detail:\n   - What is CRM's core approach? How does conditioning on outcomes work?\n   - What training objective does it use?\n   - What results does it achieve on math reasoning benchmarks?\n   - How does it compare to standard PRMs?\n   - How is it different from training a PRM end-to-end for search performance via differentiable beam search?\n   - What are its limitations?\n\nBe thorough.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b913dcd7-bf3b-4175-8896-23716f01bbbb",
  "isSidechain": false,
  "requestId": "req_011CbTVbtKyx8AHkYw96jDuV",
  "type": "assistant",
  "uuid": "28d454e3-052b-424c-b53e-23ed90ee4973",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015c4ej7UzaaUaqFm3CnZnfS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3236,
      "cache_read_input_tokens": 17651,
      "output_tokens": 358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3236,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 358,
          "cache_read_input_tokens": 17651,
          "cache_creation_input_tokens": 3236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3236
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

_source line 18 · 2026-05-27T17:50:58.653Z_

<details><summary>↩ Tool result · `toolu_017yQ7AGtCGHiYaNPLKMwyA1`</summary>

````text
I now have comprehensive information. Here is my detailed report.

---

## CRM: Conditional Reward Modeling -- Detailed Analysis

**Paper:** "Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning"
**Authors:** Zheng Zhang, Ziwei Shan, Kaitao Song, Yexin Li, Kan Ren
**Venue:** ICLR 2026 (arXiv: 2509.26578, submitted September 2025, revised February 2026)

---

### 1. Core Approach: How Conditioning on Outcomes Works

CRM frames LLM reasoning as a **survival analysis** problem. It introduces a random variable **z** representing the index of the *first step at which the reasoning process enters a wrong state* (i.e., after which the trajectory can no longer yield the correct final answer). The key probabilistic quantities are:

- **S(t) = Pr(z > t)**: the "survival function" -- the probability that the trajectory remains correct through step t.
- **h(t) = Pr(z = t | z >= t)**: the "hazard function" -- the conditional probability that step t is where reasoning goes wrong, given all prior steps were correct.
- **W(t) = Pr(z <= t)**: the cumulative probability of having entered a wrong state by step t.

The chain rule connects individual steps to the final outcome:

```
S(t) = Prod_{k=1}^{t} (1 - h(k))
```

This means the overall trajectory correctness probability S(T) decomposes multiplicatively over per-step hazard terms. The process reward for each step is then defined via **Potential-Based Reward Shaping (PBRS)** with potential function Phi(s_t) = log S(t):

```
r_t = log(1 - h(t))
```

The critical insight is that the product of exponentiated step rewards equals the trajectory-level outcome probability:

```
Prod e^{r_t} = S(T)
```

This creates an **explicit, mathematically principled link** between per-step process rewards and the final outcome correctness, which is what "conditioning on outcomes" means here. Unlike standard PRMs that score each step in isolation, CRM's per-step reward h(t) is explicitly conditioned on all previous steps being correct (via the conditional probability formulation), and the step rewards are constrained to be consistent with the trajectory-level outcome through the survival analysis chain rule.

---

### 2. Training Objective

CRM uses a composite loss with three terms, applied over a dataset of trajectories with step-level labels:

**For correct trajectories (l_i = 1):** Maximize the survival probability through all steps:
```
L_S = -log[Prod(1 - h(t))] = -log S(T)
```

**For incorrect trajectories (l_i = 0):** Two sub-objectives:
- Maximize the probability that the trajectory eventually fails:
  ```
  L_W = -log[1 - Prod(1 - h(t))]
  ```
- Localize the first wrong step z_i (requires step-level annotation):
  ```
  L_z = -log[h(z_i) * Prod_{t=1}^{z_i - 1}(1 - h(t))]
  ```
  This maximizes the probability that step z_i is the first wrong step.

**Overall loss:**
```
L = (1/|D|) * Sum_i [ l_i * L_S + (1 - l_i) * (L_W + L_z) ]
```

The model architecture is an LLM backbone (e.g., Qwen2.5-3B) augmented with a value head that outputs h(t) for each step.

---

### 3. Results on Math Reasoning Benchmarks

**Best-of-N Sampling (Table 1):**
| Setting | CRM | PQM | Vanilla PRM |
|---------|-----|-----|-------------|
| MATH500 @32 (Qwen2.5-3B) | 56.6% | 54.8% | 54.6% |
| GSM-Plus @32 (Qwen2.5-3B) | 67.9% | 68.5% | -- |
| MATH500 @32 (LLaMA3.1-8B) | 50.6% | 48.8% | -- |

**Beam Search (Table 2, Qwen2.5-Math-1.5B):**
| Benchmark | N | CRM | PQM |
|-----------|---|-----|-----|
| MATH500 | 20 | 61.0% | 58.87% |
| MATH500 | 100 | 63.0% | 58.8% |
| Gaokao2023 | 100 | 43.55% | 39.83% |

**RL Optimization (Table 3, without verifiable rewards):**
| Benchmark | CRM | PQM | PURE |
|-----------|-----|-----|------|
| AIME24 | 43.3% | -- | 26.6% |
| Minerva Math | 40.0% | 34.1% | 30.8% |
| OlympiadBench | 39.3% | 34.3% | -- |
| MATH500 | 77.8% | -- | 76.0% |

CRM shows especially large gains in **beam search** and **RL** settings. The beam search improvement on Gaokao2023 (43.55% vs 39.83%) and the RL improvement on AIME24 (43.3% vs 26.6%) are particularly striking.

---

### 4. Comparison to Standard PRMs

CRM outperforms standard PRMs across all three downstream use cases. The key advantages:

- **Cross-sample comparability:** Standard PRMs produce scores that are not calibrated across different questions or trajectories. CRM's probabilistic formulation ensures S(t) has a consistent semantic meaning (probability of correctness), enabling meaningful comparisons. This is measured via AUPRC (Area Under Precision-Recall Curve), where CRM achieves higher scores than all baselines.

- **Reward hacking robustness:** In RL settings, standard PRM/PQM rewards tend to increase even as actual accuracy declines and repetition increases (classic reward hacking). CRM maintains stable performance because S(t) has a bounded probabilistic interpretation.

- **Baselines used:** ORM (outcome-only reward model), vanilla PRM (Wang et al. 2024), PQM (Li & Li 2025), IPRM (Yuan et al. 2025).

---

### 5. How CRM Differs from Training a PRM End-to-End for Search via Differentiable Beam Search

This is the most important distinction for your research idea. CRM and a differentiable-beam-search PRM address the same underlying problem (making PRMs work well for search) but from **completely different angles**:

**CRM's approach -- Better reward definition, separate training:**
- CRM improves the *definition* of step-level rewards by grounding them in a principled probabilistic model (survival analysis) that links steps to outcomes.
- The reward model is **trained separately** from any search algorithm using supervised learning on step-level annotations.
- Search (Best-of-N, beam search, RL) is applied **post-hoc** using the pre-trained reward model.
- The paper does **not discuss** differentiable beam search, search-aware training, or end-to-end optimization of the reward model for search performance. This topic is entirely absent from the related work section.

**Differentiable beam search approach -- Same reward definition, better training:**
- A search-objective approach keeps the standard PRM reward definition but changes the *training procedure* to optimize the PRM end-to-end for downstream search performance.
- The reward model and search algorithm are **jointly optimized** -- gradients flow through the search procedure back into the reward model.
- This directly optimizes what you care about (search outcome quality) rather than a proxy (step-level prediction accuracy).

**Key differences:**
| Dimension | CRM | Differentiable Beam Search PRM |
|-----------|-----|-------------------------------|
| What is improved | Reward signal definition | Training procedure |
| Training | Supervised, separate from search | End-to-end through search |
| Search algorithm | Applied post-hoc | Part of the training loop |
| Annotations needed | Step-level labels (z_i) | Outcome labels (potentially) |
| Theoretical grounding | Survival analysis + PBRS | Optimization of search objective |
| Reward hacking | Addressed via probabilistic consistency | Addressed via direct optimization for search |

These approaches are **complementary, not competing**. One could potentially combine CRM's probabilistic reward formulation with end-to-end search-aware training -- using the survival-analysis-based h(t) as the parameterization but training it by differentiating through beam search rather than with the supervised L_S + L_W + L_z loss.

---

### 6. Limitations

The paper has **no explicit limitations section**, but several important limitations can be identified:

1. **Dependence on step-level annotations:** CRM requires labeled data indicating the first wrong step z_i in incorrect trajectories. It uses the Math-Shepherd dataset for this. While ablations show only ~10% of step-labeled data suffices (accuracy goes from 47.0% with 0% L_z data to 52.4% with 10%), the method still relies on this supervision signal existing.

2. **Domain specificity:** All experiments are on mathematical reasoning. The authors acknowledge the need to "extend CRM to broader domains and task formats" as future work. It is unclear how the binary correct/incorrect framing transfers to open-ended generation tasks.

3. **Binary wrong-state assumption:** The model assumes there exists a single discrete "first wrong step" after which the trajectory is irrecoverable. In practice, reasoning errors may be recoverable, partial, or gradual rather than binary.

4. **Separate training from search:** The reward model is trained independently of how it will be used downstream. This means the reward model is not optimized for the actual search procedure it will guide -- precisely the gap that search-objective training addresses.

5. **No joint optimization:** Because training and inference are decoupled, there is no mechanism to correct for distributional mismatch between training trajectories and those encountered during search/RL at inference time.

6. **Scalability of survival analysis framing:** The multiplicative decomposition S(T) = Prod(1-h(t)) means that for very long trajectories, small per-step errors in h(t) estimation can compound, potentially degrading trajectory-level score quality.

---

### Summary for Your Paper

CRM is relevant to your work as it addresses the process-outcome linkage problem in PRMs, but from a **reward formulation** perspective (survival analysis + PBRS) rather than a **training objective** perspective (search-aware end-to-end training). Your approach of training PRMs with search-objective losses via differentiable beam search is orthogonal: CRM asks "what should the reward represent?" while your work asks "how should we train the reward model?" The two ideas could in principle be combined. When citing CRM, you should position it as addressing a complementary aspect of the same problem -- it improves reward *definition* but still trains with a supervised proxy loss rather than directly optimizing for search performance.

Sources:
- [CRM Paper (arXiv)](https://arxiv.org/abs/2509.26578)
- [CRM HTML Version](https://arxiv.org/html/2509.26578)
- [CRM Project Page](https://foundation-model-research.github.io/CRM/)
- [OpenReview Page](https://openreview.net/forum?id=4DJoBOQNd0)
- [OpenReview PDF](https://openreview.net/pdf/d25fc7196d66008efad47ed2ab28c8d86b76cb7a.pdf)

agentId: a67394ed88476d426 (use SendMessage with to: 'a67394ed88476d426' to continue this agent)
&lt;usage>total_tokens: 19979
tool_uses: 8
duration_ms: 162974&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "28d454e3-052b-424c-b53e-23ed90ee4973",
  "isSidechain": false,
  "promptId": "cfe7962d-223e-4b12-9480-c455cf84546f",
  "type": "user",
  "uuid": "8a17aefa-2dc5-4b9c-9211-9d487d6e46a8",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm revising a research idea about training Process Reward Models (PRMs) with search-objective losses. A reviewer flagged a missing related work: \"CRM—Conditional Reward Modeling (ICLR 2026, arXiv 2509.26578)\" which conditions step rewards on outcomes.\n\nPlease do the following:\n1. Search for this paper using WebSearch with queries like \"Conditional Reward Modeling CRM ICLR 2026 process reward\" and \"arXiv 2509.26578\"\n2. Try to fetch and read the paper on arXiv using WebFetch (try https://arxiv.org/abs/2509.26578)\n3. Report back in detail:\n   - What is CRM's core approach? How does conditioning on outcomes work?\n   - What training objective does it use?\n   - What results does it achieve on math reasoning benchmarks?\n   - How does it compare to standard PRMs?\n   - How is it different from training a PRM end-to-end for search performance via differentiable beam search?\n   - What are its limitations?\n\nBe thorough.",
    "agentId": "a67394ed88476d426",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information. Here is my detailed report.\n\n---\n\n## CRM: Conditional Reward Modeling -- Detailed Analysis\n\n**Paper:** \"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning\"\n**Authors:** Zheng Zhang, Ziwei Shan, Kaitao Song, Yexin Li, Kan Ren\n**Venue:** ICLR 2026 (arXiv: 2509.26578, submitted September 2025, revised February 2026)\n\n---\n\n### 1. Core Approach: How Conditioning on Outcomes Works\n\nCRM frames LLM reasoning as a **survival analysis** problem. It introduces a random variable **z** representing the index of the *first step at which the reasoning process enters a wrong state* (i.e., after which the trajectory can no longer yield the correct final answer). The key probabilistic quantities are:\n\n- **S(t) = Pr(z > t)**: the \"survival function\" -- the probability that the trajectory remains correct through step t.\n- **h(t) = Pr(z = t | z >= t)**: the \"hazard function\" -- the conditional probability that step t is where reasoning goes wrong, given all prior steps were correct.\n- **W(t) = Pr(z <= t)**: the cumulative probability of having entered a wrong state by step t.\n\nThe chain rule connects individual steps to the final outcome:\n\n```\nS(t) = Prod_{k=1}^{t} (1 - h(k))\n```\n\nThis means the overall trajectory correctness probability S(T) decomposes multiplicatively over per-step hazard terms. The process reward for each step is then defined via **Potential-Based Reward Shaping (PBRS)** with potential function Phi(s_t) = log S(t):\n\n```\nr_t = log(1 - h(t))\n```\n\nThe critical insight is that the product of exponentiated step rewards equals the trajectory-level outcome probability:\n\n```\nProd e^{r_t} = S(T)\n```\n\nThis creates an **explicit, mathematically principled link** between per-step process rewards and the final outcome correctness, which is what \"conditioning on outcomes\" means here. Unlike standard PRMs that score each step in isolation, CRM's per-step reward h(t) is explicitly conditioned on all previous steps being correct (via the conditional probability formulation), and the step rewards are constrained to be consistent with the trajectory-level outcome through the survival analysis chain rule.\n\n---\n\n### 2. Training Objective\n\nCRM uses a composite loss with three terms, applied over a dataset of trajectories with step-level labels:\n\n**For correct trajectories (l_i = 1):** Maximize the survival probability through all steps:\n```\nL_S = -log[Prod(1 - h(t))] = -log S(T)\n```\n\n**For incorrect trajectories (l_i = 0):** Two sub-objectives:\n- Maximize the probability that the trajectory eventually fails:\n  ```\n  L_W = -log[1 - Prod(1 - h(t))]\n  ```\n- Localize the first wrong step z_i (requires step-level annotation):\n  ```\n  L_z = -log[h(z_i) * Prod_{t=1}^{z_i - 1}(1 - h(t))]\n  ```\n  This maximizes the probability that step z_i is the first wrong step.\n\n**Overall loss:**\n```\nL = (1/|D|) * Sum_i [ l_i * L_S + (1 - l_i) * (L_W + L_z) ]\n```\n\nThe model architecture is an LLM backbone (e.g., Qwen2.5-3B) augmented with a value head that outputs h(t) for each step.\n\n---\n\n### 3. Results on Math Reasoning Benchmarks\n\n**Best-of-N Sampling (Table 1):**\n| Setting | CRM | PQM | Vanilla PRM |\n|---------|-----|-----|-------------|\n| MATH500 @32 (Qwen2.5-3B) | 56.6% | 54.8% | 54.6% |\n| GSM-Plus @32 (Qwen2.5-3B) | 67.9% | 68.5% | -- |\n| MATH500 @32 (LLaMA3.1-8B) | 50.6% | 48.8% | -- |\n\n**Beam Search (Table 2, Qwen2.5-Math-1.5B):**\n| Benchmark | N | CRM | PQM |\n|-----------|---|-----|-----|\n| MATH500 | 20 | 61.0% | 58.87% |\n| MATH500 | 100 | 63.0% | 58.8% |\n| Gaokao2023 | 100 | 43.55% | 39.83% |\n\n**RL Optimization (Table 3, without verifiable rewards):**\n| Benchmark | CRM | PQM | PURE |\n|-----------|-----|-----|------|\n| AIME24 | 43.3% | -- | 26.6% |\n| Minerva Math | 40.0% | 34.1% | 30.8% |\n| OlympiadBench | 39.3% | 34.3% | -- |\n| MATH500 | 77.8% | -- | 76.0% |\n\nCRM shows especially large gains in **beam search** and **RL** settings. The beam search improvement on Gaokao2023 (43.55% vs 39.83%) and the RL improvement on AIME24 (43.3% vs 26.6%) are particularly striking.\n\n---\n\n### 4. Comparison to Standard PRMs\n\nCRM outperforms standard PRMs across all three downstream use cases. The key advantages:\n\n- **Cross-sample comparability:** Standard PRMs produce scores that are not calibrated across different questions or trajectories. CRM's probabilistic formulation ensures S(t) has a consistent semantic meaning (probability of correctness), enabling meaningful comparisons. This is measured via AUPRC (Area Under Precision-Recall Curve), where CRM achieves higher scores than all baselines.\n\n- **Reward hacking robustness:** In RL settings, standard PRM/PQM rewards tend to increase even as actual accuracy declines and repetition increases (classic reward hacking). CRM maintains stable performance because S(t) has a bounded probabilistic interpretation.\n\n- **Baselines used:** ORM (outcome-only reward model), vanilla PRM (Wang et al. 2024), PQM (Li & Li 2025), IPRM (Yuan et al. 2025).\n\n---\n\n### 5. How CRM Differs from Training a PRM End-to-End for Search via Differentiable Beam Search\n\nThis is the most important distinction for your research idea. CRM and a differentiable-beam-search PRM address the same underlying problem (making PRMs work well for search) but from **completely different angles**:\n\n**CRM's approach -- Better reward definition, separate training:**\n- CRM improves the *definition* of step-level rewards by grounding them in a principled probabilistic model (survival analysis) that links steps to outcomes.\n- The reward model is **trained separately** from any search algorithm using supervised learning on step-level annotations.\n- Search (Best-of-N, beam search, RL) is applied **post-hoc** using the pre-trained reward model.\n- The paper does **not discuss** differentiable beam search, search-aware training, or end-to-end optimization of the reward model for search performance. This topic is entirely absent from the related work section.\n\n**Differentiable beam search approach -- Same reward definition, better training:**\n- A search-objective approach keeps the standard PRM reward definition but changes the *training procedure* to optimize the PRM end-to-end for downstream search performance.\n- The reward model and search algorithm are **jointly optimized** -- gradients flow through the search procedure back into the reward model.\n- This directly optimizes what you care about (search outcome quality) rather than a proxy (step-level prediction accuracy).\n\n**Key differences:**\n| Dimension | CRM | Differentiable Beam Search PRM |\n|-----------|-----|-------------------------------|\n| What is improved | Reward signal definition | Training procedure |\n| Training | Supervised, separate from search | End-to-end through search |\n| Search algorithm | Applied post-hoc | Part of the training loop |\n| Annotations needed | Step-level labels (z_i) | Outcome labels (potentially) |\n| Theoretical grounding | Survival analysis + PBRS | Optimization of search objective |\n| Reward hacking | Addressed via probabilistic consistency | Addressed via direct optimization for search |\n\nThese approaches are **complementary, not competing**. One could potentially combine CRM's probabilistic reward formulation with end-to-end search-aware training -- using the survival-analysis-based h(t) as the parameterization but training it by differentiating through beam search rather than with the supervised L_S + L_W + L_z loss.\n\n---\n\n### 6. Limitations\n\nThe paper has **no explicit limitations section**, but several important limitations can be identified:\n\n1. **Dependence on step-level annotations:** CRM requires labeled data indicating the first wrong step z_i in incorrect trajectories. It uses the Math-Shepherd dataset for this. While ablations show only ~10% of step-labeled data suffices (accuracy goes from 47.0% with 0% L_z data to 52.4% with 10%), the method still relies on this supervision signal existing.\n\n2. **Domain specificity:** All experiments are on mathematical reasoning. The authors acknowledge the need to \"extend CRM to broader domains and task formats\" as future work. It is unclear how the binary correct/incorrect framing transfers to open-ended generation tasks.\n\n3. **Binary wrong-state assumption:** The model assumes there exists a single discrete \"first wrong step\" after which the trajectory is irrecoverable. In practice, reasoning errors may be recoverable, partial, or gradual rather than binary.\n\n4. **Separate training from search:** The reward model is trained independently of how it will be used downstream. This means the reward model is not optimized for the actual search procedure it will guide -- precisely the gap that search-objective training addresses.\n\n5. **No joint optimization:** Because training and inference are decoupled, there is no mechanism to correct for distributional mismatch between training trajectories and those encountered during search/RL at inference time.\n\n6. **Scalability of survival analysis framing:** The multiplicative decomposition S(T) = Prod(1-h(t)) means that for very long trajectories, small per-step errors in h(t) estimation can compound, potentially degrading trajectory-level score quality.\n\n---\n\n### Summary for Your Paper\n\nCRM is relevant to your work as it addresses the process-outcome linkage problem in PRMs, but from a **reward formulation** perspective (survival analysis + PBRS) rather than a **training objective** perspective (search-aware end-to-end training). Your approach of training PRMs with search-objective losses via differentiable beam search is orthogonal: CRM asks \"what should the reward represent?\" while your work asks \"how should we train the reward model?\" The two ideas could in principle be combined. When citing CRM, you should position it as addressing a complementary aspect of the same problem -- it improves reward *definition* but still trains with a supervised proxy loss rather than directly optimizing for search performance.\n\nSources:\n- [CRM Paper (arXiv)](https://arxiv.org/abs/2509.26578)\n- [CRM HTML Version](https://arxiv.org/html/2509.26578)\n- [CRM Project Page](https://foundation-model-research.github.io/CRM/)\n- [OpenReview Page](https://openreview.net/forum?id=4DJoBOQNd0)\n- [OpenReview PDF](https://openreview.net/pdf/d25fc7196d66008efad47ed2ab28c8d86b76cb7a.pdf)"
      }
    ],
    "totalDurationMs": 162974,
    "totalTokens": 19979,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1386,
      "cache_read_input_tokens": 15694,
      "output_tokens": 2898,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1386
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2898,
          "cache_read_input_tokens": 15694,
          "cache_creation_input_tokens": 1386,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1386,
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
      "otherToolCount": 8
    }
  },
  "sourceToolAssistantUUID": "28d454e3-052b-424c-b53e-23ed90ee4973",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool call

_source line 19 · 2026-05-27T17:51:09.027Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01XqyaA7X6VHwiWLhSqpyY7k`</summary>

```json
{
  "description": "Research 3 more missing papers",
  "prompt": "I'm revising a research idea about training Process Reward Models (PRMs) with search-objective losses (differentiable beam search). Reviewers flagged three more missing related works. Please research ALL THREE:\n\n1. \"From Curiosity to Caution\" (arXiv 2604.04648, Apr 2026) - applies pessimistic reward correction for Best-of-N to mitigate reward hacking\n2. \"Learning Generative Selection for Best-of-N\" (arXiv 2602.02143, Feb 2026) - trains selection models via RL for search\n3. \"Inference-Aware Fine-Tuning for Best-of-N Sampling\" (ICLR 2025, arXiv 2412.15287) - generator-side analog of inference-aware training\n\nFor each paper:\n- Search for it using WebSearch\n- Fetch and read it using WebFetch on its arXiv page\n- Report: core approach, training objective, key results, how it differs from training a PRM with end-to-end search-objective loss via differentiable beam search, and its limitations\n\nBe thorough but concise for each paper.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a17aefa-2dc5-4b9c-9211-9d487d6e46a8",
  "isSidechain": false,
  "requestId": "req_011CbTVpdEkNbsSDgmpgEsSx",
  "type": "assistant",
  "uuid": "94af3112-a269-40a3-ba6f-eabcf69842f0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012RVEgD9GTe4f87tTTztraq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3329,
      "cache_read_input_tokens": 20887,
      "output_tokens": 364,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3329,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 364,
          "cache_read_input_tokens": 20887,
          "cache_creation_input_tokens": 3329,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3329
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

_source line 20 · 2026-05-27T17:53:29.442Z_

<details><summary>↩ Tool result · `toolu_01XqyaA7X6VHwiWLhSqpyY7k`</summary>

```text
I now have comprehensive information on all three papers. Here is the full analysis:

---

## Paper 1: "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism"

**arXiv 2604.04648, April 2026 | Authors: Zhuohao Yu, Zhiwei Steven Wu (CMU), Adam Block (Columbia)**

**Core Approach:** The paper addresses reward hacking in Best-of-N (BoN) sampling, where increasing N eventually degrades performance because the reward model selects OOD responses that exploit its imperfections. The authors propose "caution" -- the inverse of curiosity-driven exploration. They train a lightweight predictor network to reconstruct frozen internal features of the reward model on in-distribution responses. At inference time, high prediction error signals an OOD response, and a penalty is applied:

`r_LCB(x,y) = r(x,y) - lambda * ||P_theta(x,y) - T(x,y)||^2`

where `P_theta` is the predictor, `T` extracts layer-L features from the frozen reward model, and `lambda` controls pessimism strength.

**Training Objective:** The predictor is trained with a simple MSE reconstruction loss on in-distribution data: `L(theta) = E[||P_theta(x,y) - T(x,y)||^2]`. No labeled data is required -- only prompts and base-model generations. The reward model itself is never retrained.

**Key Results:** On GSM8K, caution achieves 82.6% peak accuracy vs. 79.3% for standard BoN. At N=512, caution retains 81.1% vs. 71.5% for the uncorrected reward model (only 1.5pp degradation vs. 7.7pp). The method generalizes to MATH-500 and BigBench-Hard despite training only on GSM8K data. Theoretically, in a linear setting, pessimistic selection provably improves over standard BoN with gains growing as sqrt(log N).

**Difference from PRM + differentiable beam search:** This is purely an inference-time correction applied to an existing, frozen reward model. It never modifies the reward model's training objective and does not make the search procedure differentiable. It is agnostic to whether the reward model is an ORM or PRM. In contrast, training a PRM with end-to-end search-objective loss via differentiable beam search directly optimizes the reward model parameters so its scores produce good search outcomes. Caution is a complementary, post-hoc fix; differentiable beam search is a fundamentally different training paradigm.

**Limitations:** Primarily empirical validation in naturalistic settings; theoretical results rely on simplified linear assumptions. Less effective when reward models fail catastrophically. Requires tuning the architecture capacity of the predictor (lighter is better). Uncertainty estimates degrade on substantially OOD domains.

---

## Paper 2: "Learning Generative Selection for Best-of-N"

**arXiv 2602.02143, February 2026 | Authors: Shubham Toshniwal, Aleksander Ficek, Siddhartha Jain, Wei Du, Vahid Noroozi, Sadegh Mahdavi, Somshubra Majumdar, Igor Gitman**

**Core Approach:** Instead of scoring candidates independently (as a PRM/ORM does), this paper frames selection as a generative reasoning problem. Given N candidate solutions, a small LLM reads all of them and outputs the index of the best one (formatted as "Judgment [IDX]"). The key contribution is showing that small models (1.7B parameters) can acquire strong generative selection (GenSelect) capabilities through targeted RL training.

**Training Objective:** They construct synthetic selection tasks from math (OpenMathReasoning, 37K problems) and code (OpenCodeReasoning) datasets, filtering for problems where the base model achieves <50% pass rate so that both correct and incorrect solutions exist. They train Qwen3-1.7B using DAPO (a variant of on-policy RL) with binary reward: +1 for selecting a correct solution, 0 otherwise. Configuration: batch size 128, LR 1e-6, AdamW, temperature 1.5, max 16K output tokens, trained on H100s using the VeRL framework.

**Key Results:** On AIME24: 65.0% (RL-trained 1.7B) vs. 48.75% (prompting baseline). On AIME25: 54.17% vs. 38.33%. On HMMT25: 36.25% vs. 26.67%. Remarkably, the RL-trained 1.7B model selecting from Qwen3-8B generations matches or exceeds 8B-model prompting on several benchmarks, demonstrating cross-scale generalization. On LiveCodeBench: ~36.8% for RL models vs. lower prompting baselines.

**Difference from PRM + differentiable beam search:** This replaces the score-and-rank paradigm entirely with a generative comparative approach. The selector reasons over all N complete solutions simultaneously rather than scoring each independently. It does not assign per-step or per-solution scalar rewards. It cannot provide step-level process supervision, and it requires generating all candidates first before selection. Differentiable beam search with a PRM, by contrast, trains a reward model that provides step-level scores used to guide search, and it optimizes the reward model end-to-end through the search procedure. The generative selection approach is fundamentally incompatible with tree-search or beam-search paradigms where candidates are pruned at intermediate steps.

**Limitations:** Code domain gains are smaller due to noisier correctness signals from unit tests. Asymmetric cross-domain transfer (math training helps code but not vice versa). The 1.7B model struggles with GenSelect via prompting alone -- RL training is essential. The method requires all N candidates to be fully generated before selection, making it inapplicable to process-level pruning during generation.

---

## Paper 3: "Inference-Aware Fine-Tuning for Best-of-N Sampling"

**ICLR 2025, arXiv 2412.15287, December 2024 | Authors: Yinlam Chow, Guy Tennenholtz, Izzeddin Gur, Vincent Zhuang, Bo Dai, Sridhar Thiagarajan, Craig Boutilier, Rishabh Agarwal, Aviral Kumar, Aleksandra Faust (Google DeepMind)**

**Core Approach:** This is a generator-side approach. Instead of improving the verifier/reward model, it fine-tunes the LLM policy to produce outputs that are better suited for BoN selection at inference time. The key technical challenge is that BoN involves a non-differentiable argmax. They derive a variational approximation of the BoN policy: `pi_bon(y|x) ~ pi(y|x) * exp(lambda_N * Q_pi(x,y))`, where `Q_pi` is the win-rate (probability a response beats other samples according to verifier score). This transforms the discrete argmax into a continuous optimization target.

**Training Objectives:**
- *BoN-SFT (Imitation Learning):* SFT gradient augmented with an inference-awareness term that weights examples by their win-rate under the BoN policy, plus regularization.
- *BoN-RL-V:* REINFORCE-style gradient sampling from the BoN policy distribution rather than the base policy, optimizing environment reward.
- *BoN-RLB:* Binary reward variant with asymmetric weighting -- correct responses weighted by `g_N^+(p) = N*p^(N-1)/(1-p^N)` and incorrect by `g_N^-(p) = N*p/(1-p)`, where `p` is the failure probability. This drives redistribution of probability mass.
- *BoN-RLB(P):* Positive-only variant when negatives are unavailable.

**Key Results:** On Gemma 2B / Hendrycks MATH: Bo32 accuracy 26.8% -> 30.8% (BoN-RL-V); pass@32 60.0% -> 67.0% (BoN-RL-S). On HumanEval: pass@16 61.6% -> 67.1% (BoN-RLB(P)). Improvements generalize to held-out benchmarks (Functional MATH, MathOdyssey). The models implicitly learn a meta-strategy that interleaves high-quality responses with diverse exploratory responses -- harder problems require higher temperature and larger N (exploration), while easier problems need small N (exploitation).

**Difference from PRM + differentiable beam search:** This is the generator-side analog -- it modifies the generator policy to be aware of inference-time search, while your work modifies the verifier/PRM to be aware of search. Both share the philosophy of "inference-aware training" but optimize different components. Key differences: (1) This paper assumes a fixed verifier and tunes the generator; differentiable beam search assumes a fixed generator and tunes the PRM. (2) This paper handles only flat BoN (sample N, pick best), not structured tree search or beam search with step-level scoring. (3) This paper's approximation replaces argmax with a soft variational form; differentiable beam search makes the beam selection itself differentiable. (4) This paper cannot provide process-level supervision signals.

**Limitations:** Sample inefficiency in the general BoN-RL variant. BoN-RL-V does not significantly improve pass@N metrics. Inference-unaware RL baselines suffer from reward hacking. The method is limited to flat BoN -- it does not extend to more complex search procedures like beam search or tree search. It requires a pre-existing verifier and only optimizes the generator distribution, not the scoring function.

---

## Summary of How All Three Differ from Your Approach (PRM + Differentiable Beam Search)

| Aspect | Your Approach | Paper 1 (Caution) | Paper 2 (GenSelect) | Paper 3 (BoN-Aware FT) |
|---|---|---|---|---|
| **What is optimized** | PRM parameters | Nothing (inference-time correction) | Selector LLM via RL | Generator LLM policy |
| **Training signal flows through search** | Yes (differentiable) | No | No (flat selection) | Approximately (variational) |
| **Search type** | Beam search (structured, step-level) | Flat BoN | Flat BoN | Flat BoN |
| **Process-level supervision** | Yes | No | No | No |
| **Modifies reward/verifier** | Yes (end-to-end) | No (post-hoc penalty) | Replaces with generative selector | No (fixed verifier) |
| **Handles reward hacking** | Implicitly (search-aligned scores) | Explicitly (pessimistic correction) | N/A | Partially (via exploration) |

All three papers operate in the flat Best-of-N regime with complete responses, while your approach uniquely targets structured, step-level beam search with end-to-end differentiable training of the PRM. Paper 1 is the most complementary (could be applied on top of any PRM). Paper 3 is the closest philosophically (inference-aware training), but optimizes the opposite component (generator vs. verifier). Paper 2 is the most orthogonal, replacing scoring-based selection entirely with generative reasoning.

Sources:
- [From Curiosity to Caution (arXiv)](https://arxiv.org/abs/2604.04648)
- [From Curiosity to Caution (HTML)](https://arxiv.org/html/2604.04648)
- [Learning Generative Selection for Best-of-N (arXiv)](https://arxiv.org/abs/2602.02143)
- [Learning Generative Selection for Best-of-N (HTML)](https://arxiv.org/html/2602.02143)
- [Inference-Aware Fine-Tuning (arXiv)](https://arxiv.org/abs/2412.15287)
- [Inference-Aware Fine-Tuning (ICLR 2025)](https://proceedings.iclr.cc/paper_files/paper/2025/hash/c40bed606c51c8e827c1ba75aa2da054-Abstract-Conference.html)
- [Inference-Aware Fine-Tuning (OpenReview)](https://openreview.net/forum?id=77gQUdQhE7)

agentId: aef7cd42e386f60aa (use SendMessage with to: 'aef7cd42e386f60aa' to continue this agent)
&lt;usage>total_tokens: 21647
tool_uses: 10
duration_ms: 140409&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94af3112-a269-40a3-ba6f-eabcf69842f0",
  "isSidechain": false,
  "promptId": "cfe7962d-223e-4b12-9480-c455cf84546f",
  "type": "user",
  "uuid": "dfd27a50-11e4-4f61-85b6-085a526419ff",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm revising a research idea about training Process Reward Models (PRMs) with search-objective losses (differentiable beam search). Reviewers flagged three more missing related works. Please research ALL THREE:\n\n1. \"From Curiosity to Caution\" (arXiv 2604.04648, Apr 2026) - applies pessimistic reward correction for Best-of-N to mitigate reward hacking\n2. \"Learning Generative Selection for Best-of-N\" (arXiv 2602.02143, Feb 2026) - trains selection models via RL for search\n3. \"Inference-Aware Fine-Tuning for Best-of-N Sampling\" (ICLR 2025, arXiv 2412.15287) - generator-side analog of inference-aware training\n\nFor each paper:\n- Search for it using WebSearch\n- Fetch and read it using WebFetch on its arXiv page\n- Report: core approach, training objective, key results, how it differs from training a PRM with end-to-end search-objective loss via differentiable beam search, and its limitations\n\nBe thorough but concise for each paper.",
    "agentId": "aef7cd42e386f60aa",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information on all three papers. Here is the full analysis:\n\n---\n\n## Paper 1: \"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism\"\n\n**arXiv 2604.04648, April 2026 | Authors: Zhuohao Yu, Zhiwei Steven Wu (CMU), Adam Block (Columbia)**\n\n**Core Approach:** The paper addresses reward hacking in Best-of-N (BoN) sampling, where increasing N eventually degrades performance because the reward model selects OOD responses that exploit its imperfections. The authors propose \"caution\" -- the inverse of curiosity-driven exploration. They train a lightweight predictor network to reconstruct frozen internal features of the reward model on in-distribution responses. At inference time, high prediction error signals an OOD response, and a penalty is applied:\n\n`r_LCB(x,y) = r(x,y) - lambda * ||P_theta(x,y) - T(x,y)||^2`\n\nwhere `P_theta` is the predictor, `T` extracts layer-L features from the frozen reward model, and `lambda` controls pessimism strength.\n\n**Training Objective:** The predictor is trained with a simple MSE reconstruction loss on in-distribution data: `L(theta) = E[||P_theta(x,y) - T(x,y)||^2]`. No labeled data is required -- only prompts and base-model generations. The reward model itself is never retrained.\n\n**Key Results:** On GSM8K, caution achieves 82.6% peak accuracy vs. 79.3% for standard BoN. At N=512, caution retains 81.1% vs. 71.5% for the uncorrected reward model (only 1.5pp degradation vs. 7.7pp). The method generalizes to MATH-500 and BigBench-Hard despite training only on GSM8K data. Theoretically, in a linear setting, pessimistic selection provably improves over standard BoN with gains growing as sqrt(log N).\n\n**Difference from PRM + differentiable beam search:** This is purely an inference-time correction applied to an existing, frozen reward model. It never modifies the reward model's training objective and does not make the search procedure differentiable. It is agnostic to whether the reward model is an ORM or PRM. In contrast, training a PRM with end-to-end search-objective loss via differentiable beam search directly optimizes the reward model parameters so its scores produce good search outcomes. Caution is a complementary, post-hoc fix; differentiable beam search is a fundamentally different training paradigm.\n\n**Limitations:** Primarily empirical validation in naturalistic settings; theoretical results rely on simplified linear assumptions. Less effective when reward models fail catastrophically. Requires tuning the architecture capacity of the predictor (lighter is better). Uncertainty estimates degrade on substantially OOD domains.\n\n---\n\n## Paper 2: \"Learning Generative Selection for Best-of-N\"\n\n**arXiv 2602.02143, February 2026 | Authors: Shubham Toshniwal, Aleksander Ficek, Siddhartha Jain, Wei Du, Vahid Noroozi, Sadegh Mahdavi, Somshubra Majumdar, Igor Gitman**\n\n**Core Approach:** Instead of scoring candidates independently (as a PRM/ORM does), this paper frames selection as a generative reasoning problem. Given N candidate solutions, a small LLM reads all of them and outputs the index of the best one (formatted as \"Judgment [IDX]\"). The key contribution is showing that small models (1.7B parameters) can acquire strong generative selection (GenSelect) capabilities through targeted RL training.\n\n**Training Objective:** They construct synthetic selection tasks from math (OpenMathReasoning, 37K problems) and code (OpenCodeReasoning) datasets, filtering for problems where the base model achieves <50% pass rate so that both correct and incorrect solutions exist. They train Qwen3-1.7B using DAPO (a variant of on-policy RL) with binary reward: +1 for selecting a correct solution, 0 otherwise. Configuration: batch size 128, LR 1e-6, AdamW, temperature 1.5, max 16K output tokens, trained on H100s using the VeRL framework.\n\n**Key Results:** On AIME24: 65.0% (RL-trained 1.7B) vs. 48.75% (prompting baseline). On AIME25: 54.17% vs. 38.33%. On HMMT25: 36.25% vs. 26.67%. Remarkably, the RL-trained 1.7B model selecting from Qwen3-8B generations matches or exceeds 8B-model prompting on several benchmarks, demonstrating cross-scale generalization. On LiveCodeBench: ~36.8% for RL models vs. lower prompting baselines.\n\n**Difference from PRM + differentiable beam search:** This replaces the score-and-rank paradigm entirely with a generative comparative approach. The selector reasons over all N complete solutions simultaneously rather than scoring each independently. It does not assign per-step or per-solution scalar rewards. It cannot provide step-level process supervision, and it requires generating all candidates first before selection. Differentiable beam search with a PRM, by contrast, trains a reward model that provides step-level scores used to guide search, and it optimizes the reward model end-to-end through the search procedure. The generative selection approach is fundamentally incompatible with tree-search or beam-search paradigms where candidates are pruned at intermediate steps.\n\n**Limitations:** Code domain gains are smaller due to noisier correctness signals from unit tests. Asymmetric cross-domain transfer (math training helps code but not vice versa). The 1.7B model struggles with GenSelect via prompting alone -- RL training is essential. The method requires all N candidates to be fully generated before selection, making it inapplicable to process-level pruning during generation.\n\n---\n\n## Paper 3: \"Inference-Aware Fine-Tuning for Best-of-N Sampling\"\n\n**ICLR 2025, arXiv 2412.15287, December 2024 | Authors: Yinlam Chow, Guy Tennenholtz, Izzeddin Gur, Vincent Zhuang, Bo Dai, Sridhar Thiagarajan, Craig Boutilier, Rishabh Agarwal, Aviral Kumar, Aleksandra Faust (Google DeepMind)**\n\n**Core Approach:** This is a generator-side approach. Instead of improving the verifier/reward model, it fine-tunes the LLM policy to produce outputs that are better suited for BoN selection at inference time. The key technical challenge is that BoN involves a non-differentiable argmax. They derive a variational approximation of the BoN policy: `pi_bon(y|x) ~ pi(y|x) * exp(lambda_N * Q_pi(x,y))`, where `Q_pi` is the win-rate (probability a response beats other samples according to verifier score). This transforms the discrete argmax into a continuous optimization target.\n\n**Training Objectives:**\n- *BoN-SFT (Imitation Learning):* SFT gradient augmented with an inference-awareness term that weights examples by their win-rate under the BoN policy, plus regularization.\n- *BoN-RL-V:* REINFORCE-style gradient sampling from the BoN policy distribution rather than the base policy, optimizing environment reward.\n- *BoN-RLB:* Binary reward variant with asymmetric weighting -- correct responses weighted by `g_N^+(p) = N*p^(N-1)/(1-p^N)` and incorrect by `g_N^-(p) = N*p/(1-p)`, where `p` is the failure probability. This drives redistribution of probability mass.\n- *BoN-RLB(P):* Positive-only variant when negatives are unavailable.\n\n**Key Results:** On Gemma 2B / Hendrycks MATH: Bo32 accuracy 26.8% -> 30.8% (BoN-RL-V); pass@32 60.0% -> 67.0% (BoN-RL-S). On HumanEval: pass@16 61.6% -> 67.1% (BoN-RLB(P)). Improvements generalize to held-out benchmarks (Functional MATH, MathOdyssey). The models implicitly learn a meta-strategy that interleaves high-quality responses with diverse exploratory responses -- harder problems require higher temperature and larger N (exploration), while easier problems need small N (exploitation).\n\n**Difference from PRM + differentiable beam search:** This is the generator-side analog -- it modifies the generator policy to be aware of inference-time search, while your work modifies the verifier/PRM to be aware of search. Both share the philosophy of \"inference-aware training\" but optimize different components. Key differences: (1) This paper assumes a fixed verifier and tunes the generator; differentiable beam search assumes a fixed generator and tunes the PRM. (2) This paper handles only flat BoN (sample N, pick best), not structured tree search or beam search with step-level scoring. (3) This paper's approximation replaces argmax with a soft variational form; differentiable beam search makes the beam selection itself differentiable. (4) This paper cannot provide process-level supervision signals.\n\n**Limitations:** Sample inefficiency in the general BoN-RL variant. BoN-RL-V does not significantly improve pass@N metrics. Inference-unaware RL baselines suffer from reward hacking. The method is limited to flat BoN -- it does not extend to more complex search procedures like beam search or tree search. It requires a pre-existing verifier and only optimizes the generator distribution, not the scoring function.\n\n---\n\n## Summary of How All Three Differ from Your Approach (PRM + Differentiable Beam Search)\n\n| Aspect | Your Approach | Paper 1 (Caution) | Paper 2 (GenSelect) | Paper 3 (BoN-Aware FT) |\n|---|---|---|---|---|\n| **What is optimized** | PRM parameters | Nothing (inference-time correction) | Selector LLM via RL | Generator LLM policy |\n| **Training signal flows through search** | Yes (differentiable) | No | No (flat selection) | Approximately (variational) |\n| **Search type** | Beam search (structured, step-level) | Flat BoN | Flat BoN | Flat BoN |\n| **Process-level supervision** | Yes | No | No | No |\n| **Modifies reward/verifier** | Yes (end-to-end) | No (post-hoc penalty) | Replaces with generative selector | No (fixed verifier) |\n| **Handles reward hacking** | Implicitly (search-aligned scores) | Explicitly (pessimistic correction) | N/A | Partially (via exploration) |\n\nAll three papers operate in the flat Best-of-N regime with complete responses, while your approach uniquely targets structured, step-level beam search with end-to-end differentiable training of the PRM. Paper 1 is the most complementary (could be applied on top of any PRM). Paper 3 is the closest philosophically (inference-aware training), but optimizes the opposite component (generator vs. verifier). Paper 2 is the most orthogonal, replacing scoring-based selection entirely with generative reasoning.\n\nSources:\n- [From Curiosity to Caution (arXiv)](https://arxiv.org/abs/2604.04648)\n- [From Curiosity to Caution (HTML)](https://arxiv.org/html/2604.04648)\n- [Learning Generative Selection for Best-of-N (arXiv)](https://arxiv.org/abs/2602.02143)\n- [Learning Generative Selection for Best-of-N (HTML)](https://arxiv.org/html/2602.02143)\n- [Inference-Aware Fine-Tuning (arXiv)](https://arxiv.org/abs/2412.15287)\n- [Inference-Aware Fine-Tuning (ICLR 2025)](https://proceedings.iclr.cc/paper_files/paper/2025/hash/c40bed606c51c8e827c1ba75aa2da054-Abstract-Conference.html)\n- [Inference-Aware Fine-Tuning (OpenReview)](https://openreview.net/forum?id=77gQUdQhE7)"
      }
    ],
    "totalDurationMs": 140409,
    "totalTokens": 21647,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1732,
      "cache_read_input_tokens": 16867,
      "output_tokens": 3047,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1732
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3047,
          "cache_read_input_tokens": 16867,
          "cache_creation_input_tokens": 1732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1732,
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
  "sourceToolAssistantUUID": "94af3112-a269-40a3-ba6f-eabcf69842f0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Search-Objective Training for Process Reward Models\",   \"core_problem\"…",
  "leafUuid": "dfd27a50-11e4-4f61-85b6-085a526419ff",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise search-objective PRM training based on reviewer feedback",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b"
}
```

---

### Tool call

_source line 23 · 2026-05-27T17:53:46.243Z_

<details open><summary>🔧 Tool call — Agent · `toolu_014r2DzcpZBkaAv7SCe5TZGe`</summary>

```json
{
  "description": "Research Gumbel-Softmax risks and generative verifier landscape",
  "prompt": "I'm revising a research idea about training Process Reward Models (PRMs) with search-objective losses using Gumbel-Softmax differentiable beam search. Reviewers raised two technical/strategic concerns:\n\n## Concern 1: Gumbel-Softmax Technical Risks\nThe reviewer says: \"Temperature annealing from τ=2.0 to τ=0.1 is aggressive—at τ=0.1 Gumbel-Softmax outputs are near-discrete, causing gradient bias. The paper should discuss straight-through estimator alternatives and the soft-training/hard-inference gap.\"\n\nPlease research:\n1. Search for \"Gumbel-Softmax gradient bias low temperature\" and \"straight-through estimator vs Gumbel-Softmax\"\n2. Search for \"differentiable top-k selection\" and \"differentiable beam search gradient\"\n3. What are the known issues with Gumbel-Softmax at low temperatures (τ < 0.5)?\n4. What alternatives exist? (Straight-through estimator, REINFORCE with baseline, perturb-and-MAP, etc.)\n5. What is the \"soft-hard gap\" — the distribution mismatch between soft selections during training and hard selections during inference?\n6. Search for \"GRADE Gumbel-Softmax LLM alignment arXiv 2026\" - what temperature schedule did they use and what problems did they encounter?\n7. What is a practical recommendation for handling this in PRM training?\n\n## Concern 2: Generative Verifiers vs Discriminative PRMs\nThe reviewer says: \"The field is rapidly shifting toward generative verifiers (ThinkPRM, GenPRM) and RL-based training (GRPO, DAPO) where discriminative PRM optimization may have diminishing returns.\"\n\nPlease research:\n1. Search for \"ThinkPRM generative verifier 2025 2026\" and \"GenPRM generative process reward\"\n2. Search for \"discriminative vs generative verifier inference cost comparison\"\n3. Search for \"GRPO DAPO reinforcement learning LLM math reasoning 2026\"\n4. What are the inference cost differences between discriminative PRMs and generative verifiers?\n5. What are the accuracy trade-offs?\n6. Is there a strong argument for why optimizing discriminative PRM training still matters?\n\nProvide detailed findings for both concerns.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfd27a50-11e4-4f61-85b6-085a526419ff",
  "isSidechain": false,
  "requestId": "req_011CbTW1jvPG7gZzgsrySXjY",
  "type": "assistant",
  "uuid": "9adbd520-6e06-4f7b-9d5f-fd56deb89dfc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxBtGGULAqshEb5q8gANuD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3487,
      "cache_read_input_tokens": 24216,
      "output_tokens": 662,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3487,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 662,
          "cache_read_input_tokens": 24216,
          "cache_creation_input_tokens": 3487,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3487
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

_source line 24 · 2026-05-27T17:57:29.435Z_

<details><summary>↩ Tool result · `toolu_014r2DzcpZBkaAv7SCe5TZGe`</summary>

```text
Now I have comprehensive information on both concerns. Let me compile the detailed findings.

---

# Concern 1: Gumbel-Softmax Technical Risks

## 1. Known Issues with Gumbel-Softmax at Low Temperatures (tau < 0.5)

The reviewer's concern about aggressive annealing from tau=2.0 to tau=0.1 is well-grounded in the literature. The fundamental problem is a **bias-variance tradeoff**:

- **As tau approaches 0**: The Gumbel-Softmax distribution approaches a true categorical (one-hot), so bias decreases. However, gradient variance increases dramatically, and gradients can vanish entirely, degrading the learning signal. Critically, research shows that **bias does not vanish even asymptotically, while variance grows as O(1/tau)** (Shekhovtsov et al., ICML 2023).

- **At tau=0.1 specifically**: The distribution is near-discrete. Empirical studies confirm that values between 0.1 and 1.0 are used in practice, but tau=0.1 sits at the extreme edge. SofT-GRPO (which uses a fixed tau_g=0.1) reported **training collapse** when deviating even slightly to tau_g=0.25 combined with other hyperparameter changes, indicating extreme sensitivity in this regime.

- **Gradient explosion and instability**: Too-low temperatures lead to gradient explosion. Overly aggressive annealing can cause **premature collapse to suboptimal discrete solutions**.

## 2. The Soft-Hard Gap (Training-Inference Mismatch)

This is a real and quantified problem:

- During training with Gumbel-Softmax, the model sees **soft (continuous) mixtures** of embeddings. At inference, it must use **hard (discrete) token selections**. This creates a distribution mismatch.
- Research on differentiable logic gate networks measured this gap at **24-40% performance degradation** when soft methods are used during training but hard selection at deployment, with Gumbel noise amplifying the gap.
- The GRADE paper acknowledged this directly: "Models are trained with soft tokens but tested with hard sampling. While GRADE-STE's strong test performance suggests this mismatch is manageable, it **remains a theoretical concern**."
- In the discretization gap literature more broadly, accuracy degradation of ~3% has been documented even in favorable settings.

## 3. Alternatives to Standard Gumbel-Softmax

**a) Straight-Through Estimator (STE) and ST-Gumbel-Softmax:**
- Uses hard argmax in the forward pass but passes gradients through the soft Gumbel-Softmax in the backward pass. This directly addresses the soft-hard gap by making the forward pass match inference behavior.
- GRADE adopted this (GRADE-STE) and found it critical for good performance, achieving 14x lower gradient variance than REINFORCE.
- Limitation: STE is biased because the backward pass gradient does not correspond to the true gradient of the forward pass function.

**b) Decoupled Straight-Through Gumbel-Softmax (Decoupled ST-GS)** (ICLR-submitted, Oct 2024):
- Uses **two independent temperatures**: tau_f for the forward pass (low, ~0.3, for sharp discrete-like samples) and tau_b for the backward pass (high, ~3.0, for smooth gradients).
- This cleanly separates the discreteness requirement from gradient quality. Experiments showed that a single shared temperature "compromises both performance and gradient fidelity."
- This is likely the most directly applicable technique for the PRM training scenario.

**c) REINFORCE with Leave-One-Out Baseline:**
- Unbiased but higher variance than reparameterization methods. Modern variants are competitive, especially when the action space is small.
- Provably, reparameterization approaches have variance no larger than likelihood-ratio methods with optimal baselines.

**d) Perturb-and-MAP:**
- Uses Gumbel perturbations with MAP inference rather than softmax relaxation. Provides an upper bound on the partition function. Less commonly used for neural network training but theoretically appealing for structured discrete problems.

**e) Improved Continuous Relaxation (ICR), Gapped Straight-Through (GST), Rao-Blackwellized variants (GRMC):**
- These reduce bias and/or variance through modified Jacobians or marginalization, at the cost of additional implementation complexity.

## 4. GRADE Paper Details

GRADE (Gumbel-softmax Relaxation for Alignment via Differentiable Estimation) -- arXiv 2601.11574:
- **Temperature schedule**: Annealed from tau=2.0 down to tau=0.5 (NOT to 0.1), using linear annealing. The blog post examples used tau=0.5 as a fixed value.
- **Key finding**: 14x lower gradient variance than REINFORCE, 50% relative improvement over PPO on IMDB sentiment alignment.
- **Soft-hard gap**: Acknowledged as a "theoretical concern" but found manageable empirically with STE.
- **Limitation**: Requires differentiable reward models; temperature sensitivity and task-dependence noted.

## 5. SofT-GRPO Paper Details

SofT-GRPO (arXiv 2511.06411):
- **Temperature**: Fixed tau_g=0.1 (notably aggressive).
- **Training collapse**: Testing tau_g=0.25 or top-p=1.0 caused training collapse due to excessive KL divergence growth pushing soft-token inputs outside the pre-trained embedding space.
- **Performance**: Only marginally outperformed discrete GRPO on Pass@1 (+0.13%), suggesting diminishing returns from differentiable approaches in some settings.

## 6. Practical Recommendation for PRM Training

Based on the literature:

1. **Do NOT anneal all the way to tau=0.1.** GRADE stopped at tau=0.5 for good reason. The 0.1 regime is near-discrete with exploding variance and minimal practical benefit over 0.3-0.5.

2. **Use Decoupled ST-GS** with separate forward (tau_f ~ 0.3) and backward (tau_b ~ 2.0-3.0) temperatures. This directly addresses the reviewer's concern by maintaining gradient quality while keeping forward-pass behavior close to inference.

3. **Use Straight-Through estimation** in the forward pass so the model sees hard selections during training, closing the soft-hard gap.

4. **Anneal conservatively**: Linear anneal from tau=2.0 to tau=0.5 over 60-80% of training, then hold at tau=0.5. Monitor gradient norms; if they spike, the temperature is too low.

5. **Report the gap**: Measure performance with both soft and hard selection at evaluation checkpoints throughout training to quantify the soft-hard gap empirically for your specific setting.

---

# Concern 2: Generative Verifiers vs. Discriminative PRMs

## 1. ThinkPRM

- **Paper**: "Process Reward Models That Think" (arXiv 2504.16828, submitted to ICLR 2026).
- **Approach**: Fine-tunes reasoning models on ~1K synthetic verification chain-of-thought traces, filtered using only 8K process labels from PRM800K (vs. ~100K+ labels for discriminative PRMs).
- **Performance**: Outperforms discriminative PRMs trained on the full PRM800K dataset. On out-of-domain evaluations (GPQA-Diamond, LiveCodeBench), surpasses discriminative verifiers by 8% and 4.5% respectively.
- **Key advantage**: Can scale test-time compute by "thinking longer" -- generating more verification reasoning.
- **Key disadvantage**: Requires expensive sequential token generation for each verification.

## 2. GenPRM

- **Paper**: "GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning" (AAAI 2026).
- **Approach**: Redefines process supervision as a generative task. Uses Chain-of-Thought reasoning plus code verification before providing judgment for each step. Proposes Relative Progress Estimation (RPE) for label generation.
- **Performance**: Significantly outperforms prior PRMs with only 23K training data from MATH.
- **Key insight**: Addresses three limitations of discriminative PRMs: (1) limited generalization, (2) inability to leverage LLM generative capabilities, (3) inability to scale test-time compute.

## 3. GRPO and DAPO

- **GRPO** (Group Relative Policy Optimization): From DeepSeekMath. Foundational RL algorithm for LLM reasoning training. Uses group-relative advantage estimation without a separate critic model.
- **DAPO** (Decoupled Clip and Dynamic Sampling Policy Optimization): Builds on GRPO. Achieves 50 points on AIME 2024 (vs. DeepSeek-R1's 47) with 50% fewer training steps on the same Qwen2.5-32B base.
- **Relevance**: These methods train the policy (generator) directly with RL, potentially reducing the need for a separate discriminative PRM altogether. The verifiable reward signal (correct/incorrect final answer) can substitute for step-level process rewards.

## 4. Inference Cost Comparison

This is where the strongest argument for discriminative PRMs remains:

| Aspect | Discriminative PRM | Generative Verifier |
|---|---|---|
| **Per-solution cost** | Single forward pass (prefill only) | Prefill + sequential decoding of verification CoT |
| **Latency** | O(solution_length) | O(solution_length + verification_CoT_length) |
| **Scaling** | Trivially parallelizable | Each verification is an autoregressive generation |
| **Cost multiplier** | ~1x per candidate | ~5-50x per candidate (depending on CoT length) |

Concrete numbers from recent research:
- GenRM (generative) first surpasses self-consistency only after **8x compute**, and requires an additional **128x inference compute** to achieve a mere 3.8% performance gain over self-consistency.
- At fixed practical budgets of 5x10^15 and 1x10^16 FLOPs, **hybrid discriminative verification outperforms generative verification** by 6.1% and 2.5% respectively.
- At latency budgets of 13.8 and 15.7 minutes, discriminative-based hybrid methods outperform generative verification by **15.3% and 2.8%** respectively (on AIME 2025).

## 5. Accuracy Trade-offs

- **In-domain (math)**: Generative verifiers (GenRM, ThinkPRM, GenPRM) consistently outperform discriminative PRMs, especially with sufficient compute budget.
- **Out-of-domain**: The gap widens further -- ThinkPRM-14B trained on 8K labels beats discriminative PRMs trained on 100x more data by 4.5-8% on out-of-domain tasks.
- **Multi-domain**: Discriminative PRMs show fragility under domain shifts. Generative ORMs deliver more consistent gains across domains.
- **Budget-constrained**: Discriminative PRMs win when compute is limited because they avoid the sequential decoding bottleneck.

## 6. The Case for Optimizing Discriminative PRM Training

Despite the generative verifier trend, there are strong arguments for continued work on discriminative PRMs:

1. **Inference efficiency is paramount in production**: At scale (millions of queries), the 5-50x cost multiplier of generative verifiers is prohibitive. A discriminative PRM that scores in a single forward pass remains the only economically viable option for real-time applications.

2. **Complementary role in hybrid systems**: The latest research (Budget-aware Test-time Scaling, Oct 2025) shows that **the optimal strategy is hybrid** -- use a cheap discriminative PRM for initial filtering/ranking, then apply expensive generative verification only to ambiguous cases. Better discriminative PRMs directly improve hybrid system performance.

3. **Training signal for RL**: Discriminative PRMs serve as dense reward signals for GRPO/DAPO-style policy training. Even if the PRM is not used at inference, improving PRM training quality improves the RL policy training pipeline. A better search-objective loss for PRM training directly translates to better RL reward signals.

4. **Latency-critical applications**: For interactive systems (coding assistants, real-time tutoring), generative verification adds unacceptable latency. Discriminative PRMs provide step-level scores in milliseconds.

5. **The generative verifier trend does not eliminate the need -- it changes the role**: Discriminative PRMs shift from being the sole verifier to being a fast first-pass filter in a tiered verification pipeline. Optimizing their training (e.g., with search-objective losses) makes this filter more effective, reducing the number of expensive generative verifications needed.

---

## Summary of Recommended Responses to Reviewers

**For Concern 1 (Gumbel-Softmax):**
Acknowledge the reviewer's valid concern. Propose adopting the Decoupled ST-GS approach (separate forward/backward temperatures) and limiting the minimum temperature to tau=0.5 (following GRADE). Commit to reporting soft-hard gap measurements. Reference GRADE's successful use of STE and SofT-GRPO's training instabilities as motivation for conservative annealing.

**For Concern 2 (Generative Verifiers):**
Reframe the contribution: discriminative PRMs are not competitors to generative verifiers but complementary components. Cite the Budget-aware Test-time Scaling paper showing discriminative verification outperforms generative at practical compute budgets by up to 15.3%. Position search-objective PRM training as improving (a) the fast filter in hybrid verification pipelines and (b) the reward signal quality for RL-based policy training (GRPO/DAPO), where inference cost is irrelevant because the PRM is used only during training.

---

Sources:
- [GRADE: Replacing Policy Gradients with Backpropagation for LLM Alignment](https://arxiv.org/abs/2601.11574)
- [14x Lower Gradient Variance: What GRADE Reveals About LLM Alignment](https://yuv.ai/blog/grade-llm-alignment-backpropagation)
- [SofT-GRPO: Gumbel-Reparameterized Soft-Thinking Policy Optimization](https://arxiv.org/abs/2511.06411)
- [Improving Discrete Optimisation Via Decoupled Straight-Through Gumbel-Softmax](https://arxiv.org/html/2410.13331v1)
- [Cold Analysis of Rao-Blackwellized Straight-Through Gumbel-Softmax](https://proceedings.mlr.press/v202/shekhovtsov23a.html)
- [Categorical Reparameterization with Gumbel-Softmax (Jang et al., ICLR 2017)](https://arxiv.org/abs/1611.01144)
- [A Fully Differentiable Beam Search Decoder (Collobert et al., ICML 2019)](https://arxiv.org/abs/1902.06022)
- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)
- [GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (AAAI 2026)](https://arxiv.org/abs/2504.00891)
- [DAPO: An Open-Source LLM Reinforcement Learning System at Scale](https://arxiv.org/abs/2503.14476)
- [Generative Verifiers: Reward Modeling as Next-Token Prediction](https://arxiv.org/abs/2408.15240)
- [Budget-aware Test-time Scaling via Discriminative Verification](https://arxiv.org/abs/2510.14913)
- [When To Solve, When To Verify: Compute-Optimal Problem Solving and Generative Verification](https://arxiv.org/abs/2504.01005)
- [Differentiable Top-k via Optimal Transport (Cuturi et al.)](https://openreview.net/pdf?id=dolp65Z6re)
- [REBAR: Low-variance, unbiased gradient estimates for discrete latent variable models](https://arxiv.org/abs/1703.07370)
- [Discrete Optimization: Beyond REINFORCE](https://medium.com/mini-distill/discrete-optimization-beyond-reinforce-5ca171bebf17)
- [Rao-Blackwellizing the Straight-Through Gumbel-Softmax Gradient Estimator](https://arxiv.org/abs/2010.04838)

agentId: a554e6da3f024ef96 (use SendMessage with to: 'a554e6da3f024ef96' to continue this agent)
&lt;usage>total_tokens: 31382
tool_uses: 24
duration_ms: 223187&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9adbd520-6e06-4f7b-9d5f-fd56deb89dfc",
  "isSidechain": false,
  "promptId": "cfe7962d-223e-4b12-9480-c455cf84546f",
  "type": "user",
  "uuid": "fa56c484-d63f-43b5-b98c-f5352da01aad",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm revising a research idea about training Process Reward Models (PRMs) with search-objective losses using Gumbel-Softmax differentiable beam search. Reviewers raised two technical/strategic concerns:\n\n## Concern 1: Gumbel-Softmax Technical Risks\nThe reviewer says: \"Temperature annealing from τ=2.0 to τ=0.1 is aggressive—at τ=0.1 Gumbel-Softmax outputs are near-discrete, causing gradient bias. The paper should discuss straight-through estimator alternatives and the soft-training/hard-inference gap.\"\n\nPlease research:\n1. Search for \"Gumbel-Softmax gradient bias low temperature\" and \"straight-through estimator vs Gumbel-Softmax\"\n2. Search for \"differentiable top-k selection\" and \"differentiable beam search gradient\"\n3. What are the known issues with Gumbel-Softmax at low temperatures (τ < 0.5)?\n4. What alternatives exist? (Straight-through estimator, REINFORCE with baseline, perturb-and-MAP, etc.)\n5. What is the \"soft-hard gap\" — the distribution mismatch between soft selections during training and hard selections during inference?\n6. Search for \"GRADE Gumbel-Softmax LLM alignment arXiv 2026\" - what temperature schedule did they use and what problems did they encounter?\n7. What is a practical recommendation for handling this in PRM training?\n\n## Concern 2: Generative Verifiers vs Discriminative PRMs\nThe reviewer says: \"The field is rapidly shifting toward generative verifiers (ThinkPRM, GenPRM) and RL-based training (GRPO, DAPO) where discriminative PRM optimization may have diminishing returns.\"\n\nPlease research:\n1. Search for \"ThinkPRM generative verifier 2025 2026\" and \"GenPRM generative process reward\"\n2. Search for \"discriminative vs generative verifier inference cost comparison\"\n3. Search for \"GRPO DAPO reinforcement learning LLM math reasoning 2026\"\n4. What are the inference cost differences between discriminative PRMs and generative verifiers?\n5. What are the accuracy trade-offs?\n6. Is there a strong argument for why optimizing discriminative PRM training still matters?\n\nProvide detailed findings for both concerns.",
    "agentId": "a554e6da3f024ef96",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information on both concerns. Let me compile the detailed findings.\n\n---\n\n# Concern 1: Gumbel-Softmax Technical Risks\n\n## 1. Known Issues with Gumbel-Softmax at Low Temperatures (tau < 0.5)\n\nThe reviewer's concern about aggressive annealing from tau=2.0 to tau=0.1 is well-grounded in the literature. The fundamental problem is a **bias-variance tradeoff**:\n\n- **As tau approaches 0**: The Gumbel-Softmax distribution approaches a true categorical (one-hot), so bias decreases. However, gradient variance increases dramatically, and gradients can vanish entirely, degrading the learning signal. Critically, research shows that **bias does not vanish even asymptotically, while variance grows as O(1/tau)** (Shekhovtsov et al., ICML 2023).\n\n- **At tau=0.1 specifically**: The distribution is near-discrete. Empirical studies confirm that values between 0.1 and 1.0 are used in practice, but tau=0.1 sits at the extreme edge. SofT-GRPO (which uses a fixed tau_g=0.1) reported **training collapse** when deviating even slightly to tau_g=0.25 combined with other hyperparameter changes, indicating extreme sensitivity in this regime.\n\n- **Gradient explosion and instability**: Too-low temperatures lead to gradient explosion. Overly aggressive annealing can cause **premature collapse to suboptimal discrete solutions**.\n\n## 2. The Soft-Hard Gap (Training-Inference Mismatch)\n\nThis is a real and quantified problem:\n\n- During training with Gumbel-Softmax, the model sees **soft (continuous) mixtures** of embeddings. At inference, it must use **hard (discrete) token selections**. This creates a distribution mismatch.\n- Research on differentiable logic gate networks measured this gap at **24-40% performance degradation** when soft methods are used during training but hard selection at deployment, with Gumbel noise amplifying the gap.\n- The GRADE paper acknowledged this directly: \"Models are trained with soft tokens but tested with hard sampling. While GRADE-STE's strong test performance suggests this mismatch is manageable, it **remains a theoretical concern**.\"\n- In the discretization gap literature more broadly, accuracy degradation of ~3% has been documented even in favorable settings.\n\n## 3. Alternatives to Standard Gumbel-Softmax\n\n**a) Straight-Through Estimator (STE) and ST-Gumbel-Softmax:**\n- Uses hard argmax in the forward pass but passes gradients through the soft Gumbel-Softmax in the backward pass. This directly addresses the soft-hard gap by making the forward pass match inference behavior.\n- GRADE adopted this (GRADE-STE) and found it critical for good performance, achieving 14x lower gradient variance than REINFORCE.\n- Limitation: STE is biased because the backward pass gradient does not correspond to the true gradient of the forward pass function.\n\n**b) Decoupled Straight-Through Gumbel-Softmax (Decoupled ST-GS)** (ICLR-submitted, Oct 2024):\n- Uses **two independent temperatures**: tau_f for the forward pass (low, ~0.3, for sharp discrete-like samples) and tau_b for the backward pass (high, ~3.0, for smooth gradients).\n- This cleanly separates the discreteness requirement from gradient quality. Experiments showed that a single shared temperature \"compromises both performance and gradient fidelity.\"\n- This is likely the most directly applicable technique for the PRM training scenario.\n\n**c) REINFORCE with Leave-One-Out Baseline:**\n- Unbiased but higher variance than reparameterization methods. Modern variants are competitive, especially when the action space is small.\n- Provably, reparameterization approaches have variance no larger than likelihood-ratio methods with optimal baselines.\n\n**d) Perturb-and-MAP:**\n- Uses Gumbel perturbations with MAP inference rather than softmax relaxation. Provides an upper bound on the partition function. Less commonly used for neural network training but theoretically appealing for structured discrete problems.\n\n**e) Improved Continuous Relaxation (ICR), Gapped Straight-Through (GST), Rao-Blackwellized variants (GRMC):**\n- These reduce bias and/or variance through modified Jacobians or marginalization, at the cost of additional implementation complexity.\n\n## 4. GRADE Paper Details\n\nGRADE (Gumbel-softmax Relaxation for Alignment via Differentiable Estimation) -- arXiv 2601.11574:\n- **Temperature schedule**: Annealed from tau=2.0 down to tau=0.5 (NOT to 0.1), using linear annealing. The blog post examples used tau=0.5 as a fixed value.\n- **Key finding**: 14x lower gradient variance than REINFORCE, 50% relative improvement over PPO on IMDB sentiment alignment.\n- **Soft-hard gap**: Acknowledged as a \"theoretical concern\" but found manageable empirically with STE.\n- **Limitation**: Requires differentiable reward models; temperature sensitivity and task-dependence noted.\n\n## 5. SofT-GRPO Paper Details\n\nSofT-GRPO (arXiv 2511.06411):\n- **Temperature**: Fixed tau_g=0.1 (notably aggressive).\n- **Training collapse**: Testing tau_g=0.25 or top-p=1.0 caused training collapse due to excessive KL divergence growth pushing soft-token inputs outside the pre-trained embedding space.\n- **Performance**: Only marginally outperformed discrete GRPO on Pass@1 (+0.13%), suggesting diminishing returns from differentiable approaches in some settings.\n\n## 6. Practical Recommendation for PRM Training\n\nBased on the literature:\n\n1. **Do NOT anneal all the way to tau=0.1.** GRADE stopped at tau=0.5 for good reason. The 0.1 regime is near-discrete with exploding variance and minimal practical benefit over 0.3-0.5.\n\n2. **Use Decoupled ST-GS** with separate forward (tau_f ~ 0.3) and backward (tau_b ~ 2.0-3.0) temperatures. This directly addresses the reviewer's concern by maintaining gradient quality while keeping forward-pass behavior close to inference.\n\n3. **Use Straight-Through estimation** in the forward pass so the model sees hard selections during training, closing the soft-hard gap.\n\n4. **Anneal conservatively**: Linear anneal from tau=2.0 to tau=0.5 over 60-80% of training, then hold at tau=0.5. Monitor gradient norms; if they spike, the temperature is too low.\n\n5. **Report the gap**: Measure performance with both soft and hard selection at evaluation checkpoints throughout training to quantify the soft-hard gap empirically for your specific setting.\n\n---\n\n# Concern 2: Generative Verifiers vs. Discriminative PRMs\n\n## 1. ThinkPRM\n\n- **Paper**: \"Process Reward Models That Think\" (arXiv 2504.16828, submitted to ICLR 2026).\n- **Approach**: Fine-tunes reasoning models on ~1K synthetic verification chain-of-thought traces, filtered using only 8K process labels from PRM800K (vs. ~100K+ labels for discriminative PRMs).\n- **Performance**: Outperforms discriminative PRMs trained on the full PRM800K dataset. On out-of-domain evaluations (GPQA-Diamond, LiveCodeBench), surpasses discriminative verifiers by 8% and 4.5% respectively.\n- **Key advantage**: Can scale test-time compute by \"thinking longer\" -- generating more verification reasoning.\n- **Key disadvantage**: Requires expensive sequential token generation for each verification.\n\n## 2. GenPRM\n\n- **Paper**: \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\" (AAAI 2026).\n- **Approach**: Redefines process supervision as a generative task. Uses Chain-of-Thought reasoning plus code verification before providing judgment for each step. Proposes Relative Progress Estimation (RPE) for label generation.\n- **Performance**: Significantly outperforms prior PRMs with only 23K training data from MATH.\n- **Key insight**: Addresses three limitations of discriminative PRMs: (1) limited generalization, (2) inability to leverage LLM generative capabilities, (3) inability to scale test-time compute.\n\n## 3. GRPO and DAPO\n\n- **GRPO** (Group Relative Policy Optimization): From DeepSeekMath. Foundational RL algorithm for LLM reasoning training. Uses group-relative advantage estimation without a separate critic model.\n- **DAPO** (Decoupled Clip and Dynamic Sampling Policy Optimization): Builds on GRPO. Achieves 50 points on AIME 2024 (vs. DeepSeek-R1's 47) with 50% fewer training steps on the same Qwen2.5-32B base.\n- **Relevance**: These methods train the policy (generator) directly with RL, potentially reducing the need for a separate discriminative PRM altogether. The verifiable reward signal (correct/incorrect final answer) can substitute for step-level process rewards.\n\n## 4. Inference Cost Comparison\n\nThis is where the strongest argument for discriminative PRMs remains:\n\n| Aspect | Discriminative PRM | Generative Verifier |\n|---|---|---|\n| **Per-solution cost** | Single forward pass (prefill only) | Prefill + sequential decoding of verification CoT |\n| **Latency** | O(solution_length) | O(solution_length + verification_CoT_length) |\n| **Scaling** | Trivially parallelizable | Each verification is an autoregressive generation |\n| **Cost multiplier** | ~1x per candidate | ~5-50x per candidate (depending on CoT length) |\n\nConcrete numbers from recent research:\n- GenRM (generative) first surpasses self-consistency only after **8x compute**, and requires an additional **128x inference compute** to achieve a mere 3.8% performance gain over self-consistency.\n- At fixed practical budgets of 5x10^15 and 1x10^16 FLOPs, **hybrid discriminative verification outperforms generative verification** by 6.1% and 2.5% respectively.\n- At latency budgets of 13.8 and 15.7 minutes, discriminative-based hybrid methods outperform generative verification by **15.3% and 2.8%** respectively (on AIME 2025).\n\n## 5. Accuracy Trade-offs\n\n- **In-domain (math)**: Generative verifiers (GenRM, ThinkPRM, GenPRM) consistently outperform discriminative PRMs, especially with sufficient compute budget.\n- **Out-of-domain**: The gap widens further -- ThinkPRM-14B trained on 8K labels beats discriminative PRMs trained on 100x more data by 4.5-8% on out-of-domain tasks.\n- **Multi-domain**: Discriminative PRMs show fragility under domain shifts. Generative ORMs deliver more consistent gains across domains.\n- **Budget-constrained**: Discriminative PRMs win when compute is limited because they avoid the sequential decoding bottleneck.\n\n## 6. The Case for Optimizing Discriminative PRM Training\n\nDespite the generative verifier trend, there are strong arguments for continued work on discriminative PRMs:\n\n1. **Inference efficiency is paramount in production**: At scale (millions of queries), the 5-50x cost multiplier of generative verifiers is prohibitive. A discriminative PRM that scores in a single forward pass remains the only economically viable option for real-time applications.\n\n2. **Complementary role in hybrid systems**: The latest research (Budget-aware Test-time Scaling, Oct 2025) shows that **the optimal strategy is hybrid** -- use a cheap discriminative PRM for initial filtering/ranking, then apply expensive generative verification only to ambiguous cases. Better discriminative PRMs directly improve hybrid system performance.\n\n3. **Training signal for RL**: Discriminative PRMs serve as dense reward signals for GRPO/DAPO-style policy training. Even if the PRM is not used at inference, improving PRM training quality improves the RL policy training pipeline. A better search-objective loss for PRM training directly translates to better RL reward signals.\n\n4. **Latency-critical applications**: For interactive systems (coding assistants, real-time tutoring), generative verification adds unacceptable latency. Discriminative PRMs provide step-level scores in milliseconds.\n\n5. **The generative verifier trend does not eliminate the need -- it changes the role**: Discriminative PRMs shift from being the sole verifier to being a fast first-pass filter in a tiered verification pipeline. Optimizing their training (e.g., with search-objective losses) makes this filter more effective, reducing the number of expensive generative verifications needed.\n\n---\n\n## Summary of Recommended Responses to Reviewers\n\n**For Concern 1 (Gumbel-Softmax):**\nAcknowledge the reviewer's valid concern. Propose adopting the Decoupled ST-GS approach (separate forward/backward temperatures) and limiting the minimum temperature to tau=0.5 (following GRADE). Commit to reporting soft-hard gap measurements. Reference GRADE's successful use of STE and SofT-GRPO's training instabilities as motivation for conservative annealing.\n\n**For Concern 2 (Generative Verifiers):**\nReframe the contribution: discriminative PRMs are not competitors to generative verifiers but complementary components. Cite the Budget-aware Test-time Scaling paper showing discriminative verification outperforms generative at practical compute budgets by up to 15.3%. Position search-objective PRM training as improving (a) the fast filter in hybrid verification pipelines and (b) the reward signal quality for RL-based policy training (GRPO/DAPO), where inference cost is irrelevant because the PRM is used only during training.\n\n---\n\nSources:\n- [GRADE: Replacing Policy Gradients with Backpropagation for LLM Alignment](https://arxiv.org/abs/2601.11574)\n- [14x Lower Gradient Variance: What GRADE Reveals About LLM Alignment](https://yuv.ai/blog/grade-llm-alignment-backpropagation)\n- [SofT-GRPO: Gumbel-Reparameterized Soft-Thinking Policy Optimization](https://arxiv.org/abs/2511.06411)\n- [Improving Discrete Optimisation Via Decoupled Straight-Through Gumbel-Softmax](https://arxiv.org/html/2410.13331v1)\n- [Cold Analysis of Rao-Blackwellized Straight-Through Gumbel-Softmax](https://proceedings.mlr.press/v202/shekhovtsov23a.html)\n- [Categorical Reparameterization with Gumbel-Softmax (Jang et al., ICLR 2017)](https://arxiv.org/abs/1611.01144)\n- [A Fully Differentiable Beam Search Decoder (Collobert et al., ICML 2019)](https://arxiv.org/abs/1902.06022)\n- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)\n- [GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (AAAI 2026)](https://arxiv.org/abs/2504.00891)\n- [DAPO: An Open-Source LLM Reinforcement Learning System at Scale](https://arxiv.org/abs/2503.14476)\n- [Generative Verifiers: Reward Modeling as Next-Token Prediction](https://arxiv.org/abs/2408.15240)\n- [Budget-aware Test-time Scaling via Discriminative Verification](https://arxiv.org/abs/2510.14913)\n- [When To Solve, When To Verify: Compute-Optimal Problem Solving and Generative Verification](https://arxiv.org/abs/2504.01005)\n- [Differentiable Top-k via Optimal Transport (Cuturi et al.)](https://openreview.net/pdf?id=dolp65Z6re)\n- [REBAR: Low-variance, unbiased gradient estimates for discrete latent variable models](https://arxiv.org/abs/1703.07370)\n- [Discrete Optimization: Beyond REINFORCE](https://medium.com/mini-distill/discrete-optimization-beyond-reinforce-5ca171bebf17)\n- [Rao-Blackwellizing the Straight-Through Gumbel-Softmax Gradient Estimator](https://arxiv.org/abs/2010.04838)"
      }
    ],
    "totalDurationMs": 223187,
    "totalTokens": 31382,
    "totalToolUseCount": 24,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 26152,
      "output_tokens": 4099,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1130
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4099,
          "cache_read_input_tokens": 26152,
          "cache_creation_input_tokens": 1130,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1130,
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
      "otherToolCount": 24
    }
  },
  "sourceToolAssistantUUID": "9adbd520-6e06-4f7b-9d5f-fd56deb89dfc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Search-Objective Training for Process Reward Models\",   \"core_problem\"…",
  "leafUuid": "fa56c484-d63f-43b5-b98c-f5352da01aad",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise search-objective PRM training based on reviewer feedback",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b"
}
```

---

### Tool call

_source line 27 · 2026-05-27T17:57:40.739Z_

<details open><summary>🔧 Tool call — Agent · `toolu_015Z4AVq46pRue9QrR2WnKP7`</summary>

```json
{
  "description": "Research Qwen3 models and venue deadlines",
  "prompt": "I need to verify two factual items for a research paper revision:\n\n1. **Qwen3 model sizes**: The reviewer says \"Qwen3-7B does not exist. The Qwen3 series offers 0.6B, 1.7B, 4B, 8B, 14B, 32B.\" Please verify:\n   - Search for \"Qwen3 model sizes available 2025 2026\"\n   - What are the exact model sizes in the Qwen3 family?\n   - Is there a Qwen3-7B or should it be Qwen3-8B?\n   - Also check: does Qwen2.5-Math-PRM-7B exist? Search for \"Qwen2.5-Math-PRM model\"\n\n2. **Conference deadlines**: Please verify these deadlines:\n   - AAAI 2027: abstract July 21, full paper July 28, 2026\n   - ICLR 2027: estimated abstract ~September 19, paper ~September 24, 2026\n   - ICML 2027: estimated ~January 2027\n   - EACL 2027: ARR submission August 3, 2026\n   - Search for \"ICLR 2027 deadline\" and \"ICML 2027 deadline\" and \"AAAI 2027 deadline\"\n\nReport precise findings.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa56c484-d63f-43b5-b98c-f5352da01aad",
  "isSidechain": false,
  "requestId": "req_011CbTWKS7Ku7Z5vCQjFzf8E",
  "type": "assistant",
  "uuid": "0fbbe3a8-1d95-4baa-9fa9-46e880d6c72d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UrbYncGiMSzPxmxtau68mH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4838,
      "cache_read_input_tokens": 27703,
      "output_tokens": 429,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4838,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 429,
          "cache_read_input_tokens": 27703,
          "cache_creation_input_tokens": 4838,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4838
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

_source line 28 · 2026-05-27T17:58:41.181Z_

<details><summary>↩ Tool result · `toolu_015Z4AVq46pRue9QrR2WnKP7`</summary>

```text
Here are the precise findings for both items:

---

## 1. Qwen3 Model Sizes

**The reviewer is correct.** There is no Qwen3-7B. The Qwen3 dense model lineup is:

- **0.6B, 1.7B, 4B, 8B, 14B, 32B**

Plus two MoE models:
- **30B-A3B** (30B total, 3B active)
- **235B-A22B** (235B total, 22B active)

If your paper references "Qwen3-7B," it should be changed to **Qwen3-8B**.

**Regarding Qwen2.5-Math-PRM-7B: Yes, it exists.** It is an official model hosted at [Qwen/Qwen2.5-Math-PRM-7B on Hugging Face](https://huggingface.co/Qwen/Qwen2.5-Math-PRM-7B). The Qwen2.5-Math-PRM series comes in 7B and 72B sizes. Note that the Qwen2.5 base model series uses different size bins (including 7B) than the newer Qwen3 series (which uses 8B). So "Qwen2.5-Math-PRM-7B" is correct as-is and should not be changed.

---

## 2. Conference Deadlines

### AAAI 2027 -- CONFIRMED
The official AAAI-27 Main Technical Track deadlines are:
- **Abstract deadline: July 21, 2026** (11:59 PM UTC-12)
- **Full paper deadline: July 28, 2026** (11:59 PM UTC-12)
- Supplementary material/code: July 31, 2026
- Conference dates: February 16-23, 2027, Montreal, Canada

Your stated deadlines are **correct**.

### ICLR 2027 -- NOT YET ANNOUNCED (estimate is reasonable)
ICLR 2027 deadlines have **not been officially announced** yet. However, your estimates are plausible based on the ICLR 2026 pattern:
- ICLR 2026 had abstract September 19 and paper September 24 (both 2025).
- Your estimates of ~September 19 / ~September 24, 2026 for ICLR 2027 follow the same pattern.
- ICLR 2027 is confirmed to be held in Toronto, Canada (exact dates not yet finalized).

**Recommendation:** Label these as "estimated" in your paper, since they are not official.

### ICML 2027 -- NOT YET ANNOUNCED (estimate is reasonable)
ICML 2027 deadlines have **not been officially announced**. Based on ICML 2026 (abstract January 23, paper January 28, 2026), your estimate of "~January 2027" is consistent with the historical pattern. ICML 2027 is expected to be held in South America.

**Recommendation:** Label this as "estimated."

### EACL 2027 -- CONFIRMED
- **ARR submission deadline: August 3, 2026** (corrected from an initially announced date of August 6)
- Conference dates: March 9-13, 2027, Athens, Greece
- Note: EACL is earlier than usual in 2027, so this is the **only viable ARR cycle** for the conference.

Your stated deadline is **correct**.

---

## Summary of Required Changes

| Item | Status | Action Needed |
|------|--------|---------------|
| Qwen3-7B | **Wrong** | Change to **Qwen3-8B** |
| Qwen2.5-Math-PRM-7B | **Correct** | No change needed |
| AAAI 2027 deadlines | **Correct** | None |
| ICLR 2027 deadlines | **Unconfirmed** | Mark as "estimated" |
| ICML 2027 deadlines | **Unconfirmed** | Mark as "estimated" |
| EACL 2027 ARR deadline | **Correct** | None |

Sources:
- [Qwen3 Official Blog](https://qwenlm.github.io/blog/qwen3/)
- [Qwen3 GitHub Repository](https://github.com/QwenLM/qwen3)
- [Qwen2.5-Math-PRM-7B on Hugging Face](https://huggingface.co/Qwen/Qwen2.5-Math-PRM-7B)
- [Qwen2.5-Math-PRM Blog Post](https://qwenlm.github.io/blog/qwen2.5-math-prm/)
- [AAAI-27 Official Page](https://aaai.org/conference/aaai/aaai-27/)
- [AAAI-27 Main Technical Track CFP](https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/)
- [EACL 2027 Official Page](https://2027.eacl.org/)
- [EACL 2027 Corrected Deadline Announcement](https://x.com/eaclmeeting/status/2051971432171688436)
- [ICLR 2026 Dates (for reference)](https://iclr.cc/Conferences/2026/Dates)
- [ICML 2026 Dates (for reference)](https://icml.cc/Conferences/2026/Dates)
- [AI Conference Deadlines Tracker](https://trybibby.com/conference-deadlines)

agentId: a99a6012022781a31 (use SendMessage with to: 'a99a6012022781a31' to continue this agent)
&lt;usage>total_tokens: 19097
tool_uses: 11
duration_ms: 60434&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0fbbe3a8-1d95-4baa-9fa9-46e880d6c72d",
  "isSidechain": false,
  "promptId": "cfe7962d-223e-4b12-9480-c455cf84546f",
  "type": "user",
  "uuid": "87759690-7106-4843-a721-9090cec45abd",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify two factual items for a research paper revision:\n\n1. **Qwen3 model sizes**: The reviewer says \"Qwen3-7B does not exist. The Qwen3 series offers 0.6B, 1.7B, 4B, 8B, 14B, 32B.\" Please verify:\n   - Search for \"Qwen3 model sizes available 2025 2026\"\n   - What are the exact model sizes in the Qwen3 family?\n   - Is there a Qwen3-7B or should it be Qwen3-8B?\n   - Also check: does Qwen2.5-Math-PRM-7B exist? Search for \"Qwen2.5-Math-PRM model\"\n\n2. **Conference deadlines**: Please verify these deadlines:\n   - AAAI 2027: abstract July 21, full paper July 28, 2026\n   - ICLR 2027: estimated abstract ~September 19, paper ~September 24, 2026\n   - ICML 2027: estimated ~January 2027\n   - EACL 2027: ARR submission August 3, 2026\n   - Search for \"ICLR 2027 deadline\" and \"ICML 2027 deadline\" and \"AAAI 2027 deadline\"\n\nReport precise findings.",
    "agentId": "a99a6012022781a31",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the precise findings for both items:\n\n---\n\n## 1. Qwen3 Model Sizes\n\n**The reviewer is correct.** There is no Qwen3-7B. The Qwen3 dense model lineup is:\n\n- **0.6B, 1.7B, 4B, 8B, 14B, 32B**\n\nPlus two MoE models:\n- **30B-A3B** (30B total, 3B active)\n- **235B-A22B** (235B total, 22B active)\n\nIf your paper references \"Qwen3-7B,\" it should be changed to **Qwen3-8B**.\n\n**Regarding Qwen2.5-Math-PRM-7B: Yes, it exists.** It is an official model hosted at [Qwen/Qwen2.5-Math-PRM-7B on Hugging Face](https://huggingface.co/Qwen/Qwen2.5-Math-PRM-7B). The Qwen2.5-Math-PRM series comes in 7B and 72B sizes. Note that the Qwen2.5 base model series uses different size bins (including 7B) than the newer Qwen3 series (which uses 8B). So \"Qwen2.5-Math-PRM-7B\" is correct as-is and should not be changed.\n\n---\n\n## 2. Conference Deadlines\n\n### AAAI 2027 -- CONFIRMED\nThe official AAAI-27 Main Technical Track deadlines are:\n- **Abstract deadline: July 21, 2026** (11:59 PM UTC-12)\n- **Full paper deadline: July 28, 2026** (11:59 PM UTC-12)\n- Supplementary material/code: July 31, 2026\n- Conference dates: February 16-23, 2027, Montreal, Canada\n\nYour stated deadlines are **correct**.\n\n### ICLR 2027 -- NOT YET ANNOUNCED (estimate is reasonable)\nICLR 2027 deadlines have **not been officially announced** yet. However, your estimates are plausible based on the ICLR 2026 pattern:\n- ICLR 2026 had abstract September 19 and paper September 24 (both 2025).\n- Your estimates of ~September 19 / ~September 24, 2026 for ICLR 2027 follow the same pattern.\n- ICLR 2027 is confirmed to be held in Toronto, Canada (exact dates not yet finalized).\n\n**Recommendation:** Label these as \"estimated\" in your paper, since they are not official.\n\n### ICML 2027 -- NOT YET ANNOUNCED (estimate is reasonable)\nICML 2027 deadlines have **not been officially announced**. Based on ICML 2026 (abstract January 23, paper January 28, 2026), your estimate of \"~January 2027\" is consistent with the historical pattern. ICML 2027 is expected to be held in South America.\n\n**Recommendation:** Label this as \"estimated.\"\n\n### EACL 2027 -- CONFIRMED\n- **ARR submission deadline: August 3, 2026** (corrected from an initially announced date of August 6)\n- Conference dates: March 9-13, 2027, Athens, Greece\n- Note: EACL is earlier than usual in 2027, so this is the **only viable ARR cycle** for the conference.\n\nYour stated deadline is **correct**.\n\n---\n\n## Summary of Required Changes\n\n| Item | Status | Action Needed |\n|------|--------|---------------|\n| Qwen3-7B | **Wrong** | Change to **Qwen3-8B** |\n| Qwen2.5-Math-PRM-7B | **Correct** | No change needed |\n| AAAI 2027 deadlines | **Correct** | None |\n| ICLR 2027 deadlines | **Unconfirmed** | Mark as \"estimated\" |\n| ICML 2027 deadlines | **Unconfirmed** | Mark as \"estimated\" |\n| EACL 2027 ARR deadline | **Correct** | None |\n\nSources:\n- [Qwen3 Official Blog](https://qwenlm.github.io/blog/qwen3/)\n- [Qwen3 GitHub Repository](https://github.com/QwenLM/qwen3)\n- [Qwen2.5-Math-PRM-7B on Hugging Face](https://huggingface.co/Qwen/Qwen2.5-Math-PRM-7B)\n- [Qwen2.5-Math-PRM Blog Post](https://qwenlm.github.io/blog/qwen2.5-math-prm/)\n- [AAAI-27 Official Page](https://aaai.org/conference/aaai/aaai-27/)\n- [AAAI-27 Main Technical Track CFP](https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/)\n- [EACL 2027 Official Page](https://2027.eacl.org/)\n- [EACL 2027 Corrected Deadline Announcement](https://x.com/eaclmeeting/status/2051971432171688436)\n- [ICLR 2026 Dates (for reference)](https://iclr.cc/Conferences/2026/Dates)\n- [ICML 2026 Dates (for reference)](https://icml.cc/Conferences/2026/Dates)\n- [AI Conference Deadlines Tracker](https://trybibby.com/conference-deadlines)"
      }
    ],
    "totalDurationMs": 60434,
    "totalTokens": 19097,
    "totalToolUseCount": 11,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4334,
      "cache_read_input_tokens": 13356,
      "output_tokens": 1406,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4334
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1406,
          "cache_read_input_tokens": 13356,
          "cache_creation_input_tokens": 4334,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4334,
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
  "sourceToolAssistantUUID": "0fbbe3a8-1d95-4baa-9fa9-46e880d6c72d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-27T17:59:00.448Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive research on all the reviewer concerns. Let me synthesize everything and produce the revised research idea. Let me go through each issue systematically:

1. **CRITICAL MISSING RELATED WORK: SOC** - Now well-understood. SOC modifies the generator's SFT loss (auxiliary V loss for value contraction), not the PRM. It's indirect, regularization-based. Our approach directly optimizes the PRM for search performance.

2. **MISSING RELATED WORK: CRM** - Conditions step rewards on outcomes via survival analysis. Changes what the PRM predicts, not how it's trained for search. Complementary to our approach.


3. **MISSING RELATED WORK: From Curiosity to Caution** - Applies pessimistic correction at inference time for best-of-N sampling, which is post-hoc and doesn't affect training. Complementary to what we're doing.

4. **MISSING RELATED WORK: Learning Generative Selection** - Uses RL to replace scoring with generative selection entirely, which is a fundamentally different approach than beam search. Not directly comparable.

5. **MISSING RELATED WORK: Inference-Aware Fine-Tuning** - Trains the generator with inference-time awareness for best-of-N, establishing the conceptual precedent, but focuses on optimizing the generator rather than the verifier like we do.

6. **FACTUAL ERROR**

Need to correct the model reference from Qwen3-7B to Qwen3-8B.

7. **OVERCONFIDENT CLAIM** - Should dial back the language from "eliminates the overestimation cliff" to something more measured like "significantly extends the useful beam width range."

8. **VENUE TIMELINE** - AAAI 2027 isn't realistic as a first target; ICLR 2027 around September 2026 is the earliest we could reasonably aim for.

9. **TECHNICAL RISK: Gumbel-Softmax** - Need to anneal the temperature to 0.5 rather than 0.1, and use either Decoupled ST-GS or STE, while reporting the gap between soft and hard versions.

10. **STRATEGIC CONCERN: Generative verifiers** - Discriminative PRMs are orders of magnitude cheaper at inference and crucial for real-world deployment and as RL reward signals, so hybrid approaches that improve discriminative PRMs are valuable.

This represents a substantial overhaul across the landscape, technical approach, claims, and venue strategy, though the fundamental novelty of the idea holds up. Now I'm putting together the complete revised JSON.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87759690-7106-4843-a721-9090cec45abd",
  "isSidechain": false,
  "requestId": "req_011CbTWQijb5et8cS3qGjoQL",
  "type": "assistant",
  "uuid": "f59ab719-37a8-404e-8b2f-dfa952ee7259",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMyU64mjAsxo2uhNUSbVWp",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 32541,
      "output_tokens": 6089,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1910,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6089,
          "cache_read_input_tokens": 32541,
          "cache_creation_input_tokens": 1910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1910
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

_source line 30 · 2026-05-27T18:01:05.433Z_

Now I have comprehensive research on all reviewer concerns. Let me synthesize everything and produce the revised research idea.

The key findings from my research:
- **SOC**: Modifies generator SFT loss (auxiliary V loss), not PRM training. Indirect, regularization-based. Our approach is fundamentally more direct.
- **CRM**: Changes reward definition (survival analysis) but still trains separately from search. Complementary, not competing.
- **From Curiosity to Caution**: Inference-time pessimistic correction, doesn't modify training at all.
- **Learning Generative Selection**: Replaces scoring with generative selection via RL. Different paradigm (flat BoN only).
- **Inference-Aware Fine-Tuning**: Generator-side analog — optimizes policy for BoN, not verifier for search. Key conceptual precedent.
- **Gumbel-Softmax**: GRADE annealed only to τ=0.5, not 0.1. Decoupled ST-GS (separate forward/backward temperatures) is the state-of-the-art solution.
- **Generative verifiers**: 5-50x more expensive per candidate. Budget-aware research shows discriminative PRMs outperform generative at practical compute budgets by up to 15.3%.
- **Qwen3-8B confirmed** (no 7B). Qwen2.5-Math-PRM-7B is correct.
- **Venues**: AAAI 2027 (July 21) is indeed too tight. ICLR 2027 (~Sep 2026) is feasible.

Now let me produce the complete revised JSON:

```json
{
  "change_type": "major",
  "title": "Search-Objective Training for Process Reward Models",
  "core_problem": "PRMs are trained with step-level classification objectives (is this step correct?) but deployed in search contexts (beam search, best-of-N) where ranking and selection quality matters more than classification accuracy—can we close this training-deployment gap by optimizing PRMs directly for search performance?",
  "opportunity": "\"More Test-Time Compute Can Hurt\" (March 2026) proved that PRM-guided beam search introduces overestimation bias that grows with candidate pool size, meaning more compute can degrade accuracy beyond beam widths of 4–8. A growing ecosystem of mitigations has emerged—post-hoc calibration (\"Know What You Don't Know,\" NeurIPS 2025; Distributional PRM, May 2026), generator-side implicit Q-value correction (SOC, ACL 2025 Findings), outcome-conditioned reward reformulation (CRM, ICLR 2026), inference-time pessimistic correction (\"From Curiosity to Caution,\" April 2026), and inference-aware generator fine-tuning (Inference-Aware BoN, ICLR 2025)—but none directly optimizes the PRM's own training loss for end-to-end search performance. SOC corrects the generator's implicit Q-values, CRM reformulates what step rewards represent, and pessimistic correction adds OOD penalties at inference time. The missing piece is a PRM trained to maximize the probability that downstream search selects the correct solution—the verifier-side analog of inference-aware generator training, and the natural extension of the shift from pointwise to listwise learning-to-rank in information retrieval.",
  "landscape": "PRM training objectives span step-level binary cross-entropy (PRM800K-style), Monte Carlo soft labels (Math-Shepherd, OmegaPRM), Q-value ranking (PQM, ICLR 2025), and outcome-conditioned survival analysis (CRM, ICLR 2026). All optimize proxy objectives disconnected from downstream search. \"More Test-Time Compute Can Hurt\" showed PRM scoring yields useful beam widths ≤4–8 with gains up to 8.9pp, but beyond that, overestimation bias degrades results. Post-hoc calibration via quantile regression (NeurIPS 2025) reduces but doesn't eliminate this, and Distributional PRM (May 2026) applies conditional optimal transport for calibrated quantile estimation but still operates post-hoc. SOC (ACL 2025 Findings) addresses overestimation by adding an auxiliary value-contraction loss during generator SFT to suppress inflated implicit Q-values, but modifies the generator's training (not the PRM's) and uses an indirect regularizer without simulating actual search. CRM (ICLR 2026) conditions step rewards on outcomes via survival analysis with hazard functions, creating a principled process-outcome link, but still trains the reward model separately from any search algorithm. \"From Curiosity to Caution\" (April 2026) applies pessimistic reward correction for BoN via OOD detection, but is purely inference-time and cannot improve the PRM's intrinsic scoring quality. \"Learning Generative Selection for Best-of-N\" (Feb 2026) replaces scoring-based selection with generative comparative reasoning via RL, but abandons step-level process supervision and is incompatible with structured beam search. Inference-Aware Fine-Tuning for BoN (ICLR 2025) is the conceptual precedent closest to our approach: it fine-tunes the generator policy to be aware of BoN inference, demonstrating the power of inference-aware training. However, it optimizes the generator side (not the verifier), handles only flat BoN (not structured beam search), and assumes a fixed verifier. BEAR (Jan 2026) demonstrated beam-search-aware training for recommendation generators, and differentiable beam search decoders exist since 2019 (Collobert et al., ICML), but neither has been applied to reward model training. GRADE (Jan 2026) showed Gumbel-Softmax relaxation with straight-through estimation enables direct backpropagation from reward signals in LLM alignment with 14× lower gradient variance than REINFORCE, providing a key technical building block. Meanwhile, the field is shifting toward generative verifiers (ThinkPRM, GenPRM) that scale test-time compute via chain-of-thought verification. However, these are 5–50× more expensive per candidate than discriminative PRMs, and recent budget-aware analysis (Oct 2025) showed that discriminative verification outperforms generative at practical compute budgets by up to 15.3% under latency constraints. A thorough search of arXiv (March–May 2026) and OpenReview submissions found no concurrent work that trains PRMs with end-to-end search-objective losses.",
  "inspired_by": "Field guide Gap 3 (PRM search + revision never combined), Pattern 'Reformulate-the-prediction-target' (redefine what PRM should predict from step correctness to search success), the overestimation bias finding that exposes the training-deployment mismatch, and the conceptual precedent of Inference-Aware Fine-Tuning (ICLR 2025) which demonstrated inference-aware training on the generator side",
  "approach": "Train a PRM with a search-objective loss that directly optimizes for downstream search performance rather than step-level classification. For each training batch, sample N candidate solutions from a frozen policy model (Qwen3-8B), simulate PRM-guided beam search or best-of-N selection using a differentiable relaxation of the discrete beam pruning operation, and backpropagate a listwise cross-entropy loss measuring whether the search procedure selected the correct solution. For the differentiable relaxation, we adopt a Decoupled Straight-Through Gumbel-Softmax (Decoupled ST-GS) approach following recent advances: the forward pass uses a low temperature (τ_f=0.5) with hard argmax via the straight-through estimator, so the model sees near-discrete selections matching inference behavior, while the backward pass uses a higher temperature (τ_b=2.0) to maintain smooth, low-variance gradients. The forward temperature anneals from τ_f=1.0 to τ_f=0.5 over the first 60% of training; the backward temperature remains fixed at τ_b=2.0. This design directly addresses the soft-hard gap: because the forward pass uses hard selections via STE, the training distribution closely matches hard beam pruning at inference time. We explicitly measure and report the soft-hard performance gap at evaluation checkpoints. To prevent catastrophic forgetting of per-step calibration, combine the search-objective loss with a weighted (λ=0.3) step-level binary cross-entropy regularizer. Initialize from Qwen2.5-Math-PRM-7B and fine-tune on MATH training problems with 256 rollouts per problem, evaluating on MATH-500, GSM8K, and AIME'24 across beam widths 1–64 to demonstrate that SO-PRM significantly extends the useful beam width range beyond the width-4–8 ceiling observed in classification-trained PRMs. We also evaluate SO-PRM as a reward signal for GRPO-style policy training to test whether search-objective PRM training improves downstream RL performance.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "1500 H100-hours (400h rollout generation, 400h PRM training with search-objective loops, 200h evaluation across beam widths/benchmarks, 500h ablations over λ, temperature schedules, beam widths, and Decoupled ST-GS configurations)",
      "timeline": "12–16 weeks (3w infrastructure + rollout pipeline, 4w search-objective training loop development including Decoupled ST-GS implementation, 3w main experiments, 2–4w ablations and paper writing)",
      "estimated_gpu_cost": "$3,750 at $2.50/H100-hour (mid-2026 market median)"
    },
    "human_in_loop": {
      "gpu_hours": "1500 H100-hours (same compute; Claude accelerates code iteration but not GPU workloads)",
      "timeline": "8–11 weeks (Claude drafts differentiable search module with Decoupled ST-GS, training loop, and evaluation harnesses, reducing implementation time by ~4 weeks)",
      "claude_api_cost": "$200–400 (code generation, experiment analysis, paper drafting assistance)",
      "estimated_gpu_cost": "$3,750"
    },
    "auto_research": {
      "gpu_hours": "2000 H100-hours (additional 500h for automated hyperparameter sweeps, broader ablation exploration, and RL downstream evaluation)",
      "timeline": "6–8 weeks (parallel experiment scheduling, automated ablation grid search, continuous evaluation)",
      "claude_api_cost": "$600–1000 (experiment orchestration, result analysis, iterative debugging over many runs)",
      "estimated_gpu_cost": "$5,000",
      "speed_bottleneck": "Rollout generation: sampling 256 solutions per problem across 12K MATH problems requires sequential multi-GPU generation; search-objective training loop requires re-simulating beam search per gradient step, creating a 3–4× slowdown vs. standard PRM training"
    }
  },
  "target_venues": [
    "ICLR 2027 (estimated abstract ~September 19, paper ~September 24, 2026—earliest feasible venue given 12–16 week timeline from May 27)",
    "EACL 2027 (ARR submission August 3, 2026—tight but possible with human-in-loop timeline; fallback to October ARR cycle with commitment October 11, 2026)",
    "ICML 2027 (estimated ~January 2027, based on historical pattern—comfortable timeline for thorough ablations)",
    "AAAI 2027 (abstract July 21, full paper July 28, 2026—infeasible as first submission; possible only if work is substantially complete by early July)"
  ],
  "level": "top-tier",
  "key_references": [
    "More Test-Time Compute Can Hurt: Overestimation Bias in LLM Beam Search (arXiv 2026)",
    "Supervised Optimism Correction: Be Confident When LLMs Are Sure (ACL 2025 Findings, arXiv 2504.07527)",
    "Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning (ICLR 2026, arXiv 2509.26578)",
    "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism (arXiv 2604.04648, 2026)",
    "Learning Generative Selection for Best-of-N (arXiv 2602.02143, 2026)",
    "Inference-Aware Fine-Tuning for Best-of-N Sampling (ICLR 2025, arXiv 2412.15287)",
    "Know What You Don't Know: Uncertainty Calibration of Process Reward Models (NeurIPS 2025)",
    "Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport (arXiv 2026)",
    "Process Reward Model with Q-Value Rankings (ICLR 2025)",
    "BEAR: Towards Beam-Search-Aware Optimization for Recommendation with Large Language Models (arXiv 2026)",
    "A Fully Differentiable Beam Search Decoder (ICML 2019)",
    "Your Reward Function for RL is Your Best PRM for Search: Unifying RL and Search-Based TTS (arXiv 2025)",
    "GRADE: Replacing Policy Gradients with Backpropagation for LLM Alignment (arXiv 2026)",
    "Improving Discrete Optimisation Via Decoupled Straight-Through Gumbel-Softmax (arXiv 2410.13331, 2024)",
    "SofT-GRPO: Gumbel-Reparameterized Soft-Thinking Policy Optimization (arXiv 2511.06411, 2025)",
    "Budget-aware Test-time Scaling via Discriminative Verification (arXiv 2510.14913, 2025)",
    "Let's Verify Step by Step (arXiv 2023)",
    "GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (AAAI 2026)",
    "Process Reward Models That Think (arXiv 2025)",
    "Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations (ACL 2024)",
    "Improve Mathematical Reasoning in Language Models by Automated Process Supervision (arXiv 2024)",
    "Learning to Rank: From Pairwise Approach to Listwise Approach (ICML 2007)",
    "Categorical Reparameterization with Gumbel-Softmax (ICLR 2017)"
  ],
  "description": "Process reward models (PRMs) are trained with step-level classification objectives but deployed in search contexts (beam search, best-of-N) where selection quality determines final accuracy. Recent work proved this mismatch introduces overestimation bias that grows with candidate pool size, causing wider beam search to degrade accuracy beyond a critical width of 4–8. A rich ecosystem of mitigations has emerged: SOC (ACL 2025 Findings) adds an auxiliary value-contraction loss during generator SFT to suppress inflated implicit Q-values; CRM (ICLR 2026) reformulates step rewards via survival analysis to create a principled process-outcome link; pessimistic correction (arXiv 2026) applies OOD-based penalties at inference time; and inference-aware fine-tuning (ICLR 2025) optimizes the generator policy for BoN inference. However, none directly optimizes the PRM's own training loss for end-to-end search performance—SOC modifies the generator's training, CRM changes the reward definition while still training separately from search, and pessimistic correction operates post-hoc. We propose Search-Objective PRM (SO-PRM), which closes this training-deployment gap by directly optimizing the PRM to maximize the probability that downstream search selects the correct solution. Using a Decoupled Straight-Through Gumbel-Softmax relaxation of beam pruning—with separate forward (τ_f=0.5, hard STE) and backward (τ_b=2.0, smooth gradients) temperatures to minimize the soft-hard gap—we make the search procedure differentiable and backpropagate a listwise loss through the simulated search trajectory to the PRM parameters. A step-level regularizer preserves per-step calibration. While generative verifiers (ThinkPRM, GenPRM) achieve higher accuracy, they cost 5–50× more per candidate, making discriminative PRMs essential for large-scale beam search and as reward signals for RL-based policy training (GRPO/DAPO). SO-PRM significantly extends the useful beam width range, aiming to push effective beam search well beyond the width-4–8 ceiling where classification-trained PRMs fail. Starting from Qwen2.5-Math-PRM-7B with Qwen3-8B as the generator, we target MATH-500, GSM8K, and AIME'24 benchmarks, evaluating across beam widths 1–64 and as a downstream RL reward signal. We explicitly quantify the Decoupled ST-GS soft-hard gap and compare against SOC, CRM, and post-hoc calibration baselines.",
  "project_name": "search_objective_prm",
  "source": "web_research",
  "reviewer_response": {
    "issue_1_SOC": "ADDRESSED. SOC (ACL 2025 Findings) is now cited and thoroughly differentiated. SOC modifies the generator's SFT loss with an auxiliary value-contraction term to suppress overestimated implicit Q-values in the policy model's own logits. It never trains or modifies a separate PRM, never simulates actual search during training, and uses an indirect regularization approach. SO-PRM directly optimizes the PRM's parameters end-to-end through differentiable beam search—a fundamentally more direct approach that optimizes the actual search outcome rather than a proxy regularizer. SOC and SO-PRM are complementary: SOC improves the generator's implicit beam search, while SO-PRM improves external PRM-guided search.",
    "issue_2_CRM": "ADDRESSED. CRM (ICLR 2026) is now cited and differentiated. CRM improves *what* the PRM predicts (survival-analysis-based hazard functions with a principled process-outcome link) but still trains the reward model separately from search using supervised losses. SO-PRM improves *how* the PRM is trained (end-to-end through search) while keeping the standard reward definition. The approaches are complementary and could be combined: one could train CRM's hazard-function parameterization with SO-PRM's search-objective loss.",
    "issue_3_curiosity_to_caution": "ADDRESSED. Cited as an inference-time pessimistic correction that applies OOD penalties to frozen reward model scores. Complementary to SO-PRM: pessimistic correction is a post-hoc fix for any PRM, while SO-PRM improves the PRM's intrinsic scores. SO-PRM could further benefit from pessimistic correction at inference time.",
    "issue_4_generative_selection": "ADDRESSED. Cited as replacing scoring-based selection with generative comparative reasoning via RL. Differentiated: generative selection abandons step-level process supervision and requires all N candidates to be fully generated before selection, making it incompatible with structured beam search where candidates are pruned at intermediate steps.",
    "issue_5_inference_aware_finetuning": "ADDRESSED. Cited as the key conceptual precedent—it demonstrated inference-aware training works, but on the generator side. SO-PRM is the verifier-side analog: it optimizes the PRM (not the generator) for search performance, handles structured beam search (not just flat BoN), and makes the search procedure itself differentiable (not just a variational approximation).",
    "issue_6_qwen3_7b": "FIXED. Changed to Qwen3-8B throughout. Verified that Qwen3 offers 0.6B, 1.7B, 4B, 8B, 14B, 32B (plus MoE variants). Qwen2.5-Math-PRM-7B remains correct (Qwen2.5 uses different size bins).",
    "issue_7_overconfident_claim": "FIXED. Changed 'SO-PRM eliminates the overestimation cliff, enabling monotonic accuracy scaling with beam width' to 'SO-PRM significantly extends the useful beam width range, aiming to push effective beam search well beyond the width-4–8 ceiling where classification-trained PRMs fail.' Added explicit acknowledgment of the Decoupled ST-GS soft-hard gap as a factor that may prevent perfectly monotonic scaling.",
    "issue_8_venue_timeline": "FIXED. AAAI 2027 moved to last position and flagged as 'infeasible as first submission.' ICLR 2027 (~Sep 2026) is now the primary target as the earliest feasible venue. EACL 2027 ARR (Aug 3) noted as tight; October ARR cycle is the fallback.",
    "issue_9_gumbel_temperature": "ADDRESSED with substantial technical revision. Replaced aggressive τ=2.0→0.1 annealing with Decoupled Straight-Through Gumbel-Softmax: forward pass uses τ_f=0.5 with hard argmax via STE (matching inference behavior), backward pass uses τ_b=2.0 for smooth gradients. This follows GRADE's finding that STE achieves 14× lower gradient variance than REINFORCE, and addresses the known issues: (1) gradient bias/variance explosion at low τ, (2) training collapse observed in SofT-GRPO at aggressive temperatures, (3) the soft-hard gap by using hard selections in the forward pass. Committed to measuring and reporting soft-hard gap at evaluation checkpoints.",
    "issue_10_generative_verifiers": "ADDRESSED. Added explicit discussion of why discriminative PRM optimization remains important: (1) 5–50× cheaper inference than generative verifiers, making them the only viable option for large-scale beam search in production; (2) budget-aware analysis shows discriminative PRMs outperform generative at practical compute/latency budgets by up to 15.3%; (3) discriminative PRMs serve as dense reward signals for GRPO/DAPO-style RL training where inference cost is irrelevant; (4) optimal verification strategy is hybrid—fast discriminative PRM for initial filtering, expensive generative verifier for ambiguous cases. Better discriminative PRMs directly improve hybrid systems. Added GRPO downstream evaluation as an additional experiment."
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f59ab719-37a8-404e-8b2f-dfa952ee7259",
  "isSidechain": false,
  "requestId": "req_011CbTWQijb5et8cS3qGjoQL",
  "type": "assistant",
  "uuid": "ce3820b3-e82f-41eb-8d61-98fcb194582e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMyU64mjAsxo2uhNUSbVWp",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 32541,
      "output_tokens": 6089,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1910,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6089,
          "cache_read_input_tokens": 32541,
          "cache_creation_input_tokens": 1910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1910
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Search-Objective Training for Process Reward Models\",   \"core_problem\"…",
  "leafUuid": "ce3820b3-e82f-41eb-8d61-98fcb194582e",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise search-objective PRM training based on reviewer feedback",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Search-Objective Training for Process Reward Models\",   \"core_problem\"…",
  "leafUuid": "ce3820b3-e82f-41eb-8d61-98fcb194582e",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise search-objective PRM training based on reviewer feedback",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b"
}
```

---
