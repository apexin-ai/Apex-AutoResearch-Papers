# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-14 (UTC).** ## Original idea { "tit

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 100
- **Recorded user turns:** 1
- **Tool calls:** 31
- **Original source:** `logs/chats/exported-trajectories/account-2/59eecaa6-9288-4835-b915-a151c5a80b80.jsonl`
- **Structured JSON:** [`336eae66880d1466b4fb.json`](../../sessions/33/336eae66880d1466b4fb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T05:56:58.307Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T05:56:58.307Z",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-14 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Offline Advantage Conditioning for VLA Noise Decomposition\",\n  \"core_problem\": \"RECAP/π*0.6 demonstrated that advantage-conditioned VLA training dramatically improves policy quality by learning from both good and bad actions, but requires costly online robot interaction (rollouts and expert corrections). Can advantage conditioning work in a purely offline setting — learning the value function on existing demonstrations alone via hindsight reward — to decompose noise from signal without any environment access?\",\n  \"opportunity\": \"RECAP (Physical Intelligence, Nov 2025) proved advantage conditioning is remarkably effective for VLA training: the model learns to map (state, high-advantage) → expert action and (state, low-advantage) → suboptimal action, using ALL data including noisy examples as informative negative signal. V-GPS (CoRL 2024) proved value functions can be trained offline on demos alone. Combining these enables offline advantage-conditioned VLA fine-tuning: unlike filtering approaches (which discard noisy timesteps), the VLA explicitly learns what noise looks like and what to avoid. At test time, conditioning on high advantage extracts the clean policy. This is more sample-efficient than filtering and avoids the binary keep/discard threshold problem.\",\n  \"landscape\": \"RECAP/π*0.6 (Physical Intelligence, Nov 2025) uses advantage conditioning for VLA training, roughly halving failure rates on hard real-world tasks, but requires online rollouts and expert correction data — inaccessible for most labs. SimpleVLA-RL (ICLR 2026) achieves 430% improvement via online GRPO but needs parallel simulation environments. VLA-RFT (Oct 2025) uses world-model rollouts for RL fine-tuning. ARFM (AAAI 2026) performs offline RL post-training for VLA flow models via advantage weighting with Leave-One-Out estimation, but requires hand-designed 13-component dense reward functions and uses reweighting rather than conditioning. GVL (ICLR 2025 Spotlight) demonstrates VLM-based zero-shot value estimation with advantage-weighted regression on demonstrations, but targets diffusion policies rather than VLAs and uses weighting rather than conditioning. CO-RFT (arXiv 2025) does offline Q-learning for VLAs from 30-60 demos but without advantage conditioning. In the purely offline regime, AFBC (2021) showed advantage-filtered BC can learn from 65:1 noise ratios but found advantage estimates oscillate near zero with demo-only data. The gap: no work achieves advantage-conditioned (not weighted) VLA training in a purely offline setting using hindsight reward, and no work leverages VLA's pre-trained semantic features to improve the discriminative power of offline advantage estimation for this purpose.\",\n  \"approach\": \"Train an IQL-style offline value function on demonstration data (Bridge V2, LIBERO) using the pretrained VLA's (OpenVLA-OFT, 7B) frozen intermediate features as state representations, with hindsight task-progress rewards derived from cosine similarity in VLA feature space — eliminating the need for environment interaction or hand-designed dense rewards. Compute per-timestep advantages A(s,a) = Q(s,a) - V(s) and discretize into bins (high/medium/low), prepending these as conditioning tokens to the VLA's input during LoRA fine-tuning, following RECAP's conditioning paradigm but purely offline. The key technical insight is that VLA features encode rich task semantics that overcome the advantage oscillation near zero observed by AFBC with simple state representations in demo-only settings — pretrained vision-language features provide the discriminative power needed to distinguish progress from noise without online interaction. At inference, conditioning on 'high-advantage' extracts a clean policy that leverages ALL demonstration data — including noisy timesteps as informative negative signal — outperforming both naive BC and advantage-filtering/weighting methods that discard or downweight suboptimal data.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~400h A100 (value function training ~60h, VLA fine-tuning across LIBERO suites ~160h, evaluation ~40h, ablations ~100h, debugging ~40h)\",\n      \"gpu_utilization\": \"~30-40% — GPU sits idle while researcher implements advantage-conditioning on top of OpenVLA-OFT codebase, analyzes IQL value function convergence, diagnoses advantage oscillation, and iterates on feature extraction strategy\",\n      \"timeline\": \"3-5 months\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"$600-1,000 (spot instances at ~$1.50/hr, efficient instance management)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~350h A100\",\n      \"gpu_utilization\": \"~60-70% vs manual — agent autonomously queues IQL hyperparameter sweeps and VLA fine-tuning runs between human check-ins, reducing idle gaps significantly\",\n      \"timeline\": \"3-5 weeks\",\n      \"team\": \"1 researcher, ~30-45min/day check-in to review value function convergence plots and approve advantage discretization thresholds\",\n      \"claude_api_cost\": \"$150-300 (~2000-4000 turns at ~$0.08/turn)\",\n      \"estimated_gpu_cost\": \"$525-700\",\n      \"risk_note\": \"Offline advantage estimates may oscillate near zero with demo-only data (AFBC finding); human judgment critical to diagnose value function convergence and adjust IQL expectile parameter or feature extraction layer\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~800h A100 (3-5x more exploration: IQL hyperparameters, VLA feature layer selection, advantage discretization bins, conditioning token formats, and comprehensive ablations)\",\n      \"gpu_utilization\": \"~90-95% — agent runs 24/7, auto-queues next experiment immediately upon completion, explores value function architectures and advantage computation variants in parallel across GPUs\",\n      \"timeline\": \"5-10 days with 4-8 A100 GPUs\",\n      \"team\": \"0 (only initial setup and final review)\",\n      \"claude_api_cost\": \"$400-800 (~5000-10000 turns)\",\n      \"estimated_gpu_cost\": \"$1,200-1,600\",\n      \"speed_bottleneck\": \"GPU count — with 8 A100s, IQL sweeps and VLA LoRA fine-tuning run in parallel across 4 LIBERO suites; with 1-2 GPUs, sequential exploration extends to 2-3 weeks\",\n      \"risk_note\": \"Agent may over-explore IQL hyperparameter regions without recognizing advantage oscillation failure mode; advantage discretization thresholds require careful calibration that may benefit from human intuition about value function convergence\"\n    }\n  },\n  \"target_venues\": [\n    \"CoRL 2026 (paper deadline May 28-29, 2026)\",\n    \"ICLR 2027 (~October 2026)\",\n    \"AAAI 2027 (~August 2026)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"π*0.6: a VLA That Learns From Experience (arXiv 2025)\",\n    \"Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance (CoRL 2024)\",\n    \"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning (ICLR 2026)\",\n    \"Vision Language Models are In-Context Value Learners (ICLR 2025)\",\n    \"Offline Reinforcement Learning with Implicit Q-Learning (ICLR 2022)\",\n    \"A Closer Look at Advantage-Filtered Behavioral Cloning in High-Noise Datasets (arXiv 2021)\",\n    \"OpenVLA: An Open-Source Vision-Language-Action Model (CoRL 2024)\",\n    \"Balancing Signal and Variance: Adaptive Offline RL Post-Training for VLA Flow Models (AAAI 2026)\",\n    \"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success (RSS 2025)\",\n    \"VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators (arXiv 2025)\"\n  ],\n  \"description\": \"We propose Offline Advantage-Conditioned VLA (OAC-VLA), a method for improving Vision-Language-Action model fine-tuning on noisy demonstrations without any environment interaction. Unlike RECAP (Physical Intelligence, 2025) which requires online rollouts and expert corrections, OAC-VLA operates purely offline by training an IQL-based value function on demonstration data using the VLA's own frozen pretrained features as state representations and hindsight task-progress rewards derived via cosine similarity in VLA feature space. Per-timestep advantages are discretized into conditioning tokens prepended to the VLA's input during LoRA fine-tuning, enabling the model to explicitly learn what good and bad actions look like. At test time, conditioning on high-advantage tokens extracts a clean policy. The key technical contribution is leveraging semantically rich VLA features to overcome the advantage oscillation near zero identified by AFBC (2021) in demo-only offline settings. Unlike advantage-weighting approaches (ARFM, GVL), advantage conditioning preserves all data as informative signal rather than downweighting suboptimal demonstrations. Evaluated on LIBERO and SimplerEnv using OpenVLA-OFT (7B) as the base model, this approach removes the robot-interaction bottleneck for RL-enhanced VLA training, making advantage conditioning accessible to any lab with demonstration data alone.\",\n  \"project_name\": \"offline_adv_cond_vla\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 1)\nIssues: [\"CRITICAL — Advantage oscillation near zero with demo-only data (AFBC 2021): The paper's core mechanism depends on reliable per-timestep advantage estimates from demonstration data alone. AFBC showed advantages concentrate near zero in this regime, making binary/ternary discretization unreliable. The proposed fix (VLA features provide discriminative power) is speculative with zero empirical evidence.\", \"CRITICAL — OOD conditioning instability (CWBC, NeurIPS 2022): At test time, always conditioning on 'high-advantage' requires extrapolation beyond the training distribution. CWBC showed this conditioning approach degrades performance — the model hasn't learned what 'high-advantage behavior' looks like in unseen states. This directly undermines the advantage-conditioning mechanism.\", \"MISSED COMPETITOR — GR-RL (ByteDance, Dec 2025): Uses offline RL Q-values as task progress function to filter noisy demonstrations for VLA training. Stage 1 is demonstration distillation via RL scoring — directly relevant and uncited. Must be discussed and differentiated.\", \"MISSED COMPETITOR — SARM/RA-BC: Uses progress-delta reward model to weight BC loss for π₀ VLA fine-tuning, fully offline. Another demonstration quality scoring approach the generator missed.\", \"MISALIGNMENT WITH USER REQUIREMENTS: The user explicitly requested 'filtering and re-weighting' as the approach (demonstration distillation pipeline). The proposed idea argues against both filtering and weighting in favor of conditioning — a creative departure but not what was requested. The user's eval protocol (noise injection at 10/30/50%, robustness gap reporting, LIBERO-PLUS/PRO emphasis) is also underspecified in the proposal.\", \"NOVELTY OVERLAP WITH A2PO (NeurIPS 2024): A2PO already conditions on advantage values in offline RL from mixed-quality datasets. While it uses CVAE (not token conditioning) and targets D4RL (not VLAs), the conceptual novelty of 'advantage-conditioned offline policy learning from mixed-quality data' is already published at a top venue.\", \"RESOURCE ESTIMATE MISMATCH: User specified ≤200 H100-hours; proposal estimates ~400 A100-hours (manual), which is approximately 200 H100-hours at the boundary. With ablations and debugging overhead, likely exceeds the constraint. Auto estimate of 800 A100-hours (~400 H100-hours) is clearly over budget.\"]\nFeedback: The idea has a clear positioning gap (offline advantage conditioning for VLAs) but faces two fundamental technical risks that must be addressed before this can pass:\n\n1. **Address AFBC advantage oscillation head-on**: Don't just claim VLA features will fix it — design a concrete mechanism. Options: (a) use VLM-based zero-shot value estimation (GVL-style) instead of IQL, since VLMs don't suffer from the bootstrapping issues that cause oscillation; (b) use trajectory-level return ranking (not timestep advantage) as a more robust signal; (c) use a two-phase approach where coarse trajectory scoring bootstraps fine-grained timestep scoring.\n\n2. **Address CWBC's conditioning reliability concern**: The 'condition on high-advantage at test time' paradigm has known failure modes. Consider: (a) training with advantage weighting AND conditioning jointly; (b) using conservative conditioning (condition on 'above-median' rather than 'maximum'); (c) adding a consistency term that penalizes large performance gaps between conditioning values.\n\n3. **Cite and differentiate from GR-RL and SARM/RA-BC**: These are direct competitors in the 'RL scoring for VLA demo quality' space. GR-RL filters at trajectory level then does online RL; SARM weights at chunk level. Position OAC-VLA's timestep-level conditioning as finer-grained.\n\n4. **Realign with user requirements**: The user asked for demonstration distillation via filtering/re-weighting, not conditioning. Either: (a) reframe the method as a distillation pipeline that uses advantage scores for curriculum-weighted fine-tuning (closer to user's seed), or (b) include filtering/weighting as ablation baselines to demonstrate conditioning's superiority.\n\n5. **Strengthen robustness evaluation**: Specify the noise injection protocol (10/30/50% noisy demos), detail LIBERO-PLUS/PRO evaluation, and report the robustness gap metric the user requested.\n\n6. **Reduce compute to fit ≤200 H100-hours**: Consider using smaller VLA (SmolVLA) for initial validation, limit ablations, or use LIBERO subset.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\")."
}
```

---

### Runtime record

_source line 2 · 2026-05-14T05:56:58.313Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T05:56:58.313Z",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80"
}
```

---

## Round 1

98 recorded events

### User

_source line 3 · 2026-05-14T05:56:58.338Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-14 (UTC).**

## Original idea
{
  "title": "Offline Advantage Conditioning for VLA Noise Decomposition",
  "core_problem": "RECAP/π*0.6 demonstrated that advantage-conditioned VLA training dramatically improves policy quality by learning from both good and bad actions, but requires costly online robot interaction (rollouts and expert corrections). Can advantage conditioning work in a purely offline setting — learning the value function on existing demonstrations alone via hindsight reward — to decompose noise from signal without any environment access?",
  "opportunity": "RECAP (Physical Intelligence, Nov 2025) proved advantage conditioning is remarkably effective for VLA training: the model learns to map (state, high-advantage) → expert action and (state, low-advantage) → suboptimal action, using ALL data including noisy examples as informative negative signal. V-GPS (CoRL 2024) proved value functions can be trained offline on demos alone. Combining these enables offline advantage-conditioned VLA fine-tuning: unlike filtering approaches (which discard noisy timesteps), the VLA explicitly learns what noise looks like and what to avoid. At test time, conditioning on high advantage extracts the clean policy. This is more sample-efficient than filtering and avoids the binary keep/discard threshold problem.",
  "landscape": "RECAP/π*0.6 (Physical Intelligence, Nov 2025) uses advantage conditioning for VLA training, roughly halving failure rates on hard real-world tasks, but requires online rollouts and expert correction data — inaccessible for most labs. SimpleVLA-RL (ICLR 2026) achieves 430% improvement via online GRPO but needs parallel simulation environments. VLA-RFT (Oct 2025) uses world-model rollouts for RL fine-tuning. ARFM (AAAI 2026) performs offline RL post-training for VLA flow models via advantage weighting with Leave-One-Out estimation, but requires hand-designed 13-component dense reward functions and uses reweighting rather than conditioning. GVL (ICLR 2025 Spotlight) demonstrates VLM-based zero-shot value estimation with advantage-weighted regression on demonstrations, but targets diffusion policies rather than VLAs and uses weighting rather than conditioning. CO-RFT (arXiv 2025) does offline Q-learning for VLAs from 30-60 demos but without advantage conditioning. In the purely offline regime, AFBC (2021) showed advantage-filtered BC can learn from 65:1 noise ratios but found advantage estimates oscillate near zero with demo-only data. The gap: no work achieves advantage-conditioned (not weighted) VLA training in a purely offline setting using hindsight reward, and no work leverages VLA's pre-trained semantic features to improve the discriminative power of offline advantage estimation for this purpose.",
  "approach": "Train an IQL-style offline value function on demonstration data (Bridge V2, LIBERO) using the pretrained VLA's (OpenVLA-OFT, 7B) frozen intermediate features as state representations, with hindsight task-progress rewards derived from cosine similarity in VLA feature space — eliminating the need for environment interaction or hand-designed dense rewards. Compute per-timestep advantages A(s,a) = Q(s,a) - V(s) and discretize into bins (high/medium/low), prepending these as conditioning tokens to the VLA's input during LoRA fine-tuning, following RECAP's conditioning paradigm but purely offline. The key technical insight is that VLA features encode rich task semantics that overcome the advantage oscillation near zero observed by AFBC with simple state representations in demo-only settings — pretrained vision-language features provide the discriminative power needed to distinguish progress from noise without online interaction. At inference, conditioning on 'high-advantage' extracts a clean policy that leverages ALL demonstration data — including noisy timesteps as informative negative signal — outperforming both naive BC and advantage-filtering/weighting methods that discard or downweight suboptimal data.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~400h A100 (value function training ~60h, VLA fine-tuning across LIBERO suites ~160h, evaluation ~40h, ablations ~100h, debugging ~40h)",
      "gpu_utilization": "~30-40% — GPU sits idle while researcher implements advantage-conditioning on top of OpenVLA-OFT codebase, analyzes IQL value function convergence, diagnoses advantage oscillation, and iterates on feature extraction strategy",
      "timeline": "3-5 months",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "$600-1,000 (spot instances at ~$1.50/hr, efficient instance management)"
    },
    "human_in_loop": {
      "gpu_hours": "~350h A100",
      "gpu_utilization": "~60-70% vs manual — agent autonomously queues IQL hyperparameter sweeps and VLA fine-tuning runs between human check-ins, reducing idle gaps significantly",
      "timeline": "3-5 weeks",
      "team": "1 researcher, ~30-45min/day check-in to review value function convergence plots and approve advantage discretization thresholds",
      "claude_api_cost": "$150-300 (~2000-4000 turns at ~$0.08/turn)",
      "estimated_gpu_cost": "$525-700",
      "risk_note": "Offline advantage estimates may oscillate near zero with demo-only data (AFBC finding); human judgment critical to diagnose value function convergence and adjust IQL expectile parameter or feature extraction layer"
    },
    "auto_research": {
      "gpu_hours": "~800h A100 (3-5x more exploration: IQL hyperparameters, VLA feature layer selection, advantage discretization bins, conditioning token formats, and comprehensive ablations)",
      "gpu_utilization": "~90-95% — agent runs 24/7, auto-queues next experiment immediately upon completion, explores value function architectures and advantage computation variants in parallel across GPUs",
      "timeline": "5-10 days with 4-8 A100 GPUs",
      "team": "0 (only initial setup and final review)",
      "claude_api_cost": "$400-800 (~5000-10000 turns)",
      "estimated_gpu_cost": "$1,200-1,600",
      "speed_bottleneck": "GPU count — with 8 A100s, IQL sweeps and VLA LoRA fine-tuning run in parallel across 4 LIBERO suites; with 1-2 GPUs, sequential exploration extends to 2-3 weeks",
      "risk_note": "Agent may over-explore IQL hyperparameter regions without recognizing advantage oscillation failure mode; advantage discretization thresholds require careful calibration that may benefit from human intuition about value function convergence"
    }
  },
  "target_venues": [
    "CoRL 2026 (paper deadline May 28-29, 2026)",
    "ICLR 2027 (~October 2026)",
    "AAAI 2027 (~August 2026)"
  ],
  "level": "solid",
  "key_references": [
    "π*0.6: a VLA That Learns From Experience (arXiv 2025)",
    "Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance (CoRL 2024)",
    "SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning (ICLR 2026)",
    "Vision Language Models are In-Context Value Learners (ICLR 2025)",
    "Offline Reinforcement Learning with Implicit Q-Learning (ICLR 2022)",
    "A Closer Look at Advantage-Filtered Behavioral Cloning in High-Noise Datasets (arXiv 2021)",
    "OpenVLA: An Open-Source Vision-Language-Action Model (CoRL 2024)",
    "Balancing Signal and Variance: Adaptive Offline RL Post-Training for VLA Flow Models (AAAI 2026)",
    "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success (RSS 2025)",
    "VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators (arXiv 2025)"
  ],
  "description": "We propose Offline Advantage-Conditioned VLA (OAC-VLA), a method for improving Vision-Language-Action model fine-tuning on noisy demonstrations without any environment interaction. Unlike RECAP (Physical Intelligence, 2025) which requires online rollouts and expert corrections, OAC-VLA operates purely offline by training an IQL-based value function on demonstration data using the VLA's own frozen pretrained features as state representations and hindsight task-progress rewards derived via cosine similarity in VLA feature space. Per-timestep advantages are discretized into conditioning tokens prepended to the VLA's input during LoRA fine-tuning, enabling the model to explicitly learn what good and bad actions look like. At test time, conditioning on high-advantage tokens extracts a clean policy. The key technical contribution is leveraging semantically rich VLA features to overcome the advantage oscillation near zero identified by AFBC (2021) in demo-only offline settings. Unlike advantage-weighting approaches (ARFM, GVL), advantage conditioning preserves all data as informative signal rather than downweighting suboptimal demonstrations. Evaluated on LIBERO and SimplerEnv using OpenVLA-OFT (7B) as the base model, this approach removes the robot-interaction bottleneck for RL-enhanced VLA training, making advantage conditioning accessible to any lab with demonstration data alone.",
  "project_name": "offline_adv_cond_vla",
  "source": "web_research"
}

## Reviewer feedback (round 1)
Issues: ["CRITICAL — Advantage oscillation near zero with demo-only data (AFBC 2021): The paper's core mechanism depends on reliable per-timestep advantage estimates from demonstration data alone. AFBC showed advantages concentrate near zero in this regime, making binary/ternary discretization unreliable. The proposed fix (VLA features provide discriminative power) is speculative with zero empirical evidence.", "CRITICAL — OOD conditioning instability (CWBC, NeurIPS 2022): At test time, always conditioning on 'high-advantage' requires extrapolation beyond the training distribution. CWBC showed this conditioning approach degrades performance — the model hasn't learned what 'high-advantage behavior' looks like in unseen states. This directly undermines the advantage-conditioning mechanism.", "MISSED COMPETITOR — GR-RL (ByteDance, Dec 2025): Uses offline RL Q-values as task progress function to filter noisy demonstrations for VLA training. Stage 1 is demonstration distillation via RL scoring — directly relevant and uncited. Must be discussed and differentiated.", "MISSED COMPETITOR — SARM/RA-BC: Uses progress-delta reward model to weight BC loss for π₀ VLA fine-tuning, fully offline. Another demonstration quality scoring approach the generator missed.", "MISALIGNMENT WITH USER REQUIREMENTS: The user explicitly requested 'filtering and re-weighting' as the approach (demonstration distillation pipeline). The proposed idea argues against both filtering and weighting in favor of conditioning — a creative departure but not what was requested. The user's eval protocol (noise injection at 10/30/50%, robustness gap reporting, LIBERO-PLUS/PRO emphasis) is also underspecified in the proposal.", "NOVELTY OVERLAP WITH A2PO (NeurIPS 2024): A2PO already conditions on advantage values in offline RL from mixed-quality datasets. While it uses CVAE (not token conditioning) and targets D4RL (not VLAs), the conceptual novelty of 'advantage-conditioned offline policy learning from mixed-quality data' is already published at a top venue.", "RESOURCE ESTIMATE MISMATCH: User specified ≤200 H100-hours; proposal estimates ~400 A100-hours (manual), which is approximately 200 H100-hours at the boundary. With ablations and debugging overhead, likely exceeds the constraint. Auto estimate of 800 A100-hours (~400 H100-hours) is clearly over budget."]
Feedback: The idea has a clear positioning gap (offline advantage conditioning for VLAs) but faces two fundamental technical risks that must be addressed before this can pass:

1. **Address AFBC advantage oscillation head-on**: Don't just claim VLA features will fix it — design a concrete mechanism. Options: (a) use VLM-based zero-shot value estimation (GVL-style) instead of IQL, since VLMs don't suffer from the bootstrapping issues that cause oscillation; (b) use trajectory-level return ranking (not timestep advantage) as a more robust signal; (c) use a two-phase approach where coarse trajectory scoring bootstraps fine-grained timestep scoring.

2. **Address CWBC's conditioning reliability concern**: The 'condition on high-advantage at test time' paradigm has known failure modes. Consider: (a) training with advantage weighting AND conditioning jointly; (b) using conservative conditioning (condition on 'above-median' rather than 'maximum'); (c) adding a consistency term that penalizes large performance gaps between conditioning values.

3. **Cite and differentiate from GR-RL and SARM/RA-BC**: These are direct competitors in the 'RL scoring for VLA demo quality' space. GR-RL filters at trajectory level then does online RL; SARM weights at chunk level. Position OAC-VLA's timestep-level conditioning as finer-grained.

4. **Realign with user requirements**: The user asked for demonstration distillation via filtering/re-weighting, not conditioning. Either: (a) reframe the method as a distillation pipeline that uses advantage scores for curriculum-weighted fine-tuning (closer to user's seed), or (b) include filtering/weighting as ablation baselines to demonstrate conditioning's superiority.

5. **Strengthen robustness evaluation**: Specify the noise injection protocol (10/30/50% noisy demos), detail LIBERO-PLUS/PRO evaluation, and report the robustness gap metric the user requested.

6. **Reduce compute to fit ≤200 H100-hours**: Consider using smaller VLA (SmolVLA) for initial validation, limit ablations, or use LIBERO subset.

## Instructions
- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.
- Address each issue specifically.

## 深度调研要求（每一轮修订都必须执行）

不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。

1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。
   - 搜索最新的相关论文（arXiv, conference proceedings）
   - 搜索 benchmark/leaderboard 确认当前 SOTA
   - 搜索可能遗漏的相关工作和 concurrent work

2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，
   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。

3. **深度思考**：在修订之前，先独立思考以下问题：
   - 这个 idea 的核心假设是否仍然成立？
   - reviewer 的批评是否揭示了更深层的问题？
   - 有没有更好的 framing 或 approach 来解决同一个核心问题？
   - 修订后的 idea 相比上一版有什么本质性的改进？

4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，
   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。

## 针对 Review 意见的定向搜索

对 reviewer 指出的每个问题，执行以下搜索流程：

1. **如果 reviewer 说'已有类似工作'**：
   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读
   - 搜索该论文的 cited-by，找到后续跟进工作
   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot

2. **如果 reviewer 说'SOTA 过时'**：
   - 用 Papers With Code 查看当前排行榜
   - 搜索过去 6 个月的最新方法
   - 更新你的 landscape 和 baseline

3. **如果 reviewer 说'可行性有问题'**：
   - 搜索类似规模实验的实际成本和时间线
   - 搜索 GitHub 上是否有可复用的实现
   - 搜索相关数据集/模型的可获取性

4. **如果 reviewer 说'novelty 不足'**：
   - 对核心方法尽量做 3-5 种不同关键词组合的搜索
   - 搜索相邻领域是否有类似思路
   - 如果确实 novelty 不足，考虑 major revision 或 pivot

- Use WebSearch to find updated information if the reviewer flagged outdated claims.
- You have full freedom in how much to change:
  - Minor fix: if only specific details are wrong, correct them and keep everything else.
  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.
  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.
- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.
- In the output JSON, include a "change_type" field with one of: "minor", "major", or "pivot" to indicate the scope of your changes.
- Output the revised idea as a COMPLETE JSON object (same schema as original, plus "change_type").

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "b1021e79-7c12-4830-9429-5c2d39a89b04",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T05:56:58.336Z_

```json
{
  "parentUuid": "b1021e79-7c12-4830-9429-5c2d39a89b04",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
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
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
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
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "b91df3aa-8cb1-4b57-813e-30c2cd472aa2",
  "timestamp": "2026-05-14T05:56:58.336Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T05:56:58.337Z_

```json
{
  "parentUuid": "b91df3aa-8cb1-4b57-813e-30c2cd472aa2",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4110503d-c1c6-4bdc-9184-18425feaebd8",
  "timestamp": "2026-05-14T05:56:58.337Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Offline Advantage Conditioning for VLA Noise Decomposition\",   \"core_p…",
  "leafUuid": "4110503d-c1c6-4bdc-9184-18425feaebd8",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Offline VLA fine-tuning via trajectory-level return ranking and conservative advantage weighting",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80"
}
```

---

### Assistant

_source line 8 · 2026-05-14T05:57:12.091Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully before diving into research. The issues are:

1. **CRITICAL - AFBC advantage oscillation**: Core mechanism depends on reliable per-timestep advantages from demo-only data, but AFBC showed these concentrate near zero.
2. **CRITICAL - OOD conditioning instability (CWBC)**: Conditioning on 'high-advantage' at test time requires extrapolation beyond training distribution.
3. **MISSED COMPETITOR - GR-RL**: ByteDance's offline RL Q-values for filtering noisy demos.
4. **MISSED COMPETITOR - SARM/RA-BC**: Progress-delta reward model for weighting BC loss.


5. **MISALIGNMENT**: User wanted filtering/re-weighting, not conditioning.
6. **NOVELTY OVERLAP - A2PO**: Already conditions on advantage values in offline RL.
7. **RESOURCE ESTIMATE MISMATCH**: Exceeds ≤200 H100-hours budget.

The two critical flaws—advantage oscillation in AFBC and the out-of-distribution extrapolation problem in CWBC—expose fundamental weaknesses in the conditioning approach. Combined with the misalignment between what was proposed and what was actually needed, I need to pivot toward a filtering or re-weighting strategy that directly addresses the core problem rather than relying on conditioning.

Let me look at the relevant literature and see what competitors are doing in this space.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4110503d-c1c6-4bdc-9184-18425feaebd8",
  "isSidechain": false,
  "requestId": "req_011Cb1wrn8mPd3jjiATGKMb7",
  "type": "assistant",
  "uuid": "396fadcc-6d8d-4622-be62-b3c20dc9393c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jsx2FfNgw38sheXqgWCn1U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9731,
      "cache_read_input_tokens": 11841,
      "output_tokens": 448,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9731,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 448,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 9731,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9731
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

_source line 9 · 2026-05-14T05:57:12.127Z_

I'll start by researching the key papers and competitors flagged by the reviewer, then revise the idea based on findings. Let me search for the critical references in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "396fadcc-6d8d-4622-be62-b3c20dc9393c",
  "isSidechain": false,
  "requestId": "req_011Cb1wrn8mPd3jjiATGKMb7",
  "type": "assistant",
  "uuid": "90f64a3b-7225-4f0c-82a2-096f17154972",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jsx2FfNgw38sheXqgWCn1U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9731,
      "cache_read_input_tokens": 11841,
      "output_tokens": 448,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9731,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 448,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 9731,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9731
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

_source line 10 · 2026-05-14T05:57:12.239Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014u9UfX1iDHdqX5WvrrEHbS`</summary>

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
  "parentUuid": "90f64a3b-7225-4f0c-82a2-096f17154972",
  "isSidechain": false,
  "requestId": "req_011Cb1wrn8mPd3jjiATGKMb7",
  "type": "assistant",
  "uuid": "1b5e6985-ba2d-4410-af5e-ef9c1a7d381e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jsx2FfNgw38sheXqgWCn1U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9731,
      "cache_read_input_tokens": 11841,
      "output_tokens": 448,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9731,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 448,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 9731,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9731
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

_source line 11 · 2026-05-14T05:57:12.246Z_

<details><summary>↩ Tool result · `toolu_014u9UfX1iDHdqX5WvrrEHbS`</summary>

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
  "parentUuid": "1b5e6985-ba2d-4410-af5e-ef9c1a7d381e",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "e7714103-6f89-4bf1-841c-dbf3b1c6ebff",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "1b5e6985-ba2d-4410-af5e-ef9c1a7d381e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-14T05:57:15.340Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for all the key papers and competitors in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7714103-6f89-4bf1-841c-dbf3b1c6ebff",
  "isSidechain": false,
  "requestId": "req_011Cb1wsonWSvkBitFtyH4Wj",
  "type": "assistant",
  "uuid": "eda8f923-40ac-46be-81f8-a180321dcb32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016XbJEuhAdTpRx15tmcbsvf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1468,
      "cache_read_input_tokens": 21572,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1468,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 117,
          "cache_read_input_tokens": 21572,
          "cache_creation_input_tokens": 1468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1468
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

_source line 13 · 2026-05-14T05:57:15.822Z_

Let me research all the critical issues flagged by reviewers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eda8f923-40ac-46be-81f8-a180321dcb32",
  "isSidechain": false,
  "requestId": "req_011Cb1wsonWSvkBitFtyH4Wj",
  "type": "assistant",
  "uuid": "29b3630a-67ec-4acd-8569-d166c5e83cd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016XbJEuhAdTpRx15tmcbsvf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1468,
      "cache_read_input_tokens": 21572,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1468,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 117,
          "cache_read_input_tokens": 21572,
          "cache_creation_input_tokens": 1468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1468
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

_source line 14 · 2026-05-14T05:57:16.846Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FyU5g6VwCwq47ZwW48zgRg`</summary>

```json
{
  "query": "CWBC conditional weighted behavior cloning NeurIPS 2022 OOD conditioning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29b3630a-67ec-4acd-8569-d166c5e83cd6",
  "isSidechain": false,
  "requestId": "req_011Cb1wsonWSvkBitFtyH4Wj",
  "type": "assistant",
  "uuid": "6b38bc02-9db9-48cb-af76-a6e677f14169",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016XbJEuhAdTpRx15tmcbsvf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1468,
      "cache_read_input_tokens": 21572,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1468,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 117,
          "cache_read_input_tokens": 21572,
          "cache_creation_input_tokens": 1468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1468
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

_source line 15 · 2026-05-14T05:57:28.387Z_

<details><summary>↩ Tool result · `toolu_01FyU5g6VwCwq47ZwW48zgRg`</summary>

```text
Web search results for query: "CWBC conditional weighted behavior cloning NeurIPS 2022 OOD conditioning"

Links: [{"title":"Reliable Conditioning of Behavioral Cloning for Ofﬂine Reinforcement Learning","url":"https://arxiv.org/pdf/2210.05158"},{"title":"[2210.05158] Reliable Conditioning of Behavioral Cloning for Offline Reinforcement Learning","url":"https://arxiv.org/abs/2210.05158"},{"title":"ConserWeightive Behavioral Cloning for Reliable Offline Reinforcement Learning","url":"https://openreview.net/pdf?id=Ed4X0HxYFfH"},{"title":"ConserWeightive Behavioral Cloning for Reliable Offline Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=Ed4X0HxYFfH"},{"title":"(PDF) ConserWeightive Behavioral Cloning for Reliable Offline Reinforcement Learning","url":"https://www.researchgate.net/publication/364530051_ConserWeightive_Behavioral_Cloning_for_Reliable_Offline_Reinforcement_Learning"},{"title":"Reward-Aligned Behavior Cloning","url":"https://www.emergentmind.com/topics/reward-aligned-behavior-cloning-ra-bc"},{"title":"ConserWeightive Behavioral Cloning for Reliable Offline Reinforcement Learning | DeepAI","url":"https://deepai.org/publication/conserweightive-behavioral-cloning-for-reliable-offline-reinforcement-learning"},{"title":"A Policy-Guided Imitation Approach for Offline Reinforcement Learning","url":"https://papers.neurips.cc/paper_files/paper/2022/file/1a0755b249b772ed5529796b0a7cc9bd-Paper-Conference.pdf"},{"title":"Behavioral Cloning in Imitation Learning","url":"https://www.emergentmind.com/topics/behavioral-cloning-bc"},{"title":"Behavior Transformers: Cloning k modes with one stone","url":"https://proceedings.neurips.cc/paper_files/paper/2022/file/90d17e882adbdda42349db6f50123817-Paper-Conference.pdf"}]

Based on the search results, I found comprehensive information about CWBC (ConserWeightive Behavioral Cloning):

## CWBC: ConserWeightive Behavioral Cloning

ConserWeightive Behavioral Cloning (CWBC) is a method for improving the reliability of conditional BC with two key components: trajectory weighting and conservative regularization.

### The Problem It Addresses

Methods can be unreliable, as their performance may degrade significantly when conditioned on high, out-of-distribution (OOD) returns. This is crucial in practice, as we often expect the policy to perform better than the offline dataset by conditioning on an OOD value.

### Key Components

Trajectory weighting upweights the high-return trajectories to reduce the train-test gap for BC methods, while conservative regularizer encourages the policy to stay close to the data distribution for OOD conditioning.

### Application and Results

CWBC has been studied in the context of RvS (Emmons et al., 2021) and Decision Transformers (Chen et al., 2021), and shows that CWBC significantly boosts their performance on various benchmarks. CWBC (RvS+W+C) outperforms the original RvS by 72% on average.

### NeurIPS 2022 Connection

The paper was presented at FMDM@NeurIPS2022 with the TL;DR: "Simple weighted sampling + conservative regularization based on l2 penalty improves robustness of conditional BC when conditioning on large out-of-distribution returns".


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b38bc02-9db9-48cb-af76-a6e677f14169",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "d631dfb9-7913-498d-91c6-55a90119904d",
  "toolUseResult": {
    "query": "CWBC conditional weighted behavior cloning NeurIPS 2022 OOD conditioning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VJLT1uoDEroPuaLd8hoST8",
        "content": [
          {
            "title": "Reliable Conditioning of Behavioral Cloning for Ofﬂine Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2210.05158"
          },
          {
            "title": "[2210.05158] Reliable Conditioning of Behavioral Cloning for Offline Reinforcement Learning",
            "url": "https://arxiv.org/abs/2210.05158"
          },
          {
            "title": "ConserWeightive Behavioral Cloning for Reliable Offline Reinforcement Learning",
            "url": "https://openreview.net/pdf?id=Ed4X0HxYFfH"
          },
          {
            "title": "ConserWeightive Behavioral Cloning for Reliable Offline Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=Ed4X0HxYFfH"
          },
          {
            "title": "(PDF) ConserWeightive Behavioral Cloning for Reliable Offline Reinforcement Learning",
            "url": "https://www.researchgate.net/publication/364530051_ConserWeightive_Behavioral_Cloning_for_Reliable_Offline_Reinforcement_Learning"
          },
          {
            "title": "Reward-Aligned Behavior Cloning",
            "url": "https://www.emergentmind.com/topics/reward-aligned-behavior-cloning-ra-bc"
          },
          {
            "title": "ConserWeightive Behavioral Cloning for Reliable Offline Reinforcement Learning | DeepAI",
            "url": "https://deepai.org/publication/conserweightive-behavioral-cloning-for-reliable-offline-reinforcement-learning"
          },
          {
            "title": "A Policy-Guided Imitation Approach for Offline Reinforcement Learning",
            "url": "https://papers.neurips.cc/paper_files/paper/2022/file/1a0755b249b772ed5529796b0a7cc9bd-Paper-Conference.pdf"
          },
          {
            "title": "Behavioral Cloning in Imitation Learning",
            "url": "https://www.emergentmind.com/topics/behavioral-cloning-bc"
          },
          {
            "title": "Behavior Transformers: Cloning k modes with one stone",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2022/file/90d17e882adbdda42349db6f50123817-Paper-Conference.pdf"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about CWBC (ConserWeightive Behavioral Cloning):\n\n## CWBC: ConserWeightive Behavioral Cloning\n\nConserWeightive Behavioral Cloning (CWBC) is a method for improving the reliability of conditional BC with two key components: trajectory weighting and conservative regularization.\n\n### The Problem It Addresses\n\nMethods can be unreliable, as their performance may degrade significantly when conditioned on high, out-of-distribution (OOD) returns. This is crucial in practice, as we often expect the policy to perform better than the offline dataset by conditioning on an OOD value.\n\n### Key Components\n\nTrajectory weighting upweights the high-return trajectories to reduce the train-test gap for BC methods, while conservative regularizer encourages the policy to stay close to the data distribution for OOD conditioning.\n\n### Application and Results\n\nCWBC has been studied in the context of RvS (Emmons et al., 2021) and Decision Transformers (Chen et al., 2021), and shows that CWBC significantly boosts their performance on various benchmarks. CWBC (RvS+W+C) outperforms the original RvS by 72% on average.\n\n### NeurIPS 2022 Connection\n\nThe paper was presented at FMDM@NeurIPS2022 with the TL;DR: \"Simple weighted sampling + conservative regularization based on l2 penalty improves robustness of conditional BC when conditioning on large out-of-distribution returns\"."
    ],
    "durationSeconds": 11.535983272999998
  },
  "sourceToolAssistantUUID": "6b38bc02-9db9-48cb-af76-a6e677f14169",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T05:57:31.631Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GBvBt8AxA7VFSRGZiH7KjG`</summary>

```json
{
  "query": "GR-RL ByteDance offline RL VLA demonstration filtering 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d631dfb9-7913-498d-91c6-55a90119904d",
  "isSidechain": false,
  "requestId": "req_011Cb1wtzicJ6Z3i2G4fbPWi",
  "type": "assistant",
  "uuid": "3b5fc9b5-6a1d-4fdb-ba4a-9002c0b06a28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPb5sHPK7mnMnQibXvvt1K",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1070,
      "cache_read_input_tokens": 23040,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1070,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 23040,
          "cache_creation_input_tokens": 1070,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1070
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

_source line 17 · 2026-05-14T05:57:38.756Z_

<details><summary>↩ Tool result · `toolu_01GBvBt8AxA7VFSRGZiH7KjG`</summary>

```text
Web search results for query: "GR-RL ByteDance offline RL VLA demonstration filtering 2025"

Links: [{"title":"GR-RL: A Breakthrough in Dexterous Manipulation, ...","url":"https://seed.bytedance.com/en/blog/seed-research-gr-rl-released-a-breakthrough-in-high-precision-manipulation-for-vla-models-applying-real-world-reinforcement-learning-to-shoe-lacing-for-the-first-time"},{"title":"GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation - Publications - ByteDance Seed Team","url":"https://seed.bytedance.com/en/public_papers/gr-rl-going-dexterous-and-precise-for-long-horizon-robotic-manipulation"},{"title":"Seed GR-RL","url":"https://seed.bytedance.com/en/gr_rl"},{"title":"GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation","url":"https://arxiv.org/html/2512.01801v1"},{"title":"[2512.01801] GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation","url":"https://arxiv.org/abs/2512.01801"},{"title":"GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation | alphaXiv","url":"https://www.alphaxiv.org/resources/2512.01801"},{"title":"Paper page - GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation","url":"https://huggingface.co/papers/2512.01801"},{"title":"Seed News - ByteDance Seed Team","url":"https://seed.bytedance.com/en/blog/seed-research-gr-3-released-a-generalist-robot-model-for-generalization-long-horizon-tasks-and-bi-manual-deformable-object-manipulation"},{"title":"VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation","url":"https://arxiv.org/html/2603.26666v1"},{"title":"Seed Research","url":"https://seed.bytedance.com/en/research"}]

Based on the search results, I found comprehensive information about GR-RL. Here's what the research reveals:

## Overview

GR-RL is a robotic learning framework that turns a generalist vision-language-action (VLA) policy into a highly capable specialist for long-horizon dexterous manipulation.

## Key Problem Addressed

In highly dexterous and precise manipulation tasks, human demonstrations are noisy and suboptimal. Research from the ByteDance Seed team identifies two fundamental flaws in the dominant imitation learning paradigms: suboptimal human demonstrations and a mismatch between training and inference.

## Multi-Stage Training Pipeline

GR-RL proposes a multi-stage training pipeline that filters, augments, and reinforces the demonstrations by reinforcement learning. First, GR-RL learns a vision-language-conditioned task progress, filters the demonstration trajectories, and only keeps the transitions that contribute positively to the progress. 

By directly applying offline RL with sparse reward, the resulting Q-values can be treated as a robust progress function.

## Demonstration Results

GR-RL achieves the industry's first demonstration of a robot continuously lacing an entire shoe. More specifically, GR-RL is the first learning-based policy that can autonomously lace up a shoe by threading shoelaces through multiple eyelets with an 83.3% success rate, a task requiring long-horizon reasoning, millimeter-level precision, and compliant soft-body interaction.

The research was released by ByteDance's Seed team in December 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b5fc9b5-6a1d-4fdb-ba4a-9002c0b06a28",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "89f61e2e-7f90-46dd-985b-a60bb8d9b518",
  "toolUseResult": {
    "query": "GR-RL ByteDance offline RL VLA demonstration filtering 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EM2r7UTZMNgoYLxCX4zpRo",
        "content": [
          {
            "title": "GR-RL: A Breakthrough in Dexterous Manipulation, ...",
            "url": "https://seed.bytedance.com/en/blog/seed-research-gr-rl-released-a-breakthrough-in-high-precision-manipulation-for-vla-models-applying-real-world-reinforcement-learning-to-shoe-lacing-for-the-first-time"
          },
          {
            "title": "GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation - Publications - ByteDance Seed Team",
            "url": "https://seed.bytedance.com/en/public_papers/gr-rl-going-dexterous-and-precise-for-long-horizon-robotic-manipulation"
          },
          {
            "title": "Seed GR-RL",
            "url": "https://seed.bytedance.com/en/gr_rl"
          },
          {
            "title": "GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation",
            "url": "https://arxiv.org/html/2512.01801v1"
          },
          {
            "title": "[2512.01801] GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation",
            "url": "https://arxiv.org/abs/2512.01801"
          },
          {
            "title": "GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation | alphaXiv",
            "url": "https://www.alphaxiv.org/resources/2512.01801"
          },
          {
            "title": "Paper page - GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation",
            "url": "https://huggingface.co/papers/2512.01801"
          },
          {
            "title": "Seed News - ByteDance Seed Team",
            "url": "https://seed.bytedance.com/en/blog/seed-research-gr-3-released-a-generalist-robot-model-for-generalization-long-horizon-tasks-and-bi-manual-deformable-object-manipulation"
          },
          {
            "title": "VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation",
            "url": "https://arxiv.org/html/2603.26666v1"
          },
          {
            "title": "Seed Research",
            "url": "https://seed.bytedance.com/en/research"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about GR-RL. Here's what the research reveals:\n\n## Overview\n\nGR-RL is a robotic learning framework that turns a generalist vision-language-action (VLA) policy into a highly capable specialist for long-horizon dexterous manipulation.\n\n## Key Problem Addressed\n\nIn highly dexterous and precise manipulation tasks, human demonstrations are noisy and suboptimal. Research from the ByteDance Seed team identifies two fundamental flaws in the dominant imitation learning paradigms: suboptimal human demonstrations and a mismatch between training and inference.\n\n## Multi-Stage Training Pipeline\n\nGR-RL proposes a multi-stage training pipeline that filters, augments, and reinforces the demonstrations by reinforcement learning. First, GR-RL learns a vision-language-conditioned task progress, filters the demonstration trajectories, and only keeps the transitions that contribute positively to the progress. \n\nBy directly applying offline RL with sparse reward, the resulting Q-values can be treated as a robust progress function.\n\n## Demonstration Results\n\nGR-RL achieves the industry's first demonstration of a robot continuously lacing an entire shoe. More specifically, GR-RL is the first learning-based policy that can autonomously lace up a shoe by threading shoelaces through multiple eyelets with an 83.3% success rate, a task requiring long-horizon reasoning, millimeter-level precision, and compliant soft-body interaction.\n\nThe research was released by ByteDance's Seed team in December 2025."
    ],
    "durationSeconds": 7.119429196999998
  },
  "sourceToolAssistantUUID": "3b5fc9b5-6a1d-4fdb-ba4a-9002c0b06a28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T05:57:41.697Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LEiQnDjswvp8JmGVWX55W2`</summary>

```json
{
  "query": "SARM RA-BC reward-aligned behavior cloning VLA pi0 offline 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89f61e2e-7f90-46dd-985b-a60bb8d9b518",
  "isSidechain": false,
  "requestId": "req_011Cb1wukrx2QKKw4cvbXJLA",
  "type": "assistant",
  "uuid": "d196685d-4cfd-47d7-bacc-01dc51a6c628",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NKDz7xdm5QakV59aYUfjZT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1041,
      "cache_read_input_tokens": 24110,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1041,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 24110,
          "cache_creation_input_tokens": 1041,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1041
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

_source line 19 · 2026-05-14T05:57:48.768Z_

<details><summary>↩ Tool result · `toolu_01LEiQnDjswvp8JmGVWX55W2`</summary>

```text
Web search results for query: "SARM RA-BC reward-aligned behavior cloning VLA pi0 offline 2025"

Links: [{"title":"Reward-Aligned Behavior Cloning","url":"https://www.emergentmind.com/topics/reward-aligned-behavior-cloning-ra-bc"},{"title":"[2509.25358] SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation","url":"https://arxiv.org/abs/2509.25358"},{"title":"SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation","url":"https://arxiv.org/html/2509.25358"},{"title":"SARM: Stage-Aware Reward Modeling · Hugging Face","url":"https://huggingface.co/docs/lerobot/sarm"},{"title":"SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation | OpenReview","url":"https://openreview.net/forum?id=aemqAxScl9"},{"title":"Posterior Behavioral Cloning: Pretraining BC Policies for Efficient RL Finetuning","url":"https://www.researchgate.net/publication/398851434_Posterior_Behavioral_Cloning_Pretraining_BC_Policies_for_Efficient_RL_Finetuning"},{"title":"Value-aligned Behavior Cloning for Offline Reinforcement Learning via Bi-level Optimization | OpenReview","url":"https://openreview.net/forum?id=elTJBP7Fbv"},{"title":"GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub","url":"https://github.com/PRIME-RL/SimpleVLA-RL"},{"title":"Improve Your VLA training: Using Reward Models to Filter Best Training Data - Tiny struggles","url":"https://www.tinystruggles.com/posts/improving_vla_training_with_reward_model/"},{"title":"Sarm - LeRobot","url":"https://www.mintlify.com/huggingface/lerobot/policies/sarm"}]

Based on the search results, here's what I found about SARM, RA-BC, VLA, and π0:

## SARM: Stage-Aware Reward Modeling

SARM is a Stage-Aware Reward Modeling approach for Long Horizon Robot Manipulation. It leverages natural language annotations to assign progress labels and enable stable reward estimation for multi-step tasks, with the learned reward model driving a Reward-Aligned Behavior Cloning (RA-BC) framework that filters higher-quality data and improves policy performance in both simulation and the real world.

## Reward-Aligned Behavior Cloning (RA-BC)

RA-BC filters and reweights demonstrations based on reward estimates. Reward-aligned filtering and weighting, powered by stage- and progress-aware reward models, boost real-world T-shirt folding success rates from 8% (BC) to 83% (RA-BC).

## Vision-Language-Action (VLA) Models and π0

Currently PI0, PI0.5 and SmolVLA are supported with RA-BC. π0 is a vision-language-action flow model for general robot control. The SARM paper's goal is to fine-tune π₀ on T-shirt folding, a "long-horizon, contact-rich manipulation task" involving deformable objects.

## Offline Learning Application

The approach focuses on offline learning settings where standard behavior cloning treats all demonstration frames equally, but real-world robot datasets are messy, containing hesitations, corrections, and variable-quality trajectories.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d196685d-4cfd-47d7-bacc-01dc51a6c628",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "b66f7b82-43b6-42dd-bd71-7d7719e750d1",
  "toolUseResult": {
    "query": "SARM RA-BC reward-aligned behavior cloning VLA pi0 offline 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_018FJVpwkdt27CZk1JFuRWmT",
        "content": [
          {
            "title": "Reward-Aligned Behavior Cloning",
            "url": "https://www.emergentmind.com/topics/reward-aligned-behavior-cloning-ra-bc"
          },
          {
            "title": "[2509.25358] SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation",
            "url": "https://arxiv.org/abs/2509.25358"
          },
          {
            "title": "SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation",
            "url": "https://arxiv.org/html/2509.25358"
          },
          {
            "title": "SARM: Stage-Aware Reward Modeling · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/sarm"
          },
          {
            "title": "SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation | OpenReview",
            "url": "https://openreview.net/forum?id=aemqAxScl9"
          },
          {
            "title": "Posterior Behavioral Cloning: Pretraining BC Policies for Efficient RL Finetuning",
            "url": "https://www.researchgate.net/publication/398851434_Posterior_Behavioral_Cloning_Pretraining_BC_Policies_for_Efficient_RL_Finetuning"
          },
          {
            "title": "Value-aligned Behavior Cloning for Offline Reinforcement Learning via Bi-level Optimization | OpenReview",
            "url": "https://openreview.net/forum?id=elTJBP7Fbv"
          },
          {
            "title": "GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub",
            "url": "https://github.com/PRIME-RL/SimpleVLA-RL"
          },
          {
            "title": "Improve Your VLA training: Using Reward Models to Filter Best Training Data - Tiny struggles",
            "url": "https://www.tinystruggles.com/posts/improving_vla_training_with_reward_model/"
          },
          {
            "title": "Sarm - LeRobot",
            "url": "https://www.mintlify.com/huggingface/lerobot/policies/sarm"
          }
        ]
      },
      "Based on the search results, here's what I found about SARM, RA-BC, VLA, and π0:\n\n## SARM: Stage-Aware Reward Modeling\n\nSARM is a Stage-Aware Reward Modeling approach for Long Horizon Robot Manipulation. It leverages natural language annotations to assign progress labels and enable stable reward estimation for multi-step tasks, with the learned reward model driving a Reward-Aligned Behavior Cloning (RA-BC) framework that filters higher-quality data and improves policy performance in both simulation and the real world.\n\n## Reward-Aligned Behavior Cloning (RA-BC)\n\nRA-BC filters and reweights demonstrations based on reward estimates. Reward-aligned filtering and weighting, powered by stage- and progress-aware reward models, boost real-world T-shirt folding success rates from 8% (BC) to 83% (RA-BC).\n\n## Vision-Language-Action (VLA) Models and π0\n\nCurrently PI0, PI0.5 and SmolVLA are supported with RA-BC. π0 is a vision-language-action flow model for general robot control. The SARM paper's goal is to fine-tune π₀ on T-shirt folding, a \"long-horizon, contact-rich manipulation task\" involving deformable objects.\n\n## Offline Learning Application\n\nThe approach focuses on offline learning settings where standard behavior cloning treats all demonstration frames equally, but real-world robot datasets are messy, containing hesitations, corrections, and variable-quality trajectories."
    ],
    "durationSeconds": 7.065237921
  },
  "sourceToolAssistantUUID": "d196685d-4cfd-47d7-bacc-01dc51a6c628",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Offline Advantage Conditioning for VLA Noise Decomposition\",   \"core_p…",
  "leafUuid": "b66f7b82-43b6-42dd-bd71-7d7719e750d1",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Offline VLA fine-tuning via trajectory-level return ranking and conservative advantage weighting",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80"
}
```

---

### Tool call

_source line 22 · 2026-05-14T05:57:51.201Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MnSFzrTXT8nHprKRszoz75`</summary>

```json
{
  "query": "A2PO advantage-aware policy optimization NeurIPS 2024 offline RL conditioning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b66f7b82-43b6-42dd-bd71-7d7719e750d1",
  "isSidechain": false,
  "requestId": "req_011Cb1wvVewG85Ntt7xvkgAz",
  "type": "assistant",
  "uuid": "d2edb57c-a105-4678-ba45-d3c697ccd394",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JrSUkB6758HHJp4R91XBzR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1011,
      "cache_read_input_tokens": 25151,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1011,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 25151,
          "cache_creation_input_tokens": 1011,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1011
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

_source line 23 · 2026-05-14T05:57:56.846Z_

<details><summary>↩ Tool result · `toolu_01MnSFzrTXT8nHprKRszoz75`</summary>

```text
Web search results for query: "A2PO advantage-aware policy optimization NeurIPS 2024 offline RL conditioning"

Links: [{"title":"A2PO: Towards Effective Offline Reinforcement Learning from an Advantage-aware Perspective","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/333a7697dbb67f09249337f81c27d749-Abstract-Conference.html"},{"title":"A2PO: Towards Effective Offline Reinforcement Learning ...","url":"https://arxiv.org/pdf/2403.07262"},{"title":"GitHub - Plankson/A2PO_gym: Official code for NeurIPS2024 (poster): \"A2PO: Towards Effective Offline Reinforcement Learning from an Advantage-aware Perspective\" in gym tasks.","url":"https://github.com/Plankson/A2PO_gym"},{"title":"NeurIPS Poster A2PO: Towards Effective Offline Reinforcement Learning from an Advantage-aware Perspective","url":"https://nips.cc/virtual/2024/poster/94058"},{"title":"Advantage-Aware Policy Optimization for Offline Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=mqCt76eiNt"},{"title":"[Quick Review] A2PO: Towards Effective Offline Reinforcement Learning from an Advantage-aware Perspective","url":"https://liner.com/review/a2po-towards-effective-offline-reinforcement-learning-from-an-advantageaware-perspective"},{"title":"[2403.07262] A2PO: Towards Effective Offline Reinforcement Learning from an Advantage-aware Perspective","url":"https://arxiv.org/abs/2403.07262"},{"title":"A2PO: Towards Effective Offline Reinforcement Learning from an Advantage-aware Perspective","url":"https://arxiv.org/html/2403.07262"},{"title":"A2PO: Towards Effective Offline Reinforcement Learning from an ...","url":"https://www.proceedings.com/content/079/079017-0915open.pdf"},{"title":"Advantage-Aware Policy Optimization for Offline Reinforcement Learning","url":"https://arxiv.org/html/2403.07262v1"}]

Based on the search results, here's information about A2PO (Advantage-Aware Policy Optimization):

## Overview

A2PO was presented at NeurIPS 2024 in the Main Conference Track as a method for offline reinforcement learning. The A2PO method explicitly constructs advantage-aware policy constraints for offline learning under mixed-quality datasets.

## Key Technical Approach

A2PO employs a conditional variational auto-encoder to disentangle the action distributions of intertwined behavior policies by modeling the advantage values of all training data as conditional variables. The agent can then follow such disentangled action distribution constraints to optimize the advantage-aware policy towards high advantage values.

## Problem It Addresses

Existing works often suffer from the constraint conflict issue when offline datasets are collected from multiple behavior policies, i.e., different behavior policies may exhibit inconsistent actions with distinct returns across the state space. Previous advantage-weighted methods prioritize samples with high advantage values for agent training while inevitably ignoring the diversity of behavior policy.

## Experimental Validation

Extensive experiments conducted on both the single-quality and mixed-quality datasets of the D4RL benchmark demonstrate that A2PO yields results superior to the counterparts.

The code is available at https://github.com/Plankson/A2PO.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2edb57c-a105-4678-ba45-d3c697ccd394",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "555772ea-cf02-4941-8018-e89b49b49d91",
  "toolUseResult": {
    "query": "A2PO advantage-aware policy optimization NeurIPS 2024 offline RL conditioning",
    "results": [
      {
        "tool_use_id": "srvtoolu_019x4tTHoRZNnWBdmjaNnrYk",
        "content": [
          {
            "title": "A2PO: Towards Effective Offline Reinforcement Learning from an Advantage-aware Perspective",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/hash/333a7697dbb67f09249337f81c27d749-Abstract-Conference.html"
          },
          {
            "title": "A2PO: Towards Effective Offline Reinforcement Learning ...",
            "url": "https://arxiv.org/pdf/2403.07262"
          },
          {
            "title": "GitHub - Plankson/A2PO_gym: Official code for NeurIPS2024 (poster): \"A2PO: Towards Effective Offline Reinforcement Learning from an Advantage-aware Perspective\" in gym tasks.",
            "url": "https://github.com/Plankson/A2PO_gym"
          },
          {
            "title": "NeurIPS Poster A2PO: Towards Effective Offline Reinforcement Learning from an Advantage-aware Perspective",
            "url": "https://nips.cc/virtual/2024/poster/94058"
          },
          {
            "title": "Advantage-Aware Policy Optimization for Offline Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=mqCt76eiNt"
          },
          {
            "title": "[Quick Review] A2PO: Towards Effective Offline Reinforcement Learning from an Advantage-aware Perspective",
            "url": "https://liner.com/review/a2po-towards-effective-offline-reinforcement-learning-from-an-advantageaware-perspective"
          },
          {
            "title": "[2403.07262] A2PO: Towards Effective Offline Reinforcement Learning from an Advantage-aware Perspective",
            "url": "https://arxiv.org/abs/2403.07262"
          },
          {
            "title": "A2PO: Towards Effective Offline Reinforcement Learning from an Advantage-aware Perspective",
            "url": "https://arxiv.org/html/2403.07262"
          },
          {
            "title": "A2PO: Towards Effective Offline Reinforcement Learning from an ...",
            "url": "https://www.proceedings.com/content/079/079017-0915open.pdf"
          },
          {
            "title": "Advantage-Aware Policy Optimization for Offline Reinforcement Learning",
            "url": "https://arxiv.org/html/2403.07262v1"
          }
        ]
      },
      "Based on the search results, here's information about A2PO (Advantage-Aware Policy Optimization):\n\n## Overview\n\nA2PO was presented at NeurIPS 2024 in the Main Conference Track as a method for offline reinforcement learning. The A2PO method explicitly constructs advantage-aware policy constraints for offline learning under mixed-quality datasets.\n\n## Key Technical Approach\n\nA2PO employs a conditional variational auto-encoder to disentangle the action distributions of intertwined behavior policies by modeling the advantage values of all training data as conditional variables. The agent can then follow such disentangled action distribution constraints to optimize the advantage-aware policy towards high advantage values.\n\n## Problem It Addresses\n\nExisting works often suffer from the constraint conflict issue when offline datasets are collected from multiple behavior policies, i.e., different behavior policies may exhibit inconsistent actions with distinct returns across the state space. Previous advantage-weighted methods prioritize samples with high advantage values for agent training while inevitably ignoring the diversity of behavior policy.\n\n## Experimental Validation\n\nExtensive experiments conducted on both the single-quality and mixed-quality datasets of the D4RL benchmark demonstrate that A2PO yields results superior to the counterparts.\n\nThe code is available at https://github.com/Plankson/A2PO."
    ],
    "durationSeconds": 5.640108698999997
  },
  "sourceToolAssistantUUID": "d2edb57c-a105-4678-ba45-d3c697ccd394",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T05:57:59.890Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QYeuPUQmijrnsDNu7pwNXD`</summary>

```json
{
  "query": "AFBC advantage filtered behavioral cloning demo-only data oscillation 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "555772ea-cf02-4941-8018-e89b49b49d91",
  "isSidechain": false,
  "requestId": "req_011Cb1ww6BLKPyMvo9r1g31M",
  "type": "assistant",
  "uuid": "e14eb45b-f728-4530-9d11-57a07c6b38e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018vWwE6hHZQH9YRCdT42hqQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 961,
      "cache_read_input_tokens": 26162,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 961,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 26162,
          "cache_creation_input_tokens": 961,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 961
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

_source line 25 · 2026-05-14T05:58:06.682Z_

<details><summary>↩ Tool result · `toolu_01QYeuPUQmijrnsDNu7pwNXD`</summary>

```text
Web search results for query: "AFBC advantage filtered behavioral cloning demo-only data oscillation 2021"

Links: [{"title":"A Closer Look at Advantage-Filtered Behavioral Cloning in High-Noise Datasets","url":"https://arxiv.org/html/2110.04698v2"},{"title":"(PDF) A Closer Look at Advantage-Filtered Behavioral Cloning in High-Noise Datasets","url":"https://www.researchgate.net/publication/355223836_A_Closer_Look_at_Advantage-Filtered_Behavioral_Cloning_in_High-Noise_Datasets"},{"title":"[2110.04698] A Closer Look at Advantage-Filtered Behavioral Cloning in High-Noise Datasets","url":"https://arxiv.org/abs/2110.04698"},{"title":"A Closer Look at Advantage-Filtered Behavioral Cloning in ...","url":"https://csdmp.github.io/docs/grigsby2021.pdf"},{"title":"Discriminator-Weighted Offline Imitation Learning from ...","url":"https://proceedings.mlr.press/v162/xu22l/xu22l.pdf"},{"title":"A Closer Look at Advantage-Filtered Behavioral Cloning in ...","url":"https://arxiv.org/pdf/2110.04698"},{"title":"Reliable Conditioning of Behavioral Cloning for Ofﬂine Reinforcement Learning","url":"https://arxiv.org/pdf/2210.05158"},{"title":"[2210.05158] Reliable Conditioning of Behavioral Cloning for Offline Reinforcement Learning","url":"https://arxiv.org/abs/2210.05158"},{"title":"Implicit Behavioral Cloning","url":"https://implicitbc.github.io/"},{"title":"Behavior Cloning","url":"https://www.emergentmind.com/topics/behavior-cloning"}]

The search found a highly relevant paper. Here's what the results show:

## Summary of Findings

The paper investigates the performance of AFBC (Advantage-Filtered Behavioral Cloning) as the quality of the dataset decreases, and useful demonstrations are hidden in sub-optimal noise.

### Key Issue with Demo-Only Data Oscillation

A critical problem identified in the research is related to advantage estimation oscillation in noisy datasets. Many of the demonstrations have advantage estimates that oscillate close enough to zero that they can be labeled as positive or negative based on randomness in the estimator. This is particularly problematic because they rely on a small fraction of each batch to compute gradients and improve the actor, with the effect being most apparent when using binary filters, where a large portion of each minibatch may be entirely disregarded.

### Solutions Proposed

The paper proposes using PER (Prioritized Experience Replay) which samples actions that are more likely to have positive advantage, meaning that fewer samples are masked or down-weighted by the advantage filter, leading to a dramatic improvement in performance on noisy datasets.

The paper is titled "A Closer Look at Advantage-Filtered Behavioral Cloning in High-Noise Datasets" by Jake Grigsby and colleagues, originally submitted to arXiv on October 10, 2021.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e14eb45b-f728-4530-9d11-57a07c6b38e1",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "2a4cfa2a-db1a-4ced-9a87-96db511a9e89",
  "toolUseResult": {
    "query": "AFBC advantage filtered behavioral cloning demo-only data oscillation 2021",
    "results": [
      {
        "tool_use_id": "srvtoolu_012rtTWvGsPeMhcZB7PPZxYM",
        "content": [
          {
            "title": "A Closer Look at Advantage-Filtered Behavioral Cloning in High-Noise Datasets",
            "url": "https://arxiv.org/html/2110.04698v2"
          },
          {
            "title": "(PDF) A Closer Look at Advantage-Filtered Behavioral Cloning in High-Noise Datasets",
            "url": "https://www.researchgate.net/publication/355223836_A_Closer_Look_at_Advantage-Filtered_Behavioral_Cloning_in_High-Noise_Datasets"
          },
          {
            "title": "[2110.04698] A Closer Look at Advantage-Filtered Behavioral Cloning in High-Noise Datasets",
            "url": "https://arxiv.org/abs/2110.04698"
          },
          {
            "title": "A Closer Look at Advantage-Filtered Behavioral Cloning in ...",
            "url": "https://csdmp.github.io/docs/grigsby2021.pdf"
          },
          {
            "title": "Discriminator-Weighted Offline Imitation Learning from ...",
            "url": "https://proceedings.mlr.press/v162/xu22l/xu22l.pdf"
          },
          {
            "title": "A Closer Look at Advantage-Filtered Behavioral Cloning in ...",
            "url": "https://arxiv.org/pdf/2110.04698"
          },
          {
            "title": "Reliable Conditioning of Behavioral Cloning for Ofﬂine Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2210.05158"
          },
          {
            "title": "[2210.05158] Reliable Conditioning of Behavioral Cloning for Offline Reinforcement Learning",
            "url": "https://arxiv.org/abs/2210.05158"
          },
          {
            "title": "Implicit Behavioral Cloning",
            "url": "https://implicitbc.github.io/"
          },
          {
            "title": "Behavior Cloning",
            "url": "https://www.emergentmind.com/topics/behavior-cloning"
          }
        ]
      },
      "The search found a highly relevant paper. Here's what the results show:\n\n## Summary of Findings\n\nThe paper investigates the performance of AFBC (Advantage-Filtered Behavioral Cloning) as the quality of the dataset decreases, and useful demonstrations are hidden in sub-optimal noise.\n\n### Key Issue with Demo-Only Data Oscillation\n\nA critical problem identified in the research is related to advantage estimation oscillation in noisy datasets. Many of the demonstrations have advantage estimates that oscillate close enough to zero that they can be labeled as positive or negative based on randomness in the estimator. This is particularly problematic because they rely on a small fraction of each batch to compute gradients and improve the actor, with the effect being most apparent when using binary filters, where a large portion of each minibatch may be entirely disregarded.\n\n### Solutions Proposed\n\nThe paper proposes using PER (Prioritized Experience Replay) which samples actions that are more likely to have positive advantage, meaning that fewer samples are masked or down-weighted by the advantage filter, leading to a dramatic improvement in performance on noisy datasets.\n\nThe paper is titled \"A Closer Look at Advantage-Filtered Behavioral Cloning in High-Noise Datasets\" by Jake Grigsby and colleagues, originally submitted to arXiv on October 10, 2021."
    ],
    "durationSeconds": 6.787201404999992
  },
  "sourceToolAssistantUUID": "e14eb45b-f728-4530-9d11-57a07c6b38e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-14T05:58:09.509Z_

Now let me fetch the actual papers for deeper understanding.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a4cfa2a-db1a-4ced-9a87-96db511a9e89",
  "isSidechain": false,
  "requestId": "req_011Cb1wwpEfHxBV4eZEyxF7f",
  "type": "assistant",
  "uuid": "2cb8433a-3afa-429b-b664-c0e2631cb88b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TQ6frzemLHqGRinFYrrcPa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 861,
      "cache_read_input_tokens": 27123,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 861,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 27123,
          "cache_creation_input_tokens": 861,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 861
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

_source line 27 · 2026-05-14T05:58:16.433Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EqBJV8ggRSNQivvPFk3qNk`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.01801",
  "prompt": "Extract the full method description of GR-RL. Specifically: (1) How does Stage 1 demonstration distillation work? (2) How are Q-values used as task progress function? (3) How are demonstrations filtered? (4) What is the full pipeline (Stage 1, 2, 3)? (5) What VLA model do they use? (6) What are the key results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cb8433a-3afa-429b-b664-c0e2631cb88b",
  "isSidechain": false,
  "requestId": "req_011Cb1wwpEfHxBV4eZEyxF7f",
  "type": "assistant",
  "uuid": "2e9062a7-5904-4814-b6a3-dcd28b2beaf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TQ6frzemLHqGRinFYrrcPa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 861,
      "cache_read_input_tokens": 27123,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 861,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 27123,
          "cache_creation_input_tokens": 861,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 861
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

_source line 28 · 2026-05-14T05:58:21.858Z_

<details><summary>↩ Tool result · `toolu_01EqBJV8ggRSNQivvPFk3qNk`</summary>

```text
# GR-RL Method Summary

Based on the arXiv abstract provided, I can only offer limited details, as the full paper content isn't included:

## Available Information:

**Pipeline Overview:**
The framework consists of three stages: "(1) filters, augments, and reinforces demonstrations by reinforcement learning."

**Stage 1 - Demonstration Filtering:**
The method "learns a vision-language-conditioned task progress, filters the demonstration trajectories, and only keeps the transitions that contribute positively to the progress." Notably, "Q-values can be treated as a robust progress function" derived from offline RL with sparse rewards.

**Stage 2 - Augmentation:**
"Morphological symmetry augmentation" is introduced to improve generalization and performance.

**Stage 3 - Online Refinement:**
The researchers "perform online RL by learning a latent space noise predictor" to align deployment behavior for high-precision control.

## Key Results:

The framework achieved "83.3% success rate" on shoe-lacing—described as "the first learning-based policy that can autonomously lace up a shoe by threading shoelaces through multiple eyelets." This task demands "long-horizon reasoning, millimeter-level precision, and compliant soft-body interaction."

## Limitations:

The abstract doesn't specify which VLA model was used or provide complete technical details on implementation. The full paper would be needed for comprehensive methodology coverage.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e9062a7-5904-4814-b6a3-dcd28b2beaf1",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "ee76e71d-95e0-496c-8d8a-cbc2bcfa75b8",
  "toolUseResult": {
    "bytes": 49954,
    "code": 200,
    "codeText": "OK",
    "result": "# GR-RL Method Summary\n\nBased on the arXiv abstract provided, I can only offer limited details, as the full paper content isn't included:\n\n## Available Information:\n\n**Pipeline Overview:**\nThe framework consists of three stages: \"(1) filters, augments, and reinforces demonstrations by reinforcement learning.\"\n\n**Stage 1 - Demonstration Filtering:**\nThe method \"learns a vision-language-conditioned task progress, filters the demonstration trajectories, and only keeps the transitions that contribute positively to the progress.\" Notably, \"Q-values can be treated as a robust progress function\" derived from offline RL with sparse rewards.\n\n**Stage 2 - Augmentation:**\n\"Morphological symmetry augmentation\" is introduced to improve generalization and performance.\n\n**Stage 3 - Online Refinement:**\nThe researchers \"perform online RL by learning a latent space noise predictor\" to align deployment behavior for high-precision control.\n\n## Key Results:\n\nThe framework achieved \"83.3% success rate\" on shoe-lacing—described as \"the first learning-based policy that can autonomously lace up a shoe by threading shoelaces through multiple eyelets.\" This task demands \"long-horizon reasoning, millimeter-level precision, and compliant soft-body interaction.\"\n\n## Limitations:\n\nThe abstract doesn't specify which VLA model was used or provide complete technical details on implementation. The full paper would be needed for comprehensive methodology coverage.",
    "durationMs": 5420,
    "url": "https://arxiv.org/abs/2512.01801"
  },
  "sourceToolAssistantUUID": "2e9062a7-5904-4814-b6a3-dcd28b2beaf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-14T05:58:21.865Z_

```json
{
  "parentUuid": "ee76e71d-95e0-496c-8d8a-cbc2bcfa75b8",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "eb956d38-9d1f-4b50-b08e-efd88bdf6dde",
  "timestamp": "2026-05-14T05:58:21.865Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-14T05:58:26.755Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EHAi9z67C3TKwcBNdN2D6S`</summary>

```json
{
  "url": "https://arxiv.org/html/2512.01801v1",
  "prompt": "Extract the detailed method of GR-RL, focusing on: (1) Stage 1: How exactly are Q-values from offline RL used as task progress function? What RL algorithm is used (IQL, CQL, etc.)? How is demo filtering done based on Q-values? (2) Stage 2: What is morphological symmetry augmentation? (3) Stage 3: How does online RL refine the policy? (4) What VLA base model do they use? (5) What datasets and benchmarks are used? (6) Key ablation results showing the contribution of each stage."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb956d38-9d1f-4b50-b08e-efd88bdf6dde",
  "isSidechain": false,
  "requestId": "req_011Cb1wxw8Rg48BeXfKLvuJZ",
  "type": "assistant",
  "uuid": "a2bb6722-6a17-46ef-96b4-f79034bde749",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JpqSXjhnEoZWZmUTb2G4tL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 621,
      "cache_read_input_tokens": 27984,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 621,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 217,
          "cache_read_input_tokens": 27984,
          "cache_creation_input_tokens": 621,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 621
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

_source line 31 · 2026-05-14T05:58:45.607Z_

<details><summary>↩ Tool result · `toolu_01EHAi9z67C3TKwcBNdN2D6S`</summary>

```text
# GR-RL Method Summary

## Stage 1: Data Filtering with Task Progress Evaluator

**RL Algorithm & Q-value Usage:**
The approach uses "TD3+BC" with "distributional reinforcement learning" to train a critic model. Critically, they "treat values as a discrete distribution with upper and lower bounds" (0 to 1), which "naturally reflects the progress of the task."

The sparse reward is defined as: positive only in the final k steps if the trajectory succeeds, zero otherwise. They augment failed trajectories using "hindsight experience replay" by marking retry keyframes in successful demonstrations.

**Demo Filtering Process:**
They compute progress ρ_t as the "mean of the categorical distribution" from Q-values. A sample is marked suboptimal if there's "a value drop greater than a certain threshold δ" in the sequence. These suboptimal transitions are excluded before behavior cloning on the filtered dataset.

**Key Insight:** Distributional critics provide "stronger robustness than non-distributional ones" under sparse rewards, avoiding severe overestimation that plagues regression-based critics.

---

## Stage 2: Morphological Symmetry Augmentation

This augmentation leverages bimanual robot structure:
- Horizontally flip RGB images, then swap left/right wrist camera views
- Mirror transform proprioception and actions via world-frame symmetry
- Flip spatial language descriptions (e.g., "hole on left" → "hole on right")

Result: "Symmetry data augmentation can effectively enhance the performance of the policy."

---

## Stage 3: Online Reinforcement Learning

**Problem Addressed:** System-level post-processing (temporal ensembling, receding horizon control) causes "mismatch between training and deployment."

**Solution:** Add a lightweight noise predictor (51.5M parameters) after the VLM backbone to predict initial noise for the action diffusion transformer. This enables "structured exploration in latent space" rather than action space.

Training objectives:
- Noise predictor maximizes Q_φ' values while penalizing divergence from standard normal via penalty term
- Separate critic Q_φ' in noise space trained via distillation to avoid backpropagating through the flow model
- Mix off-policy (673 offline rollout trajectories) and on-policy buffers equally

---

## Base VLA Model

They use **GR-3**, a large-scale generalist policy with "Mixture-of-Transformer architecture" (5B parameters). It employs "Qwen2.5-VL-3B-Instruct" as the vision-language backbone and predicts action chunks via "action diffusion transformer trained by flow matching objectives."

---

## Datasets & Benchmarks

- **Task:** Shoe lacing (threading shoelaces through multiple eyelets)
- **Robot:** ByteMini-v2 (7-DoF dual arms + mobile base)
- **Data:** Human teleoperated demonstrations with annotated retry keyframes
- **Reward:** Binary sparse signal (1 only when shoelace threaded correctly and placed on table)
- **Evaluation:** Success rate on real robot trials

---

## Key Ablation Results

| Stage | Success Rate |
|-------|--------------|
| Base GR-3 (behavior cloning) | 45.7% |
| + Data filtering | 61.6% |
| + Symmetry augmentation | 72.7% |
| + Online RL (500 steps) | 83.3% |

**Filtering Impact:** Removes suboptimal hesitations/mistakes from demonstrations, substantial 16% improvement alone.

**Augmentation Impact:** Smaller but consistent gains across all task stages.

**Online RL Impact:** Largest gains (>10%), rapidly recovering and exceeding offline performance despite initial distribution shift.

**Progress Evaluator Ablation:** Distributional critics outperform regression-based progress predictors, which "overly smooth" predictions and miss subtle millimeter-scale failures.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2bb6722-6a17-46ef-96b4-f79034bde749",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "e4b48ff8-8113-4ef8-91f1-ca0da08f0a5e",
  "toolUseResult": {
    "bytes": 125891,
    "code": 200,
    "codeText": "OK",
    "result": "# GR-RL Method Summary\n\n## Stage 1: Data Filtering with Task Progress Evaluator\n\n**RL Algorithm & Q-value Usage:**\nThe approach uses \"TD3+BC\" with \"distributional reinforcement learning\" to train a critic model. Critically, they \"treat values as a discrete distribution with upper and lower bounds\" (0 to 1), which \"naturally reflects the progress of the task.\"\n\nThe sparse reward is defined as: positive only in the final k steps if the trajectory succeeds, zero otherwise. They augment failed trajectories using \"hindsight experience replay\" by marking retry keyframes in successful demonstrations.\n\n**Demo Filtering Process:**\nThey compute progress ρ_t as the \"mean of the categorical distribution\" from Q-values. A sample is marked suboptimal if there's \"a value drop greater than a certain threshold δ\" in the sequence. These suboptimal transitions are excluded before behavior cloning on the filtered dataset.\n\n**Key Insight:** Distributional critics provide \"stronger robustness than non-distributional ones\" under sparse rewards, avoiding severe overestimation that plagues regression-based critics.\n\n---\n\n## Stage 2: Morphological Symmetry Augmentation\n\nThis augmentation leverages bimanual robot structure:\n- Horizontally flip RGB images, then swap left/right wrist camera views\n- Mirror transform proprioception and actions via world-frame symmetry\n- Flip spatial language descriptions (e.g., \"hole on left\" → \"hole on right\")\n\nResult: \"Symmetry data augmentation can effectively enhance the performance of the policy.\"\n\n---\n\n## Stage 3: Online Reinforcement Learning\n\n**Problem Addressed:** System-level post-processing (temporal ensembling, receding horizon control) causes \"mismatch between training and deployment.\"\n\n**Solution:** Add a lightweight noise predictor (51.5M parameters) after the VLM backbone to predict initial noise for the action diffusion transformer. This enables \"structured exploration in latent space\" rather than action space.\n\nTraining objectives:\n- Noise predictor maximizes Q_φ' values while penalizing divergence from standard normal via penalty term\n- Separate critic Q_φ' in noise space trained via distillation to avoid backpropagating through the flow model\n- Mix off-policy (673 offline rollout trajectories) and on-policy buffers equally\n\n---\n\n## Base VLA Model\n\nThey use **GR-3**, a large-scale generalist policy with \"Mixture-of-Transformer architecture\" (5B parameters). It employs \"Qwen2.5-VL-3B-Instruct\" as the vision-language backbone and predicts action chunks via \"action diffusion transformer trained by flow matching objectives.\"\n\n---\n\n## Datasets & Benchmarks\n\n- **Task:** Shoe lacing (threading shoelaces through multiple eyelets)\n- **Robot:** ByteMini-v2 (7-DoF dual arms + mobile base)\n- **Data:** Human teleoperated demonstrations with annotated retry keyframes\n- **Reward:** Binary sparse signal (1 only when shoelace threaded correctly and placed on table)\n- **Evaluation:** Success rate on real robot trials\n\n---\n\n## Key Ablation Results\n\n| Stage | Success Rate |\n|-------|--------------|\n| Base GR-3 (behavior cloning) | 45.7% |\n| + Data filtering | 61.6% |\n| + Symmetry augmentation | 72.7% |\n| + Online RL (500 steps) | 83.3% |\n\n**Filtering Impact:** Removes suboptimal hesitations/mistakes from demonstrations, substantial 16% improvement alone.\n\n**Augmentation Impact:** Smaller but consistent gains across all task stages.\n\n**Online RL Impact:** Largest gains (>10%), rapidly recovering and exceeding offline performance despite initial distribution shift.\n\n**Progress Evaluator Ablation:** Distributional critics outperform regression-based progress predictors, which \"overly smooth\" predictions and miss subtle millimeter-scale failures.",
    "durationMs": 18848,
    "url": "https://arxiv.org/html/2512.01801v1"
  },
  "sourceToolAssistantUUID": "a2bb6722-6a17-46ef-96b4-f79034bde749",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Offline Advantage Conditioning for VLA Noise Decomposition\",   \"core_p…",
  "leafUuid": "e4b48ff8-8113-4ef8-91f1-ca0da08f0a5e",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Offline VLA fine-tuning via trajectory-level return ranking and conservative advantage weighting",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80"
}
```

---

### Tool call

_source line 34 · 2026-05-14T05:58:51.978Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013nptRtm7FSZBAPvNJM18uh`</summary>

```json
{
  "url": "https://arxiv.org/html/2509.25358",
  "prompt": "Extract the detailed method of SARM (Stage-Aware Reward Modeling) and RA-BC (Reward-Aligned Behavior Cloning). Specifically: (1) How is the reward model trained? What signals does it use? (2) How does RA-BC filter and reweight demonstrations? (3) What VLA model is used as base? (4) What is the full training pipeline? (5) Key results comparing RA-BC to standard BC. (6) Is this purely offline or does it require online interaction?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4b48ff8-8113-4ef8-91f1-ca0da08f0a5e",
  "isSidechain": false,
  "requestId": "req_011Cb1wzghKBmc1ZBcYrjZX8",
  "type": "assistant",
  "uuid": "1eb832e1-a091-4ef8-83f4-c6333768bf31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016E7L2WSJ63mQzHGJ7JgMT7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1144,
      "cache_read_input_tokens": 28605,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1144,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 28605,
          "cache_creation_input_tokens": 1144,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1144
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

_source line 35 · 2026-05-14T05:59:01.102Z_

<details><summary>↩ Tool result · `toolu_013nptRtm7FSZBAPvNJM18uh`</summary>

```text
# SARM and RA-BC: Method Summary

## (1) Reward Model Training

**Training signals:** SARM uses a dual-head architecture that jointly predicts task stage and fine-grained progress. The model derives progress labels from natural language subtask annotations rather than frame indices. 

The approach computes dataset-level priors for each subtask's temporal proportion, then assigns normalized progress targets through linear interpolation within subtasks. As stated in the paper: "progress labels remain closely aligned with the semantic meaning of the motions while maintaining consistency."

**Architecture:** A frozen CLIP encoder processes RGB frames, which are combined with joint states and processed through a transformer backbone (8 layers, 12 heads). Twin MLP heads output stage logits and continuous progress predictions [0,1].

## (2) RA-BC Filtering and Reweighting

RA-BC computes progress deltas between consecutive observation windows using the trained reward model. Each training sample receives a weight based on its estimated reward signal:

- Raw deltas are mapped to weights using running statistics (mean and standard deviation)
- A linear ramp clips values between (μ-2σ) and (μ+2σ)
- Prior overrides assign full weight to items exceeding threshold κ

The weighted loss becomes: "sum of weighted losses divided by sum of weights plus epsilon."

## (3) Base VLA Model

The work fine-tunes **π0**, described as "a vision-language-action flow model for general robot control." Training uses low-rank adaptation (LoRA) across dual GPUs.

## (4) Training Pipeline

1. Collect demonstrations with subtask annotations
2. Train SARM reward model on annotated data
3. Apply SARM to compute progress deltas on full diverse dataset
4. Fine-tune π0 using RA-BC with computed weights
5. Evaluate on real robot tasks (T-shirt folding at multiple difficulty levels)

## (5) Key Results

On T-shirt folding from flattened state, RA-BC-SARM achieved **83% success** at 40K steps versus:
- BC-All (standard): ~8%
- BC-2min (filtered by duration): ~58%
- RA-BC-ReWiND: ~58%

On hard task (crumpled state): RA-BC-SARM reached **67% success** compared to 0% for standard approaches.

## (6) Offline vs. Online

This is **purely offline imitation learning**. The approach requires no online robot interaction during policy training—only pre-collected demonstrations with annotations and a pre-trained base model (π0).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1eb832e1-a091-4ef8-83f4-c6333768bf31",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "562427ef-6273-4b93-a7e0-77804fa863a8",
  "toolUseResult": {
    "bytes": 303117,
    "code": 200,
    "codeText": "OK",
    "result": "# SARM and RA-BC: Method Summary\n\n## (1) Reward Model Training\n\n**Training signals:** SARM uses a dual-head architecture that jointly predicts task stage and fine-grained progress. The model derives progress labels from natural language subtask annotations rather than frame indices. \n\nThe approach computes dataset-level priors for each subtask's temporal proportion, then assigns normalized progress targets through linear interpolation within subtasks. As stated in the paper: \"progress labels remain closely aligned with the semantic meaning of the motions while maintaining consistency.\"\n\n**Architecture:** A frozen CLIP encoder processes RGB frames, which are combined with joint states and processed through a transformer backbone (8 layers, 12 heads). Twin MLP heads output stage logits and continuous progress predictions [0,1].\n\n## (2) RA-BC Filtering and Reweighting\n\nRA-BC computes progress deltas between consecutive observation windows using the trained reward model. Each training sample receives a weight based on its estimated reward signal:\n\n- Raw deltas are mapped to weights using running statistics (mean and standard deviation)\n- A linear ramp clips values between (μ-2σ) and (μ+2σ)\n- Prior overrides assign full weight to items exceeding threshold κ\n\nThe weighted loss becomes: \"sum of weighted losses divided by sum of weights plus epsilon.\"\n\n## (3) Base VLA Model\n\nThe work fine-tunes **π0**, described as \"a vision-language-action flow model for general robot control.\" Training uses low-rank adaptation (LoRA) across dual GPUs.\n\n## (4) Training Pipeline\n\n1. Collect demonstrations with subtask annotations\n2. Train SARM reward model on annotated data\n3. Apply SARM to compute progress deltas on full diverse dataset\n4. Fine-tune π0 using RA-BC with computed weights\n5. Evaluate on real robot tasks (T-shirt folding at multiple difficulty levels)\n\n## (5) Key Results\n\nOn T-shirt folding from flattened state, RA-BC-SARM achieved **83% success** at 40K steps versus:\n- BC-All (standard): ~8%\n- BC-2min (filtered by duration): ~58%\n- RA-BC-ReWiND: ~58%\n\nOn hard task (crumpled state): RA-BC-SARM reached **67% success** compared to 0% for standard approaches.\n\n## (6) Offline vs. Online\n\nThis is **purely offline imitation learning**. The approach requires no online robot interaction during policy training—only pre-collected demonstrations with annotations and a pre-trained base model (π0).",
    "durationMs": 9119,
    "url": "https://arxiv.org/html/2509.25358"
  },
  "sourceToolAssistantUUID": "1eb832e1-a091-4ef8-83f4-c6333768bf31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-14T05:59:05.504Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0144euMPnhgkznUFqSzw5JVG`</summary>

```json
{
  "url": "https://arxiv.org/abs/2403.07262",
  "prompt": "Extract the key method details of A2PO (Advantage-Aware Policy Optimization): (1) How does it condition on advantage values? (2) What is the CVAE architecture used? (3) How does it handle mixed-quality offline datasets? (4) How does it differ from advantage-weighted methods? (5) What are the key limitations?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "562427ef-6273-4b93-a7e0-77804fa863a8",
  "isSidechain": false,
  "requestId": "req_011Cb1x1pyfyugTRF9kGN7T3",
  "type": "assistant",
  "uuid": "c0f7dd64-e147-47ff-9e75-457a8e9b403a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BVVG1wDzrwmZy4G6ejfCPj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 810,
      "cache_read_input_tokens": 29749,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 810,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 29749,
          "cache_creation_input_tokens": 810,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 810
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

_source line 37 · 2026-05-14T05:59:10.393Z_

<details><summary>↩ Tool result · `toolu_0144euMPnhgkznUFqSzw5JVG`</summary>

```text
# A2PO Method Analysis

Based on the arXiv abstract provided, here's what can be extracted about A2PO's key methodological aspects:

## (1) Advantage Value Conditioning
The method models "advantage values of all training data as conditional variables" within its generative framework, allowing the system to differentiate between high and low-value actions.

## (2) CVAE Architecture
A2PO employs "a conditional variational auto-encoder to disentangle the action distributions of intertwined behavior policies." However, specific architectural details beyond this description are not provided in the abstract.

## (3) Mixed-Quality Dataset Handling
The approach constructs "advantage-aware policy constraints for offline learning under mixed-quality datasets," directly addressing scenarios where multiple behavior policies contribute conflicting action preferences across the state space.

## (4) Distinction from Advantage-Weighted Methods
While earlier advantage-weighted approaches "prioritize samples with high advantage values," they "inevitably ignore the diversity of behavior policy." A2PO aims to maintain this diversity while still focusing on high-advantage actions through disentanglement.

## (5) Key Limitations
The abstract does not explicitly discuss limitations. It only notes that existing methods suffer from "constraint conflict issue when offline datasets are collected from multiple behavior policies."

**Note:** Complete architectural and limitation details would require reviewing the full paper, as the abstract focuses on problem motivation and high-level contributions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0f7dd64-e147-47ff-9e75-457a8e9b403a",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "82c96c6d-711e-49fc-93e2-93b5481767a8",
  "toolUseResult": {
    "bytes": 48624,
    "code": 200,
    "codeText": "OK",
    "result": "# A2PO Method Analysis\n\nBased on the arXiv abstract provided, here's what can be extracted about A2PO's key methodological aspects:\n\n## (1) Advantage Value Conditioning\nThe method models \"advantage values of all training data as conditional variables\" within its generative framework, allowing the system to differentiate between high and low-value actions.\n\n## (2) CVAE Architecture\nA2PO employs \"a conditional variational auto-encoder to disentangle the action distributions of intertwined behavior policies.\" However, specific architectural details beyond this description are not provided in the abstract.\n\n## (3) Mixed-Quality Dataset Handling\nThe approach constructs \"advantage-aware policy constraints for offline learning under mixed-quality datasets,\" directly addressing scenarios where multiple behavior policies contribute conflicting action preferences across the state space.\n\n## (4) Distinction from Advantage-Weighted Methods\nWhile earlier advantage-weighted approaches \"prioritize samples with high advantage values,\" they \"inevitably ignore the diversity of behavior policy.\" A2PO aims to maintain this diversity while still focusing on high-advantage actions through disentanglement.\n\n## (5) Key Limitations\nThe abstract does not explicitly discuss limitations. It only notes that existing methods suffer from \"constraint conflict issue when offline datasets are collected from multiple behavior policies.\"\n\n**Note:** Complete architectural and limitation details would require reviewing the full paper, as the abstract focuses on problem motivation and high-level contributions.",
    "durationMs": 4886,
    "url": "https://arxiv.org/abs/2403.07262"
  },
  "sourceToolAssistantUUID": "c0f7dd64-e147-47ff-9e75-457a8e9b403a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-14T05:59:13.002Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QkdUaDmfSUiZUKDKNFhajX`</summary>

```json
{
  "query": "CO-RFT offline Q-learning VLA 2025 arXiv demonstration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82c96c6d-711e-49fc-93e2-93b5481767a8",
  "isSidechain": false,
  "requestId": "req_011Cb1x2WjqNmtw6UwG3exyV",
  "type": "assistant",
  "uuid": "1954ac07-a62f-426a-96b7-8f045a6206e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015WPJu3VgRopms6N8zkwrPb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 482,
      "cache_read_input_tokens": 30559,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 482,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 30559,
          "cache_creation_input_tokens": 482,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 482
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

_source line 39 · 2026-05-14T05:59:20.161Z_

<details><summary>↩ Tool result · `toolu_01QkdUaDmfSUiZUKDKNFhajX`</summary>

```text
Web search results for query: "CO-RFT offline Q-learning VLA 2025 arXiv demonstration"

Links: [{"title":"CO-RFT: Efficient Fine-Tuning of Vision-Language-Action Models through Chunked Offline Reinforcement Learning","url":"https://arxiv.org/html/2508.02219v1"},{"title":"[2508.02219] CO-RFT: Efficient Fine-Tuning of Vision-Language-Action Models through Chunked Offline Reinforcement Learning","url":"https://arxiv.org/abs/2508.02219"},{"title":"CO-RFT: Efficient Fine-Tuning of Vision-Language-Action Models through","url":"https://arxiv.org/pdf/2508.02219"},{"title":"Openpi Comet: Competition Solution For 2025 BEHAVIOR Challenge","url":"https://arxiv.org/html/2512.10071"},{"title":"VLA-RFT: Vision-language-action Reinforcement fine-tuning with verified rewards in world simulators","url":"https://arxiv.org/html/2510.00406"},{"title":"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning","url":"https://arxiv.org/html/2601.06748v1"},{"title":"VLA-RFT: VISION-LANGUAGE-ACTION REINFORCE- MENT FINE-TUNING WITH VERIFIED","url":"https://arxiv.org/pdf/2510.00406"},{"title":"Openpi Comet: Competition Solution For 2025 BEHAVIOR Challenge Team Comet","url":"https://arxiv.org/pdf/2512.10071"},{"title":"VLA-RFT: Vision-Language-Action Reinforcement Fine-Tuning with Verified Rewards in World Simulators | OpenReview","url":"https://openreview.net/forum?id=Jaut99EHeu"},{"title":"DynVLA: Learning World Dynamics for Action Reasoning in Autonomous Driving","url":"https://arxiv.org/html/2603.11041"}]

Based on the search results, here's what I found about CO-RFT:

## CO-RFT: Chunked Offline Reinforcement Learning for VLAs

CO-RFT is an algorithm aimed at fine-tuning Vision-Language-Action (VLA) models using a limited set of demonstrations (30 to 60 samples). It explores the fine-tuning of VLA models through offline reinforcement learning incorporating action chunking, proposing Chunked RL, a novel reinforcement learning framework specifically designed for VLA models, which extends temporal difference (TD) learning to incorporate action chunking.

### Key Features:

The method first conducts imitation learning (IL) with full parameter fine-tuning to initialize both the backbone and the policy, and subsequently implements offline RL with action chunking to optimize the pretrained policy. In addition to VLMs and action experts commonly utilized in VLA models, the framework incorporates a critic expert to generate Q-values, with the critic expert predicting a sequence of Q-values based on the action chunk.

### Performance Results:

The empirical results in real-world environments demonstrate that CO-RFT outperforms previous supervised methods, achieving a 57% improvement in success rate and a 22.3% reduction in cycle time, with robust positional generalization capabilities, attaining a success rate of 44.3% in previously unseen positions.

The paper was published on arXiv on August 4, 2025 (arXiv:2508.02219).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1954ac07-a62f-426a-96b7-8f045a6206e4",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "4995d846-4857-4734-af40-cfaa6431ed4a",
  "toolUseResult": {
    "query": "CO-RFT offline Q-learning VLA 2025 arXiv demonstration",
    "results": [
      {
        "tool_use_id": "srvtoolu_018Wbghuf8J8tFNCqJk9a7GR",
        "content": [
          {
            "title": "CO-RFT: Efficient Fine-Tuning of Vision-Language-Action Models through Chunked Offline Reinforcement Learning",
            "url": "https://arxiv.org/html/2508.02219v1"
          },
          {
            "title": "[2508.02219] CO-RFT: Efficient Fine-Tuning of Vision-Language-Action Models through Chunked Offline Reinforcement Learning",
            "url": "https://arxiv.org/abs/2508.02219"
          },
          {
            "title": "CO-RFT: Efficient Fine-Tuning of Vision-Language-Action Models through",
            "url": "https://arxiv.org/pdf/2508.02219"
          },
          {
            "title": "Openpi Comet: Competition Solution For 2025 BEHAVIOR Challenge",
            "url": "https://arxiv.org/html/2512.10071"
          },
          {
            "title": "VLA-RFT: Vision-language-action Reinforcement fine-tuning with verified rewards in world simulators",
            "url": "https://arxiv.org/html/2510.00406"
          },
          {
            "title": "On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/html/2601.06748v1"
          },
          {
            "title": "VLA-RFT: VISION-LANGUAGE-ACTION REINFORCE- MENT FINE-TUNING WITH VERIFIED",
            "url": "https://arxiv.org/pdf/2510.00406"
          },
          {
            "title": "Openpi Comet: Competition Solution For 2025 BEHAVIOR Challenge Team Comet",
            "url": "https://arxiv.org/pdf/2512.10071"
          },
          {
            "title": "VLA-RFT: Vision-Language-Action Reinforcement Fine-Tuning with Verified Rewards in World Simulators | OpenReview",
            "url": "https://openreview.net/forum?id=Jaut99EHeu"
          },
          {
            "title": "DynVLA: Learning World Dynamics for Action Reasoning in Autonomous Driving",
            "url": "https://arxiv.org/html/2603.11041"
          }
        ]
      },
      "Based on the search results, here's what I found about CO-RFT:\n\n## CO-RFT: Chunked Offline Reinforcement Learning for VLAs\n\nCO-RFT is an algorithm aimed at fine-tuning Vision-Language-Action (VLA) models using a limited set of demonstrations (30 to 60 samples). It explores the fine-tuning of VLA models through offline reinforcement learning incorporating action chunking, proposing Chunked RL, a novel reinforcement learning framework specifically designed for VLA models, which extends temporal difference (TD) learning to incorporate action chunking.\n\n### Key Features:\n\nThe method first conducts imitation learning (IL) with full parameter fine-tuning to initialize both the backbone and the policy, and subsequently implements offline RL with action chunking to optimize the pretrained policy. In addition to VLMs and action experts commonly utilized in VLA models, the framework incorporates a critic expert to generate Q-values, with the critic expert predicting a sequence of Q-values based on the action chunk.\n\n### Performance Results:\n\nThe empirical results in real-world environments demonstrate that CO-RFT outperforms previous supervised methods, achieving a 57% improvement in success rate and a 22.3% reduction in cycle time, with robust positional generalization capabilities, attaining a success rate of 44.3% in previously unseen positions.\n\nThe paper was published on arXiv on August 4, 2025 (arXiv:2508.02219)."
    ],
    "durationSeconds": 7.153222721000027
  },
  "sourceToolAssistantUUID": "1954ac07-a62f-426a-96b7-8f045a6206e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-14T05:59:23.521Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W2ZWrrkXxvP2vhAsdgYeVX`</summary>

```json
{
  "query": "VLA demonstration distillation filtering noisy data offline reward model 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4995d846-4857-4734-af40-cfaa6431ed4a",
  "isSidechain": false,
  "requestId": "req_011Cb1x3EPcTicAgyF75qoiT",
  "type": "assistant",
  "uuid": "59dcf4d0-dab8-4b9d-94a4-1bfbf5f6ecbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FmhVMQqrRS9TbCtAPkGfQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 943,
      "cache_read_input_tokens": 31041,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 943,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 31041,
          "cache_creation_input_tokens": 943,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 943
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

_source line 41 · 2026-05-14T05:59:30.611Z_

<details><summary>↩ Tool result · `toolu_01W2ZWrrkXxvP2vhAsdgYeVX`</summary>

```text
Web search results for query: "VLA demonstration distillation filtering noisy data offline reward model 2025 2026"

Links: [{"title":"VLA-RFT: Vision-Language-Action Reinforcement Fine-Tuning with Verified Rewards in World Simulators | OpenReview","url":"https://openreview.net/forum?id=Jaut99EHeu"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | OpenReview","url":"https://openreview.net/forum?id=eUGoqrZ6Ea"},{"title":"2025-9-22 A Vision-Language-Action-Critic Model","url":"https://arxiv.org/pdf/2509.15937"},{"title":"SIMPLEVLA-RL: SCALING VLA TRAINING VIA RE","url":"https://openreview.net/pdf/04ee56414bb3cef5c18010f6993f98e74dbcd5aa.pdf"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"Refined Policy Distillation: From VLA Generalists to RL Experts","url":"https://arxiv.org/html/2503.05833v1"},{"title":"Self-Improving Vision-Language-Action Models with Data ...","url":"https://wenlixiao.com/self-improve-VLA-PLD/assets/doc/pld-fullpaper.pdf"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"Distill Not Only Data but Also Rewards: Can Smaller Language Models Surpass Larger Ones? | OpenReview","url":"https://openreview.net/forum?id=tK6VZy5RYr"}]

Based on the search results, I found several recent research papers (2025-2026) related to Vision-Language-Action (VLA) models that address demonstration distillation, filtering noisy data, and offline reward models:

## Key Papers Found:

**1. VLA-RFT (Vision-Language-Action Reinforcement Fine-Tuning)**
VLA-RFT is a Reinforcement Fine-Tuning framework that leverages a data-driven world model as a controllable simulator.

**2. PLD (Probe, Learn, Distill)**
PLD is a plug-and-play framework that improves VLAs through residual reinforcement learning and distribution-aware data collection. The collected data for multiple tasks are distilled back into the base model through supervised fine-tuning (SFT), a process agnostic to VLA architectures.

**3. VLAC (Vision-Language-Action-Critic Model)**
VLAC is a general process reward model trained on large scale heterogeneous datasets that outputs dense progress delta and done signal, eliminating task-specific reward engineering. It uses a graded human-in-the-loop protocol including offline demonstration replay, return and explore, and human guided explore.

**4. SimpleVLA-RL**
Recent breakthroughs show that using only sparse outcome rewards, RL can significantly enhance models' ability to generate correct step-by-step reasoning chains.

**5. Reward Distillation for LLMs**
A unified distillation framework transfers both responses and evaluation ability by distilling reward signals from the teacher, eliminating the need for costly human annotations.

These papers address key challenges in VLA research including handling noisy data, offline learning from demonstrations, and learning reward models without extensive manual labeling.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59dcf4d0-dab8-4b9d-94a4-1bfbf5f6ecbe",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "3547efd5-6797-42a5-b260-29484c1af6b0",
  "toolUseResult": {
    "query": "VLA demonstration distillation filtering noisy data offline reward model 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WfiF9MtnmBpPyK35QWXgcB",
        "content": [
          {
            "title": "VLA-RFT: Vision-Language-Action Reinforcement Fine-Tuning with Verified Rewards in World Simulators | OpenReview",
            "url": "https://openreview.net/forum?id=Jaut99EHeu"
          },
          {
            "title": "Pure Vision Language Action (VLA) Models: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2509.19012v1"
          },
          {
            "title": "Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | OpenReview",
            "url": "https://openreview.net/forum?id=eUGoqrZ6Ea"
          },
          {
            "title": "2025-9-22 A Vision-Language-Action-Critic Model",
            "url": "https://arxiv.org/pdf/2509.15937"
          },
          {
            "title": "SIMPLEVLA-RL: SCALING VLA TRAINING VIA RE",
            "url": "https://openreview.net/pdf/04ee56414bb3cef5c18010f6993f98e74dbcd5aa.pdf"
          },
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          },
          {
            "title": "Refined Policy Distillation: From VLA Generalists to RL Experts",
            "url": "https://arxiv.org/html/2503.05833v1"
          },
          {
            "title": "Self-Improving Vision-Language-Action Models with Data ...",
            "url": "https://wenlixiao.com/self-improve-VLA-PLD/assets/doc/pld-fullpaper.pdf"
          },
          {
            "title": "State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss",
            "url": "https://mbreuss.github.io/blog_post_iclr_26_vla.html"
          },
          {
            "title": "Distill Not Only Data but Also Rewards: Can Smaller Language Models Surpass Larger Ones? | OpenReview",
            "url": "https://openreview.net/forum?id=tK6VZy5RYr"
          }
        ]
      },
      "Based on the search results, I found several recent research papers (2025-2026) related to Vision-Language-Action (VLA) models that address demonstration distillation, filtering noisy data, and offline reward models:\n\n## Key Papers Found:\n\n**1. VLA-RFT (Vision-Language-Action Reinforcement Fine-Tuning)**\nVLA-RFT is a Reinforcement Fine-Tuning framework that leverages a data-driven world model as a controllable simulator.\n\n**2. PLD (Probe, Learn, Distill)**\nPLD is a plug-and-play framework that improves VLAs through residual reinforcement learning and distribution-aware data collection. The collected data for multiple tasks are distilled back into the base model through supervised fine-tuning (SFT), a process agnostic to VLA architectures.\n\n**3. VLAC (Vision-Language-Action-Critic Model)**\nVLAC is a general process reward model trained on large scale heterogeneous datasets that outputs dense progress delta and done signal, eliminating task-specific reward engineering. It uses a graded human-in-the-loop protocol including offline demonstration replay, return and explore, and human guided explore.\n\n**4. SimpleVLA-RL**\nRecent breakthroughs show that using only sparse outcome rewards, RL can significantly enhance models' ability to generate correct step-by-step reasoning chains.\n\n**5. Reward Distillation for LLMs**\nA unified distillation framework transfers both responses and evaluation ability by distilling reward signals from the teacher, eliminating the need for costly human annotations.\n\nThese papers address key challenges in VLA research including handling noisy data, offline learning from demonstrations, and learning reward models without extensive manual labeling."
    ],
    "durationSeconds": 7.087212303999986
  },
  "sourceToolAssistantUUID": "59dcf4d0-dab8-4b9d-94a4-1bfbf5f6ecbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-14T05:59:37.883Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BYdZWRmmnhB75zB5VoZMRL`</summary>

```json
{
  "query": "VLAC vision language action critic process reward model dense progress 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3547efd5-6797-42a5-b260-29484c1af6b0",
  "isSidechain": false,
  "requestId": "req_011Cb1x416vzsAXsWkAteS3C",
  "type": "assistant",
  "uuid": "d0a70702-9209-4fa0-96db-ee1345f5601e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PKrMTNX4JhqNYvfYo26DRL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1089,
      "cache_read_input_tokens": 31984,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1089,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 31984,
          "cache_creation_input_tokens": 1089,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1089
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

_source line 43 · 2026-05-14T05:59:44.701Z_

<details><summary>↩ Tool result · `toolu_01BYdZWRmmnhB75zB5VoZMRL`</summary>

```text
Web search results for query: "VLAC vision language action critic process reward model dense progress 2025"

Links: [{"title":"GitHub - InternRobotics/VLAC: VLAC: A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning · GitHub","url":"https://github.com/InternRobotics/VLAC"},{"title":"VLAC: A Generalist Action-Critic Model via Pair-wise Progress Understanding | OpenReview","url":"https://openreview.net/forum?id=PmYX0XiQQ0"},{"title":"[2509.15937] A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning","url":"https://arxiv.org/abs/2509.15937"},{"title":"2025-9-22 A Vision-Language-Action-Critic Model","url":"https://arxiv.org/pdf/2509.15937"},{"title":"A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning","url":"https://arxiv.org/html/2509.15937v1"},{"title":"Paper page - A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning","url":"https://huggingface.co/papers/2509.15937"},{"title":"[Quick Review] A Vision-Language-Action-Critic Model for Robotic Real-World\\n Reinforcement Learning","url":"https://liner.com/review/visionlanguageactioncritic-model-for-robotic-realworld-reinforcement-learning"},{"title":"InternRobotics/VLAC · Hugging Face","url":"https://huggingface.co/InternRobotics/VLAC"},{"title":"A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning - Paper Detail","url":"https://deeplearn.org/arxiv/638657/a-vision-language-action-critic-model-for-robotic-real-world-reinforcement-learning"},{"title":"Embodied AI Reading Notes on X: \"VLAC: A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning Project: https://t.co/dS3nHtlWeR Paper: https://t.co/QMg4znfTDf This VLA model unifies the role of “actor” and “critic” within a single autoregressive architecture by generating dense https://t.co/hr5SWJB7He\" / X","url":"https://x.com/EmbodiedAIRead/status/1968555311029158322"}]

Based on the search results, here's what I found about VLAC:

## Overview

VLAC is a general process reward model built upon InternVL and trained on large scale heterogeneous datasets. It is a generalist Vision Language Action-Critic model which can integrate both human and robot data, and unify action generation and task progress understanding within a single autoregressive architecture.

## Key Features

Given pairwise observations and a language goal, it outputs dense progress delta and done signal, eliminating task-specific reward engineering, and supports one-shot in-context transfer to unseen tasks and environments.

The model proposes a scalable and generalizable pair-wise progress understanding approach to predict the task progress delta between any two images in one visual trajectory, and generate the action based on the first image.

## Training Data

VLAC is trained on 3000h+ human egocentric data, 1200h+ comprehensive public robotic manipulation data, and 15h+ self-collected manipulation data.

## Real-World Performance

Across four distinct real-world manipulation tasks, VLAC lifts success rates from about 30% to about 90% within 200 real-world interaction episodes; incorporating human-in-the-loop interventions yields a further 50% improvement in sample efficiency and achieves up to 100% final success.

## Dense Reward Capabilities

It can predict task progress and distinguish failure action or trajectory, providing dense reward feedback for real-world RL and offering guidance for data refinement.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0a70702-9209-4fa0-96db-ee1345f5601e",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "9c7fb461-fd25-4b75-9a79-0226d7b16cb5",
  "toolUseResult": {
    "query": "VLAC vision language action critic process reward model dense progress 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_016RsHVg4Lcs27WLMtoTpS46",
        "content": [
          {
            "title": "GitHub - InternRobotics/VLAC: VLAC: A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning · GitHub",
            "url": "https://github.com/InternRobotics/VLAC"
          },
          {
            "title": "VLAC: A Generalist Action-Critic Model via Pair-wise Progress Understanding | OpenReview",
            "url": "https://openreview.net/forum?id=PmYX0XiQQ0"
          },
          {
            "title": "[2509.15937] A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning",
            "url": "https://arxiv.org/abs/2509.15937"
          },
          {
            "title": "2025-9-22 A Vision-Language-Action-Critic Model",
            "url": "https://arxiv.org/pdf/2509.15937"
          },
          {
            "title": "A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning",
            "url": "https://arxiv.org/html/2509.15937v1"
          },
          {
            "title": "Paper page - A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning",
            "url": "https://huggingface.co/papers/2509.15937"
          },
          {
            "title": "[Quick Review] A Vision-Language-Action-Critic Model for Robotic Real-World\\n Reinforcement Learning",
            "url": "https://liner.com/review/visionlanguageactioncritic-model-for-robotic-realworld-reinforcement-learning"
          },
          {
            "title": "InternRobotics/VLAC · Hugging Face",
            "url": "https://huggingface.co/InternRobotics/VLAC"
          },
          {
            "title": "A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning - Paper Detail",
            "url": "https://deeplearn.org/arxiv/638657/a-vision-language-action-critic-model-for-robotic-real-world-reinforcement-learning"
          },
          {
            "title": "Embodied AI Reading Notes on X: \"VLAC: A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning Project: https://t.co/dS3nHtlWeR Paper: https://t.co/QMg4znfTDf This VLA model unifies the role of “actor” and “critic” within a single autoregressive architecture by generating dense https://t.co/hr5SWJB7He\" / X",
            "url": "https://x.com/EmbodiedAIRead/status/1968555311029158322"
          }
        ]
      },
      "Based on the search results, here's what I found about VLAC:\n\n## Overview\n\nVLAC is a general process reward model built upon InternVL and trained on large scale heterogeneous datasets. It is a generalist Vision Language Action-Critic model which can integrate both human and robot data, and unify action generation and task progress understanding within a single autoregressive architecture.\n\n## Key Features\n\nGiven pairwise observations and a language goal, it outputs dense progress delta and done signal, eliminating task-specific reward engineering, and supports one-shot in-context transfer to unseen tasks and environments.\n\nThe model proposes a scalable and generalizable pair-wise progress understanding approach to predict the task progress delta between any two images in one visual trajectory, and generate the action based on the first image.\n\n## Training Data\n\nVLAC is trained on 3000h+ human egocentric data, 1200h+ comprehensive public robotic manipulation data, and 15h+ self-collected manipulation data.\n\n## Real-World Performance\n\nAcross four distinct real-world manipulation tasks, VLAC lifts success rates from about 30% to about 90% within 200 real-world interaction episodes; incorporating human-in-the-loop interventions yields a further 50% improvement in sample efficiency and achieves up to 100% final success.\n\n## Dense Reward Capabilities\n\nIt can predict task progress and distinguish failure action or trajectory, providing dense reward feedback for real-world RL and offering guidance for data refinement."
    ],
    "durationSeconds": 6.809924488000019
  },
  "sourceToolAssistantUUID": "d0a70702-9209-4fa0-96db-ee1345f5601e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Offline Advantage Conditioning for VLA Noise Decomposition\",   \"core_p…",
  "leafUuid": "9c7fb461-fd25-4b75-9a79-0226d7b16cb5",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Offline VLA fine-tuning via trajectory-level return ranking and conservative advantage weighting",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80"
}
```

---

### Tool call

_source line 46 · 2026-05-14T05:59:47.691Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Fx4XVGcUhtvn21ifcihXqT`</summary>

```json
{
  "query": "offline advantage estimation demonstration-only data VLA VLM value function 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c7fb461-fd25-4b75-9a79-0226d7b16cb5",
  "isSidechain": false,
  "requestId": "req_011Cb1x53LQMnXUxKt674VCG",
  "type": "assistant",
  "uuid": "08801b86-37e2-46cf-a16b-1b71a171ef6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012k9vFccnDtSDPig58DK8aY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1070,
      "cache_read_input_tokens": 33073,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1070,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 33073,
          "cache_creation_input_tokens": 1070,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1070
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

_source line 47 · 2026-05-14T05:59:55.638Z_

<details><summary>↩ Tool result · `toolu_01Fx4XVGcUhtvn21ifcihXqT`</summary>

```text
Web search results for query: "offline advantage estimation demonstration-only data VLA VLM value function 2025 2026"

Links: [{"title":"Generative Value Learning: Vision Language Models are In-Context Value Learners","url":"https://generative-value-learning.github.io/"},{"title":"Adaptive Q-Chunking for Offline-to-Online Reinforcement Learning","url":"https://arxiv.org/html/2605.05544"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"Generative AI in Industrial Robotics: 2026 Layers Guide","url":"https://www.evsint.com/generative-ai-industrial-robotics-foundation-models-code-generation-2026/"},{"title":"Exploring the Robustness of Vision-Language-Action Models against Sensor Attacks | Proceedings of the 2025 Workshop on Large AI Systems and Models with Privacy and Security Analysis","url":"https://dl.acm.org/doi/10.1145/3733800.3763262"},{"title":"VLM: How Vision-Language Models Work (2026 Guide) | Label Your Data","url":"https://labelyourdata.com/articles/machine-learning/vision-language-models"},{"title":"[2604.10701] Bringing Value Models Back: Generative Critics for Value Modeling in LLM Reinforcement Learning","url":"https://arxiv.org/abs/2604.10701"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"[2411.05273] Real-World Offline Reinforcement Learning from Vision Language Model Feedback","url":"https://arxiv.org/abs/2411.05273"},{"title":"VLA-OPD: Bridging Offline SFT and Online RL for...","url":"https://arxiv.org/abs/2603.26666"}]

I found several relevant results related to your search query. Here's what I discovered:

## Key Findings

**Generative Value Learning (GVL)**: A universal value function estimator that leverages the world knowledge embedded in vision-language models (VLMs) to predict task progress. GVL poses value estimation as a temporal ordering problem over shuffled video frames to encourage VLMs to exploit their semantic and temporal grounding capabilities. GVL can assign importance weights to individual transitions within trajectories at a fine-grained level akin to offline reinforcement learning, using real-world demonstration data collected by human teleoperation on bi-manual ALOHA robot setups.

**Adaptive Q-Chunking (AQC)**: Adaptive Q-Chunking resolves value comparison failures by comparing the advantage of each chunk size relative to a per-horizon baseline, normalized by the discount factor. AQC achieves state-of-the-art offline and online success rates on OGBench and Robomimic, and can be applied to enhance the performance of large-scale VLA models.

**Generative Actor-Critic (GenAC)**: A generative critic approach that replaces one-shot scalar value prediction with a critic that performs chain-of-thought reasoning before producing a value estimate.

**Offline RL with VLM Feedback**: A system that automatically generates reward labels for offline datasets using preference feedback from a vision-language model and learns a policy using offline RL with the reward-labeled dataset.

These approaches all address advantage and value function estimation challenges in vision-language-action models and offline reinforcement learning contexts within the 2025-2026 timeframe.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08801b86-37e2-46cf-a16b-1b71a171ef6c",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "d2c043cf-7a28-46e7-9e3a-ffcc83f164cc",
  "toolUseResult": {
    "query": "offline advantage estimation demonstration-only data VLA VLM value function 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JPR8xVedqspRqy5uuYBS45",
        "content": [
          {
            "title": "Generative Value Learning: Vision Language Models are In-Context Value Learners",
            "url": "https://generative-value-learning.github.io/"
          },
          {
            "title": "Adaptive Q-Chunking for Offline-to-Online Reinforcement Learning",
            "url": "https://arxiv.org/html/2605.05544"
          },
          {
            "title": "State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss",
            "url": "https://mbreuss.github.io/blog_post_iclr_26_vla.html"
          },
          {
            "title": "Generative AI in Industrial Robotics: 2026 Layers Guide",
            "url": "https://www.evsint.com/generative-ai-industrial-robotics-foundation-models-code-generation-2026/"
          },
          {
            "title": "Exploring the Robustness of Vision-Language-Action Models against Sensor Attacks | Proceedings of the 2025 Workshop on Large AI Systems and Models with Privacy and Security Analysis",
            "url": "https://dl.acm.org/doi/10.1145/3733800.3763262"
          },
          {
            "title": "VLM: How Vision-Language Models Work (2026 Guide) | Label Your Data",
            "url": "https://labelyourdata.com/articles/machine-learning/vision-language-models"
          },
          {
            "title": "[2604.10701] Bringing Value Models Back: Generative Critics for Value Modeling in LLM Reinforcement Learning",
            "url": "https://arxiv.org/abs/2604.10701"
          },
          {
            "title": "Vision-language-action model - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Vision-language-action_model"
          },
          {
            "title": "[2411.05273] Real-World Offline Reinforcement Learning from Vision Language Model Feedback",
            "url": "https://arxiv.org/abs/2411.05273"
          },
          {
            "title": "VLA-OPD: Bridging Offline SFT and Online RL for...",
            "url": "https://arxiv.org/abs/2603.26666"
          }
        ]
      },
      "I found several relevant results related to your search query. Here's what I discovered:\n\n## Key Findings\n\n**Generative Value Learning (GVL)**: A universal value function estimator that leverages the world knowledge embedded in vision-language models (VLMs) to predict task progress. GVL poses value estimation as a temporal ordering problem over shuffled video frames to encourage VLMs to exploit their semantic and temporal grounding capabilities. GVL can assign importance weights to individual transitions within trajectories at a fine-grained level akin to offline reinforcement learning, using real-world demonstration data collected by human teleoperation on bi-manual ALOHA robot setups.\n\n**Adaptive Q-Chunking (AQC)**: Adaptive Q-Chunking resolves value comparison failures by comparing the advantage of each chunk size relative to a per-horizon baseline, normalized by the discount factor. AQC achieves state-of-the-art offline and online success rates on OGBench and Robomimic, and can be applied to enhance the performance of large-scale VLA models.\n\n**Generative Actor-Critic (GenAC)**: A generative critic approach that replaces one-shot scalar value prediction with a critic that performs chain-of-thought reasoning before producing a value estimate.\n\n**Offline RL with VLM Feedback**: A system that automatically generates reward labels for offline datasets using preference feedback from a vision-language model and learns a policy using offline RL with the reward-labeled dataset.\n\nThese approaches all address advantage and value function estimation challenges in vision-language-action models and offline reinforcement learning contexts within the 2025-2026 timeframe."
    ],
    "durationSeconds": 7.942125468000013
  },
  "sourceToolAssistantUUID": "08801b86-37e2-46cf-a16b-1b71a171ef6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-14T05:59:58.391Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013Rqyt6a7mASCs6mc5Kssjh`</summary>

```json
{
  "query": "VLA-OPD offline SFT online RL vision language action on-policy distillation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2c043cf-7a28-46e7-9e3a-ffcc83f164cc",
  "isSidechain": false,
  "requestId": "req_011Cb1x5r5m7CiRdzoECuYrR",
  "type": "assistant",
  "uuid": "74cd586f-7807-4cc0-bb05-e7debcc459f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015NMmK4U3tyok27NXwq1CuZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 980,
      "cache_read_input_tokens": 34143,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 980,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 34143,
          "cache_creation_input_tokens": 980,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 980
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

_source line 49 · 2026-05-14T06:00:06.943Z_

<details><summary>↩ Tool result · `toolu_013Rqyt6a7mASCs6mc5Kssjh`</summary>

```text
Web search results for query: "VLA-OPD offline SFT online RL vision language action on-policy distillation 2026"

Links: [{"title":"VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation","url":"https://arxiv.org/html/2603.26666v1"},{"title":"[2603.26666] VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation","url":"https://arxiv.org/abs/2603.26666"},{"title":"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | OpenReview","url":"https://openreview.net/forum?id=eUGoqrZ6Ea"},{"title":"Paper page - Lightning OPD: Efficient Post-Training for Large Reasoning Models with Offline On-Policy Distillation","url":"https://huggingface.co/papers/2604.13010"},{"title":"VLA-RFT: Vision-Language-Action Reinforcement Fine-Tuning with Verified Rewards in World Simulators | OpenReview","url":"https://openreview.net/forum?id=Jaut99EHeu"},{"title":"PLD: Self-Improving Vision-Language-Action Models (ICLR 2026)","url":"https://wenlixiao.com/self-improve-VLA-PLD"},{"title":"Lightning OPD: Efficient Post-Training for Large Reasoning Models with Offline On-Policy Distillation","url":"https://arxiv.org/html/2604.13010"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"SOD: Step-wise On-policy Distillation for Small Language Model Agents","url":"https://arxiv.org/html/2605.07725"},{"title":"What Can RL Bring to VLA Generalization? An Empirical Study","url":"https://rlvla.github.io/"}]

Based on the web search results, I found relevant information about VLA-OPD:

## VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models

VLA-OPD is a framework addressing how pre-trained Vision-Language-Action (VLA) models require post-training to ensure reliable performance during deployment, where standard offline Supervised Fine-Tuning (SFT) suffers from distribution shifts and catastrophic forgetting, while online Reinforcement Learning (RL) struggles with sparse rewards and poor sample efficiency.

### Key Approach

VLA-OPD is a framework bridging the efficiency of SFT with the robustness of RL, leveraging an expert teacher to provide dense, token-level supervision on the student's self-generated trajectories instead of relying on sparse environmental rewards.

### Technical Innovation

The framework formulates a Reverse-KL distillation objective for VLA models, where its bounded mode-seeking property effectively filters out the teacher's epistemic uncertainty while maintaining action diversity, preventing both the entropy explosion of Forward-KL and the premature entropy collapse of Hard-CE.

### Performance Results

Extensive evaluations across LIBERO and RoboTwin2.0 benchmarks demonstrate that VLA-OPD achieves superior robustness and success rates compared to SFT, while requiring substantially fewer training steps than on-policy RL baselines.

Experiments on LIBERO and RoboTwin2.0 benchmarks demonstrate that VLA-OPD significantly improves sample efficiency over RL and robustness over SFT, while effectively mitigating catastrophic forgetting during post-training.

The paper was published in March 2026 on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74cd586f-7807-4cc0-bb05-e7debcc459f1",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "70c07ce6-ee24-42f5-97e6-2cb0da0d33b7",
  "toolUseResult": {
    "query": "VLA-OPD offline SFT online RL vision language action on-policy distillation 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NnkjcBRcdoLbw3aPTfuzvw",
        "content": [
          {
            "title": "VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation",
            "url": "https://arxiv.org/html/2603.26666v1"
          },
          {
            "title": "[2603.26666] VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation",
            "url": "https://arxiv.org/abs/2603.26666"
          },
          {
            "title": "Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | OpenReview",
            "url": "https://openreview.net/forum?id=eUGoqrZ6Ea"
          },
          {
            "title": "Paper page - Lightning OPD: Efficient Post-Training for Large Reasoning Models with Offline On-Policy Distillation",
            "url": "https://huggingface.co/papers/2604.13010"
          },
          {
            "title": "VLA-RFT: Vision-Language-Action Reinforcement Fine-Tuning with Verified Rewards in World Simulators | OpenReview",
            "url": "https://openreview.net/forum?id=Jaut99EHeu"
          },
          {
            "title": "PLD: Self-Improving Vision-Language-Action Models (ICLR 2026)",
            "url": "https://wenlixiao.com/self-improve-VLA-PLD"
          },
          {
            "title": "Lightning OPD: Efficient Post-Training for Large Reasoning Models with Offline On-Policy Distillation",
            "url": "https://arxiv.org/html/2604.13010"
          },
          {
            "title": "Pure Vision Language Action (VLA) Models: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2509.19012v1"
          },
          {
            "title": "SOD: Step-wise On-policy Distillation for Small Language Model Agents",
            "url": "https://arxiv.org/html/2605.07725"
          },
          {
            "title": "What Can RL Bring to VLA Generalization? An Empirical Study",
            "url": "https://rlvla.github.io/"
          }
        ]
      },
      "Based on the web search results, I found relevant information about VLA-OPD:\n\n## VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models\n\nVLA-OPD is a framework addressing how pre-trained Vision-Language-Action (VLA) models require post-training to ensure reliable performance during deployment, where standard offline Supervised Fine-Tuning (SFT) suffers from distribution shifts and catastrophic forgetting, while online Reinforcement Learning (RL) struggles with sparse rewards and poor sample efficiency.\n\n### Key Approach\n\nVLA-OPD is a framework bridging the efficiency of SFT with the robustness of RL, leveraging an expert teacher to provide dense, token-level supervision on the student's self-generated trajectories instead of relying on sparse environmental rewards.\n\n### Technical Innovation\n\nThe framework formulates a Reverse-KL distillation objective for VLA models, where its bounded mode-seeking property effectively filters out the teacher's epistemic uncertainty while maintaining action diversity, preventing both the entropy explosion of Forward-KL and the premature entropy collapse of Hard-CE.\n\n### Performance Results\n\nExtensive evaluations across LIBERO and RoboTwin2.0 benchmarks demonstrate that VLA-OPD achieves superior robustness and success rates compared to SFT, while requiring substantially fewer training steps than on-policy RL baselines.\n\nExperiments on LIBERO and RoboTwin2.0 benchmarks demonstrate that VLA-OPD significantly improves sample efficiency over RL and robustness over SFT, while effectively mitigating catastrophic forgetting during post-training.\n\nThe paper was published in March 2026 on arXiv."
    ],
    "durationSeconds": 8.54830754899999
  },
  "sourceToolAssistantUUID": "74cd586f-7807-4cc0-bb05-e7debcc459f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-14T06:00:10.291Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GnpNJe4JKF9VqfMTwmFPFz`</summary>

```json
{
  "query": "Adaptive Q-Chunking AQC offline RL VLA robomimic OGBench 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70c07ce6-ee24-42f5-97e6-2cb0da0d33b7",
  "isSidechain": false,
  "requestId": "req_011Cb1x6gSrHamyrYNu6YzJE",
  "type": "assistant",
  "uuid": "63711351-0eed-4fdd-802d-41930c05fd6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LSq7PZNMYtLoj3jsGx29u2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1029,
      "cache_read_input_tokens": 35123,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1029,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 35123,
          "cache_creation_input_tokens": 1029,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1029
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

_source line 51 · 2026-05-14T06:00:18.748Z_

<details><summary>↩ Tool result · `toolu_01GnpNJe4JKF9VqfMTwmFPFz`</summary>

```text
Web search results for query: "Adaptive Q-Chunking AQC offline RL VLA robomimic OGBench 2025"

Links: [{"title":"Adaptive Q-Chunking for Offline-to-Online Reinforcement Learning","url":"https://arxiv.org/html/2605.05544"},{"title":"[2605.05544] Adaptive Q-Chunking for Offline-to-Online Reinforcement Learning","url":"https://arxiv.org/abs/2605.05544"},{"title":"Reinforcement Learning with Action Chunking","url":"https://arxiv.org/html/2507.07969v1"},{"title":"Q-chunking in Reinforcement Learning","url":"https://www.emergentmind.com/topics/q-chunking"},{"title":"Reinforcement Learning with Action Chunking","url":"https://openreview.net/pdf?id=XUks1Y96NR"},{"title":"Reinforcement Learning with Action Chunking","url":"https://bhakthan.substack.com/p/reinforcement-learning-with-action"},{"title":"GitHub - ColinQiyangLi/qc · GitHub","url":"https://github.com/ColinQiyangLi/qc"},{"title":"GitHub - DongTian95/RLAC: Reinforcement Learning with Action Chunking","url":"https://github.com/DongTian95/RLAC"},{"title":"Preprint. DECOUPLED Q-CHUNKING Qiyang Li UC Berkeley qcli@berkeley.edu","url":"https://arxiv.org/pdf/2512.10926"},{"title":"[2410.20092] OGBench: Benchmarking Offline Goal-Conditioned RL","url":"https://arxiv.org/abs/2410.20092"}]

Based on the search results, here's what I found about Adaptive Q-Chunking and related topics:

## Adaptive Q-Chunking (AQC)

Adaptive Q-Chunking (AQC) resolves failures in naive multi-chunk methods by comparing the advantage of each chunk size relative to a per-horizon baseline, normalized by the discount factor. AQC is an offline-to-online RL method that adapts chunk sizes per state through a principled advantage-based criterion.

The VLA natively outputs action chunks; AQC scores multiple candidate chunks at each scale and selects the best prefix via the per-scale advantage criterion, giving the VLA reactive control near contacts while preserving smooth motion in free space, all without modifying the underlying model.

## Results and Benchmarks

AQC achieves state-of-the-art results on OGBench and Robomimic. The approach enhances the performance of VLA policies on RoboCasa-GR1 tabletop tasks, exceeding prior chunked-critic methods on contact-rich manipulation.

## Theoretical Contributions

AQC provides theoretical analysis establishing advantage separability, value dominance over fixed-chunk policies, and closed-loop optimality bounds.

The search results show that AQC is a recent method (from 2025) designed to improve offline-to-online reinforcement learning for vision-language-action (VLA) models and other RL approaches by intelligently adapting action chunk sizes during execution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63711351-0eed-4fdd-802d-41930c05fd6c",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "8d8aa368-f067-465b-a78a-1d6d847b4efa",
  "toolUseResult": {
    "query": "Adaptive Q-Chunking AQC offline RL VLA robomimic OGBench 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01H6HBboQj8k84C6tHfcgLZW",
        "content": [
          {
            "title": "Adaptive Q-Chunking for Offline-to-Online Reinforcement Learning",
            "url": "https://arxiv.org/html/2605.05544"
          },
          {
            "title": "[2605.05544] Adaptive Q-Chunking for Offline-to-Online Reinforcement Learning",
            "url": "https://arxiv.org/abs/2605.05544"
          },
          {
            "title": "Reinforcement Learning with Action Chunking",
            "url": "https://arxiv.org/html/2507.07969v1"
          },
          {
            "title": "Q-chunking in Reinforcement Learning",
            "url": "https://www.emergentmind.com/topics/q-chunking"
          },
          {
            "title": "Reinforcement Learning with Action Chunking",
            "url": "https://openreview.net/pdf?id=XUks1Y96NR"
          },
          {
            "title": "Reinforcement Learning with Action Chunking",
            "url": "https://bhakthan.substack.com/p/reinforcement-learning-with-action"
          },
          {
            "title": "GitHub - ColinQiyangLi/qc · GitHub",
            "url": "https://github.com/ColinQiyangLi/qc"
          },
          {
            "title": "GitHub - DongTian95/RLAC: Reinforcement Learning with Action Chunking",
            "url": "https://github.com/DongTian95/RLAC"
          },
          {
            "title": "Preprint. DECOUPLED Q-CHUNKING Qiyang Li UC Berkeley qcli@berkeley.edu",
            "url": "https://arxiv.org/pdf/2512.10926"
          },
          {
            "title": "[2410.20092] OGBench: Benchmarking Offline Goal-Conditioned RL",
            "url": "https://arxiv.org/abs/2410.20092"
          }
        ]
      },
      "Based on the search results, here's what I found about Adaptive Q-Chunking and related topics:\n\n## Adaptive Q-Chunking (AQC)\n\nAdaptive Q-Chunking (AQC) resolves failures in naive multi-chunk methods by comparing the advantage of each chunk size relative to a per-horizon baseline, normalized by the discount factor. AQC is an offline-to-online RL method that adapts chunk sizes per state through a principled advantage-based criterion.\n\nThe VLA natively outputs action chunks; AQC scores multiple candidate chunks at each scale and selects the best prefix via the per-scale advantage criterion, giving the VLA reactive control near contacts while preserving smooth motion in free space, all without modifying the underlying model.\n\n## Results and Benchmarks\n\nAQC achieves state-of-the-art results on OGBench and Robomimic. The approach enhances the performance of VLA policies on RoboCasa-GR1 tabletop tasks, exceeding prior chunked-critic methods on contact-rich manipulation.\n\n## Theoretical Contributions\n\nAQC provides theoretical analysis establishing advantage separability, value dominance over fixed-chunk policies, and closed-loop optimality bounds.\n\nThe search results show that AQC is a recent method (from 2025) designed to improve offline-to-online reinforcement learning for vision-language-action (VLA) models and other RL approaches by intelligently adapting action chunk sizes during execution."
    ],
    "durationSeconds": 8.450806874000001
  },
  "sourceToolAssistantUUID": "63711351-0eed-4fdd-802d-41930c05fd6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-14T06:00:25.067Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CajSC2DmvNUcgbyGUbGKWF`</summary>

```json
{
  "query": "\"reward model\" \"demonstration quality\" VLA filtering weighting offline fine-tuning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d8aa368-f067-465b-a78a-1d6d847b4efa",
  "isSidechain": false,
  "requestId": "req_011Cb1x7Yww6ZZjw9pRzexUA",
  "type": "assistant",
  "uuid": "977b1e20-0838-4d7e-b168-bfb94d01fecc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGXfg3YfFKuZh7jS8yNzJ7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 879,
      "cache_read_input_tokens": 36152,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 879,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 36152,
          "cache_creation_input_tokens": 879,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 879
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

_source line 53 · 2026-05-14T06:00:34.559Z_

<details><summary>↩ Tool result · `toolu_01CajSC2DmvNUcgbyGUbGKWF`</summary>

```text
Web search results for query: ""reward model" "demonstration quality" VLA filtering weighting offline fine-tuning 2026"

Links: [{"title":"VLA-RFT: Vision-Language-Action Reinforcement Fine-Tuning with Verified Rewards in World Simulators | OpenReview","url":"https://openreview.net/forum?id=Jaut99EHeu"},{"title":"GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub","url":"https://github.com/PRIME-RL/SimpleVLA-RL"},{"title":"ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy","url":"https://arxiv.org/html/2502.05450v1"},{"title":"CO-RFT: Efficient Fine-Tuning of Vision-Language-Action Models through Chunked Offline Reinforcement Learning","url":"https://arxiv.org/html/2508.02219v1"},{"title":"ConRFT: A Reinforced Fine-tuning Method for VLA Models via...","url":"https://arxiv.org/abs/2502.05450"},{"title":"Yuhui Chen - 陈宇辉","url":"https://cccedric.github.io/"},{"title":"Reinforcement Fine-Tuning of Flow-Matching Policies for Vision-Language-Action Models","url":"https://arxiv.org/html/2510.09976"},{"title":"(PDF) ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy","url":"https://www.researchgate.net/publication/388884199_ConRFT_A_Reinforced_Fine-tuning_Method_for_VLA_Models_via_Consistency_Policy"},{"title":"VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation","url":"https://arxiv.org/html/2603.26666"},{"title":"VLA-OPD: Bridging Offline SFT and Online RL for...","url":"https://arxiv.org/abs/2603.26666"}]

I found several recent papers and resources related to reward models, demonstration quality, VLA (Vision-Language-Action) filtering, weighting, and offline fine-tuning from 2025-2026. Here are the key findings:

## Recent VLA Fine-Tuning Approaches

**Reinforcement Fine-Tuning Methods:**

VLA-RFT introduces a Reinforcement Fine-Tuning framework that leverages a data-driven world model as a controllable simulator, which predicts future visual observations conditioned on actions and allows policy rollouts with dense, trajectory-level rewards derived from goal-achieving references.

ConRFT proposes a reinforced fine-tuning approach for VLA models consisting of offline and online fine-tuning with a unified consistency-based training objective, where the offline stage integrates behavior cloning and Q-learning to effectively extract policy from a small set of demonstrations and stabilize value estimating.

**Offline RL with Demonstration Quality:**

CO-RFT is an algorithm aimed at fine-tuning VLA models using a limited set of demonstrations (30 to 60 samples), implementing offline RL with action chunking to optimize the pretrained policy, achieving a 57% improvement in success rate.

On offline RL tasks, increased guidance weighting leads to increased performance.

**On-Policy Distillation Approach:**

VLA-OPD leverages an expert teacher to provide dense, token-level supervision on the student's self-generated trajectories, with a bounded mode-seeking objective that filters out the teacher's epistemic uncertainty while maintaining action diversity.

SimpleVLA-RL uses binary (0/1) outcome rewards with no complex reward design needed and includes exploration strategies like dynamic sampling, adaptive clipping, and temperature tuning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "977b1e20-0838-4d7e-b168-bfb94d01fecc",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "d606a354-2081-4f43-8870-a83df4202cd9",
  "toolUseResult": {
    "query": "\"reward model\" \"demonstration quality\" VLA filtering weighting offline fine-tuning 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01K4s48gGBan2WHMAT1vma2k",
        "content": [
          {
            "title": "VLA-RFT: Vision-Language-Action Reinforcement Fine-Tuning with Verified Rewards in World Simulators | OpenReview",
            "url": "https://openreview.net/forum?id=Jaut99EHeu"
          },
          {
            "title": "GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub",
            "url": "https://github.com/PRIME-RL/SimpleVLA-RL"
          },
          {
            "title": "ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy",
            "url": "https://arxiv.org/html/2502.05450v1"
          },
          {
            "title": "CO-RFT: Efficient Fine-Tuning of Vision-Language-Action Models through Chunked Offline Reinforcement Learning",
            "url": "https://arxiv.org/html/2508.02219v1"
          },
          {
            "title": "ConRFT: A Reinforced Fine-tuning Method for VLA Models via...",
            "url": "https://arxiv.org/abs/2502.05450"
          },
          {
            "title": "Yuhui Chen - 陈宇辉",
            "url": "https://cccedric.github.io/"
          },
          {
            "title": "Reinforcement Fine-Tuning of Flow-Matching Policies for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.09976"
          },
          {
            "title": "(PDF) ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy",
            "url": "https://www.researchgate.net/publication/388884199_ConRFT_A_Reinforced_Fine-tuning_Method_for_VLA_Models_via_Consistency_Policy"
          },
          {
            "title": "VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation",
            "url": "https://arxiv.org/html/2603.26666"
          },
          {
            "title": "VLA-OPD: Bridging Offline SFT and Online RL for...",
            "url": "https://arxiv.org/abs/2603.26666"
          }
        ]
      },
      "I found several recent papers and resources related to reward models, demonstration quality, VLA (Vision-Language-Action) filtering, weighting, and offline fine-tuning from 2025-2026. Here are the key findings:\n\n## Recent VLA Fine-Tuning Approaches\n\n**Reinforcement Fine-Tuning Methods:**\n\nVLA-RFT introduces a Reinforcement Fine-Tuning framework that leverages a data-driven world model as a controllable simulator, which predicts future visual observations conditioned on actions and allows policy rollouts with dense, trajectory-level rewards derived from goal-achieving references.\n\nConRFT proposes a reinforced fine-tuning approach for VLA models consisting of offline and online fine-tuning with a unified consistency-based training objective, where the offline stage integrates behavior cloning and Q-learning to effectively extract policy from a small set of demonstrations and stabilize value estimating.\n\n**Offline RL with Demonstration Quality:**\n\nCO-RFT is an algorithm aimed at fine-tuning VLA models using a limited set of demonstrations (30 to 60 samples), implementing offline RL with action chunking to optimize the pretrained policy, achieving a 57% improvement in success rate.\n\nOn offline RL tasks, increased guidance weighting leads to increased performance.\n\n**On-Policy Distillation Approach:**\n\nVLA-OPD leverages an expert teacher to provide dense, token-level supervision on the student's self-generated trajectories, with a bounded mode-seeking objective that filters out the teacher's epistemic uncertainty while maintaining action diversity.\n\nSimpleVLA-RL uses binary (0/1) outcome rewards with no complex reward design needed and includes exploration strategies like dynamic sampling, adaptive clipping, and temperature tuning."
    ],
    "durationSeconds": 9.486052384999988
  },
  "sourceToolAssistantUUID": "977b1e20-0838-4d7e-b168-bfb94d01fecc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 54 · 2026-05-14T06:00:34.563Z_

```json
{
  "parentUuid": "d606a354-2081-4f43-8870-a83df4202cd9",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3eea2d01-2966-4740-936a-16eae9de7031",
  "timestamp": "2026-05-14T06:00:34.563Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Offline Advantage Conditioning for VLA Noise Decomposition\",   \"core_p…",
  "leafUuid": "3eea2d01-2966-4740-936a-16eae9de7031",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Offline VLA fine-tuning via trajectory-level return ranking and conservative advantage weighting",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80"
}
```

---

### Tool call

_source line 57 · 2026-05-14T06:00:37.861Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PR1zxeV6EocvPbYGGnca6F`</summary>

```json
{
  "query": "SmolVLA small vision language action model 2025 2026 efficient"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3eea2d01-2966-4740-936a-16eae9de7031",
  "isSidechain": false,
  "requestId": "req_011Cb1x8ibtVotMGTJprj1eb",
  "type": "assistant",
  "uuid": "c30c9709-723a-4951-a0e9-5aa83918a842",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011z5ByHv37gknnStwSDeEUo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1149,
      "cache_read_input_tokens": 37031,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1149,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 37031,
          "cache_creation_input_tokens": 1149,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1149
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

_source line 58 · 2026-05-14T06:00:47.369Z_

<details><summary>↩ Tool result · `toolu_01PR1zxeV6EocvPbYGGnca6F`</summary>

```text
Web search results for query: "SmolVLA small vision language action model 2025 2026 efficient"

Links: [{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844"},{"title":"arXiv:2506.01844v1 [cs.LG] 2 Jun 2025 SmolVLA: A vision-language-action model","url":"https://arxiv.org/pdf/2506.01844"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"[PDF] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SmolVLA:-A-Vision-Language-Action-Model-for-and-Shukor-Aubakirova/6ab4d113676d00e74b55e918fee4c7affaa8652f"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"Hugging Face Releases SmolVLA: A Compact Vision-Language-Action Model for Affordable and Efficient Robotics - MarkTechPost","url":"https://www.marktechpost.com/2025/06/03/hugging-face-releases-smolvla-a-compact-vision-language-action-model-for-affordable-and-efficient-robotics/"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250601844S/abstract"},{"title":"Paper page - SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://huggingface.co/papers/2506.01844"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/smolvla-vision-language-action-model-affordable-efficient"}]

Here are the search results for SmolVLA:

## Overview

SmolVLA is a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance. SmolVLA is an open-source compact VLA with 450 million parameters released by Hugging Face.

## Key Features

**Size and Efficiency:**
- SmolVLA is designed to be trained on a single GPU and deployed on consumer-grade GPUs or even CPUs.
- Despite its compact size, SmolVLA achieves performance comparable to VLAs that are 10x larger.
- Despite using fewer than 30k training episodes—an order of magnitude less than other VLAs—SmolVLA matches or exceeds the performance of much larger models, both in simulation and the real world.

**Architecture:**
- SmolVLA is composed of two main components: (i) a pretrained VLM tasked with perception and (ii) an action expert, trained to act.
- SmolVLA uses SmolVLM2 as its VLM backbone, optimized for multi-image inputs and consisting of a SigLIP vision encoder and a SmolLM2 language decoder.

**Asynchronous Inference:**
- An asynchronous inference stack decouples perception and action prediction from action execution, allowing higher control rates with chunked action generation.
- Asynchronous inference enables 30% faster response and 2× task throughput.

**Training Data:**
- SmolVLA was trained entirely on LeRobot, an open-source dataset collected and curated by the community.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c30c9709-723a-4951-a0e9-5aa83918a842",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "66555e65-3016-4c52-ae30-03e9113d14ee",
  "toolUseResult": {
    "query": "SmolVLA small vision language action model 2025 2026 efficient",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AQ7tDjaZoGZh3Tp5EH2B85",
        "content": [
          {
            "title": "[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics",
            "url": "https://arxiv.org/abs/2506.01844"
          },
          {
            "title": "arXiv:2506.01844v1 [cs.LG] 2 Jun 2025 SmolVLA: A vision-language-action model",
            "url": "https://arxiv.org/pdf/2506.01844"
          },
          {
            "title": "Vision-language-action model - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Vision-language-action_model"
          },
          {
            "title": "SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data",
            "url": "https://huggingface.co/blog/smolvla"
          },
          {
            "title": "[PDF] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/SmolVLA:-A-Vision-Language-Action-Model-for-and-Shukor-Aubakirova/6ab4d113676d00e74b55e918fee4c7affaa8652f"
          },
          {
            "title": "SmolVLA: A vision-language-action model for affordable and efficient robotics",
            "url": "https://arxiv.org/html/2506.01844v1"
          },
          {
            "title": "Hugging Face Releases SmolVLA: A Compact Vision-Language-Action Model for Affordable and Efficient Robotics - MarkTechPost",
            "url": "https://www.marktechpost.com/2025/06/03/hugging-face-releases-smolvla-a-compact-vision-language-action-model-for-affordable-and-efficient-robotics/"
          },
          {
            "title": "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250601844S/abstract"
          },
          {
            "title": "Paper page - SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics",
            "url": "https://huggingface.co/papers/2506.01844"
          },
          {
            "title": "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/smolvla-vision-language-action-model-affordable-efficient"
          }
        ]
      },
      "Here are the search results for SmolVLA:\n\n## Overview\n\nSmolVLA is a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance. SmolVLA is an open-source compact VLA with 450 million parameters released by Hugging Face.\n\n## Key Features\n\n**Size and Efficiency:**\n- SmolVLA is designed to be trained on a single GPU and deployed on consumer-grade GPUs or even CPUs.\n- Despite its compact size, SmolVLA achieves performance comparable to VLAs that are 10x larger.\n- Despite using fewer than 30k training episodes—an order of magnitude less than other VLAs—SmolVLA matches or exceeds the performance of much larger models, both in simulation and the real world.\n\n**Architecture:**\n- SmolVLA is composed of two main components: (i) a pretrained VLM tasked with perception and (ii) an action expert, trained to act.\n- SmolVLA uses SmolVLM2 as its VLM backbone, optimized for multi-image inputs and consisting of a SigLIP vision encoder and a SmolLM2 language decoder.\n\n**Asynchronous Inference:**\n- An asynchronous inference stack decouples perception and action prediction from action execution, allowing higher control rates with chunked action generation.\n- Asynchronous inference enables 30% faster response and 2× task throughput.\n\n**Training Data:**\n- SmolVLA was trained entirely on LeRobot, an open-source dataset collected and curated by the community."
    ],
    "durationSeconds": 9.502811616999999
  },
  "sourceToolAssistantUUID": "c30c9709-723a-4951-a0e9-5aa83918a842",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-14T06:00:50.118Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SUcCQpyo4mp6N4FRy2eBBr`</summary>

```json
{
  "query": "ARFM advantage-weighted offline RL VLA flow model AAAI 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66555e65-3016-4c52-ae30-03e9113d14ee",
  "isSidechain": false,
  "requestId": "req_011Cb1x9fGz8wUC4igQ6zMkG",
  "type": "assistant",
  "uuid": "1d62c60f-af9e-4e39-ac2e-83a0f11462cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013SLWQVKt9NEjRiHd9Kms1q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1083,
      "cache_read_input_tokens": 38180,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1083,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 38180,
          "cache_creation_input_tokens": 1083,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1083
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

_source line 60 · 2026-05-14T06:00:56.685Z_

<details><summary>↩ Tool result · `toolu_01SUcCQpyo4mp6N4FRy2eBBr`</summary>

```text
Web search results for query: "ARFM advantage-weighted offline RL VLA flow model AAAI 2026"

Links: [{"title":"Balancing Signal and Variance: Adaptive Offline RL Post-Training for VLA Flow Models","url":"https://arxiv.org/html/2509.04063"},{"title":"[2509.04063] Balancing Signal and Variance: Adaptive Offline RL Post-Training for VLA Flow Models","url":"https://arxiv.org/abs/2509.04063"},{"title":"Adaptive Q-Chunking for Offline-to-Online Reinforcement Learning","url":"https://arxiv.org/html/2605.05544"},{"title":"A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2510.24795v1"},{"title":"VLA-RFT: Vision-language-action Reinforcement fine-tuning with verified rewards in world simulators","url":"https://arxiv.org/html/2510.00406v1"},{"title":"1 Introduction","url":"https://arxiv.org/html/2511.01331v1"},{"title":"VLA-OPD: Bridging Offline SFT and Online RL for...","url":"https://arxiv.org/abs/2603.26666"},{"title":"Behavior Regularization with Flow Latent Policy for Offline Reinforcement Learning | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/39916"},{"title":"Adaptive Offline RL Post-Training for VLA Flow Models","url":"https://ojs.aaai.org/index.php/AAAI/article/download/38944/42906"},{"title":"VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation","url":"https://arxiv.org/html/2603.26666v1"}]

Based on the search results, I found relevant information about ARFM:

ARFM (Adaptive Reinforced Flow Matching) is a novel adaptive offline RL fine-tuning method for VLA flow models. The method theoretically constructs an energy-weighted flow matching loss with adaptive scaling factor, aiming to balance the RL signal and gradient variance on the data samples, and controls the strength of the RL signal introduced into the sample data by introducing an adaptively adjusted scaling factor in the VLA flow loss function.

The approach aims to dynamically select the scaling factor to preserve the RL signal, meaning samples with higher RL advantage are still amplified in the data distribution during flow model fine-tuning. The method theoretically establishes the optimization objective of adaptively adjusting the scaling factor and induces a bisection iterative algorithm to update the factor in real time, thereby achieving efficient VLA flow model fine-tuning.

Extensive experiments in simulation and real-world robot manipulation tasks show that ARFM exhibits state-of-the-art generalization ability, robustness to dynamic perturbations, and excellent performance in few-shot and continuous learning scenarios.

The paper appears to have been published at AAAI 2026, as evidenced by the official AAAI proceedings link in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d62c60f-af9e-4e39-ac2e-83a0f11462cd",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "442d2891-378e-4409-89b8-2cec1c3f725b",
  "toolUseResult": {
    "query": "ARFM advantage-weighted offline RL VLA flow model AAAI 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EEXpkunFD8JiXYYUEHVbVU",
        "content": [
          {
            "title": "Balancing Signal and Variance: Adaptive Offline RL Post-Training for VLA Flow Models",
            "url": "https://arxiv.org/html/2509.04063"
          },
          {
            "title": "[2509.04063] Balancing Signal and Variance: Adaptive Offline RL Post-Training for VLA Flow Models",
            "url": "https://arxiv.org/abs/2509.04063"
          },
          {
            "title": "Adaptive Q-Chunking for Offline-to-Online Reinforcement Learning",
            "url": "https://arxiv.org/html/2605.05544"
          },
          {
            "title": "A Survey on Efficient Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.24795v1"
          },
          {
            "title": "VLA-RFT: Vision-language-action Reinforcement fine-tuning with verified rewards in world simulators",
            "url": "https://arxiv.org/html/2510.00406v1"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2511.01331v1"
          },
          {
            "title": "VLA-OPD: Bridging Offline SFT and Online RL for...",
            "url": "https://arxiv.org/abs/2603.26666"
          },
          {
            "title": "Behavior Regularization with Flow Latent Policy for Offline Reinforcement Learning | Proceedings of the AAAI Conference on Artificial Intelligence",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/39916"
          },
          {
            "title": "Adaptive Offline RL Post-Training for VLA Flow Models",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/download/38944/42906"
          },
          {
            "title": "VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation",
            "url": "https://arxiv.org/html/2603.26666v1"
          }
        ]
      },
      "Based on the search results, I found relevant information about ARFM:\n\nARFM (Adaptive Reinforced Flow Matching) is a novel adaptive offline RL fine-tuning method for VLA flow models. The method theoretically constructs an energy-weighted flow matching loss with adaptive scaling factor, aiming to balance the RL signal and gradient variance on the data samples, and controls the strength of the RL signal introduced into the sample data by introducing an adaptively adjusted scaling factor in the VLA flow loss function.\n\nThe approach aims to dynamically select the scaling factor to preserve the RL signal, meaning samples with higher RL advantage are still amplified in the data distribution during flow model fine-tuning. The method theoretically establishes the optimization objective of adaptively adjusting the scaling factor and induces a bisection iterative algorithm to update the factor in real time, thereby achieving efficient VLA flow model fine-tuning.\n\nExtensive experiments in simulation and real-world robot manipulation tasks show that ARFM exhibits state-of-the-art generalization ability, robustness to dynamic perturbations, and excellent performance in few-shot and continuous learning scenarios.\n\nThe paper appears to have been published at AAAI 2026, as evidenced by the official AAAI proceedings link in the search results."
    ],
    "durationSeconds": 6.562252721999975
  },
  "sourceToolAssistantUUID": "1d62c60f-af9e-4e39-ac2e-83a0f11462cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-14T06:00:59.238Z_

Now let me search for the most recent work on this specific topic to ensure I'm not missing any concurrent work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "442d2891-378e-4409-89b8-2cec1c3f725b",
  "isSidechain": false,
  "requestId": "req_011Cb1xAM785bNV5gokiDSeD",
  "type": "assistant",
  "uuid": "d182bd3d-b896-4d5c-8a9b-f6ee51273d92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pMsfrYCTYgiqHRY2Vs4iJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 881,
      "cache_read_input_tokens": 39263,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 881,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 94,
          "cache_read_input_tokens": 39263,
          "cache_creation_input_tokens": 881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 881
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

_source line 62 · 2026-05-14T06:01:00.013Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015hSftyaiDUdw5T6Hv64k3s`</summary>

```json
{
  "query": "offline demonstration quality scoring VLA reward-weighted fine-tuning noisy demonstrations 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d182bd3d-b896-4d5c-8a9b-f6ee51273d92",
  "isSidechain": false,
  "requestId": "req_011Cb1xAM785bNV5gokiDSeD",
  "type": "assistant",
  "uuid": "45dfd023-293e-45d4-9832-4cf33eaaa46c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pMsfrYCTYgiqHRY2Vs4iJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 881,
      "cache_read_input_tokens": 39263,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 881,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 94,
          "cache_read_input_tokens": 39263,
          "cache_creation_input_tokens": 881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 881
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

_source line 63 · 2026-05-14T06:01:10.503Z_

<details><summary>↩ Tool result · `toolu_015hSftyaiDUdw5T6Hv64k3s`</summary>

```text
Web search results for query: "offline demonstration quality scoring VLA reward-weighted fine-tuning noisy demonstrations 2026"

Links: [{"title":"VLA-RFT: Vision-Language-Action Reinforcement Fine-Tuning with Verified Rewards in World Simulators | OpenReview","url":"https://openreview.net/forum?id=Jaut99EHeu"},{"title":"EVOLVE-VLA: Test-Time Training from Environment","url":"https://arxiv.org/pdf/2512.14666"},{"title":"EVOLVE-VLA: Test-Time Training from Environment Feedback for Vision-Language-Action Models","url":"https://arxiv.org/html/2512.14666"},{"title":"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion","url":"https://arxiv.org/html/2511.14178"},{"title":"CO-RFT: Efficient Fine-Tuning of Vision-Language-Action Models through Chunked Offline Reinforcement Learning","url":"https://arxiv.org/html/2508.02219v1"},{"title":"CO-RFT: Efficient Fine-Tuning of Vision-Language-Action Models through","url":"https://arxiv.org/pdf/2508.02219"},{"title":"ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy","url":"https://arxiv.org/html/2502.05450v1"},{"title":"VLA-RFT: Vision-language-action Reinforcement fine-tuning with verified rewards in world simulators","url":"https://arxiv.org/html/2510.00406v1"},{"title":"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | OpenReview","url":"https://openreview.net/forum?id=eUGoqrZ6Ea"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v2"}]

I found several relevant research papers related to your search query. Here are the key results:

## Recent VLA Fine-Tuning Research (2025-2026)

### 1. **VLA-RFT: Vision-Language-Action Reinforcement Fine-Tuning**
VLA-RFT is a Reinforcement Fine-Tuning framework that leverages a data-driven world model as a controllable simulator, trained from real interaction data, which predicts future visual observations conditioned on actions, allowing policy rollouts with dense, trajectory-level rewards derived from goal-achieving references. With fewer than 400 fine-tuning steps, VLA-RFT surpasses strong supervised baselines and achieves greater efficiency than simulator-based RL.

### 2. **EVOLVE-VLA: Test-Time Training with Noisy Demonstrations**
The framework addresses handling noisy signals through an accumulative progress estimation mechanism smoothing noisy point-wise estimates, and a progressive horizon extension strategy enabling gradual policy evolution. EVOLVE-VLA achieves substantial gains: +8.6% on long-horizon tasks, +22.0% in 1-shot learning, and cross-task transfer.

### 3. **CO-RFT: Offline Reinforcement Learning for VLA Models**
CO-RFT is an algorithm aimed at fine-tuning VLA models using a limited set of demonstrations (30 to 60 samples). Empirical results in real-world environments demonstrate that CO-RFT outperforms previous supervised methods, achieving a 57% improvement in success rate and a 22.3% reduction in cycle time.

### 4. **ConRFT: Reinforced Fine-tuning with Consistency Policy**
ConRFT consists of offline and online fine-tuning with a unified consistency-based training objective, where the offline stage integrates behavior cloning and Q-learning to effectively extract policy from a small set of demonstrations and stabilize value estimating.

All of these papers address the key challenges of handling noisy demonstrations and improving VLA model performance through reward-weighted and offline reinforcement learning approaches in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45dfd023-293e-45d4-9832-4cf33eaaa46c",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "ff22b8be-de06-40e4-b8b6-2e068a0756d2",
  "toolUseResult": {
    "query": "offline demonstration quality scoring VLA reward-weighted fine-tuning noisy demonstrations 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PGDYLwae5dFtoLpQQpMkrt",
        "content": [
          {
            "title": "VLA-RFT: Vision-Language-Action Reinforcement Fine-Tuning with Verified Rewards in World Simulators | OpenReview",
            "url": "https://openreview.net/forum?id=Jaut99EHeu"
          },
          {
            "title": "EVOLVE-VLA: Test-Time Training from Environment",
            "url": "https://arxiv.org/pdf/2512.14666"
          },
          {
            "title": "EVOLVE-VLA: Test-Time Training from Environment Feedback for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2512.14666"
          },
          {
            "title": "Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion",
            "url": "https://arxiv.org/html/2511.14178"
          },
          {
            "title": "CO-RFT: Efficient Fine-Tuning of Vision-Language-Action Models through Chunked Offline Reinforcement Learning",
            "url": "https://arxiv.org/html/2508.02219v1"
          },
          {
            "title": "CO-RFT: Efficient Fine-Tuning of Vision-Language-Action Models through",
            "url": "https://arxiv.org/pdf/2508.02219"
          },
          {
            "title": "ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy",
            "url": "https://arxiv.org/html/2502.05450v1"
          },
          {
            "title": "VLA-RFT: Vision-language-action Reinforcement fine-tuning with verified rewards in world simulators",
            "url": "https://arxiv.org/html/2510.00406v1"
          },
          {
            "title": "Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | OpenReview",
            "url": "https://openreview.net/forum?id=eUGoqrZ6Ea"
          },
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/html/2502.19645v2"
          }
        ]
      },
      "I found several relevant research papers related to your search query. Here are the key results:\n\n## Recent VLA Fine-Tuning Research (2025-2026)\n\n### 1. **VLA-RFT: Vision-Language-Action Reinforcement Fine-Tuning**\nVLA-RFT is a Reinforcement Fine-Tuning framework that leverages a data-driven world model as a controllable simulator, trained from real interaction data, which predicts future visual observations conditioned on actions, allowing policy rollouts with dense, trajectory-level rewards derived from goal-achieving references. With fewer than 400 fine-tuning steps, VLA-RFT surpasses strong supervised baselines and achieves greater efficiency than simulator-based RL.\n\n### 2. **EVOLVE-VLA: Test-Time Training with Noisy Demonstrations**\nThe framework addresses handling noisy signals through an accumulative progress estimation mechanism smoothing noisy point-wise estimates, and a progressive horizon extension strategy enabling gradual policy evolution. EVOLVE-VLA achieves substantial gains: +8.6% on long-horizon tasks, +22.0% in 1-shot learning, and cross-task transfer.\n\n### 3. **CO-RFT: Offline Reinforcement Learning for VLA Models**\nCO-RFT is an algorithm aimed at fine-tuning VLA models using a limited set of demonstrations (30 to 60 samples). Empirical results in real-world environments demonstrate that CO-RFT outperforms previous supervised methods, achieving a 57% improvement in success rate and a 22.3% reduction in cycle time.\n\n### 4. **ConRFT: Reinforced Fine-tuning with Consistency Policy**\nConRFT consists of offline and online fine-tuning with a unified consistency-based training objective, where the offline stage integrates behavior cloning and Q-learning to effectively extract policy from a small set of demonstrations and stabilize value estimating.\n\nAll of these papers address the key challenges of handling noisy demonstrations and improving VLA model performance through reward-weighted and offline reinforcement learning approaches in 2025-2026."
    ],
    "durationSeconds": 10.484708829999988
  },
  "sourceToolAssistantUUID": "45dfd023-293e-45d4-9832-4cf33eaaa46c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-14T06:01:13.990Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K9RZUFAuhuxZxS5BaC7ycd`</summary>

```json
{
  "query": "VLM-based reward model progress estimation robotics offline zero-shot GVL 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff22b8be-de06-40e4-b8b6-2e068a0756d2",
  "isSidechain": false,
  "requestId": "req_011Cb1xBNA9caXAHKuTGHXXa",
  "type": "assistant",
  "uuid": "476bdb66-568c-4902-8422-2f30091a6ca6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmJV9hFrEnMYYkLbnCecMz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 40144,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1119,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 40144,
          "cache_creation_input_tokens": 1119,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1119
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

_source line 65 · 2026-05-14T06:01:22.819Z_

<details><summary>↩ Tool result · `toolu_01K9RZUFAuhuxZxS5BaC7ycd`</summary>

```text
Web search results for query: "VLM-based reward model progress estimation robotics offline zero-shot GVL 2025 2026"

Links: [{"title":"TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics","url":"https://arxiv.org/html/2602.19313v1"},{"title":"Large Reward Models: Generalizable Online Robot Reward Generation with Vision-Language Models","url":"https://arxiv.org/html/2603.16065"},{"title":"[2603.16065] Large Reward Models: Generalizable Online Robot Reward Generation with Vision-Language Models","url":"https://arxiv.org/abs/2603.16065"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)","url":"https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"},{"title":"Towards zero-shot robot tool manipulation in industrial context: A modular VLM framework enhanced by multimodal affordance representation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0736584525002157"},{"title":"Vision-Language Models are Zero-Shot Reward Models for Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=N0I2RtD8je"},{"title":"[2410.24164] $π_0$: A Vision-Language-Action Flow Model for General Robot Control","url":"https://arxiv.org/abs/2410.24164"},{"title":"GitHub - zli12321/Vision-Language-Models-Overview: A most Frontend Collection and survey of vision-language model papers, and models GitHub repository. Continuous updates. · GitHub","url":"https://github.com/zli12321/Vision-Language-Models-Overview"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"}]

Based on the web search results, here's what I found regarding VLM-based reward models, progress estimation, and robotics in the 2025-2026 timeframe:

## Key Research Areas

**Progress Estimation with VLMs:**
Recent literature has converged on progress estimation as a primary proxy for state-value estimations, functioning as a temporal value function that monotonically increases as a task nears completion, aligning with principles of Universal Value Learning. The state-of-the-art training-free method, GVL, casts progress estimation as visual question-answering but performs well only on proprietary VLMs like Gemini and GPT-4, collapsing on open-source alternatives.

**TOPReward Approach:**
TOPReward evaluates on three video-language models: Qwen3-VL-8B, Molmo2, and Gemini-2.5-Pro. This work addresses the gap where open-source VLMs are not yet "robotics-ready" for progress estimation.

**Zero-Shot Reward Models:**
A framework for online policy refinement adapts foundation VLMs into online reward generators, developing a robust, scalable reward model trained on a large-scale, multi-source dataset encompassing real-world robot trajectories, human-object interactions, and diverse simulated environments. This reward model operates in a purely zero-shot manner within test environments.

**Generalist Reward Models:**
Generalist reward models such as RoboReward and RoboDopamine are trained on large-scale datasets of successes and failures to predict progress scores or distance-to-goal estimates.

The field is actively developing VLM-based approaches to overcome the challenge of designing generalizable reward functions for robotic learning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "476bdb66-568c-4902-8422-2f30091a6ca6",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "c6517755-c885-4e94-a91d-69e60b14f759",
  "toolUseResult": {
    "query": "VLM-based reward model progress estimation robotics offline zero-shot GVL 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01H9pk7Xd7Pd1f5mJs6zqRR7",
        "content": [
          {
            "title": "TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics",
            "url": "https://arxiv.org/html/2602.19313v1"
          },
          {
            "title": "Large Reward Models: Generalizable Online Robot Reward Generation with Vision-Language Models",
            "url": "https://arxiv.org/html/2603.16065"
          },
          {
            "title": "[2603.16065] Large Reward Models: Generalizable Online Robot Reward Generation with Vision-Language Models",
            "url": "https://arxiv.org/abs/2603.16065"
          },
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          },
          {
            "title": "Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)",
            "url": "https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"
          },
          {
            "title": "Towards zero-shot robot tool manipulation in industrial context: A modular VLM framework enhanced by multimodal affordance representation - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S0736584525002157"
          },
          {
            "title": "Vision-Language Models are Zero-Shot Reward Models for Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=N0I2RtD8je"
          },
          {
            "title": "[2410.24164] $π_0$: A Vision-Language-Action Flow Model for General Robot Control",
            "url": "https://arxiv.org/abs/2410.24164"
          },
          {
            "title": "GitHub - zli12321/Vision-Language-Models-Overview: A most Frontend Collection and survey of vision-language model papers, and models GitHub repository. Continuous updates. · GitHub",
            "url": "https://github.com/zli12321/Vision-Language-Models-Overview"
          },
          {
            "title": "World Action Models are Zero-shot Policies",
            "url": "https://arxiv.org/html/2602.15922v1"
          }
        ]
      },
      "Based on the web search results, here's what I found regarding VLM-based reward models, progress estimation, and robotics in the 2025-2026 timeframe:\n\n## Key Research Areas\n\n**Progress Estimation with VLMs:**\nRecent literature has converged on progress estimation as a primary proxy for state-value estimations, functioning as a temporal value function that monotonically increases as a task nears completion, aligning with principles of Universal Value Learning. The state-of-the-art training-free method, GVL, casts progress estimation as visual question-answering but performs well only on proprietary VLMs like Gemini and GPT-4, collapsing on open-source alternatives.\n\n**TOPReward Approach:**\nTOPReward evaluates on three video-language models: Qwen3-VL-8B, Molmo2, and Gemini-2.5-Pro. This work addresses the gap where open-source VLMs are not yet \"robotics-ready\" for progress estimation.\n\n**Zero-Shot Reward Models:**\nA framework for online policy refinement adapts foundation VLMs into online reward generators, developing a robust, scalable reward model trained on a large-scale, multi-source dataset encompassing real-world robot trajectories, human-object interactions, and diverse simulated environments. This reward model operates in a purely zero-shot manner within test environments.\n\n**Generalist Reward Models:**\nGeneralist reward models such as RoboReward and RoboDopamine are trained on large-scale datasets of successes and failures to predict progress scores or distance-to-goal estimates.\n\nThe field is actively developing VLM-based approaches to overcome the challenge of designing generalizable reward functions for robotic learning tasks."
    ],
    "durationSeconds": 8.820745195999974
  },
  "sourceToolAssistantUUID": "476bdb66-568c-4902-8422-2f30091a6ca6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 66_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Offline Advantage Conditioning for VLA Noise Decomposition\",   \"core_p…",
  "leafUuid": "c6517755-c885-4e94-a91d-69e60b14f759",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80"
}
```

---

### Runtime record

_source line 67_

```json
{
  "type": "ai-title",
  "aiTitle": "Offline VLA fine-tuning via trajectory-level return ranking and conservative advantage weighting",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80"
}
```

---

### Tool call

_source line 68 · 2026-05-14T06:01:26.296Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GdEBAvKxWRvRqbm7z76auK`</summary>

```json
{
  "query": "LIBERO benchmark SOTA success rate 2025 2026 VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6517755-c885-4e94-a91d-69e60b14f759",
  "isSidechain": false,
  "requestId": "req_011Cb1xCGphxLEGU2VmM5Za7",
  "type": "assistant",
  "uuid": "4412897d-7b62-47e3-b331-0d7d30863939",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ZT8tQSiA2qkTFdML6QJT9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1086,
      "cache_read_input_tokens": 41263,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1086,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 41263,
          "cache_creation_input_tokens": 1086,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1086
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

_source line 69 · 2026-05-14T06:01:35.115Z_

<details><summary>↩ Tool result · `toolu_01GdEBAvKxWRvRqbm7z76auK`</summary>

```text
Web search results for query: "LIBERO benchmark SOTA success rate 2025 2026 VLA"

Links: [{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"VLA SOTA Leaderboard","url":"https://sota.evomind-tech.com/"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"VLA & Dexterous Manipulation SOTA Leaderboard","url":"https://github.com/MINT-SJTU/Evo-SOTA.io/blob/main/README.md"}]

Based on the search results, here's what I found about LIBERO benchmark SOTA success rates for VLA models in 2025-2026:

## Current SOTA Success Rates

OpenVLA-OFT achieves SOTA results in LIBERO with a 97.1% average success rate across 4 task suites, outperforming π0, MDT, Seer, DiT Policy, Octo, and Diffusion Policy. This represents the leading performance as of February 2025.

## Important Caveats About These Numbers

However, these headline success rates come with significant caveats. Reported SOTA figures (>95% success) reflect performance under clean, nearly identically distributed train/test splits, whereas systematic robustness analyses reveal significant brittleness and a tendency toward memorization.

## Robustness Limitations

Recent analysis from October 2025 through LIBERO-Plus reveals critical weaknesses: models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

Additionally, current VLA models remain brittle, showing particular vulnerability to camera and robot state changes, largely ignore language instructions, and exhibit positional bias rather than genuine semantic understanding.

## New Robustness Benchmarks

Ongoing work focuses on procedural growth, annotation extensibility, structured perception, RL integration, and, most critically, fair evaluation under meaningful semantic, perceptual, and compositional generalization regimes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4412897d-7b62-47e3-b331-0d7d30863939",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "5739564d-20de-4958-ab9e-8e8fb0c6f0ab",
  "toolUseResult": {
    "query": "LIBERO benchmark SOTA success rate 2025 2026 VLA",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AoBAPhMZNWWwPzWkePUcnJ",
        "content": [
          {
            "title": "LIBERO Benchmark: Vision-Language-Action in Robotics",
            "url": "https://www.emergentmind.com/topics/libero"
          },
          {
            "title": "GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub",
            "url": "https://github.com/sylvestf/LIBERO-plus"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://openvla-oft.github.io/"
          },
          {
            "title": "OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-",
            "url": "https://arxiv.org/pdf/2510.13626"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://sylvestf.github.io/LIBERO-plus/"
          },
          {
            "title": "VLA SOTA Leaderboard",
            "url": "https://sota.evomind-tech.com/"
          },
          {
            "title": "Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2510.13626"
          },
          {
            "title": "[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.13626"
          },
          {
            "title": "VLA & Dexterous Manipulation SOTA Leaderboard",
            "url": "https://github.com/MINT-SJTU/Evo-SOTA.io/blob/main/README.md"
          }
        ]
      },
      "Based on the search results, here's what I found about LIBERO benchmark SOTA success rates for VLA models in 2025-2026:\n\n## Current SOTA Success Rates\n\nOpenVLA-OFT achieves SOTA results in LIBERO with a 97.1% average success rate across 4 task suites, outperforming π0, MDT, Seer, DiT Policy, Octo, and Diffusion Policy. This represents the leading performance as of February 2025.\n\n## Important Caveats About These Numbers\n\nHowever, these headline success rates come with significant caveats. Reported SOTA figures (>95% success) reflect performance under clean, nearly identically distributed train/test splits, whereas systematic robustness analyses reveal significant brittleness and a tendency toward memorization.\n\n## Robustness Limitations\n\nRecent analysis from October 2025 through LIBERO-Plus reveals critical weaknesses: models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.\n\nAdditionally, current VLA models remain brittle, showing particular vulnerability to camera and robot state changes, largely ignore language instructions, and exhibit positional bias rather than genuine semantic understanding.\n\n## New Robustness Benchmarks\n\nOngoing work focuses on procedural growth, annotation extensibility, structured perception, RL integration, and, most critically, fair evaluation under meaningful semantic, perceptual, and compositional generalization regimes."
    ],
    "durationSeconds": 8.812710322999978
  },
  "sourceToolAssistantUUID": "4412897d-7b62-47e3-b331-0d7d30863939",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-14T06:01:38.146Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C3WtRjwvdesiZXnShhSci3`</summary>

```json
{
  "query": "LIBERO-Plus LIBERO-PRO robustness evaluation VLA noise injection protocol 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5739564d-20de-4958-ab9e-8e8fb0c6f0ab",
  "isSidechain": false,
  "requestId": "req_011Cb1xDBQJftPwKkNoZ99tV",
  "type": "assistant",
  "uuid": "312a5652-390d-4bb6-89b3-fa7528329192",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K1hitU4D43UN8FhpLmGJtq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 916,
      "cache_read_input_tokens": 42349,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 916,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 42349,
          "cache_creation_input_tokens": 916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 916
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

_source line 71 · 2026-05-14T06:01:45.320Z_

<details><summary>↩ Tool result · `toolu_01C3WtRjwvdesiZXnShhSci3`</summary>

```text
Web search results for query: "LIBERO-Plus LIBERO-PRO robustness evaluation VLA noise injection protocol 2025"

Links: [{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"How brittle are the VLA models in robotics | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/how-brittle-are-the-vla-models-in-robotics-66ab85286ecf"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2026/poster/38735"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"}]

Based on the web search results, here's what I found about LIBERO-Plus, LIBERO-PRO, robustness evaluation, and VLA noise injection protocols:

## LIBERO-Plus: In-depth Robustness Analysis

LIBERO-Plus is a comprehensive, automatic, and fine-grained evaluation framework with controlled perturbations across seven dimensions: object layouts, camera viewpoints, robot initial states, language instructions, lighting conditions, background textures, and sensor noise.

### Key Findings

Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations. Surprisingly, models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.

### Benchmark Structure

LIBERO-plus offers three key advancements: (1) Comprehensive: Evaluation across seven robustness dimensions and 21 sub-dimensions, ensuring a thorough assessment of model generalization. (2) Automation: Automated task generation, enabling the creation of a large number of diverse training and test samples. (3) Fine-grained: Incorporation of difficulty levels (L1–L5), providing detailed insights into when and how VLA models fail.

### Sensor Noise Protocol

Sensor Noise involves injecting photometric distortions to evaluate robustness under degraded input quality, including motion blur, gaussian blur, zoom blur, glass blur and fog or haze.

## LIBERO-PRO

LIBERO-PRO shows that without systematic robustness evaluation, benchmark success rates are misleading. The work addresses concerns about whether high LIBERO scores truly reflect model competency in more diverse and realistic settings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "312a5652-390d-4bb6-89b3-fa7528329192",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "922c5eb0-fa96-43c0-84cf-95ec72b30b39",
  "toolUseResult": {
    "query": "LIBERO-Plus LIBERO-PRO robustness evaluation VLA noise injection protocol 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CRCU1Dho6mtxoyjkr8o3et",
        "content": [
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://sylvestf.github.io/LIBERO-plus/"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of ...",
            "url": "https://arxiv.org/pdf/2510.03827"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2510.13626"
          },
          {
            "title": "[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.13626"
          },
          {
            "title": "LIBERO Benchmark: Vision-Language-Action in Robotics",
            "url": "https://www.emergentmind.com/topics/libero"
          },
          {
            "title": "How brittle are the VLA models in robotics | by Yanan Chen | Medium",
            "url": "https://medium.com/@yananchen1116/how-brittle-are-the-vla-models-in-robotics-66ab85286ecf"
          },
          {
            "title": "GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub",
            "url": "https://github.com/sylvestf/LIBERO-plus"
          },
          {
            "title": "CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models",
            "url": "https://cvpr.thecvf.com/virtual/2026/poster/38735"
          },
          {
            "title": "OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-",
            "url": "https://arxiv.org/pdf/2510.13626"
          }
        ]
      },
      "Based on the web search results, here's what I found about LIBERO-Plus, LIBERO-PRO, robustness evaluation, and VLA noise injection protocols:\n\n## LIBERO-Plus: In-depth Robustness Analysis\n\nLIBERO-Plus is a comprehensive, automatic, and fine-grained evaluation framework with controlled perturbations across seven dimensions: object layouts, camera viewpoints, robot initial states, language instructions, lighting conditions, background textures, and sensor noise.\n\n### Key Findings\n\nModels exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations. Surprisingly, models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.\n\n### Benchmark Structure\n\nLIBERO-plus offers three key advancements: (1) Comprehensive: Evaluation across seven robustness dimensions and 21 sub-dimensions, ensuring a thorough assessment of model generalization. (2) Automation: Automated task generation, enabling the creation of a large number of diverse training and test samples. (3) Fine-grained: Incorporation of difficulty levels (L1–L5), providing detailed insights into when and how VLA models fail.\n\n### Sensor Noise Protocol\n\nSensor Noise involves injecting photometric distortions to evaluate robustness under degraded input quality, including motion blur, gaussian blur, zoom blur, glass blur and fog or haze.\n\n## LIBERO-PRO\n\nLIBERO-PRO shows that without systematic robustness evaluation, benchmark success rates are misleading. The work addresses concerns about whether high LIBERO scores truly reflect model competency in more diverse and realistic settings."
    ],
    "durationSeconds": 7.170134245000023
  },
  "sourceToolAssistantUUID": "312a5652-390d-4bb6-89b3-fa7528329192",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-14T06:01:47.902Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018QT8W5tf861s3MkDusPMcX`</summary>

```json
{
  "query": "CoRL 2026 paper deadline submission date"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "922c5eb0-fa96-43c0-84cf-95ec72b30b39",
  "isSidechain": false,
  "requestId": "req_011Cb1xDvzezpbEu7uPfrD3a",
  "type": "assistant",
  "uuid": "5e2c54df-3470-4f9c-a30d-8effce8f1473",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dwyq5mMYFszbVcd8uBEH7E",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1016,
      "cache_read_input_tokens": 43265,
      "output_tokens": 61,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1016,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 61,
          "cache_read_input_tokens": 43265,
          "cache_creation_input_tokens": 1016,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1016
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

_source line 73 · 2026-05-14T06:01:51.188Z_

<details><summary>↩ Tool result · `toolu_018QT8W5tf861s3MkDusPMcX`</summary>

```text
Web search results for query: "CoRL 2026 paper deadline submission date"

Links: [{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf?lang=en"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL — The Conference on Robot Learning | Austin 2026-11-10 | Tadqiq.uz","url":"https://tadqiq.uz/en/xalqaro-konferensiyalar/corl"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"}]

Based on the search results, here are the key submission deadlines for CoRL 2026:

The abstract submission deadline is May 25, 2026, and the full paper submission deadline is May 28, 2026. However, note that the paper submission deadline is Thursday (5/28) EOD rather than Friday.

The conference itself will take place November 9-12 in Austin, TX.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e2c54df-3470-4f9c-a30d-8effce8f1473",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "fdbb3238-5bca-41af-937d-93a00388f837",
  "toolUseResult": {
    "query": "CoRL 2026 paper deadline submission date",
    "results": [
      {
        "tool_use_id": "srvtoolu_018qFoNb8Ng3QaqWAFjbSUtq",
        "content": [
          {
            "title": "Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"
          },
          {
            "title": "CoRL 2026 - Instruction for Authors",
            "url": "https://www.corl.org/contributions/instruction-for-authors"
          },
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "CoRL 2026",
            "url": "https://www.corl.org/"
          },
          {
            "title": "Conference on Robot Learning (@corl_conf) / Posts / X",
            "url": "https://x.com/corl_conf?lang=en"
          },
          {
            "title": "CoRL LaTeX Template | Robot Learning Conference Format | Underleaf",
            "url": "https://www.underleaf.ai/templates/corl"
          },
          {
            "title": "CoRL 2026 Conference | OpenReview",
            "url": "https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"
          },
          {
            "title": "Robot Learning Foundation",
            "url": "https://www.robot-learning.org/"
          },
          {
            "title": "CoRL — The Conference on Robot Learning | Austin 2026-11-10 | Tadqiq.uz",
            "url": "https://tadqiq.uz/en/xalqaro-konferensiyalar/corl"
          },
          {
            "title": "CoRL 2026 - Annoucements",
            "url": "https://www.corl.org/annoucements"
          }
        ]
      },
      "Based on the search results, here are the key submission deadlines for CoRL 2026:\n\nThe abstract submission deadline is May 25, 2026, and the full paper submission deadline is May 28, 2026. However, note that the paper submission deadline is Thursday (5/28) EOD rather than Friday.\n\nThe conference itself will take place November 9-12 in Austin, TX."
    ],
    "durationSeconds": 3.2803556199999875
  },
  "sourceToolAssistantUUID": "5e2c54df-3470-4f9c-a30d-8effce8f1473",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-14T06:01:53.889Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GMZo6h7WzKXRfkehKpxasE`</summary>

```json
{
  "query": "OpenVLA-OFT LIBERO Bridge V2 success rate LoRA fine-tuning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdbb3238-5bca-41af-937d-93a00388f837",
  "isSidechain": false,
  "requestId": "req_011Cb1xEN7WZUx59ob2XxsEA",
  "type": "assistant",
  "uuid": "c19f3ef2-b513-4dac-a8a4-6a72df48be07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DSte6ghgBi3RWNuZMNpry6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 599,
      "cache_read_input_tokens": 44281,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 599,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 44281,
          "cache_creation_input_tokens": 599,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 599
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

_source line 75 · 2026-05-14T06:02:01.702Z_

<details><summary>↩ Tool result · `toolu_01GMZo6h7WzKXRfkehKpxasE`</summary>

```text
Web search results for query: "OpenVLA-OFT LIBERO Bridge V2 success rate LoRA fine-tuning 2025"

Links: [{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v2"},{"title":"GitHub - CHELabUB/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/CHELabUB/openvla"},{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/html/2406.09246v3"},{"title":"Training Data for OpenVLA | Data Requirements & Formats | Claru","url":"https://claru.ai/models/openvla"}]

Based on the search results, here's what I found about OpenVLA-OFT on the LIBERO Bridge V2 with LoRA fine-tuning:

## Key Success Rate Results

OpenVLA-OFT significantly boosted OpenVLA's average success rate across four LIBERO task suites from 76.5% to 97.1%. This represents a major improvement through the optimized fine-tuning approach.

## Fine-Tuning Approach

The study used OpenVLA as the base model, adapting it via LoRA fine-tuning due to relatively small training datasets (500 demonstrations versus 1M demonstrations for pretraining).

## OFT Recipe Components

The Optimized Fine-Tuning (OFT) recipe integrates parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective to altogether improve inference efficiency, policy performance, and flexibility.

## Performance Impact

Beyond simulation, in real-world evaluations, the fine-tuning recipe enables OpenVLA to successfully execute dexterous, high-frequency control tasks on a bimanual ALOHA robot and outperform other VLAs by up to 15% (absolute) in average success rate.

The paper presenting these results was published in 2025, with the most recent version available in April 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c19f3ef2-b513-4dac-a8a4-6a72df48be07",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "e391f6d1-4f58-4cbb-a997-77438f0fb253",
  "toolUseResult": {
    "query": "OpenVLA-OFT LIBERO Bridge V2 success rate LoRA fine-tuning 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Fuer4eyiY8V5qgxys3EYLL",
        "content": [
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://openvla-oft.github.io/"
          },
          {
            "title": "GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub",
            "url": "https://github.com/openvla/openvla"
          },
          {
            "title": "GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub",
            "url": "https://github.com/moojink/openvla-oft"
          },
          {
            "title": "[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/abs/2502.19645"
          },
          {
            "title": "OpenVLA: An Open-Source Vision-Language-Action Model",
            "url": "https://openvla.github.io/"
          },
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/html/2502.19645v2"
          },
          {
            "title": "GitHub - CHELabUB/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub",
            "url": "https://github.com/CHELabUB/openvla"
          },
          {
            "title": "OpenVLA: Open Source VLA for Robotics",
            "url": "https://www.emergentmind.com/topics/openvla"
          },
          {
            "title": "OpenVLA: An Open-Source Vision-Language-Action Model",
            "url": "https://arxiv.org/html/2406.09246v3"
          },
          {
            "title": "Training Data for OpenVLA | Data Requirements & Formats | Claru",
            "url": "https://claru.ai/models/openvla"
          }
        ]
      },
      "Based on the search results, here's what I found about OpenVLA-OFT on the LIBERO Bridge V2 with LoRA fine-tuning:\n\n## Key Success Rate Results\n\nOpenVLA-OFT significantly boosted OpenVLA's average success rate across four LIBERO task suites from 76.5% to 97.1%. This represents a major improvement through the optimized fine-tuning approach.\n\n## Fine-Tuning Approach\n\nThe study used OpenVLA as the base model, adapting it via LoRA fine-tuning due to relatively small training datasets (500 demonstrations versus 1M demonstrations for pretraining).\n\n## OFT Recipe Components\n\nThe Optimized Fine-Tuning (OFT) recipe integrates parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective to altogether improve inference efficiency, policy performance, and flexibility.\n\n## Performance Impact\n\nBeyond simulation, in real-world evaluations, the fine-tuning recipe enables OpenVLA to successfully execute dexterous, high-frequency control tasks on a bimanual ALOHA robot and outperform other VLAs by up to 15% (absolute) in average success rate.\n\nThe paper presenting these results was published in 2025, with the most recent version available in April 2025."
    ],
    "durationSeconds": 7.808860473000037
  },
  "sourceToolAssistantUUID": "c19f3ef2-b513-4dac-a8a4-6a72df48be07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 76 · 2026-05-14T06:02:14.413Z_

Now I have comprehensive research. Let me synthesize everything and formulate the revised idea. The key insights from my research:

1. **AFBC oscillation** is a real problem — need a robust alternative to IQL for advantage estimation
2. **CWBC** showed conditioning on OOD returns fails — need conservative conditioning or weighting
3. **GR-RL** uses distributional Q-values as progress function + filtering (direct competitor)
4. **SARM/RA-BC** uses progress-delta reward model + weighting for π0 (direct competitor)
5. **VLAC** is a generalist progress estimator trained on diverse data
6. **A2PO** already does advantage-conditioned offline RL via CVAE
7. **User wanted filtering/re-weighting**, not conditioning
8. **SmolVLA** (450M params) available for compute-efficient validation

Given all these issues — especially the CWBC problem with conditioning, A2PO novelty overlap, user misalignment, and the strong showing of GR-RL and SARM/RA-BC as competitors — I should do a **major revision** that pivots from conditioning to a demonstration distillation pipeline using reward-weighted fine-tuning, while maintaining the core insight of using VLA's own features for offline quality scoring.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e391f6d1-4f58-4cbb-a997-77438f0fb253",
  "isSidechain": false,
  "requestId": "req_011Cb1xF93UUg3EzK1Aiw2wt",
  "type": "assistant",
  "uuid": "e4c0bbb6-f124-4ab7-ba0d-1d24c28ed474",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DoaaiqUBP9gTLQCtsCn3Zc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 875,
      "cache_read_input_tokens": 44880,
      "output_tokens": 368,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 875,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 368,
          "cache_read_input_tokens": 44880,
          "cache_creation_input_tokens": 875,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 875
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

_source line 77 · 2026-05-14T06:02:15.186Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ji7phQWA2iKwLWaSvUWKtG`</summary>

```json
{
  "query": "VLA pretrained features intermediate representations value estimation self-supervised reward 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4c0bbb6-f124-4ab7-ba0d-1d24c28ed474",
  "isSidechain": false,
  "requestId": "req_011Cb1xF93UUg3EzK1Aiw2wt",
  "type": "assistant",
  "uuid": "dfaac9c9-ec3f-41ee-b997-82456663ccfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DoaaiqUBP9gTLQCtsCn3Zc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 875,
      "cache_read_input_tokens": 44880,
      "output_tokens": 368,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 875,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 368,
          "cache_read_input_tokens": 44880,
          "cache_creation_input_tokens": 875,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 875
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

_source line 78_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Offline Advantage Conditioning for VLA Noise Decomposition\",   \"core_p…",
  "leafUuid": "dfaac9c9-ec3f-41ee-b997-82456663ccfa",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80"
}
```

---

### Runtime record

_source line 79_

```json
{
  "type": "ai-title",
  "aiTitle": "Offline VLA fine-tuning via trajectory-level return ranking and conservative advantage weighting",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80"
}
```

---

### Tool result

_source line 80 · 2026-05-14T06:02:23.452Z_

<details><summary>↩ Tool result · `toolu_01Ji7phQWA2iKwLWaSvUWKtG`</summary>

```text
Web search results for query: "VLA pretrained features intermediate representations value estimation self-supervised reward 2025"

Links: [{"title":"2025-9-22 A Vision-Language-Action-Critic Model","url":"https://arxiv.org/pdf/2509.15937"},{"title":"[2411.17451] VL-RewardBench: A Challenging Benchmark for Vision-Language Generative Reward Models","url":"https://arxiv.org/abs/2411.17451"},{"title":"VLA-RFT: Vision-Language-Action Reinforcement Fine-Tuning with Verified Rewards in World Simulators | OpenReview","url":"https://openreview.net/forum?id=Jaut99EHeu"},{"title":"CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf"},{"title":"[2510.00406] VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators","url":"https://arxiv.org/abs/2510.00406"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Vision-language-action+(VLA)+models"},{"title":"FUTURE-VLA: Forecasting Unified Trajectories Under Real-time Execution","url":"https://arxiv.org/html/2602.15882"},{"title":"IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model","url":"https://www.arxiv.org/pdf/2508.06571"},{"title":"VLA-RFT: Vision-language-action Reinforcement fine-tuning with verified rewards in world simulators","url":"https://arxiv.org/html/2510.00406v1"},{"title":"A Survey on Reinforcement Learning of Vision-Language-Action Models for Robotic Manipulation | TechRxiv","url":"https://www.techrxiv.org/users/934012/articles/1366553/master/file/data/TechrxivA_Survey_on_Reinforcement_Learning_of_Vision-Language-Action_Models_for_Robotic_Manipulation/TechrxivA_Survey_on_Reinforcement_Learning_of_Vision-Language-Action_Models_for_Robotic_Manipulation.pdf?inline=true"}]

I found several relevant research papers from 2025 on Vision-Language-Action (VLA) models that relate to your search query. Here's a summary of the key findings:

## Recent VLA Research with Reward and Value Learning

Robotic reinforcement learning with VLA models is bottlenecked by sparse, handcrafted rewards. VLAC is a general process reward model built upon InternVL that outputs dense progress delta and done signal, eliminating task-specific reward engineering and supporting one-shot in-context transfer to unseen tasks and environments.

VLA-RFT is a Reinforcement Fine-Tuning framework that leverages a data-driven world model as a controllable simulator. Trained from real interaction data, the simulator predicts future visual observations conditioned on actions, allowing policy rollouts with dense, trajectory-level rewards derived from goal-achieving references, delivering an efficient and action-aligned learning signal.

## Self-Supervised Representations for Value Estimation

Self-Referential Policy Optimization (SRPO) eliminates the need for external demonstrations or manual reward engineering by leveraging the model's own successful trajectories as a self-reference. A core innovation is the use of latent world representations to measure behavioral progress robustly. Instead of relying on raw pixels or requiring domain-specific fine-tuning, compressed, transferable encodings from a world model's latent space are utilized, which naturally capture progress patterns across environments.

V-JEPA 2 involves self-supervised video models that enable understanding, prediction and planning.

These papers represent active research in 2025 focused on leveraging pretrained VLA features and intermediate representations for improved value estimation and self-supervised reward learning in robotic manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfaac9c9-ec3f-41ee-b997-82456663ccfa",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "f16aa643-4327-4d6b-832e-e1da02e5fb29",
  "toolUseResult": {
    "query": "VLA pretrained features intermediate representations value estimation self-supervised reward 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_012WGFadBFEFvg5aQQZemwkM",
        "content": [
          {
            "title": "2025-9-22 A Vision-Language-Action-Critic Model",
            "url": "https://arxiv.org/pdf/2509.15937"
          },
          {
            "title": "[2411.17451] VL-RewardBench: A Challenging Benchmark for Vision-Language Generative Reward Models",
            "url": "https://arxiv.org/abs/2411.17451"
          },
          {
            "title": "VLA-RFT: Vision-Language-Action Reinforcement Fine-Tuning with Verified Rewards in World Simulators | OpenReview",
            "url": "https://openreview.net/forum?id=Jaut99EHeu"
          },
          {
            "title": "CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models",
            "url": "https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf"
          },
          {
            "title": "[2510.00406] VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators",
            "url": "https://arxiv.org/abs/2510.00406"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=Vision-language-action+(VLA)+models"
          },
          {
            "title": "FUTURE-VLA: Forecasting Unified Trajectories Under Real-time Execution",
            "url": "https://arxiv.org/html/2602.15882"
          },
          {
            "title": "IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model",
            "url": "https://www.arxiv.org/pdf/2508.06571"
          },
          {
            "title": "VLA-RFT: Vision-language-action Reinforcement fine-tuning with verified rewards in world simulators",
            "url": "https://arxiv.org/html/2510.00406v1"
          },
          {
            "title": "A Survey on Reinforcement Learning of Vision-Language-Action Models for Robotic Manipulation | TechRxiv",
            "url": "https://www.techrxiv.org/users/934012/articles/1366553/master/file/data/TechrxivA_Survey_on_Reinforcement_Learning_of_Vision-Language-Action_Models_for_Robotic_Manipulation/TechrxivA_Survey_on_Reinforcement_Learning_of_Vision-Language-Action_Models_for_Robotic_Manipulation.pdf?inline=true"
          }
        ]
      },
      "I found several relevant research papers from 2025 on Vision-Language-Action (VLA) models that relate to your search query. Here's a summary of the key findings:\n\n## Recent VLA Research with Reward and Value Learning\n\nRobotic reinforcement learning with VLA models is bottlenecked by sparse, handcrafted rewards. VLAC is a general process reward model built upon InternVL that outputs dense progress delta and done signal, eliminating task-specific reward engineering and supporting one-shot in-context transfer to unseen tasks and environments.\n\nVLA-RFT is a Reinforcement Fine-Tuning framework that leverages a data-driven world model as a controllable simulator. Trained from real interaction data, the simulator predicts future visual observations conditioned on actions, allowing policy rollouts with dense, trajectory-level rewards derived from goal-achieving references, delivering an efficient and action-aligned learning signal.\n\n## Self-Supervised Representations for Value Estimation\n\nSelf-Referential Policy Optimization (SRPO) eliminates the need for external demonstrations or manual reward engineering by leveraging the model's own successful trajectories as a self-reference. A core innovation is the use of latent world representations to measure behavioral progress robustly. Instead of relying on raw pixels or requiring domain-specific fine-tuning, compressed, transferable encodings from a world model's latent space are utilized, which naturally capture progress patterns across environments.\n\nV-JEPA 2 involves self-supervised video models that enable understanding, prediction and planning.\n\nThese papers represent active research in 2025 focused on leveraging pretrained VLA features and intermediate representations for improved value estimation and self-supervised reward learning in robotic manipulation tasks."
    ],
    "durationSeconds": 8.261062676000002
  },
  "sourceToolAssistantUUID": "dfaac9c9-ec3f-41ee-b997-82456663ccfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 81 · 2026-05-14T06:02:23.461Z_

```json
{
  "parentUuid": "f16aa643-4327-4d6b-832e-e1da02e5fb29",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "40c8fbd3-ec58-4ccc-b1f5-e870ed0be5b4",
  "timestamp": "2026-05-14T06:02:23.461Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 82 · 2026-05-14T06:02:26.039Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PFZeoxfzKu5XUkrw72SoL4`</summary>

```json
{
  "query": "IRL-VLA reward world model vision language action 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40c8fbd3-ec58-4ccc-b1f5-e870ed0be5b4",
  "isSidechain": false,
  "requestId": "req_011Cb1xGk5AE9gkSJ44dy6d3",
  "type": "assistant",
  "uuid": "a4b78236-9076-4d69-8fec-b28106279691",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PZ8jZKuNxQ3Yd6MFPBwqop",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1519,
      "cache_read_input_tokens": 45755,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1519,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 65,
          "cache_read_input_tokens": 45755,
          "cache_creation_input_tokens": 1519,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1519
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

_source line 83 · 2026-05-14T06:02:32.840Z_

<details><summary>↩ Tool result · `toolu_01PFZeoxfzKu5XUkrw72SoL4`</summary>

```text
Web search results for query: "IRL-VLA reward world model vision language action 2025"

Links: [{"title":"[2508.06571] IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model","url":"https://arxiv.org/abs/2508.06571"},{"title":"IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250806571J/abstract"},{"title":"IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model","url":"https://www.arxiv.org/pdf/2508.06571"},{"title":"IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model - Jiang Anqing","url":"https://peterjaq.github.io/IRLVLA/"},{"title":"IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model | alphaXiv","url":"https://www.alphaxiv.org/overview/2508.06571"},{"title":"GitHub - IRL-VLA/IRL-VLA: Official repo for IRL-VLA · GitHub","url":"https://github.com/IRL-VLA/IRL-VLA"},{"title":"IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model for End-to-End Autonomous Driving","url":"https://arxiv.org/html/2508.06571"},{"title":"IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model","url":"https://arxiv.org/html/2508.06571v1"},{"title":"IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2508.06571"},{"title":"[PDF] IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/IRL-VLA:-Training-an-Vision-Language-Action-Policy-Jiang-Gao/d2e28c42829e199261c05e615c0dba33fbc121b3"}]

Here are the search results for IRL-VLA reward world model vision language action:

## Overview

IRL-VLA is a framework developed by researchers from Bosch Corporate Research and academic institutions that trains a Vision-Language-Action (VLA) policy for end-to-end autonomous driving using a Reward World Model (RWM) and inverse reinforcement learning.

## Key Approach

The framework uses a three-stage approach—imitation policy learning, inverse environment learning, and close-loop reinforcement learning—to address the limitations of open-loop imitation learning and simulator-based training. Specifically:

1. **Stage 1**: The VLA architecture is proposed and the VLA policy is pretrained via imitation learning.

2. **Stage 2**: A lightweight reward world model is constructed via inverse reinforcement learning to enable efficient close-loop reward computation.

3. **Stage 3**: Specialized reward world model guidance reinforcement learning via PPO (Proximal Policy Optimization) is designed to effectively balance safety incidents, comfortable driving, and traffic efficiency.

## Performance and Innovation

IRL-VLA achieves state-of-the-art performance on the NAVSIM v2 CVPR challenge benchmark, scoring 45.0 EDPM5 and securing the 1st runner-up position in the CVPR 2025 Autonomous Grand Challenge. Additionally, IRL-VLA is the first close-loop VLA approach incorporating sensor inputs without relying on simulators.

The paper was published in August 2025 on arXiv (arXiv:2508.06571).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4b78236-9076-4d69-8fec-b28106279691",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "a559863a-4392-4d73-a055-1374c676697a",
  "toolUseResult": {
    "query": "IRL-VLA reward world model vision language action 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BZLUPBHkTc29VwAsQnKJgT",
        "content": [
          {
            "title": "[2508.06571] IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model",
            "url": "https://arxiv.org/abs/2508.06571"
          },
          {
            "title": "IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250806571J/abstract"
          },
          {
            "title": "IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model",
            "url": "https://www.arxiv.org/pdf/2508.06571"
          },
          {
            "title": "IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model - Jiang Anqing",
            "url": "https://peterjaq.github.io/IRLVLA/"
          },
          {
            "title": "IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2508.06571"
          },
          {
            "title": "GitHub - IRL-VLA/IRL-VLA: Official repo for IRL-VLA · GitHub",
            "url": "https://github.com/IRL-VLA/IRL-VLA"
          },
          {
            "title": "IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model for End-to-End Autonomous Driving",
            "url": "https://arxiv.org/html/2508.06571"
          },
          {
            "title": "IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model",
            "url": "https://arxiv.org/html/2508.06571v1"
          },
          {
            "title": "IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/arxiv/2508.06571"
          },
          {
            "title": "[PDF] IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/IRL-VLA:-Training-an-Vision-Language-Action-Policy-Jiang-Gao/d2e28c42829e199261c05e615c0dba33fbc121b3"
          }
        ]
      },
      "Here are the search results for IRL-VLA reward world model vision language action:\n\n## Overview\n\nIRL-VLA is a framework developed by researchers from Bosch Corporate Research and academic institutions that trains a Vision-Language-Action (VLA) policy for end-to-end autonomous driving using a Reward World Model (RWM) and inverse reinforcement learning.\n\n## Key Approach\n\nThe framework uses a three-stage approach—imitation policy learning, inverse environment learning, and close-loop reinforcement learning—to address the limitations of open-loop imitation learning and simulator-based training. Specifically:\n\n1. **Stage 1**: The VLA architecture is proposed and the VLA policy is pretrained via imitation learning.\n\n2. **Stage 2**: A lightweight reward world model is constructed via inverse reinforcement learning to enable efficient close-loop reward computation.\n\n3. **Stage 3**: Specialized reward world model guidance reinforcement learning via PPO (Proximal Policy Optimization) is designed to effectively balance safety incidents, comfortable driving, and traffic efficiency.\n\n## Performance and Innovation\n\nIRL-VLA achieves state-of-the-art performance on the NAVSIM v2 CVPR challenge benchmark, scoring 45.0 EDPM5 and securing the 1st runner-up position in the CVPR 2025 Autonomous Grand Challenge. Additionally, IRL-VLA is the first close-loop VLA approach incorporating sensor inputs without relying on simulators.\n\nThe paper was published in August 2025 on arXiv (arXiv:2508.06571)."
    ],
    "durationSeconds": 6.795682433000009
  },
  "sourceToolAssistantUUID": "a4b78236-9076-4d69-8fec-b28106279691",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-14T06:02:35.597Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NxBsfdyDiAC6aNgjJKt7EE`</summary>

```json
{
  "query": "TOPReward token probabilities zero-shot reward VLM robotics 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a559863a-4392-4d73-a055-1374c676697a",
  "isSidechain": false,
  "requestId": "req_011Cb1xHSAffaQAeRibR2PN8",
  "type": "assistant",
  "uuid": "507120db-d9d5-40ae-a636-5661250e8a61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B7Pm13bVJMhakhNaP7uhfv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1007,
      "cache_read_input_tokens": 47274,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1007,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 47274,
          "cache_creation_input_tokens": 1007,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1007
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

_source line 85 · 2026-05-14T06:02:43.108Z_

<details><summary>↩ Tool result · `toolu_01NxBsfdyDiAC6aNgjJKt7EE`</summary>

```text
Web search results for query: "TOPReward token probabilities zero-shot reward VLM robotics 2026"

Links: [{"title":"TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics","url":"https://arxiv.org/html/2602.19313v1"},{"title":"TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics","url":"https://topreward.github.io/webpage/"},{"title":"[2602.19313] TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics","url":"https://arxiv.org/abs/2602.19313"},{"title":"GitHub - TOPReward/TOPReward: TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics · GitHub","url":"https://github.com/TOPReward/TOPReward"},{"title":"TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics | alphaXiv","url":"https://www.alphaxiv.org/overview/2602.19313v1"},{"title":"[Quick Review] TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics","url":"https://liner.com/review/topreward-token-probabilities-as-hidden-zeroshot-rewards-for-robotics"},{"title":"Paper page - TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics","url":"https://huggingface.co/papers/2602.19313"},{"title":"Topreward: Token Probabilities As Hidden Zero-Shot Rewards For Robotics | PDF | Cognitive Science | Computing","url":"https://www.scribd.com/document/1003030020/2602-19313v1"},{"title":"TOPReward: VLM Token Logits for Robotic Rewards - YouTube","url":"https://www.youtube.com/watch?v=Tkt5KjbnsRY"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=TOPReward:+Token+Probabilities+as+Hidden+Zero-Shot+Rewards+for+Robotics."}]

I found comprehensive information about TOPReward. Here's what the search results reveal:

## Overview

TOPReward poses a binary completion query ("does this trajectory complete the task?") and extracts the probability of the affirmative token as a continuous reward. It is a zero-shot progress estimator for robotic manipulation that interprets pretrained video VLM token likelihoods as temporal value functions.

## Key Innovation

Instead of prompting the VLM to output the value of the completion percentage in text space, TOPReward extracts the model's internal "belief" by analyzing the probabilistic distribution of its token logits. By measuring the shift in confidence toward task-completion tokens over time, it derives a continuous, well-posed progress signal directly from the VLM's latent world knowledge.

## Performance Results

In zero-shot evaluations across 130+ distinct real-world tasks and multiple robot platforms (e.g., Franka, YAM, SO-100/101), TOPReward achieves 0.947 mean Value-Order Correlation (VOC) on Qwen3-VL, dramatically outperforming the state-of-the-art GVL baseline which achieves near-zero correlation on the same open-source model.

On the Open X-Embodiment dataset, TOPReward with Qwen3-VL-8B achieves a Value-Order Correlation (VOC) of 0.857. Similarly, with Molmo2-8B, TOPReward reaches 0.417 VOC compared to GVL's near-zero -0.016.

## Benchmark

ManiRewardBench is a benchmark comprising over 130 distinct real-world manipulation tasks spanning multiple robot platforms (Franka Emika arms, Single-Arm/Bimanual YAM, SO-100/101) with temporal annotations of task progress.

## Applications

TOPReward serves as a versatile tool for downstream applications, including success detection and reward-aligned behavior cloning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "507120db-d9d5-40ae-a636-5661250e8a61",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "38c3f415-e33a-4d47-8600-0d445ed6d5f6",
  "toolUseResult": {
    "query": "TOPReward token probabilities zero-shot reward VLM robotics 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016py9wrUdjH1K4ihzpWv3Bs",
        "content": [
          {
            "title": "TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics",
            "url": "https://arxiv.org/html/2602.19313v1"
          },
          {
            "title": "TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics",
            "url": "https://topreward.github.io/webpage/"
          },
          {
            "title": "[2602.19313] TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics",
            "url": "https://arxiv.org/abs/2602.19313"
          },
          {
            "title": "GitHub - TOPReward/TOPReward: TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics · GitHub",
            "url": "https://github.com/TOPReward/TOPReward"
          },
          {
            "title": "TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2602.19313v1"
          },
          {
            "title": "[Quick Review] TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics",
            "url": "https://liner.com/review/topreward-token-probabilities-as-hidden-zeroshot-rewards-for-robotics"
          },
          {
            "title": "Paper page - TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics",
            "url": "https://huggingface.co/papers/2602.19313"
          },
          {
            "title": "Topreward: Token Probabilities As Hidden Zero-Shot Rewards For Robotics | PDF | Cognitive Science | Computing",
            "url": "https://www.scribd.com/document/1003030020/2602-19313v1"
          },
          {
            "title": "TOPReward: VLM Token Logits for Robotic Rewards - YouTube",
            "url": "https://www.youtube.com/watch?v=Tkt5KjbnsRY"
          },
          {
            "title": "Google Scholar",
            "url": "https://scholar.google.com/scholar?q=TOPReward:+Token+Probabilities+as+Hidden+Zero-Shot+Rewards+for+Robotics."
          }
        ]
      },
      "I found comprehensive information about TOPReward. Here's what the search results reveal:\n\n## Overview\n\nTOPReward poses a binary completion query (\"does this trajectory complete the task?\") and extracts the probability of the affirmative token as a continuous reward. It is a zero-shot progress estimator for robotic manipulation that interprets pretrained video VLM token likelihoods as temporal value functions.\n\n## Key Innovation\n\nInstead of prompting the VLM to output the value of the completion percentage in text space, TOPReward extracts the model's internal \"belief\" by analyzing the probabilistic distribution of its token logits. By measuring the shift in confidence toward task-completion tokens over time, it derives a continuous, well-posed progress signal directly from the VLM's latent world knowledge.\n\n## Performance Results\n\nIn zero-shot evaluations across 130+ distinct real-world tasks and multiple robot platforms (e.g., Franka, YAM, SO-100/101), TOPReward achieves 0.947 mean Value-Order Correlation (VOC) on Qwen3-VL, dramatically outperforming the state-of-the-art GVL baseline which achieves near-zero correlation on the same open-source model.\n\nOn the Open X-Embodiment dataset, TOPReward with Qwen3-VL-8B achieves a Value-Order Correlation (VOC) of 0.857. Similarly, with Molmo2-8B, TOPReward reaches 0.417 VOC compared to GVL's near-zero -0.016.\n\n## Benchmark\n\nManiRewardBench is a benchmark comprising over 130 distinct real-world manipulation tasks spanning multiple robot platforms (Franka Emika arms, Single-Arm/Bimanual YAM, SO-100/101) with temporal annotations of task progress.\n\n## Applications\n\nTOPReward serves as a versatile tool for downstream applications, including success detection and reward-aligned behavior cloning."
    ],
    "durationSeconds": 7.505726263999997
  },
  "sourceToolAssistantUUID": "507120db-d9d5-40ae-a636-5661250e8a61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 86 · 2026-05-14T06:03:55.197Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the landscape. Let me synthesize my findings and formulate the revised idea.

Key insights from research:

1. **AFBC oscillation problem is real** - IQL-based advantage estimation from demo-only data produces near-zero advantages. The original idea's fix (VLA features) is speculative.

2. **CWBC shows conditioning on OOD values degrades** - Pure advantage conditioning at test time is unreliable.

3. **GR-RL** (ByteDance, Dec 2025) - Uses distributional Q-values as task progress function to filter demonstrations. Stage 1 filters with Q-value progress, Stage 2 augments, Stage 3 does online RL. Direct competitor.
   
4. **SARM/RA-BC** - Uses a progress-delta reward model to weight BC loss during fine-tuning, staying purely offline and achieving 83% on T-shirt folding versus 8% for the baseline. Another direct competitor.

5. **A2PO** (NeurIPS 2024) - Already tackles advantage-conditioned offline RL, so there's significant novelty overlap.

6. **VLAC** - A general-purpose VLA critic that provides dense progress estimates, making it highly relevant to this direction.

7. **TOPReward** (Feb 2026) - Uses zero-shot VLM-based progress estimation via token probabilities, achieving 0.947 VOC on real tasks and substantially outperforming GVL on open-source models.

The user actually wants filtering and re-weighting rather than conditioning, so I need to shift my approach. Given the compute constraint of 200 H100-hours, the right direction is a major pivot toward VLA self-scoring demonstration distillation—a fully offline method that leverages the VLA's own pretrained features to score demonstration quality at each timestep, then applies curriculum-weighted fine-tuning to improve learning from noisy data without environment interaction. This differentiates from GR-RL's distributional Q-learning approach and addresses the core challenge of improving VLA fine-tuning quality.

The key advantages over related work are clear: unlike GR-RL, we avoid training a separate critic and the binary threshold problem; unlike SARM and RA-BC, we don't need natural language annotations; unlike ARFM, we skip hand-designed reward functions; unlike TOPReward and GVL, we use the VLA's own task-adapted representations instead of external VLMs, cutting inference costs; and unlike A2PO, we're not conditioning on anything.

Now for the technical approach: I'm using the VLA's frozen pretrained features to score task progress by measuring cosine similarity between consecutive feature representations and goal embeddings, which captures the same intuition as TOPReward but leverages the VLA's internal representations. Then I'm computing rewards as the delta in progress between timesteps.

Instead of hard filtering or conditioning like prior work, I'm applying a soft curriculum that weights each timestep's loss contribution based on its progress score—this keeps noisy data in the training signal rather than discarding it. I'm also combining timestep-level and trajectory-level scoring to stabilize the weighting and avoid the oscillation problems I've seen in other approaches.

But wait, I'm realizing this is starting to overlap significantly with SARM and RA-BC. Let me reconsider what actually differentiates this approach...

The core distinction is that I'm using the VLA's own frozen pretrained features for quality scoring rather than training a separate reward model or relying on external annotations. The VLA essentially scores its own training data using representations it already has, which eliminates the overhead of additional models or environment interaction. The question is whether the VLA's intermediate features are actually richer than what CLIP alone provides—since most VLAs already use CLIP-based vision encoders anyway—but the full feature hierarchy from the VLA's multimodal training should capture more nuanced task-relevant information than raw CLIP embeddings.

Now I need to step back and address what the reviewer is really asking for: the core novelty should directly tackle the specific problems they identified—AFBC oscillation, CWBC out-of-distribution conditioning, and the computational constraints—rather than just proposing a self-referential scoring mechanism. The key decision is whether to frame this as a filtering/re-weighting approach that uses VLA features for robust advantage estimation, or to pursue something else entirely. A: VLA self-referential scoring (using VLA's own features as reward signal)
- Pros: Elegant, annotation-free, no separate model
- Cons: May not work well if VLA features aren't discriminative enough for progress estimation in demo-only data
- Differentiation from SARM: No separate reward model, no annotations needed
- Differentiation from GR-RL: No separate critic, no online RL
- Differentiation from TOPReward/GVL: Uses VLA features internally, not external VLM

Option B: Multi-granularity progress scoring with adaptive weighting
- Use trajectory-level ranking (robust, avoids AFBC oscillation) as a coarse signal
- Use timestep-level progress deltas (fine-grained, but noisy) as a fine signal
- Combine via a hierarchical weighting scheme where trajectory rank sets the base weight and timestep delta refines it, which addresses AFBC oscillation since the trajectory-level signal stays stable even when timestep advantages fluctuate

Option C combines both approaches—VLA self-referential scoring at multiple granularities with adaptive weighting. I think this is the strongest direction. The core idea is to extract self-referential progress scores from the VLA's frozen features at each timestep, aggregate them into trajectory-level returns, then use hierarchical reward-weighted BC where the trajectory return anchors the base weight and timestep progress deltas provide fine-grained refinement. This naturally sidesteps the oscillation problems that plague AFBC.

Now I'm questioning how novel the hierarchical weighting really is—ARFM already does adaptive loss weighting and SARM already weights by progress deltas. The real novelty has to be sharper. What actually matters is that the VLA's pretrained representations already implicitly encode task progress from large-scale robot data pretraining, so a lightweight progress estimator probing those frozen features can extract quality signals without needing external reward models, language annotations, environment interaction, or separate critic networks.

This is essentially self-distillation—the VLA identifies which training examples are good using knowledge already baked into its weights. Compared to SARM, which requires natural language subtask annotations and trains a full transformer reward model on generic CLIP features, our approach needs no annotations, leverages the VLA's richer task-adapted representations, and uses only a cheap frozen-feature MLP probe. For handling the AFBC oscillation issue—

trajectory-level ranking is more robust than noisy timestep deltas, which GR-RL's success validates empirically. I'm planning to evaluate on LIBERO with controlled noise injection at multiple rates, starting with SmolVLA for efficiency and scaling to OpenVLA-OFT for final validation. Let me check if anyone's already explored self-referential scoring specifically for VLAs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38c3f415-e33a-4d47-8600-0d445ed6d5f6",
  "isSidechain": false,
  "requestId": "req_011Cb1xJC48X4uWpBe1ei9Kn",
  "type": "assistant",
  "uuid": "39a23c01-25f8-43f5-9888-15e951685b08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JSerYUc2yXtBa5ZUcoLNAp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1091,
      "cache_read_input_tokens": 48281,
      "output_tokens": 2686,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1091,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2686,
          "cache_read_input_tokens": 48281,
          "cache_creation_input_tokens": 1091,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1091
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

_source line 87 · 2026-05-14T06:03:55.199Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CNovoFC5c5tcpJxqcuYc95`</summary>

```json
{
  "query": "\"self-referential\" OR \"self-scoring\" OR \"self-distillation\" VLA demonstration quality pretrained features 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39a23c01-25f8-43f5-9888-15e951685b08",
  "isSidechain": false,
  "requestId": "req_011Cb1xJC48X4uWpBe1ei9Kn",
  "type": "assistant",
  "uuid": "2ee5335a-c7e6-4aba-958a-e062c85fa5c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JSerYUc2yXtBa5ZUcoLNAp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1091,
      "cache_read_input_tokens": 48281,
      "output_tokens": 2686,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1091,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2686,
          "cache_read_input_tokens": 48281,
          "cache_creation_input_tokens": 1091,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1091
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

_source line 88_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Offline Advantage Conditioning for VLA Noise Decomposition\",   \"core_p…",
  "leafUuid": "2ee5335a-c7e6-4aba-958a-e062c85fa5c3",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80"
}
```

---

### Runtime record

_source line 89_

```json
{
  "type": "ai-title",
  "aiTitle": "Offline VLA fine-tuning via trajectory-level return ranking and conservative advantage weighting",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80"
}
```

---

### Tool result

_source line 90 · 2026-05-14T06:04:02.930Z_

<details><summary>↩ Tool result · `toolu_01CNovoFC5c5tcpJxqcuYc95`</summary>

```text
Web search results for query: ""self-referential" OR "self-scoring" OR "self-distillation" VLA demonstration quality pretrained features 2025 2026"

Links: [{"title":"Self-Distillation Zero: Self-Revision Turns Binary Rewards into Dense Supervision","url":"https://arxiv.org/html/2604.12002v1"},{"title":"Reinforcement Learning via Self-Distillation","url":"https://arxiv.org/pdf/2601.20802"},{"title":"REINFORCEMENT LEARNING VIA SELF-DISTILLATION","url":"https://openreview.net/pdf?id=k8DcHShsrJ"},{"title":"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | OpenReview","url":"https://openreview.net/forum?id=eUGoqrZ6Ea"},{"title":"Feature Refinement via Self-Knowledge Distillation","url":"https://openaccess.thecvf.com/content/CVPR2021/papers/Ji_Refine_Myself_by_Teaching_Myself_Feature_Refinement_via_Self-Knowledge_Distillation_CVPR_2021_paper.pdf"},{"title":"[2601.19897] Self-Distillation Enables Continual Learning","url":"https://arxiv.org/abs/2601.19897"},{"title":"SELF-DISTILLATION ENABLES CONTINUAL LEARNING Idan Shenfeld1 2∗ Mehul Damani1","url":"https://arxiv.org/pdf/2601.19897"},{"title":"Self-Distillation Enables Continual Learning","url":"https://arxiv.org/html/2601.19897v1"},{"title":"Paper page - Self-Distillation Enables Continual Learning","url":"https://huggingface.co/papers/2601.19897"},{"title":"(PDF) Reinforcement Learning via Self-Distillation","url":"https://www.researchgate.net/publication/400178402_Reinforcement_Learning_via_Self-Distillation"}]

I've completed the web search on your query about self-referential, self-scoring, and self-distillation methods for VLAs (vision-language-action models) with demonstration quality and pretrained features from 2025-2026. Here are the key findings:

## Self-Distillation Methods (2025-2026)

Recent work uses the current policy as a "self-teacher" that, rather than sampling a new response, re-evaluates the existing rollout after receiving rich feedback. This approach addresses a key limitation in reinforcement learning for language models.

### Self-Distillation Fine-Tuning (SDFT)

Self-Distillation Fine-Tuning (SDFT) is a method that enables on-policy learning directly from demonstrations. When models learn from data generated by their current policy, they exhibit substantially reduced catastrophic forgetting compared to off-policy alternatives.

### Self-Distillation for RL

Recent self-distillation methods eliminate the need for external teachers by conditioning the student on privileged information to serve as its own teacher, where the privileged context can include reasoning traces, in-context demonstrations, or conciseness prompts.

### VLA Applications

Supervised fine-tuning (SFT) has become the de facto post-training strategy for large vision-language-action (VLA) models, but its reliance on costly human demonstrations limits scalability. A framework called Probe, Learn, Distill (PLD) improves VLAs through residual reinforcement learning and distribution-aware data collection.

The research shows that these self-distillation approaches enable more efficient learning from demonstrations while maintaining model capabilities across multiple tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ee5335a-c7e6-4aba-958a-e062c85fa5c3",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "0b5148e2-380f-46db-ace6-c4854a67c220",
  "toolUseResult": {
    "query": "\"self-referential\" OR \"self-scoring\" OR \"self-distillation\" VLA demonstration quality pretrained features 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TKn9C9bNuWTwG1mfKGkZfD",
        "content": [
          {
            "title": "Self-Distillation Zero: Self-Revision Turns Binary Rewards into Dense Supervision",
            "url": "https://arxiv.org/html/2604.12002v1"
          },
          {
            "title": "Reinforcement Learning via Self-Distillation",
            "url": "https://arxiv.org/pdf/2601.20802"
          },
          {
            "title": "REINFORCEMENT LEARNING VIA SELF-DISTILLATION",
            "url": "https://openreview.net/pdf?id=k8DcHShsrJ"
          },
          {
            "title": "Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | OpenReview",
            "url": "https://openreview.net/forum?id=eUGoqrZ6Ea"
          },
          {
            "title": "Feature Refinement via Self-Knowledge Distillation",
            "url": "https://openaccess.thecvf.com/content/CVPR2021/papers/Ji_Refine_Myself_by_Teaching_Myself_Feature_Refinement_via_Self-Knowledge_Distillation_CVPR_2021_paper.pdf"
          },
          {
            "title": "[2601.19897] Self-Distillation Enables Continual Learning",
            "url": "https://arxiv.org/abs/2601.19897"
          },
          {
            "title": "SELF-DISTILLATION ENABLES CONTINUAL LEARNING Idan Shenfeld1 2∗ Mehul Damani1",
            "url": "https://arxiv.org/pdf/2601.19897"
          },
          {
            "title": "Self-Distillation Enables Continual Learning",
            "url": "https://arxiv.org/html/2601.19897v1"
          },
          {
            "title": "Paper page - Self-Distillation Enables Continual Learning",
            "url": "https://huggingface.co/papers/2601.19897"
          },
          {
            "title": "(PDF) Reinforcement Learning via Self-Distillation",
            "url": "https://www.researchgate.net/publication/400178402_Reinforcement_Learning_via_Self-Distillation"
          }
        ]
      },
      "I've completed the web search on your query about self-referential, self-scoring, and self-distillation methods for VLAs (vision-language-action models) with demonstration quality and pretrained features from 2025-2026. Here are the key findings:\n\n## Self-Distillation Methods (2025-2026)\n\nRecent work uses the current policy as a \"self-teacher\" that, rather than sampling a new response, re-evaluates the existing rollout after receiving rich feedback. This approach addresses a key limitation in reinforcement learning for language models.\n\n### Self-Distillation Fine-Tuning (SDFT)\n\nSelf-Distillation Fine-Tuning (SDFT) is a method that enables on-policy learning directly from demonstrations. When models learn from data generated by their current policy, they exhibit substantially reduced catastrophic forgetting compared to off-policy alternatives.\n\n### Self-Distillation for RL\n\nRecent self-distillation methods eliminate the need for external teachers by conditioning the student on privileged information to serve as its own teacher, where the privileged context can include reasoning traces, in-context demonstrations, or conciseness prompts.\n\n### VLA Applications\n\nSupervised fine-tuning (SFT) has become the de facto post-training strategy for large vision-language-action (VLA) models, but its reliance on costly human demonstrations limits scalability. A framework called Probe, Learn, Distill (PLD) improves VLAs through residual reinforcement learning and distribution-aware data collection.\n\nThe research shows that these self-distillation approaches enable more efficient learning from demonstrations while maintaining model capabilities across multiple tasks."
    ],
    "durationSeconds": 7.72237373500003
  },
  "sourceToolAssistantUUID": "2ee5335a-c7e6-4aba-958a-e062c85fa5c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-14T06:04:05.900Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LnYyxTS5BPmHoiTDUNXpsv`</summary>

```json
{
  "query": "VLA internal features probe reward estimation frozen backbone manipulation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b5148e2-380f-46db-ace6-c4854a67c220",
  "isSidechain": false,
  "requestId": "req_011Cb1xQ5TRmPghpBnwC6P3h",
  "type": "assistant",
  "uuid": "7e8a1fda-603f-4b2f-97c5-9f8c12343c9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0146bd5t5wmrG3Z4rCGvG4PA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3601,
      "cache_read_input_tokens": 49372,
      "output_tokens": 64,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3601,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 64,
          "cache_read_input_tokens": 49372,
          "cache_creation_input_tokens": 3601,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3601
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

_source line 92 · 2026-05-14T06:04:12.194Z_

<details><summary>↩ Tool result · `toolu_01LnYyxTS5BPmHoiTDUNXpsv`</summary>

```text
Web search results for query: "VLA internal features probe reward estimation frozen backbone manipulation 2025"

Links: [{"title":"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | OpenReview","url":"https://openreview.net/forum?id=eUGoqrZ6Ea"},{"title":"Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models","url":"https://arxiv.org/html/2603.19183v1"},{"title":"VLA-ADAPTER: AN EFFECTIVE PARADIGM FOR TINY-SCALE VISION-LANGUAGE-ACTION MODEL","url":"https://arxiv.org/pdf/2509.09372"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"Exploring the Robustness of Vision-Language-Action Models against Sensor Attacks | Proceedings of the 2025 Workshop on Large AI Systems and Models with Privacy and Security Analysis","url":"https://dl.acm.org/doi/10.1145/3733800.3763262"},{"title":"Vision Language Action Models (VLA) & Policies for Robots","url":"https://learnopencv.com/vision-language-action-models-lerobot-policy/"},{"title":"SimVLA: A Simple VLA Baseline for Robotic Manipulation","url":"https://arxiv.org/html/2602.18224"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"2025-9-18 ThinkAct: Vision-Language-Action Reasoning via","url":"https://jasper0314-huang.github.io/assets/pdf/neurips25_thinkact.pdf"}]

I found several highly relevant research papers and resources related to your search query about VLA internal features, probing, reward estimation, and frozen backbone manipulation:

## Key Research Areas Found:

**1. Sparse Autoencoders for Probing VLA Internal Representations**

Research applies mechanistic interpretability techniques to understand VLA models' inner workings, training Sparse Autoencoders (SAEs) on hidden layer activations to probe internal representations. SAEs learn a sparse dictionary with features serving as an interpretable basis for computation, where most extracted features correspond to memorized sequences, though some represent interpretable, general, and steerable motion primitives and semantic properties.

**2. Frozen Backbone Approaches**

One framework freezes the VLA backbone and trains lightweight residual actors via off-policy RL, with these specialists probing failure regions of the generalist policy. Additionally, VLA-Adapter performs strongly even when the backbone is frozen, attributed to features being already adapted to the action domain after robotic pretraining.

**3. Reward Estimation and RL for VLAs**

ThinkAct is a dual-system framework that bridges high-level reasoning with low-level action execution via reinforced visual latent planning, training a multimodal LLM to generate embodied reasoning plans guided by reinforcing action-aligned visual rewards based on goal completion and trajectory consistency.

These developments represent important advances in understanding and improving VLA models for robotic manipulation in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e8a1fda-603f-4b2f-97c5-9f8c12343c9e",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "ea55275c-92fe-4cc9-89b4-38edb697658e",
  "toolUseResult": {
    "query": "VLA internal features probe reward estimation frozen backbone manipulation 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JfFnPhosUFaeDe3V6Nz7Xc",
        "content": [
          {
            "title": "Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | OpenReview",
            "url": "https://openreview.net/forum?id=eUGoqrZ6Ea"
          },
          {
            "title": "Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models",
            "url": "https://arxiv.org/html/2603.19183v1"
          },
          {
            "title": "VLA-ADAPTER: AN EFFECTIVE PARADIGM FOR TINY-SCALE VISION-LANGUAGE-ACTION MODEL",
            "url": "https://arxiv.org/pdf/2509.09372"
          },
          {
            "title": "Vision-language-action model - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Vision-language-action_model"
          },
          {
            "title": "Pure Vision Language Action (VLA) Models: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2509.19012v1"
          },
          {
            "title": "Exploring the Robustness of Vision-Language-Action Models against Sensor Attacks | Proceedings of the 2025 Workshop on Large AI Systems and Models with Privacy and Security Analysis",
            "url": "https://dl.acm.org/doi/10.1145/3733800.3763262"
          },
          {
            "title": "Vision Language Action Models (VLA) & Policies for Robots",
            "url": "https://learnopencv.com/vision-language-action-models-lerobot-policy/"
          },
          {
            "title": "SimVLA: A Simple VLA Baseline for Robotic Manipulation",
            "url": "https://arxiv.org/html/2602.18224"
          },
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          },
          {
            "title": "2025-9-18 ThinkAct: Vision-Language-Action Reasoning via",
            "url": "https://jasper0314-huang.github.io/assets/pdf/neurips25_thinkact.pdf"
          }
        ]
      },
      "I found several highly relevant research papers and resources related to your search query about VLA internal features, probing, reward estimation, and frozen backbone manipulation:\n\n## Key Research Areas Found:\n\n**1. Sparse Autoencoders for Probing VLA Internal Representations**\n\nResearch applies mechanistic interpretability techniques to understand VLA models' inner workings, training Sparse Autoencoders (SAEs) on hidden layer activations to probe internal representations. SAEs learn a sparse dictionary with features serving as an interpretable basis for computation, where most extracted features correspond to memorized sequences, though some represent interpretable, general, and steerable motion primitives and semantic properties.\n\n**2. Frozen Backbone Approaches**\n\nOne framework freezes the VLA backbone and trains lightweight residual actors via off-policy RL, with these specialists probing failure regions of the generalist policy. Additionally, VLA-Adapter performs strongly even when the backbone is frozen, attributed to features being already adapted to the action domain after robotic pretraining.\n\n**3. Reward Estimation and RL for VLAs**\n\nThinkAct is a dual-system framework that bridges high-level reasoning with low-level action execution via reinforced visual latent planning, training a multimodal LLM to generate embodied reasoning plans guided by reinforcing action-aligned visual rewards based on goal completion and trajectory consistency.\n\nThese developments represent important advances in understanding and improving VLA models for robotic manipulation in 2025."
    ],
    "durationSeconds": 6.290705967000045
  },
  "sourceToolAssistantUUID": "7e8a1fda-603f-4b2f-97c5-9f8c12343c9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-14T06:04:16.824Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015rX5toV7p8ukZ3tWfUKKo2`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.19183",
  "prompt": "Extract the key findings about Sparse Autoencoders on VLA models: (1) What VLA model was studied? (2) Which layers were probed? (3) What types of features were discovered? (4) Were any features useful for steering or quality estimation? (5) Key conclusions about VLA internal representations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea55275c-92fe-4cc9-89b4-38edb697658e",
  "isSidechain": false,
  "requestId": "req_011Cb1xQkzwoJuC4MffT4TG5",
  "type": "assistant",
  "uuid": "1239359f-025a-42d1-a17d-955535542ded",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FR5k1jArcRuKE7U6jmRhuW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 967,
      "cache_read_input_tokens": 52973,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 967,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 151,
          "cache_read_input_tokens": 52973,
          "cache_creation_input_tokens": 967,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 967
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

_source line 94 · 2026-05-14T06:04:23.087Z_

<details><summary>↩ Tool result · `toolu_015rX5toV7p8ukZ3tWfUKKo2`</summary>

```text
# Key Findings on Sparse Autoencoders in VLA Models

**(1) VLA Model Studied:**
The paper does not specify a particular VLA model name. It references general "Vision-Language-Action (VLA) models" for robot manipulation tasks and validates findings using the "LIBERO benchmark."

**(2) Layers Probed:**
The abstract does not identify specific layer numbers. The authors trained SAEs on "hidden layer activations of the VLA" without specifying which layers were examined.

**(3) Feature Types Discovered:**
Two primary categories emerged: memorized sequences from training demonstrations dominated the learned features, but importantly, some features represented "interpretable, general, and steerable motion primitives and semantic properties."

**(4) Steering and Quality:**
Yes—steering experiments proved productive. The researchers demonstrated that "individual SAE features causally influence robot behavior" and that steering general features produced "behaviors consistent with their semantic meaning" applicable across multiple tasks and scenes.

**(5) Key Conclusions:**
The work provides "the first mechanistic evidence that VLAs can learn generalizable features across tasks and scenes." Critically, supervised fine-tuning on small datasets amplified memorization, whereas training on larger, diverse datasets (like DROID) or knowledge insulation promoted more generalizable features.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1239359f-025a-42d1-a17d-955535542ded",
  "isSidechain": false,
  "promptId": "ca49de66-8aea-4111-9fb0-a16f082c081c",
  "type": "user",
  "uuid": "483b995e-13ba-4942-ba75-9d26a962890a",
  "toolUseResult": {
    "bytes": 48392,
    "code": 200,
    "codeText": "OK",
    "result": "# Key Findings on Sparse Autoencoders in VLA Models\n\n**(1) VLA Model Studied:**\nThe paper does not specify a particular VLA model name. It references general \"Vision-Language-Action (VLA) models\" for robot manipulation tasks and validates findings using the \"LIBERO benchmark.\"\n\n**(2) Layers Probed:**\nThe abstract does not identify specific layer numbers. The authors trained SAEs on \"hidden layer activations of the VLA\" without specifying which layers were examined.\n\n**(3) Feature Types Discovered:**\nTwo primary categories emerged: memorized sequences from training demonstrations dominated the learned features, but importantly, some features represented \"interpretable, general, and steerable motion primitives and semantic properties.\"\n\n**(4) Steering and Quality:**\nYes—steering experiments proved productive. The researchers demonstrated that \"individual SAE features causally influence robot behavior\" and that steering general features produced \"behaviors consistent with their semantic meaning\" applicable across multiple tasks and scenes.\n\n**(5) Key Conclusions:**\nThe work provides \"the first mechanistic evidence that VLAs can learn generalizable features across tasks and scenes.\" Critically, supervised fine-tuning on small datasets amplified memorization, whereas training on larger, diverse datasets (like DROID) or knowledge insulation promoted more generalizable features.",
    "durationMs": 6256,
    "url": "https://arxiv.org/abs/2603.19183"
  },
  "sourceToolAssistantUUID": "1239359f-025a-42d1-a17d-955535542ded",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 95 · 2026-05-14T06:05:05.387Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a very comprehensive picture. Let me think deeply about the revision:

**Core questions:**

1. **Is the core problem still valid?** Yes — improving VLA fine-tuning from noisy demonstrations without environment interaction is a real and important problem. GR-RL, SARM, ARFM, and CO-RFT all address this, confirming the problem is relevant. But the space is getting crowded.

2. **What's the remaining gap?** 
   - GR-RL: Requires separate distributional critic training + online RL in Stage 3
   - SARM/RA-BC: Requires natural language subtask annotations for reward model training
   - ARFM: Requires hand-designed 13-component dense rewards
   - CO-RFT: Focuses on small demo sets (30-60), uses full parameter fine-tuning + separate critic expert
   - TOPReward: Uses external VLM for scoring (inference cost, not integrated with VLA)
   - VLAC: Requires massive training data (3000h+)
   
   **The gap**: No existing method leverages the VLA's own pretrained representations for self-referential, annotation-free demonstration quality scoring to guide reward-weighted fine-tuning — they all require either external models, manual annotations, hand-crafted rewards, or massive data.

Now I'm thinking about whether the VLA can score itself. The SAE paper demonstrates that VLA features encode interpretable task-relevant information, and VLA-Adapter shows frozen features already adapt to action prediction. Combined with TOPReward's finding that VLM token probabilities can estimate progress zero-shot, this suggests the VLA's internal representations should contain a usable progress signal.

For addressing AFBC's oscillation problem, I'd avoid bootstrapped Q-learning on limited demonstrations entirely. Instead, I'd train a lightweight probe on frozen VLA features to directly estimate task progress using hindsight labels from trajectory completion — the VLA's richer feature space should capture far more signal than the simple state representations AFBC relied on.

To stabilize this, I'd leverage trajectory-level ranking as a coarse but reliable signal alongside timestep-level estimates, giving the multi-granularity approach robustness even when individual timestep predictions are noisy.

For CWBC, the solution is straightforward: skip conditioning altogether and use reward weighting instead, which sidesteps the OOD extrapolation problem entirely and aligns with the original filtering/re-weighting request.

Differentiating from A2PO is clear — they use CVAE conditioning in D4RL's MuJoCo domain, while this approach uses reward-weighted BC in the VLA domain with self-referential scoring, making them fundamentally different in architecture, domain, and mechanism.

Now I'm reframing the core idea: keeping the problem of improving VLA fine-tuning from noisy offline demonstrations but completely shifting from a conditioning-based approach to self-referential scoring combined with reward-weighted fine-tuning.

The new framing is "Self-Scored Demonstration Distillation for Offline VLA Fine-Tuning" — capturing the self-referential scoring and distillation aspects.

For resource planning, I'm estimating SmolVLA at 450M parameters as the primary validation model to keep costs down, with the progress probe training on frozen features taking roughly 10-20 hours on H100, SmolVLA LoRA fine-tuning across the LIBERO suites around 80-160 hours total, and OpenVLA-7B validation on a subset adding another 30-50 hours, plus additional time for ablations.

Tightening the budget to stay under 200 H100-hours, I'm breaking down the plan more carefully: progress probe training at 5 hours, SmolVLA LoRA fine-tuning at 60 hours across all suites, evaluation at 10 hours, key ablations at 40 hours, OpenVLA-7B validation on the hardest suite at 30 hours, and noise injection experiments at 30 hours, bringing the total to around 175 hours.

Now I'm moving forward with finalizing the JSON structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "483b995e-13ba-4942-ba75-9d26a962890a",
  "isSidechain": false,
  "requestId": "req_011Cb1xRZa8ni4rRTBJL6Z41",
  "type": "assistant",
  "uuid": "f56231c6-60d1-4c68-a488-0880fc59fb8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WLUCHQDAKBznSkYihyvisM",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 451,
      "cache_read_input_tokens": 53940,
      "output_tokens": 5893,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 451,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5893,
          "cache_read_input_tokens": 53940,
          "cache_creation_input_tokens": 451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 451
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

_source line 96 · 2026-05-14T06:06:44.411Z_

Now I have comprehensive understanding of the landscape. Let me synthesize the findings and produce the revised idea. The research reveals that:

1. **AFBC oscillation is real** — IQL-style bootstrapped Q-learning on demo-only data produces near-zero advantages
2. **CWBC kills conditioning** — conditioning on OOD high-advantage degrades performance
3. **GR-RL** uses distributional Q-values + filtering + online RL (requires separate critic + online stage)
4. **SARM/RA-BC** uses progress-delta weighting but needs natural language subtask annotations
5. **TOPReward** (Feb 2026) achieves 0.947 VOC for zero-shot progress estimation via VLM token probabilities
6. **SAE probing** shows VLA features contain interpretable, steerable, task-relevant features
7. **SmolVLA** (450M) enables compute-efficient experiments

This calls for a **major revision**: pivot from conditioning to self-referential reward-weighted fine-tuning.

```json
{
  "title": "VLA-SSD: Self-Scored Demonstration Distillation for Offline VLA Fine-Tuning",
  "change_type": "major",
  "core_problem": "Scaling VLA fine-tuning requires learning from large, heterogeneous demonstration datasets that inevitably contain noisy, suboptimal, or inconsistent timesteps (hesitations, corrections, imprecise grasps). Current approaches to handling noisy demonstrations either require online robot interaction (RECAP/π*0.6, GR-RL Stage 3, SimpleVLA-RL), hand-designed dense reward functions (ARFM's 13-component reward), natural language subtask annotations (SARM/RA-BC), or external VLM inference (GVL, TOPReward). Can a VLA score its own training data quality using knowledge already embedded in its pretrained representations — enabling annotation-free, environment-free demonstration distillation?",
  "opportunity": "VLA models pretrained on large-scale robot data (Open X-Embodiment, DROID) develop rich intermediate representations that encode task semantics, progress dynamics, and action-relevant features — as recently evidenced by SAE probing studies showing VLAs learn interpretable motion primitives and semantic properties (arXiv 2603.19183). Meanwhile, SARM/RA-BC proved that progress-delta reward weighting dramatically improves VLA fine-tuning (8% → 83% on T-shirt folding with π0), and GR-RL showed Q-value-based demonstration filtering improves success rates by 16% absolute. But SARM requires stage-level natural language annotations, GR-RL requires training a distributional critic network and an online RL stage, and ARFM requires hand-designed 13-component dense rewards. The opportunity is to close this loop: use the VLA's own frozen pretrained features as a self-referential progress estimator, eliminating external dependencies while achieving comparable or superior demonstration distillation quality. This is feasible because VLA features are already adapted to the action domain through pretraining — a finding confirmed by VLA-Adapter work showing frozen VLA backbones perform strongly even without fine-tuning.",
  "landscape": "The VLA demonstration quality improvement space has three active approaches, each with limitations: (1) **Filtering**: GR-RL (ByteDance, Dec 2025) trains a distributional TD3+BC critic to score transitions, filters those with negative progress delta, then applies symmetry augmentation and online RL — achieving 83.3% on shoe-lacing. Requires separate critic training, hindsight replay engineering, and online RL in Stage 3. (2) **Reward-weighted BC**: SARM/RA-BC (arXiv 2509.25358) trains a stage-aware reward model (CLIP encoder + 8-layer transformer) using natural language subtask annotations, then weights π0's BC loss by progress delta — boosting T-shirt folding from 8% to 83%. Requires per-task subtask annotations. ARFM (AAAI 2026) does adaptive advantage-weighted flow matching for VLA post-training but requires hand-designed 13-component dense rewards and Leave-One-Out advantage estimation. (3) **External VLM scoring**: GVL (ICLR 2025) uses VLM temporal ordering for zero-shot value estimation; TOPReward (Feb 2026) extracts VLM token probabilities as progress signals achieving 0.947 VOC. Both require running a separate VLM at inference time and struggle with open-source models (GVL collapses on non-proprietary VLMs). (4) **Offline RL for VLAs**: CO-RFT (Aug 2025) does chunked offline Q-learning from 30-60 demos; ConRFT (Feb 2025) integrates BC + Q-learning with consistency objectives. These learn value functions but don't specifically target demonstration quality scoring. (5) **Advantage conditioning**: A2PO (NeurIPS 2024) conditions on advantage values via CVAE for D4RL locomotion; RECAP/π*0.6 (Nov 2025) conditions VLA training on online advantage estimates. CWBC (NeurIPS 2022 Workshop) showed conditioning on OOD high-return values degrades performance, requiring conservative regularization. **Gap**: No work uses the VLA's own pretrained representations as a self-referential, annotation-free demonstration quality scorer for reward-weighted fine-tuning — eliminating the need for external models, annotations, separate critic networks, or environment interaction.",
  "approach": "VLA-SSD is a three-stage offline demonstration distillation pipeline: **Stage 1 — Self-Referential Progress Probing**: Extract frozen intermediate features from the pretrained VLA (SmolVLA 450M or OpenVLA-OFT 7B) at a selected hidden layer for each demonstration timestep. Train a lightweight MLP probe (2-layer, ~1M params) on these frozen features to predict task progress ∈ [0,1], using hindsight completion labels: for successful trajectories, progress = t/T (normalized timestep); for failed trajectories, progress plateaus at the failure point. This avoids IQL-style bootstrapped Q-learning entirely, sidestepping the AFBC advantage oscillation problem — the probe learns a direct mapping from features to progress without Bellman backup. **Stage 2 — Hierarchical Quality Scoring**: Compute per-timestep progress deltas Δ_t = progress(t+1) − progress(t) and trajectory-level returns R_τ = Σ_t Δ_t. Combine into a hierarchical quality score: w_t = σ(α · rank(R_τ)/N + β · clip(Δ_t, μ−2σ, μ+2σ)), where trajectory-level ranking provides a robust coarse signal (immune to AFBC-style timestep-level oscillation) and timestep-level deltas provide fine-grained discrimination. The trajectory-level component stabilizes the weighting even when individual timestep estimates are noisy, since trajectory ordering is far more reliable than timestep ordering in demo-only data (confirmed by GR-RL's success with trajectory-level filtering). **Stage 3 — Reward-Weighted LoRA Fine-Tuning**: Fine-tune the VLA with LoRA using weighted BC loss: L = Σ_t w_t · ||a_t − π_θ(s_t)||², where w_t are the hierarchical quality scores from Stage 2. Unlike advantage conditioning (RECAP, A2PO), this uses standard BC with weighted loss, completely avoiding CWBC's OOD conditioning failure mode — there is no test-time conditioning token, so no distribution shift at inference. Unlike binary filtering (GR-RL), all timesteps contribute gradient signal proportional to their quality, avoiding the threshold sensitivity problem. **Key differentiators from closest competitors**: vs SARM/RA-BC — no natural language subtask annotations needed, uses VLA's own features instead of separate CLIP+transformer reward model; vs GR-RL — no separate distributional critic training, no online RL stage, soft weighting instead of binary filtering; vs ARFM — no hand-designed dense rewards, uses learned progress from VLA features; vs TOPReward/GVL — no external VLM inference, uses VLA's internal representations directly; vs A2PO/RECAP — reward weighting not conditioning, avoids CWBC's OOD problem entirely.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~180h H100 (progress probe training ~10h, SmolVLA LoRA fine-tuning across 4 LIBERO suites ~70h, noise injection experiments at 10/30/50% ~30h, OpenVLA-OFT 7B validation on LIBERO-Long ~25h, ablations ~30h, evaluation ~15h)",
      "gpu_utilization": "~35-45% — researcher iterates on progress probe architecture, analyzes quality score distributions, and designs noise injection protocol between GPU runs",
      "timeline": "2.5-4 months",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "$500-750 (H100 spot at ~$2.50-3.50/hr)"
    },
    "human_in_loop": {
      "gpu_hours": "~160h H100",
      "gpu_utilization": "~60-70% — agent autonomously queues probe training sweeps and LoRA fine-tuning runs, researcher reviews quality score distributions at check-ins",
      "timeline": "3-4 weeks",
      "team": "1 researcher, ~20-30min/day check-in to review progress probe convergence and quality score calibration",
      "claude_api_cost": "$100-200 (~1500-2500 turns at ~$0.08/turn)",
      "estimated_gpu_cost": "$400-600",
      "risk_note": "Progress probe may underfit if VLA features at selected layer lack sufficient progress discrimination — human judgment needed to select optimal layer via probing accuracy across layers"
    },
    "auto_research": {
      "gpu_hours": "~400h H100 (2x exploration: probe architecture sweep across VLA layers, hierarchical weighting hyperparameters α/β, noise injection ratios, SmolVLA + OpenVLA-OFT comparison)",
      "gpu_utilization": "~85-90% — agent runs 24/7, parallelizes probe training across layers and LoRA fine-tuning across LIBERO suites",
      "timeline": "4-7 days with 4 H100 GPUs",
      "team": "0 (setup + final review only)",
      "claude_api_cost": "$250-500 (~3000-6000 turns)",
      "estimated_gpu_cost": "$1,000-1,400",
      "speed_bottleneck": "GPU count — with 4 H100s, LIBERO suites parallelize across GPUs; with 1 GPU, sequential processing extends to 2-3 weeks",
      "risk_note": "Agent may over-explore probe architectures without recognizing when VLA features at a given layer are fundamentally uninformative for progress estimation"
    }
  },
  "target_venues": [
    "CoRL 2026 (abstract deadline May 25, full paper May 28, 2026)",
    "AAAI 2027 (~August 2026)",
    "ICLR 2027 (~October 2026)"
  ],
  "level": "solid",
  "key_references": [
    "GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation (ByteDance, Dec 2025)",
    "SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation (arXiv 2509.25358)",
    "π*0.6: a VLA That Learns From Experience (Physical Intelligence, Nov 2025)",
    "TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics (Feb 2026)",
    "Balancing Signal and Variance: Adaptive Offline RL Post-Training for VLA Flow Models [ARFM] (AAAI 2026)",
    "Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models (arXiv 2603.19183)",
    "A2PO: Towards Effective Offline Reinforcement Learning from an Advantage-aware Perspective (NeurIPS 2024)",
    "ConserWeightive Behavioral Cloning for Reliable Offline Reinforcement Learning [CWBC] (NeurIPS 2022 Workshop)",
    "A Closer Look at Advantage-Filtered Behavioral Cloning in High-Noise Datasets [AFBC] (arXiv 2021)",
    "Vision Language Models are In-Context Value Learners [GVL] (ICLR 2025)",
    "Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance [V-GPS] (CoRL 2024)",
    "CO-RFT: Efficient Fine-Tuning of VLA Models through Chunked Offline Reinforcement Learning (Aug 2025)",
    "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics (Jun 2025)",
    "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success [OpenVLA-OFT] (RSS 2025)",
    "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (CVPR 2026)",
    "VLAC: A Vision-Language-Action-Critic Model for Robotic Real-World RL (Sep 2025)",
    "SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning (ICLR 2026)"
  ],
  "description": "We propose VLA-SSD (Self-Scored Demonstration Distillation), a purely offline method for improving VLA fine-tuning on noisy demonstrations without environment interaction, external VLMs, subtask annotations, or hand-designed rewards. VLA-SSD exploits a key insight: pretrained VLA representations already encode task-relevant progress dynamics through large-scale pretraining — as evidenced by recent SAE probing studies showing VLAs learn interpretable motion primitives. The method has three stages: (1) Train a lightweight MLP progress probe on the VLA's frozen intermediate features using hindsight completion labels (progress = t/T for successful trajectories), completely avoiding IQL-style bootstrapped Q-learning and its known advantage oscillation failure mode (AFBC, 2021). (2) Compute hierarchical quality scores combining robust trajectory-level return ranking with fine-grained timestep-level progress deltas, providing reliability even when individual timestep estimates are noisy. (3) Fine-tune the VLA with LoRA using reward-weighted BC loss, where each timestep's gradient contribution is proportional to its quality score — using weighting rather than conditioning to avoid the OOD extrapolation failure identified by CWBC (NeurIPS 2022). Unlike GR-RL (ByteDance, 2025), VLA-SSD requires no separate distributional critic training and no online RL stage. Unlike SARM/RA-BC, it needs no natural language subtask annotations. Unlike ARFM (AAAI 2026), it requires no hand-designed dense rewards. Unlike TOPReward/GVL, it uses the VLA's own features rather than an external VLM. Evaluated on LIBERO (4 suites) and LIBERO-Plus (robustness analysis) with controlled noise injection at 10/30/50% noisy demonstration ratios, using SmolVLA (450M) as the primary model for compute efficiency and OpenVLA-OFT (7B) for scale validation. The robustness gap (clean vs. noisy performance degradation) is reported as a primary metric alongside absolute success rate, with LIBERO-Plus perturbation dimensions (camera, object layout, robot state) providing systematic robustness evaluation.",
  "project_name": "offline_adv_cond_vla",
  "source": "web_research"
}
```

**Summary of changes (major revision):**

1. **Pivoted from conditioning to reward-weighted BC** — directly addresses CWBC's OOD conditioning failure and realigns with user's request for filtering/re-weighting
2. **Replaced IQL advantage estimation with direct progress probing** — lightweight MLP on frozen VLA features avoids AFBC's bootstrapping-induced oscillation entirely
3. **Added hierarchical scoring** (trajectory-level ranking + timestep deltas) — robust even when individual timestep estimates are noisy
4. **Cited and differentiated from GR-RL, SARM/RA-BC, A2PO, TOPReward, VLAC** — positioned as the only annotation-free, self-referential approach requiring no external models
5. **Added SmolVLA (450M) as primary model** — cuts compute to ~180h H100, within the ≤200h budget
6. **Specified noise injection protocol** (10/30/50%) with LIBERO-Plus robustness evaluation and robustness gap metric

Sources:
- [GR-RL: Going Dexterous and Precise](https://arxiv.org/abs/2512.01801)
- [SARM: Stage-Aware Reward Modeling](https://arxiv.org/abs/2509.25358)
- [A2PO: Advantage-Aware Policy Optimization](https://arxiv.org/abs/2403.07262)
- [CWBC: ConserWeightive Behavioral Cloning](https://arxiv.org/abs/2210.05158)
- [AFBC: Advantage-Filtered Behavioral Cloning](https://arxiv.org/abs/2110.04698)
- [TOPReward: Token Probabilities as Zero-Shot Rewards](https://arxiv.org/abs/2602.19313)
- [SAE Probing of VLA Features](https://arxiv.org/abs/2603.19183)
- [SmolVLA](https://arxiv.org/abs/2506.01844)
- [LIBERO-Plus Robustness Benchmark](https://arxiv.org/abs/2510.13626)
- [ARFM / Adaptive Offline RL for VLA Flow Models](https://arxiv.org/abs/2509.04063)
- [CO-RFT: Chunked Offline RL for VLAs](https://arxiv.org/abs/2508.02219)
- [VLAC: Vision-Language-Action-Critic](https://arxiv.org/abs/2509.15937)
- [OpenVLA-OFT](https://arxiv.org/abs/2502.19645)
- [CoRL 2026 Deadlines](https://www.corl.org/contributions/call-for-papers)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f56231c6-60d1-4c68-a488-0880fc59fb8f",
  "isSidechain": false,
  "requestId": "req_011Cb1xRZa8ni4rRTBJL6Z41",
  "type": "assistant",
  "uuid": "3936ea59-ecca-412b-8689-01eb1bb9877e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WLUCHQDAKBznSkYihyvisM",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 451,
      "cache_read_input_tokens": 53940,
      "output_tokens": 5893,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 451,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5893,
          "cache_read_input_tokens": 53940,
          "cache_creation_input_tokens": 451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 451
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

_source line 97_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Offline Advantage Conditioning for VLA Noise Decomposition\",   \"core_p…",
  "leafUuid": "3936ea59-ecca-412b-8689-01eb1bb9877e",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80"
}
```

---

### Runtime record

_source line 98_

```json
{
  "type": "ai-title",
  "aiTitle": "Offline VLA fine-tuning via trajectory-level return ranking and conservative advantage weighting",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80"
}
```

---

### Runtime record

_source line 99_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Offline Advantage Conditioning for VLA Noise Decomposition\",   \"core_p…",
  "leafUuid": "3936ea59-ecca-412b-8689-01eb1bb9877e",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80"
}
```

---

### Runtime record

_source line 100_

```json
{
  "type": "ai-title",
  "aiTitle": "Offline VLA fine-tuning via trajectory-level return ranking and conservative advantage weighting",
  "sessionId": "59eecaa6-9288-4835-b915-a151c5a80b80"
}
```

---
