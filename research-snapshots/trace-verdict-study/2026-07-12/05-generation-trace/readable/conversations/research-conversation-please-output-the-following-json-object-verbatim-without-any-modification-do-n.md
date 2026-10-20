# Research conversation: Please output the following JSON object verbatim, without any modification. Do not add any commentary before or after. J

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 3
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ab54c303334e43304.jsonl`
- **Structured JSON:** [`61d2e025c2b8dc77fe26.json`](../../sessions/61/61d2e025c2b8dc77fe26.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

3 recorded events

### User

_source line 1 · 2026-05-10T06:48:50.576Z_

Please output the following JSON object verbatim, without any modification. Do not add any commentary before or after. Just output the raw JSON:

{
  "title": "Cross-Lingual Self-Consistency Pseudo-Reward for Multilingual Commonsense RL",
  "core_problem": "Reinforcement learning with verifiable rewards (GRPO, RLVR) has proven substantially superior to supervised fine-tuning for multilingual reasoning, but every existing multilingual RL setup trains exclusively on mathematical tasks. polyGRPO (Apr 2026) demonstrates that math-only RL does generalize to English commonsense (+4.9% on X-CSQA English), but no existing work closes the multilingual commonsense gap: polyGRPO reports no improvement on XCOPA or XStoryCloze in non-English languages, and the paper does not evaluate non-English X-CSQA. Two structural barriers prevent commonsense RL from advancing multilingually: (1) XCOPA and XStoryCloze are evaluation-only benchmarks with no training splits, so there is no standard multilingual commonsense training corpus; (2) commonsense tasks lack gold verifiable answers at training time, so existing reward formulations do not transfer from math.",
  "opportunity": "The polyGRPO finding is double-edged: math-RL generalizes to English commonsense but fails to close cross-lingual gaps, creating a precise and well-motivated target for commonsense-specific multilingual RL. Two observations make this tractable: (1) X-CSQA (Lin et al., ACL 2021) and X-CODAH provide English training sets with 8,888 and 8,476 items respectively—no multilingual RL paper has used these training splits; machine-translating them into the 11 XCOPA evaluation languages via NLLB-200 creates a clean multilingual commonsense training corpus that keeps XCOPA and XStoryCloze strictly as held-out evaluation benchmarks with zero contamination. (2) For multiple-choice commonsense items, cross-lingual answer agreement across K languages constitutes a pseudo-verifiable reward without gold labels: querying the model on the same item in K languages and measuring the fraction of language pairs agreeing on the same answer option is exact and cheap for option-labeled multiple-choice tasks. For 4-option items (X-CSQA, X-CODAH), random pairwise agreement is ~25%, making the signal substantially more discriminable than binary tasks and providing a cleaner training signal than the 50% random-agreement baseline in binary COPA items.",
  "landscape": "polyGRPO (arXiv 2604.21593, Apr 2026) achieves +4.9% on English X-CSQA from 18.1K math-only training examples—the only existing multilingual RL paper to quantify commonsense generalization—but reports no multilingual commonsense improvement and does not evaluate on XCOPA, XStoryCloze, or non-English X-CSQA. Think Natively (arXiv 2510.07300) and M-Thinker achieve near-100% language consistency on math-oriented multilingual benchmarks. TRIT (arXiv 2602.05940) and Beyond English-Centric Training (arXiv 2509.23657) train exclusively on mathematical data. CoVo (arXiv 2506.08745, Jun 2025) proposes self-rewarding RL via within-language reasoning path consistency: for a single language, K reasoning trajectories are generated per question, and rewards are assigned based on how consistently intermediate reasoning states converge toward their own final answers (high consistency) with minimal deviation toward other candidates (low volatility). CoVo evaluates on math and knowledge tasks (GSM8K, AIME, OlympiadBench, MMLU-Pro, GPQA, CommonsenseQA) with no multilingual component. This is the closest related mechanism to XLSC-GRPO but operates along a perpendicular axis: CoVo aggregates K same-language paths within one question-language pairing; XLSC-GRPO aggregates final answers across K languages for the same question. GRPO-CARE (arXiv 2506.16141, Jun 2025) implements a two-tiered consistency reward for multimodal video reasoning (within-language, not multilingual). MetaXCR (arXiv 2503.06531, Mar 2025) applies reinforcement-based meta-transfer to XCOPA at mBERT scale using supervised English source data—not pseudo-verifiable consistency rewards and not GRPO at LLM scale. X-CSQA and X-CODAH training splits (Lin et al., ACL 2021, inklab.usc.edu/XCSR) are unused by any multilingual RL paper, covering 16 languages with 8,888 and 8,476 English training items respectively. 'Why Multilingual Gaps Emerge' (arXiv 2510.27269) shows language understanding failure—not reasoning capability—drives cross-lingual gaps across task types, making language-consistent training directly causal to the documented performance deficit. MGSM-Pro (arXiv 2601.21225) extends math evaluation robustness but does not extend RL training to commonsense.",
  "approach": "We propose XLSC-GRPO (Cross-Lingual Self-Consistency GRPO), redesigned to address all execution constraints identified in reviewer feedback.\n\nTraining Data Construction: We machine-translate the English X-CSQA training set (8,888 items) and English X-CODAH training set (8,476 items) into the 11 XCOPA evaluation languages (et, ht, id, it, qu, sw, ta, th, tr, vi, zh) using NLLB-200 (Meta AI, 200-language open-source MT model), yielding ~190K translated items before quality filtering. The English COPA training set (400 items, public domain) is machine-translated into the same 11 languages as a domain-matched complement closer to the XCOPA evaluation distribution (4,400 items). Quality filtering via MT confidence scores and length-ratio checks reduces the effective corpus to ~110-130K high-confidence items. XCOPA (validation+test, 600 items/language) and XStoryCloze are held out exclusively for evaluation—no training items from these benchmarks are ever used.\n\nPseudo-Verifiable Reward: For each multiple-choice commonsense item, the model is queried in K=3 languages sampled per batch step (uniform over available translations). The reward equals the fraction of C(K,2)=3 language pairs agreeing on the same answer option index. For 4-option X-CSQA/X-CODAH items, random pairwise agreement is ~25%, providing a discriminable gradient signal above chance. A per-language confidence weight (softmax probability of chosen option) scales the per-pair reward to penalize low-confidence agreement and reduce reward hacking. Training warm-starts from a math-RL checkpoint (GRPO-pretrained on MGSM for 5K steps) to ensure the model achieves initial cross-lingual consistency before commonsense reward becomes the primary signal—directly addressing the reward discrimination concern for early training.\n\nModel: Qwen3-8B-Instruct (Alibaba, April 2025). Qwen3 dense variants exist at 0.6B, 1.7B, 4B, 8B, 14B, and 32B—there is no 7B variant in any Qwen3/Qwen3.5/Qwen3.6 release. Qwen3-8B supports 100+ languages (pre-trained on 36T tokens across 119 languages) and is the smallest Qwen3 dense model large enough to exhibit strong multilingual instruction following while fitting within the LoRA GRPO compute budget.\n\nTraining Configuration: GRPO with LoRA (r=64, alpha=128) on 2×H100 per ablation run; G=8 completions per prompt; batch size 8 questions (each queried in K=3 languages); vLLM for generation. Estimated ~35h per training ablation at this configuration.\n\n4-Ablation Design within the 200h hard constraint:\n- A1 — Math-RL baseline (~30h): MGSM-only GRPO on Qwen3-8B-Instruct; evaluate on XCOPA, XStoryCloze, X-CSQA multilingual to establish the polyGRPO-style transfer ceiling. This ablation directly answers whether dedicated multilingual commonsense training adds value over math-RL generalization.\n- A2 — XLSC-GRPO full (~35h): X-CSQA+X-CODAH+COPA MT training data with cross-lingual agreement reward, K=3, warm-started from math-RL checkpoint.\n- A3 — Math+Commonsense mixed (~35h): joint MGSM + XLSC-GRPO training to study whether cross-task mixing improves commonsense without degrading math performance.\n- A4 — Reward formulation ablation (~35h): exact-match pairwise agreement (A2 setup) vs. NLI-similarity reward (using mDeBERTa-v3 as cross-lingual NLI scorer for answer equivalence).\n- Evaluation across all ablations on XCOPA (11 langs × 500 test items), XStoryCloze (9 langs), X-CSQA multilingual dev (~30h).\n- Total: ~165h, within the 200h constraint.\n\nPrimary Claims: (i) XLSC-GRPO (A2) outperforms math-RL baseline (A1) on multilingual XCOPA and XStoryCloze, demonstrating dedicated commonsense RL adds value beyond polyGRPO-style generalization; (ii) mixed training (A3) retains math performance while improving multilingual commonsense; (iii) the gap between exact-match and NLI-similarity reward (A4) quantifies how much semantic flexibility in the reward function matters for multiple-choice commonsense; (iv) low-resource XCOPA languages (qu, ht) benefit disproportionately from within-training-language consistency signals.",
  "resource_estimate": {
    "constraint": "200 H100-hours maximum (hard user constraint; all three modes stay under this ceiling)",
    "manual": {
      "gpu_hours": "~165h H100",
      "gpu_utilization": "55-70%; human-directed scheduling with idle time between ablation runs",
      "timeline": "6-8 weeks",
      "team": "2 researchers (1 NLP + 1 ML engineer)",
      "estimated_gpu_cost": "~$415-575 at $2.50-3.50/H100-hr (Lambda Labs / RunPod 2026 rates)"
    },
    "human_in_loop": {
      "gpu_hours": "~180h H100",
      "gpu_utilization": "75-80%; agent queues ablations and monitors training curves; human approves reward formulation changes and interprets convergence plots",
      "timeline": "3-4 weeks",
      "team": "1 researcher, ~30 min/day check-in",
      "claude_api_cost": "$350-500 (~3,000-4,500 turns at Claude Opus 4.7 rates)",
      "estimated_gpu_cost": "~$450-630 at $2.50-3.50/H100-hr",
      "risk_note": "Reward discrimination risk for binary-choice COPA-derived items (50% random pairwise agreement); mitigated by: (1) using 4-option X-CSQA/X-CODAH as primary training data (25% random baseline), (2) warm-starting from math-RL checkpoint to establish initial language consistency, (3) confidence-weighted reward scaling"
    },
    "auto_research": {
      "gpu_hours": "~190h H100 (adds K sensitivity sweep K in {2,3,5} and language sampling strategy ablation within the same 200h ceiling)",
      "gpu_utilization": "90-95%; next experiment queued automatically upon completion, near-zero idle",
      "timeline": "5-8 days with 4 concurrent H100s",
      "team": "0 (initial setup only)",
      "claude_api_cost": "$600-900 (~5,000-8,000 turns for experiment orchestration, result parsing, and draft writing)",
      "estimated_gpu_cost": "~$475-665 at $2.50-3.50/H100-hr",
      "risk_note": "Without human oversight, language collapse (model outputs same tokens regardless of query language) may not be caught early; requires automatic per-language output entropy monitoring hook in the training loop"
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR August 2026 cycle; expected deadline approximately August 15-25, 2026; 3-4 months of run time available from May 2026 — the previously listed ARR May 2026 deadline of May 25 is infeasible given today's date of May 10, 2026)",
    "ICLR 2027 (expected submission window September-October 2026; not yet formally announced — speculative target, clearly labeled as such)"
  ],
  "level": "solid",
  "key_references": [
    "Think Natively: Unlocking Multilingual Reasoning with Consistency-Enhanced Reinforcement Learning (arXiv 2510.07300, 2025)",
    "Language as a Latent Variable for Reasoning Optimization [polyGRPO] (arXiv 2604.21593, 2026)",
    "Self-Improving Multilingual Long Reasoning via Translation-Reasoning Integrated Training [TRIT] (arXiv 2602.05940, 2026)",
    "Beyond English-Centric Training: How Reinforcement Learning Improves Cross-Lingual Reasoning in LLMs (arXiv 2509.23657, 2025)",
    "Why Do Multilingual Reasoning Gaps Emerge in Reasoning Language Models? (arXiv 2510.27269, 2025)",
    "XCOPA: A Multilingual Dataset for Causal Commonsense Reasoning (EMNLP 2020)",
    "Few-shot Learning with Multilingual Generative Language Models [XStoryCloze] (arXiv 2112.10668, EMNLP 2022)",
    "Common Sense Beyond English: Evaluating and Improving Multilingual Language Models for Commonsense Reasoning [X-CSQA/X-CODAH] (ACL 2021)",
    "MetaXCR: Reinforcement-Based Meta-Transfer Learning for Cross-Lingual Commonsense Reasoning (arXiv 2503.06531, 2025)",
    "Self-Consistency Improves Chain of Thought Reasoning in Language Models (ICLR 2023)",
    "Consistent Paths Lead to Truth: Self-Rewarding Reinforcement Learning for LLM Reasoning [CoVo] (arXiv 2506.08745, Jun 2025)",
    "No Language Left Behind: Scaling Human-Centered Machine Translation [NLLB-200] (arXiv 2207.04672, Meta AI 2022)"
  ],
  "description": "XLSC-GRPO addresses the untapped gap in multilingual RL: all existing GRPO-based multilingual training is restricted to mathematical tasks, and polyGRPO's +4.9% English commonsense gain (on X-CSQA English) does not extend to multilingual XCOPA or XStoryCloze. The core innovation is formalizing cross-lingual self-consistency as a pseudo-verifiable reward: querying the model on the same multiple-choice commonsense item in K=3 languages per batch step and rewarding the fraction of language pairs agreeing on the same answer option, requiring no gold labels. This revision incorporates four major changes from reviewer feedback: (1) Training data is now sourced from X-CSQA English training set (8,888 items) and X-CODAH (8,476 items) machine-translated via NLLB-200 into XCOPA's 11 evaluation languages, supplemented by COPA English training set (400 items) similarly translated — XCOPA and XStoryCloze are held out strictly for evaluation, eliminating benchmark contamination. (2) The model backbone is corrected to Qwen3-8B-Instruct (April 2025; 100+ languages; Qwen3.6-7B does not exist — the Qwen3 dense series has 8B as its sub-10B option). (3) Compute is redesigned around 4 LoRA GRPO ablations on 2xH100 totaling ~165h, within the 200h hard constraint. (4) CoVo (arXiv 2506.08745) is added as a key related work with explicit differentiation: CoVo measures within-language reasoning path consistency (K paths in one language), while XLSC-GRPO measures cross-lingual answer agreement (K languages for one question) — perpendicular axes addressing different problems. Ablation A1 (math-RL-only baseline on Qwen3-8B) directly tests whether dedicated commonsense RL outperforms polyGRPO-style transfer on XCOPA/XStoryCloze. Primary target: EMNLP 2026 via ARR August 2026 cycle.",
  "project_name": "xlsc_grpo_commonsense",
  "source": "web_research",
  "change_type": "major"
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "6f9e8fd4-c6ec-49d5-bf00-ee68123cd481",
  "agentId": "ab54c303334e43304",
  "type": "user",
  "uuid": "ae3978ae-72f6-45e3-ad7c-678d1c8c2f05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "da422424-82b6-400b-a084-e76255ff6006",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T06:48:50.581Z_

```json
{
  "parentUuid": "ae3978ae-72f6-45e3-ad7c-678d1c8c2f05",
  "isSidechain": true,
  "agentId": "ab54c303334e43304",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "d6b4c5e0-35b9-4a7c-a956-b12a95fb6c78",
  "timestamp": "2026-05-10T06:48:50.581Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "da422424-82b6-400b-a084-e76255ff6006",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T06:50:17.009Z_

{
  "title": "Cross-Lingual Self-Consistency Pseudo-Reward for Multilingual Commonsense RL",
  "core_problem": "Reinforcement learning with verifiable rewards (GRPO, RLVR) has proven substantially superior to supervised fine-tuning for multilingual reasoning, but every existing multilingual RL setup trains exclusively on mathematical tasks. polyGRPO (Apr 2026) demonstrates that math-only RL does generalize to English commonsense (+4.9% on X-CSQA English), but no existing work closes the multilingual commonsense gap: polyGRPO reports no improvement on XCOPA or XStoryCloze in non-English languages, and the paper does not evaluate non-English X-CSQA. Two structural barriers prevent commonsense RL from advancing multilingually: (1) XCOPA and XStoryCloze are evaluation-only benchmarks with no training splits, so there is no standard multilingual commonsense training corpus; (2) commonsense tasks lack gold verifiable answers at training time, so existing reward formulations do not transfer from math.",
  "opportunity": "The polyGRPO finding is double-edged: math-RL generalizes to English commonsense but fails to close cross-lingual gaps, creating a precise and well-motivated target for commonsense-specific multilingual RL. Two observations make this tractable: (1) X-CSQA (Lin et al., ACL 2021) and X-CODAH provide English training sets with 8,888 and 8,476 items respectively—no multilingual RL paper has used these training splits; machine-translating them into the 11 XCOPA evaluation languages via NLLB-200 creates a clean multilingual commonsense training corpus that keeps XCOPA and XStoryCloze strictly as held-out evaluation benchmarks with zero contamination. (2) For multiple-choice commonsense items, cross-lingual answer agreement across K languages constitutes a pseudo-verifiable reward without gold labels: querying the model on the same item in K languages and measuring the fraction of language pairs agreeing on the same answer option is exact and cheap for option-labeled multiple-choice tasks. For 4-option items (X-CSQA, X-CODAH), random pairwise agreement is ~25%, making the signal substantially more discriminable than binary tasks and providing a cleaner training signal than the 50% random-agreement baseline in binary COPA items.",
  "landscape": "polyGRPO (arXiv 2604.21593, Apr 2026) achieves +4.9% on English X-CSQA from 18.1K math-only training examples—the only existing multilingual RL paper to quantify commonsense generalization—but reports no multilingual commonsense improvement and does not evaluate on XCOPA, XStoryCloze, or non-English X-CSQA. Think Natively (arXiv 2510.07300) and M-Thinker achieve near-100% language consistency on math-oriented multilingual benchmarks. TRIT (arXiv 2602.05940) and Beyond English-Centric Training (arXiv 2509.23657) train exclusively on mathematical data. CoVo (arXiv 2506.08745, Jun 2025) proposes self-rewarding RL via within-language reasoning path consistency: for a single language, K reasoning trajectories are generated per question, and rewards are assigned based on how consistently intermediate reasoning states converge toward their own final answers (high consistency) with minimal deviation toward other candidates (low volatility). CoVo evaluates on math and knowledge tasks (GSM8K, AIME, OlympiadBench, MMLU-Pro, GPQA, CommonsenseQA) with no multilingual component. This is the closest related mechanism to XLSC-GRPO but operates along a perpendicular axis: CoVo aggregates K same-language paths within one question-language pairing; XLSC-GRPO aggregates final answers across K languages for the same question. GRPO-CARE (arXiv 2506.16141, Jun 2025) implements a two-tiered consistency reward for multimodal video reasoning (within-language, not multilingual). MetaXCR (arXiv 2503.06531, Mar 2025) applies reinforcement-based meta-transfer to XCOPA at mBERT scale using supervised English source data—not pseudo-verifiable consistency rewards and not GRPO at LLM scale. X-CSQA and X-CODAH training splits (Lin et al., ACL 2021, inklab.usc.edu/XCSR) are unused by any multilingual RL paper, covering 16 languages with 8,888 and 8,476 English training items respectively. 'Why Multilingual Gaps Emerge' (arXiv 2510.27269) shows language understanding failure—not reasoning capability—drives cross-lingual gaps across task types, making language-consistent training directly causal to the documented performance deficit. MGSM-Pro (arXiv 2601.21225) extends math evaluation robustness but does not extend RL training to commonsense.",
  "approach": "We propose XLSC-GRPO (Cross-Lingual Self-Consistency GRPO), redesigned to address all execution constraints identified in reviewer feedback.\n\nTraining Data Construction: We machine-translate the English X-CSQA training set (8,888 items) and English X-CODAH training set (8,476 items) into the 11 XCOPA evaluation languages (et, ht, id, it, qu, sw, ta, th, tr, vi, zh) using NLLB-200 (Meta AI, 200-language open-source MT model), yielding ~190K translated items before quality filtering. The English COPA training set (400 items, public domain) is machine-translated into the same 11 languages as a domain-matched complement closer to the XCOPA evaluation distribution (4,400 items). Quality filtering via MT confidence scores and length-ratio checks reduces the effective corpus to ~110-130K high-confidence items. XCOPA (validation+test, 600 items/language) and XStoryCloze are held out exclusively for evaluation—no training items from these benchmarks are ever used.\n\nPseudo-Verifiable Reward: For each multiple-choice commonsense item, the model is queried in K=3 languages sampled per batch step (uniform over available translations). The reward equals the fraction of C(K,2)=3 language pairs agreeing on the same answer option index. For 4-option X-CSQA/X-CODAH items, random pairwise agreement is ~25%, providing a discriminable gradient signal above chance. A per-language confidence weight (softmax probability of chosen option) scales the per-pair reward to penalize low-confidence agreement and reduce reward hacking. Training warm-starts from a math-RL checkpoint (GRPO-pretrained on MGSM for 5K steps) to ensure the model achieves initial cross-lingual consistency before commonsense reward becomes the primary signal—directly addressing the reward discrimination concern for early training.\n\nModel: Qwen3-8B-Instruct (Alibaba, April 2025). Qwen3 dense variants exist at 0.6B, 1.7B, 4B, 8B, 14B, and 32B—there is no 7B variant in any Qwen3/Qwen3.5/Qwen3.6 release. Qwen3-8B supports 100+ languages (pre-trained on 36T tokens across 119 languages) and is the smallest Qwen3 dense model large enough to exhibit strong multilingual instruction following while fitting within the LoRA GRPO compute budget.\n\nTraining Configuration: GRPO with LoRA (r=64, alpha=128) on 2×H100 per ablation run; G=8 completions per prompt; batch size 8 questions (each queried in K=3 languages); vLLM for generation. Estimated ~35h per training ablation at this configuration.\n\n4-Ablation Design within the 200h hard constraint:\n- A1 — Math-RL baseline (~30h): MGSM-only GRPO on Qwen3-8B-Instruct; evaluate on XCOPA, XStoryCloze, X-CSQA multilingual to establish the polyGRPO-style transfer ceiling. This ablation directly answers whether dedicated multilingual commonsense training adds value over math-RL generalization.\n- A2 — XLSC-GRPO full (~35h): X-CSQA+X-CODAH+COPA MT training data with cross-lingual agreement reward, K=3, warm-started from math-RL checkpoint.\n- A3 — Math+Commonsense mixed (~35h): joint MGSM + XLSC-GRPO training to study whether cross-task mixing improves commonsense without degrading math performance.\n- A4 — Reward formulation ablation (~35h): exact-match pairwise agreement (A2 setup) vs. NLI-similarity reward (using mDeBERTa-v3 as cross-lingual NLI scorer for answer equivalence).\n- Evaluation across all ablations on XCOPA (11 langs × 500 test items), XStoryCloze (9 langs), X-CSQA multilingual dev (~30h).\n- Total: ~165h, within the 200h constraint.\n\nPrimary Claims: (i) XLSC-GRPO (A2) outperforms math-RL baseline (A1) on multilingual XCOPA and XStoryCloze, demonstrating dedicated commonsense RL adds value beyond polyGRPO-style generalization; (ii) mixed training (A3) retains math performance while improving multilingual commonsense; (iii) the gap between exact-match and NLI-similarity reward (A4) quantifies how much semantic flexibility in the reward function matters for multiple-choice commonsense; (iv) low-resource XCOPA languages (qu, ht) benefit disproportionately from within-training-language consistency signals.",
  "resource_estimate": {
    "constraint": "200 H100-hours maximum (hard user constraint; all three modes stay under this ceiling)",
    "manual": {
      "gpu_hours": "~165h H100",
      "gpu_utilization": "55-70%; human-directed scheduling with idle time between ablation runs",
      "timeline": "6-8 weeks",
      "team": "2 researchers (1 NLP + 1 ML engineer)",
      "estimated_gpu_cost": "~$415-575 at $2.50-3.50/H100-hr (Lambda Labs / RunPod 2026 rates)"
    },
    "human_in_loop": {
      "gpu_hours": "~180h H100",
      "gpu_utilization": "75-80%; agent queues ablations and monitors training curves; human approves reward formulation changes and interprets convergence plots",
      "timeline": "3-4 weeks",
      "team": "1 researcher, ~30 min/day check-in",
      "claude_api_cost": "$350-500 (~3,000-4,500 turns at Claude Opus 4.7 rates)",
      "estimated_gpu_cost": "~$450-630 at $2.50-3.50/H100-hr",
      "risk_note": "Reward discrimination risk for binary-choice COPA-derived items (50% random pairwise agreement); mitigated by: (1) using 4-option X-CSQA/X-CODAH as primary training data (25% random baseline), (2) warm-starting from math-RL checkpoint to establish initial language consistency, (3) confidence-weighted reward scaling"
    },
    "auto_research": {
      "gpu_hours": "~190h H100 (adds K sensitivity sweep K in {2,3,5} and language sampling strategy ablation within the same 200h ceiling)",
      "gpu_utilization": "90-95%; next experiment queued automatically upon completion, near-zero idle",
      "timeline": "5-8 days with 4 concurrent H100s",
      "team": "0 (initial setup only)",
      "claude_api_cost": "$600-900 (~5,000-8,000 turns for experiment orchestration, result parsing, and draft writing)",
      "estimated_gpu_cost": "~$475-665 at $2.50-3.50/H100-hr",
      "risk_note": "Without human oversight, language collapse (model outputs same tokens regardless of query language) may not be caught early; requires automatic per-language output entropy monitoring hook in the training loop"
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR August 2026 cycle; expected deadline approximately August 15-25, 2026; 3-4 months of run time available from May 2026 — the previously listed ARR May 2026 deadline of May 25 is infeasible given today's date of May 10, 2026)",
    "ICLR 2027 (expected submission window September-October 2026; not yet formally announced — speculative target, clearly labeled as such)"
  ],
  "level": "solid",
  "key_references": [
    "Think Natively: Unlocking Multilingual Reasoning with Consistency-Enhanced Reinforcement Learning (arXiv 2510.07300, 2025)",
    "Language as a Latent Variable for Reasoning Optimization [polyGRPO] (arXiv 2604.21593, 2026)",
    "Self-Improving Multilingual Long Reasoning via Translation-Reasoning Integrated Training [TRIT] (arXiv 2602.05940, 2026)",
    "Beyond English-Centric Training: How Reinforcement Learning Improves Cross-Lingual Reasoning in LLMs (arXiv 2509.23657, 2025)",
    "Why Do Multilingual Reasoning Gaps Emerge in Reasoning Language Models? (arXiv 2510.27269, 2025)",
    "XCOPA: A Multilingual Dataset for Causal Commonsense Reasoning (EMNLP 2020)",
    "Few-shot Learning with Multilingual Generative Language Models [XStoryCloze] (arXiv 2112.10668, EMNLP 2022)",
    "Common Sense Beyond English: Evaluating and Improving Multilingual Language Models for Commonsense Reasoning [X-CSQA/X-CODAH] (ACL 2021)",
    "MetaXCR: Reinforcement-Based Meta-Transfer Learning for Cross-Lingual Commonsense Reasoning (arXiv 2503.06531, 2025)",
    "Self-Consistency Improves Chain of Thought Reasoning in Language Models (ICLR 2023)",
    "Consistent Paths Lead to Truth: Self-Rewarding Reinforcement Learning for LLM Reasoning [CoVo] (arXiv 2506.08745, Jun 2025)",
    "No Language Left Behind: Scaling Human-Centered Machine Translation [NLLB-200] (arXiv 2207.04672, Meta AI 2022)"
  ],
  "description": "XLSC-GRPO addresses the untapped gap in multilingual RL: all existing GRPO-based multilingual training is restricted to mathematical tasks, and polyGRPO's +4.9% English commonsense gain (on X-CSQA English) does not extend to multilingual XCOPA or XStoryCloze. The core innovation is formalizing cross-lingual self-consistency as a pseudo-verifiable reward: querying the model on the same multiple-choice commonsense item in K=3 languages per batch step and rewarding the fraction of language pairs agreeing on the same answer option, requiring no gold labels. This revision incorporates four major changes from reviewer feedback: (1) Training data is now sourced from X-CSQA English training set (8,888 items) and X-CODAH (8,476 items) machine-translated via NLLB-200 into XCOPA's 11 evaluation languages, supplemented by COPA English training set (400 items) similarly translated — XCOPA and XStoryCloze are held out strictly for evaluation, eliminating benchmark contamination. (2) The model backbone is corrected to Qwen3-8B-Instruct (April 2025; 100+ languages; Qwen3.6-7B does not exist — the Qwen3 dense series has 8B as its sub-10B option). (3) Compute is redesigned around 4 LoRA GRPO ablations on 2xH100 totaling ~165h, within the 200h hard constraint. (4) CoVo (arXiv 2506.08745) is added as a key related work with explicit differentiation: CoVo measures within-language reasoning path consistency (K paths in one language), while XLSC-GRPO measures cross-lingual answer agreement (K languages for one question) — perpendicular axes addressing different problems. Ablation A1 (math-RL-only baseline on Qwen3-8B) directly tests whether dedicated commonsense RL outperforms polyGRPO-style transfer on XCOPA/XStoryCloze. Primary target: EMNLP 2026 via ARR August 2026 cycle.",
  "project_name": "xlsc_grpo_commonsense",
  "source": "web_research",
  "change_type": "major"
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6b4c5e0-35b9-4a7c-a956-b12a95fb6c78",
  "isSidechain": true,
  "agentId": "ab54c303334e43304",
  "requestId": "req_011CatSaXphLQrfW3jVymggj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f70765ba-8416-46e8-8cea-bf5807631b2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "da422424-82b6-400b-a084-e76255ff6006",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FtNB3zjbPazrLoCT5zZ1ys",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12890,
      "cache_read_input_tokens": 0,
      "output_tokens": 4232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12890
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4232,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 12890,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12890,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---
