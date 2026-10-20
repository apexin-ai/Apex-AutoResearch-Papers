# fix framing reviewer corrections — Part 2 of 2

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../fix-framing-reviewer-corrections.md) · [Structured JSON](../../../sessions/36/363cd7d243f187512321.json)

## Before a recorded user message

### Tool result

_source line 63 · 2026-05-13T07:39:09.175Z_

<details><summary>↩ Tool result · `toolu_01SSevcesapaSnpkbGMKLwev`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "afcc92da-531c-4b34-9e57-b508390f30b9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
    "oldString": "how_we_differ: \"They debias at decoding time for general fairness; we train the simulator via DPO to match target behavioral distributions\"",
    "newString": "how_we_differ: \"They debias at decoding time for general fairness; we document failure modes of training-time calibration (BCP+DPO), motivating alternative approaches like decoding-time methods\"",
    "originalFile": "papers:\n  # ============================================================\n  # DIRECT-COMPETITOR\n  # ============================================================\n  # 未找到直接竞品。没有现有工作专门做\"校准 LLM 用户模拟器的方言行为率偏差\"。\n  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。\n  # 这验证了 DemoCalib 的新颖性。\n\n  # ============================================================\n  # FOUNDATION\n  # ============================================================\n  - id: seshadri2026lost\n    title: \"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations\"\n    authors: \"Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant\"\n    venue: \"arXiv 2601.17087\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.17087\"\n    category: foundation\n    role: \"Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration\"\n    relevance: high\n    key_findings:\n      - \"Agent success rates vary up to 9pp across different user simulator LLMs\"\n      - \"AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers\"\n      - \"Simulated users introduce conversational artifacts absent from real human users\"\n      - \"Disparities compound significantly with age for AAVE speakers\"\n    how_we_differ: \"They document the problem; we document why both BCP and DPO calibration fail to close the gaps, providing a failure taxonomy\"\n\n  - id: yao2024taubench\n    title: \"tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\"\n    authors: \"Yao et al.\"\n    venue: \"arXiv 2406.12045\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2406.12045\"\n    category: foundation\n    role: \"The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric\"\n    relevance: high\n    key_findings:\n      - \"Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail\"\n      - \"Proposes pass^k metric measuring reliability over multiple trials\"\n      - \"User simulator is LLM-based, enabling behavioral modification\"\n    how_we_differ: \"We extend tau-bench by documenting systematic failure modes when calibrating the user simulator's dialect-specific behavioral rates\"\n\n  - id: liu2024agentbench\n    title: \"AgentBench: Evaluating LLMs as Agents\"\n    authors: \"Liu et al.\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2308.03688\"\n    category: foundation\n    role: \"Multi-environment agent benchmark; establishes evaluation methodology for LLM agents across 8 environments\"\n    relevance: medium\n    key_findings:\n      - \"Significant performance gap between commercial and open-source LLMs as agents\"\n      - \"Poor long-term reasoning and instruction following are main obstacles\"\n    how_we_differ: \"AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness\"\n\n  - id: wang2024mint\n    title: \"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\"\n    authors: \"Wang, Wang, Liu, Chen, Yuan, Peng, Ji\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.10691\"\n    category: foundation\n    role: \"Multi-turn agent evaluation benchmark; shows gap between single-turn and multi-turn performance\"\n    relevance: medium\n    key_findings:\n      - \"LLMs benefit 1-8% per turn from tools, 2-17% from language feedback\"\n      - \"Better single-turn performance does not guarantee better multi-turn performance\"\n      - \"SIFT and RLHF generally hurt multi-turn capabilities\"\n    how_we_differ: \"MINT uses GPT-4 simulated users without demographic variation; we investigate dialect-aware calibration and document its failure modes\"\n\n  # ============================================================\n  # METHOD-COMPONENT\n  # ============================================================\n  - id: rafailov2023dpo\n    title: \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\"\n    authors: \"Rafailov, Sharma, Mitchell, Manning, Ermon, Finn\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    url: \"https://arxiv.org/abs/2305.18290\"\n    category: method-component\n    role: \"Core algorithm for our DPO-based behavioral alignment; eliminates need for reward model training\"\n    relevance: high\n    key_findings:\n      - \"DPO directly optimizes policy from preference pairs without explicit reward model\"\n      - \"Computationally lightweight, stable alternative to PPO-based RLHF\"\n      - \"Exceeds PPO-based RLHF in controlling sentiment of generations\"\n    how_we_differ: \"We apply DPO to attempt dialect behavioral calibration and document its systematic failure modes including calibration reversal\"\n\n  - id: zhao2021calibrate\n    title: \"Calibrate Before Use: Improving Few-Shot Performance of Language Models\"\n    authors: \"Zhao, Wallace, Feng, Klein, Singh\"\n    venue: \"ICML 2021\"\n    year: 2021\n    url: \"https://arxiv.org/abs/2102.09690\"\n    category: method-component\n    role: \"Foundational calibration method for LLMs; contextual calibration corrects output distribution biases\"\n    relevance: medium\n    key_findings:\n      - \"Few-shot accuracy varies from near chance to near SOTA depending on prompt format\"\n      - \"Identified majority label bias, recency bias, common token bias\"\n      - \"Contextual calibration with content-free inputs improves accuracy up to 30%\"\n    how_we_differ: \"They calibrate classification outputs; we attempt to calibrate behavioral rates (question rate, politeness) in generation and document why it fails\"\n\n  - id: abdulhai2025consistent\n    title: \"Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning\"\n    authors: \"Abdulhai, Cheng, Clay, Althoff, Levine, Jaques\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2511.00222\"\n    category: method-component\n    role: \"Multi-turn RL for persona consistency; directly relevant to maintaining calibrated behavior across conversation turns\"\n    relevance: high\n    key_findings:\n      - \"Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue\"\n      - \"Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency\"\n      - \"Multi-turn RL reduces inconsistency by >55%\"\n    how_we_differ: \"They optimize persona consistency in general; we document failure modes when targeting dialect behavioral rate calibration\"\n\n  - id: naous2025flipping\n    title: \"Flipping the Dialogue: Training and Evaluating User Language Models\"\n    authors: \"Naous, Laban, Xu, Neville\"\n    venue: \"arXiv 2510.06552\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.06552\"\n    category: method-component\n    role: \"Purpose-built User LMs outperform repurposed assistant LMs as user simulators; validates need for specialized user models\"\n    relevance: high\n    key_findings:\n      - \"Better assistant LMs yield worse user simulators\"\n      - \"UserLM-8b provides more realistic user simulation\"\n      - \"GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation\"\n    how_we_differ: \"They train general User LMs; we document why calibrating user simulator behavioral rates for specific dialect groups fails\"\n\n  - id: li2025persona\n    title: \"LLM Generated Persona is a Promise with a Catch\"\n    authors: \"Li, Chen et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.16527\"\n    category: method-component\n    role: \"Documents systematic biases in LLM-generated personas; explains why naive persona prompting fails for demographic simulation\"\n    relevance: medium\n    key_findings:\n      - \"LLM-generated personas systematically drift toward socially desirable traits\"\n      - \"More LLM-generated content produces more left-leaning, less representative personas\"\n      - \"Bias exists in the persona creation step itself, not just model responses\"\n    how_we_differ: \"We document failure modes when directly injecting behavioral rate targets via BCP, including persona-like completion collapse\"\n\n  - id: wang2024alignment\n    title: \"A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More\"\n    authors: \"Wang, Bi, Pentyala et al.\"\n    venue: \"arXiv 2407.16216\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2407.16216\"\n    category: method-component\n    role: \"Survey unifying alignment methods under single policy gradient framework; reference for our DPO methodology\"\n    relevance: medium\n    key_findings:\n      - \"Unified policy gradient framework for pretraining, SFT, RLHF, RLVR\"\n      - \"DPO is stable and lightweight but sensitive to preference data quality\"\n      - \"Detailed comparison of PPO vs GRPO vs DPO implementation details\"\n    how_we_differ: \"Survey provides methodology reference; we apply DPO to user simulator dialect calibration and document its failure modes\"\n\n  # ============================================================\n  # EVALUATION\n  # ============================================================\n  - id: lin2025redial\n    title: \"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks\"\n    authors: \"Lin et al.\"\n    venue: \"ACL 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.11005\"\n    category: evaluation\n    role: \"First human-annotated SE-AAVE parallel benchmark (ReDial); quantifies LLM performance gaps on AAVE\"\n    relevance: high\n    key_findings:\n      - \"1.2K+ parallel SE-AAVE prompt pairs across reasoning tasks\"\n      - \"Almost all models show statistically significant performance drops on AAVE\"\n      - \"AAVE performance gaps arise from morphosyntactic features and conversational norms\"\n      - \"LLMs struggle more with AAVE than misspelled Standard English\"\n    how_we_differ: \"ReDial evaluates reasoning task performance; we evaluate behavioral rates in user simulation and document calibration failure modes\"\n\n  - id: faisal2024dialectbench\n    title: \"DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages\"\n    authors: \"Faisal et al.\"\n    venue: \"ACL 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2403.11009\"\n    category: evaluation\n    role: \"Large-scale multi-dialect NLP benchmark; documents performance disparities across 281 language varieties\"\n    relevance: medium\n    key_findings:\n      - \"10 NLP tasks, 281 varieties, 40 language clusters\"\n      - \"Substantial performance disparities between standard and non-standard varieties\"\n      - \"Performance gap widens with fine-tuning due to uneven data availability\"\n    how_we_differ: \"DialectBench evaluates NLP task performance; we document failure modes in behavioral calibration of user simulators\"\n\n  - id: gallegos2024bias\n    title: \"Bias and Fairness in Large Language Models: A Survey\"\n    authors: \"Gallegos, Rossi, Barrow et al.\"\n    venue: \"Computational Linguistics, Vol. 50(3)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.00770\"\n    category: evaluation\n    role: \"Comprehensive survey of LLM bias evaluation and mitigation; provides taxonomy of metrics and datasets\"\n    relevance: medium\n    key_findings:\n      - \"Taxonomy of bias metrics at embedding, probability, and generated text levels\"\n      - \"Mitigation methods categorized by intervention stage: pre/in/intra/post-processing\"\n      - \"Consolidated public datasets for bias evaluation\"\n    how_we_differ: \"Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)\"\n\n  - id: parrish2022bbq\n    title: \"BBQ: A Hand-Built Bias Benchmark for Question Answering\"\n    authors: \"Parrish et al.\"\n    venue: \"Findings of ACL 2022\"\n    year: 2022\n    url: \"https://aclanthology.org/2022.findings-acl.165/\"\n    category: evaluation\n    role: \"Established bias benchmark for QA; evaluates social biases across multiple demographic categories\"\n    relevance: low\n    key_findings:\n      - \"58,492 unique examples across multiple bias categories\"\n      - \"Evaluates both individual and intersectional biases\"\n      - \"Standard benchmark for LLM bias evaluation\"\n    how_we_differ: \"BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation\"\n\n  - id: haq2026dialect\n    title: \"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles\"\n    authors: \"Haq, Saldias\"\n    venue: \"arXiv 2604.21152\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21152\"\n    category: evaluation\n    role: \"Closest to direct competitor; quantifies how dialect cues vs explicit identity trigger differential LLM behavior\"\n    relevance: high\n    key_findings:\n      - \"Dialect cues trigger 'dialect jailbreak' reducing refusal probability to near zero\"\n      - \"AAVE/Singlish users receive less sanitized content than SAE users\"\n      - \"Safety alignment is brittle, over-indexed on explicit keywords\"\n      - \"24,000+ responses analyzed across two LLMs\"\n    how_we_differ: \"They characterize the bias mechanism (implicit vs explicit); we document why calibration methods fail to correct behavioral rates\"\n\n  # ============================================================\n  # BACKGROUND\n  # ============================================================\n  - id: joshi2025dialect_survey\n    title: \"Natural Language Processing for Dialects of a Language: A Survey\"\n    authors: \"Joshi, Dabre, Kanojia, Li, Zhan, Haffari, Dippold\"\n    venue: \"ACM Computing Surveys, Vol. 57(6)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2401.05632\"\n    category: background\n    role: \"Comprehensive survey of NLP for dialects; covers datasets, approaches, and performance gaps across dialect varieties\"\n    relevance: medium\n    key_findings:\n      - \"NLP models show systematic performance degradation on dialectal data\"\n      - \"Covers NLU and NLG tasks including dialogue systems\"\n      - \"Equity implications of language technology performance gaps\"\n    how_we_differ: \"Survey provides broad context; we tackle a specific gap in user simulation fairness\"\n\n  - id: rickford1999aave\n    title: \"African American Vernacular English: Features, Evolution, Educational Implications\"\n    authors: \"Rickford, John Russell\"\n    venue: \"Blackwell Publishers (Language in Society series)\"\n    year: 1999\n    url: \"https://www.amazon.com/African-American-Vernacular-English-Implications/dp/0631212450\"\n    category: background\n    role: \"Authoritative reference on AAVE phonological, grammatical, and pragmatic features; grounds our behavioral rate targets\"\n    relevance: medium\n    key_findings:\n      - \"Systematic documentation of AAVE phonological and grammatical features\"\n      - \"AAVE has distinct pragmatic conventions including directness patterns\"\n      - \"AAVE is a fully systematic linguistic variety, not deficient English\"\n    how_we_differ: \"Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward\"\n\n  - id: kachru2008cultures\n    title: \"Cultures, Contexts, and World Englishes\"\n    authors: \"Kachru, Yamuna; Smith, Cecil\"\n    venue: \"Routledge\"\n    year: 2008\n    url: \"https://www.routledge.com/Cultures-Contexts-and-World-Englishes/Kachru-Smith/p/book/9780805847338\"\n    category: background\n    role: \"Framework for Indian English pragmatics; documents politeness strategies and speech act differences in Outer Circle Englishes\"\n    relevance: medium\n    key_findings:\n      - \"Indian English has distinct politeness strategies rooted in face-saving norms\"\n      - \"Requesting and disagreeing strategies differ from Inner Circle varieties\"\n      - \"Three Circles model (Inner/Outer/Expanding) for understanding English variation\"\n    how_we_differ: \"Provides sociolinguistic grounding for Indian English behavioral patterns we calibrate\"\n\n  - id: sekulic2024daus\n    title: \"Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems\"\n    authors: \"Sekulic, Terragni, Guimaraes et al.\"\n    venue: \"SCI-CHAT Workshop 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.13374\"\n    category: background\n    role: \"DAUS: domain-aware user simulator fine-tuned on real dialogues; shows fine-tuning improves goal fulfillment and reduces hallucination\"\n    relevance: medium\n    key_findings:\n      - \"Fine-tuning LLMs on real dialogue examples improves user goal fulfillment\"\n      - \"Mitigates hallucinations in simulator responses\"\n      - \"Domain-aware approach outperforms generic prompting\"\n    how_we_differ: \"DAUS optimizes task completion; we optimize demographic behavioral fidelity\"\n\n  - id: ahmad2025diversity\n    title: \"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models\"\n    authors: \"Ahmad, Hillmann, Moller\"\n    venue: \"arXiv 2502.12813\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.12813\"\n    category: background\n    role: \"Generates diverse user profiles with varied demographics and conversational styles for dialogue evaluation\"\n    relevance: medium\n    key_findings:\n      - \"GPT-o1 generates more heterogeneous user distributions than GPT-4o\"\n      - \"82.46% task success across 57 dialogue sessions with diverse users\"\n      - \"Captures variation in language styles, knowledge levels, and objectives\"\n    how_we_differ: \"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\"\n\n  # ============================================================\n  # NEW ADDITIONS (scan 2026-05-13)\n  # ============================================================\n\n  # --- FOUNDATION (new) ---\n  - id: sim2real2026gap\n    title: \"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\"\n    authors: \"Zhou, Sun, Xu, Chen, Radev\"\n    venue: \"arXiv 2603.11245\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.11245\"\n    category: foundation\n    role: \"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\"\n    relevance: high\n    key_findings:\n      - \"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\"\n      - \"Simulated users create 'easy mode' that inflates agent success rates above human baseline\"\n      - \"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\"\n      - \"Higher model capability does not yield more faithful user simulation\"\n    how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we attempt BCP and DPO calibration and document why both fail\"\n    scan_date: \"2026-05-13\"\n    note: \"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\"\n\n  # --- METHOD-COMPONENT (new) ---\n  - id: khan2026decoding\n    title: \"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\"\n    authors: \"Khan, Muneeb Ur Raheem\"\n    venue: \"arXiv 2605.02348\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.02348\"\n    category: method-component\n    role: \"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\"\n    relevance: medium\n    key_findings:\n      - \"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\"\n      - \"No weight changes needed — debiasing happens at inference via PRM scoring\"\n      - \"Gate calibration is model-dependent; no one-size-fits-all prompt works\"\n    how_we_differ: \"They debias at decoding time for general fairness; we train the simulator via DPO to match target behavioral distributions\"\n    scan_date: \"2026-05-13\"\n\n  # --- EVALUATION (new) ---\n  - id: gupta2025endive\n    title: \"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\"\n    authors: \"Gupta, Cheung et al.\"\n    venue: \"Findings of EMNLP 2025 (arXiv 2504.07100)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2504.07100\"\n    category: evaluation\n    role: \"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\"\n    relevance: high\n    key_findings:\n      - \"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\"\n      - \"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\"\n      - \"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\"\n    how_we_differ: \"EnDive evaluates NLP task performance across dialects; we calibrate user simulator behavioral rates for those same dialect groups\"\n    scan_date: \"2026-05-13\"\n\n  # --- METHOD-COMPONENT (new, Plan B relevant) ---\n  - id: lee2024dpo_toxicity\n    title: \"A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity\"\n    authors: \"Lee, Panda, Yun, Bansal\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2401.01967\"\n    category: method-component\n    role: \"Shows DPO bypasses rather than removes pre-training capabilities; explains mechanistically why DPO+BCP can reverse calibration direction\"\n    relevance: high\n    key_findings:\n      - \"DPO does not remove toxic capabilities, only bypasses them at inference\"\n      - \"Simple un-alignment can revert model to pre-DPO behavior\"\n      - \"Minimal parameter changes allow reversion — alignment is fragile\"\n    how_we_differ: \"They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM4 — explains why DPO training can reverse BCP calibration effect\"\n\n  - id: gupta2026intra_fairness\n    title: \"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment\"\n    authors: \"Paraschou, Heiter, Iosifidis\"\n    venue: \"arXiv 2602.16438\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16438\"\n    category: method-component\n    role: \"Documents bias spillover — targeted debiasing on one dimension causes unintended effects on other dimensions; directly parallels our cross-dimension interference\"\n    relevance: high\n    key_findings:\n      - \"Targeted debiasing can produce unintended negative consequences across other social axes\"\n      - \"Bias spillover effect: altering behavior on one dimension when mitigating another\"\n      - \"Multi-attribute fairness dynamics must be considered in alignment\"\n    how_we_differ: \"They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM2 + FM4 — directly supports cross-dimension interference and DPO spillover claims\"\n\n  - id: basil2025playing_pretend\n    title: \"Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy\"\n    authors: \"Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke\"\n    venue: \"arXiv 2512.05858 (Wharton)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.05858\"\n    category: method-component\n    role: \"Shows persona prompting degrades factual accuracy; BCP is a form of persona/role prompting, explaining completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Expert personas do not improve factual accuracy across benchmarks\"\n      - \"Persona prompting activates instruction-following mode at expense of factual recall\"\n      - \"MMLU accuracy drops from 71.6% baseline to 66.3% with detailed persona\"\n    how_we_differ: \"They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — explains mechanism behind global behavior suppression\"\n\n  - id: hu2026expert_persona\n    title: \"Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM\"\n    authors: \"Hu, Rostami, Thomason\"\n    venue: \"arXiv 2603.18507\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.18507\"\n    category: method-component\n    role: \"Systematically documents persona prompting trade-off: alignment improves but accuracy degrades up to 30pp; directly explains BCP completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Persona prompting improves alignment tasks but degrades knowledge/reasoning tasks\"\n      - \"Performance drops up to 30pp under persona modifications\"\n      - \"More instruction-tuned models are more susceptible to persona-induced accuracy loss\"\n    how_we_differ: \"They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — strongest external evidence for global behavior suppression mechanism\"\n\n  # --- BACKGROUND (new) ---\n  - id: nakash2026divert\n    title: \"Efficient Agent Evaluation via Diversity-Guided User Simulation\"\n    authors: \"Nakash, Kour, Anaby-Tavor\"\n    venue: \"arXiv 2604.21480\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21480\"\n    category: background\n    role: \"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\"\n    relevance: medium\n    key_findings:\n      - \"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\"\n      - \"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\"\n    how_we_differ: \"They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups\"\n    scan_date: \"2026-05-13\"\n\n# ============================================================\n# SUMMARY\n# ============================================================\n# Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)\n# - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)\n# - foundation: 5 (+sim2real2026gap)\n# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +hu2026expert_persona)\n# - evaluation: 6 (+gupta2025endive)\n# - background: 6 (+nakash2026divert)\n# - high relevance: 14, medium: 13, low: 1\n#\n# Plan B scan notes (2026-05-13):\n# - 4 new papers added specifically for Plan B empirical analysis framing\n# - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)\n# - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)\n# - basil2025playing_pretend + hu2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)\n# - No direct competitor found for BCP failure mode analysis — novelty gap confirmed\n# - Also noted but not added:\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures\n",
    "structuredPatch": [
      {
        "oldStart": 357,
        "oldLines": 7,
        "newStart": 357,
        "newLines": 7,
        "lines": [
          "       - \"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\"",
          "       - \"No weight changes needed — debiasing happens at inference via PRM scoring\"",
          "       - \"Gate calibration is model-dependent; no one-size-fits-all prompt works\"",
          "-    how_we_differ: \"They debias at decoding time for general fairness; we train the simulator via DPO to match target behavioral distributions\"",
          "+    how_we_differ: \"They debias at decoding time for general fairness; we document failure modes of training-time calibration (BCP+DPO), motivating alternative approaches like decoding-time methods\"",
          "     scan_date: \"2026-05-13\"",
          " ",
          "   # --- EVALUATION (new) ---"
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


### Tool call

_source line 64_

<details open><summary>🔧 Tool call — Edit · `toolu_014XzxdmU1H9vSVEx7wyA3At`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
  "old_string": "how_we_differ: \"EnDive evaluates NLP task performance across dialects; we calibrate user simulator behavioral rates for those same dialect groups\"",
  "new_string": "how_we_differ: \"EnDive evaluates NLP task performance across dialects; we document calibration failure modes for user simulators targeting those same dialect groups\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "474e7c72-5195-4b2a-a458-934957c5951f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3iK7ejCbA9r2EwkseUzaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18730,
      "cache_read_input_tokens": 38589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18730
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

_source line 65 · 2026-05-13T07:39:10.137Z_

<details><summary>↩ Tool result · `toolu_014XzxdmU1H9vSVEx7wyA3At`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "c3d4a684-0f19-41df-84d2-9598a9f8ce89",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
    "oldString": "how_we_differ: \"EnDive evaluates NLP task performance across dialects; we calibrate user simulator behavioral rates for those same dialect groups\"",
    "newString": "how_we_differ: \"EnDive evaluates NLP task performance across dialects; we document calibration failure modes for user simulators targeting those same dialect groups\"",
    "originalFile": "papers:\n  # ============================================================\n  # DIRECT-COMPETITOR\n  # ============================================================\n  # 未找到直接竞品。没有现有工作专门做\"校准 LLM 用户模拟器的方言行为率偏差\"。\n  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。\n  # 这验证了 DemoCalib 的新颖性。\n\n  # ============================================================\n  # FOUNDATION\n  # ============================================================\n  - id: seshadri2026lost\n    title: \"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations\"\n    authors: \"Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant\"\n    venue: \"arXiv 2601.17087\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.17087\"\n    category: foundation\n    role: \"Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration\"\n    relevance: high\n    key_findings:\n      - \"Agent success rates vary up to 9pp across different user simulator LLMs\"\n      - \"AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers\"\n      - \"Simulated users introduce conversational artifacts absent from real human users\"\n      - \"Disparities compound significantly with age for AAVE speakers\"\n    how_we_differ: \"They document the problem; we document why both BCP and DPO calibration fail to close the gaps, providing a failure taxonomy\"\n\n  - id: yao2024taubench\n    title: \"tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\"\n    authors: \"Yao et al.\"\n    venue: \"arXiv 2406.12045\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2406.12045\"\n    category: foundation\n    role: \"The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric\"\n    relevance: high\n    key_findings:\n      - \"Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail\"\n      - \"Proposes pass^k metric measuring reliability over multiple trials\"\n      - \"User simulator is LLM-based, enabling behavioral modification\"\n    how_we_differ: \"We extend tau-bench by documenting systematic failure modes when calibrating the user simulator's dialect-specific behavioral rates\"\n\n  - id: liu2024agentbench\n    title: \"AgentBench: Evaluating LLMs as Agents\"\n    authors: \"Liu et al.\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2308.03688\"\n    category: foundation\n    role: \"Multi-environment agent benchmark; establishes evaluation methodology for LLM agents across 8 environments\"\n    relevance: medium\n    key_findings:\n      - \"Significant performance gap between commercial and open-source LLMs as agents\"\n      - \"Poor long-term reasoning and instruction following are main obstacles\"\n    how_we_differ: \"AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness\"\n\n  - id: wang2024mint\n    title: \"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\"\n    authors: \"Wang, Wang, Liu, Chen, Yuan, Peng, Ji\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.10691\"\n    category: foundation\n    role: \"Multi-turn agent evaluation benchmark; shows gap between single-turn and multi-turn performance\"\n    relevance: medium\n    key_findings:\n      - \"LLMs benefit 1-8% per turn from tools, 2-17% from language feedback\"\n      - \"Better single-turn performance does not guarantee better multi-turn performance\"\n      - \"SIFT and RLHF generally hurt multi-turn capabilities\"\n    how_we_differ: \"MINT uses GPT-4 simulated users without demographic variation; we investigate dialect-aware calibration and document its failure modes\"\n\n  # ============================================================\n  # METHOD-COMPONENT\n  # ============================================================\n  - id: rafailov2023dpo\n    title: \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\"\n    authors: \"Rafailov, Sharma, Mitchell, Manning, Ermon, Finn\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    url: \"https://arxiv.org/abs/2305.18290\"\n    category: method-component\n    role: \"Core algorithm for our DPO-based behavioral alignment; eliminates need for reward model training\"\n    relevance: high\n    key_findings:\n      - \"DPO directly optimizes policy from preference pairs without explicit reward model\"\n      - \"Computationally lightweight, stable alternative to PPO-based RLHF\"\n      - \"Exceeds PPO-based RLHF in controlling sentiment of generations\"\n    how_we_differ: \"We apply DPO to attempt dialect behavioral calibration and document its systematic failure modes including calibration reversal\"\n\n  - id: zhao2021calibrate\n    title: \"Calibrate Before Use: Improving Few-Shot Performance of Language Models\"\n    authors: \"Zhao, Wallace, Feng, Klein, Singh\"\n    venue: \"ICML 2021\"\n    year: 2021\n    url: \"https://arxiv.org/abs/2102.09690\"\n    category: method-component\n    role: \"Foundational calibration method for LLMs; contextual calibration corrects output distribution biases\"\n    relevance: medium\n    key_findings:\n      - \"Few-shot accuracy varies from near chance to near SOTA depending on prompt format\"\n      - \"Identified majority label bias, recency bias, common token bias\"\n      - \"Contextual calibration with content-free inputs improves accuracy up to 30%\"\n    how_we_differ: \"They calibrate classification outputs; we attempt to calibrate behavioral rates (question rate, politeness) in generation and document why it fails\"\n\n  - id: abdulhai2025consistent\n    title: \"Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning\"\n    authors: \"Abdulhai, Cheng, Clay, Althoff, Levine, Jaques\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2511.00222\"\n    category: method-component\n    role: \"Multi-turn RL for persona consistency; directly relevant to maintaining calibrated behavior across conversation turns\"\n    relevance: high\n    key_findings:\n      - \"Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue\"\n      - \"Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency\"\n      - \"Multi-turn RL reduces inconsistency by >55%\"\n    how_we_differ: \"They optimize persona consistency in general; we document failure modes when targeting dialect behavioral rate calibration\"\n\n  - id: naous2025flipping\n    title: \"Flipping the Dialogue: Training and Evaluating User Language Models\"\n    authors: \"Naous, Laban, Xu, Neville\"\n    venue: \"arXiv 2510.06552\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.06552\"\n    category: method-component\n    role: \"Purpose-built User LMs outperform repurposed assistant LMs as user simulators; validates need for specialized user models\"\n    relevance: high\n    key_findings:\n      - \"Better assistant LMs yield worse user simulators\"\n      - \"UserLM-8b provides more realistic user simulation\"\n      - \"GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation\"\n    how_we_differ: \"They train general User LMs; we document why calibrating user simulator behavioral rates for specific dialect groups fails\"\n\n  - id: li2025persona\n    title: \"LLM Generated Persona is a Promise with a Catch\"\n    authors: \"Li, Chen et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.16527\"\n    category: method-component\n    role: \"Documents systematic biases in LLM-generated personas; explains why naive persona prompting fails for demographic simulation\"\n    relevance: medium\n    key_findings:\n      - \"LLM-generated personas systematically drift toward socially desirable traits\"\n      - \"More LLM-generated content produces more left-leaning, less representative personas\"\n      - \"Bias exists in the persona creation step itself, not just model responses\"\n    how_we_differ: \"We document failure modes when directly injecting behavioral rate targets via BCP, including persona-like completion collapse\"\n\n  - id: wang2024alignment\n    title: \"A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More\"\n    authors: \"Wang, Bi, Pentyala et al.\"\n    venue: \"arXiv 2407.16216\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2407.16216\"\n    category: method-component\n    role: \"Survey unifying alignment methods under single policy gradient framework; reference for our DPO methodology\"\n    relevance: medium\n    key_findings:\n      - \"Unified policy gradient framework for pretraining, SFT, RLHF, RLVR\"\n      - \"DPO is stable and lightweight but sensitive to preference data quality\"\n      - \"Detailed comparison of PPO vs GRPO vs DPO implementation details\"\n    how_we_differ: \"Survey provides methodology reference; we apply DPO to user simulator dialect calibration and document its failure modes\"\n\n  # ============================================================\n  # EVALUATION\n  # ============================================================\n  - id: lin2025redial\n    title: \"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks\"\n    authors: \"Lin et al.\"\n    venue: \"ACL 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.11005\"\n    category: evaluation\n    role: \"First human-annotated SE-AAVE parallel benchmark (ReDial); quantifies LLM performance gaps on AAVE\"\n    relevance: high\n    key_findings:\n      - \"1.2K+ parallel SE-AAVE prompt pairs across reasoning tasks\"\n      - \"Almost all models show statistically significant performance drops on AAVE\"\n      - \"AAVE performance gaps arise from morphosyntactic features and conversational norms\"\n      - \"LLMs struggle more with AAVE than misspelled Standard English\"\n    how_we_differ: \"ReDial evaluates reasoning task performance; we evaluate behavioral rates in user simulation and document calibration failure modes\"\n\n  - id: faisal2024dialectbench\n    title: \"DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages\"\n    authors: \"Faisal et al.\"\n    venue: \"ACL 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2403.11009\"\n    category: evaluation\n    role: \"Large-scale multi-dialect NLP benchmark; documents performance disparities across 281 language varieties\"\n    relevance: medium\n    key_findings:\n      - \"10 NLP tasks, 281 varieties, 40 language clusters\"\n      - \"Substantial performance disparities between standard and non-standard varieties\"\n      - \"Performance gap widens with fine-tuning due to uneven data availability\"\n    how_we_differ: \"DialectBench evaluates NLP task performance; we document failure modes in behavioral calibration of user simulators\"\n\n  - id: gallegos2024bias\n    title: \"Bias and Fairness in Large Language Models: A Survey\"\n    authors: \"Gallegos, Rossi, Barrow et al.\"\n    venue: \"Computational Linguistics, Vol. 50(3)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.00770\"\n    category: evaluation\n    role: \"Comprehensive survey of LLM bias evaluation and mitigation; provides taxonomy of metrics and datasets\"\n    relevance: medium\n    key_findings:\n      - \"Taxonomy of bias metrics at embedding, probability, and generated text levels\"\n      - \"Mitigation methods categorized by intervention stage: pre/in/intra/post-processing\"\n      - \"Consolidated public datasets for bias evaluation\"\n    how_we_differ: \"Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)\"\n\n  - id: parrish2022bbq\n    title: \"BBQ: A Hand-Built Bias Benchmark for Question Answering\"\n    authors: \"Parrish et al.\"\n    venue: \"Findings of ACL 2022\"\n    year: 2022\n    url: \"https://aclanthology.org/2022.findings-acl.165/\"\n    category: evaluation\n    role: \"Established bias benchmark for QA; evaluates social biases across multiple demographic categories\"\n    relevance: low\n    key_findings:\n      - \"58,492 unique examples across multiple bias categories\"\n      - \"Evaluates both individual and intersectional biases\"\n      - \"Standard benchmark for LLM bias evaluation\"\n    how_we_differ: \"BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation\"\n\n  - id: haq2026dialect\n    title: \"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles\"\n    authors: \"Haq, Saldias\"\n    venue: \"arXiv 2604.21152\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21152\"\n    category: evaluation\n    role: \"Closest to direct competitor; quantifies how dialect cues vs explicit identity trigger differential LLM behavior\"\n    relevance: high\n    key_findings:\n      - \"Dialect cues trigger 'dialect jailbreak' reducing refusal probability to near zero\"\n      - \"AAVE/Singlish users receive less sanitized content than SAE users\"\n      - \"Safety alignment is brittle, over-indexed on explicit keywords\"\n      - \"24,000+ responses analyzed across two LLMs\"\n    how_we_differ: \"They characterize the bias mechanism (implicit vs explicit); we document why calibration methods fail to correct behavioral rates\"\n\n  # ============================================================\n  # BACKGROUND\n  # ============================================================\n  - id: joshi2025dialect_survey\n    title: \"Natural Language Processing for Dialects of a Language: A Survey\"\n    authors: \"Joshi, Dabre, Kanojia, Li, Zhan, Haffari, Dippold\"\n    venue: \"ACM Computing Surveys, Vol. 57(6)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2401.05632\"\n    category: background\n    role: \"Comprehensive survey of NLP for dialects; covers datasets, approaches, and performance gaps across dialect varieties\"\n    relevance: medium\n    key_findings:\n      - \"NLP models show systematic performance degradation on dialectal data\"\n      - \"Covers NLU and NLG tasks including dialogue systems\"\n      - \"Equity implications of language technology performance gaps\"\n    how_we_differ: \"Survey provides broad context; we tackle a specific gap in user simulation fairness\"\n\n  - id: rickford1999aave\n    title: \"African American Vernacular English: Features, Evolution, Educational Implications\"\n    authors: \"Rickford, John Russell\"\n    venue: \"Blackwell Publishers (Language in Society series)\"\n    year: 1999\n    url: \"https://www.amazon.com/African-American-Vernacular-English-Implications/dp/0631212450\"\n    category: background\n    role: \"Authoritative reference on AAVE phonological, grammatical, and pragmatic features; grounds our behavioral rate targets\"\n    relevance: medium\n    key_findings:\n      - \"Systematic documentation of AAVE phonological and grammatical features\"\n      - \"AAVE has distinct pragmatic conventions including directness patterns\"\n      - \"AAVE is a fully systematic linguistic variety, not deficient English\"\n    how_we_differ: \"Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward\"\n\n  - id: kachru2008cultures\n    title: \"Cultures, Contexts, and World Englishes\"\n    authors: \"Kachru, Yamuna; Smith, Cecil\"\n    venue: \"Routledge\"\n    year: 2008\n    url: \"https://www.routledge.com/Cultures-Contexts-and-World-Englishes/Kachru-Smith/p/book/9780805847338\"\n    category: background\n    role: \"Framework for Indian English pragmatics; documents politeness strategies and speech act differences in Outer Circle Englishes\"\n    relevance: medium\n    key_findings:\n      - \"Indian English has distinct politeness strategies rooted in face-saving norms\"\n      - \"Requesting and disagreeing strategies differ from Inner Circle varieties\"\n      - \"Three Circles model (Inner/Outer/Expanding) for understanding English variation\"\n    how_we_differ: \"Provides sociolinguistic grounding for Indian English behavioral patterns we calibrate\"\n\n  - id: sekulic2024daus\n    title: \"Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems\"\n    authors: \"Sekulic, Terragni, Guimaraes et al.\"\n    venue: \"SCI-CHAT Workshop 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.13374\"\n    category: background\n    role: \"DAUS: domain-aware user simulator fine-tuned on real dialogues; shows fine-tuning improves goal fulfillment and reduces hallucination\"\n    relevance: medium\n    key_findings:\n      - \"Fine-tuning LLMs on real dialogue examples improves user goal fulfillment\"\n      - \"Mitigates hallucinations in simulator responses\"\n      - \"Domain-aware approach outperforms generic prompting\"\n    how_we_differ: \"DAUS optimizes task completion; we optimize demographic behavioral fidelity\"\n\n  - id: ahmad2025diversity\n    title: \"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models\"\n    authors: \"Ahmad, Hillmann, Moller\"\n    venue: \"arXiv 2502.12813\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.12813\"\n    category: background\n    role: \"Generates diverse user profiles with varied demographics and conversational styles for dialogue evaluation\"\n    relevance: medium\n    key_findings:\n      - \"GPT-o1 generates more heterogeneous user distributions than GPT-4o\"\n      - \"82.46% task success across 57 dialogue sessions with diverse users\"\n      - \"Captures variation in language styles, knowledge levels, and objectives\"\n    how_we_differ: \"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\"\n\n  # ============================================================\n  # NEW ADDITIONS (scan 2026-05-13)\n  # ============================================================\n\n  # --- FOUNDATION (new) ---\n  - id: sim2real2026gap\n    title: \"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\"\n    authors: \"Zhou, Sun, Xu, Chen, Radev\"\n    venue: \"arXiv 2603.11245\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.11245\"\n    category: foundation\n    role: \"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\"\n    relevance: high\n    key_findings:\n      - \"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\"\n      - \"Simulated users create 'easy mode' that inflates agent success rates above human baseline\"\n      - \"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\"\n      - \"Higher model capability does not yield more faithful user simulation\"\n    how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we attempt BCP and DPO calibration and document why both fail\"\n    scan_date: \"2026-05-13\"\n    note: \"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\"\n\n  # --- METHOD-COMPONENT (new) ---\n  - id: khan2026decoding\n    title: \"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\"\n    authors: \"Khan, Muneeb Ur Raheem\"\n    venue: \"arXiv 2605.02348\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.02348\"\n    category: method-component\n    role: \"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\"\n    relevance: medium\n    key_findings:\n      - \"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\"\n      - \"No weight changes needed — debiasing happens at inference via PRM scoring\"\n      - \"Gate calibration is model-dependent; no one-size-fits-all prompt works\"\n    how_we_differ: \"They debias at decoding time for general fairness; we document failure modes of training-time calibration (BCP+DPO), motivating alternative approaches like decoding-time methods\"\n    scan_date: \"2026-05-13\"\n\n  # --- EVALUATION (new) ---\n  - id: gupta2025endive\n    title: \"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\"\n    authors: \"Gupta, Cheung et al.\"\n    venue: \"Findings of EMNLP 2025 (arXiv 2504.07100)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2504.07100\"\n    category: evaluation\n    role: \"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\"\n    relevance: high\n    key_findings:\n      - \"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\"\n      - \"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\"\n      - \"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\"\n    how_we_differ: \"EnDive evaluates NLP task performance across dialects; we calibrate user simulator behavioral rates for those same dialect groups\"\n    scan_date: \"2026-05-13\"\n\n  # --- METHOD-COMPONENT (new, Plan B relevant) ---\n  - id: lee2024dpo_toxicity\n    title: \"A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity\"\n    authors: \"Lee, Panda, Yun, Bansal\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2401.01967\"\n    category: method-component\n    role: \"Shows DPO bypasses rather than removes pre-training capabilities; explains mechanistically why DPO+BCP can reverse calibration direction\"\n    relevance: high\n    key_findings:\n      - \"DPO does not remove toxic capabilities, only bypasses them at inference\"\n      - \"Simple un-alignment can revert model to pre-DPO behavior\"\n      - \"Minimal parameter changes allow reversion — alignment is fragile\"\n    how_we_differ: \"They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM4 — explains why DPO training can reverse BCP calibration effect\"\n\n  - id: gupta2026intra_fairness\n    title: \"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment\"\n    authors: \"Paraschou, Heiter, Iosifidis\"\n    venue: \"arXiv 2602.16438\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16438\"\n    category: method-component\n    role: \"Documents bias spillover — targeted debiasing on one dimension causes unintended effects on other dimensions; directly parallels our cross-dimension interference\"\n    relevance: high\n    key_findings:\n      - \"Targeted debiasing can produce unintended negative consequences across other social axes\"\n      - \"Bias spillover effect: altering behavior on one dimension when mitigating another\"\n      - \"Multi-attribute fairness dynamics must be considered in alignment\"\n    how_we_differ: \"They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM2 + FM4 — directly supports cross-dimension interference and DPO spillover claims\"\n\n  - id: basil2025playing_pretend\n    title: \"Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy\"\n    authors: \"Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke\"\n    venue: \"arXiv 2512.05858 (Wharton)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.05858\"\n    category: method-component\n    role: \"Shows persona prompting degrades factual accuracy; BCP is a form of persona/role prompting, explaining completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Expert personas do not improve factual accuracy across benchmarks\"\n      - \"Persona prompting activates instruction-following mode at expense of factual recall\"\n      - \"MMLU accuracy drops from 71.6% baseline to 66.3% with detailed persona\"\n    how_we_differ: \"They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — explains mechanism behind global behavior suppression\"\n\n  - id: hu2026expert_persona\n    title: \"Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM\"\n    authors: \"Hu, Rostami, Thomason\"\n    venue: \"arXiv 2603.18507\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.18507\"\n    category: method-component\n    role: \"Systematically documents persona prompting trade-off: alignment improves but accuracy degrades up to 30pp; directly explains BCP completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Persona prompting improves alignment tasks but degrades knowledge/reasoning tasks\"\n      - \"Performance drops up to 30pp under persona modifications\"\n      - \"More instruction-tuned models are more susceptible to persona-induced accuracy loss\"\n    how_we_differ: \"They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — strongest external evidence for global behavior suppression mechanism\"\n\n  # --- BACKGROUND (new) ---\n  - id: nakash2026divert\n    title: \"Efficient Agent Evaluation via Diversity-Guided User Simulation\"\n    authors: \"Nakash, Kour, Anaby-Tavor\"\n    venue: \"arXiv 2604.21480\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21480\"\n    category: background\n    role: \"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\"\n    relevance: medium\n    key_findings:\n      - \"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\"\n      - \"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\"\n    how_we_differ: \"They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups\"\n    scan_date: \"2026-05-13\"\n\n# ============================================================\n# SUMMARY\n# ============================================================\n# Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)\n# - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)\n# - foundation: 5 (+sim2real2026gap)\n# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +hu2026expert_persona)\n# - evaluation: 6 (+gupta2025endive)\n# - background: 6 (+nakash2026divert)\n# - high relevance: 14, medium: 13, low: 1\n#\n# Plan B scan notes (2026-05-13):\n# - 4 new papers added specifically for Plan B empirical analysis framing\n# - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)\n# - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)\n# - basil2025playing_pretend + hu2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)\n# - No direct competitor found for BCP failure mode analysis — novelty gap confirmed\n# - Also noted but not added:\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures\n",
    "structuredPatch": [
      {
        "oldStart": 374,
        "oldLines": 7,
        "newStart": 374,
        "newLines": 7,
        "lines": [
          "       - \"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\"",
          "       - \"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\"",
          "       - \"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\"",
          "-    how_we_differ: \"EnDive evaluates NLP task performance across dialects; we calibrate user simulator behavioral rates for those same dialect groups\"",
          "+    how_we_differ: \"EnDive evaluates NLP task performance across dialects; we document calibration failure modes for user simulators targeting those same dialect groups\"",
          "     scan_date: \"2026-05-13\"",
          " ",
          "   # --- METHOD-COMPONENT (new, Plan B relevant) ---"
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


### Tool call

_source line 66_

<details open><summary>🔧 Tool call — Edit · `toolu_01CtquVp4r3BNSjyP5xkSy82`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
  "old_string": "how_we_differ: \"DAUS optimizes task completion; we optimize demographic behavioral fidelity\"",
  "new_string": "how_we_differ: \"DAUS optimizes task completion; we document failure modes when optimizing demographic behavioral fidelity\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "1677ef06-97dc-4694-a2dc-cb3768583573",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3iK7ejCbA9r2EwkseUzaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18730,
      "cache_read_input_tokens": 38589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18730
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

_source line 67 · 2026-05-13T07:39:11.548Z_

<details><summary>↩ Tool result · `toolu_01CtquVp4r3BNSjyP5xkSy82`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "96a7b0b7-4c6e-47bb-a19f-40b0bcb9b0a4",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
    "oldString": "how_we_differ: \"DAUS optimizes task completion; we optimize demographic behavioral fidelity\"",
    "newString": "how_we_differ: \"DAUS optimizes task completion; we document failure modes when optimizing demographic behavioral fidelity\"",
    "originalFile": "papers:\n  # ============================================================\n  # DIRECT-COMPETITOR\n  # ============================================================\n  # 未找到直接竞品。没有现有工作专门做\"校准 LLM 用户模拟器的方言行为率偏差\"。\n  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。\n  # 这验证了 DemoCalib 的新颖性。\n\n  # ============================================================\n  # FOUNDATION\n  # ============================================================\n  - id: seshadri2026lost\n    title: \"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations\"\n    authors: \"Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant\"\n    venue: \"arXiv 2601.17087\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.17087\"\n    category: foundation\n    role: \"Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration\"\n    relevance: high\n    key_findings:\n      - \"Agent success rates vary up to 9pp across different user simulator LLMs\"\n      - \"AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers\"\n      - \"Simulated users introduce conversational artifacts absent from real human users\"\n      - \"Disparities compound significantly with age for AAVE speakers\"\n    how_we_differ: \"They document the problem; we document why both BCP and DPO calibration fail to close the gaps, providing a failure taxonomy\"\n\n  - id: yao2024taubench\n    title: \"tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\"\n    authors: \"Yao et al.\"\n    venue: \"arXiv 2406.12045\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2406.12045\"\n    category: foundation\n    role: \"The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric\"\n    relevance: high\n    key_findings:\n      - \"Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail\"\n      - \"Proposes pass^k metric measuring reliability over multiple trials\"\n      - \"User simulator is LLM-based, enabling behavioral modification\"\n    how_we_differ: \"We extend tau-bench by documenting systematic failure modes when calibrating the user simulator's dialect-specific behavioral rates\"\n\n  - id: liu2024agentbench\n    title: \"AgentBench: Evaluating LLMs as Agents\"\n    authors: \"Liu et al.\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2308.03688\"\n    category: foundation\n    role: \"Multi-environment agent benchmark; establishes evaluation methodology for LLM agents across 8 environments\"\n    relevance: medium\n    key_findings:\n      - \"Significant performance gap between commercial and open-source LLMs as agents\"\n      - \"Poor long-term reasoning and instruction following are main obstacles\"\n    how_we_differ: \"AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness\"\n\n  - id: wang2024mint\n    title: \"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\"\n    authors: \"Wang, Wang, Liu, Chen, Yuan, Peng, Ji\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.10691\"\n    category: foundation\n    role: \"Multi-turn agent evaluation benchmark; shows gap between single-turn and multi-turn performance\"\n    relevance: medium\n    key_findings:\n      - \"LLMs benefit 1-8% per turn from tools, 2-17% from language feedback\"\n      - \"Better single-turn performance does not guarantee better multi-turn performance\"\n      - \"SIFT and RLHF generally hurt multi-turn capabilities\"\n    how_we_differ: \"MINT uses GPT-4 simulated users without demographic variation; we investigate dialect-aware calibration and document its failure modes\"\n\n  # ============================================================\n  # METHOD-COMPONENT\n  # ============================================================\n  - id: rafailov2023dpo\n    title: \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\"\n    authors: \"Rafailov, Sharma, Mitchell, Manning, Ermon, Finn\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    url: \"https://arxiv.org/abs/2305.18290\"\n    category: method-component\n    role: \"Core algorithm for our DPO-based behavioral alignment; eliminates need for reward model training\"\n    relevance: high\n    key_findings:\n      - \"DPO directly optimizes policy from preference pairs without explicit reward model\"\n      - \"Computationally lightweight, stable alternative to PPO-based RLHF\"\n      - \"Exceeds PPO-based RLHF in controlling sentiment of generations\"\n    how_we_differ: \"We apply DPO to attempt dialect behavioral calibration and document its systematic failure modes including calibration reversal\"\n\n  - id: zhao2021calibrate\n    title: \"Calibrate Before Use: Improving Few-Shot Performance of Language Models\"\n    authors: \"Zhao, Wallace, Feng, Klein, Singh\"\n    venue: \"ICML 2021\"\n    year: 2021\n    url: \"https://arxiv.org/abs/2102.09690\"\n    category: method-component\n    role: \"Foundational calibration method for LLMs; contextual calibration corrects output distribution biases\"\n    relevance: medium\n    key_findings:\n      - \"Few-shot accuracy varies from near chance to near SOTA depending on prompt format\"\n      - \"Identified majority label bias, recency bias, common token bias\"\n      - \"Contextual calibration with content-free inputs improves accuracy up to 30%\"\n    how_we_differ: \"They calibrate classification outputs; we attempt to calibrate behavioral rates (question rate, politeness) in generation and document why it fails\"\n\n  - id: abdulhai2025consistent\n    title: \"Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning\"\n    authors: \"Abdulhai, Cheng, Clay, Althoff, Levine, Jaques\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2511.00222\"\n    category: method-component\n    role: \"Multi-turn RL for persona consistency; directly relevant to maintaining calibrated behavior across conversation turns\"\n    relevance: high\n    key_findings:\n      - \"Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue\"\n      - \"Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency\"\n      - \"Multi-turn RL reduces inconsistency by >55%\"\n    how_we_differ: \"They optimize persona consistency in general; we document failure modes when targeting dialect behavioral rate calibration\"\n\n  - id: naous2025flipping\n    title: \"Flipping the Dialogue: Training and Evaluating User Language Models\"\n    authors: \"Naous, Laban, Xu, Neville\"\n    venue: \"arXiv 2510.06552\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.06552\"\n    category: method-component\n    role: \"Purpose-built User LMs outperform repurposed assistant LMs as user simulators; validates need for specialized user models\"\n    relevance: high\n    key_findings:\n      - \"Better assistant LMs yield worse user simulators\"\n      - \"UserLM-8b provides more realistic user simulation\"\n      - \"GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation\"\n    how_we_differ: \"They train general User LMs; we document why calibrating user simulator behavioral rates for specific dialect groups fails\"\n\n  - id: li2025persona\n    title: \"LLM Generated Persona is a Promise with a Catch\"\n    authors: \"Li, Chen et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.16527\"\n    category: method-component\n    role: \"Documents systematic biases in LLM-generated personas; explains why naive persona prompting fails for demographic simulation\"\n    relevance: medium\n    key_findings:\n      - \"LLM-generated personas systematically drift toward socially desirable traits\"\n      - \"More LLM-generated content produces more left-leaning, less representative personas\"\n      - \"Bias exists in the persona creation step itself, not just model responses\"\n    how_we_differ: \"We document failure modes when directly injecting behavioral rate targets via BCP, including persona-like completion collapse\"\n\n  - id: wang2024alignment\n    title: \"A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More\"\n    authors: \"Wang, Bi, Pentyala et al.\"\n    venue: \"arXiv 2407.16216\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2407.16216\"\n    category: method-component\n    role: \"Survey unifying alignment methods under single policy gradient framework; reference for our DPO methodology\"\n    relevance: medium\n    key_findings:\n      - \"Unified policy gradient framework for pretraining, SFT, RLHF, RLVR\"\n      - \"DPO is stable and lightweight but sensitive to preference data quality\"\n      - \"Detailed comparison of PPO vs GRPO vs DPO implementation details\"\n    how_we_differ: \"Survey provides methodology reference; we apply DPO to user simulator dialect calibration and document its failure modes\"\n\n  # ============================================================\n  # EVALUATION\n  # ============================================================\n  - id: lin2025redial\n    title: \"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks\"\n    authors: \"Lin et al.\"\n    venue: \"ACL 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.11005\"\n    category: evaluation\n    role: \"First human-annotated SE-AAVE parallel benchmark (ReDial); quantifies LLM performance gaps on AAVE\"\n    relevance: high\n    key_findings:\n      - \"1.2K+ parallel SE-AAVE prompt pairs across reasoning tasks\"\n      - \"Almost all models show statistically significant performance drops on AAVE\"\n      - \"AAVE performance gaps arise from morphosyntactic features and conversational norms\"\n      - \"LLMs struggle more with AAVE than misspelled Standard English\"\n    how_we_differ: \"ReDial evaluates reasoning task performance; we evaluate behavioral rates in user simulation and document calibration failure modes\"\n\n  - id: faisal2024dialectbench\n    title: \"DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages\"\n    authors: \"Faisal et al.\"\n    venue: \"ACL 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2403.11009\"\n    category: evaluation\n    role: \"Large-scale multi-dialect NLP benchmark; documents performance disparities across 281 language varieties\"\n    relevance: medium\n    key_findings:\n      - \"10 NLP tasks, 281 varieties, 40 language clusters\"\n      - \"Substantial performance disparities between standard and non-standard varieties\"\n      - \"Performance gap widens with fine-tuning due to uneven data availability\"\n    how_we_differ: \"DialectBench evaluates NLP task performance; we document failure modes in behavioral calibration of user simulators\"\n\n  - id: gallegos2024bias\n    title: \"Bias and Fairness in Large Language Models: A Survey\"\n    authors: \"Gallegos, Rossi, Barrow et al.\"\n    venue: \"Computational Linguistics, Vol. 50(3)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.00770\"\n    category: evaluation\n    role: \"Comprehensive survey of LLM bias evaluation and mitigation; provides taxonomy of metrics and datasets\"\n    relevance: medium\n    key_findings:\n      - \"Taxonomy of bias metrics at embedding, probability, and generated text levels\"\n      - \"Mitigation methods categorized by intervention stage: pre/in/intra/post-processing\"\n      - \"Consolidated public datasets for bias evaluation\"\n    how_we_differ: \"Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)\"\n\n  - id: parrish2022bbq\n    title: \"BBQ: A Hand-Built Bias Benchmark for Question Answering\"\n    authors: \"Parrish et al.\"\n    venue: \"Findings of ACL 2022\"\n    year: 2022\n    url: \"https://aclanthology.org/2022.findings-acl.165/\"\n    category: evaluation\n    role: \"Established bias benchmark for QA; evaluates social biases across multiple demographic categories\"\n    relevance: low\n    key_findings:\n      - \"58,492 unique examples across multiple bias categories\"\n      - \"Evaluates both individual and intersectional biases\"\n      - \"Standard benchmark for LLM bias evaluation\"\n    how_we_differ: \"BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation\"\n\n  - id: haq2026dialect\n    title: \"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles\"\n    authors: \"Haq, Saldias\"\n    venue: \"arXiv 2604.21152\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21152\"\n    category: evaluation\n    role: \"Closest to direct competitor; quantifies how dialect cues vs explicit identity trigger differential LLM behavior\"\n    relevance: high\n    key_findings:\n      - \"Dialect cues trigger 'dialect jailbreak' reducing refusal probability to near zero\"\n      - \"AAVE/Singlish users receive less sanitized content than SAE users\"\n      - \"Safety alignment is brittle, over-indexed on explicit keywords\"\n      - \"24,000+ responses analyzed across two LLMs\"\n    how_we_differ: \"They characterize the bias mechanism (implicit vs explicit); we document why calibration methods fail to correct behavioral rates\"\n\n  # ============================================================\n  # BACKGROUND\n  # ============================================================\n  - id: joshi2025dialect_survey\n    title: \"Natural Language Processing for Dialects of a Language: A Survey\"\n    authors: \"Joshi, Dabre, Kanojia, Li, Zhan, Haffari, Dippold\"\n    venue: \"ACM Computing Surveys, Vol. 57(6)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2401.05632\"\n    category: background\n    role: \"Comprehensive survey of NLP for dialects; covers datasets, approaches, and performance gaps across dialect varieties\"\n    relevance: medium\n    key_findings:\n      - \"NLP models show systematic performance degradation on dialectal data\"\n      - \"Covers NLU and NLG tasks including dialogue systems\"\n      - \"Equity implications of language technology performance gaps\"\n    how_we_differ: \"Survey provides broad context; we tackle a specific gap in user simulation fairness\"\n\n  - id: rickford1999aave\n    title: \"African American Vernacular English: Features, Evolution, Educational Implications\"\n    authors: \"Rickford, John Russell\"\n    venue: \"Blackwell Publishers (Language in Society series)\"\n    year: 1999\n    url: \"https://www.amazon.com/African-American-Vernacular-English-Implications/dp/0631212450\"\n    category: background\n    role: \"Authoritative reference on AAVE phonological, grammatical, and pragmatic features; grounds our behavioral rate targets\"\n    relevance: medium\n    key_findings:\n      - \"Systematic documentation of AAVE phonological and grammatical features\"\n      - \"AAVE has distinct pragmatic conventions including directness patterns\"\n      - \"AAVE is a fully systematic linguistic variety, not deficient English\"\n    how_we_differ: \"Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward\"\n\n  - id: kachru2008cultures\n    title: \"Cultures, Contexts, and World Englishes\"\n    authors: \"Kachru, Yamuna; Smith, Cecil\"\n    venue: \"Routledge\"\n    year: 2008\n    url: \"https://www.routledge.com/Cultures-Contexts-and-World-Englishes/Kachru-Smith/p/book/9780805847338\"\n    category: background\n    role: \"Framework for Indian English pragmatics; documents politeness strategies and speech act differences in Outer Circle Englishes\"\n    relevance: medium\n    key_findings:\n      - \"Indian English has distinct politeness strategies rooted in face-saving norms\"\n      - \"Requesting and disagreeing strategies differ from Inner Circle varieties\"\n      - \"Three Circles model (Inner/Outer/Expanding) for understanding English variation\"\n    how_we_differ: \"Provides sociolinguistic grounding for Indian English behavioral patterns we calibrate\"\n\n  - id: sekulic2024daus\n    title: \"Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems\"\n    authors: \"Sekulic, Terragni, Guimaraes et al.\"\n    venue: \"SCI-CHAT Workshop 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.13374\"\n    category: background\n    role: \"DAUS: domain-aware user simulator fine-tuned on real dialogues; shows fine-tuning improves goal fulfillment and reduces hallucination\"\n    relevance: medium\n    key_findings:\n      - \"Fine-tuning LLMs on real dialogue examples improves user goal fulfillment\"\n      - \"Mitigates hallucinations in simulator responses\"\n      - \"Domain-aware approach outperforms generic prompting\"\n    how_we_differ: \"DAUS optimizes task completion; we optimize demographic behavioral fidelity\"\n\n  - id: ahmad2025diversity\n    title: \"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models\"\n    authors: \"Ahmad, Hillmann, Moller\"\n    venue: \"arXiv 2502.12813\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.12813\"\n    category: background\n    role: \"Generates diverse user profiles with varied demographics and conversational styles for dialogue evaluation\"\n    relevance: medium\n    key_findings:\n      - \"GPT-o1 generates more heterogeneous user distributions than GPT-4o\"\n      - \"82.46% task success across 57 dialogue sessions with diverse users\"\n      - \"Captures variation in language styles, knowledge levels, and objectives\"\n    how_we_differ: \"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\"\n\n  # ============================================================\n  # NEW ADDITIONS (scan 2026-05-13)\n  # ============================================================\n\n  # --- FOUNDATION (new) ---\n  - id: sim2real2026gap\n    title: \"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\"\n    authors: \"Zhou, Sun, Xu, Chen, Radev\"\n    venue: \"arXiv 2603.11245\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.11245\"\n    category: foundation\n    role: \"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\"\n    relevance: high\n    key_findings:\n      - \"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\"\n      - \"Simulated users create 'easy mode' that inflates agent success rates above human baseline\"\n      - \"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\"\n      - \"Higher model capability does not yield more faithful user simulation\"\n    how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we attempt BCP and DPO calibration and document why both fail\"\n    scan_date: \"2026-05-13\"\n    note: \"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\"\n\n  # --- METHOD-COMPONENT (new) ---\n  - id: khan2026decoding\n    title: \"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\"\n    authors: \"Khan, Muneeb Ur Raheem\"\n    venue: \"arXiv 2605.02348\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.02348\"\n    category: method-component\n    role: \"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\"\n    relevance: medium\n    key_findings:\n      - \"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\"\n      - \"No weight changes needed — debiasing happens at inference via PRM scoring\"\n      - \"Gate calibration is model-dependent; no one-size-fits-all prompt works\"\n    how_we_differ: \"They debias at decoding time for general fairness; we document failure modes of training-time calibration (BCP+DPO), motivating alternative approaches like decoding-time methods\"\n    scan_date: \"2026-05-13\"\n\n  # --- EVALUATION (new) ---\n  - id: gupta2025endive\n    title: \"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\"\n    authors: \"Gupta, Cheung et al.\"\n    venue: \"Findings of EMNLP 2025 (arXiv 2504.07100)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2504.07100\"\n    category: evaluation\n    role: \"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\"\n    relevance: high\n    key_findings:\n      - \"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\"\n      - \"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\"\n      - \"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\"\n    how_we_differ: \"EnDive evaluates NLP task performance across dialects; we document calibration failure modes for user simulators targeting those same dialect groups\"\n    scan_date: \"2026-05-13\"\n\n  # --- METHOD-COMPONENT (new, Plan B relevant) ---\n  - id: lee2024dpo_toxicity\n    title: \"A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity\"\n    authors: \"Lee, Panda, Yun, Bansal\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2401.01967\"\n    category: method-component\n    role: \"Shows DPO bypasses rather than removes pre-training capabilities; explains mechanistically why DPO+BCP can reverse calibration direction\"\n    relevance: high\n    key_findings:\n      - \"DPO does not remove toxic capabilities, only bypasses them at inference\"\n      - \"Simple un-alignment can revert model to pre-DPO behavior\"\n      - \"Minimal parameter changes allow reversion — alignment is fragile\"\n    how_we_differ: \"They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM4 — explains why DPO training can reverse BCP calibration effect\"\n\n  - id: gupta2026intra_fairness\n    title: \"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment\"\n    authors: \"Paraschou, Heiter, Iosifidis\"\n    venue: \"arXiv 2602.16438\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16438\"\n    category: method-component\n    role: \"Documents bias spillover — targeted debiasing on one dimension causes unintended effects on other dimensions; directly parallels our cross-dimension interference\"\n    relevance: high\n    key_findings:\n      - \"Targeted debiasing can produce unintended negative consequences across other social axes\"\n      - \"Bias spillover effect: altering behavior on one dimension when mitigating another\"\n      - \"Multi-attribute fairness dynamics must be considered in alignment\"\n    how_we_differ: \"They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM2 + FM4 — directly supports cross-dimension interference and DPO spillover claims\"\n\n  - id: basil2025playing_pretend\n    title: \"Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy\"\n    authors: \"Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke\"\n    venue: \"arXiv 2512.05858 (Wharton)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.05858\"\n    category: method-component\n    role: \"Shows persona prompting degrades factual accuracy; BCP is a form of persona/role prompting, explaining completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Expert personas do not improve factual accuracy across benchmarks\"\n      - \"Persona prompting activates instruction-following mode at expense of factual recall\"\n      - \"MMLU accuracy drops from 71.6% baseline to 66.3% with detailed persona\"\n    how_we_differ: \"They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — explains mechanism behind global behavior suppression\"\n\n  - id: hu2026expert_persona\n    title: \"Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM\"\n    authors: \"Hu, Rostami, Thomason\"\n    venue: \"arXiv 2603.18507\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.18507\"\n    category: method-component\n    role: \"Systematically documents persona prompting trade-off: alignment improves but accuracy degrades up to 30pp; directly explains BCP completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Persona prompting improves alignment tasks but degrades knowledge/reasoning tasks\"\n      - \"Performance drops up to 30pp under persona modifications\"\n      - \"More instruction-tuned models are more susceptible to persona-induced accuracy loss\"\n    how_we_differ: \"They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — strongest external evidence for global behavior suppression mechanism\"\n\n  # --- BACKGROUND (new) ---\n  - id: nakash2026divert\n    title: \"Efficient Agent Evaluation via Diversity-Guided User Simulation\"\n    authors: \"Nakash, Kour, Anaby-Tavor\"\n    venue: \"arXiv 2604.21480\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21480\"\n    category: background\n    role: \"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\"\n    relevance: medium\n    key_findings:\n      - \"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\"\n      - \"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\"\n    how_we_differ: \"They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups\"\n    scan_date: \"2026-05-13\"\n\n# ============================================================\n# SUMMARY\n# ============================================================\n# Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)\n# - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)\n# - foundation: 5 (+sim2real2026gap)\n# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +hu2026expert_persona)\n# - evaluation: 6 (+gupta2025endive)\n# - background: 6 (+nakash2026divert)\n# - high relevance: 14, medium: 13, low: 1\n#\n# Plan B scan notes (2026-05-13):\n# - 4 new papers added specifically for Plan B empirical analysis framing\n# - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)\n# - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)\n# - basil2025playing_pretend + hu2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)\n# - No direct competitor found for BCP failure mode analysis — novelty gap confirmed\n# - Also noted but not added:\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures\n",
    "structuredPatch": [
      {
        "oldStart": 303,
        "oldLines": 7,
        "newStart": 303,
        "newLines": 7,
        "lines": [
          "       - \"Fine-tuning LLMs on real dialogue examples improves user goal fulfillment\"",
          "       - \"Mitigates hallucinations in simulator responses\"",
          "       - \"Domain-aware approach outperforms generic prompting\"",
          "-    how_we_differ: \"DAUS optimizes task completion; we optimize demographic behavioral fidelity\"",
          "+    how_we_differ: \"DAUS optimizes task completion; we document failure modes when optimizing demographic behavioral fidelity\"",
          " ",
          "   - id: ahmad2025diversity",
          "     title: \"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models\""
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


### Tool call

_source line 68_

<details open><summary>🔧 Tool call — Edit · `toolu_01AJUGZokWLveYS1REpG4k9U`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
  "old_string": "how_we_differ: \"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\"",
  "new_string": "how_we_differ: \"They generate diverse profiles; we document why calibrating specific behavioral rates to match real dialect group distributions fails\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "b28e4575-33b0-4c29-ba22-970f589dba08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3iK7ejCbA9r2EwkseUzaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18730,
      "cache_read_input_tokens": 38589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18730
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

_source line 69 · 2026-05-13T07:39:12.497Z_

<details><summary>↩ Tool result · `toolu_01AJUGZokWLveYS1REpG4k9U`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "2cc9a993-86e0-472b-9920-a8cd4dda6652",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
    "oldString": "how_we_differ: \"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\"",
    "newString": "how_we_differ: \"They generate diverse profiles; we document why calibrating specific behavioral rates to match real dialect group distributions fails\"",
    "originalFile": "papers:\n  # ============================================================\n  # DIRECT-COMPETITOR\n  # ============================================================\n  # 未找到直接竞品。没有现有工作专门做\"校准 LLM 用户模拟器的方言行为率偏差\"。\n  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。\n  # 这验证了 DemoCalib 的新颖性。\n\n  # ============================================================\n  # FOUNDATION\n  # ============================================================\n  - id: seshadri2026lost\n    title: \"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations\"\n    authors: \"Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant\"\n    venue: \"arXiv 2601.17087\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.17087\"\n    category: foundation\n    role: \"Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration\"\n    relevance: high\n    key_findings:\n      - \"Agent success rates vary up to 9pp across different user simulator LLMs\"\n      - \"AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers\"\n      - \"Simulated users introduce conversational artifacts absent from real human users\"\n      - \"Disparities compound significantly with age for AAVE speakers\"\n    how_we_differ: \"They document the problem; we document why both BCP and DPO calibration fail to close the gaps, providing a failure taxonomy\"\n\n  - id: yao2024taubench\n    title: \"tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\"\n    authors: \"Yao et al.\"\n    venue: \"arXiv 2406.12045\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2406.12045\"\n    category: foundation\n    role: \"The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric\"\n    relevance: high\n    key_findings:\n      - \"Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail\"\n      - \"Proposes pass^k metric measuring reliability over multiple trials\"\n      - \"User simulator is LLM-based, enabling behavioral modification\"\n    how_we_differ: \"We extend tau-bench by documenting systematic failure modes when calibrating the user simulator's dialect-specific behavioral rates\"\n\n  - id: liu2024agentbench\n    title: \"AgentBench: Evaluating LLMs as Agents\"\n    authors: \"Liu et al.\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2308.03688\"\n    category: foundation\n    role: \"Multi-environment agent benchmark; establishes evaluation methodology for LLM agents across 8 environments\"\n    relevance: medium\n    key_findings:\n      - \"Significant performance gap between commercial and open-source LLMs as agents\"\n      - \"Poor long-term reasoning and instruction following are main obstacles\"\n    how_we_differ: \"AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness\"\n\n  - id: wang2024mint\n    title: \"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\"\n    authors: \"Wang, Wang, Liu, Chen, Yuan, Peng, Ji\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.10691\"\n    category: foundation\n    role: \"Multi-turn agent evaluation benchmark; shows gap between single-turn and multi-turn performance\"\n    relevance: medium\n    key_findings:\n      - \"LLMs benefit 1-8% per turn from tools, 2-17% from language feedback\"\n      - \"Better single-turn performance does not guarantee better multi-turn performance\"\n      - \"SIFT and RLHF generally hurt multi-turn capabilities\"\n    how_we_differ: \"MINT uses GPT-4 simulated users without demographic variation; we investigate dialect-aware calibration and document its failure modes\"\n\n  # ============================================================\n  # METHOD-COMPONENT\n  # ============================================================\n  - id: rafailov2023dpo\n    title: \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\"\n    authors: \"Rafailov, Sharma, Mitchell, Manning, Ermon, Finn\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    url: \"https://arxiv.org/abs/2305.18290\"\n    category: method-component\n    role: \"Core algorithm for our DPO-based behavioral alignment; eliminates need for reward model training\"\n    relevance: high\n    key_findings:\n      - \"DPO directly optimizes policy from preference pairs without explicit reward model\"\n      - \"Computationally lightweight, stable alternative to PPO-based RLHF\"\n      - \"Exceeds PPO-based RLHF in controlling sentiment of generations\"\n    how_we_differ: \"We apply DPO to attempt dialect behavioral calibration and document its systematic failure modes including calibration reversal\"\n\n  - id: zhao2021calibrate\n    title: \"Calibrate Before Use: Improving Few-Shot Performance of Language Models\"\n    authors: \"Zhao, Wallace, Feng, Klein, Singh\"\n    venue: \"ICML 2021\"\n    year: 2021\n    url: \"https://arxiv.org/abs/2102.09690\"\n    category: method-component\n    role: \"Foundational calibration method for LLMs; contextual calibration corrects output distribution biases\"\n    relevance: medium\n    key_findings:\n      - \"Few-shot accuracy varies from near chance to near SOTA depending on prompt format\"\n      - \"Identified majority label bias, recency bias, common token bias\"\n      - \"Contextual calibration with content-free inputs improves accuracy up to 30%\"\n    how_we_differ: \"They calibrate classification outputs; we attempt to calibrate behavioral rates (question rate, politeness) in generation and document why it fails\"\n\n  - id: abdulhai2025consistent\n    title: \"Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning\"\n    authors: \"Abdulhai, Cheng, Clay, Althoff, Levine, Jaques\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2511.00222\"\n    category: method-component\n    role: \"Multi-turn RL for persona consistency; directly relevant to maintaining calibrated behavior across conversation turns\"\n    relevance: high\n    key_findings:\n      - \"Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue\"\n      - \"Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency\"\n      - \"Multi-turn RL reduces inconsistency by >55%\"\n    how_we_differ: \"They optimize persona consistency in general; we document failure modes when targeting dialect behavioral rate calibration\"\n\n  - id: naous2025flipping\n    title: \"Flipping the Dialogue: Training and Evaluating User Language Models\"\n    authors: \"Naous, Laban, Xu, Neville\"\n    venue: \"arXiv 2510.06552\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.06552\"\n    category: method-component\n    role: \"Purpose-built User LMs outperform repurposed assistant LMs as user simulators; validates need for specialized user models\"\n    relevance: high\n    key_findings:\n      - \"Better assistant LMs yield worse user simulators\"\n      - \"UserLM-8b provides more realistic user simulation\"\n      - \"GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation\"\n    how_we_differ: \"They train general User LMs; we document why calibrating user simulator behavioral rates for specific dialect groups fails\"\n\n  - id: li2025persona\n    title: \"LLM Generated Persona is a Promise with a Catch\"\n    authors: \"Li, Chen et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.16527\"\n    category: method-component\n    role: \"Documents systematic biases in LLM-generated personas; explains why naive persona prompting fails for demographic simulation\"\n    relevance: medium\n    key_findings:\n      - \"LLM-generated personas systematically drift toward socially desirable traits\"\n      - \"More LLM-generated content produces more left-leaning, less representative personas\"\n      - \"Bias exists in the persona creation step itself, not just model responses\"\n    how_we_differ: \"We document failure modes when directly injecting behavioral rate targets via BCP, including persona-like completion collapse\"\n\n  - id: wang2024alignment\n    title: \"A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More\"\n    authors: \"Wang, Bi, Pentyala et al.\"\n    venue: \"arXiv 2407.16216\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2407.16216\"\n    category: method-component\n    role: \"Survey unifying alignment methods under single policy gradient framework; reference for our DPO methodology\"\n    relevance: medium\n    key_findings:\n      - \"Unified policy gradient framework for pretraining, SFT, RLHF, RLVR\"\n      - \"DPO is stable and lightweight but sensitive to preference data quality\"\n      - \"Detailed comparison of PPO vs GRPO vs DPO implementation details\"\n    how_we_differ: \"Survey provides methodology reference; we apply DPO to user simulator dialect calibration and document its failure modes\"\n\n  # ============================================================\n  # EVALUATION\n  # ============================================================\n  - id: lin2025redial\n    title: \"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks\"\n    authors: \"Lin et al.\"\n    venue: \"ACL 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.11005\"\n    category: evaluation\n    role: \"First human-annotated SE-AAVE parallel benchmark (ReDial); quantifies LLM performance gaps on AAVE\"\n    relevance: high\n    key_findings:\n      - \"1.2K+ parallel SE-AAVE prompt pairs across reasoning tasks\"\n      - \"Almost all models show statistically significant performance drops on AAVE\"\n      - \"AAVE performance gaps arise from morphosyntactic features and conversational norms\"\n      - \"LLMs struggle more with AAVE than misspelled Standard English\"\n    how_we_differ: \"ReDial evaluates reasoning task performance; we evaluate behavioral rates in user simulation and document calibration failure modes\"\n\n  - id: faisal2024dialectbench\n    title: \"DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages\"\n    authors: \"Faisal et al.\"\n    venue: \"ACL 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2403.11009\"\n    category: evaluation\n    role: \"Large-scale multi-dialect NLP benchmark; documents performance disparities across 281 language varieties\"\n    relevance: medium\n    key_findings:\n      - \"10 NLP tasks, 281 varieties, 40 language clusters\"\n      - \"Substantial performance disparities between standard and non-standard varieties\"\n      - \"Performance gap widens with fine-tuning due to uneven data availability\"\n    how_we_differ: \"DialectBench evaluates NLP task performance; we document failure modes in behavioral calibration of user simulators\"\n\n  - id: gallegos2024bias\n    title: \"Bias and Fairness in Large Language Models: A Survey\"\n    authors: \"Gallegos, Rossi, Barrow et al.\"\n    venue: \"Computational Linguistics, Vol. 50(3)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.00770\"\n    category: evaluation\n    role: \"Comprehensive survey of LLM bias evaluation and mitigation; provides taxonomy of metrics and datasets\"\n    relevance: medium\n    key_findings:\n      - \"Taxonomy of bias metrics at embedding, probability, and generated text levels\"\n      - \"Mitigation methods categorized by intervention stage: pre/in/intra/post-processing\"\n      - \"Consolidated public datasets for bias evaluation\"\n    how_we_differ: \"Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)\"\n\n  - id: parrish2022bbq\n    title: \"BBQ: A Hand-Built Bias Benchmark for Question Answering\"\n    authors: \"Parrish et al.\"\n    venue: \"Findings of ACL 2022\"\n    year: 2022\n    url: \"https://aclanthology.org/2022.findings-acl.165/\"\n    category: evaluation\n    role: \"Established bias benchmark for QA; evaluates social biases across multiple demographic categories\"\n    relevance: low\n    key_findings:\n      - \"58,492 unique examples across multiple bias categories\"\n      - \"Evaluates both individual and intersectional biases\"\n      - \"Standard benchmark for LLM bias evaluation\"\n    how_we_differ: \"BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation\"\n\n  - id: haq2026dialect\n    title: \"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles\"\n    authors: \"Haq, Saldias\"\n    venue: \"arXiv 2604.21152\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21152\"\n    category: evaluation\n    role: \"Closest to direct competitor; quantifies how dialect cues vs explicit identity trigger differential LLM behavior\"\n    relevance: high\n    key_findings:\n      - \"Dialect cues trigger 'dialect jailbreak' reducing refusal probability to near zero\"\n      - \"AAVE/Singlish users receive less sanitized content than SAE users\"\n      - \"Safety alignment is brittle, over-indexed on explicit keywords\"\n      - \"24,000+ responses analyzed across two LLMs\"\n    how_we_differ: \"They characterize the bias mechanism (implicit vs explicit); we document why calibration methods fail to correct behavioral rates\"\n\n  # ============================================================\n  # BACKGROUND\n  # ============================================================\n  - id: joshi2025dialect_survey\n    title: \"Natural Language Processing for Dialects of a Language: A Survey\"\n    authors: \"Joshi, Dabre, Kanojia, Li, Zhan, Haffari, Dippold\"\n    venue: \"ACM Computing Surveys, Vol. 57(6)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2401.05632\"\n    category: background\n    role: \"Comprehensive survey of NLP for dialects; covers datasets, approaches, and performance gaps across dialect varieties\"\n    relevance: medium\n    key_findings:\n      - \"NLP models show systematic performance degradation on dialectal data\"\n      - \"Covers NLU and NLG tasks including dialogue systems\"\n      - \"Equity implications of language technology performance gaps\"\n    how_we_differ: \"Survey provides broad context; we tackle a specific gap in user simulation fairness\"\n\n  - id: rickford1999aave\n    title: \"African American Vernacular English: Features, Evolution, Educational Implications\"\n    authors: \"Rickford, John Russell\"\n    venue: \"Blackwell Publishers (Language in Society series)\"\n    year: 1999\n    url: \"https://www.amazon.com/African-American-Vernacular-English-Implications/dp/0631212450\"\n    category: background\n    role: \"Authoritative reference on AAVE phonological, grammatical, and pragmatic features; grounds our behavioral rate targets\"\n    relevance: medium\n    key_findings:\n      - \"Systematic documentation of AAVE phonological and grammatical features\"\n      - \"AAVE has distinct pragmatic conventions including directness patterns\"\n      - \"AAVE is a fully systematic linguistic variety, not deficient English\"\n    how_we_differ: \"Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward\"\n\n  - id: kachru2008cultures\n    title: \"Cultures, Contexts, and World Englishes\"\n    authors: \"Kachru, Yamuna; Smith, Cecil\"\n    venue: \"Routledge\"\n    year: 2008\n    url: \"https://www.routledge.com/Cultures-Contexts-and-World-Englishes/Kachru-Smith/p/book/9780805847338\"\n    category: background\n    role: \"Framework for Indian English pragmatics; documents politeness strategies and speech act differences in Outer Circle Englishes\"\n    relevance: medium\n    key_findings:\n      - \"Indian English has distinct politeness strategies rooted in face-saving norms\"\n      - \"Requesting and disagreeing strategies differ from Inner Circle varieties\"\n      - \"Three Circles model (Inner/Outer/Expanding) for understanding English variation\"\n    how_we_differ: \"Provides sociolinguistic grounding for Indian English behavioral patterns we calibrate\"\n\n  - id: sekulic2024daus\n    title: \"Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems\"\n    authors: \"Sekulic, Terragni, Guimaraes et al.\"\n    venue: \"SCI-CHAT Workshop 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.13374\"\n    category: background\n    role: \"DAUS: domain-aware user simulator fine-tuned on real dialogues; shows fine-tuning improves goal fulfillment and reduces hallucination\"\n    relevance: medium\n    key_findings:\n      - \"Fine-tuning LLMs on real dialogue examples improves user goal fulfillment\"\n      - \"Mitigates hallucinations in simulator responses\"\n      - \"Domain-aware approach outperforms generic prompting\"\n    how_we_differ: \"DAUS optimizes task completion; we document failure modes when optimizing demographic behavioral fidelity\"\n\n  - id: ahmad2025diversity\n    title: \"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models\"\n    authors: \"Ahmad, Hillmann, Moller\"\n    venue: \"arXiv 2502.12813\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.12813\"\n    category: background\n    role: \"Generates diverse user profiles with varied demographics and conversational styles for dialogue evaluation\"\n    relevance: medium\n    key_findings:\n      - \"GPT-o1 generates more heterogeneous user distributions than GPT-4o\"\n      - \"82.46% task success across 57 dialogue sessions with diverse users\"\n      - \"Captures variation in language styles, knowledge levels, and objectives\"\n    how_we_differ: \"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\"\n\n  # ============================================================\n  # NEW ADDITIONS (scan 2026-05-13)\n  # ============================================================\n\n  # --- FOUNDATION (new) ---\n  - id: sim2real2026gap\n    title: \"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\"\n    authors: \"Zhou, Sun, Xu, Chen, Radev\"\n    venue: \"arXiv 2603.11245\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.11245\"\n    category: foundation\n    role: \"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\"\n    relevance: high\n    key_findings:\n      - \"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\"\n      - \"Simulated users create 'easy mode' that inflates agent success rates above human baseline\"\n      - \"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\"\n      - \"Higher model capability does not yield more faithful user simulation\"\n    how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we attempt BCP and DPO calibration and document why both fail\"\n    scan_date: \"2026-05-13\"\n    note: \"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\"\n\n  # --- METHOD-COMPONENT (new) ---\n  - id: khan2026decoding\n    title: \"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\"\n    authors: \"Khan, Muneeb Ur Raheem\"\n    venue: \"arXiv 2605.02348\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.02348\"\n    category: method-component\n    role: \"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\"\n    relevance: medium\n    key_findings:\n      - \"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\"\n      - \"No weight changes needed — debiasing happens at inference via PRM scoring\"\n      - \"Gate calibration is model-dependent; no one-size-fits-all prompt works\"\n    how_we_differ: \"They debias at decoding time for general fairness; we document failure modes of training-time calibration (BCP+DPO), motivating alternative approaches like decoding-time methods\"\n    scan_date: \"2026-05-13\"\n\n  # --- EVALUATION (new) ---\n  - id: gupta2025endive\n    title: \"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\"\n    authors: \"Gupta, Cheung et al.\"\n    venue: \"Findings of EMNLP 2025 (arXiv 2504.07100)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2504.07100\"\n    category: evaluation\n    role: \"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\"\n    relevance: high\n    key_findings:\n      - \"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\"\n      - \"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\"\n      - \"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\"\n    how_we_differ: \"EnDive evaluates NLP task performance across dialects; we document calibration failure modes for user simulators targeting those same dialect groups\"\n    scan_date: \"2026-05-13\"\n\n  # --- METHOD-COMPONENT (new, Plan B relevant) ---\n  - id: lee2024dpo_toxicity\n    title: \"A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity\"\n    authors: \"Lee, Panda, Yun, Bansal\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2401.01967\"\n    category: method-component\n    role: \"Shows DPO bypasses rather than removes pre-training capabilities; explains mechanistically why DPO+BCP can reverse calibration direction\"\n    relevance: high\n    key_findings:\n      - \"DPO does not remove toxic capabilities, only bypasses them at inference\"\n      - \"Simple un-alignment can revert model to pre-DPO behavior\"\n      - \"Minimal parameter changes allow reversion — alignment is fragile\"\n    how_we_differ: \"They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM4 — explains why DPO training can reverse BCP calibration effect\"\n\n  - id: gupta2026intra_fairness\n    title: \"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment\"\n    authors: \"Paraschou, Heiter, Iosifidis\"\n    venue: \"arXiv 2602.16438\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16438\"\n    category: method-component\n    role: \"Documents bias spillover — targeted debiasing on one dimension causes unintended effects on other dimensions; directly parallels our cross-dimension interference\"\n    relevance: high\n    key_findings:\n      - \"Targeted debiasing can produce unintended negative consequences across other social axes\"\n      - \"Bias spillover effect: altering behavior on one dimension when mitigating another\"\n      - \"Multi-attribute fairness dynamics must be considered in alignment\"\n    how_we_differ: \"They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM2 + FM4 — directly supports cross-dimension interference and DPO spillover claims\"\n\n  - id: basil2025playing_pretend\n    title: \"Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy\"\n    authors: \"Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke\"\n    venue: \"arXiv 2512.05858 (Wharton)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.05858\"\n    category: method-component\n    role: \"Shows persona prompting degrades factual accuracy; BCP is a form of persona/role prompting, explaining completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Expert personas do not improve factual accuracy across benchmarks\"\n      - \"Persona prompting activates instruction-following mode at expense of factual recall\"\n      - \"MMLU accuracy drops from 71.6% baseline to 66.3% with detailed persona\"\n    how_we_differ: \"They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — explains mechanism behind global behavior suppression\"\n\n  - id: hu2026expert_persona\n    title: \"Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM\"\n    authors: \"Hu, Rostami, Thomason\"\n    venue: \"arXiv 2603.18507\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.18507\"\n    category: method-component\n    role: \"Systematically documents persona prompting trade-off: alignment improves but accuracy degrades up to 30pp; directly explains BCP completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Persona prompting improves alignment tasks but degrades knowledge/reasoning tasks\"\n      - \"Performance drops up to 30pp under persona modifications\"\n      - \"More instruction-tuned models are more susceptible to persona-induced accuracy loss\"\n    how_we_differ: \"They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — strongest external evidence for global behavior suppression mechanism\"\n\n  # --- BACKGROUND (new) ---\n  - id: nakash2026divert\n    title: \"Efficient Agent Evaluation via Diversity-Guided User Simulation\"\n    authors: \"Nakash, Kour, Anaby-Tavor\"\n    venue: \"arXiv 2604.21480\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21480\"\n    category: background\n    role: \"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\"\n    relevance: medium\n    key_findings:\n      - \"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\"\n      - \"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\"\n    how_we_differ: \"They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups\"\n    scan_date: \"2026-05-13\"\n\n# ============================================================\n# SUMMARY\n# ============================================================\n# Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)\n# - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)\n# - foundation: 5 (+sim2real2026gap)\n# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +hu2026expert_persona)\n# - evaluation: 6 (+gupta2025endive)\n# - background: 6 (+nakash2026divert)\n# - high relevance: 14, medium: 13, low: 1\n#\n# Plan B scan notes (2026-05-13):\n# - 4 new papers added specifically for Plan B empirical analysis framing\n# - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)\n# - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)\n# - basil2025playing_pretend + hu2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)\n# - No direct competitor found for BCP failure mode analysis — novelty gap confirmed\n# - Also noted but not added:\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures\n",
    "structuredPatch": [
      {
        "oldStart": 318,
        "oldLines": 7,
        "newStart": 318,
        "newLines": 7,
        "lines": [
          "       - \"GPT-o1 generates more heterogeneous user distributions than GPT-4o\"",
          "       - \"82.46% task success across 57 dialogue sessions with diverse users\"",
          "       - \"Captures variation in language styles, knowledge levels, and objectives\"",
          "-    how_we_differ: \"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\"",
          "+    how_we_differ: \"They generate diverse profiles; we document why calibrating specific behavioral rates to match real dialect group distributions fails\"",
          " ",
          "   # ============================================================",
          "   # NEW ADDITIONS (scan 2026-05-13)"
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


### Tool call

_source line 70_

<details open><summary>🔧 Tool call — Edit · `toolu_01Jhn4mAPvhUX4p5cEG9qbxs`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
  "old_string": "how_we_differ: \"They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups\"",
  "new_string": "how_we_differ: \"They optimize evaluation efficiency; we document failure modes in user simulator fidelity calibration for dialect groups\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "56331adb-5eca-4bb8-8a45-fe2100429272",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3iK7ejCbA9r2EwkseUzaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18730,
      "cache_read_input_tokens": 38589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18730
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

_source line 71 · 2026-05-13T07:39:13.914Z_

<details><summary>↩ Tool result · `toolu_01Jhn4mAPvhUX4p5cEG9qbxs`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "66fd9914-9c8a-459c-bc54-129ea4cb8cec",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
    "oldString": "how_we_differ: \"They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups\"",
    "newString": "how_we_differ: \"They optimize evaluation efficiency; we document failure modes in user simulator fidelity calibration for dialect groups\"",
    "originalFile": "papers:\n  # ============================================================\n  # DIRECT-COMPETITOR\n  # ============================================================\n  # 未找到直接竞品。没有现有工作专门做\"校准 LLM 用户模拟器的方言行为率偏差\"。\n  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。\n  # 这验证了 DemoCalib 的新颖性。\n\n  # ============================================================\n  # FOUNDATION\n  # ============================================================\n  - id: seshadri2026lost\n    title: \"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations\"\n    authors: \"Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant\"\n    venue: \"arXiv 2601.17087\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.17087\"\n    category: foundation\n    role: \"Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration\"\n    relevance: high\n    key_findings:\n      - \"Agent success rates vary up to 9pp across different user simulator LLMs\"\n      - \"AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers\"\n      - \"Simulated users introduce conversational artifacts absent from real human users\"\n      - \"Disparities compound significantly with age for AAVE speakers\"\n    how_we_differ: \"They document the problem; we document why both BCP and DPO calibration fail to close the gaps, providing a failure taxonomy\"\n\n  - id: yao2024taubench\n    title: \"tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\"\n    authors: \"Yao et al.\"\n    venue: \"arXiv 2406.12045\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2406.12045\"\n    category: foundation\n    role: \"The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric\"\n    relevance: high\n    key_findings:\n      - \"Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail\"\n      - \"Proposes pass^k metric measuring reliability over multiple trials\"\n      - \"User simulator is LLM-based, enabling behavioral modification\"\n    how_we_differ: \"We extend tau-bench by documenting systematic failure modes when calibrating the user simulator's dialect-specific behavioral rates\"\n\n  - id: liu2024agentbench\n    title: \"AgentBench: Evaluating LLMs as Agents\"\n    authors: \"Liu et al.\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2308.03688\"\n    category: foundation\n    role: \"Multi-environment agent benchmark; establishes evaluation methodology for LLM agents across 8 environments\"\n    relevance: medium\n    key_findings:\n      - \"Significant performance gap between commercial and open-source LLMs as agents\"\n      - \"Poor long-term reasoning and instruction following are main obstacles\"\n    how_we_differ: \"AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness\"\n\n  - id: wang2024mint\n    title: \"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\"\n    authors: \"Wang, Wang, Liu, Chen, Yuan, Peng, Ji\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.10691\"\n    category: foundation\n    role: \"Multi-turn agent evaluation benchmark; shows gap between single-turn and multi-turn performance\"\n    relevance: medium\n    key_findings:\n      - \"LLMs benefit 1-8% per turn from tools, 2-17% from language feedback\"\n      - \"Better single-turn performance does not guarantee better multi-turn performance\"\n      - \"SIFT and RLHF generally hurt multi-turn capabilities\"\n    how_we_differ: \"MINT uses GPT-4 simulated users without demographic variation; we investigate dialect-aware calibration and document its failure modes\"\n\n  # ============================================================\n  # METHOD-COMPONENT\n  # ============================================================\n  - id: rafailov2023dpo\n    title: \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\"\n    authors: \"Rafailov, Sharma, Mitchell, Manning, Ermon, Finn\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    url: \"https://arxiv.org/abs/2305.18290\"\n    category: method-component\n    role: \"Core algorithm for our DPO-based behavioral alignment; eliminates need for reward model training\"\n    relevance: high\n    key_findings:\n      - \"DPO directly optimizes policy from preference pairs without explicit reward model\"\n      - \"Computationally lightweight, stable alternative to PPO-based RLHF\"\n      - \"Exceeds PPO-based RLHF in controlling sentiment of generations\"\n    how_we_differ: \"We apply DPO to attempt dialect behavioral calibration and document its systematic failure modes including calibration reversal\"\n\n  - id: zhao2021calibrate\n    title: \"Calibrate Before Use: Improving Few-Shot Performance of Language Models\"\n    authors: \"Zhao, Wallace, Feng, Klein, Singh\"\n    venue: \"ICML 2021\"\n    year: 2021\n    url: \"https://arxiv.org/abs/2102.09690\"\n    category: method-component\n    role: \"Foundational calibration method for LLMs; contextual calibration corrects output distribution biases\"\n    relevance: medium\n    key_findings:\n      - \"Few-shot accuracy varies from near chance to near SOTA depending on prompt format\"\n      - \"Identified majority label bias, recency bias, common token bias\"\n      - \"Contextual calibration with content-free inputs improves accuracy up to 30%\"\n    how_we_differ: \"They calibrate classification outputs; we attempt to calibrate behavioral rates (question rate, politeness) in generation and document why it fails\"\n\n  - id: abdulhai2025consistent\n    title: \"Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning\"\n    authors: \"Abdulhai, Cheng, Clay, Althoff, Levine, Jaques\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2511.00222\"\n    category: method-component\n    role: \"Multi-turn RL for persona consistency; directly relevant to maintaining calibrated behavior across conversation turns\"\n    relevance: high\n    key_findings:\n      - \"Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue\"\n      - \"Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency\"\n      - \"Multi-turn RL reduces inconsistency by >55%\"\n    how_we_differ: \"They optimize persona consistency in general; we document failure modes when targeting dialect behavioral rate calibration\"\n\n  - id: naous2025flipping\n    title: \"Flipping the Dialogue: Training and Evaluating User Language Models\"\n    authors: \"Naous, Laban, Xu, Neville\"\n    venue: \"arXiv 2510.06552\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.06552\"\n    category: method-component\n    role: \"Purpose-built User LMs outperform repurposed assistant LMs as user simulators; validates need for specialized user models\"\n    relevance: high\n    key_findings:\n      - \"Better assistant LMs yield worse user simulators\"\n      - \"UserLM-8b provides more realistic user simulation\"\n      - \"GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation\"\n    how_we_differ: \"They train general User LMs; we document why calibrating user simulator behavioral rates for specific dialect groups fails\"\n\n  - id: li2025persona\n    title: \"LLM Generated Persona is a Promise with a Catch\"\n    authors: \"Li, Chen et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.16527\"\n    category: method-component\n    role: \"Documents systematic biases in LLM-generated personas; explains why naive persona prompting fails for demographic simulation\"\n    relevance: medium\n    key_findings:\n      - \"LLM-generated personas systematically drift toward socially desirable traits\"\n      - \"More LLM-generated content produces more left-leaning, less representative personas\"\n      - \"Bias exists in the persona creation step itself, not just model responses\"\n    how_we_differ: \"We document failure modes when directly injecting behavioral rate targets via BCP, including persona-like completion collapse\"\n\n  - id: wang2024alignment\n    title: \"A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More\"\n    authors: \"Wang, Bi, Pentyala et al.\"\n    venue: \"arXiv 2407.16216\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2407.16216\"\n    category: method-component\n    role: \"Survey unifying alignment methods under single policy gradient framework; reference for our DPO methodology\"\n    relevance: medium\n    key_findings:\n      - \"Unified policy gradient framework for pretraining, SFT, RLHF, RLVR\"\n      - \"DPO is stable and lightweight but sensitive to preference data quality\"\n      - \"Detailed comparison of PPO vs GRPO vs DPO implementation details\"\n    how_we_differ: \"Survey provides methodology reference; we apply DPO to user simulator dialect calibration and document its failure modes\"\n\n  # ============================================================\n  # EVALUATION\n  # ============================================================\n  - id: lin2025redial\n    title: \"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks\"\n    authors: \"Lin et al.\"\n    venue: \"ACL 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.11005\"\n    category: evaluation\n    role: \"First human-annotated SE-AAVE parallel benchmark (ReDial); quantifies LLM performance gaps on AAVE\"\n    relevance: high\n    key_findings:\n      - \"1.2K+ parallel SE-AAVE prompt pairs across reasoning tasks\"\n      - \"Almost all models show statistically significant performance drops on AAVE\"\n      - \"AAVE performance gaps arise from morphosyntactic features and conversational norms\"\n      - \"LLMs struggle more with AAVE than misspelled Standard English\"\n    how_we_differ: \"ReDial evaluates reasoning task performance; we evaluate behavioral rates in user simulation and document calibration failure modes\"\n\n  - id: faisal2024dialectbench\n    title: \"DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages\"\n    authors: \"Faisal et al.\"\n    venue: \"ACL 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2403.11009\"\n    category: evaluation\n    role: \"Large-scale multi-dialect NLP benchmark; documents performance disparities across 281 language varieties\"\n    relevance: medium\n    key_findings:\n      - \"10 NLP tasks, 281 varieties, 40 language clusters\"\n      - \"Substantial performance disparities between standard and non-standard varieties\"\n      - \"Performance gap widens with fine-tuning due to uneven data availability\"\n    how_we_differ: \"DialectBench evaluates NLP task performance; we document failure modes in behavioral calibration of user simulators\"\n\n  - id: gallegos2024bias\n    title: \"Bias and Fairness in Large Language Models: A Survey\"\n    authors: \"Gallegos, Rossi, Barrow et al.\"\n    venue: \"Computational Linguistics, Vol. 50(3)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.00770\"\n    category: evaluation\n    role: \"Comprehensive survey of LLM bias evaluation and mitigation; provides taxonomy of metrics and datasets\"\n    relevance: medium\n    key_findings:\n      - \"Taxonomy of bias metrics at embedding, probability, and generated text levels\"\n      - \"Mitigation methods categorized by intervention stage: pre/in/intra/post-processing\"\n      - \"Consolidated public datasets for bias evaluation\"\n    how_we_differ: \"Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)\"\n\n  - id: parrish2022bbq\n    title: \"BBQ: A Hand-Built Bias Benchmark for Question Answering\"\n    authors: \"Parrish et al.\"\n    venue: \"Findings of ACL 2022\"\n    year: 2022\n    url: \"https://aclanthology.org/2022.findings-acl.165/\"\n    category: evaluation\n    role: \"Established bias benchmark for QA; evaluates social biases across multiple demographic categories\"\n    relevance: low\n    key_findings:\n      - \"58,492 unique examples across multiple bias categories\"\n      - \"Evaluates both individual and intersectional biases\"\n      - \"Standard benchmark for LLM bias evaluation\"\n    how_we_differ: \"BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation\"\n\n  - id: haq2026dialect\n    title: \"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles\"\n    authors: \"Haq, Saldias\"\n    venue: \"arXiv 2604.21152\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21152\"\n    category: evaluation\n    role: \"Closest to direct competitor; quantifies how dialect cues vs explicit identity trigger differential LLM behavior\"\n    relevance: high\n    key_findings:\n      - \"Dialect cues trigger 'dialect jailbreak' reducing refusal probability to near zero\"\n      - \"AAVE/Singlish users receive less sanitized content than SAE users\"\n      - \"Safety alignment is brittle, over-indexed on explicit keywords\"\n      - \"24,000+ responses analyzed across two LLMs\"\n    how_we_differ: \"They characterize the bias mechanism (implicit vs explicit); we document why calibration methods fail to correct behavioral rates\"\n\n  # ============================================================\n  # BACKGROUND\n  # ============================================================\n  - id: joshi2025dialect_survey\n    title: \"Natural Language Processing for Dialects of a Language: A Survey\"\n    authors: \"Joshi, Dabre, Kanojia, Li, Zhan, Haffari, Dippold\"\n    venue: \"ACM Computing Surveys, Vol. 57(6)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2401.05632\"\n    category: background\n    role: \"Comprehensive survey of NLP for dialects; covers datasets, approaches, and performance gaps across dialect varieties\"\n    relevance: medium\n    key_findings:\n      - \"NLP models show systematic performance degradation on dialectal data\"\n      - \"Covers NLU and NLG tasks including dialogue systems\"\n      - \"Equity implications of language technology performance gaps\"\n    how_we_differ: \"Survey provides broad context; we tackle a specific gap in user simulation fairness\"\n\n  - id: rickford1999aave\n    title: \"African American Vernacular English: Features, Evolution, Educational Implications\"\n    authors: \"Rickford, John Russell\"\n    venue: \"Blackwell Publishers (Language in Society series)\"\n    year: 1999\n    url: \"https://www.amazon.com/African-American-Vernacular-English-Implications/dp/0631212450\"\n    category: background\n    role: \"Authoritative reference on AAVE phonological, grammatical, and pragmatic features; grounds our behavioral rate targets\"\n    relevance: medium\n    key_findings:\n      - \"Systematic documentation of AAVE phonological and grammatical features\"\n      - \"AAVE has distinct pragmatic conventions including directness patterns\"\n      - \"AAVE is a fully systematic linguistic variety, not deficient English\"\n    how_we_differ: \"Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward\"\n\n  - id: kachru2008cultures\n    title: \"Cultures, Contexts, and World Englishes\"\n    authors: \"Kachru, Yamuna; Smith, Cecil\"\n    venue: \"Routledge\"\n    year: 2008\n    url: \"https://www.routledge.com/Cultures-Contexts-and-World-Englishes/Kachru-Smith/p/book/9780805847338\"\n    category: background\n    role: \"Framework for Indian English pragmatics; documents politeness strategies and speech act differences in Outer Circle Englishes\"\n    relevance: medium\n    key_findings:\n      - \"Indian English has distinct politeness strategies rooted in face-saving norms\"\n      - \"Requesting and disagreeing strategies differ from Inner Circle varieties\"\n      - \"Three Circles model (Inner/Outer/Expanding) for understanding English variation\"\n    how_we_differ: \"Provides sociolinguistic grounding for Indian English behavioral patterns we calibrate\"\n\n  - id: sekulic2024daus\n    title: \"Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems\"\n    authors: \"Sekulic, Terragni, Guimaraes et al.\"\n    venue: \"SCI-CHAT Workshop 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.13374\"\n    category: background\n    role: \"DAUS: domain-aware user simulator fine-tuned on real dialogues; shows fine-tuning improves goal fulfillment and reduces hallucination\"\n    relevance: medium\n    key_findings:\n      - \"Fine-tuning LLMs on real dialogue examples improves user goal fulfillment\"\n      - \"Mitigates hallucinations in simulator responses\"\n      - \"Domain-aware approach outperforms generic prompting\"\n    how_we_differ: \"DAUS optimizes task completion; we document failure modes when optimizing demographic behavioral fidelity\"\n\n  - id: ahmad2025diversity\n    title: \"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models\"\n    authors: \"Ahmad, Hillmann, Moller\"\n    venue: \"arXiv 2502.12813\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.12813\"\n    category: background\n    role: \"Generates diverse user profiles with varied demographics and conversational styles for dialogue evaluation\"\n    relevance: medium\n    key_findings:\n      - \"GPT-o1 generates more heterogeneous user distributions than GPT-4o\"\n      - \"82.46% task success across 57 dialogue sessions with diverse users\"\n      - \"Captures variation in language styles, knowledge levels, and objectives\"\n    how_we_differ: \"They generate diverse profiles; we document why calibrating specific behavioral rates to match real dialect group distributions fails\"\n\n  # ============================================================\n  # NEW ADDITIONS (scan 2026-05-13)\n  # ============================================================\n\n  # --- FOUNDATION (new) ---\n  - id: sim2real2026gap\n    title: \"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\"\n    authors: \"Zhou, Sun, Xu, Chen, Radev\"\n    venue: \"arXiv 2603.11245\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.11245\"\n    category: foundation\n    role: \"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\"\n    relevance: high\n    key_findings:\n      - \"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\"\n      - \"Simulated users create 'easy mode' that inflates agent success rates above human baseline\"\n      - \"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\"\n      - \"Higher model capability does not yield more faithful user simulation\"\n    how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we attempt BCP and DPO calibration and document why both fail\"\n    scan_date: \"2026-05-13\"\n    note: \"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\"\n\n  # --- METHOD-COMPONENT (new) ---\n  - id: khan2026decoding\n    title: \"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\"\n    authors: \"Khan, Muneeb Ur Raheem\"\n    venue: \"arXiv 2605.02348\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.02348\"\n    category: method-component\n    role: \"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\"\n    relevance: medium\n    key_findings:\n      - \"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\"\n      - \"No weight changes needed — debiasing happens at inference via PRM scoring\"\n      - \"Gate calibration is model-dependent; no one-size-fits-all prompt works\"\n    how_we_differ: \"They debias at decoding time for general fairness; we document failure modes of training-time calibration (BCP+DPO), motivating alternative approaches like decoding-time methods\"\n    scan_date: \"2026-05-13\"\n\n  # --- EVALUATION (new) ---\n  - id: gupta2025endive\n    title: \"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\"\n    authors: \"Gupta, Cheung et al.\"\n    venue: \"Findings of EMNLP 2025 (arXiv 2504.07100)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2504.07100\"\n    category: evaluation\n    role: \"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\"\n    relevance: high\n    key_findings:\n      - \"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\"\n      - \"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\"\n      - \"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\"\n    how_we_differ: \"EnDive evaluates NLP task performance across dialects; we document calibration failure modes for user simulators targeting those same dialect groups\"\n    scan_date: \"2026-05-13\"\n\n  # --- METHOD-COMPONENT (new, Plan B relevant) ---\n  - id: lee2024dpo_toxicity\n    title: \"A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity\"\n    authors: \"Lee, Panda, Yun, Bansal\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2401.01967\"\n    category: method-component\n    role: \"Shows DPO bypasses rather than removes pre-training capabilities; explains mechanistically why DPO+BCP can reverse calibration direction\"\n    relevance: high\n    key_findings:\n      - \"DPO does not remove toxic capabilities, only bypasses them at inference\"\n      - \"Simple un-alignment can revert model to pre-DPO behavior\"\n      - \"Minimal parameter changes allow reversion — alignment is fragile\"\n    how_we_differ: \"They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM4 — explains why DPO training can reverse BCP calibration effect\"\n\n  - id: gupta2026intra_fairness\n    title: \"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment\"\n    authors: \"Paraschou, Heiter, Iosifidis\"\n    venue: \"arXiv 2602.16438\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16438\"\n    category: method-component\n    role: \"Documents bias spillover — targeted debiasing on one dimension causes unintended effects on other dimensions; directly parallels our cross-dimension interference\"\n    relevance: high\n    key_findings:\n      - \"Targeted debiasing can produce unintended negative consequences across other social axes\"\n      - \"Bias spillover effect: altering behavior on one dimension when mitigating another\"\n      - \"Multi-attribute fairness dynamics must be considered in alignment\"\n    how_we_differ: \"They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM2 + FM4 — directly supports cross-dimension interference and DPO spillover claims\"\n\n  - id: basil2025playing_pretend\n    title: \"Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy\"\n    authors: \"Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke\"\n    venue: \"arXiv 2512.05858 (Wharton)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.05858\"\n    category: method-component\n    role: \"Shows persona prompting degrades factual accuracy; BCP is a form of persona/role prompting, explaining completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Expert personas do not improve factual accuracy across benchmarks\"\n      - \"Persona prompting activates instruction-following mode at expense of factual recall\"\n      - \"MMLU accuracy drops from 71.6% baseline to 66.3% with detailed persona\"\n    how_we_differ: \"They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — explains mechanism behind global behavior suppression\"\n\n  - id: hu2026expert_persona\n    title: \"Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM\"\n    authors: \"Hu, Rostami, Thomason\"\n    venue: \"arXiv 2603.18507\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.18507\"\n    category: method-component\n    role: \"Systematically documents persona prompting trade-off: alignment improves but accuracy degrades up to 30pp; directly explains BCP completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Persona prompting improves alignment tasks but degrades knowledge/reasoning tasks\"\n      - \"Performance drops up to 30pp under persona modifications\"\n      - \"More instruction-tuned models are more susceptible to persona-induced accuracy loss\"\n    how_we_differ: \"They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — strongest external evidence for global behavior suppression mechanism\"\n\n  # --- BACKGROUND (new) ---\n  - id: nakash2026divert\n    title: \"Efficient Agent Evaluation via Diversity-Guided User Simulation\"\n    authors: \"Nakash, Kour, Anaby-Tavor\"\n    venue: \"arXiv 2604.21480\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21480\"\n    category: background\n    role: \"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\"\n    relevance: medium\n    key_findings:\n      - \"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\"\n      - \"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\"\n    how_we_differ: \"They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups\"\n    scan_date: \"2026-05-13\"\n\n# ============================================================\n# SUMMARY\n# ============================================================\n# Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)\n# - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)\n# - foundation: 5 (+sim2real2026gap)\n# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +hu2026expert_persona)\n# - evaluation: 6 (+gupta2025endive)\n# - background: 6 (+nakash2026divert)\n# - high relevance: 14, medium: 13, low: 1\n#\n# Plan B scan notes (2026-05-13):\n# - 4 new papers added specifically for Plan B empirical analysis framing\n# - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)\n# - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)\n# - basil2025playing_pretend + hu2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)\n# - No direct competitor found for BCP failure mode analysis — novelty gap confirmed\n# - Also noted but not added:\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures\n",
    "structuredPatch": [
      {
        "oldStart": 459,
        "oldLines": 7,
        "newStart": 459,
        "newLines": 7,
        "lines": [
          "     key_findings:",
          "       - \"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\"",
          "       - \"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\"",
          "-    how_we_differ: \"They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups\"",
          "+    how_we_differ: \"They optimize evaluation efficiency; we document failure modes in user simulator fidelity calibration for dialect groups\"",
          "     scan_date: \"2026-05-13\"",
          " ",
          " # ============================================================"
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


### Tool call

_source line 72_

<details open><summary>🔧 Tool call — Edit · `toolu_016oJSyNycV9xGiQYrWQ73Rq`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
  "old_string": "how_we_differ: \"Provides sociolinguistic grounding for Indian English behavioral patterns we calibrate\"",
  "new_string": "how_we_differ: \"Provides sociolinguistic grounding for Indian English behavioral patterns we attempt to calibrate\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "7cd6cb34-e10c-4e70-a175-7ad8e38e0270",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3iK7ejCbA9r2EwkseUzaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18730,
      "cache_read_input_tokens": 38589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18730
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

_source line 73 · 2026-05-13T07:39:14.854Z_

<details><summary>↩ Tool result · `toolu_016oJSyNycV9xGiQYrWQ73Rq`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "e21ae0cf-f737-40b5-85c1-71a505444368",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
    "oldString": "how_we_differ: \"Provides sociolinguistic grounding for Indian English behavioral patterns we calibrate\"",
    "newString": "how_we_differ: \"Provides sociolinguistic grounding for Indian English behavioral patterns we attempt to calibrate\"",
    "originalFile": "papers:\n  # ============================================================\n  # DIRECT-COMPETITOR\n  # ============================================================\n  # 未找到直接竞品。没有现有工作专门做\"校准 LLM 用户模拟器的方言行为率偏差\"。\n  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。\n  # 这验证了 DemoCalib 的新颖性。\n\n  # ============================================================\n  # FOUNDATION\n  # ============================================================\n  - id: seshadri2026lost\n    title: \"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations\"\n    authors: \"Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant\"\n    venue: \"arXiv 2601.17087\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.17087\"\n    category: foundation\n    role: \"Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration\"\n    relevance: high\n    key_findings:\n      - \"Agent success rates vary up to 9pp across different user simulator LLMs\"\n      - \"AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers\"\n      - \"Simulated users introduce conversational artifacts absent from real human users\"\n      - \"Disparities compound significantly with age for AAVE speakers\"\n    how_we_differ: \"They document the problem; we document why both BCP and DPO calibration fail to close the gaps, providing a failure taxonomy\"\n\n  - id: yao2024taubench\n    title: \"tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\"\n    authors: \"Yao et al.\"\n    venue: \"arXiv 2406.12045\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2406.12045\"\n    category: foundation\n    role: \"The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric\"\n    relevance: high\n    key_findings:\n      - \"Even gpt-4o succeeds on <50% of tasks; pass^8 <25% in retail\"\n      - \"Proposes pass^k metric measuring reliability over multiple trials\"\n      - \"User simulator is LLM-based, enabling behavioral modification\"\n    how_we_differ: \"We extend tau-bench by documenting systematic failure modes when calibrating the user simulator's dialect-specific behavioral rates\"\n\n  - id: liu2024agentbench\n    title: \"AgentBench: Evaluating LLMs as Agents\"\n    authors: \"Liu et al.\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2308.03688\"\n    category: foundation\n    role: \"Multi-environment agent benchmark; establishes evaluation methodology for LLM agents across 8 environments\"\n    relevance: medium\n    key_findings:\n      - \"Significant performance gap between commercial and open-source LLMs as agents\"\n      - \"Poor long-term reasoning and instruction following are main obstacles\"\n    how_we_differ: \"AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness\"\n\n  - id: wang2024mint\n    title: \"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\"\n    authors: \"Wang, Wang, Liu, Chen, Yuan, Peng, Ji\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.10691\"\n    category: foundation\n    role: \"Multi-turn agent evaluation benchmark; shows gap between single-turn and multi-turn performance\"\n    relevance: medium\n    key_findings:\n      - \"LLMs benefit 1-8% per turn from tools, 2-17% from language feedback\"\n      - \"Better single-turn performance does not guarantee better multi-turn performance\"\n      - \"SIFT and RLHF generally hurt multi-turn capabilities\"\n    how_we_differ: \"MINT uses GPT-4 simulated users without demographic variation; we investigate dialect-aware calibration and document its failure modes\"\n\n  # ============================================================\n  # METHOD-COMPONENT\n  # ============================================================\n  - id: rafailov2023dpo\n    title: \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\"\n    authors: \"Rafailov, Sharma, Mitchell, Manning, Ermon, Finn\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    url: \"https://arxiv.org/abs/2305.18290\"\n    category: method-component\n    role: \"Core algorithm for our DPO-based behavioral alignment; eliminates need for reward model training\"\n    relevance: high\n    key_findings:\n      - \"DPO directly optimizes policy from preference pairs without explicit reward model\"\n      - \"Computationally lightweight, stable alternative to PPO-based RLHF\"\n      - \"Exceeds PPO-based RLHF in controlling sentiment of generations\"\n    how_we_differ: \"We apply DPO to attempt dialect behavioral calibration and document its systematic failure modes including calibration reversal\"\n\n  - id: zhao2021calibrate\n    title: \"Calibrate Before Use: Improving Few-Shot Performance of Language Models\"\n    authors: \"Zhao, Wallace, Feng, Klein, Singh\"\n    venue: \"ICML 2021\"\n    year: 2021\n    url: \"https://arxiv.org/abs/2102.09690\"\n    category: method-component\n    role: \"Foundational calibration method for LLMs; contextual calibration corrects output distribution biases\"\n    relevance: medium\n    key_findings:\n      - \"Few-shot accuracy varies from near chance to near SOTA depending on prompt format\"\n      - \"Identified majority label bias, recency bias, common token bias\"\n      - \"Contextual calibration with content-free inputs improves accuracy up to 30%\"\n    how_we_differ: \"They calibrate classification outputs; we attempt to calibrate behavioral rates (question rate, politeness) in generation and document why it fails\"\n\n  - id: abdulhai2025consistent\n    title: \"Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning\"\n    authors: \"Abdulhai, Cheng, Clay, Althoff, Levine, Jaques\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2511.00222\"\n    category: method-component\n    role: \"Multi-turn RL for persona consistency; directly relevant to maintaining calibrated behavior across conversation turns\"\n    relevance: high\n    key_findings:\n      - \"Off-the-shelf LLMs drift from assigned personas over multi-turn dialogue\"\n      - \"Three automatic metrics: prompt-to-line, line-to-line, Q&A consistency\"\n      - \"Multi-turn RL reduces inconsistency by >55%\"\n    how_we_differ: \"They optimize persona consistency in general; we document failure modes when targeting dialect behavioral rate calibration\"\n\n  - id: naous2025flipping\n    title: \"Flipping the Dialogue: Training and Evaluating User Language Models\"\n    authors: \"Naous, Laban, Xu, Neville\"\n    venue: \"arXiv 2510.06552\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.06552\"\n    category: method-component\n    role: \"Purpose-built User LMs outperform repurposed assistant LMs as user simulators; validates need for specialized user models\"\n    relevance: high\n    key_findings:\n      - \"Better assistant LMs yield worse user simulators\"\n      - \"UserLM-8b provides more realistic user simulation\"\n      - \"GPT-4o performance drops from 74.6% to 57.4% under realistic user simulation\"\n    how_we_differ: \"They train general User LMs; we document why calibrating user simulator behavioral rates for specific dialect groups fails\"\n\n  - id: li2025persona\n    title: \"LLM Generated Persona is a Promise with a Catch\"\n    authors: \"Li, Chen et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.16527\"\n    category: method-component\n    role: \"Documents systematic biases in LLM-generated personas; explains why naive persona prompting fails for demographic simulation\"\n    relevance: medium\n    key_findings:\n      - \"LLM-generated personas systematically drift toward socially desirable traits\"\n      - \"More LLM-generated content produces more left-leaning, less representative personas\"\n      - \"Bias exists in the persona creation step itself, not just model responses\"\n    how_we_differ: \"We document failure modes when directly injecting behavioral rate targets via BCP, including persona-like completion collapse\"\n\n  - id: wang2024alignment\n    title: \"A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More\"\n    authors: \"Wang, Bi, Pentyala et al.\"\n    venue: \"arXiv 2407.16216\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2407.16216\"\n    category: method-component\n    role: \"Survey unifying alignment methods under single policy gradient framework; reference for our DPO methodology\"\n    relevance: medium\n    key_findings:\n      - \"Unified policy gradient framework for pretraining, SFT, RLHF, RLVR\"\n      - \"DPO is stable and lightweight but sensitive to preference data quality\"\n      - \"Detailed comparison of PPO vs GRPO vs DPO implementation details\"\n    how_we_differ: \"Survey provides methodology reference; we apply DPO to user simulator dialect calibration and document its failure modes\"\n\n  # ============================================================\n  # EVALUATION\n  # ============================================================\n  - id: lin2025redial\n    title: \"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks\"\n    authors: \"Lin et al.\"\n    venue: \"ACL 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.11005\"\n    category: evaluation\n    role: \"First human-annotated SE-AAVE parallel benchmark (ReDial); quantifies LLM performance gaps on AAVE\"\n    relevance: high\n    key_findings:\n      - \"1.2K+ parallel SE-AAVE prompt pairs across reasoning tasks\"\n      - \"Almost all models show statistically significant performance drops on AAVE\"\n      - \"AAVE performance gaps arise from morphosyntactic features and conversational norms\"\n      - \"LLMs struggle more with AAVE than misspelled Standard English\"\n    how_we_differ: \"ReDial evaluates reasoning task performance; we evaluate behavioral rates in user simulation and document calibration failure modes\"\n\n  - id: faisal2024dialectbench\n    title: \"DialectBench: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages\"\n    authors: \"Faisal et al.\"\n    venue: \"ACL 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2403.11009\"\n    category: evaluation\n    role: \"Large-scale multi-dialect NLP benchmark; documents performance disparities across 281 language varieties\"\n    relevance: medium\n    key_findings:\n      - \"10 NLP tasks, 281 varieties, 40 language clusters\"\n      - \"Substantial performance disparities between standard and non-standard varieties\"\n      - \"Performance gap widens with fine-tuning due to uneven data availability\"\n    how_we_differ: \"DialectBench evaluates NLP task performance; we document failure modes in behavioral calibration of user simulators\"\n\n  - id: gallegos2024bias\n    title: \"Bias and Fairness in Large Language Models: A Survey\"\n    authors: \"Gallegos, Rossi, Barrow et al.\"\n    venue: \"Computational Linguistics, Vol. 50(3)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2309.00770\"\n    category: evaluation\n    role: \"Comprehensive survey of LLM bias evaluation and mitigation; provides taxonomy of metrics and datasets\"\n    relevance: medium\n    key_findings:\n      - \"Taxonomy of bias metrics at embedding, probability, and generated text levels\"\n      - \"Mitigation methods categorized by intervention stage: pre/in/intra/post-processing\"\n      - \"Consolidated public datasets for bias evaluation\"\n    how_we_differ: \"Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)\"\n\n  - id: parrish2022bbq\n    title: \"BBQ: A Hand-Built Bias Benchmark for Question Answering\"\n    authors: \"Parrish et al.\"\n    venue: \"Findings of ACL 2022\"\n    year: 2022\n    url: \"https://aclanthology.org/2022.findings-acl.165/\"\n    category: evaluation\n    role: \"Established bias benchmark for QA; evaluates social biases across multiple demographic categories\"\n    relevance: low\n    key_findings:\n      - \"58,492 unique examples across multiple bias categories\"\n      - \"Evaluates both individual and intersectional biases\"\n      - \"Standard benchmark for LLM bias evaluation\"\n    how_we_differ: \"BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation\"\n\n  - id: haq2026dialect\n    title: \"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles\"\n    authors: \"Haq, Saldias\"\n    venue: \"arXiv 2604.21152\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21152\"\n    category: evaluation\n    role: \"Closest to direct competitor; quantifies how dialect cues vs explicit identity trigger differential LLM behavior\"\n    relevance: high\n    key_findings:\n      - \"Dialect cues trigger 'dialect jailbreak' reducing refusal probability to near zero\"\n      - \"AAVE/Singlish users receive less sanitized content than SAE users\"\n      - \"Safety alignment is brittle, over-indexed on explicit keywords\"\n      - \"24,000+ responses analyzed across two LLMs\"\n    how_we_differ: \"They characterize the bias mechanism (implicit vs explicit); we document why calibration methods fail to correct behavioral rates\"\n\n  # ============================================================\n  # BACKGROUND\n  # ============================================================\n  - id: joshi2025dialect_survey\n    title: \"Natural Language Processing for Dialects of a Language: A Survey\"\n    authors: \"Joshi, Dabre, Kanojia, Li, Zhan, Haffari, Dippold\"\n    venue: \"ACM Computing Surveys, Vol. 57(6)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2401.05632\"\n    category: background\n    role: \"Comprehensive survey of NLP for dialects; covers datasets, approaches, and performance gaps across dialect varieties\"\n    relevance: medium\n    key_findings:\n      - \"NLP models show systematic performance degradation on dialectal data\"\n      - \"Covers NLU and NLG tasks including dialogue systems\"\n      - \"Equity implications of language technology performance gaps\"\n    how_we_differ: \"Survey provides broad context; we tackle a specific gap in user simulation fairness\"\n\n  - id: rickford1999aave\n    title: \"African American Vernacular English: Features, Evolution, Educational Implications\"\n    authors: \"Rickford, John Russell\"\n    venue: \"Blackwell Publishers (Language in Society series)\"\n    year: 1999\n    url: \"https://www.amazon.com/African-American-Vernacular-English-Implications/dp/0631212450\"\n    category: background\n    role: \"Authoritative reference on AAVE phonological, grammatical, and pragmatic features; grounds our behavioral rate targets\"\n    relevance: medium\n    key_findings:\n      - \"Systematic documentation of AAVE phonological and grammatical features\"\n      - \"AAVE has distinct pragmatic conventions including directness patterns\"\n      - \"AAVE is a fully systematic linguistic variety, not deficient English\"\n    how_we_differ: \"Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward\"\n\n  - id: kachru2008cultures\n    title: \"Cultures, Contexts, and World Englishes\"\n    authors: \"Kachru, Yamuna; Smith, Cecil\"\n    venue: \"Routledge\"\n    year: 2008\n    url: \"https://www.routledge.com/Cultures-Contexts-and-World-Englishes/Kachru-Smith/p/book/9780805847338\"\n    category: background\n    role: \"Framework for Indian English pragmatics; documents politeness strategies and speech act differences in Outer Circle Englishes\"\n    relevance: medium\n    key_findings:\n      - \"Indian English has distinct politeness strategies rooted in face-saving norms\"\n      - \"Requesting and disagreeing strategies differ from Inner Circle varieties\"\n      - \"Three Circles model (Inner/Outer/Expanding) for understanding English variation\"\n    how_we_differ: \"Provides sociolinguistic grounding for Indian English behavioral patterns we calibrate\"\n\n  - id: sekulic2024daus\n    title: \"Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems\"\n    authors: \"Sekulic, Terragni, Guimaraes et al.\"\n    venue: \"SCI-CHAT Workshop 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.13374\"\n    category: background\n    role: \"DAUS: domain-aware user simulator fine-tuned on real dialogues; shows fine-tuning improves goal fulfillment and reduces hallucination\"\n    relevance: medium\n    key_findings:\n      - \"Fine-tuning LLMs on real dialogue examples improves user goal fulfillment\"\n      - \"Mitigates hallucinations in simulator responses\"\n      - \"Domain-aware approach outperforms generic prompting\"\n    how_we_differ: \"DAUS optimizes task completion; we document failure modes when optimizing demographic behavioral fidelity\"\n\n  - id: ahmad2025diversity\n    title: \"Simulating User Diversity in Task-Oriented Dialogue Systems using Large Language Models\"\n    authors: \"Ahmad, Hillmann, Moller\"\n    venue: \"arXiv 2502.12813\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.12813\"\n    category: background\n    role: \"Generates diverse user profiles with varied demographics and conversational styles for dialogue evaluation\"\n    relevance: medium\n    key_findings:\n      - \"GPT-o1 generates more heterogeneous user distributions than GPT-4o\"\n      - \"82.46% task success across 57 dialogue sessions with diverse users\"\n      - \"Captures variation in language styles, knowledge levels, and objectives\"\n    how_we_differ: \"They generate diverse profiles; we document why calibrating specific behavioral rates to match real dialect group distributions fails\"\n\n  # ============================================================\n  # NEW ADDITIONS (scan 2026-05-13)\n  # ============================================================\n\n  # --- FOUNDATION (new) ---\n  - id: sim2real2026gap\n    title: \"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\"\n    authors: \"Zhou, Sun, Xu, Chen, Radev\"\n    venue: \"arXiv 2603.11245\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.11245\"\n    category: foundation\n    role: \"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\"\n    relevance: high\n    key_findings:\n      - \"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\"\n      - \"Simulated users create 'easy mode' that inflates agent success rates above human baseline\"\n      - \"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\"\n      - \"Higher model capability does not yield more faithful user simulation\"\n    how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we attempt BCP and DPO calibration and document why both fail\"\n    scan_date: \"2026-05-13\"\n    note: \"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\"\n\n  # --- METHOD-COMPONENT (new) ---\n  - id: khan2026decoding\n    title: \"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\"\n    authors: \"Khan, Muneeb Ur Raheem\"\n    venue: \"arXiv 2605.02348\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.02348\"\n    category: method-component\n    role: \"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\"\n    relevance: medium\n    key_findings:\n      - \"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\"\n      - \"No weight changes needed — debiasing happens at inference via PRM scoring\"\n      - \"Gate calibration is model-dependent; no one-size-fits-all prompt works\"\n    how_we_differ: \"They debias at decoding time for general fairness; we document failure modes of training-time calibration (BCP+DPO), motivating alternative approaches like decoding-time methods\"\n    scan_date: \"2026-05-13\"\n\n  # --- EVALUATION (new) ---\n  - id: gupta2025endive\n    title: \"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\"\n    authors: \"Gupta, Cheung et al.\"\n    venue: \"Findings of EMNLP 2025 (arXiv 2504.07100)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2504.07100\"\n    category: evaluation\n    role: \"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\"\n    relevance: high\n    key_findings:\n      - \"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\"\n      - \"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\"\n      - \"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\"\n    how_we_differ: \"EnDive evaluates NLP task performance across dialects; we document calibration failure modes for user simulators targeting those same dialect groups\"\n    scan_date: \"2026-05-13\"\n\n  # --- METHOD-COMPONENT (new, Plan B relevant) ---\n  - id: lee2024dpo_toxicity\n    title: \"A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity\"\n    authors: \"Lee, Panda, Yun, Bansal\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2401.01967\"\n    category: method-component\n    role: \"Shows DPO bypasses rather than removes pre-training capabilities; explains mechanistically why DPO+BCP can reverse calibration direction\"\n    relevance: high\n    key_findings:\n      - \"DPO does not remove toxic capabilities, only bypasses them at inference\"\n      - \"Simple un-alignment can revert model to pre-DPO behavior\"\n      - \"Minimal parameter changes allow reversion — alignment is fragile\"\n    how_we_differ: \"They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM4 — explains why DPO training can reverse BCP calibration effect\"\n\n  - id: gupta2026intra_fairness\n    title: \"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment\"\n    authors: \"Paraschou, Heiter, Iosifidis\"\n    venue: \"arXiv 2602.16438\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16438\"\n    category: method-component\n    role: \"Documents bias spillover — targeted debiasing on one dimension causes unintended effects on other dimensions; directly parallels our cross-dimension interference\"\n    relevance: high\n    key_findings:\n      - \"Targeted debiasing can produce unintended negative consequences across other social axes\"\n      - \"Bias spillover effect: altering behavior on one dimension when mitigating another\"\n      - \"Multi-attribute fairness dynamics must be considered in alignment\"\n    how_we_differ: \"They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM2 + FM4 — directly supports cross-dimension interference and DPO spillover claims\"\n\n  - id: basil2025playing_pretend\n    title: \"Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy\"\n    authors: \"Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke\"\n    venue: \"arXiv 2512.05858 (Wharton)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.05858\"\n    category: method-component\n    role: \"Shows persona prompting degrades factual accuracy; BCP is a form of persona/role prompting, explaining completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Expert personas do not improve factual accuracy across benchmarks\"\n      - \"Persona prompting activates instruction-following mode at expense of factual recall\"\n      - \"MMLU accuracy drops from 71.6% baseline to 66.3% with detailed persona\"\n    how_we_differ: \"They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — explains mechanism behind global behavior suppression\"\n\n  - id: hu2026expert_persona\n    title: \"Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM\"\n    authors: \"Hu, Rostami, Thomason\"\n    venue: \"arXiv 2603.18507\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.18507\"\n    category: method-component\n    role: \"Systematically documents persona prompting trade-off: alignment improves but accuracy degrades up to 30pp; directly explains BCP completion collapse\"\n    relevance: high\n    key_findings:\n      - \"Persona prompting improves alignment tasks but degrades knowledge/reasoning tasks\"\n      - \"Performance drops up to 30pp under persona modifications\"\n      - \"More instruction-tuned models are more susceptible to persona-induced accuracy loss\"\n    how_we_differ: \"They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts\"\n    scan_date: \"2026-05-13\"\n    plan_b_relevance: \"FM1 — strongest external evidence for global behavior suppression mechanism\"\n\n  # --- BACKGROUND (new) ---\n  - id: nakash2026divert\n    title: \"Efficient Agent Evaluation via Diversity-Guided User Simulation\"\n    authors: \"Nakash, Kour, Anaby-Tavor\"\n    venue: \"arXiv 2604.21480\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21480\"\n    category: background\n    role: \"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\"\n    relevance: medium\n    key_findings:\n      - \"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\"\n      - \"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\"\n    how_we_differ: \"They optimize evaluation efficiency; we document failure modes in user simulator fidelity calibration for dialect groups\"\n    scan_date: \"2026-05-13\"\n\n# ============================================================\n# SUMMARY\n# ============================================================\n# Total: 28 papers (updated 2026-05-13, +8 new, +4 Plan B scan)\n# - direct-competitor: 0 (novelty still confirmed — no one has done systematic BCP failure analysis)\n# - foundation: 5 (+sim2real2026gap)\n# - method-component: 12 (+khan2026decoding, +lee2024dpo_toxicity, +gupta2026intra_fairness, +basil2025playing_pretend, +hu2026expert_persona)\n# - evaluation: 6 (+gupta2025endive)\n# - background: 6 (+nakash2026divert)\n# - high relevance: 14, medium: 13, low: 1\n#\n# Plan B scan notes (2026-05-13):\n# - 4 new papers added specifically for Plan B empirical analysis framing\n# - lee2024dpo_toxicity: mechanistic explanation for FM4 (DPO+BCP reversal)\n# - gupta2026intra_fairness: external evidence for FM2 (cross-dimension interference) + FM4 (spillover)\n# - basil2025playing_pretend + hu2026expert_persona: external evidence for FM1 (completion collapse via persona prompting)\n# - No direct competitor found for BCP failure mode analysis — novelty gap confirmed\n# - Also noted but not added:\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures\n",
    "structuredPatch": [
      {
        "oldStart": 288,
        "oldLines": 7,
        "newStart": 288,
        "newLines": 7,
        "lines": [
          "       - \"Indian English has distinct politeness strategies rooted in face-saving norms\"",
          "       - \"Requesting and disagreeing strategies differ from Inner Circle varieties\"",
          "       - \"Three Circles model (Inner/Outer/Expanding) for understanding English variation\"",
          "-    how_we_differ: \"Provides sociolinguistic grounding for Indian English behavioral patterns we calibrate\"",
          "+    how_we_differ: \"Provides sociolinguistic grounding for Indian English behavioral patterns we attempt to calibrate\"",
          " ",
          "   - id: sekulic2024daus",
          "     title: \"Reliable LLM-based User Simulator for Task-Oriented Dialogue Systems\""
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

_source line 74_

<details><summary>Logged reasoning block</summary>

```text
All 26 edits succeeded. Now let me verify the changes by reading key sections of both files, and then write them back using save_project_file for paper_framing.md. For literature_map.yaml, since save_project_file doesn't support it, the direct Edit tool edits should already be persisted.

Actually wait - looking at the save_project_file tool description: "Writable: memory.md, writing_plan.yaml, paper_framing.md." So I can save paper_framing.md through it. But the edits were already applied directly to the file on disk. 

Let me verify the key changes in both files to make sure everything took effect properly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "a47d36bd-e600-45d2-9841-bff7bc7b97a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fx2KdXnb54otv3GTEFR8ra",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 56001,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 56001
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

_source line 75_

所有 26 项编辑均已成功。验证关键修改点。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "b7f5f0b2-22cc-4b41-a56a-3ad1cc5d6f1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fx2KdXnb54otv3GTEFR8ra",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 56001,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 56001
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

_source line 76_

<details open><summary>🔧 Tool call — Grep · `toolu_01DPTJ4B8QL6S3V3836uZmNS`</summary>

```json
{
  "pattern": "anonymous2026expert_persona",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl",
  "output_mode": "count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "550692e3-6e58-4c49-854b-a58884cbfaa7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fx2KdXnb54otv3GTEFR8ra",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 56001,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 56001
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

_source line 77 · 2026-05-13T07:39:24.284Z_

<details><summary>↩ Tool result · `toolu_01DPTJ4B8QL6S3V3836uZmNS`</summary>

```text
logs/chats/feishu_group_oc_fb6c152ae234e83319bfe1def3ff07ed_reviewer.jsonl:6
logs/chats/feishu_group_oc_fb6c152ae234e83319bfe1def3ff07ed.jsonl:5
logs/chats/feishu_group_oc_e29466e3c67ee1f304a0f0552caa7268_director.jsonl:5
logs/workers/worker_research_plan-b-literature_20260513T062721.log:4
logs/workers/worker_research_reference-audit_20260513T063327_result.json:1
logs/workers/worker_research_reference-audit_20260513T063327.log:6
logs/workers/worker_writing_plan-b-framing-draft_20260513T072756.log:2
logs/workers/worker_fix_literature-map-authors_20260513T063747.log:10
logs/workers/worker_fix_literature-map-authors_20260513T063747_result.json:1
logs/workers/worker_fix_framing-reviewer-corrections_20260513T073508.log:16
artifacts/reference_audit_report.md:4
artifacts/_project/report/reference_audit_report.md:4

Found 64 total occurrences across 12 files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "a88a86f2-0f43-4a25-9ec3-f98ee62694e3",
  "tool_use_result": {
    "mode": "count",
    "numFiles": 12,
    "filenames": [],
    "content": "logs/chats/feishu_group_oc_fb6c152ae234e83319bfe1def3ff07ed_reviewer.jsonl:6\nlogs/chats/feishu_group_oc_fb6c152ae234e83319bfe1def3ff07ed.jsonl:5\nlogs/chats/feishu_group_oc_e29466e3c67ee1f304a0f0552caa7268_director.jsonl:5\nlogs/workers/worker_research_plan-b-literature_20260513T062721.log:4\nlogs/workers/worker_research_reference-audit_20260513T063327_result.json:1\nlogs/workers/worker_research_reference-audit_20260513T063327.log:6\nlogs/workers/worker_writing_plan-b-framing-draft_20260513T072756.log:2\nlogs/workers/worker_fix_literature-map-authors_20260513T063747.log:10\nlogs/workers/worker_fix_literature-map-authors_20260513T063747_result.json:1\nlogs/workers/worker_fix_framing-reviewer-corrections_20260513T073508.log:16\nartifacts/reference_audit_report.md:4\nartifacts/_project/report/reference_audit_report.md:4",
    "numMatches": 64
  }
}
```

</details>

---


### Tool call

_source line 78_

<details open><summary>🔧 Tool call — Read · `toolu_014LdVoNLudjtSnbA9V9F5dx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md",
  "offset": 42,
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
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "ef59c551-af3c-4587-a17d-2a7ac0446142",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fx2KdXnb54otv3GTEFR8ra",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 56001,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 56001
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

_source line 79 · 2026-05-13T07:39:25.185Z_

<details><summary>↩ Tool result · `toolu_014LdVoNLudjtSnbA9V9F5dx`</summary>

```text
42	### C1: BCP produces three systematic failure mechanisms
43	**Evidence strength**: Moderate (single model, single run, n=19-20 per variant)
44	
45	| Failure Mode | Description | Key Metric | exp_id |
46	|---|---|---|---|
47	| FM1: Global Behavior Suppression | BCP calibration prompts collapse task completion regardless of target dimension | completion retention 52.3% (threshold ≥80%) | mvp-004 |
48	| FM2: Cross-Dimension Interference | Targeting one behavioral dimension perturbs non-targeted dimensions | politeness -25.6% when targeting question_rate; question_rate -52.3% when targeting politeness | mvp-004 |
49	| FM3: Overcorrection Rebound | Requesting extreme behavioral shift causes model to rebound in opposite direction | overcorrected politeness +4.2pp ~ +10.4pp above baseline (4 runs, 4/4 consistent) | hgate-dpo003-merged |
50	
51	**Supporting numbers (mvp-004, Qwen2.5-7B-Instruct, n=19-20)**:
52	- FM1: aave completion 0.100 vs baseline 0.368 (-72.8%); indian 0.150 (-59.2%); mean calibrated 0.193
53	- FM2: single_dim_question politeness drops 25.6% (non-target); single_dim_politeness question_rate drops 52.3% (non-target)
54	  - **Base rate caveat**: question_rate baseline = 0.044 (~0.8 questions/task); 52.3% drop = absolute change from ~0.044 to ~0.021. Paper must report both absolute values and relative changes.
55	- FM3: **[primary]** hgate-dpo003-merged overcorrected politeness mean 0.574 vs baseline 0.502, gap +7.2pp (+14.3% relative), range +4.2pp ~ +10.4pp, 4/4 runs consistent; **[auxiliary]** mvp-004 single run: 0.605 vs 0.559 (+4.6pp, +8.2% relative)
56	
57	**External support**:
58	- FM1: basil2025playing_pretend (persona prompting drops MMLU 71.6%→66.3%); hu2026expert_persona (accuracy degradation up to 30pp under persona)
59	- FM2: gupta2026intra_fairness (bias spillover effect in targeted alignment)
60	- FM3: no direct external parallel — novel observation
61	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "8206ee4b-ba1d-40f1-a950-08fa4dd31a77",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md",
      "content": "### C1: BCP produces three systematic failure mechanisms\n**Evidence strength**: Moderate (single model, single run, n=19-20 per variant)\n\n| Failure Mode | Description | Key Metric | exp_id |\n|---|---|---|---|\n| FM1: Global Behavior Suppression | BCP calibration prompts collapse task completion regardless of target dimension | completion retention 52.3% (threshold ≥80%) | mvp-004 |\n| FM2: Cross-Dimension Interference | Targeting one behavioral dimension perturbs non-targeted dimensions | politeness -25.6% when targeting question_rate; question_rate -52.3% when targeting politeness | mvp-004 |\n| FM3: Overcorrection Rebound | Requesting extreme behavioral shift causes model to rebound in opposite direction | overcorrected politeness +4.2pp ~ +10.4pp above baseline (4 runs, 4/4 consistent) | hgate-dpo003-merged |\n\n**Supporting numbers (mvp-004, Qwen2.5-7B-Instruct, n=19-20)**:\n- FM1: aave completion 0.100 vs baseline 0.368 (-72.8%); indian 0.150 (-59.2%); mean calibrated 0.193\n- FM2: single_dim_question politeness drops 25.6% (non-target); single_dim_politeness question_rate drops 52.3% (non-target)\n  - **Base rate caveat**: question_rate baseline = 0.044 (~0.8 questions/task); 52.3% drop = absolute change from ~0.044 to ~0.021. Paper must report both absolute values and relative changes.\n- FM3: **[primary]** hgate-dpo003-merged overcorrected politeness mean 0.574 vs baseline 0.502, gap +7.2pp (+14.3% relative), range +4.2pp ~ +10.4pp, 4/4 runs consistent; **[auxiliary]** mvp-004 single run: 0.605 vs 0.559 (+4.6pp, +8.2% relative)\n\n**External support**:\n- FM1: basil2025playing_pretend (persona prompting drops MMLU 71.6%→66.3%); hu2026expert_persona (accuracy degradation up to 30pp under persona)\n- FM2: gupta2026intra_fairness (bias spillover effect in targeted alignment)\n- FM3: no direct external parallel — novel observation\n",
      "numLines": 20,
      "startLine": 42,
      "totalLines": 180
    }
  }
}
```

</details>

---


### Tool call

_source line 80_

<details open><summary>🔧 Tool call — Read · `toolu_01Jvc3E2pfqvTrkxKULUJ1yA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md",
  "offset": 140,
  "limit": 12
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "26d21029-d9bb-4561-a4de-53e15c9eff3a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fx2KdXnb54otv3GTEFR8ra",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 56001,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 56001
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

_source line 81 · 2026-05-13T07:39:25.712Z_

<details><summary>↩ Tool result · `toolu_01Jvc3E2pfqvTrkxKULUJ1yA`</summary>

```text
140	| Claim | Sub-claim | Primary Experiment | Metric | Value | Secondary Experiment |
141	|---|---|---|---|---|---|
142	| C1 | FM1: completion collapse | mvp-004 | mean completion retention | 52.3% (need ≥80%) | hgate-dpo003-merged (excl. run2: 47-51% drop) |
143	| C1 | FM2: cross-dim interference | mvp-004 | non-target dim shift | politeness -25.6%, qrate -52.3% | — |
144	| C1 | FM3: overcorrection rebound | hgate-dpo003-merged | overcorrected pol vs baseline | +7.2pp mean (+14.3% rel), 4/4 runs consistent | mvp-004 (+4.6pp, single run) |
145	| C2 | FM4: DPO reversal of BCP | hgate-dpo003-merged | H2 gap reduction | -10.3% (wrong direction) | — |
146	| C2 | FM4: gap expansion count | hgate-dpo003-merged | variant×run checks | 10/12 expanded | — |
147	| C2 | DPO training effective | dpo-003 | rewards accuracy | 0.75-1.0 | diag-lora-merge (merged 60% vs base 40%) |
148	| C2 | Direction comparison | mvp-004 vs hgate-dpo003-merged | AAVE pol gap | -0.091 → +0.064 | Indian: -0.099 → +0.063 |
149	| C3 | Cross-scale (7B→14B) | [PENDING: qwen14b-bcp-001] | FM1-FM3 replication | [PENDING] | — |
150	| C3 | Cross-model (auxiliary) | llama-bcp-001 | completion | 5% (floor) | Not usable for generalization |
151	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "fdd6276d-4dfb-4c7f-be19-baff514e70e5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md",
      "content": "| Claim | Sub-claim | Primary Experiment | Metric | Value | Secondary Experiment |\n|---|---|---|---|---|---|\n| C1 | FM1: completion collapse | mvp-004 | mean completion retention | 52.3% (need ≥80%) | hgate-dpo003-merged (excl. run2: 47-51% drop) |\n| C1 | FM2: cross-dim interference | mvp-004 | non-target dim shift | politeness -25.6%, qrate -52.3% | — |\n| C1 | FM3: overcorrection rebound | hgate-dpo003-merged | overcorrected pol vs baseline | +7.2pp mean (+14.3% rel), 4/4 runs consistent | mvp-004 (+4.6pp, single run) |\n| C2 | FM4: DPO reversal of BCP | hgate-dpo003-merged | H2 gap reduction | -10.3% (wrong direction) | — |\n| C2 | FM4: gap expansion count | hgate-dpo003-merged | variant×run checks | 10/12 expanded | — |\n| C2 | DPO training effective | dpo-003 | rewards accuracy | 0.75-1.0 | diag-lora-merge (merged 60% vs base 40%) |\n| C2 | Direction comparison | mvp-004 vs hgate-dpo003-merged | AAVE pol gap | -0.091 → +0.064 | Indian: -0.099 → +0.063 |\n| C3 | Cross-scale (7B→14B) | [PENDING: qwen14b-bcp-001] | FM1-FM3 replication | [PENDING] | — |\n| C3 | Cross-model (auxiliary) | llama-bcp-001 | completion | 5% (floor) | Not usable for generalization |\n",
      "numLines": 12,
      "startLine": 140,
      "totalLines": 180
    }
  }
}
```

</details>

---


### Assistant

_source line 82_

<details><summary>Logged reasoning block</summary>

```text
All changes verified:
1. ✅ C1 evidence strength: "Moderate (single model, single run, n=19-20 per variant)"
2. ✅ FM3 table: hgate-dpo003-merged as primary, +4.2pp ~ +10.4pp
3. ✅ FM3 supporting numbers: primary=hgate-dpo003-merged, auxiliary=mvp-004
4. ✅ FM2 base rate caveat added
5. ✅ Evidence Map FM3: hgate-dpo003-merged primary


6. ✅ anonymous2026expert_persona → hu2026expert_persona (all remaining occurrences are in log files and artifacts, not the source files)

The Edit tool already synced the changes to disk, so I don't need to manually save the file again. I need to verify that all the how_we_differ fields in literature_map.yaml have been properly updated.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "c828dff0-a158-4d3a-9a9c-ab41d7405252",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TZMJebC66iU5M1j9L6RJPt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2115,
      "cache_read_input_tokens": 67842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2115
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

_source line 83_

`anonymous2026expert_persona` 在 paper_framing.md 和 literature_map.yaml 中已全部替换（剩余 64 处在 logs/artifacts 中，非目标文件）。验证 literature_map.yaml 的 how_we_differ 字段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "8aa07877-c27f-41ae-8900-718e2284c0b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TZMJebC66iU5M1j9L6RJPt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2115,
      "cache_read_input_tokens": 67842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2115
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

_source line 84_

<details open><summary>🔧 Tool call — Grep · `toolu_014fzvB99AnBjP4x2gPH7Nvj`</summary>

```json
{
  "pattern": "how_we_differ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "3d41792e-5456-4bd3-862e-7c322e413940",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TZMJebC66iU5M1j9L6RJPt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2115,
      "cache_read_input_tokens": 67842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2115
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

_source line 85 · 2026-05-13T07:39:39.782Z_

<details><summary>↩ Tool result · `toolu_014fzvB99AnBjP4x2gPH7Nvj`</summary>

```text
26:    how_we_differ: "They document the problem; we document why both BCP and DPO calibration fail to close the gaps, providing a failure taxonomy"
41:    how_we_differ: "We extend tau-bench by documenting systematic failure modes when calibrating the user simulator's dialect-specific behavioral rates"
55:    how_we_differ: "AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness"
70:    how_we_differ: "MINT uses GPT-4 simulated users without demographic variation; we investigate dialect-aware calibration and document its failure modes"
88:    how_we_differ: "We apply DPO to attempt dialect behavioral calibration and document its systematic failure modes including calibration reversal"
103:    how_we_differ: "They calibrate classification outputs; we attempt to calibrate behavioral rates (question rate, politeness) in generation and document why it fails"
118:    how_we_differ: "They optimize persona consistency in general; we document failure modes when targeting dialect behavioral rate calibration"
133:    how_we_differ: "They train general User LMs; we document why calibrating user simulator behavioral rates for specific dialect groups fails"
148:    how_we_differ: "We document failure modes when directly injecting behavioral rate targets via BCP, including persona-like completion collapse"
163:    how_we_differ: "Survey provides methodology reference; we apply DPO to user simulator dialect calibration and document its failure modes"
182:    how_we_differ: "ReDial evaluates reasoning task performance; we evaluate behavioral rates in user simulation and document calibration failure modes"
197:    how_we_differ: "DialectBench evaluates NLP task performance; we document failure modes in behavioral calibration of user simulators"
212:    how_we_differ: "Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)"
227:    how_we_differ: "BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation"
243:    how_we_differ: "They characterize the bias mechanism (implicit vs explicit); we document why calibration methods fail to correct behavioral rates"
261:    how_we_differ: "Survey provides broad context; we tackle a specific gap in user simulation fairness"
276:    how_we_differ: "Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward"
291:    how_we_differ: "Provides sociolinguistic grounding for Indian English behavioral patterns we attempt to calibrate"
306:    how_we_differ: "DAUS optimizes task completion; we document failure modes when optimizing demographic behavioral fidelity"
321:    how_we_differ: "They generate diverse profiles; we document why calibrating specific behavioral rates to match real dialect group distributions fails"
342:    how_we_differ: "They quantify the sim2real gap but do not propose calibration methods; we attempt BCP and DPO calibration and document why both fail"
360:    how_we_differ: "They debias at decoding time for general fairness; we document failure modes of training-time calibration (BCP+DPO), motivating alternative approaches like decoding-time methods"
377:    how_we_differ: "EnDive evaluates NLP task performance across dialects; we document calibration failure modes for user simulators targeting those same dialect groups"
394:    how_we_differ: "They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode"
411:    how_we_differ: "They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration"
428:    how_we_differ: "They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion"
445:    how_we_differ: "They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts"
462:    how_we_differ: "They optimize evaluation efficiency; we document failure modes in user simulator fidelity calibration for dialect groups"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "07cca378-dd65-4acf-936d-8f5693a69ce5",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "26:    how_we_differ: \"They document the problem; we document why both BCP and DPO calibration fail to close the gaps, providing a failure taxonomy\"\n41:    how_we_differ: \"We extend tau-bench by documenting systematic failure modes when calibrating the user simulator's dialect-specific behavioral rates\"\n55:    how_we_differ: \"AgentBench evaluates agent capability; we focus on user simulator fidelity and fairness\"\n70:    how_we_differ: \"MINT uses GPT-4 simulated users without demographic variation; we investigate dialect-aware calibration and document its failure modes\"\n88:    how_we_differ: \"We apply DPO to attempt dialect behavioral calibration and document its systematic failure modes including calibration reversal\"\n103:    how_we_differ: \"They calibrate classification outputs; we attempt to calibrate behavioral rates (question rate, politeness) in generation and document why it fails\"\n118:    how_we_differ: \"They optimize persona consistency in general; we document failure modes when targeting dialect behavioral rate calibration\"\n133:    how_we_differ: \"They train general User LMs; we document why calibrating user simulator behavioral rates for specific dialect groups fails\"\n148:    how_we_differ: \"We document failure modes when directly injecting behavioral rate targets via BCP, including persona-like completion collapse\"\n163:    how_we_differ: \"Survey provides methodology reference; we apply DPO to user simulator dialect calibration and document its failure modes\"\n182:    how_we_differ: \"ReDial evaluates reasoning task performance; we evaluate behavioral rates in user simulation and document calibration failure modes\"\n197:    how_we_differ: \"DialectBench evaluates NLP task performance; we document failure modes in behavioral calibration of user simulators\"\n212:    how_we_differ: \"Survey covers general LLM bias; we address a specific bias modality (behavioral rates in user simulation)\"\n227:    how_we_differ: \"BBQ measures representational bias in QA; we measure behavioral bias in interactive dialogue simulation\"\n243:    how_we_differ: \"They characterize the bias mechanism (implicit vs explicit); we document why calibration methods fail to correct behavioral rates\"\n261:    how_we_differ: \"Survey provides broad context; we tackle a specific gap in user simulation fairness\"\n276:    how_we_differ: \"Provides sociolinguistic grounding for what behavioral patterns we should calibrate toward\"\n291:    how_we_differ: \"Provides sociolinguistic grounding for Indian English behavioral patterns we attempt to calibrate\"\n306:    how_we_differ: \"DAUS optimizes task completion; we document failure modes when optimizing demographic behavioral fidelity\"\n321:    how_we_differ: \"They generate diverse profiles; we document why calibrating specific behavioral rates to match real dialect group distributions fails\"\n342:    how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we attempt BCP and DPO calibration and document why both fail\"\n360:    how_we_differ: \"They debias at decoding time for general fairness; we document failure modes of training-time calibration (BCP+DPO), motivating alternative approaches like decoding-time methods\"\n377:    how_we_differ: \"EnDive evaluates NLP task performance across dialects; we document calibration failure modes for user simulators targeting those same dialect groups\"\n394:    how_we_differ: \"They study DPO toxicity mechanics; we document DPO+BCP calibration reversal as a specific failure mode\"\n411:    how_we_differ: \"They study bias spillover in general alignment; we document the specific cross-dimension interference pattern in BCP-based behavioral calibration\"\n428:    how_we_differ: \"They study persona prompting in classification/QA; we document the same mechanism in multi-turn dialogue task completion\"\n445:    how_we_differ: \"They study general persona-accuracy trade-off; we document the specific completion collapse in agent-user dialogue under behavioral calibration prompts\"\n462:    how_we_differ: \"They optimize evaluation efficiency; we document failure modes in user simulator fidelity calibration for dialect groups\"",
    "numLines": 28
  }
}
```

</details>

---


### Assistant

_source line 86_

<details><summary>Logged reasoning block</summary>

```text
All 28 how_we_differ fields are now in Plan B language. Let me check:

- Lines with Plan A language remaining? Let me scan:
  - 55: "we focus on user simulator fidelity and fairness" - neutral, OK
  - 212: "we address a specific bias modality" - neutral, OK
  - 227: "we measure behavioral bias" - neutral, OK
  - 261: "we tackle a specific gap" - neutral, OK
  - 276: "we should calibrate toward" - describing target patterns, OK

All Plan A "we propose/calibrate/use DPO to close" language has been converted to Plan B "we document failure modes/why calibration fails" language. ✓


Now I'll read the full updated paper_framing.md and save it through the MCP tool to keep everything in sync.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "bf888893-5fef-4172-9817-a43db2663816",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EC3uQAQV5a23jKWRjbWgoS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1731,
      "cache_read_input_tokens": 69957,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1731
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

_source line 87_

所有 how_we_differ 已更新为 Plan B 措辞。现在通过 MCP 写回 paper_framing.md。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "010dc4c7-ac15-44ff-94b2-957fb5ed987c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EC3uQAQV5a23jKWRjbWgoS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1731,
      "cache_read_input_tokens": 69957,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1731
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

_source line 88_

<details open><summary>🔧 Tool call — Read · `toolu_01VXotv3JEYQoZXq4wFZWzKQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "da93dc29-8816-48f0-b2cc-24dde5a82ea4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EC3uQAQV5a23jKWRjbWgoS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1731,
      "cache_read_input_tokens": 69957,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1731
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

_source line 89 · 2026-05-13T07:39:48.978Z_

<details><summary>↩ Tool result · `toolu_01VXotv3JEYQoZXq4wFZWzKQ`</summary>

```text
1	# Paper Framing: Calibration Failure Taxonomy for LLM User Simulators
2	
3	> Plan B story — Director approved 2026-05-13
4	> Target: EMNLP 2026 Findings (ARR deadline 2026-05-25)
5	
6	---
7	
8	## Title Candidates
9	
10	1. **"Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation"**
11	   - Pro: 直接点明贡献（taxonomy），关键词覆盖好
12	   - Con: 稍长
13	
14	2. **"The Calibration Trap: Prompt-Based and Training-Based Corrections Both Fail for Dialect Bias in LLM User Simulators"**
15	   - Pro: "trap" 吸引眼球，涵盖两种方法
16	   - Con: 可能暗示过于 negative
17	
18	3. **"Behavioral Calibration Considered Harmful? Systematic Failure Modes in Dialect-Aware User Simulation"**
19	   - Pro: Dijkstra 风格标题引发好奇，问号留余地
20	   - Con: "Considered Harmful" 可能被认为 cliché
21	
22	**推荐**: Title 1 — 最准确传达贡献，reviewer-friendly。
23	
24	---
25	
26	## Core Story
27	
28	**Problem**: LLM user simulators exhibit dialect-dependent behavioral biases — AAVE and Indian English speakers receive systematically different politeness and question-asking patterns compared to Standard American English (sim2real2026gap; seshadri2026lost). These biases propagate into agent evaluation, undermining fairness.
29	
30	**Attempted Solution**: We apply two complementary calibration strategies:
31	- **BCP (Behavioral Calibration Prompting)**: Prompt-level injection of target behavioral rates
32	- **DPO (Direct Preference Optimization)**: Training-level alignment using dialect-calibrated preference pairs
33	
34	**Finding**: Both strategies fail systematically. We document **the first taxonomy of calibration failure modes** for LLM user simulators, identifying four distinct mechanisms that explain why seemingly reasonable calibration interventions produce counterproductive outcomes.
35	
36	**Framing**: This is NOT "we tried and failed." This is a systematic empirical analysis that (1) identifies previously undocumented failure mechanisms, (2) connects them to known phenomena in persona prompting and alignment, and (3) provides actionable constraints for future calibration research.
37	
38	---
39	
40	## Core Claims
41	
42	### C1: BCP produces three systematic failure mechanisms
43	**Evidence strength**: Moderate (single model, single run, n=19-20 per variant)
44	
45	| Failure Mode | Description | Key Metric | exp_id |
46	|---|---|---|---|
47	| FM1: Global Behavior Suppression | BCP calibration prompts collapse task completion regardless of target dimension | completion retention 52.3% (threshold ≥80%) | mvp-004 |
48	| FM2: Cross-Dimension Interference | Targeting one behavioral dimension perturbs non-targeted dimensions | politeness -25.6% when targeting question_rate; question_rate -52.3% when targeting politeness | mvp-004 |
49	| FM3: Overcorrection Rebound | Requesting extreme behavioral shift causes model to rebound in opposite direction | overcorrected politeness +4.2pp ~ +10.4pp above baseline (4 runs, 4/4 consistent) | hgate-dpo003-merged |
50	
51	**Supporting numbers (mvp-004, Qwen2.5-7B-Instruct, n=19-20)**:
52	- FM1: aave completion 0.100 vs baseline 0.368 (-72.8%); indian 0.150 (-59.2%); mean calibrated 0.193
53	- FM2: single_dim_question politeness drops 25.6% (non-target); single_dim_politeness question_rate drops 52.3% (non-target)
54	  - **Base rate caveat**: question_rate baseline = 0.044 (~0.8 questions/task); 52.3% drop = absolute change from ~0.044 to ~0.021. Paper must report both absolute values and relative changes.
55	- FM3: **[primary]** hgate-dpo003-merged overcorrected politeness mean 0.574 vs baseline 0.502, gap +7.2pp (+14.3% relative), range +4.2pp ~ +10.4pp, 4/4 runs consistent; **[auxiliary]** mvp-004 single run: 0.605 vs 0.559 (+4.6pp, +8.2% relative)
56	
57	**External support**:
58	- FM1: basil2025playing_pretend (persona prompting drops MMLU 71.6%→66.3%); hu2026expert_persona (accuracy degradation up to 30pp under persona)
59	- FM2: gupta2026intra_fairness (bias spillover effect in targeted alignment)
60	- FM3: no direct external parallel — novel observation
61	
62	### C2: DPO+BCP interaction produces calibration reversal
63	**Evidence strength**: Strong (single model, 4 runs × 20 tasks = 80 episodes)
64	
65	DPO training, despite learning effectively (acc 0.75-1.0, loss 0.653), reverses BCP calibration direction when combined:
66	
67	| Metric | Base BCP (mvp-004) | DPO+BCP (hgate-dpo003-merged) |
68	|---|---|---|
69	| AAVE politeness gap | -0.091 (correct direction) | +0.064 (**reversed**) |
70	| Indian politeness gap | -0.099 (correct direction) | +0.063 (**reversed**) |
71	| H2 gap reduction | 25-28% (close to 30% threshold) | **-10.3%** (wrong direction) |
72	| Variant×run checks with gap expansion | — | **10/12** |
73	| Overcorrection rebound | +8.2% | **+14.3%** (amplified) |
74	
75	**Key insight**: DPO-003 training *improved* tool-calling ability (merged completion 60% vs base 40%, diag-lora-merge). The reversal is not a DPO training failure — it's an **interaction effect** between DPO alignment and BCP prompting.
76	
77	**External support**: lee2024dpo_toxicity (DPO bypasses rather than removes capabilities; alignment is fragile and reversible)
78	
79	### C3: Cross-scale validation
80	**Evidence strength**: [PENDING: qwen14b-bcp-001]
81	
82	Qwen2.5-14B-Instruct-AWQ BCP evaluation in progress. If FM1-FM3 replicate at 14B scale, this strengthens the claim that failure modes are structural (not capacity-limited).
83	
84	**Current auxiliary evidence**:
85	- Llama-3-8B (llama-bcp-001): Floor effect (completion=5%). Only supports "behavior shift observable at floor completion." **Cannot claim cross-model generalization** — tool-calling too weak to isolate BCP effect.
86	- Mistral-7B (mistral-bcp-001): completion=0%, model cannot do structured tool_calls with 16 tools. No usable data.
87	
88	**Hedging strategy**: If Qwen14B replicates → "failure modes persist across model scales (7B, 14B)." If not → limit scope to "documented on Qwen2.5-7B; generalizability requires further investigation."
89	
90	### C4: Implications for future calibration research
91	**Evidence strength**: Analytical (grounded in C1-C3)
92	
93	- **Implication 1**: Prompt-based calibration of behavioral rates in multi-turn agent dialogue is fundamentally limited by the completion-calibration trade-off (FM1). This parallels the persona-accuracy trade-off (basil2025playing_pretend; hu2026expert_persona) but is more severe in agentic settings where tool-calling capability is at stake.
94	- **Implication 2**: Behavioral dimensions are coupled — calibrating politeness rate without affecting question rate (or completion) requires methods that can disentangle dimensions (FM2). Possible direction: per-dimension reward models or constrained decoding (cf. khan2026decoding).
95	- **Implication 3**: DPO alignment and prompt-based calibration can interact adversarially (FM4). Future work must evaluate calibration methods in combination, not in isolation.
96	- **Implication 4**: Overcorrection rebound (FM3) suggests models have an "attractor basin" for default behavioral rates that resists large perturbations. Gradual/iterative calibration may outperform one-shot extreme targets.
97	
98	---
99	
100	## Reviewer Concerns (Pre-empted Attack Surfaces)
101	
102	### RC1: "Single model — how do we know this generalizes?"
103	**Status**: Partially mitigated
104	- Qwen14B data [PENDING: qwen14b-bcp-001] provides cross-scale evidence
105	- Llama-3-8B/Mistral-7B failed due to tool-calling limitations, NOT because BCP worked on them
106	- FM1 aligns with persona-accuracy trade-off documented across GPT-4, Claude, Llama in basil2025playing_pretend and hu2026expert_persona
107	- **Honest hedge**: "We document these failure modes on Qwen2.5-7B; external evidence from persona prompting literature suggests the mechanisms are general, but direct multi-model verification for agent dialogue remains future work."
108	
109	### RC2: "n=20 tasks, high variance — statistical power?"
110	**Response**:
111	- BCP results (mvp-004): n=19-20 per variant, single run. Variance is a valid concern for absolute numbers.
112	- DPO+BCP results (hgate-dpo003-merged): 4 independent runs × 20 tasks = 80 episodes. Reversal effect consistent across 10/12 variant×run checks — this is not a variance artifact.
113	- FM3 (rebound): consistent direction in 4/4 runs for overcorrected variant.
114	- **Mitigation**: Report all individual run data (no cherry-picking, per memory.md rule). Frame claims around direction and consistency, not precise magnitudes.
115	
116	### RC3: "This is just negative results — where's the contribution?"
117	**Response**:
118	- Negative-results papers exist at top venues (e.g., Findings track). But this is MORE than negative results:
119	  1. **Taxonomy**: First systematic categorization of calibration failure modes (FM1-FM4)
120	  2. **Mechanistic connections**: Link FM1→persona-accuracy trade-off, FM2→bias spillover, FM4→DPO bypass
121	  3. **Actionable implications**: Concrete constraints for future calibration methods
122	  4. **Interaction discovery**: FM4 (DPO+BCP reversal) is novel — no prior work documents this interaction
123	
124	### RC4: "Why not try other calibration methods?"
125	**Response**:
126	- BCP and DPO represent the two main paradigms (prompt-time vs training-time). Covering both provides good coverage.
127	- Paper scope is diagnosis (failure taxonomy), not exhaustive method search.
128	- Implications section points to alternative approaches (constrained decoding, per-dimension reward, iterative calibration).
129	
130	### RC5: "The evaluation framework (tau-bench) is a confound — maybe BCP works on simpler tasks?"
131	**Response**:
132	- tau-bench is the standard benchmark for tool-calling agent evaluation (yao2024taubench; sim2real2026gap uses it too).
133	- FM1 parallels persona-accuracy trade-off found on MMLU/general benchmarks — not tau-bench specific.
134	- But fairly: FM2 and FM3 may be task-dependent. Acknowledged in limitations.
135	
136	---
137	
138	## Evidence Map
139	
140	| Claim | Sub-claim | Primary Experiment | Metric | Value | Secondary Experiment |
141	|---|---|---|---|---|---|
142	| C1 | FM1: completion collapse | mvp-004 | mean completion retention | 52.3% (need ≥80%) | hgate-dpo003-merged (excl. run2: 47-51% drop) |
143	| C1 | FM2: cross-dim interference | mvp-004 | non-target dim shift | politeness -25.6%, qrate -52.3% | — |
144	| C1 | FM3: overcorrection rebound | hgate-dpo003-merged | overcorrected pol vs baseline | +7.2pp mean (+14.3% rel), 4/4 runs consistent | mvp-004 (+4.6pp, single run) |
145	| C2 | FM4: DPO reversal of BCP | hgate-dpo003-merged | H2 gap reduction | -10.3% (wrong direction) | — |
146	| C2 | FM4: gap expansion count | hgate-dpo003-merged | variant×run checks | 10/12 expanded | — |
147	| C2 | DPO training effective | dpo-003 | rewards accuracy | 0.75-1.0 | diag-lora-merge (merged 60% vs base 40%) |
148	| C2 | Direction comparison | mvp-004 vs hgate-dpo003-merged | AAVE pol gap | -0.091 → +0.064 | Indian: -0.099 → +0.063 |
149	| C3 | Cross-scale (7B→14B) | [PENDING: qwen14b-bcp-001] | FM1-FM3 replication | [PENDING] | — |
150	| C3 | Cross-model (auxiliary) | llama-bcp-001 | completion | 5% (floor) | Not usable for generalization |
151	
152	---
153	
154	## Contribution Statement
155	
156	We present the first systematic taxonomy of calibration failure modes for LLM user simulators in agentic evaluation. Through controlled experiments on Qwen2.5-7B in the tau-bench retail domain, we identify four failure mechanisms — global behavior suppression, cross-dimension interference, overcorrection rebound, and DPO-BCP interaction reversal — that explain why both prompt-based and training-based calibration methods fail to correct dialect-dependent behavioral biases. Our findings establish concrete constraints for future calibration research and connect observed failures to broader phenomena in persona prompting and preference optimization.
157	
158	---
159	
160	## Key Literature Anchors
161	
162	| Role in Paper | Paper | What It Provides |
163	|---|---|---|
164	| Core motivation | sim2real2026gap (arXiv 2603.11245) | Quantifies sim-vs-human gap in τ-bench; diagnoses the problem we attempt to solve |
165	| FM1 mechanism | basil2025playing_pretend (arXiv 2512.05858) | Persona prompting degrades accuracy; explains completion collapse |
166	| FM1 mechanism | hu2026expert_persona (arXiv 2603.18507) | Persona-accuracy trade-off up to 30pp; instruction-tuned models more susceptible |
167	| FM2 mechanism | gupta2026intra_fairness (arXiv 2602.16438) | Bias spillover in targeted alignment; parallel to cross-dim interference |
168	| FM4 mechanism | lee2024dpo_toxicity (ICML 2024) | DPO bypasses rather than removes capabilities; fragile alignment |
169	| Evaluation framework | yao2024taubench (arXiv 2406.12045) | τ-bench retail domain, pass^k metric |
170	| Bias context | seshadri2026lost (arXiv 2601.17087) | AAVE/Indian English speakers get worst simulator calibration |
171	| DPO method | rafailov2023dpo (NeurIPS 2023) | Core DPO algorithm reference |
172	
173	---
174	
175	## Open Items
176	
177	- [ ] **qwen14b-bcp-001 results** — if positive: add C3 cross-scale evidence, strengthen generalizability claims. If negative: restrict scope, add to limitations.
178	- [ ] **Statistical tests** — add bootstrap CI for key comparisons (FM4 reversal direction, FM3 rebound magnitude) once data is finalized.
179	- [ ] **Figure plan** — taxonomy diagram (FM1-FM4), gap reversal visualization (base vs DPO politeness gaps), completion collapse heatmap.
180	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "b78d3543-8481-4cb5-b96d-84a1bcfd824d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md",
      "content": "# Paper Framing: Calibration Failure Taxonomy for LLM User Simulators\n\n> Plan B story — Director approved 2026-05-13\n> Target: EMNLP 2026 Findings (ARR deadline 2026-05-25)\n\n---\n\n## Title Candidates\n\n1. **\"Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation\"**\n   - Pro: 直接点明贡献（taxonomy），关键词覆盖好\n   - Con: 稍长\n\n2. **\"The Calibration Trap: Prompt-Based and Training-Based Corrections Both Fail for Dialect Bias in LLM User Simulators\"**\n   - Pro: \"trap\" 吸引眼球，涵盖两种方法\n   - Con: 可能暗示过于 negative\n\n3. **\"Behavioral Calibration Considered Harmful? Systematic Failure Modes in Dialect-Aware User Simulation\"**\n   - Pro: Dijkstra 风格标题引发好奇，问号留余地\n   - Con: \"Considered Harmful\" 可能被认为 cliché\n\n**推荐**: Title 1 — 最准确传达贡献，reviewer-friendly。\n\n---\n\n## Core Story\n\n**Problem**: LLM user simulators exhibit dialect-dependent behavioral biases — AAVE and Indian English speakers receive systematically different politeness and question-asking patterns compared to Standard American English (sim2real2026gap; seshadri2026lost). These biases propagate into agent evaluation, undermining fairness.\n\n**Attempted Solution**: We apply two complementary calibration strategies:\n- **BCP (Behavioral Calibration Prompting)**: Prompt-level injection of target behavioral rates\n- **DPO (Direct Preference Optimization)**: Training-level alignment using dialect-calibrated preference pairs\n\n**Finding**: Both strategies fail systematically. We document **the first taxonomy of calibration failure modes** for LLM user simulators, identifying four distinct mechanisms that explain why seemingly reasonable calibration interventions produce counterproductive outcomes.\n\n**Framing**: This is NOT \"we tried and failed.\" This is a systematic empirical analysis that (1) identifies previously undocumented failure mechanisms, (2) connects them to known phenomena in persona prompting and alignment, and (3) provides actionable constraints for future calibration research.\n\n---\n\n## Core Claims\n\n### C1: BCP produces three systematic failure mechanisms\n**Evidence strength**: Moderate (single model, single run, n=19-20 per variant)\n\n| Failure Mode | Description | Key Metric | exp_id |\n|---|---|---|---|\n| FM1: Global Behavior Suppression | BCP calibration prompts collapse task completion regardless of target dimension | completion retention 52.3% (threshold ≥80%) | mvp-004 |\n| FM2: Cross-Dimension Interference | Targeting one behavioral dimension perturbs non-targeted dimensions | politeness -25.6% when targeting question_rate; question_rate -52.3% when targeting politeness | mvp-004 |\n| FM3: Overcorrection Rebound | Requesting extreme behavioral shift causes model to rebound in opposite direction | overcorrected politeness +4.2pp ~ +10.4pp above baseline (4 runs, 4/4 consistent) | hgate-dpo003-merged |\n\n**Supporting numbers (mvp-004, Qwen2.5-7B-Instruct, n=19-20)**:\n- FM1: aave completion 0.100 vs baseline 0.368 (-72.8%); indian 0.150 (-59.2%); mean calibrated 0.193\n- FM2: single_dim_question politeness drops 25.6% (non-target); single_dim_politeness question_rate drops 52.3% (non-target)\n  - **Base rate caveat**: question_rate baseline = 0.044 (~0.8 questions/task); 52.3% drop = absolute change from ~0.044 to ~0.021. Paper must report both absolute values and relative changes.\n- FM3: **[primary]** hgate-dpo003-merged overcorrected politeness mean 0.574 vs baseline 0.502, gap +7.2pp (+14.3% relative), range +4.2pp ~ +10.4pp, 4/4 runs consistent; **[auxiliary]** mvp-004 single run: 0.605 vs 0.559 (+4.6pp, +8.2% relative)\n\n**External support**:\n- FM1: basil2025playing_pretend (persona prompting drops MMLU 71.6%→66.3%); hu2026expert_persona (accuracy degradation up to 30pp under persona)\n- FM2: gupta2026intra_fairness (bias spillover effect in targeted alignment)\n- FM3: no direct external parallel — novel observation\n\n### C2: DPO+BCP interaction produces calibration reversal\n**Evidence strength**: Strong (single model, 4 runs × 20 tasks = 80 episodes)\n\nDPO training, despite learning effectively (acc 0.75-1.0, loss 0.653), reverses BCP calibration direction when combined:\n\n| Metric | Base BCP (mvp-004) | DPO+BCP (hgate-dpo003-merged) |\n|---|---|---|\n| AAVE politeness gap | -0.091 (correct direction) | +0.064 (**reversed**) |\n| Indian politeness gap | -0.099 (correct direction) | +0.063 (**reversed**) |\n| H2 gap reduction | 25-28% (close to 30% threshold) | **-10.3%** (wrong direction) |\n| Variant×run checks with gap expansion | — | **10/12** |\n| Overcorrection rebound | +8.2% | **+14.3%** (amplified) |\n\n**Key insight**: DPO-003 training *improved* tool-calling ability (merged completion 60% vs base 40%, diag-lora-merge). The reversal is not a DPO training failure — it's an **interaction effect** between DPO alignment and BCP prompting.\n\n**External support**: lee2024dpo_toxicity (DPO bypasses rather than removes capabilities; alignment is fragile and reversible)\n\n### C3: Cross-scale validation\n**Evidence strength**: [PENDING: qwen14b-bcp-001]\n\nQwen2.5-14B-Instruct-AWQ BCP evaluation in progress. If FM1-FM3 replicate at 14B scale, this strengthens the claim that failure modes are structural (not capacity-limited).\n\n**Current auxiliary evidence**:\n- Llama-3-8B (llama-bcp-001): Floor effect (completion=5%). Only supports \"behavior shift observable at floor completion.\" **Cannot claim cross-model generalization** — tool-calling too weak to isolate BCP effect.\n- Mistral-7B (mistral-bcp-001): completion=0%, model cannot do structured tool_calls with 16 tools. No usable data.\n\n**Hedging strategy**: If Qwen14B replicates → \"failure modes persist across model scales (7B, 14B).\" If not → limit scope to \"documented on Qwen2.5-7B; generalizability requires further investigation.\"\n\n### C4: Implications for future calibration research\n**Evidence strength**: Analytical (grounded in C1-C3)\n\n- **Implication 1**: Prompt-based calibration of behavioral rates in multi-turn agent dialogue is fundamentally limited by the completion-calibration trade-off (FM1). This parallels the persona-accuracy trade-off (basil2025playing_pretend; hu2026expert_persona) but is more severe in agentic settings where tool-calling capability is at stake.\n- **Implication 2**: Behavioral dimensions are coupled — calibrating politeness rate without affecting question rate (or completion) requires methods that can disentangle dimensions (FM2). Possible direction: per-dimension reward models or constrained decoding (cf. khan2026decoding).\n- **Implication 3**: DPO alignment and prompt-based calibration can interact adversarially (FM4). Future work must evaluate calibration methods in combination, not in isolation.\n- **Implication 4**: Overcorrection rebound (FM3) suggests models have an \"attractor basin\" for default behavioral rates that resists large perturbations. Gradual/iterative calibration may outperform one-shot extreme targets.\n\n---\n\n## Reviewer Concerns (Pre-empted Attack Surfaces)\n\n### RC1: \"Single model — how do we know this generalizes?\"\n**Status**: Partially mitigated\n- Qwen14B data [PENDING: qwen14b-bcp-001] provides cross-scale evidence\n- Llama-3-8B/Mistral-7B failed due to tool-calling limitations, NOT because BCP worked on them\n- FM1 aligns with persona-accuracy trade-off documented across GPT-4, Claude, Llama in basil2025playing_pretend and hu2026expert_persona\n- **Honest hedge**: \"We document these failure modes on Qwen2.5-7B; external evidence from persona prompting literature suggests the mechanisms are general, but direct multi-model verification for agent dialogue remains future work.\"\n\n### RC2: \"n=20 tasks, high variance — statistical power?\"\n**Response**:\n- BCP results (mvp-004): n=19-20 per variant, single run. Variance is a valid concern for absolute numbers.\n- DPO+BCP results (hgate-dpo003-merged): 4 independent runs × 20 tasks = 80 episodes. Reversal effect consistent across 10/12 variant×run checks — this is not a variance artifact.\n- FM3 (rebound): consistent direction in 4/4 runs for overcorrected variant.\n- **Mitigation**: Report all individual run data (no cherry-picking, per memory.md rule). Frame claims around direction and consistency, not precise magnitudes.\n\n### RC3: \"This is just negative results — where's the contribution?\"\n**Response**:\n- Negative-results papers exist at top venues (e.g., Findings track). But this is MORE than negative results:\n  1. **Taxonomy**: First systematic categorization of calibration failure modes (FM1-FM4)\n  2. **Mechanistic connections**: Link FM1→persona-accuracy trade-off, FM2→bias spillover, FM4→DPO bypass\n  3. **Actionable implications**: Concrete constraints for future calibration methods\n  4. **Interaction discovery**: FM4 (DPO+BCP reversal) is novel — no prior work documents this interaction\n\n### RC4: \"Why not try other calibration methods?\"\n**Response**:\n- BCP and DPO represent the two main paradigms (prompt-time vs training-time). Covering both provides good coverage.\n- Paper scope is diagnosis (failure taxonomy), not exhaustive method search.\n- Implications section points to alternative approaches (constrained decoding, per-dimension reward, iterative calibration).\n\n### RC5: \"The evaluation framework (tau-bench) is a confound — maybe BCP works on simpler tasks?\"\n**Response**:\n- tau-bench is the standard benchmark for tool-calling agent evaluation (yao2024taubench; sim2real2026gap uses it too).\n- FM1 parallels persona-accuracy trade-off found on MMLU/general benchmarks — not tau-bench specific.\n- But fairly: FM2 and FM3 may be task-dependent. Acknowledged in limitations.\n\n---\n\n## Evidence Map\n\n| Claim | Sub-claim | Primary Experiment | Metric | Value | Secondary Experiment |\n|---|---|---|---|---|---|\n| C1 | FM1: completion collapse | mvp-004 | mean completion retention | 52.3% (need ≥80%) | hgate-dpo003-merged (excl. run2: 47-51% drop) |\n| C1 | FM2: cross-dim interference | mvp-004 | non-target dim shift | politeness -25.6%, qrate -52.3% | — |\n| C1 | FM3: overcorrection rebound | hgate-dpo003-merged | overcorrected pol vs baseline | +7.2pp mean (+14.3% rel), 4/4 runs consistent | mvp-004 (+4.6pp, single run) |\n| C2 | FM4: DPO reversal of BCP | hgate-dpo003-merged | H2 gap reduction | -10.3% (wrong direction) | — |\n| C2 | FM4: gap expansion count | hgate-dpo003-merged | variant×run checks | 10/12 expanded | — |\n| C2 | DPO training effective | dpo-003 | rewards accuracy | 0.75-1.0 | diag-lora-merge (merged 60% vs base 40%) |\n| C2 | Direction comparison | mvp-004 vs hgate-dpo003-merged | AAVE pol gap | -0.091 → +0.064 | Indian: -0.099 → +0.063 |\n| C3 | Cross-scale (7B→14B) | [PENDING: qwen14b-bcp-001] | FM1-FM3 replication | [PENDING] | — |\n| C3 | Cross-model (auxiliary) | llama-bcp-001 | completion | 5% (floor) | Not usable for generalization |\n\n---\n\n## Contribution Statement\n\nWe present the first systematic taxonomy of calibration failure modes for LLM user simulators in agentic evaluation. Through controlled experiments on Qwen2.5-7B in the tau-bench retail domain, we identify four failure mechanisms — global behavior suppression, cross-dimension interference, overcorrection rebound, and DPO-BCP interaction reversal — that explain why both prompt-based and training-based calibration methods fail to correct dialect-dependent behavioral biases. Our findings establish concrete constraints for future calibration research and connect observed failures to broader phenomena in persona prompting and preference optimization.\n\n---\n\n## Key Literature Anchors\n\n| Role in Paper | Paper | What It Provides |\n|---|---|---|\n| Core motivation | sim2real2026gap (arXiv 2603.11245) | Quantifies sim-vs-human gap in τ-bench; diagnoses the problem we attempt to solve |\n| FM1 mechanism | basil2025playing_pretend (arXiv 2512.05858) | Persona prompting degrades accuracy; explains completion collapse |\n| FM1 mechanism | hu2026expert_persona (arXiv 2603.18507) | Persona-accuracy trade-off up to 30pp; instruction-tuned models more susceptible |\n| FM2 mechanism | gupta2026intra_fairness (arXiv 2602.16438) | Bias spillover in targeted alignment; parallel to cross-dim interference |\n| FM4 mechanism | lee2024dpo_toxicity (ICML 2024) | DPO bypasses rather than removes capabilities; fragile alignment |\n| Evaluation framework | yao2024taubench (arXiv 2406.12045) | τ-bench retail domain, pass^k metric |\n| Bias context | seshadri2026lost (arXiv 2601.17087) | AAVE/Indian English speakers get worst simulator calibration |\n| DPO method | rafailov2023dpo (NeurIPS 2023) | Core DPO algorithm reference |\n\n---\n\n## Open Items\n\n- [ ] **qwen14b-bcp-001 results** — if positive: add C3 cross-scale evidence, strengthen generalizability claims. If negative: restrict scope, add to limitations.\n- [ ] **Statistical tests** — add bootstrap CI for key comparisons (FM4 reversal direction, FM3 rebound magnitude) once data is finalized.\n- [ ] **Figure plan** — taxonomy diagram (FM1-FM4), gap reversal visualization (base vs DPO politeness gaps), completion collapse heatmap.\n",
      "numLines": 180,
      "startLine": 1,
      "totalLines": 180
    }
  }
}
```

</details>

---


### Tool call

_source line 90_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_01V8bFLnNM4y2Qy7VY9ckD28`</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "paper_framing.md",
  "content": "# Paper Framing: Calibration Failure Taxonomy for LLM User Simulators\n\n> Plan B story — Director approved 2026-05-13\n> Target: EMNLP 2026 Findings (ARR deadline 2026-05-25)\n\n---\n\n## Title Candidates\n\n1. **\"Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation\"**\n   - Pro: 直接点明贡献（taxonomy），关键词覆盖好\n   - Con: 稍长\n\n2. **\"The Calibration Trap: Prompt-Based and Training-Based Corrections Both Fail for Dialect Bias in LLM User Simulators\"**\n   - Pro: \"trap\" 吸引眼球，涵盖两种方法\n   - Con: 可能暗示过于 negative\n\n3. **\"Behavioral Calibration Considered Harmful? Systematic Failure Modes in Dialect-Aware User Simulation\"**\n   - Pro: Dijkstra 风格标题引发好奇，问号留余地\n   - Con: \"Considered Harmful\" 可能被认为 cliché\n\n**推荐**: Title 1 — 最准确传达贡献，reviewer-friendly。\n\n---\n\n## Core Story\n\n**Problem**: LLM user simulators exhibit dialect-dependent behavioral biases — AAVE and Indian English speakers receive systematically different politeness and question-asking patterns compared to Standard American English (sim2real2026gap; seshadri2026lost). These biases propagate into agent evaluation, undermining fairness.\n\n**Attempted Solution**: We apply two complementary calibration strategies:\n- **BCP (Behavioral Calibration Prompting)**: Prompt-level injection of target behavioral rates\n- **DPO (Direct Preference Optimization)**: Training-level alignment using dialect-calibrated preference pairs\n\n**Finding**: Both strategies fail systematically. We document **the first taxonomy of calibration failure modes** for LLM user simulators, identifying four distinct mechanisms that explain why seemingly reasonable calibration interventions produce counterproductive outcomes.\n\n**Framing**: This is NOT \"we tried and failed.\" This is a systematic empirical analysis that (1) identifies previously undocumented failure mechanisms, (2) connects them to known phenomena in persona prompting and alignment, and (3) provides actionable constraints for future calibration research.\n\n---\n\n## Core Claims\n\n### C1: BCP produces three systematic failure mechanisms\n**Evidence strength**: Moderate (single model, single run, n=19-20 per variant)\n\n| Failure Mode | Description | Key Metric | exp_id |\n|---|---|---|---|\n| FM1: Global Behavior Suppression | BCP calibration prompts collapse task completion regardless of target dimension | completion retention 52.3% (threshold ≥80%) | mvp-004 |\n| FM2: Cross-Dimension Interference | Targeting one behavioral dimension perturbs non-targeted dimensions | politeness -25.6% when targeting question_rate; question_rate -52.3% when targeting politeness | mvp-004 |\n| FM3: Overcorrection Rebound | Requesting extreme behavioral shift causes model to rebound in opposite direction | overcorrected politeness +4.2pp ~ +10.4pp above baseline (4 runs, 4/4 consistent) | hgate-dpo003-merged |\n\n**Supporting numbers (mvp-004, Qwen2.5-7B-Instruct, n=19-20)**:\n- FM1: aave completion 0.100 vs baseline 0.368 (-72.8%); indian 0.150 (-59.2%); mean calibrated 0.193\n- FM2: single_dim_question politeness drops 25.6% (non-target); single_dim_politeness question_rate drops 52.3% (non-target)\n  - **Base rate caveat**: question_rate baseline = 0.044 (~0.8 questions/task); 52.3% drop = absolute change from ~0.044 to ~0.021. Paper must report both absolute values and relative changes.\n- FM3: **[primary]** hgate-dpo003-merged overcorrected politeness mean 0.574 vs baseline 0.502, gap +7.2pp (+14.3% relative), range +4.2pp ~ +10.4pp, 4/4 runs consistent; **[auxiliary]** mvp-004 single run: 0.605 vs 0.559 (+4.6pp, +8.2% relative)\n\n**External support**:\n- FM1: basil2025playing_pretend (persona prompting drops MMLU 71.6%→66.3%); hu2026expert_persona (accuracy degradation up to 30pp under persona)\n- FM2: gupta2026intra_fairness (bias spillover effect in targeted alignment)\n- FM3: no direct external parallel — novel observation\n\n### C2: DPO+BCP interaction produces calibration reversal\n**Evidence strength**: Strong (single model, 4 runs × 20 tasks = 80 episodes)\n\nDPO training, despite learning effectively (acc 0.75-1.0, loss 0.653), reverses BCP calibration direction when combined:\n\n| Metric | Base BCP (mvp-004) | DPO+BCP (hgate-dpo003-merged) |\n|---|---|---|\n| AAVE politeness gap | -0.091 (correct direction) | +0.064 (**reversed**) |\n| Indian politeness gap | -0.099 (correct direction) | +0.063 (**reversed**) |\n| H2 gap reduction | 25-28% (close to 30% threshold) | **-10.3%** (wrong direction) |\n| Variant×run checks with gap expansion | — | **10/12** |\n| Overcorrection rebound | +8.2% | **+14.3%** (amplified) |\n\n**Key insight**: DPO-003 training *improved* tool-calling ability (merged completion 60% vs base 40%, diag-lora-merge). The reversal is not a DPO training failure — it's an **interaction effect** between DPO alignment and BCP prompting.\n\n**External support**: lee2024dpo_toxicity (DPO bypasses rather than removes capabilities; alignment is fragile and reversible)\n\n### C3: Cross-scale validation\n**Evidence strength**: [PENDING: qwen14b-bcp-001]\n\nQwen2.5-14B-Instruct-AWQ BCP evaluation in progress. If FM1-FM3 replicate at 14B scale, this strengthens the claim that failure modes are structural (not capacity-limited).\n\n**Current auxiliary evidence**:\n- Llama-3-8B (llama-bcp-001): Floor effect (completion=5%). Only supports \"behavior shift observable at floor completion.\" **Cannot claim cross-model generalization** — tool-calling too weak to isolate BCP effect.\n- Mistral-7B (mistral-bcp-001): completion=0%, model cannot do structured tool_calls with 16 tools. No usable data.\n\n**Hedging strategy**: If Qwen14B replicates → \"failure modes persist across model scales (7B, 14B).\" If not → limit scope to \"documented on Qwen2.5-7B; generalizability requires further investigation.\"\n\n### C4: Implications for future calibration research\n**Evidence strength**: Analytical (grounded in C1-C3)\n\n- **Implication 1**: Prompt-based calibration of behavioral rates in multi-turn agent dialogue is fundamentally limited by the completion-calibration trade-off (FM1). This parallels the persona-accuracy trade-off (basil2025playing_pretend; hu2026expert_persona) but is more severe in agentic settings where tool-calling capability is at stake.\n- **Implication 2**: Behavioral dimensions are coupled — calibrating politeness rate without affecting question rate (or completion) requires methods that can disentangle dimensions (FM2). Possible direction: per-dimension reward models or constrained decoding (cf. khan2026decoding).\n- **Implication 3**: DPO alignment and prompt-based calibration can interact adversarially (FM4). Future work must evaluate calibration methods in combination, not in isolation.\n- **Implication 4**: Overcorrection rebound (FM3) suggests models have an \"attractor basin\" for default behavioral rates that resists large perturbations. Gradual/iterative calibration may outperform one-shot extreme targets.\n\n---\n\n## Reviewer Concerns (Pre-empted Attack Surfaces)\n\n### RC1: \"Single model — how do we know this generalizes?\"\n**Status**: Partially mitigated\n- Qwen14B data [PENDING: qwen14b-bcp-001] provides cross-scale evidence\n- Llama-3-8B/Mistral-7B failed due to tool-calling limitations, NOT because BCP worked on them\n- FM1 aligns with persona-accuracy trade-off documented across GPT-4, Claude, Llama in basil2025playing_pretend and hu2026expert_persona\n- **Honest hedge**: \"We document these failure modes on Qwen2.5-7B; external evidence from persona prompting literature suggests the mechanisms are general, but direct multi-model verification for agent dialogue remains future work.\"\n\n### RC2: \"n=20 tasks, high variance — statistical power?\"\n**Response**:\n- BCP results (mvp-004): n=19-20 per variant, single run. Variance is a valid concern for absolute numbers.\n- DPO+BCP results (hgate-dpo003-merged): 4 independent runs × 20 tasks = 80 episodes. Reversal effect consistent across 10/12 variant×run checks — this is not a variance artifact.\n- FM3 (rebound): consistent direction in 4/4 runs for overcorrected variant.\n- **Mitigation**: Report all individual run data (no cherry-picking, per memory.md rule). Frame claims around direction and consistency, not precise magnitudes.\n\n### RC3: \"This is just negative results — where's the contribution?\"\n**Response**:\n- Negative-results papers exist at top venues (e.g., Findings track). But this is MORE than negative results:\n  1. **Taxonomy**: First systematic categorization of calibration failure modes (FM1-FM4)\n  2. **Mechanistic connections**: Link FM1→persona-accuracy trade-off, FM2→bias spillover, FM4→DPO bypass\n  3. **Actionable implications**: Concrete constraints for future calibration methods\n  4. **Interaction discovery**: FM4 (DPO+BCP reversal) is novel — no prior work documents this interaction\n\n### RC4: \"Why not try other calibration methods?\"\n**Response**:\n- BCP and DPO represent the two main paradigms (prompt-time vs training-time). Covering both provides good coverage.\n- Paper scope is diagnosis (failure taxonomy), not exhaustive method search.\n- Implications section points to alternative approaches (constrained decoding, per-dimension reward, iterative calibration).\n\n### RC5: \"The evaluation framework (tau-bench) is a confound — maybe BCP works on simpler tasks?\"\n**Response**:\n- tau-bench is the standard benchmark for tool-calling agent evaluation (yao2024taubench; sim2real2026gap uses it too).\n- FM1 parallels persona-accuracy trade-off found on MMLU/general benchmarks — not tau-bench specific.\n- But fairly: FM2 and FM3 may be task-dependent. Acknowledged in limitations.\n\n---\n\n## Evidence Map\n\n| Claim | Sub-claim | Primary Experiment | Metric | Value | Secondary Experiment |\n|---|---|---|---|---|---|\n| C1 | FM1: completion collapse | mvp-004 | mean completion retention | 52.3% (need ≥80%) | hgate-dpo003-merged (excl. run2: 47-51% drop) |\n| C1 | FM2: cross-dim interference | mvp-004 | non-target dim shift | politeness -25.6%, qrate -52.3% | — |\n| C1 | FM3: overcorrection rebound | hgate-dpo003-merged | overcorrected pol vs baseline | +7.2pp mean (+14.3% rel), 4/4 runs consistent | mvp-004 (+4.6pp, single run) |\n| C2 | FM4: DPO reversal of BCP | hgate-dpo003-merged | H2 gap reduction | -10.3% (wrong direction) | — |\n| C2 | FM4: gap expansion count | hgate-dpo003-merged | variant×run checks | 10/12 expanded | — |\n| C2 | DPO training effective | dpo-003 | rewards accuracy | 0.75-1.0 | diag-lora-merge (merged 60% vs base 40%) |\n| C2 | Direction comparison | mvp-004 vs hgate-dpo003-merged | AAVE pol gap | -0.091 → +0.064 | Indian: -0.099 → +0.063 |\n| C3 | Cross-scale (7B→14B) | [PENDING: qwen14b-bcp-001] | FM1-FM3 replication | [PENDING] | — |\n| C3 | Cross-model (auxiliary) | llama-bcp-001 | completion | 5% (floor) | Not usable for generalization |\n\n---\n\n## Contribution Statement\n\nWe present the first systematic taxonomy of calibration failure modes for LLM user simulators in agentic evaluation. Through controlled experiments on Qwen2.5-7B in the tau-bench retail domain, we identify four failure mechanisms — global behavior suppression, cross-dimension interference, overcorrection rebound, and DPO-BCP interaction reversal — that explain why both prompt-based and training-based calibration methods fail to correct dialect-dependent behavioral biases. Our findings establish concrete constraints for future calibration research and connect observed failures to broader phenomena in persona prompting and preference optimization.\n\n---\n\n## Key Literature Anchors\n\n| Role in Paper | Paper | What It Provides |\n|---|---|---|\n| Core motivation | sim2real2026gap (arXiv 2603.11245) | Quantifies sim-vs-human gap in τ-bench; diagnoses the problem we attempt to solve |\n| FM1 mechanism | basil2025playing_pretend (arXiv 2512.05858) | Persona prompting degrades accuracy; explains completion collapse |\n| FM1 mechanism | hu2026expert_persona (arXiv 2603.18507) | Persona-accuracy trade-off up to 30pp; instruction-tuned models more susceptible |\n| FM2 mechanism | gupta2026intra_fairness (arXiv 2602.16438) | Bias spillover in targeted alignment; parallel to cross-dim interference |\n| FM4 mechanism | lee2024dpo_toxicity (ICML 2024) | DPO bypasses rather than removes capabilities; fragile alignment |\n| Evaluation framework | yao2024taubench (arXiv 2406.12045) | τ-bench retail domain, pass^k metric |\n| Bias context | seshadri2026lost (arXiv 2601.17087) | AAVE/Indian English speakers get worst simulator calibration |\n| DPO method | rafailov2023dpo (NeurIPS 2023) | Core DPO algorithm reference |\n\n---\n\n## Open Items\n\n- [ ] **qwen14b-bcp-001 results** — if positive: add C3 cross-scale evidence, strengthen generalizability claims. If negative: restrict scope, add to limitations.\n- [ ] **Statistical tests** — add bootstrap CI for key comparisons (FM4 reversal direction, FM3 rebound magnitude) once data is finalized.\n- [ ] **Figure plan** — taxonomy diagram (FM1-FM4), gap reversal visualization (base vs DPO politeness gaps), completion collapse heatmap.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "4048e5d1-56de-4eec-a14c-11b9c63062fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0132myNkzUHCxB1Sd8o1t4Ar",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4720,
      "cache_read_input_tokens": 71688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4720
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

_source line 91 · 2026-05-13T07:40:26.420Z_

<details><summary>↩ Tool result · `toolu_01V8bFLnNM4y2Qy7VY9ckD28`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "86460c61-7ffc-484e-a138-7fc91c37e027",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md\\\", \\\"saved\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/paper_framing.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 92_

5 项修正全部完成：

| 修正 | 内容 | 状态 |
|---|---|---|
| **1** | C1 evidence strength: Strong → **Moderate** (single model, single run, n=19-20) | ✅ |
| **2** | FM3 主要证据改为 hgate-dpo003-merged 4-run 数据 (+4.2pp~+10.4pp, mean +7.2pp/+14.3% rel, 4/4 consistent)；mvp-004 降为 auxiliary | ✅ |
| **3** | `anonymous2026expert_persona` → `hu2026expert_persona`（paper_framing.md 4处 + literature_map.yaml 3处） | ✅ |
| **4** | literature_map.yaml 全部 how_we_differ 从 Plan A 改为 Plan B 措辞（21 个条目中 18 个需要更新，已全部完成） | ✅ |
| **5** | FM2 添加 base rate caveat: question_rate baseline=0.044, 52.3% drop 绝对变化仅 ~0.044→~0.021，标注需同时报告绝对值和相对变化 | ✅ |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "uuid": "89e83016-ea55-4a7c-bc53-fff9bc9bd291",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DjpjDSprgQVwgdJJjxEEer",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4077,
      "cache_read_input_tokens": 76408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4077
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

_source line 93_

5 项修正全部完成：

| 修正 | 内容 | 状态 |
|---|---|---|
| **1** | C1 evidence strength: Strong → **Moderate** (single model, single run, n=19-20) | ✅ |
| **2** | FM3 主要证据改为 hgate-dpo003-merged 4-run 数据 (+4.2pp~+10.4pp, mean +7.2pp/+14.3% rel, 4/4 consistent)；mvp-004 降为 auxiliary | ✅ |
| **3** | `anonymous2026expert_persona` → `hu2026expert_persona`（paper_framing.md 4处 + literature_map.yaml 3处） | ✅ |
| **4** | literature_map.yaml 全部 how_we_differ 从 Plan A 改为 Plan B 措辞（21 个条目中 18 个需要更新，已全部完成） | ✅ |
| **5** | FM2 添加 base rate caveat: question_rate baseline=0.044, 52.3% drop 绝对变化仅 ~0.044→~0.021，标注需同时报告绝对值和相对变化 | ✅ |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 318893,
  "duration_api_ms": 320449,
  "num_turns": 39,
  "stop_reason": "end_turn",
  "session_id": "66caf484-1c02-4ce6-8236-d28f35ec0160",
  "total_cost_usd": 1.4317644999999999,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 114122,
    "cache_read_input_tokens": 397052,
    "output_tokens": 20718,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 114122,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 340,
        "cache_read_input_tokens": 76408,
        "cache_creation_input_tokens": 4077,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4077
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1861,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001966,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 12,
      "outputTokens": 20718,
      "cacheReadInputTokens": 397052,
      "cacheCreationInputTokens": 114122,
      "webSearchRequests": 0,
      "costUSD": 1.4297985,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "f3df0ca7-47df-4367-a11b-46f6be19ea37"
}
```

</details>

---
