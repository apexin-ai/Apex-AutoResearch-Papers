# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-19 (UTC).** ## Original idea { "tit

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/593b0787-5a72-44d5-85e8-706f2a81fa97.jsonl`
- **Structured JSON:** [`b510f20364dab7582226.json`](../../sessions/b5/b510f20364dab7582226.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T09:22:37.053Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T09:22:37.053Z",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-19 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Verifier Disagreement as Tail-Preservation Signal in Synthetic Data Curation\",\n  \"core_problem\": \"Can the disagreement region between diverse verifiers serve as a principled signal for identifying and preserving distribution-tail data during iterative synthetic retraining, thereby widening the verifier ceiling?\",\n  \"opportunity\": \"Yi et al. (2025) proved the verifier ceiling theorem: a single verifier's biases bound achievable performance. Falahati et al. (2026) showed pluralistic preferences prevent collapse theoretically, but no one has operationalized multi-verifier disagreement as a data selection mechanism. The 'Helping or Herding?' paper (2023) demonstrated RM ensembles disagree more after distribution shift—precisely where tail data resides—but never connected this to collapse prevention. Meanwhile, 'Synthetic Eggs in Many Baskets' (ACL 2026) showed multi-source synthetic diversity mitigates collapse empirically, without explaining the mechanism.\",\n  \"landscape\": \"Current SOTA for verified synthetic data curation uses a single verifier (Yi et al. 2025; Feng et al. ICLR 2025) or co-evolving generator-verifier pairs (CoVerRL, March 2026; RL Tango, NeurIPS 2025). Pluralistic preferences theory (Falahati et al. 2026) proves convergence to a weighted Nash bargaining solution under multiple rewards, but remains purely theoretical. DPH-RL (2025) addresses diversity collapse in RLVR via f-divergence choice but does not address data curation. Weaver (NeurIPS 2025) combines multiple weak verifiers into a strong one but targets test-time verification, not iterative data curation or tail preservation. QAQ (March 2026) uses strong-vs-weak model disagreement ('cognitive gap') for synthetic code instruction selection, but operates with only two models and does not address iterative retraining or tail-distribution preservation. The key gap: no work uses the specific regions where multiple verifiers disagree as a positive signal to upweight underrepresented distribution tails during iterative retraining. The disagreement region is exactly where verifier biases diverge—and thus where useful tail information may reside.\",\n  \"inspired_by\": \"Gap: Verifier ceiling theorem (Section 2.1) + Pluralistic preferences theory (Section 4.2). The field guide identifies that pluralistic curation 'widens' but does not 'break' the ceiling. Untried combination: operationalizing verifier disagreement regions (from RM ensemble literature) as a tail-preservation mechanism for iterative synthetic data curation.\",\n  \"approach\": \"Assemble a panel of K>=3 structurally diverse verifiers—an outcome reward model (e.g., Skywork-Reward-8B), a process reward model (e.g., VersaPRM), and a rule-based symbolic checker (SymPy for math, test-case execution for code)—and use their pairwise disagreement on synthetically generated candidates as an upweighting signal during iterative retraining. At each round, generate N=256 candidate solutions per problem from the current policy (Qwen3-8B), compute a normalized disagreement score d(x) across all K verifiers per candidate, and construct the next-round training set with sampling weights proportional to alpha + (1-alpha)*d(x), where alpha controls the floor weight for consensus-accepted samples. Run 8 iterative retraining rounds, measuring tail preservation via Pass@k/Pass@1 ratio, solution-strategy coverage entropy, and hardest-decile benchmark accuracy. Compare against single-verifier filtering (Yi et al.), CoVerRL co-evolution, RL Tango, DPH-RL f-divergence regularization, and uniform sampling baselines on MATH-500, AIME 2024, and LiveCodeBench.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"700-1000 H100-hours (3 verifier trainings ~150h, 8 retraining rounds ~256h, generation ~100h, ablations ~200h)\",\n      \"timeline\": \"12-16 weeks with 2 researchers\",\n      \"estimated_gpu_cost\": \"$1,750-$2,500 at ~$2.50/H100-hr on Lambda/Spheron\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"700-1000 H100-hours (same GPU workload; Claude accelerates code and analysis, not compute)\",\n      \"timeline\": \"8-11 weeks with 1-2 researchers\",\n      \"claude_api_cost\": \"$300-500 (experiment scripting, analysis notebooks, paper drafting via Sonnet 4.6)\",\n      \"estimated_gpu_cost\": \"$1,750-$2,500\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"1200-1500 H100-hours (broader hyperparameter sweeps over alpha, K, disagreement metrics, automated ablation grid)\",\n      \"timeline\": \"5-7 weeks\",\n      \"claude_api_cost\": \"$800-1,200 (orchestration, code generation, iterative analysis, paper writing via Sonnet 4.6 + Opus 4.7 for theory)\",\n      \"estimated_gpu_cost\": \"$3,000-$3,750\",\n      \"speed_bottleneck\": \"GPU cluster queue time for parallel retraining rounds; each 8-round sweep is sequential by design (~32h wall-clock per configuration on 8xH100)\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (full paper deadline: July 28, 2026)\",\n    \"ICLR 2027 (estimated deadline: ~October 2026, not yet announced)\",\n    \"EMNLP 2026 via ARR May cycle (deadline: May 25, 2026 — only feasible if paper is near-complete)\",\n    \"AACL-IJCNLP 2026 via ARR May cycle (deadline: May 25, 2026 — same constraint)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Escaping Model Collapse via Synthetic Data Verification (Yi et al., ICLR 2026 DATA-FM Workshop)\",\n    \"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification (Feng et al., ICLR 2025)\",\n    \"Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences (Falahati et al., arXiv 2026)\",\n    \"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking (Eisenstein et al., ICML 2024)\",\n    \"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning (Schaffelder & Gatt, ACL Findings 2026)\",\n    \"CoVerRL: Breaking the Consensus Trap in Label-Free Reasoning via Generator-Verifier Co-Evolution (arXiv 2026)\",\n    \"RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning (Zha et al., NeurIPS 2025)\",\n    \"The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in RLVR (arXiv 2025)\",\n    \"Verification Limits Code LLM Training (Gureja et al., arXiv 2025)\",\n    \"Weaver: Shrinking the Generation-Verification Gap with Weak Verifiers (Saad-Falcon et al., NeurIPS 2025)\",\n    \"QAQ: Bidirectional Semantic Coherence for Selecting High-Quality Synthetic Code Instructions (arXiv 2026)\"\n  ],\n  \"description\": \"We propose Disagreement-Weighted Iterative Curation (DWIC), a method that operationalizes multi-verifier disagreement as a tail-preservation signal during iterative synthetic retraining. A panel of K>=3 structurally diverse verifiers (outcome RM, process RM, symbolic checker) independently scores each synthetically generated candidate. Candidates in high-disagreement regions—where verifier biases diverge—receive upweighted sampling probability in the next retraining round, on the hypothesis that these regions disproportionately encode distribution-tail phenomena (rare solution strategies, edge cases) that any single verifier would systematically filter out. This directly addresses the verifier ceiling theorem (Yi et al. 2025): by preserving data that no single verifier confidently accepts or rejects, we prevent the iterative collapse toward any one verifier's knowledge center. Unlike QAQ's two-model cognitive gap (code-only, non-iterative), DWIC uses a diverse verifier panel across domains and explicitly tracks tail diversity over multiple retraining rounds. We evaluate on math reasoning (MATH-500, AIME 2024) and code generation (LiveCodeBench), measuring both downstream accuracy and distribution health (Pass@k ratio, strategy-coverage entropy, hardest-decile accuracy) across 8 iterative rounds against single-verifier, CoVerRL, RL Tango, and DPH-RL baselines.\",\n  \"project_name\": \"disagree_tail_curate\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 1)\nIssues: [\"CRITICAL: The central hypothesis 'verifier disagreement ≈ distribution-tail data' is unsubstantiated. Disagreement could equally indicate noisy, ambiguous, or adversarial samples. The proposal needs a theoretical argument or at least preliminary pilot data showing the disagreement–tail correlation holds.\", \"MISSING COMPETITOR: PROF (arXiv 2509.03403, Sep 2025) uses PRM+ORM for data curation in iterative RL training — the most closely related prior work. It uses consistency (agreement) to filter data, which is the inverse of DWIC's disagreement upweighting. Must be discussed and compared against.\", \"MISSING COMPETITOR: The 'behavioral entanglement' paper (arXiv 2604.07650, Apr 2026) shows LLM verifiers have correlated biases due to shared pretraining, directly undermining the assumption that 'structurally diverse verifiers' will produce meaningfully independent disagreement signals. An ORM, PRM, and symbolic checker may be more diverse than LLM-only panels, but this concern must be explicitly addressed.\", \"VENUE REALISM: ARR May 25, 2026 deadline is 6 days away — effectively impossible unless the paper is already written. Remove EMNLP 2026 and AACL-IJCNLP 2026 via ARR May cycle from target venues.\", \"The connection to query-by-committee active learning (QBC) is unacknowledged. DWIC is essentially QBC applied to synthetic data curation with a tail-preservation framing. The proposal must position itself relative to this classical literature to avoid appearing naive about the intellectual ancestry.\", \"The 'verifier ceiling widening' claim attributed to a 'field guide' is ungrounded — Falahati et al. (2605.07724) does NOT discuss 'widening' vs 'breaking' the ceiling, and Yi et al. does not use the phrase 'verifier ceiling theorem.' These framings appear to be the proposal's own interpretations presented as established concepts.\", \"The alpha hyperparameter in the weighting formula alpha + (1-alpha)*d(x) is underspecified — no guidance on expected ranges, sensitivity analysis, or how it interacts with the number of verifiers K. This is a core design choice that needs ablation planning.\"]\nFeedback: The idea has a valid core — operationalizing multi-verifier disagreement for iterative data curation — but needs substantive revisions: (1) Provide a theoretical or empirical argument for WHY disagreement maps to useful tail data rather than noise; consider a pilot experiment on a toy setting. (2) Add PROF as a primary baseline — it's the closest existing work using multi-reward-type signals for data curation. (3) Address the verifier entanglement concern: if ORM and PRM share pretraining biases, their disagreement may be less informative than assumed. Discuss why ORM+PRM+symbolic checker is a 'structurally diverse' panel. (4) Acknowledge QBC as intellectual heritage and clearly delineate what DWIC adds beyond standard committee disagreement in the iterative retraining context. (5) Remove the infeasible ARR May 2026 venues. (6) Don't over-claim theoretical novelty — the 'verifier ceiling theorem' and 'widening vs breaking' language should be softened to reflect these are your interpretations, not established results.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.\n- Address each issue specifically.\n\n## 深度调研要求\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。\n3. **深度思考**：\n   - 核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach？\n4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。\n\n## 针对 Review 意见的定向搜索\n\n1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点\n2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline\n3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现\n4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot\n\n- You have full freedom: minor fix, major revision, or pivot.\n- Include a \"change_type\" field: \"minor\", \"major\", or \"pivot\".\n- Output a COMPLETE JSON object with ALL fields."
}
```

---

### Runtime record

_source line 2 · 2026-05-19T09:22:37.056Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T09:22:37.056Z",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97"
}
```

---

## Round 1

33 recorded events

### User

_source line 3 · 2026-05-19T09:22:37.066Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-19 (UTC).**

## Original idea
{
  "title": "Verifier Disagreement as Tail-Preservation Signal in Synthetic Data Curation",
  "core_problem": "Can the disagreement region between diverse verifiers serve as a principled signal for identifying and preserving distribution-tail data during iterative synthetic retraining, thereby widening the verifier ceiling?",
  "opportunity": "Yi et al. (2025) proved the verifier ceiling theorem: a single verifier's biases bound achievable performance. Falahati et al. (2026) showed pluralistic preferences prevent collapse theoretically, but no one has operationalized multi-verifier disagreement as a data selection mechanism. The 'Helping or Herding?' paper (2023) demonstrated RM ensembles disagree more after distribution shift—precisely where tail data resides—but never connected this to collapse prevention. Meanwhile, 'Synthetic Eggs in Many Baskets' (ACL 2026) showed multi-source synthetic diversity mitigates collapse empirically, without explaining the mechanism.",
  "landscape": "Current SOTA for verified synthetic data curation uses a single verifier (Yi et al. 2025; Feng et al. ICLR 2025) or co-evolving generator-verifier pairs (CoVerRL, March 2026; RL Tango, NeurIPS 2025). Pluralistic preferences theory (Falahati et al. 2026) proves convergence to a weighted Nash bargaining solution under multiple rewards, but remains purely theoretical. DPH-RL (2025) addresses diversity collapse in RLVR via f-divergence choice but does not address data curation. Weaver (NeurIPS 2025) combines multiple weak verifiers into a strong one but targets test-time verification, not iterative data curation or tail preservation. QAQ (March 2026) uses strong-vs-weak model disagreement ('cognitive gap') for synthetic code instruction selection, but operates with only two models and does not address iterative retraining or tail-distribution preservation. The key gap: no work uses the specific regions where multiple verifiers disagree as a positive signal to upweight underrepresented distribution tails during iterative retraining. The disagreement region is exactly where verifier biases diverge—and thus where useful tail information may reside.",
  "inspired_by": "Gap: Verifier ceiling theorem (Section 2.1) + Pluralistic preferences theory (Section 4.2). The field guide identifies that pluralistic curation 'widens' but does not 'break' the ceiling. Untried combination: operationalizing verifier disagreement regions (from RM ensemble literature) as a tail-preservation mechanism for iterative synthetic data curation.",
  "approach": "Assemble a panel of K>=3 structurally diverse verifiers—an outcome reward model (e.g., Skywork-Reward-8B), a process reward model (e.g., VersaPRM), and a rule-based symbolic checker (SymPy for math, test-case execution for code)—and use their pairwise disagreement on synthetically generated candidates as an upweighting signal during iterative retraining. At each round, generate N=256 candidate solutions per problem from the current policy (Qwen3-8B), compute a normalized disagreement score d(x) across all K verifiers per candidate, and construct the next-round training set with sampling weights proportional to alpha + (1-alpha)*d(x), where alpha controls the floor weight for consensus-accepted samples. Run 8 iterative retraining rounds, measuring tail preservation via Pass@k/Pass@1 ratio, solution-strategy coverage entropy, and hardest-decile benchmark accuracy. Compare against single-verifier filtering (Yi et al.), CoVerRL co-evolution, RL Tango, DPH-RL f-divergence regularization, and uniform sampling baselines on MATH-500, AIME 2024, and LiveCodeBench.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "700-1000 H100-hours (3 verifier trainings ~150h, 8 retraining rounds ~256h, generation ~100h, ablations ~200h)",
      "timeline": "12-16 weeks with 2 researchers",
      "estimated_gpu_cost": "$1,750-$2,500 at ~$2.50/H100-hr on Lambda/Spheron"
    },
    "human_in_loop": {
      "gpu_hours": "700-1000 H100-hours (same GPU workload; Claude accelerates code and analysis, not compute)",
      "timeline": "8-11 weeks with 1-2 researchers",
      "claude_api_cost": "$300-500 (experiment scripting, analysis notebooks, paper drafting via Sonnet 4.6)",
      "estimated_gpu_cost": "$1,750-$2,500"
    },
    "auto_research": {
      "gpu_hours": "1200-1500 H100-hours (broader hyperparameter sweeps over alpha, K, disagreement metrics, automated ablation grid)",
      "timeline": "5-7 weeks",
      "claude_api_cost": "$800-1,200 (orchestration, code generation, iterative analysis, paper writing via Sonnet 4.6 + Opus 4.7 for theory)",
      "estimated_gpu_cost": "$3,000-$3,750",
      "speed_bottleneck": "GPU cluster queue time for parallel retraining rounds; each 8-round sweep is sequential by design (~32h wall-clock per configuration on 8xH100)"
    }
  },
  "target_venues": [
    "AAAI 2027 (full paper deadline: July 28, 2026)",
    "ICLR 2027 (estimated deadline: ~October 2026, not yet announced)",
    "EMNLP 2026 via ARR May cycle (deadline: May 25, 2026 — only feasible if paper is near-complete)",
    "AACL-IJCNLP 2026 via ARR May cycle (deadline: May 25, 2026 — same constraint)"
  ],
  "level": "top-tier",
  "key_references": [
    "Escaping Model Collapse via Synthetic Data Verification (Yi et al., ICLR 2026 DATA-FM Workshop)",
    "Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification (Feng et al., ICLR 2025)",
    "Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences (Falahati et al., arXiv 2026)",
    "Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking (Eisenstein et al., ICML 2024)",
    "Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning (Schaffelder & Gatt, ACL Findings 2026)",
    "CoVerRL: Breaking the Consensus Trap in Label-Free Reasoning via Generator-Verifier Co-Evolution (arXiv 2026)",
    "RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning (Zha et al., NeurIPS 2025)",
    "The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in RLVR (arXiv 2025)",
    "Verification Limits Code LLM Training (Gureja et al., arXiv 2025)",
    "Weaver: Shrinking the Generation-Verification Gap with Weak Verifiers (Saad-Falcon et al., NeurIPS 2025)",
    "QAQ: Bidirectional Semantic Coherence for Selecting High-Quality Synthetic Code Instructions (arXiv 2026)"
  ],
  "description": "We propose Disagreement-Weighted Iterative Curation (DWIC), a method that operationalizes multi-verifier disagreement as a tail-preservation signal during iterative synthetic retraining. A panel of K>=3 structurally diverse verifiers (outcome RM, process RM, symbolic checker) independently scores each synthetically generated candidate. Candidates in high-disagreement regions—where verifier biases diverge—receive upweighted sampling probability in the next retraining round, on the hypothesis that these regions disproportionately encode distribution-tail phenomena (rare solution strategies, edge cases) that any single verifier would systematically filter out. This directly addresses the verifier ceiling theorem (Yi et al. 2025): by preserving data that no single verifier confidently accepts or rejects, we prevent the iterative collapse toward any one verifier's knowledge center. Unlike QAQ's two-model cognitive gap (code-only, non-iterative), DWIC uses a diverse verifier panel across domains and explicitly tracks tail diversity over multiple retraining rounds. We evaluate on math reasoning (MATH-500, AIME 2024) and code generation (LiveCodeBench), measuring both downstream accuracy and distribution health (Pass@k ratio, strategy-coverage entropy, hardest-decile accuracy) across 8 iterative rounds against single-verifier, CoVerRL, RL Tango, and DPH-RL baselines.",
  "project_name": "disagree_tail_curate",
  "source": "web_research"
}

## Reviewer feedback (round 1)
Issues: ["CRITICAL: The central hypothesis 'verifier disagreement ≈ distribution-tail data' is unsubstantiated. Disagreement could equally indicate noisy, ambiguous, or adversarial samples. The proposal needs a theoretical argument or at least preliminary pilot data showing the disagreement–tail correlation holds.", "MISSING COMPETITOR: PROF (arXiv 2509.03403, Sep 2025) uses PRM+ORM for data curation in iterative RL training — the most closely related prior work. It uses consistency (agreement) to filter data, which is the inverse of DWIC's disagreement upweighting. Must be discussed and compared against.", "MISSING COMPETITOR: The 'behavioral entanglement' paper (arXiv 2604.07650, Apr 2026) shows LLM verifiers have correlated biases due to shared pretraining, directly undermining the assumption that 'structurally diverse verifiers' will produce meaningfully independent disagreement signals. An ORM, PRM, and symbolic checker may be more diverse than LLM-only panels, but this concern must be explicitly addressed.", "VENUE REALISM: ARR May 25, 2026 deadline is 6 days away — effectively impossible unless the paper is already written. Remove EMNLP 2026 and AACL-IJCNLP 2026 via ARR May cycle from target venues.", "The connection to query-by-committee active learning (QBC) is unacknowledged. DWIC is essentially QBC applied to synthetic data curation with a tail-preservation framing. The proposal must position itself relative to this classical literature to avoid appearing naive about the intellectual ancestry.", "The 'verifier ceiling widening' claim attributed to a 'field guide' is ungrounded — Falahati et al. (2605.07724) does NOT discuss 'widening' vs 'breaking' the ceiling, and Yi et al. does not use the phrase 'verifier ceiling theorem.' These framings appear to be the proposal's own interpretations presented as established concepts.", "The alpha hyperparameter in the weighting formula alpha + (1-alpha)*d(x) is underspecified — no guidance on expected ranges, sensitivity analysis, or how it interacts with the number of verifiers K. This is a core design choice that needs ablation planning."]
Feedback: The idea has a valid core — operationalizing multi-verifier disagreement for iterative data curation — but needs substantive revisions: (1) Provide a theoretical or empirical argument for WHY disagreement maps to useful tail data rather than noise; consider a pilot experiment on a toy setting. (2) Add PROF as a primary baseline — it's the closest existing work using multi-reward-type signals for data curation. (3) Address the verifier entanglement concern: if ORM and PRM share pretraining biases, their disagreement may be less informative than assumed. Discuss why ORM+PRM+symbolic checker is a 'structurally diverse' panel. (4) Acknowledge QBC as intellectual heritage and clearly delineate what DWIC adds beyond standard committee disagreement in the iterative retraining context. (5) Remove the infeasible ARR May 2026 venues. (6) Don't over-claim theoretical novelty — the 'verifier ceiling theorem' and 'widening vs breaking' language should be softened to reflect these are your interpretations, not established results.

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
  "promptId": "ae35a659-7407-4079-9c58-2bf4f6ffeb73",
  "type": "user",
  "uuid": "ec87ca10-d960-45b4-99b9-53abc017712c",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T09:22:37.065Z_

```json
{
  "parentUuid": "ec87ca10-d960-45b4-99b9-53abc017712c",
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
  "uuid": "cdbaa3c4-c0b9-4ab7-912a-88a492794a39",
  "timestamp": "2026-05-19T09:22:37.065Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T09:22:37.065Z_

```json
{
  "parentUuid": "cdbaa3c4-c0b9-4ab7-912a-88a492794a39",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "2038d27a-465d-4e60-a77c-4ee065f4f9db",
  "timestamp": "2026-05-19T09:22:37.065Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
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
  "aiTitle": "Revise verifier disagreement tail-preservation hypothesis",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97"
}
```

---

### Assistant

_source line 7 · 2026-05-19T09:22:46.692Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully and plan my research strategy:

1. **CRITICAL**: The hypothesis that "verifier disagreement ≈ distribution-tail data" is unsubstantiated. Need theoretical/empirical grounding.
2. **MISSING COMPETITOR**: PROF (arXiv 2509.03403) - PRM+ORM for data curation in iterative RL
3. **MISSING COMPETITOR**: Behavioral entanglement paper (arXiv 2604.07650) - LLM verifiers have correlated biases
4. **VENUE REALISM**: Remove ARR May 2026 venues


5. **QBC connection**: Query-by-committee active learning ancestry
6. **Over-claiming**: "verifier ceiling theorem" and "widening vs breaking" language need toning down
7. **Alpha hyperparameter**: Underspecified, needs ablation planning

I need to dig into the literature on these fronts—reading both missing papers, understanding the theoretical grounding for disagreement as a tail-data signal, exploring the QBC lineage, and planning ablations for the alpha parameter.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2038d27a-465d-4e60-a77c-4ee065f4f9db",
  "isSidechain": false,
  "requestId": "req_011CbBgatz7WoJpUCyqX69yi",
  "type": "assistant",
  "uuid": "d4699ae0-0f64-4767-9c0d-c902d216bd15",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wo5qiCu1pqUCVVmorVCdvY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4912,
      "cache_read_input_tokens": 11374,
      "output_tokens": 407,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4912,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 407,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 4912,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4912
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

_source line 8 · 2026-05-19T09:22:46.695Z_

I'll conduct deep research on each reviewer concern in parallel before revising. Let me launch several focused research agents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4699ae0-0f64-4767-9c0d-c902d216bd15",
  "isSidechain": false,
  "requestId": "req_011CbBgatz7WoJpUCyqX69yi",
  "type": "assistant",
  "uuid": "5cbdba2e-61ea-4186-a7ea-59732948adca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wo5qiCu1pqUCVVmorVCdvY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4912,
      "cache_read_input_tokens": 11374,
      "output_tokens": 407,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4912,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 407,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 4912,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4912
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

_source line 9 · 2026-05-19T09:22:46.800Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CsFRFaj3CSVT62cmW1nayW`</summary>

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
  "parentUuid": "5cbdba2e-61ea-4186-a7ea-59732948adca",
  "isSidechain": false,
  "requestId": "req_011CbBgatz7WoJpUCyqX69yi",
  "type": "assistant",
  "uuid": "b6af4c8b-fc23-4710-8a2d-5f7fe4809324",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wo5qiCu1pqUCVVmorVCdvY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4912,
      "cache_read_input_tokens": 11374,
      "output_tokens": 407,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4912,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 407,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 4912,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4912
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

_source line 10 · 2026-05-19T09:22:46.806Z_

<details><summary>↩ Tool result · `toolu_01CsFRFaj3CSVT62cmW1nayW`</summary>

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
  "parentUuid": "b6af4c8b-fc23-4710-8a2d-5f7fe4809324",
  "isSidechain": false,
  "promptId": "ae35a659-7407-4079-9c58-2bf4f6ffeb73",
  "type": "user",
  "uuid": "d1a653f5-86ac-4bc3-8957-77b1e8372496",
  "toolUseResult": {
    "matches": [
      "WebFetch",
      "WebSearch"
    ],
    "query": "select:WebFetch,WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "b6af4c8b-fc23-4710-8a2d-5f7fe4809324",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"Verifier Disagreement as Tail-Preservation Signal in Synthetic Data Cu…",
  "leafUuid": "d1a653f5-86ac-4bc3-8957-77b1e8372496",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise verifier disagreement tail-preservation hypothesis",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97"
}
```

---

### Assistant

_source line 13 · 2026-05-19T09:22:49.155Z_

Now let me launch parallel research agents for each major reviewer concern:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1a653f5-86ac-4bc3-8957-77b1e8372496",
  "isSidechain": false,
  "requestId": "req_011CbBgbcbAKpdj8M55ERwQf",
  "type": "assistant",
  "uuid": "c57ac0df-1193-4171-ad89-58b9d006e8ef",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMbLfDykmWvFijLqHMfFTD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1426,
      "cache_read_input_tokens": 16286,
      "output_tokens": 1798,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1426,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1798,
          "cache_read_input_tokens": 16286,
          "cache_creation_input_tokens": 1426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1426
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

_source line 14 · 2026-05-19T09:22:55.499Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01KDDXb7d8pDmuY3kbhJAjM6`</summary>

```json
{
  "description": "Research PROF paper (2509.03403)",
  "prompt": "I need to deeply research the paper PROF (arXiv 2509.03403, September 2025) which uses PRM+ORM for data curation in iterative RL training. This is a critical missing competitor for a research proposal about using multi-verifier disagreement for synthetic data curation.\n\nPlease:\n1. Search for \"PROF PRM ORM iterative RL training arXiv 2509.03403\" and related queries\n2. Fetch and read the actual paper from arxiv.org (try https://arxiv.org/abs/2509.03403 and the PDF)\n3. Extract:\n   - The exact method: how does PROF use PRM and ORM together?\n   - Does it use agreement/consistency to FILTER data (as claimed by the reviewer)?\n   - How does it handle the interplay between different verifier types?\n   - What benchmarks and baselines does it use?\n   - What are its key results and limitations?\n   - How does it relate to using disagreement (the INVERSE of what PROF does) as a signal?\n\nReport your findings in detail. This is crucial for positioning our work against PROF.",
  "model": "opus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c57ac0df-1193-4171-ad89-58b9d006e8ef",
  "isSidechain": false,
  "requestId": "req_011CbBgbcbAKpdj8M55ERwQf",
  "type": "assistant",
  "uuid": "22039368-b2ec-4cbd-a133-e3c688144802",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMbLfDykmWvFijLqHMfFTD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1426,
      "cache_read_input_tokens": 16286,
      "output_tokens": 1798,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1426,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1798,
          "cache_read_input_tokens": 16286,
          "cache_creation_input_tokens": 1426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1426
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

_source line 15 · 2026-05-19T09:23:00.207Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Lm4y8gakZqPGnoFkBZZsEW`</summary>

```json
{
  "description": "Research behavioral entanglement paper",
  "prompt": "I need to deeply research the \"behavioral entanglement\" paper (arXiv 2604.07650, April 2026) which shows LLM verifiers have correlated biases due to shared pretraining. This directly challenges a research proposal's assumption that \"structurally diverse verifiers\" produce meaningfully independent disagreement signals.\n\nPlease:\n1. Search for \"behavioral entanglement LLM verifiers correlated biases arXiv 2604.07650\" and related queries\n2. Fetch and read the paper from https://arxiv.org/abs/2604.07650\n3. Extract:\n   - What exactly is \"behavioral entanglement\"?\n   - How correlated are LLM-based verifiers' biases?\n   - Does the paper distinguish between LLM-only panels vs. mixed panels (LLM + symbolic checker)?\n   - What are the implications for using diverse verifier panels?\n   - Are there any suggested mitigations?\n   - Does this paper say anything about ORM vs PRM vs rule-based verifiers specifically?\n\nReport findings in detail. I need to understand how seriously this undermines the assumption that an ORM + PRM + symbolic checker panel is \"structurally diverse.\"",
  "model": "opus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22039368-b2ec-4cbd-a133-e3c688144802",
  "isSidechain": false,
  "requestId": "req_011CbBgbcbAKpdj8M55ERwQf",
  "type": "assistant",
  "uuid": "4e6c88cf-b429-48ab-930f-75edf183b1dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMbLfDykmWvFijLqHMfFTD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1426,
      "cache_read_input_tokens": 16286,
      "output_tokens": 1798,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1426,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1798,
          "cache_read_input_tokens": 16286,
          "cache_creation_input_tokens": 1426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1426
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

_source line 16 · 2026-05-19T09:23:07.794Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01CgEAiLm3d4CTZmX6u9T4QH`</summary>

```json
{
  "description": "Research disagreement-tail hypothesis",
  "prompt": "A research proposal claims that \"verifier disagreement correlates with distribution-tail data\" in the context of synthetic data curation for LLM training. Reviewers flagged this as unsubstantiated — disagreement could equally indicate noise, ambiguity, or adversarial samples.\n\nI need you to deeply research whether there is theoretical or empirical support for this hypothesis. Please:\n\n1. Search for: \"classifier disagreement distribution tail\" and \"ensemble disagreement rare examples machine learning\"\n2. Search for: \"query by committee uncertainty sampling tail distribution\"\n3. Search for: \"reward model disagreement out of distribution\" and \"ensemble disagreement epistemic uncertainty\"\n4. Search for: \"verifier disagreement noise vs signal synthetic data\"\n\nKey questions to answer:\n- Is there ANY theoretical result linking ensemble/committee disagreement to tail-of-distribution data specifically?\n- What does the epistemic vs aleatoric uncertainty literature say? (Disagreement often captures epistemic uncertainty, which could be high for BOTH tail data AND noise)\n- Are there results from active learning/QBC that distinguish \"informative disagreement\" from \"noisy disagreement\"?\n- What conditions are needed for disagreement to be a useful signal rather than noise?\n- Are there any toy/pilot experiments in the literature demonstrating this connection?\n\nBe thorough and honest — if the evidence is weak, say so. This is the most critical issue in the review.",
  "model": "opus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e6c88cf-b429-48ab-930f-75edf183b1dd",
  "isSidechain": false,
  "requestId": "req_011CbBgbcbAKpdj8M55ERwQf",
  "type": "assistant",
  "uuid": "8e769e91-6796-43ed-a7fd-cafe40891d32",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMbLfDykmWvFijLqHMfFTD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1426,
      "cache_read_input_tokens": 16286,
      "output_tokens": 1798,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1426,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1798,
          "cache_read_input_tokens": 16286,
          "cache_creation_input_tokens": 1426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1426
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

_source line 17 · 2026-05-19T09:23:15.909Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01YDg4K1L13e37pbQYYcq2rQ`</summary>

```json
{
  "description": "Research QBC and active learning",
  "prompt": "A research proposal about \"Disagreement-Weighted Iterative Curation (DWIC)\" — using multi-verifier disagreement to preserve tail data in synthetic retraining — was criticized for not acknowledging its connection to Query-by-Committee (QBC) active learning. The reviewer said \"DWIC is essentially QBC applied to synthetic data curation with a tail-preservation framing.\"\n\nPlease research:\n\n1. Search for \"query by committee active learning\" - find the seminal papers (Seung, Opper, Sompolinsky 1992; Freund et al. 1997)\n2. Search for \"query by committee synthetic data\" and \"active learning data curation LLM\"\n3. Search for \"committee disagreement data selection language models 2024 2025\"\n4. Read key papers to understand:\n   - The classical QBC framework and its theoretical properties\n   - How QBC relates to selecting samples at the decision boundary vs. the tail\n   - Key differences between QBC (selecting what to LABEL next) vs. DWIC (selecting what to RETAIN/UPWEIGHT in retraining)\n   - Any recent work applying QBC-like ideas to LLM training data curation\n   - What specifically DWIC adds beyond standard QBC\n\nThe goal is to properly position DWIC relative to this intellectual ancestry while clearly articulating what is novel. Report findings in detail.",
  "model": "opus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e769e91-6796-43ed-a7fd-cafe40891d32",
  "isSidechain": false,
  "requestId": "req_011CbBgbcbAKpdj8M55ERwQf",
  "type": "assistant",
  "uuid": "a226bab4-a430-441a-9534-8d0286e19b54",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMbLfDykmWvFijLqHMfFTD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1426,
      "cache_read_input_tokens": 16286,
      "output_tokens": 1798,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1426,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1798,
          "cache_read_input_tokens": 16286,
          "cache_creation_input_tokens": 1426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1426
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

_source line 18 · 2026-05-19T09:23:21.038Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0153r5HJ2uAHmEop8YCdX9px`</summary>

```json
{
  "description": "Research recent verifier diversity work",
  "prompt": "I'm revising a research proposal about using multi-verifier disagreement for iterative synthetic data curation. I need to check for any additional recent (2025-2026) work I might be missing on:\n\n1. Search \"multi-verifier synthetic data curation 2025 2026\"\n2. Search \"reward model diversity iterative training LLM 2025 2026\" \n3. Search \"model collapse prevention data selection 2025 2026\"\n4. Search \"process reward model outcome reward model combined 2025 2026\"\n5. Search \"symbolic verifier neural verifier combined math reasoning 2025 2026\"\n\nFor each relevant paper found, extract:\n- Title, authors, venue, date\n- Key method\n- How it relates to using verifier disagreement for data curation\n- Whether it's a competitor, complementary, or irrelevant\n\nAlso specifically check: has anyone done a pilot study showing that verifier disagreement regions contain useful/tail data rather than just noise? This would be extremely valuable for our proposal.\n\nReport all findings.",
  "model": "opus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a226bab4-a430-441a-9534-8d0286e19b54",
  "isSidechain": false,
  "requestId": "req_011CbBgbcbAKpdj8M55ERwQf",
  "type": "assistant",
  "uuid": "8a848347-95f6-4141-9004-c86b13af2cd8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMbLfDykmWvFijLqHMfFTD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1426,
      "cache_read_input_tokens": 16286,
      "output_tokens": 1798,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1426,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1798,
          "cache_read_input_tokens": 16286,
          "cache_creation_input_tokens": 1426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1426
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

_source line 19 · 2026-05-19T09:25:36.619Z_

<details><summary>↩ Tool result · `toolu_01KDDXb7d8pDmuY3kbhJAjM6`</summary>

````text
I now have comprehensive information to provide a thorough analysis. Here is the complete research report:

---

## PROF: Deep Research Report

### Paper Identity

**Title:** "Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"
**arXiv ID:** 2509.03403 (submitted September 4, 2025)
**Authors:** Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal (Amazon / UIUC)
**Code:** https://github.com/Chenluye99/PROF
**OpenReview status:** The submission to OpenReview (ID: JKr77ZmZcM) shows status **"Withdrawn Submission"**, which is a potentially useful detail for positioning.

---

### 1. The Exact Method: How PROF Uses PRM and ORM Together

PROF (PRocess cOnsistency Filter) is a **data curation / sample filtering** method inserted between the rollout phase and the policy update phase of GRPO training. It does NOT blend PRM and ORM scores into the reward function. Instead:

**Step-by-step algorithm:**

1. **Oversample:** Generate n=8 rollouts per prompt (vs. n=4 for vanilla GRPO), keeping only m=4 for the policy update.

2. **Compute consistency score** for each trajectory i:
   ```
   r_i^pro = [ (1/H_i) * sum(r_i^h for h=1..H_i) - lambda * I(H_i=1 or H_i >= H_lambda) ] * r_o,i
   ```
   Where:
   - `r_i^h` = PRM score for step h
   - `H_i` = number of steps in the trajectory
   - `r_o,i` = outcome reward (+1 or -1)
   - `lambda=10, H_lambda=30` = step-length regularization parameters
   - The multiplication by `r_o,i` is critical: for correct responses (r_o=+1), high avg PRM means high consistency; for incorrect responses (r_o=-1), the sign flips so low avg PRM means high consistency.

3. **Separate into groups:** G+ (correct, r_o=+1) and G- (incorrect, r_o=-1).

4. **Compute balanced removal counts** k+, k- to maintain a balanced correct/incorrect ratio (maximizing outcome reward variance).

5. **Rank and filter:**
   - In the correct group G+: **keep the top-ranked** by consistency (highest avg PRM scores) -> removes correct answers with poor reasoning.
   - In the incorrect group G-: **keep the top-ranked** by consistency (which, due to the sign flip from r_o=-1, means lowest avg PRM scores) -> removes incorrect answers with deceptively good-looking reasoning.

6. **Output:** m=4 filtered trajectories used for standard GRPO policy update with outcome-based advantages only. PRM values are NEVER fed into the gradient computation.

---

### 2. Does PROF Use Agreement/Consistency to FILTER Data?

**Yes, this is precisely what it does.** PROF is fundamentally an **agreement-based filter**. It retains samples where PRM and ORM **agree**:

- **Kept:** Correct answer + high PRM scores (agreement: good process, good outcome)
- **Kept:** Incorrect answer + low PRM scores (agreement: bad process, bad outcome)

It **discards** samples where PRM and ORM **disagree**:

- **Discarded:** Correct answer + low PRM scores (disagreement: bad process, lucky outcome -- "false positive")
- **Discarded:** Incorrect answer + high PRM scores (disagreement: good process, unlucky outcome -- "false negative")

The paper explicitly validates this with Claude-3-7-Sonnet: among filtered-out correct responses, **30.1% were confirmed to contain flawed reasoning**, showing the filter successfully catches false positives from ORM.

---

### 3. How PROF Handles the Interplay Between Different Verifier Types

PROF's key design insight is that PRM and ORM have **complementary failure modes**:

| Verifier | Strength | Weakness |
|----------|----------|----------|
| ORM | Accurate (verifiable ground truth) | Coarse-grained, cannot see reasoning quality |
| PRM | Fine-grained, step-level signal | Noisy, suffers from distribution shift, reward hacking |

PROF addresses this by:
- **Using ORM as the authority on correctness** (binary, reliable).
- **Using PRM only as a ranking signal within ORM-defined groups** (never in the loss function).
- This separation is critical: the "Blend" baseline that linearly combines PRM into the reward (r = r_o + beta * avg_PRM, with beta=0.8) suffers severe **entropy collapse** and **response length explosion** (reward hacking), performing WORSE than vanilla GRPO.
- PROF avoids reward hacking because PRM scores never enter the gradient computation; they only determine which samples are selected.

---

### 4. Benchmarks and Baselines

**Training data:** Numina-Math (~860k math problems)

**Base models:** Qwen2.5-Math-1.5B-base, Qwen2.5-Math-7B-base, LLaMA-3.2-3B-instruct (ablation)

**PRM:** Qwen2.5-Math-PRM-7B

**Evaluation benchmarks (Average@16):**
- Math500
- Minerva Math
- Olympiad Bench
- AMC2023
- AIME2024

**Baselines:**
- Base model (no RL)
- Vanilla GRPO (n=4 rollouts, outcome reward only)
- Blend-PRM-GRPO (linearly blends averaged PRM into outcome reward with beta=0.8)

---

### 5. Key Results

**Main performance (7B model):**
| Method | Average Accuracy |
|--------|-----------------|
| Base | 23.4% |
| GRPO | 49.9% |
| Blend-PRM-GRPO | 47.3% (WORSE than GRPO) |
| **PROF-GRPO** | **51.7%** (+1.8% over GRPO, +4.4% over Blend) |

**Main performance (1.5B model):**
| Method | Average Accuracy |
|--------|-----------------|
| GRPO | 37.2% |
| Blend-PRM-GRPO | 35.3% |
| **PROF-GRPO** | **39.6%** (+2.4% over GRPO) |

**Process quality improvement (Monte Carlo value estimation, 7B):**
- Improvements of 9.2% to 37.4% on intermediate step quality across benchmarks -- much larger than outcome accuracy gains.

**Ablation findings:**
- Separating groups is essential; without it, incorrect samples get disproportionately removed.
- Filter-Correct alone is nearly as good as filtering both groups.
- Optimal rollout count is n=8 (with m=4); performance degrades beyond n=12.
- Mean aggregation of PRM scores outperforms minimum, sum, or ratio-based methods.
- Cross-model (LLaMA with Qwen PRM): Filter-Correct is safer when PRM is less reliable.

---

### 6. Limitations

1. **PRM dependency:** Quality is tied to the pre-trained PRM. The authors do not develop improved PRMs.
2. **Domain restriction:** Only tested on mathematical reasoning. Extension to coding/web navigation is future work.
3. **Single PRM architecture:** Only uses Qwen2.5-Math-PRM-7B. No experiments with diverse or ensemble PRMs.
4. **Small test sets:** AIME2024 has only 30 samples; statistical significance is questionable.
5. **Withdrawn from peer review:** The paper was withdrawn from its OpenReview submission (venue unknown), which may indicate issues identified during review.
6. **Modest absolute gains:** The improvement over vanilla GRPO is ~2% in outcome accuracy. The larger story is process quality improvement.

---

### 7. Critical Analysis: PROF vs. Disagreement-Based Curation

This is the most important section for positioning your work. PROF and a disagreement-based approach represent **two sides of the same coin**:

**PROF uses AGREEMENT as a signal to KEEP data:**
- Agreement between PRM and ORM -> "clean" training signal -> keep for RL training.
- The goal: remove noisy gradients from inconsistent samples.

**Your proposed approach uses DISAGREEMENT as a signal (the inverse):**
- Disagreement between multiple verifiers -> identifies "interesting" or "hard" or "uncertain" samples.
- The key question is: what do you DO with the disagreement signal?

**Key differentiators for your positioning:**

1. **PROF uses exactly TWO verifiers (one PRM, one ORM) in a fixed hierarchy.** The ORM is treated as ground truth (it IS ground truth for math). PROF cannot work in domains without verifiable outcomes. A multi-verifier disagreement approach could work with arbitrary combinations of verifiers without requiring one to be a ground-truth oracle.

2. **PROF discards disagreement cases entirely.** It throws away the most "interesting" samples -- the ones where process and outcome conflict. Your work could argue that these disagreement cases contain the richest learning signal (e.g., for curriculum design, targeted improvement, or uncertainty-aware training).

3. **PROF is limited to the binary agree/disagree between process and outcome.** A multi-verifier framework could capture richer disagreement patterns across many verifiers (e.g., 3+ reward models, LLM-as-judge, formal verifiers, unit tests), enabling more nuanced data curation.

4. **PROF addresses reward hacking by excluding PRM from gradients.** A disagreement approach could use disagreement to detect and characterize reward hacking more directly (samples where one verifier is "fooled" but others are not).

5. **PROF's 30.1% flawed-reasoning detection rate** means it catches less than a third of the problematic samples among filtered correct responses. This leaves room for improvement that a multi-verifier disagreement approach might capture.

6. **PROF was withdrawn from peer review**, suggesting potential issues with the approach that reviewers identified.

**Positioning language suggestion:**
PROF demonstrates that PRM-ORM consistency is a useful signal for data curation in RL training. However, PROF treats PRM-ORM disagreement purely as noise to be discarded. Your work takes the complementary view: multi-verifier disagreement is an **informative signal** that identifies samples at the decision boundary where targeted training is most valuable. While PROF uses a fixed two-verifier hierarchy (PRM subordinate to ground-truth ORM), your approach generalizes to arbitrary verifier ensembles without requiring ground-truth outcomes, making it applicable beyond math to domains like code generation, open-ended reasoning, and scientific discovery.

Sources:
- [PROF Paper (arXiv)](https://arxiv.org/abs/2509.03403)
- [PROF Paper HTML](https://arxiv.org/html/2509.03403v1)
- [PROF on HuggingFace Papers](https://huggingface.co/papers/2509.03403)
- [PROF OpenReview (Withdrawn)](https://openreview.net/forum?id=JKr77ZmZcM)
- [PROF GitHub Repository](https://github.com/Chenluye99/PROF)
- [Eisenstein et al. 2023 - Reward Model Ensembles](https://arxiv.org/abs/2312.09244)

agentId: a4fe046b7e78cd743 (use SendMessage with to: 'a4fe046b7e78cd743' to continue this agent)
&lt;usage>total_tokens: 45967
tool_uses: 13
duration_ms: 161116&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "22039368-b2ec-4cbd-a133-e3c688144802",
  "isSidechain": false,
  "promptId": "ae35a659-7407-4079-9c58-2bf4f6ffeb73",
  "type": "user",
  "uuid": "31dab7e8-ad0f-450f-ae28-553525c16701",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to deeply research the paper PROF (arXiv 2509.03403, September 2025) which uses PRM+ORM for data curation in iterative RL training. This is a critical missing competitor for a research proposal about using multi-verifier disagreement for synthetic data curation.\n\nPlease:\n1. Search for \"PROF PRM ORM iterative RL training arXiv 2509.03403\" and related queries\n2. Fetch and read the actual paper from arxiv.org (try https://arxiv.org/abs/2509.03403 and the PDF)\n3. Extract:\n   - The exact method: how does PROF use PRM and ORM together?\n   - Does it use agreement/consistency to FILTER data (as claimed by the reviewer)?\n   - How does it handle the interplay between different verifier types?\n   - What benchmarks and baselines does it use?\n   - What are its key results and limitations?\n   - How does it relate to using disagreement (the INVERSE of what PROF does) as a signal?\n\nReport your findings in detail. This is crucial for positioning our work against PROF.",
    "agentId": "a4fe046b7e78cd743",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information to provide a thorough analysis. Here is the complete research report:\n\n---\n\n## PROF: Deep Research Report\n\n### Paper Identity\n\n**Title:** \"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training\"\n**arXiv ID:** 2509.03403 (submitted September 4, 2025)\n**Authors:** Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal (Amazon / UIUC)\n**Code:** https://github.com/Chenluye99/PROF\n**OpenReview status:** The submission to OpenReview (ID: JKr77ZmZcM) shows status **\"Withdrawn Submission\"**, which is a potentially useful detail for positioning.\n\n---\n\n### 1. The Exact Method: How PROF Uses PRM and ORM Together\n\nPROF (PRocess cOnsistency Filter) is a **data curation / sample filtering** method inserted between the rollout phase and the policy update phase of GRPO training. It does NOT blend PRM and ORM scores into the reward function. Instead:\n\n**Step-by-step algorithm:**\n\n1. **Oversample:** Generate n=8 rollouts per prompt (vs. n=4 for vanilla GRPO), keeping only m=4 for the policy update.\n\n2. **Compute consistency score** for each trajectory i:\n   ```\n   r_i^pro = [ (1/H_i) * sum(r_i^h for h=1..H_i) - lambda * I(H_i=1 or H_i >= H_lambda) ] * r_o,i\n   ```\n   Where:\n   - `r_i^h` = PRM score for step h\n   - `H_i` = number of steps in the trajectory\n   - `r_o,i` = outcome reward (+1 or -1)\n   - `lambda=10, H_lambda=30` = step-length regularization parameters\n   - The multiplication by `r_o,i` is critical: for correct responses (r_o=+1), high avg PRM means high consistency; for incorrect responses (r_o=-1), the sign flips so low avg PRM means high consistency.\n\n3. **Separate into groups:** G+ (correct, r_o=+1) and G- (incorrect, r_o=-1).\n\n4. **Compute balanced removal counts** k+, k- to maintain a balanced correct/incorrect ratio (maximizing outcome reward variance).\n\n5. **Rank and filter:**\n   - In the correct group G+: **keep the top-ranked** by consistency (highest avg PRM scores) -> removes correct answers with poor reasoning.\n   - In the incorrect group G-: **keep the top-ranked** by consistency (which, due to the sign flip from r_o=-1, means lowest avg PRM scores) -> removes incorrect answers with deceptively good-looking reasoning.\n\n6. **Output:** m=4 filtered trajectories used for standard GRPO policy update with outcome-based advantages only. PRM values are NEVER fed into the gradient computation.\n\n---\n\n### 2. Does PROF Use Agreement/Consistency to FILTER Data?\n\n**Yes, this is precisely what it does.** PROF is fundamentally an **agreement-based filter**. It retains samples where PRM and ORM **agree**:\n\n- **Kept:** Correct answer + high PRM scores (agreement: good process, good outcome)\n- **Kept:** Incorrect answer + low PRM scores (agreement: bad process, bad outcome)\n\nIt **discards** samples where PRM and ORM **disagree**:\n\n- **Discarded:** Correct answer + low PRM scores (disagreement: bad process, lucky outcome -- \"false positive\")\n- **Discarded:** Incorrect answer + high PRM scores (disagreement: good process, unlucky outcome -- \"false negative\")\n\nThe paper explicitly validates this with Claude-3-7-Sonnet: among filtered-out correct responses, **30.1% were confirmed to contain flawed reasoning**, showing the filter successfully catches false positives from ORM.\n\n---\n\n### 3. How PROF Handles the Interplay Between Different Verifier Types\n\nPROF's key design insight is that PRM and ORM have **complementary failure modes**:\n\n| Verifier | Strength | Weakness |\n|----------|----------|----------|\n| ORM | Accurate (verifiable ground truth) | Coarse-grained, cannot see reasoning quality |\n| PRM | Fine-grained, step-level signal | Noisy, suffers from distribution shift, reward hacking |\n\nPROF addresses this by:\n- **Using ORM as the authority on correctness** (binary, reliable).\n- **Using PRM only as a ranking signal within ORM-defined groups** (never in the loss function).\n- This separation is critical: the \"Blend\" baseline that linearly combines PRM into the reward (r = r_o + beta * avg_PRM, with beta=0.8) suffers severe **entropy collapse** and **response length explosion** (reward hacking), performing WORSE than vanilla GRPO.\n- PROF avoids reward hacking because PRM scores never enter the gradient computation; they only determine which samples are selected.\n\n---\n\n### 4. Benchmarks and Baselines\n\n**Training data:** Numina-Math (~860k math problems)\n\n**Base models:** Qwen2.5-Math-1.5B-base, Qwen2.5-Math-7B-base, LLaMA-3.2-3B-instruct (ablation)\n\n**PRM:** Qwen2.5-Math-PRM-7B\n\n**Evaluation benchmarks (Average@16):**\n- Math500\n- Minerva Math\n- Olympiad Bench\n- AMC2023\n- AIME2024\n\n**Baselines:**\n- Base model (no RL)\n- Vanilla GRPO (n=4 rollouts, outcome reward only)\n- Blend-PRM-GRPO (linearly blends averaged PRM into outcome reward with beta=0.8)\n\n---\n\n### 5. Key Results\n\n**Main performance (7B model):**\n| Method | Average Accuracy |\n|--------|-----------------|\n| Base | 23.4% |\n| GRPO | 49.9% |\n| Blend-PRM-GRPO | 47.3% (WORSE than GRPO) |\n| **PROF-GRPO** | **51.7%** (+1.8% over GRPO, +4.4% over Blend) |\n\n**Main performance (1.5B model):**\n| Method | Average Accuracy |\n|--------|-----------------|\n| GRPO | 37.2% |\n| Blend-PRM-GRPO | 35.3% |\n| **PROF-GRPO** | **39.6%** (+2.4% over GRPO) |\n\n**Process quality improvement (Monte Carlo value estimation, 7B):**\n- Improvements of 9.2% to 37.4% on intermediate step quality across benchmarks -- much larger than outcome accuracy gains.\n\n**Ablation findings:**\n- Separating groups is essential; without it, incorrect samples get disproportionately removed.\n- Filter-Correct alone is nearly as good as filtering both groups.\n- Optimal rollout count is n=8 (with m=4); performance degrades beyond n=12.\n- Mean aggregation of PRM scores outperforms minimum, sum, or ratio-based methods.\n- Cross-model (LLaMA with Qwen PRM): Filter-Correct is safer when PRM is less reliable.\n\n---\n\n### 6. Limitations\n\n1. **PRM dependency:** Quality is tied to the pre-trained PRM. The authors do not develop improved PRMs.\n2. **Domain restriction:** Only tested on mathematical reasoning. Extension to coding/web navigation is future work.\n3. **Single PRM architecture:** Only uses Qwen2.5-Math-PRM-7B. No experiments with diverse or ensemble PRMs.\n4. **Small test sets:** AIME2024 has only 30 samples; statistical significance is questionable.\n5. **Withdrawn from peer review:** The paper was withdrawn from its OpenReview submission (venue unknown), which may indicate issues identified during review.\n6. **Modest absolute gains:** The improvement over vanilla GRPO is ~2% in outcome accuracy. The larger story is process quality improvement.\n\n---\n\n### 7. Critical Analysis: PROF vs. Disagreement-Based Curation\n\nThis is the most important section for positioning your work. PROF and a disagreement-based approach represent **two sides of the same coin**:\n\n**PROF uses AGREEMENT as a signal to KEEP data:**\n- Agreement between PRM and ORM -> \"clean\" training signal -> keep for RL training.\n- The goal: remove noisy gradients from inconsistent samples.\n\n**Your proposed approach uses DISAGREEMENT as a signal (the inverse):**\n- Disagreement between multiple verifiers -> identifies \"interesting\" or \"hard\" or \"uncertain\" samples.\n- The key question is: what do you DO with the disagreement signal?\n\n**Key differentiators for your positioning:**\n\n1. **PROF uses exactly TWO verifiers (one PRM, one ORM) in a fixed hierarchy.** The ORM is treated as ground truth (it IS ground truth for math). PROF cannot work in domains without verifiable outcomes. A multi-verifier disagreement approach could work with arbitrary combinations of verifiers without requiring one to be a ground-truth oracle.\n\n2. **PROF discards disagreement cases entirely.** It throws away the most \"interesting\" samples -- the ones where process and outcome conflict. Your work could argue that these disagreement cases contain the richest learning signal (e.g., for curriculum design, targeted improvement, or uncertainty-aware training).\n\n3. **PROF is limited to the binary agree/disagree between process and outcome.** A multi-verifier framework could capture richer disagreement patterns across many verifiers (e.g., 3+ reward models, LLM-as-judge, formal verifiers, unit tests), enabling more nuanced data curation.\n\n4. **PROF addresses reward hacking by excluding PRM from gradients.** A disagreement approach could use disagreement to detect and characterize reward hacking more directly (samples where one verifier is \"fooled\" but others are not).\n\n5. **PROF's 30.1% flawed-reasoning detection rate** means it catches less than a third of the problematic samples among filtered correct responses. This leaves room for improvement that a multi-verifier disagreement approach might capture.\n\n6. **PROF was withdrawn from peer review**, suggesting potential issues with the approach that reviewers identified.\n\n**Positioning language suggestion:**\nPROF demonstrates that PRM-ORM consistency is a useful signal for data curation in RL training. However, PROF treats PRM-ORM disagreement purely as noise to be discarded. Your work takes the complementary view: multi-verifier disagreement is an **informative signal** that identifies samples at the decision boundary where targeted training is most valuable. While PROF uses a fixed two-verifier hierarchy (PRM subordinate to ground-truth ORM), your approach generalizes to arbitrary verifier ensembles without requiring ground-truth outcomes, making it applicable beyond math to domains like code generation, open-ended reasoning, and scientific discovery.\n\nSources:\n- [PROF Paper (arXiv)](https://arxiv.org/abs/2509.03403)\n- [PROF Paper HTML](https://arxiv.org/html/2509.03403v1)\n- [PROF on HuggingFace Papers](https://huggingface.co/papers/2509.03403)\n- [PROF OpenReview (Withdrawn)](https://openreview.net/forum?id=JKr77ZmZcM)\n- [PROF GitHub Repository](https://github.com/Chenluye99/PROF)\n- [Eisenstein et al. 2023 - Reward Model Ensembles](https://arxiv.org/abs/2312.09244)"
      }
    ],
    "totalDurationMs": 161116,
    "totalTokens": 45967,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 42154,
      "output_tokens": 2861,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 951
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2861,
          "cache_read_input_tokens": 42154,
          "cache_creation_input_tokens": 951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 951,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 12
    }
  },
  "sourceToolAssistantUUID": "22039368-b2ec-4cbd-a133-e3c688144802",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"Verifier Disagreement as Tail-Preservation Signal in Synthetic Data Cu…",
  "leafUuid": "31dab7e8-ad0f-450f-ae28-553525c16701",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise verifier disagreement tail-preservation hypothesis",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97"
}
```

---

### Tool result

_source line 22 · 2026-05-19T09:25:51.594Z_

<details><summary>↩ Tool result · `toolu_01CgEAiLm3d4CTZmX6u9T4QH`</summary>

```text
Now I have enough evidence to provide a comprehensive, honest assessment. Here is my analysis:

---

## Deep Research Report: Does Verifier Disagreement Correlate with Distribution-Tail Data?

### Executive Summary

**The reviewers are substantially correct to flag this claim as unsubstantiated.** There is no direct theoretical result establishing that ensemble/verifier disagreement specifically correlates with distribution-tail data. The relationship is indirect, partial, and confounded. Disagreement is a general signal of epistemic uncertainty, which is elevated for tail data, but is equally elevated for noise, ambiguity, label errors, and adversarial inputs. The claim as stated conflates a necessary condition (tail data causes disagreement) with a sufficient condition (disagreement identifies tail data), and the literature does not support the latter.

---

### 1. What the Epistemic vs. Aleatoric Uncertainty Literature Says

The most fundamental issue is the well-established distinction between **epistemic uncertainty** (reducible, due to lack of knowledge/data) and **aleatoric uncertainty** (irreducible, due to inherent noise or ambiguity).

Ensemble disagreement is widely recognized as a proxy for **epistemic uncertainty** specifically. The mutual information between ensemble member predictions and the ensemble index is mathematically equivalent to ensemble disagreement ([Efficient Epistemic Uncertainty Estimation in Regression Ensemble Models](https://arxiv.org/pdf/2308.13498)). This is the foundation of methods like **BALD** (Bayesian Active Learning by Disagreement), which selects points where epistemic uncertainty is highest ([BALD overview](https://www.emergentmind.com/topics/bayesian-active-learning-by-disagreement-bald)).

**However**, recent work seriously challenges the clean separation. A 2025 ICLR blog post documents that estimates from epistemic and aleatoric estimators are internally rank-correlated by **0.8 to 0.999**, and that aleatoric uncertainty estimators are approximately as predictive for OOD detection as epistemic ones ([Reexamining the Aleatoric and Epistemic Uncertainty Dichotomy](https://iclr-blogposts.github.io/2025/blog/reexamining-the-aleatoric-and-epistemic-uncertainty-dichotomy/)). This means disagreement captures a mixture of both signal types, making it unreliable as a pure indicator of either tail data or noise.

**Bottom line:** Disagreement captures epistemic uncertainty, which is high for tail/rare data -- but also high for noisy, ambiguous, mislabeled, or adversarial examples. The literature explicitly warns against interpreting high disagreement as indicating any single cause.

---

### 2. Is There a Theoretical Result Linking Disagreement to Tail-of-Distribution Data?

**No direct theoretical result exists.** I searched extensively and found nothing that establishes a formal connection between ensemble disagreement and tail-of-distribution data specifically. The closest results are:

- **Seung, Opper & Sompolinsky (1992)** -- the foundational QBC paper -- proves that committee disagreement is maximized near decision boundaries in version space. This is about **decision boundaries**, not distribution tails. The two can overlap (decision boundaries may be more uncertain in low-density regions) but are not the same concept ([Query by Committee, 1992](https://dl.acm.org/doi/10.1145/130385.130417)).

- **Theisen et al. (NeurIPS 2023), "When Are Ensembles Really Effective?"** -- proves that ensemble improvement is bounded by linear functions of the disagreement-error ratio. This tells us when ensembling helps but says nothing about whether disagreement localizes to distribution tails ([When are ensembles really effective?](https://arxiv.org/abs/2305.12313)).

- **"The Disparate Benefits of Deep Ensembles" (2024)** -- shows that ensembles disproportionately benefit minority/underrepresented groups, with per-group differences in predictive diversity explaining the effect. This is the closest empirical evidence to the claim: ensembles help more on rare subgroups because disagreement (diversity) is higher there. But this is about **performance improvement from ensembling**, not about using disagreement as a **data curation signal** ([The Disparate Benefits of Deep Ensembles](https://arxiv.org/abs/2410.13831)).

- **"Subsampled Ensemble Can Improve Generalization Tail Exponentially" (2024)** -- shows ensembles can achieve exponentially decaying tails for excess risk. Again, about ensemble performance on tail risk, not about disagreement as a selector for tail data ([arxiv.org/pdf/2405.14741](https://arxiv.org/pdf/2405.14741)).

There is an informal intuition in the literature that ensemble members will disagree more in low-density regions of the data distribution (because fewer training examples constrain the models there), and low-density regions include distribution tails. But **this intuition has been explicitly challenged**: research on deep ensembles for OOD detection shows that the diversity-implies-distributional-shift intuition "is not valid for OOD detection for CNNs at ImageNet-scale" ([On the Usefulness of Deep Ensemble Diversity for OOD Detection](https://arxiv.org/pdf/2207.07517); [Revisiting Deep Ensemble for OOD Detection](https://arxiv.org/pdf/2310.14227)).

---

### 3. Active Learning / QBC: Distinguishing Informative from Noisy Disagreement

The active learning literature is acutely aware that disagreement-based selection is **biased toward outliers and noise**:

- QBC "can be biased towards outliers or noisy samples, which can be very uncertain but not very informative" ([Active Learning overview](https://medium.com/data-science/active-learning-overview-strategies-and-uncertainty-measures-521565e0b0b)).
- Uncertainty sampling "runs the risk of gravitating towards complex or noisy instances" and "the density of such noisy samples is higher near the classification boundary" ([Improve Cost Efficiency of Active Learning over Noisy Dataset](https://arxiv.org/html/2403.01346v1)).
- Active learning "may always incorporate a bias simply because the data is no longer produced by sampling independently according to the true underlying distribution" ([Mitigating Sampling Bias in Active Learning](https://arxiv.org/pdf/2109.06321)).

**Proposed solutions** include:
- Combining uncertainty with **density-weighted** approaches (favoring high-disagreement points in high-density regions, which explicitly works against selecting tail data) ([Distribution Aware Active Learning](https://arxiv.org/pdf/1805.08916))
- **Evidential uncertainty** methods that decompose uncertainty more carefully ([Evidential Uncertainty Sampling](https://arxiv.org/pdf/2309.12494))
- **Batch-BALD** and **Core-set** methods that add diversity constraints to prevent over-selection of noisy clusters

The key insight from this literature: **without additional mechanisms, disagreement alone cannot distinguish informative samples from noisy ones**. The standard fix is to weight by density or add representativeness constraints -- which would actually suppress tail examples.

---

### 4. Reward Model Disagreement in LLM Settings

The LLM/RLHF literature provides the most relevant practical context:

- **Reward model ensembles** are used to detect reward hacking and OOD inputs. High disagreement among reward models is treated as a signal of **unreliability**, not as a signal of tail-data value ([Reward-Robust RLHF in LLMs](https://arxiv.org/html/2409.15360v1)).
- **"Ask a Strong LLM Judge when Your Reward Model is Uncertain" (NeurIPS 2025)** routes high-disagreement samples to a stronger judge, treating disagreement as indicating **unreliable RM predictions**, not distribution-tail value. The paper explicitly frames disagreement as capturing cases where "classical RMs trained on human preferences are vulnerable to reward hacking and generalize poorly to out-of-distribution inputs" ([Ask a Strong LLM Judge](https://arxiv.org/abs/2510.20369)).
- **Policy Filtration for RLHF** filters out samples where reward estimates are unreliable (high disagreement), improving signal-to-noise ratio by **removing** high-disagreement samples rather than prioritizing them ([Policy Filtration for RLHF](https://arxiv.org/pdf/2409.06957)).
- **Uncertainty-Weighted Optimization** penalizes high disagreement among reward models ([Reward-Robust RLHF](https://arxiv.org/html/2409.15360v1)).

The operational consensus in the RLHF literature is that disagreement indicates **unreliability** and should be handled with caution (routing, filtering, or penalizing), not that it identifies valuable tail data.

---

### 5. The Ensembles with Regularized Disagreement (ERD) Result

One paper provides a partial counter-argument: **Tifrea et al. (UAI 2022), "Semi-supervised novelty detection using ensembles with regularized disagreement"** shows that with careful regularization, ensemble disagreement can be channeled to specifically indicate OOD/novel inputs rather than noise ([Semi-supervised novelty detection using ensembles with regularized disagreement](https://arxiv.org/abs/2012.05825)). However, this requires:
1. Regularization to suppress in-distribution disagreement
2. Access to unlabeled OOD data during training
3. The specific goal of novelty detection (binary OOD vs. in-distribution)

This is far from a general result that "verifier disagreement correlates with distribution-tail data" -- it is an engineered system designed to make disagreement do something it does not naturally do.

---

### 6. The Epistemic Uncertainty Collapse Problem

A further complication for large models: **"(Implicit) Ensembles of Ensembles: Epistemic Uncertainty Collapse in Large Models" (2024)** shows that as ensemble size and model capacity grow, ensemble members converge to similar predictive distributions, causing disagreement-based uncertainty measures to **collapse to zero** ([Epistemic Uncertainty Collapse](https://arxiv.org/html/2409.02628)). This suggests that for the large models relevant to LLM training, disagreement may become an increasingly unreliable signal of anything at all.

---

### 7. Synthesis and Verdict

**The claim that "verifier disagreement correlates with distribution-tail data" has at best weak, indirect support and significant counter-evidence.**

| Aspect | Evidence |
|--------|----------|
| Disagreement is high for tail data | Plausible (low-density = less constrained models = more disagreement), but not formally proven for distribution tails specifically |
| Disagreement is high ONLY for tail data | **False.** Disagreement is also high for noise, ambiguity, mislabeling, adversarial inputs, and decision boundaries in high-density regions |
| There exists a theoretical result | **No.** No theorem links disagreement to distribution tails. QBC theory is about decision boundaries. Ensemble theory is about disagreement-error ratios. |
| Empirical evidence in LLM settings | **Works against the claim.** The RLHF literature treats disagreement as unreliability, filtering or penalizing it rather than using it to identify valuable tail data. |
| Conditions for disagreement to be useful | Requires additional mechanisms (density weighting, regularization, representativeness constraints) that are not part of the claim |
| Direct experiments | **None found** demonstrating that verifier disagreement specifically identifies distribution-tail data in a synthetic data curation pipeline |

**The reviewers are correct:** the claim is unsubstantiated. Disagreement is a **necessary but not sufficient** indicator of tail data. It is an omnibus signal of uncertainty that could equally indicate noise, ambiguity, or adversarial examples. Without a mechanism to decompose disagreement into its sources (epistemic from data sparsity vs. aleatoric from inherent ambiguity vs. noise from labeling errors), the claim that it specifically identifies distribution-tail data is not supported by the existing literature.

If the authors want to rescue this claim, they would need to either:
1. Provide empirical evidence from their specific pipeline showing that high-disagreement samples are disproportionately drawn from distribution tails (with a clear operational definition of "tail")
2. Describe a decomposition mechanism that separates tail-induced disagreement from noise-induced disagreement
3. Cite the ERD-style work but acknowledge it requires specific architectural choices not present in generic verifier ensembles

---

Sources:
- [Efficient Epistemic Uncertainty Estimation in Regression Ensemble Models](https://arxiv.org/pdf/2308.13498)
- [BALD: Bayesian Active Learning by Disagreement](https://www.emergentmind.com/topics/bayesian-active-learning-by-disagreement-bald)
- [Reexamining the Aleatoric and Epistemic Uncertainty Dichotomy (ICLR 2025)](https://iclr-blogposts.github.io/2025/blog/reexamining-the-aleatoric-and-epistemic-uncertainty-dichotomy/)
- [Query by Committee (Seung, Opper, Sompolinsky 1992)](https://dl.acm.org/doi/10.1145/130385.130417)
- [When Are Ensembles Really Effective? (NeurIPS 2023)](https://arxiv.org/abs/2305.12313)
- [The Disparate Benefits of Deep Ensembles (2024)](https://arxiv.org/abs/2410.13831)
- [Subsampled Ensemble Can Improve Generalization Tail Exponentially (2024)](https://arxiv.org/pdf/2405.14741)
- [On the Usefulness of Deep Ensemble Diversity for OOD Detection](https://arxiv.org/pdf/2207.07517)
- [Revisiting Deep Ensemble for OOD Detection: A Loss Landscape Perspective](https://arxiv.org/pdf/2310.14227)
- [Semi-supervised Novelty Detection Using Ensembles with Regularized Disagreement (UAI 2022)](https://arxiv.org/abs/2012.05825)
- [(Implicit) Ensembles of Ensembles: Epistemic Uncertainty Collapse in Large Models (2024)](https://arxiv.org/html/2409.02628)
- [Reward-Robust RLHF in LLMs](https://arxiv.org/html/2409.15360v1)
- [Ask a Strong LLM Judge when Your Reward Model is Uncertain (NeurIPS 2025)](https://arxiv.org/abs/2510.20369)
- [Policy Filtration for RLHF to Mitigate Noise in Reward Models](https://arxiv.org/pdf/2409.06957)
- [Improve Cost Efficiency of Active Learning over Noisy Dataset](https://arxiv.org/html/2403.01346v1)
- [Distribution Aware Active Learning](https://arxiv.org/pdf/1805.08916)
- [Evidential Uncertainty Sampling for Active Learning](https://arxiv.org/pdf/2309.12494)
- [Mitigating Sampling Bias and Improving Robustness in Active Learning](https://arxiv.org/pdf/2109.06321)
- [A Deeper Look into Aleatoric and Epistemic Uncertainty Disentanglement](https://arxiv.org/pdf/2204.09308)
- [Training Ensembles to Detect Adversarial Examples](https://arxiv.org/pdf/1712.04006)
- [Disagreement on Tail (Chen et al.)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5628930)
- [Escaping Collapse: The Strength of Weak Data for LLM Training](https://arxiv.org/pdf/2502.08924)

agentId: a8f9f53d72f9bd1a5 (use SendMessage with to: 'a8f9f53d72f9bd1a5' to continue this agent)
&lt;usage>total_tokens: 32475
tool_uses: 24
duration_ms: 163797&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e769e91-6796-43ed-a7fd-cafe40891d32",
  "isSidechain": false,
  "promptId": "ae35a659-7407-4079-9c58-2bf4f6ffeb73",
  "type": "user",
  "uuid": "060d5ee1-9d71-4efe-b3d3-694c94016bd4",
  "toolUseResult": {
    "status": "completed",
    "prompt": "A research proposal claims that \"verifier disagreement correlates with distribution-tail data\" in the context of synthetic data curation for LLM training. Reviewers flagged this as unsubstantiated — disagreement could equally indicate noise, ambiguity, or adversarial samples.\n\nI need you to deeply research whether there is theoretical or empirical support for this hypothesis. Please:\n\n1. Search for: \"classifier disagreement distribution tail\" and \"ensemble disagreement rare examples machine learning\"\n2. Search for: \"query by committee uncertainty sampling tail distribution\"\n3. Search for: \"reward model disagreement out of distribution\" and \"ensemble disagreement epistemic uncertainty\"\n4. Search for: \"verifier disagreement noise vs signal synthetic data\"\n\nKey questions to answer:\n- Is there ANY theoretical result linking ensemble/committee disagreement to tail-of-distribution data specifically?\n- What does the epistemic vs aleatoric uncertainty literature say? (Disagreement often captures epistemic uncertainty, which could be high for BOTH tail data AND noise)\n- Are there results from active learning/QBC that distinguish \"informative disagreement\" from \"noisy disagreement\"?\n- What conditions are needed for disagreement to be a useful signal rather than noise?\n- Are there any toy/pilot experiments in the literature demonstrating this connection?\n\nBe thorough and honest — if the evidence is weak, say so. This is the most critical issue in the review.",
    "agentId": "a8f9f53d72f9bd1a5",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have enough evidence to provide a comprehensive, honest assessment. Here is my analysis:\n\n---\n\n## Deep Research Report: Does Verifier Disagreement Correlate with Distribution-Tail Data?\n\n### Executive Summary\n\n**The reviewers are substantially correct to flag this claim as unsubstantiated.** There is no direct theoretical result establishing that ensemble/verifier disagreement specifically correlates with distribution-tail data. The relationship is indirect, partial, and confounded. Disagreement is a general signal of epistemic uncertainty, which is elevated for tail data, but is equally elevated for noise, ambiguity, label errors, and adversarial inputs. The claim as stated conflates a necessary condition (tail data causes disagreement) with a sufficient condition (disagreement identifies tail data), and the literature does not support the latter.\n\n---\n\n### 1. What the Epistemic vs. Aleatoric Uncertainty Literature Says\n\nThe most fundamental issue is the well-established distinction between **epistemic uncertainty** (reducible, due to lack of knowledge/data) and **aleatoric uncertainty** (irreducible, due to inherent noise or ambiguity).\n\nEnsemble disagreement is widely recognized as a proxy for **epistemic uncertainty** specifically. The mutual information between ensemble member predictions and the ensemble index is mathematically equivalent to ensemble disagreement ([Efficient Epistemic Uncertainty Estimation in Regression Ensemble Models](https://arxiv.org/pdf/2308.13498)). This is the foundation of methods like **BALD** (Bayesian Active Learning by Disagreement), which selects points where epistemic uncertainty is highest ([BALD overview](https://www.emergentmind.com/topics/bayesian-active-learning-by-disagreement-bald)).\n\n**However**, recent work seriously challenges the clean separation. A 2025 ICLR blog post documents that estimates from epistemic and aleatoric estimators are internally rank-correlated by **0.8 to 0.999**, and that aleatoric uncertainty estimators are approximately as predictive for OOD detection as epistemic ones ([Reexamining the Aleatoric and Epistemic Uncertainty Dichotomy](https://iclr-blogposts.github.io/2025/blog/reexamining-the-aleatoric-and-epistemic-uncertainty-dichotomy/)). This means disagreement captures a mixture of both signal types, making it unreliable as a pure indicator of either tail data or noise.\n\n**Bottom line:** Disagreement captures epistemic uncertainty, which is high for tail/rare data -- but also high for noisy, ambiguous, mislabeled, or adversarial examples. The literature explicitly warns against interpreting high disagreement as indicating any single cause.\n\n---\n\n### 2. Is There a Theoretical Result Linking Disagreement to Tail-of-Distribution Data?\n\n**No direct theoretical result exists.** I searched extensively and found nothing that establishes a formal connection between ensemble disagreement and tail-of-distribution data specifically. The closest results are:\n\n- **Seung, Opper & Sompolinsky (1992)** -- the foundational QBC paper -- proves that committee disagreement is maximized near decision boundaries in version space. This is about **decision boundaries**, not distribution tails. The two can overlap (decision boundaries may be more uncertain in low-density regions) but are not the same concept ([Query by Committee, 1992](https://dl.acm.org/doi/10.1145/130385.130417)).\n\n- **Theisen et al. (NeurIPS 2023), \"When Are Ensembles Really Effective?\"** -- proves that ensemble improvement is bounded by linear functions of the disagreement-error ratio. This tells us when ensembling helps but says nothing about whether disagreement localizes to distribution tails ([When are ensembles really effective?](https://arxiv.org/abs/2305.12313)).\n\n- **\"The Disparate Benefits of Deep Ensembles\" (2024)** -- shows that ensembles disproportionately benefit minority/underrepresented groups, with per-group differences in predictive diversity explaining the effect. This is the closest empirical evidence to the claim: ensembles help more on rare subgroups because disagreement (diversity) is higher there. But this is about **performance improvement from ensembling**, not about using disagreement as a **data curation signal** ([The Disparate Benefits of Deep Ensembles](https://arxiv.org/abs/2410.13831)).\n\n- **\"Subsampled Ensemble Can Improve Generalization Tail Exponentially\" (2024)** -- shows ensembles can achieve exponentially decaying tails for excess risk. Again, about ensemble performance on tail risk, not about disagreement as a selector for tail data ([arxiv.org/pdf/2405.14741](https://arxiv.org/pdf/2405.14741)).\n\nThere is an informal intuition in the literature that ensemble members will disagree more in low-density regions of the data distribution (because fewer training examples constrain the models there), and low-density regions include distribution tails. But **this intuition has been explicitly challenged**: research on deep ensembles for OOD detection shows that the diversity-implies-distributional-shift intuition \"is not valid for OOD detection for CNNs at ImageNet-scale\" ([On the Usefulness of Deep Ensemble Diversity for OOD Detection](https://arxiv.org/pdf/2207.07517); [Revisiting Deep Ensemble for OOD Detection](https://arxiv.org/pdf/2310.14227)).\n\n---\n\n### 3. Active Learning / QBC: Distinguishing Informative from Noisy Disagreement\n\nThe active learning literature is acutely aware that disagreement-based selection is **biased toward outliers and noise**:\n\n- QBC \"can be biased towards outliers or noisy samples, which can be very uncertain but not very informative\" ([Active Learning overview](https://medium.com/data-science/active-learning-overview-strategies-and-uncertainty-measures-521565e0b0b)).\n- Uncertainty sampling \"runs the risk of gravitating towards complex or noisy instances\" and \"the density of such noisy samples is higher near the classification boundary\" ([Improve Cost Efficiency of Active Learning over Noisy Dataset](https://arxiv.org/html/2403.01346v1)).\n- Active learning \"may always incorporate a bias simply because the data is no longer produced by sampling independently according to the true underlying distribution\" ([Mitigating Sampling Bias in Active Learning](https://arxiv.org/pdf/2109.06321)).\n\n**Proposed solutions** include:\n- Combining uncertainty with **density-weighted** approaches (favoring high-disagreement points in high-density regions, which explicitly works against selecting tail data) ([Distribution Aware Active Learning](https://arxiv.org/pdf/1805.08916))\n- **Evidential uncertainty** methods that decompose uncertainty more carefully ([Evidential Uncertainty Sampling](https://arxiv.org/pdf/2309.12494))\n- **Batch-BALD** and **Core-set** methods that add diversity constraints to prevent over-selection of noisy clusters\n\nThe key insight from this literature: **without additional mechanisms, disagreement alone cannot distinguish informative samples from noisy ones**. The standard fix is to weight by density or add representativeness constraints -- which would actually suppress tail examples.\n\n---\n\n### 4. Reward Model Disagreement in LLM Settings\n\nThe LLM/RLHF literature provides the most relevant practical context:\n\n- **Reward model ensembles** are used to detect reward hacking and OOD inputs. High disagreement among reward models is treated as a signal of **unreliability**, not as a signal of tail-data value ([Reward-Robust RLHF in LLMs](https://arxiv.org/html/2409.15360v1)).\n- **\"Ask a Strong LLM Judge when Your Reward Model is Uncertain\" (NeurIPS 2025)** routes high-disagreement samples to a stronger judge, treating disagreement as indicating **unreliable RM predictions**, not distribution-tail value. The paper explicitly frames disagreement as capturing cases where \"classical RMs trained on human preferences are vulnerable to reward hacking and generalize poorly to out-of-distribution inputs\" ([Ask a Strong LLM Judge](https://arxiv.org/abs/2510.20369)).\n- **Policy Filtration for RLHF** filters out samples where reward estimates are unreliable (high disagreement), improving signal-to-noise ratio by **removing** high-disagreement samples rather than prioritizing them ([Policy Filtration for RLHF](https://arxiv.org/pdf/2409.06957)).\n- **Uncertainty-Weighted Optimization** penalizes high disagreement among reward models ([Reward-Robust RLHF](https://arxiv.org/html/2409.15360v1)).\n\nThe operational consensus in the RLHF literature is that disagreement indicates **unreliability** and should be handled with caution (routing, filtering, or penalizing), not that it identifies valuable tail data.\n\n---\n\n### 5. The Ensembles with Regularized Disagreement (ERD) Result\n\nOne paper provides a partial counter-argument: **Tifrea et al. (UAI 2022), \"Semi-supervised novelty detection using ensembles with regularized disagreement\"** shows that with careful regularization, ensemble disagreement can be channeled to specifically indicate OOD/novel inputs rather than noise ([Semi-supervised novelty detection using ensembles with regularized disagreement](https://arxiv.org/abs/2012.05825)). However, this requires:\n1. Regularization to suppress in-distribution disagreement\n2. Access to unlabeled OOD data during training\n3. The specific goal of novelty detection (binary OOD vs. in-distribution)\n\nThis is far from a general result that \"verifier disagreement correlates with distribution-tail data\" -- it is an engineered system designed to make disagreement do something it does not naturally do.\n\n---\n\n### 6. The Epistemic Uncertainty Collapse Problem\n\nA further complication for large models: **\"(Implicit) Ensembles of Ensembles: Epistemic Uncertainty Collapse in Large Models\" (2024)** shows that as ensemble size and model capacity grow, ensemble members converge to similar predictive distributions, causing disagreement-based uncertainty measures to **collapse to zero** ([Epistemic Uncertainty Collapse](https://arxiv.org/html/2409.02628)). This suggests that for the large models relevant to LLM training, disagreement may become an increasingly unreliable signal of anything at all.\n\n---\n\n### 7. Synthesis and Verdict\n\n**The claim that \"verifier disagreement correlates with distribution-tail data\" has at best weak, indirect support and significant counter-evidence.**\n\n| Aspect | Evidence |\n|--------|----------|\n| Disagreement is high for tail data | Plausible (low-density = less constrained models = more disagreement), but not formally proven for distribution tails specifically |\n| Disagreement is high ONLY for tail data | **False.** Disagreement is also high for noise, ambiguity, mislabeling, adversarial inputs, and decision boundaries in high-density regions |\n| There exists a theoretical result | **No.** No theorem links disagreement to distribution tails. QBC theory is about decision boundaries. Ensemble theory is about disagreement-error ratios. |\n| Empirical evidence in LLM settings | **Works against the claim.** The RLHF literature treats disagreement as unreliability, filtering or penalizing it rather than using it to identify valuable tail data. |\n| Conditions for disagreement to be useful | Requires additional mechanisms (density weighting, regularization, representativeness constraints) that are not part of the claim |\n| Direct experiments | **None found** demonstrating that verifier disagreement specifically identifies distribution-tail data in a synthetic data curation pipeline |\n\n**The reviewers are correct:** the claim is unsubstantiated. Disagreement is a **necessary but not sufficient** indicator of tail data. It is an omnibus signal of uncertainty that could equally indicate noise, ambiguity, or adversarial examples. Without a mechanism to decompose disagreement into its sources (epistemic from data sparsity vs. aleatoric from inherent ambiguity vs. noise from labeling errors), the claim that it specifically identifies distribution-tail data is not supported by the existing literature.\n\nIf the authors want to rescue this claim, they would need to either:\n1. Provide empirical evidence from their specific pipeline showing that high-disagreement samples are disproportionately drawn from distribution tails (with a clear operational definition of \"tail\")\n2. Describe a decomposition mechanism that separates tail-induced disagreement from noise-induced disagreement\n3. Cite the ERD-style work but acknowledge it requires specific architectural choices not present in generic verifier ensembles\n\n---\n\nSources:\n- [Efficient Epistemic Uncertainty Estimation in Regression Ensemble Models](https://arxiv.org/pdf/2308.13498)\n- [BALD: Bayesian Active Learning by Disagreement](https://www.emergentmind.com/topics/bayesian-active-learning-by-disagreement-bald)\n- [Reexamining the Aleatoric and Epistemic Uncertainty Dichotomy (ICLR 2025)](https://iclr-blogposts.github.io/2025/blog/reexamining-the-aleatoric-and-epistemic-uncertainty-dichotomy/)\n- [Query by Committee (Seung, Opper, Sompolinsky 1992)](https://dl.acm.org/doi/10.1145/130385.130417)\n- [When Are Ensembles Really Effective? (NeurIPS 2023)](https://arxiv.org/abs/2305.12313)\n- [The Disparate Benefits of Deep Ensembles (2024)](https://arxiv.org/abs/2410.13831)\n- [Subsampled Ensemble Can Improve Generalization Tail Exponentially (2024)](https://arxiv.org/pdf/2405.14741)\n- [On the Usefulness of Deep Ensemble Diversity for OOD Detection](https://arxiv.org/pdf/2207.07517)\n- [Revisiting Deep Ensemble for OOD Detection: A Loss Landscape Perspective](https://arxiv.org/pdf/2310.14227)\n- [Semi-supervised Novelty Detection Using Ensembles with Regularized Disagreement (UAI 2022)](https://arxiv.org/abs/2012.05825)\n- [(Implicit) Ensembles of Ensembles: Epistemic Uncertainty Collapse in Large Models (2024)](https://arxiv.org/html/2409.02628)\n- [Reward-Robust RLHF in LLMs](https://arxiv.org/html/2409.15360v1)\n- [Ask a Strong LLM Judge when Your Reward Model is Uncertain (NeurIPS 2025)](https://arxiv.org/abs/2510.20369)\n- [Policy Filtration for RLHF to Mitigate Noise in Reward Models](https://arxiv.org/pdf/2409.06957)\n- [Improve Cost Efficiency of Active Learning over Noisy Dataset](https://arxiv.org/html/2403.01346v1)\n- [Distribution Aware Active Learning](https://arxiv.org/pdf/1805.08916)\n- [Evidential Uncertainty Sampling for Active Learning](https://arxiv.org/pdf/2309.12494)\n- [Mitigating Sampling Bias and Improving Robustness in Active Learning](https://arxiv.org/pdf/2109.06321)\n- [A Deeper Look into Aleatoric and Epistemic Uncertainty Disentanglement](https://arxiv.org/pdf/2204.09308)\n- [Training Ensembles to Detect Adversarial Examples](https://arxiv.org/pdf/1712.04006)\n- [Disagreement on Tail (Chen et al.)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5628930)\n- [Escaping Collapse: The Strength of Weak Data for LLM Training](https://arxiv.org/pdf/2502.08924)"
      }
    ],
    "totalDurationMs": 163797,
    "totalTokens": 32475,
    "totalToolUseCount": 24,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2903,
      "cache_read_input_tokens": 25710,
      "output_tokens": 3861,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2903
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3861,
          "cache_read_input_tokens": 25710,
          "cache_creation_input_tokens": 2903,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2903,
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
  "sourceToolAssistantUUID": "8e769e91-6796-43ed-a7fd-cafe40891d32",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"Verifier Disagreement as Tail-Preservation Signal in Synthetic Data Cu…",
  "leafUuid": "060d5ee1-9d71-4efe-b3d3-694c94016bd4",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise verifier disagreement tail-preservation hypothesis",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97"
}
```

---

### Tool result

_source line 25 · 2026-05-19T09:25:59.609Z_

<details><summary>↩ Tool result · `toolu_01Lm4y8gakZqPGnoFkBZZsEW`</summary>

```text
I now have comprehensive information from multiple sources. Let me compile my detailed findings.

---

Here is my detailed research report on arXiv 2604.07650 and its implications for your research proposal.

---

## Paper Identity

**Title:** "How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles"
**Authors:** Chenchen Kuai, Jiwan Jiang, Zihao Zhu, Hao Wang, Keshu Wu, Zihao Li, Yunlong Zhang, Chenxi Liu, Zhengzhong Tu, Zhiwen Fan, Yang Zhou (Texas A&M University)
**Published:** April 8, 2026 (arXiv:2604.07650)

---

## 1. What Exactly Is "Behavioral Entanglement"?

The paper defines behavioral entanglement as: "ostensibly independent models exhibit synchronized reasoning patterns and similar failure modes despite being developed separately." The core claim is that shared pretraining data, knowledge distillation, and alignment pipelines induce **hidden behavioral dependencies** ("latent entanglement") that cause LLMs to fail on the same problems in the same ways, even across model families.

The critical insight: "apparent agreement may reflect correlated failure rather than independent verification." When multiple LLM judges unanimously endorse an answer, this consensus may be an artifact of shared training lineage rather than genuine independent validation.

The paper formalizes this through a **multi-resolution statistical hierarchy**:

- **Level 1 (Binary):** The Difficulty-Weighted Behavioral Entanglement Index (BEI_w) measures whether two models fail on the same problems more often than expected under conditional independence given task difficulty. It uses residuals from logistic regression on difficulty, weighted by task easiness (a_t = 1 - d_t) to emphasize synchronized failures on easy tasks (where co-failure is statistically unlikely under independence). Significance is tested via sign-flip randomization.

- **Level 2 (Categorical):** The Cumulative Information Gain (CIG) metric measures whether model pairs select the **same wrong answer** more often than expected. It incorporates distractor attractiveness and surprisal weighting. This captures directional alignment in errors -- not just that models fail together, but that they fail identically.

---

## 2. How Correlated Are LLM-Based Verifiers' Biases?

The quantitative findings are striking. Tested on 18 LLMs across 6 families (GPT, Claude, Qwen, Llama, Gemini, DeepSeek) using MMLU-Pro:

**Within-family entanglement (strongest):**
- Llama-3-70B / Llama-3.1-70B: BEI = 0.0446 (p < 0.0001), CIG = 403.37 (p < 0.0001)
- Qwen1.5-14B / Qwen1.5-72B: CIG = 260.07

**Cross-family entanglement (weaker but statistically significant):**
- DeepSeek-v2.5 / Gemini-1.5-Flash: CIG = 260.53 (p < 0.0001)
- Gemini / Claude pairs: CIG = 238.36

**Impact on judge precision:** CIG exhibits Spearman correlation of **0.64 (p < 0.001)** with GPT-4o-mini judge precision degradation and **0.71 (p < 0.01)** with Llama3-based judge precision degradation. Stronger entanglement directly corresponds to increased **over-endorsement bias** -- judges systematically approve incorrect answers from entangled models.

**Era-based clustering:** The paper identifies that frontier models from the same era (e.g., GPT-5, Claude 4.6, Gemini 3.1) show cross-family synchronization that goes beyond genealogical lineage, suggesting alignment-era convergence effects.

---

## 3. Does the Paper Distinguish LLM-Only Panels vs. Mixed Panels (LLM + Symbolic)?

**No.** This is a critical gap. The paper treats all 18 models as black-box LLM judges evaluating MCQ correctness. There is **zero discussion** of:
- Symbolic checkers or formal verifiers
- Rule-based verification systems
- Non-neural verification approaches
- Mixed/hybrid verification panels
- ORM vs. PRM distinction

The paper's scope is exclusively **LLM-to-LLM entanglement**. The framework requires black-box access to model outputs and is designed for analyzing neural model ensembles, not heterogeneous verification systems.

---

## 4. What Are the Implications for Using Diverse Verifier Panels?

The paper's central warning is that **"apparent agreement among LLMs should not be treated as evidence of independence."** Specific implications:

- **Majority voting is vulnerable:** Entanglement-unaware majority voting across LLM judges achieves only 0.847 accuracy. The entanglement-aware reweighting achieves 0.896 (a 4.5% gain).
- **Family diversity is necessary but insufficient:** Cross-family entanglement is weaker than within-family, but it still exists at statistically significant levels. Simply picking one model from each family does not guarantee independence.
- **Self-preference bias compounds the problem:** Judges favor outputs from related models and models within their family, creating a feedback loop where entangled judges preferentially endorse entangled generators.

---

## 5. Suggested Mitigations

The paper proposes **one mitigation**: De-entangled Verifier Ensemble Reweighting. The method:

1. Computes pairwise entanglement: E(i,j) = lambda_1 * BEI(i,j) + (1-lambda_1) * CIG(i,j)
2. Measures each verifier's **internal dependence** (average entanglement with other panel members) and **target dependence** (entanglement with the model being evaluated)
3. Reweights verifiers via softmax: w_m = exp(kappa * log(q_m) - eta_1 * Delta_in_m - eta_2 * Delta_tar_m) / Z, where q_m is competence, eta_1 penalizes internal redundancy, eta_2 penalizes target alignment.

This achieves 0.896 accuracy vs. 0.847 for majority voting and 0.881 for competence-only reweighting.

No other mitigations are proposed. The paper does not suggest adding non-LLM verifiers as a decorrelation strategy.

---

## 6. ORM vs. PRM vs. Rule-Based Verifiers

The paper itself says **nothing** about these distinctions. However, I found highly relevant complementary evidence from related work:

**From "Reward Models Inherit Value Biases from Pretraining" (arXiv 2601.20838, Jan 2026):** Reward models (including ORMs and PRMs) inherit persistent value biases from their base LLM. Llama-based RMs systematically prefer "agency" while Gemma-based RMs prefer "communion" -- even with identical finetuning data. This means an ORM and a PRM built on the same base model will share correlated biases.

**From "Helping or Herding?" (arXiv 2312.09244):** Reward model ensembles mitigate but do not eliminate reward hacking. Pretrain-seed diversity outperforms finetune-only diversity, but "several qualitative reward hacking phenomena persist across all ensemble members." Shared pretraining causes all models in the ensemble to exhibit similar error patterns.

**From "From Accuracy to Robustness" (arXiv 2505.22203, May 2025):** Rule-based verifiers and model-based verifiers have **qualitatively different failure modes**:
- Rule-based verifiers: format-sensitivity causing **false negatives** (missing correct answers in non-standard formats)
- Model-based verifiers: susceptible to **hacking** and pattern exploitation causing false positives

This is a key finding: the failure modes are structurally different, which suggests a mixed panel genuinely does provide some decorrelation.

---

## Assessment: How Seriously Does This Undermine the ORM + PRM + Symbolic Checker Panel?

**The short answer: it partially undermines it, but less than you might fear, because the paper's scope is narrower than your design.**

Here is the nuanced breakdown:

**What the paper DOES threaten:**
- The assumption that an ORM and a PRM produce independent signals. If both are neural models trained on similar data (especially the same base model), their errors will be correlated. The BEI and CIG metrics would likely show significant entanglement between an ORM and PRM from the same model family.
- The assumption that "structural diversity" (different training objectives: outcome vs. process) is sufficient to decorrelate. The paper shows that shared pretraining dominates -- models fail together because of shared knowledge representations, not because of similar training objectives.
- Any verification pipeline that uses multiple LLM judges and treats their agreement as evidence of correctness.

**What the paper does NOT threaten (and where your design has a genuine advantage):**
- **The symbolic checker component.** The paper studies exclusively LLM-to-LLM entanglement. A symbolic/rule-based checker has no shared pretraining, no alignment pipeline, no knowledge distillation lineage. Its failure modes are **categorically different** (format-sensitivity false negatives vs. neural hallucination false positives, per arXiv 2505.22203). The behavioral entanglement framework literally cannot apply to a system that was never pretrained.
- **The decorrelation between neural and non-neural verifiers.** The entanglement arises from shared training data and procedures. A Z3 solver, a unit test harness, or a type checker shares none of these. The independence assumption is far more defensible for LLM + symbolic than for LLM + LLM.

**Concrete recommendations for your proposal:**

1. **Acknowledge the paper explicitly.** Cite it to show you are aware that ORM-PRM independence is weaker than naive "structural diversity" suggests.

2. **Reframe your diversity argument.** Do not claim ORM + PRM + symbolic provides "three independent signals." Instead argue it provides "two partially correlated neural signals plus one categorically independent non-neural signal." The symbolic checker is the genuine source of decorrelation; the ORM/PRM split provides weaker (but non-zero) diversity.

3. **If your ORM and PRM use the same base model, flag this.** The entanglement will be strongest in this case. Consider using ORM and PRM from different model families to at least get cross-family decorrelation (BEI ~0.01-0.03 rather than ~0.04+).

4. **Consider applying the de-entangled reweighting.** The paper's reweighting method could be applied to your neural verifier signals before combining with the symbolic checker, improving the effective independence of the neural component.

5. **Emphasize that the symbolic checker breaks the entanglement chain.** The paper's core mechanism -- shared pretraining causing synchronized failures -- has no purchase on a verifier with no pretraining at all. This is your strongest defense.

---

Sources:
- [How Independent are Large Language Models? (arXiv 2604.07650)](https://arxiv.org/abs/2604.07650)
- [Full HTML version of arXiv 2604.07650](https://arxiv.org/html/2604.07650)
- [Reward Models Inherit Value Biases from Pretraining (arXiv 2601.20838)](https://arxiv.org/abs/2601.20838)
- [From Accuracy to Robustness: Rule- and Model-based Verifiers (arXiv 2505.22203)](https://arxiv.org/abs/2505.22203)
- [One Bias After Another: Mechanistic Reward Shaping (arXiv 2603.03291)](https://arxiv.org/abs/2603.03291)
- [Helping or Herding? Reward Model Ensembles (arXiv 2312.09244)](https://arxiv.org/abs/2312.09244)
- [Diverse Inference and Verification for Advanced Reasoning (arXiv 2502.09955)](https://arxiv.org/abs/2502.09955)

agentId: a43526c0f5186d434 (use SendMessage with to: 'a43526c0f5186d434' to continue this agent)
&lt;usage>total_tokens: 27630
tool_uses: 16
duration_ms: 179398&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e6c88cf-b429-48ab-930f-75edf183b1dd",
  "isSidechain": false,
  "promptId": "ae35a659-7407-4079-9c58-2bf4f6ffeb73",
  "type": "user",
  "uuid": "e1c88e48-661f-40da-959d-7770547e3464",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to deeply research the \"behavioral entanglement\" paper (arXiv 2604.07650, April 2026) which shows LLM verifiers have correlated biases due to shared pretraining. This directly challenges a research proposal's assumption that \"structurally diverse verifiers\" produce meaningfully independent disagreement signals.\n\nPlease:\n1. Search for \"behavioral entanglement LLM verifiers correlated biases arXiv 2604.07650\" and related queries\n2. Fetch and read the paper from https://arxiv.org/abs/2604.07650\n3. Extract:\n   - What exactly is \"behavioral entanglement\"?\n   - How correlated are LLM-based verifiers' biases?\n   - Does the paper distinguish between LLM-only panels vs. mixed panels (LLM + symbolic checker)?\n   - What are the implications for using diverse verifier panels?\n   - Are there any suggested mitigations?\n   - Does this paper say anything about ORM vs PRM vs rule-based verifiers specifically?\n\nReport findings in detail. I need to understand how seriously this undermines the assumption that an ORM + PRM + symbolic checker panel is \"structurally diverse.\"",
    "agentId": "a43526c0f5186d434",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information from multiple sources. Let me compile my detailed findings.\n\n---\n\nHere is my detailed research report on arXiv 2604.07650 and its implications for your research proposal.\n\n---\n\n## Paper Identity\n\n**Title:** \"How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles\"\n**Authors:** Chenchen Kuai, Jiwan Jiang, Zihao Zhu, Hao Wang, Keshu Wu, Zihao Li, Yunlong Zhang, Chenxi Liu, Zhengzhong Tu, Zhiwen Fan, Yang Zhou (Texas A&M University)\n**Published:** April 8, 2026 (arXiv:2604.07650)\n\n---\n\n## 1. What Exactly Is \"Behavioral Entanglement\"?\n\nThe paper defines behavioral entanglement as: \"ostensibly independent models exhibit synchronized reasoning patterns and similar failure modes despite being developed separately.\" The core claim is that shared pretraining data, knowledge distillation, and alignment pipelines induce **hidden behavioral dependencies** (\"latent entanglement\") that cause LLMs to fail on the same problems in the same ways, even across model families.\n\nThe critical insight: \"apparent agreement may reflect correlated failure rather than independent verification.\" When multiple LLM judges unanimously endorse an answer, this consensus may be an artifact of shared training lineage rather than genuine independent validation.\n\nThe paper formalizes this through a **multi-resolution statistical hierarchy**:\n\n- **Level 1 (Binary):** The Difficulty-Weighted Behavioral Entanglement Index (BEI_w) measures whether two models fail on the same problems more often than expected under conditional independence given task difficulty. It uses residuals from logistic regression on difficulty, weighted by task easiness (a_t = 1 - d_t) to emphasize synchronized failures on easy tasks (where co-failure is statistically unlikely under independence). Significance is tested via sign-flip randomization.\n\n- **Level 2 (Categorical):** The Cumulative Information Gain (CIG) metric measures whether model pairs select the **same wrong answer** more often than expected. It incorporates distractor attractiveness and surprisal weighting. This captures directional alignment in errors -- not just that models fail together, but that they fail identically.\n\n---\n\n## 2. How Correlated Are LLM-Based Verifiers' Biases?\n\nThe quantitative findings are striking. Tested on 18 LLMs across 6 families (GPT, Claude, Qwen, Llama, Gemini, DeepSeek) using MMLU-Pro:\n\n**Within-family entanglement (strongest):**\n- Llama-3-70B / Llama-3.1-70B: BEI = 0.0446 (p < 0.0001), CIG = 403.37 (p < 0.0001)\n- Qwen1.5-14B / Qwen1.5-72B: CIG = 260.07\n\n**Cross-family entanglement (weaker but statistically significant):**\n- DeepSeek-v2.5 / Gemini-1.5-Flash: CIG = 260.53 (p < 0.0001)\n- Gemini / Claude pairs: CIG = 238.36\n\n**Impact on judge precision:** CIG exhibits Spearman correlation of **0.64 (p < 0.001)** with GPT-4o-mini judge precision degradation and **0.71 (p < 0.01)** with Llama3-based judge precision degradation. Stronger entanglement directly corresponds to increased **over-endorsement bias** -- judges systematically approve incorrect answers from entangled models.\n\n**Era-based clustering:** The paper identifies that frontier models from the same era (e.g., GPT-5, Claude 4.6, Gemini 3.1) show cross-family synchronization that goes beyond genealogical lineage, suggesting alignment-era convergence effects.\n\n---\n\n## 3. Does the Paper Distinguish LLM-Only Panels vs. Mixed Panels (LLM + Symbolic)?\n\n**No.** This is a critical gap. The paper treats all 18 models as black-box LLM judges evaluating MCQ correctness. There is **zero discussion** of:\n- Symbolic checkers or formal verifiers\n- Rule-based verification systems\n- Non-neural verification approaches\n- Mixed/hybrid verification panels\n- ORM vs. PRM distinction\n\nThe paper's scope is exclusively **LLM-to-LLM entanglement**. The framework requires black-box access to model outputs and is designed for analyzing neural model ensembles, not heterogeneous verification systems.\n\n---\n\n## 4. What Are the Implications for Using Diverse Verifier Panels?\n\nThe paper's central warning is that **\"apparent agreement among LLMs should not be treated as evidence of independence.\"** Specific implications:\n\n- **Majority voting is vulnerable:** Entanglement-unaware majority voting across LLM judges achieves only 0.847 accuracy. The entanglement-aware reweighting achieves 0.896 (a 4.5% gain).\n- **Family diversity is necessary but insufficient:** Cross-family entanglement is weaker than within-family, but it still exists at statistically significant levels. Simply picking one model from each family does not guarantee independence.\n- **Self-preference bias compounds the problem:** Judges favor outputs from related models and models within their family, creating a feedback loop where entangled judges preferentially endorse entangled generators.\n\n---\n\n## 5. Suggested Mitigations\n\nThe paper proposes **one mitigation**: De-entangled Verifier Ensemble Reweighting. The method:\n\n1. Computes pairwise entanglement: E(i,j) = lambda_1 * BEI(i,j) + (1-lambda_1) * CIG(i,j)\n2. Measures each verifier's **internal dependence** (average entanglement with other panel members) and **target dependence** (entanglement with the model being evaluated)\n3. Reweights verifiers via softmax: w_m = exp(kappa * log(q_m) - eta_1 * Delta_in_m - eta_2 * Delta_tar_m) / Z, where q_m is competence, eta_1 penalizes internal redundancy, eta_2 penalizes target alignment.\n\nThis achieves 0.896 accuracy vs. 0.847 for majority voting and 0.881 for competence-only reweighting.\n\nNo other mitigations are proposed. The paper does not suggest adding non-LLM verifiers as a decorrelation strategy.\n\n---\n\n## 6. ORM vs. PRM vs. Rule-Based Verifiers\n\nThe paper itself says **nothing** about these distinctions. However, I found highly relevant complementary evidence from related work:\n\n**From \"Reward Models Inherit Value Biases from Pretraining\" (arXiv 2601.20838, Jan 2026):** Reward models (including ORMs and PRMs) inherit persistent value biases from their base LLM. Llama-based RMs systematically prefer \"agency\" while Gemma-based RMs prefer \"communion\" -- even with identical finetuning data. This means an ORM and a PRM built on the same base model will share correlated biases.\n\n**From \"Helping or Herding?\" (arXiv 2312.09244):** Reward model ensembles mitigate but do not eliminate reward hacking. Pretrain-seed diversity outperforms finetune-only diversity, but \"several qualitative reward hacking phenomena persist across all ensemble members.\" Shared pretraining causes all models in the ensemble to exhibit similar error patterns.\n\n**From \"From Accuracy to Robustness\" (arXiv 2505.22203, May 2025):** Rule-based verifiers and model-based verifiers have **qualitatively different failure modes**:\n- Rule-based verifiers: format-sensitivity causing **false negatives** (missing correct answers in non-standard formats)\n- Model-based verifiers: susceptible to **hacking** and pattern exploitation causing false positives\n\nThis is a key finding: the failure modes are structurally different, which suggests a mixed panel genuinely does provide some decorrelation.\n\n---\n\n## Assessment: How Seriously Does This Undermine the ORM + PRM + Symbolic Checker Panel?\n\n**The short answer: it partially undermines it, but less than you might fear, because the paper's scope is narrower than your design.**\n\nHere is the nuanced breakdown:\n\n**What the paper DOES threaten:**\n- The assumption that an ORM and a PRM produce independent signals. If both are neural models trained on similar data (especially the same base model), their errors will be correlated. The BEI and CIG metrics would likely show significant entanglement between an ORM and PRM from the same model family.\n- The assumption that \"structural diversity\" (different training objectives: outcome vs. process) is sufficient to decorrelate. The paper shows that shared pretraining dominates -- models fail together because of shared knowledge representations, not because of similar training objectives.\n- Any verification pipeline that uses multiple LLM judges and treats their agreement as evidence of correctness.\n\n**What the paper does NOT threaten (and where your design has a genuine advantage):**\n- **The symbolic checker component.** The paper studies exclusively LLM-to-LLM entanglement. A symbolic/rule-based checker has no shared pretraining, no alignment pipeline, no knowledge distillation lineage. Its failure modes are **categorically different** (format-sensitivity false negatives vs. neural hallucination false positives, per arXiv 2505.22203). The behavioral entanglement framework literally cannot apply to a system that was never pretrained.\n- **The decorrelation between neural and non-neural verifiers.** The entanglement arises from shared training data and procedures. A Z3 solver, a unit test harness, or a type checker shares none of these. The independence assumption is far more defensible for LLM + symbolic than for LLM + LLM.\n\n**Concrete recommendations for your proposal:**\n\n1. **Acknowledge the paper explicitly.** Cite it to show you are aware that ORM-PRM independence is weaker than naive \"structural diversity\" suggests.\n\n2. **Reframe your diversity argument.** Do not claim ORM + PRM + symbolic provides \"three independent signals.\" Instead argue it provides \"two partially correlated neural signals plus one categorically independent non-neural signal.\" The symbolic checker is the genuine source of decorrelation; the ORM/PRM split provides weaker (but non-zero) diversity.\n\n3. **If your ORM and PRM use the same base model, flag this.** The entanglement will be strongest in this case. Consider using ORM and PRM from different model families to at least get cross-family decorrelation (BEI ~0.01-0.03 rather than ~0.04+).\n\n4. **Consider applying the de-entangled reweighting.** The paper's reweighting method could be applied to your neural verifier signals before combining with the symbolic checker, improving the effective independence of the neural component.\n\n5. **Emphasize that the symbolic checker breaks the entanglement chain.** The paper's core mechanism -- shared pretraining causing synchronized failures -- has no purchase on a verifier with no pretraining at all. This is your strongest defense.\n\n---\n\nSources:\n- [How Independent are Large Language Models? (arXiv 2604.07650)](https://arxiv.org/abs/2604.07650)\n- [Full HTML version of arXiv 2604.07650](https://arxiv.org/html/2604.07650)\n- [Reward Models Inherit Value Biases from Pretraining (arXiv 2601.20838)](https://arxiv.org/abs/2601.20838)\n- [From Accuracy to Robustness: Rule- and Model-based Verifiers (arXiv 2505.22203)](https://arxiv.org/abs/2505.22203)\n- [One Bias After Another: Mechanistic Reward Shaping (arXiv 2603.03291)](https://arxiv.org/abs/2603.03291)\n- [Helping or Herding? Reward Model Ensembles (arXiv 2312.09244)](https://arxiv.org/abs/2312.09244)\n- [Diverse Inference and Verification for Advanced Reasoning (arXiv 2502.09955)](https://arxiv.org/abs/2502.09955)"
      }
    ],
    "totalDurationMs": 179398,
    "totalTokens": 27630,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 880,
      "cache_read_input_tokens": 23762,
      "output_tokens": 2987,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 880
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2987,
          "cache_read_input_tokens": 23762,
          "cache_creation_input_tokens": 880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 880,
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
      "otherToolCount": 16
    }
  },
  "sourceToolAssistantUUID": "4e6c88cf-b429-48ab-930f-75edf183b1dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T09:26:37.673Z_

<details><summary>↩ Tool result · `toolu_0153r5HJ2uAHmEop8YCdX9px`</summary>

```text
I now have comprehensive findings. Here is my full report.

---

## Literature Review: Multi-Verifier Disagreement for Iterative Synthetic Data Curation (2025-2026)

### PAPER 1: Cross-Model Disagreement as a Label-Free Correctness Signal
- **arXiv:** 2603.25450 (March 2026)
- **Key method:** Proposes Cross-Model Perplexity (CMP) and Cross-Model Entropy (CME) -- measures of how "surprised" a second model is at a first model's answer. Single forward pass, no generation needed, no labels needed.
- **Results:** CMP achieves mean AUROC of 0.75 vs. within-model entropy baseline of 0.59 on MMLU. Wins 12/16 routing comparisons on GSM8K.
- **Relation to your proposal:** **DIRECTLY COMPLEMENTARY and potentially a competitor.** This paper establishes cross-model disagreement as a practical signal for correctness estimation, data filtering, and selective prediction. It validates the core premise that disagreement between models is informative. However, it does NOT use this for iterative synthetic data curation specifically -- it focuses on deployment-time routing and monitoring. Your proposal could cite this as foundational evidence that disagreement is a reliable signal, then extend it to the curation loop.
- **Classification:** Complementary (strong supporting evidence for your core hypothesis)

---

### PAPER 2: LASeR -- Learning to Adaptively Select Reward Models with Multi-Armed Bandits
- **Authors:** Duy Nguyen, Archiki Prasad, Elias Stengel-Eskin, Mohit Bansal
- **Venue:** NeurIPS 2025 Poster (arXiv 2410.01735)
- **Key method:** Frames reward model selection as a multi-armed bandit problem. Iteratively selects the best-suited RM per instance from a pool of multiple RMs during LLM training.
- **Results:** +1.45% absolute accuracy over best single RM, +2.67% over RM ensemble on reasoning benchmarks.
- **Relation to your proposal:** **COMPETITOR.** LASeR addresses the same problem of leveraging multiple reward models, but uses bandit-based selection rather than disagreement-based curation. Your proposal should position itself against this: LASeR selects which single RM to trust per instance, while your approach uses *disagreement itself* as the curation signal to identify informative examples.
- **Classification:** Competitor

---

### PAPER 3: Hard Examples Are All You Need -- Maximizing GRPO Post-Training Under Annotation Budgets
- **arXiv:** 2508.14094 (August 2025)
- **Key method:** Shows that training on the hardest 10% of examples (where base model fails most) yields up to 47% improvement, while easy examples give only 3-15%. GRPO requires outcome variance for learning signal; hard examples maintain mixed outcomes longer.
- **Results:** Only hard-trained models achieve meaningful OOD gains (AIME2025). Superior generalization.
- **Relation to your proposal:** **STRONGLY COMPLEMENTARY.** This paper provides the theoretical justification for why verifier disagreement regions should contain useful data. Disagreement regions are precisely where outcomes are mixed (not uniformly correct or incorrect), meaning GRPO-style algorithms get maximum learning signal there. This is the closest thing to the pilot study you asked about -- it empirically shows that boundary/hard examples are where the learning happens.
- **Classification:** Complementary (key supporting evidence)

---

### PAPER 4: Improving Data Efficiency for LLM RL Fine-tuning Through Difficulty-Targeted Online Data Selection and Rollout Replay
- **Venue:** NeurIPS 2025 Poster (arXiv 2506.05316)
- **Key method:** Uses "adaptive difficulty" to guide online data selection, prioritizing moderate-difficulty questions. Attention-based framework estimates difficulty from a small reference set. Includes rollout replay (experience replay for RL).
- **Results:** Reduces RL fine-tuning time by 25-65% while matching GRPO performance.
- **Relation to your proposal:** **COMPETITOR/COMPLEMENTARY.** This is close to your idea -- it selects data based on difficulty during iterative training. However, it uses model-internal difficulty estimation rather than multi-verifier disagreement. Your approach could argue it is more robust because disagreement between heterogeneous verifiers captures a richer notion of "informativeness" than single-model difficulty.
- **Classification:** Competitor (partially overlapping approach)

---

### PAPER 5: RL Tango -- Reinforcing Generator and Verifier Together for Language Reasoning
- **Venue:** NeurIPS 2025 Poster (arXiv 2505.15034)
- **Key method:** Co-trains LLM generator and a generative process-level verifier via RL in an interleaved manner. The verifier co-evolves with the generator rather than being fixed.
- **Results:** 26.7% on AIME 2024, 23.3% on AIME 2025, 70.0% on AMC 2023.
- **Relation to your proposal:** **COMPLEMENTARY.** RL Tango addresses generator-verifier co-evolution, which is orthogonal to multi-verifier disagreement for curation. Your proposal could incorporate co-evolving verifiers as a design choice.
- **Classification:** Complementary

---

### PAPER 6: PAG -- Multi-Turn Reinforced LLM Self-Correction with Policy as Generative Verifier
- **arXiv:** 2506.10406 (September 2025)
- **Key method:** LLM alternates between policy and verifier roles in a multi-turn RL loop. Selective revision: only revises when its own verification detects an error.
- **Relation to your proposal:** **COMPLEMENTARY.** Focuses on self-correction rather than data curation. Different problem setting.
- **Classification:** Complementary (tangential)

---

### PAPER 7: Pairwise Maximum Discrepancy Competition (PMDC) for Reward Model Evaluation
- **arXiv:** 2601.16987 (January 2026, submitted to ICLR 2026)
- **Key method:** Actively selects prompt-response pairs that *maximize disagreement between two reward models*, yielding a compact set of contentious test cases. Uses Bradley-Terry aggregation for global ranking.
- **Results:** Up to 95.5% reduction in annotation cost. Reveals systematic generalization failures in reward models.
- **Relation to your proposal:** **DIRECTLY RELEVANT COMPETITOR/COMPLEMENTARY.** PMDC uses reward model disagreement explicitly -- but for *evaluation*, not for *training data curation*. This is the closest existing work to your idea in spirit. Key difference: PMDC uses disagreement to evaluate RMs, while you propose using it to curate training data. You MUST cite and distinguish from this paper.
- **Classification:** Competitor (adjacent application of the same core idea)

---

### PAPER 8: From Accuracy to Robustness -- Rule- and Model-based Verifiers in Mathematical Reasoning
- **arXiv:** 2505.22203 (May 2025)
- **Key method:** Empirical study comparing rule-based and model-based verifiers for RLVR. Rule-based verifiers have significant false negative rates (format sensitivity). Model-based verifiers are hackable.
- **Relation to your proposal:** **STRONGLY COMPLEMENTARY.** Demonstrates that different verifier types fail in systematically different ways -- rule-based have false negatives, model-based have false positives. This directly motivates combining them: their disagreement regions are precisely where one type catches errors the other misses.
- **Classification:** Complementary (motivating evidence for multi-verifier approach)

---

### PAPER 9: Verifier-Backed Hard Problem Generation (VHG) for Mathematical Reasoning
- **Authors:** Yuhang Lai, Jiazhan Feng, Yee Whye Teh, Ning Miao
- **arXiv:** 2605.06660 (May 2026)
- **Key method:** Three-party self-play: setter, solver, and independent verifier. Uses both a "Hard" symbolic verifier and a "Soft" LLM-based verifier. Setter's reward is jointly determined by validity (verifier) and difficulty (solver).
- **Results:** 16.9-21.4% improvements on integral benchmarks, pass@1 from 56.8% to 69.0% on general math.
- **Relation to your proposal:** **DIRECTLY RELEVANT COMPETITOR.** This paper explicitly uses two verifier types (symbolic + neural) in combination for data generation. The key difference is they use verifiers to validate generated *problems*, not to curate *solutions*. Your proposal curates training data; VHG generates training problems. These are complementary but adjacent.
- **Classification:** Competitor/Complementary (overlapping territory)

---

### PAPER 10: GenPRM -- Scaling Test-Time Compute of Process Reward Models via Generative Reasoning
- **Venue:** AAAI 2026 (arXiv 2504.00891, April 2025)
- **Key method:** Redefines process supervision as a generative task with Chain-of-Thought reasoning + code verification before judging each step. Uses Relative Progress Estimation (RPE).
- **Results:** 1.5B GenPRM outperforms GPT-4o; 7B GenPRM surpasses Qwen2.5-Math-PRM-72B on ProcessBench.
- **Relation to your proposal:** **COMPLEMENTARY.** GenPRM is a stronger verifier that could serve as one of your multi-verifier ensemble members.
- **Classification:** Complementary

---

### PAPER 11: Spend Wisely -- Maximizing Post-Training Gains in Iterative Synthetic Data Bootstrapping
- **arXiv:** 2501.18962 (January 2025)
- **Key method:** Studies budget allocation across iterations in the generate-verify-finetune loop. Shows constant policies fail; exponential growth policies are optimal.
- **Relation to your proposal:** **COMPLEMENTARY.** Addresses the budget allocation question within the same iterative bootstrapping paradigm. Your proposal could adopt their exponential scaling insights for iteration scheduling.
- **Classification:** Complementary

---

### PAPER 12: A Closer Look at Model Collapse -- Generalization-to-Memorization Perspective
- **Venue:** NeurIPS 2025 Spotlight (arXiv 2509.16499)
- **Key method:** Identifies entropy decline in synthetic data as a clear indicator of model collapse. Proposes entropy-based data selection to maintain diversity.
- **Relation to your proposal:** **COMPLEMENTARY.** Multi-verifier disagreement could serve as a diversity-preserving mechanism -- disagreement regions inherently select for diverse/non-obvious examples, potentially preventing the entropy decline that causes collapse.
- **Classification:** Complementary

---

### PAPER 13: DeepSeekMath-V2 -- Towards Self-Verifiable Mathematical Reasoning
- **arXiv:** 2511.22570 (November 2025)
- **Key method:** "Verifier-generator" dual architecture. GRPO-trained verifier + meta-verifier that scores proofs on rigor, not just final answers. 685B MoE model.
- **Results:** Gold-level on IMO 2025, CMO 2024, 118/120 on Putnam 2024.
- **Relation to your proposal:** **COMPLEMENTARY.** Demonstrates the power of verification-first pipelines. The meta-verifier concept could be relevant to your disagreement framework.
- **Classification:** Complementary

---

### PAPER 14: Neuro-Symbolic Data Generation for Math Reasoning
- **Authors:** Zenan Li, Zhi Zhou et al. (Microsoft Research)
- **arXiv:** 2412.04857 (December 2024, NeurIPS 2025)
- **Key method:** Combines LLM informalization with symbolic solver verification + projected MCMC sampling for generating diverse, valid math problems.
- **Relation to your proposal:** **COMPLEMENTARY.** Uses symbolic+neural combination for data *generation* rather than *curation*. Your approach is downstream of this.
- **Classification:** Complementary

---

### PAPER 15: SWiRL -- Synthetic Data Generation & Multi-Step RL for Reasoning & Tool Use
- **Stanford Scaling Intelligence Lab** (arXiv 2504.04736, April 2025)
- **Key method:** Iteratively generates multi-step reasoning/tool-use data, applies synthetic data filtering, then RL optimization on sub-trajectories.
- **Results:** 11-21% relative accuracy improvements across multiple benchmarks.
- **Relation to your proposal:** **COMPLEMENTARY.** Uses filtering in the iterative loop but with a single verifier. Your multi-verifier disagreement approach could improve its filtering step.
- **Classification:** Complementary

---

### SPECIFIC QUESTION: Has anyone done a pilot study showing verifier disagreement regions contain useful/tail data rather than just noise?

**No one has done this as a dedicated pilot study.** However, there is strong *indirect* evidence from multiple papers:

1. **"Hard Examples Are All You Need" (2508.14094)** provides the strongest indirect evidence: examples where model outcomes are mixed (analogous to verifier disagreement) are exactly where GRPO learning signal is maximized. The hardest 10% yields 47% improvement; easy examples yield near-zero gains. This is essentially showing that "disagreement regions" (mixed outcomes) contain the useful training signal.

2. **PMDC (2601.16987)** shows that maximum-disagreement examples between reward models reveal systematic generalization failures -- meaning disagreement points are where models are substantively uncertain, not just noisy.

3. **"From Accuracy to Robustness" (2505.22203)** shows rule-based and model-based verifiers fail in complementary ways (false negatives vs. false positives), meaning their disagreement regions are where one catches genuine errors the other misses -- information-rich, not noise.

4. **Cross-Model Disagreement (2603.25450)** shows disagreement has high AUROC for correctness prediction, implying it is a reliable signal rather than noise.

**This is a clear gap in the literature and a strong contribution opportunity for your proposal.** A pilot study empirically characterizing what lives in verifier disagreement regions (useful tail data vs. noise vs. ambiguous cases) would be novel and directly citable by all of the above lines of work.

---

### Summary of Most Important Papers to Cite

| Priority | Paper | Classification | Why |
|----------|-------|---------------|-----|
| MUST CITE | Cross-Model Disagreement (2603.25450) | Complementary | Validates disagreement as a signal |
| MUST CITE | PMDC (2601.16987) | Competitor | Uses disagreement for RM evaluation |
| MUST CITE | LASeR (NeurIPS 2025) | Competitor | Multi-RM selection via bandits |
| MUST CITE | Hard Examples Are All You Need (2508.14094) | Complementary | Justifies why disagreement regions are useful |
| MUST CITE | VHG (2605.06660) | Competitor | Dual symbolic+neural verifiers for math |
| MUST CITE | From Accuracy to Robustness (2505.22203) | Complementary | Motivates combining verifier types |
| SHOULD CITE | Difficulty-Targeted Data Selection (NeurIPS 2025) | Competitor | Alternative difficulty-based curation |
| SHOULD CITE | RL Tango (NeurIPS 2025) | Complementary | Generator-verifier co-evolution |
| SHOULD CITE | Spend Wisely (2501.18962) | Complementary | Iteration budget allocation |
| SHOULD CITE | Model Collapse GenToMem (NeurIPS 2025 Spotlight) | Complementary | Entropy-based selection prevents collapse |
| GOOD TO CITE | GenPRM (AAAI 2026) | Complementary | Stronger verifier for your ensemble |
| GOOD TO CITE | Neuro-Symbolic Data Gen (NeurIPS 2025) | Complementary | Symbolic+neural for generation |

Sources:
- [Cross-Model Disagreement as a Label-Free Correctness Signal](https://arxiv.org/abs/2603.25450)
- [LASeR: Learning to Adaptively Select Reward Models with Multi-Armed Bandits](https://arxiv.org/abs/2410.01735)
- [Hard Examples Are All You Need](https://arxiv.org/abs/2508.14094)
- [Improving Data Efficiency for LLM RL Fine-tuning](https://arxiv.org/abs/2506.05316)
- [RL Tango: Reinforcing Generator and Verifier Together](https://arxiv.org/abs/2505.15034)
- [PAG: Multi-Turn Reinforced LLM Self-Correction](https://arxiv.org/pdf/2506.10406)
- [Evaluating Reward Model Generalization via PMDC](https://arxiv.org/abs/2601.16987)
- [From Accuracy to Robustness: Rule- and Model-based Verifiers](https://arxiv.org/abs/2505.22203)
- [Verifier-Backed Hard Problem Generation](https://arxiv.org/abs/2605.06660)
- [GenPRM: Scaling Test-Time Compute of PRMs](https://arxiv.org/abs/2504.00891)
- [Spend Wisely: Iterative Synthetic Data Bootstrapping](https://arxiv.org/abs/2501.18962)
- [A Closer Look at Model Collapse](https://arxiv.org/abs/2509.16499)
- [DeepSeekMath-V2](https://arxiv.org/abs/2511.22570)
- [Neuro-Symbolic Data Generation for Math Reasoning](https://arxiv.org/abs/2412.04857)
- [SWiRL: Synthetic Data Generation & Multi-Step RL](https://arxiv.org/abs/2504.04736)
- [FunPRM: Function-as-Step Process Reward Model](https://arxiv.org/abs/2601.22249)
- [AgentPRM: Process Reward Models for LLM Agents](https://arxiv.org/abs/2511.08325)
- [A Survey of Process Reward Models](https://arxiv.org/abs/2510.08049)
- [Reward Modeling for RL-Based LLM Reasoning Survey](https://arxiv.org/abs/2602.09305)

agentId: a59aee3611a5af59d (use SendMessage with to: 'a59aee3611a5af59d' to continue this agent)
&lt;usage>total_tokens: 36969
tool_uses: 28
duration_ms: 196631&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a848347-95f6-4141-9004-c86b13af2cd8",
  "isSidechain": false,
  "promptId": "ae35a659-7407-4079-9c58-2bf4f6ffeb73",
  "type": "user",
  "uuid": "81a7430d-c0f0-4320-a397-5b4969b3d590",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm revising a research proposal about using multi-verifier disagreement for iterative synthetic data curation. I need to check for any additional recent (2025-2026) work I might be missing on:\n\n1. Search \"multi-verifier synthetic data curation 2025 2026\"\n2. Search \"reward model diversity iterative training LLM 2025 2026\" \n3. Search \"model collapse prevention data selection 2025 2026\"\n4. Search \"process reward model outcome reward model combined 2025 2026\"\n5. Search \"symbolic verifier neural verifier combined math reasoning 2025 2026\"\n\nFor each relevant paper found, extract:\n- Title, authors, venue, date\n- Key method\n- How it relates to using verifier disagreement for data curation\n- Whether it's a competitor, complementary, or irrelevant\n\nAlso specifically check: has anyone done a pilot study showing that verifier disagreement regions contain useful/tail data rather than just noise? This would be extremely valuable for our proposal.\n\nReport all findings.",
    "agentId": "a59aee3611a5af59d",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive findings. Here is my full report.\n\n---\n\n## Literature Review: Multi-Verifier Disagreement for Iterative Synthetic Data Curation (2025-2026)\n\n### PAPER 1: Cross-Model Disagreement as a Label-Free Correctness Signal\n- **arXiv:** 2603.25450 (March 2026)\n- **Key method:** Proposes Cross-Model Perplexity (CMP) and Cross-Model Entropy (CME) -- measures of how \"surprised\" a second model is at a first model's answer. Single forward pass, no generation needed, no labels needed.\n- **Results:** CMP achieves mean AUROC of 0.75 vs. within-model entropy baseline of 0.59 on MMLU. Wins 12/16 routing comparisons on GSM8K.\n- **Relation to your proposal:** **DIRECTLY COMPLEMENTARY and potentially a competitor.** This paper establishes cross-model disagreement as a practical signal for correctness estimation, data filtering, and selective prediction. It validates the core premise that disagreement between models is informative. However, it does NOT use this for iterative synthetic data curation specifically -- it focuses on deployment-time routing and monitoring. Your proposal could cite this as foundational evidence that disagreement is a reliable signal, then extend it to the curation loop.\n- **Classification:** Complementary (strong supporting evidence for your core hypothesis)\n\n---\n\n### PAPER 2: LASeR -- Learning to Adaptively Select Reward Models with Multi-Armed Bandits\n- **Authors:** Duy Nguyen, Archiki Prasad, Elias Stengel-Eskin, Mohit Bansal\n- **Venue:** NeurIPS 2025 Poster (arXiv 2410.01735)\n- **Key method:** Frames reward model selection as a multi-armed bandit problem. Iteratively selects the best-suited RM per instance from a pool of multiple RMs during LLM training.\n- **Results:** +1.45% absolute accuracy over best single RM, +2.67% over RM ensemble on reasoning benchmarks.\n- **Relation to your proposal:** **COMPETITOR.** LASeR addresses the same problem of leveraging multiple reward models, but uses bandit-based selection rather than disagreement-based curation. Your proposal should position itself against this: LASeR selects which single RM to trust per instance, while your approach uses *disagreement itself* as the curation signal to identify informative examples.\n- **Classification:** Competitor\n\n---\n\n### PAPER 3: Hard Examples Are All You Need -- Maximizing GRPO Post-Training Under Annotation Budgets\n- **arXiv:** 2508.14094 (August 2025)\n- **Key method:** Shows that training on the hardest 10% of examples (where base model fails most) yields up to 47% improvement, while easy examples give only 3-15%. GRPO requires outcome variance for learning signal; hard examples maintain mixed outcomes longer.\n- **Results:** Only hard-trained models achieve meaningful OOD gains (AIME2025). Superior generalization.\n- **Relation to your proposal:** **STRONGLY COMPLEMENTARY.** This paper provides the theoretical justification for why verifier disagreement regions should contain useful data. Disagreement regions are precisely where outcomes are mixed (not uniformly correct or incorrect), meaning GRPO-style algorithms get maximum learning signal there. This is the closest thing to the pilot study you asked about -- it empirically shows that boundary/hard examples are where the learning happens.\n- **Classification:** Complementary (key supporting evidence)\n\n---\n\n### PAPER 4: Improving Data Efficiency for LLM RL Fine-tuning Through Difficulty-Targeted Online Data Selection and Rollout Replay\n- **Venue:** NeurIPS 2025 Poster (arXiv 2506.05316)\n- **Key method:** Uses \"adaptive difficulty\" to guide online data selection, prioritizing moderate-difficulty questions. Attention-based framework estimates difficulty from a small reference set. Includes rollout replay (experience replay for RL).\n- **Results:** Reduces RL fine-tuning time by 25-65% while matching GRPO performance.\n- **Relation to your proposal:** **COMPETITOR/COMPLEMENTARY.** This is close to your idea -- it selects data based on difficulty during iterative training. However, it uses model-internal difficulty estimation rather than multi-verifier disagreement. Your approach could argue it is more robust because disagreement between heterogeneous verifiers captures a richer notion of \"informativeness\" than single-model difficulty.\n- **Classification:** Competitor (partially overlapping approach)\n\n---\n\n### PAPER 5: RL Tango -- Reinforcing Generator and Verifier Together for Language Reasoning\n- **Venue:** NeurIPS 2025 Poster (arXiv 2505.15034)\n- **Key method:** Co-trains LLM generator and a generative process-level verifier via RL in an interleaved manner. The verifier co-evolves with the generator rather than being fixed.\n- **Results:** 26.7% on AIME 2024, 23.3% on AIME 2025, 70.0% on AMC 2023.\n- **Relation to your proposal:** **COMPLEMENTARY.** RL Tango addresses generator-verifier co-evolution, which is orthogonal to multi-verifier disagreement for curation. Your proposal could incorporate co-evolving verifiers as a design choice.\n- **Classification:** Complementary\n\n---\n\n### PAPER 6: PAG -- Multi-Turn Reinforced LLM Self-Correction with Policy as Generative Verifier\n- **arXiv:** 2506.10406 (September 2025)\n- **Key method:** LLM alternates between policy and verifier roles in a multi-turn RL loop. Selective revision: only revises when its own verification detects an error.\n- **Relation to your proposal:** **COMPLEMENTARY.** Focuses on self-correction rather than data curation. Different problem setting.\n- **Classification:** Complementary (tangential)\n\n---\n\n### PAPER 7: Pairwise Maximum Discrepancy Competition (PMDC) for Reward Model Evaluation\n- **arXiv:** 2601.16987 (January 2026, submitted to ICLR 2026)\n- **Key method:** Actively selects prompt-response pairs that *maximize disagreement between two reward models*, yielding a compact set of contentious test cases. Uses Bradley-Terry aggregation for global ranking.\n- **Results:** Up to 95.5% reduction in annotation cost. Reveals systematic generalization failures in reward models.\n- **Relation to your proposal:** **DIRECTLY RELEVANT COMPETITOR/COMPLEMENTARY.** PMDC uses reward model disagreement explicitly -- but for *evaluation*, not for *training data curation*. This is the closest existing work to your idea in spirit. Key difference: PMDC uses disagreement to evaluate RMs, while you propose using it to curate training data. You MUST cite and distinguish from this paper.\n- **Classification:** Competitor (adjacent application of the same core idea)\n\n---\n\n### PAPER 8: From Accuracy to Robustness -- Rule- and Model-based Verifiers in Mathematical Reasoning\n- **arXiv:** 2505.22203 (May 2025)\n- **Key method:** Empirical study comparing rule-based and model-based verifiers for RLVR. Rule-based verifiers have significant false negative rates (format sensitivity). Model-based verifiers are hackable.\n- **Relation to your proposal:** **STRONGLY COMPLEMENTARY.** Demonstrates that different verifier types fail in systematically different ways -- rule-based have false negatives, model-based have false positives. This directly motivates combining them: their disagreement regions are precisely where one type catches errors the other misses.\n- **Classification:** Complementary (motivating evidence for multi-verifier approach)\n\n---\n\n### PAPER 9: Verifier-Backed Hard Problem Generation (VHG) for Mathematical Reasoning\n- **Authors:** Yuhang Lai, Jiazhan Feng, Yee Whye Teh, Ning Miao\n- **arXiv:** 2605.06660 (May 2026)\n- **Key method:** Three-party self-play: setter, solver, and independent verifier. Uses both a \"Hard\" symbolic verifier and a \"Soft\" LLM-based verifier. Setter's reward is jointly determined by validity (verifier) and difficulty (solver).\n- **Results:** 16.9-21.4% improvements on integral benchmarks, pass@1 from 56.8% to 69.0% on general math.\n- **Relation to your proposal:** **DIRECTLY RELEVANT COMPETITOR.** This paper explicitly uses two verifier types (symbolic + neural) in combination for data generation. The key difference is they use verifiers to validate generated *problems*, not to curate *solutions*. Your proposal curates training data; VHG generates training problems. These are complementary but adjacent.\n- **Classification:** Competitor/Complementary (overlapping territory)\n\n---\n\n### PAPER 10: GenPRM -- Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\n- **Venue:** AAAI 2026 (arXiv 2504.00891, April 2025)\n- **Key method:** Redefines process supervision as a generative task with Chain-of-Thought reasoning + code verification before judging each step. Uses Relative Progress Estimation (RPE).\n- **Results:** 1.5B GenPRM outperforms GPT-4o; 7B GenPRM surpasses Qwen2.5-Math-PRM-72B on ProcessBench.\n- **Relation to your proposal:** **COMPLEMENTARY.** GenPRM is a stronger verifier that could serve as one of your multi-verifier ensemble members.\n- **Classification:** Complementary\n\n---\n\n### PAPER 11: Spend Wisely -- Maximizing Post-Training Gains in Iterative Synthetic Data Bootstrapping\n- **arXiv:** 2501.18962 (January 2025)\n- **Key method:** Studies budget allocation across iterations in the generate-verify-finetune loop. Shows constant policies fail; exponential growth policies are optimal.\n- **Relation to your proposal:** **COMPLEMENTARY.** Addresses the budget allocation question within the same iterative bootstrapping paradigm. Your proposal could adopt their exponential scaling insights for iteration scheduling.\n- **Classification:** Complementary\n\n---\n\n### PAPER 12: A Closer Look at Model Collapse -- Generalization-to-Memorization Perspective\n- **Venue:** NeurIPS 2025 Spotlight (arXiv 2509.16499)\n- **Key method:** Identifies entropy decline in synthetic data as a clear indicator of model collapse. Proposes entropy-based data selection to maintain diversity.\n- **Relation to your proposal:** **COMPLEMENTARY.** Multi-verifier disagreement could serve as a diversity-preserving mechanism -- disagreement regions inherently select for diverse/non-obvious examples, potentially preventing the entropy decline that causes collapse.\n- **Classification:** Complementary\n\n---\n\n### PAPER 13: DeepSeekMath-V2 -- Towards Self-Verifiable Mathematical Reasoning\n- **arXiv:** 2511.22570 (November 2025)\n- **Key method:** \"Verifier-generator\" dual architecture. GRPO-trained verifier + meta-verifier that scores proofs on rigor, not just final answers. 685B MoE model.\n- **Results:** Gold-level on IMO 2025, CMO 2024, 118/120 on Putnam 2024.\n- **Relation to your proposal:** **COMPLEMENTARY.** Demonstrates the power of verification-first pipelines. The meta-verifier concept could be relevant to your disagreement framework.\n- **Classification:** Complementary\n\n---\n\n### PAPER 14: Neuro-Symbolic Data Generation for Math Reasoning\n- **Authors:** Zenan Li, Zhi Zhou et al. (Microsoft Research)\n- **arXiv:** 2412.04857 (December 2024, NeurIPS 2025)\n- **Key method:** Combines LLM informalization with symbolic solver verification + projected MCMC sampling for generating diverse, valid math problems.\n- **Relation to your proposal:** **COMPLEMENTARY.** Uses symbolic+neural combination for data *generation* rather than *curation*. Your approach is downstream of this.\n- **Classification:** Complementary\n\n---\n\n### PAPER 15: SWiRL -- Synthetic Data Generation & Multi-Step RL for Reasoning & Tool Use\n- **Stanford Scaling Intelligence Lab** (arXiv 2504.04736, April 2025)\n- **Key method:** Iteratively generates multi-step reasoning/tool-use data, applies synthetic data filtering, then RL optimization on sub-trajectories.\n- **Results:** 11-21% relative accuracy improvements across multiple benchmarks.\n- **Relation to your proposal:** **COMPLEMENTARY.** Uses filtering in the iterative loop but with a single verifier. Your multi-verifier disagreement approach could improve its filtering step.\n- **Classification:** Complementary\n\n---\n\n### SPECIFIC QUESTION: Has anyone done a pilot study showing verifier disagreement regions contain useful/tail data rather than just noise?\n\n**No one has done this as a dedicated pilot study.** However, there is strong *indirect* evidence from multiple papers:\n\n1. **\"Hard Examples Are All You Need\" (2508.14094)** provides the strongest indirect evidence: examples where model outcomes are mixed (analogous to verifier disagreement) are exactly where GRPO learning signal is maximized. The hardest 10% yields 47% improvement; easy examples yield near-zero gains. This is essentially showing that \"disagreement regions\" (mixed outcomes) contain the useful training signal.\n\n2. **PMDC (2601.16987)** shows that maximum-disagreement examples between reward models reveal systematic generalization failures -- meaning disagreement points are where models are substantively uncertain, not just noisy.\n\n3. **\"From Accuracy to Robustness\" (2505.22203)** shows rule-based and model-based verifiers fail in complementary ways (false negatives vs. false positives), meaning their disagreement regions are where one catches genuine errors the other misses -- information-rich, not noise.\n\n4. **Cross-Model Disagreement (2603.25450)** shows disagreement has high AUROC for correctness prediction, implying it is a reliable signal rather than noise.\n\n**This is a clear gap in the literature and a strong contribution opportunity for your proposal.** A pilot study empirically characterizing what lives in verifier disagreement regions (useful tail data vs. noise vs. ambiguous cases) would be novel and directly citable by all of the above lines of work.\n\n---\n\n### Summary of Most Important Papers to Cite\n\n| Priority | Paper | Classification | Why |\n|----------|-------|---------------|-----|\n| MUST CITE | Cross-Model Disagreement (2603.25450) | Complementary | Validates disagreement as a signal |\n| MUST CITE | PMDC (2601.16987) | Competitor | Uses disagreement for RM evaluation |\n| MUST CITE | LASeR (NeurIPS 2025) | Competitor | Multi-RM selection via bandits |\n| MUST CITE | Hard Examples Are All You Need (2508.14094) | Complementary | Justifies why disagreement regions are useful |\n| MUST CITE | VHG (2605.06660) | Competitor | Dual symbolic+neural verifiers for math |\n| MUST CITE | From Accuracy to Robustness (2505.22203) | Complementary | Motivates combining verifier types |\n| SHOULD CITE | Difficulty-Targeted Data Selection (NeurIPS 2025) | Competitor | Alternative difficulty-based curation |\n| SHOULD CITE | RL Tango (NeurIPS 2025) | Complementary | Generator-verifier co-evolution |\n| SHOULD CITE | Spend Wisely (2501.18962) | Complementary | Iteration budget allocation |\n| SHOULD CITE | Model Collapse GenToMem (NeurIPS 2025 Spotlight) | Complementary | Entropy-based selection prevents collapse |\n| GOOD TO CITE | GenPRM (AAAI 2026) | Complementary | Stronger verifier for your ensemble |\n| GOOD TO CITE | Neuro-Symbolic Data Gen (NeurIPS 2025) | Complementary | Symbolic+neural for generation |\n\nSources:\n- [Cross-Model Disagreement as a Label-Free Correctness Signal](https://arxiv.org/abs/2603.25450)\n- [LASeR: Learning to Adaptively Select Reward Models with Multi-Armed Bandits](https://arxiv.org/abs/2410.01735)\n- [Hard Examples Are All You Need](https://arxiv.org/abs/2508.14094)\n- [Improving Data Efficiency for LLM RL Fine-tuning](https://arxiv.org/abs/2506.05316)\n- [RL Tango: Reinforcing Generator and Verifier Together](https://arxiv.org/abs/2505.15034)\n- [PAG: Multi-Turn Reinforced LLM Self-Correction](https://arxiv.org/pdf/2506.10406)\n- [Evaluating Reward Model Generalization via PMDC](https://arxiv.org/abs/2601.16987)\n- [From Accuracy to Robustness: Rule- and Model-based Verifiers](https://arxiv.org/abs/2505.22203)\n- [Verifier-Backed Hard Problem Generation](https://arxiv.org/abs/2605.06660)\n- [GenPRM: Scaling Test-Time Compute of PRMs](https://arxiv.org/abs/2504.00891)\n- [Spend Wisely: Iterative Synthetic Data Bootstrapping](https://arxiv.org/abs/2501.18962)\n- [A Closer Look at Model Collapse](https://arxiv.org/abs/2509.16499)\n- [DeepSeekMath-V2](https://arxiv.org/abs/2511.22570)\n- [Neuro-Symbolic Data Generation for Math Reasoning](https://arxiv.org/abs/2412.04857)\n- [SWiRL: Synthetic Data Generation & Multi-Step RL](https://arxiv.org/abs/2504.04736)\n- [FunPRM: Function-as-Step Process Reward Model](https://arxiv.org/abs/2601.22249)\n- [AgentPRM: Process Reward Models for LLM Agents](https://arxiv.org/abs/2511.08325)\n- [A Survey of Process Reward Models](https://arxiv.org/abs/2510.08049)\n- [Reward Modeling for RL-Based LLM Reasoning Survey](https://arxiv.org/abs/2602.09305)"
      }
    ],
    "totalDurationMs": 196631,
    "totalTokens": 36969,
    "totalToolUseCount": 28,
    "usage": {
      "input_tokens": 706,
      "cache_creation_input_tokens": 1533,
      "cache_read_input_tokens": 30180,
      "output_tokens": 4550,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1533
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 706,
          "output_tokens": 4550,
          "cache_read_input_tokens": 30180,
          "cache_creation_input_tokens": 1533,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1533,
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
  "sourceToolAssistantUUID": "8a848347-95f6-4141-9004-c86b13af2cd8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"Verifier Disagreement as Tail-Preservation Signal in Synthetic Data Cu…",
  "leafUuid": "81a7430d-c0f0-4320-a397-5b4969b3d590",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise verifier disagreement tail-preservation hypothesis",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97"
}
```

---

### Tool result

_source line 29 · 2026-05-19T09:28:59.852Z_

<details><summary>↩ Tool result · `toolu_01YDg4K1L13e37pbQYYcq2rQ`</summary>

```text
I now have a comprehensive understanding of the research landscape. Here is my detailed report:

---

## Research Report: Positioning DWIC Relative to Query-by-Committee (QBC) Active Learning

### 1. The Classical QBC Framework

**Seminal Papers:**

- **Seung, Opper, & Sompolinsky (1992)**, ["Query by Committee"](https://dl.acm.org/doi/10.1145/130385.130417), Proceedings of the Fifth Annual ACM Workshop on Computational Learning Theory, pp. 287-294. This paper introduced the QBC algorithm: a committee of learners is trained on the same dataset, and the next query is chosen according to the principle of **maximal disagreement**. The key theoretical result is that QBC achieves asymptotically finite information gain per query, leading to generalization error that decreases **exponentially** with the number of examples -- in contrast to random sampling, which yields zero information gain and only inverse power-law error decrease.

- **Freund, Seung, Shamir, & Tishby (1997)**, ["Selective Sampling Using the Query by Committee Algorithm"](https://link.springer.com/article/10.1023/A:1007330508534), Machine Learning 28(2-3), pp. 133-168. This paper extended QBC to the **selective sampling** (stream-based) setting: given an infinite stream of unlabeled examples, the algorithm decides which to send to an oracle for labeling. The key result: if a two-member committee achieves information gain with positive lower bound, prediction error decreases exponentially with the number of queries.

**Core QBC Mechanism:**
- A committee of models is drawn from the **version space** (the set of hypotheses consistent with current labeled data)
- Each committee member votes on the label of each candidate
- The candidate with **maximum disagreement** (measured via vote entropy, consensus entropy, or KL divergence) is selected for labeling
- The goal is to **minimize the version space** as rapidly as possible by querying the most informative samples
- This process concentrates queries on samples near **decision boundaries** -- where committee members disagree most

### 2. What QBC Selects: Decision Boundaries, Not Tails

This is a critical distinction. QBC fundamentally selects samples that lie near the **decision boundary** between competing hypotheses. As noted in [Burr Settles' Active Learning Literature Survey](https://burrsettles.com/pub/settles.activelearning.pdf), uncertainty-based methods including QBC have a well-known limitation: they are "prone to querying outliers" near the classification boundary, and the most uncertain instance "is not 'representative' of other instances in the distribution, so knowing its label is unlikely to improve the accuracy of the data as a whole." This has led to complementary approaches like **density-weighted methods** that combine uncertainty with representativeness.

In other words, QBC is designed to **resolve ambiguity at the boundary** -- it targets the samples that are most confusing to the current hypothesis set. It does NOT specifically target tail/rare examples unless those happen to coincide with the decision boundary. In many real distributions, tail examples may actually fall far from any decision boundary and would be **ignored** by standard QBC.

### 3. The Key Paradigm Difference: "What to Label" vs. "What to Retain"

This is the most fundamental distinction between QBC and DWIC:

- **QBC (Active Learning)**: Operates in a setting where you have a large pool of **unlabeled** data and a limited labeling budget. The question is: "Which samples should I send to an oracle for annotation?" The goal is **efficient label acquisition**. Selected samples get labeled and added to the training set.

- **DWIC (Data Curation for Retraining)**: Operates in a setting where you have a large corpus of **already-generated synthetic data** (or a mix of real + synthetic). The question is: "Which samples should I retain or upweight in the next round of training?" The goal is **preventing distribution collapse** in iterative retraining. Selected samples are retained/upweighted rather than labeled.

Research from [CVPR 2025 (Active Data Curation)](https://arxiv.org/abs/2411.18674) explicitly notes this paradigm shift: active data curation reframes selection as "implicit distillation" rather than traditional active learning, and the authors show that techniques from active learning "do not trivially extend" to data curation settings.

### 4. The Model Collapse Problem DWIC Addresses

The [Shumailov et al. (2024) Nature paper](https://pubmed.ncbi.nlm.nih.gov/39048682/) established that iterative training on synthetic data causes **model collapse** -- specifically, "tails of the original content distribution disappear." The mechanism: finite sampling from a model underrepresents tail regions, the next model trained on this data generates even fewer tail samples, and errors compound across generations. Early-stage collapse manifests as **tail disappearance**; late-stage collapse converges to a shrunken, low-variance distribution.

This is the specific problem DWIC targets: using multi-verifier disagreement as a signal to **preserve tail data** that would otherwise be lost in iterative synthetic retraining loops.

### 5. Recent Related Work at the Intersection

Several 2024-2025 works operate in the space between QBC and DWIC:

- **"Curated Synthetic Data Doesn't Have to Collapse"** ([arXiv:2605.07724](https://arxiv.org/abs/2605.07724), 2025): Shows that using **pluralistic/multiple reward functions** during data curation prevents mode collapse. When different reward functions disagree on what to favor, the resulting distribution converges to a stable mixture maintaining support over all high-reward regions. The parallel to DWIC is direct: disagreement between evaluators preserves diversity.

- **"Escaping Model Collapse via Synthetic Data Verification"** ([arXiv:2510.16657](https://arxiv.org/abs/2510.16657)): Analyzes iterative retraining with an external verifier that filters synthetic data. Uses a single verifier (not a committee), provides theoretical conditions under which verification prevents collapse. Does not address tail preservation specifically.

- **Multi-Agent Verification (MAV)** ([arXiv:2502.20379](https://arxiv.org/abs/2502.20379)): Uses multiple verifiers at inference time (not training-time curation), treating disagreement between verifiers as a feature that provides robustness. Operates at test time only, not for training data selection.

- **Superfiltering** ([ACL 2024](https://aclanthology.org/2024.acl-long.769/)): Uses Instruction-Following Difficulty (IFD) scores to filter training data, showing strong rank correlation between weak and strong models. This is a single-model filtering approach, not committee-based.

- **QAQ** ([arXiv:2603.12165](https://arxiv.org/pdf/2603.12165)): Uses the "cognitive gap" between strong and weak models as a selection signal for synthetic code instructions. Retains samples where models disagree (valid but challenging). This is perhaps the closest existing work to a QBC-like approach applied to synthetic data curation.

- **Multi-Actor Collaborative Data Selection** ([ACL 2025](https://aclanthology.org/2025.acl-long.466/)): Uses multiple independent scoring actors (quality, domain, topic) with a console that dynamically integrates their signals. However, it aggregates via weighted consensus rather than leveraging disagreement as the primary signal, and does not address tail preservation.

- **ACID/ACED** ([CVPR 2025](https://arxiv.org/abs/2411.18674)): Active data curation using a reference model's loss vs. student model's loss as a selection criterion. Explicitly notes this is NOT disagreement-based -- it measures the gap between reference and student rather than committee disagreement.

### 6. What DWIC Adds Beyond Standard QBC

The reviewer's claim that "DWIC is essentially QBC applied to synthetic data curation with a tail-preservation framing" captures the intellectual ancestry but undersells several important distinctions:

**A. Inverted Selection Logic**
- QBC selects high-disagreement samples **for labeling** (to efficiently reduce the version space)
- DWIC uses disagreement to **retain/upweight** samples in retraining (to prevent distributional collapse)
- This is not a trivial reframing. In QBC, high-disagreement samples need labels because they are at the decision boundary. In DWIC, high-disagreement samples need retention because they represent distributional regions at risk of being lost.

**B. Different Objective Function**
- QBC optimizes for **label efficiency** -- minimize the number of queries needed for good classification
- DWIC optimizes for **distributional fidelity** -- preserve the full distribution (especially tails) across iterative retraining rounds
- QBC's exponential error reduction guarantee is about classification error at the decision boundary, not about preserving the shape of the overall data distribution.

**C. The Tail-Preservation Insight**
- QBC focuses on the decision boundary -- the region of maximum classifier ambiguity
- DWIC's insight is that verifier disagreement can serve as a proxy for tail/rare data -- regions where different verifiers have learned different representations because the data is sparse
- This is a genuinely different use of disagreement: not "these samples are hard to classify" but rather "these samples are underrepresented and at risk of disappearing"

**D. Iterative Retraining Context**
- QBC operates in a single learning loop (label, retrain, query, repeat)
- DWIC operates in a **generative retraining loop** where the data itself is synthetic and the risk is compound distributional drift across generations
- The theoretical concerns are fundamentally different: QBC worries about sample efficiency for learning; DWIC worries about model collapse from recursive self-training

**E. No Oracle Assumption**
- QBC assumes access to an oracle that provides ground-truth labels for queried samples
- DWIC has no oracle -- the signal comes entirely from inter-verifier disagreement. The verifiers themselves are imperfect and their disagreement is the only supervision signal for curation.

### 7. Recommended Positioning

The honest and strongest positioning acknowledges QBC as clear intellectual ancestry while articulating the genuine novelty:

1. **Acknowledge**: DWIC shares QBC's core mechanism -- using committee disagreement as an information signal for data selection. The lineage from Seung et al. (1992) and Freund et al. (1997) should be explicitly cited.

2. **Distinguish the problem setting**: QBC is an active learning algorithm for efficient label acquisition. DWIC repurposes the committee disagreement signal for a fundamentally different problem: preventing distributional collapse in iterative synthetic retraining. This is akin to how attention mechanisms originated in one domain and were repurposed for another -- the mechanism is shared, but the problem formulation is novel.

3. **Highlight the inversion**: In QBC, disagreement identifies samples that need external information (labels). In DWIC, disagreement identifies samples that contain information at risk of being lost. QBC adds information to the system; DWIC preserves information already in the system.

4. **Emphasize the tail connection**: QBC's theoretical analysis focuses on decision boundary regions and version space reduction. DWIC's contribution is connecting disagreement to tail preservation -- arguing that verifier disagreement is a proxy for distributional sparsity, not just classifier uncertainty. This is supported by the model collapse literature showing that tails are the first casualty of iterative retraining (Shumailov et al., 2024).

5. **Cite the emerging intermediate literature**: The "Curated Synthetic Data Doesn't Have to Collapse" paper (2605.07724) provides theoretical support that pluralistic/disagreeing evaluators preserve distributional diversity. The QAQ framework shows cognitive-gap disagreement as a practical selection signal for synthetic data. These works occupy the space between classical QBC and DWIC without fully instantiating DWIC's specific proposal.

### Summary

The reviewer is right that QBC is the clear ancestor and must be acknowledged prominently. But the claim that DWIC is "essentially QBC" oversimplifies in important ways: the problem setting (curation vs. labeling), the objective (distributional preservation vs. label efficiency), the theoretical concerns (model collapse vs. version space reduction), the role of disagreement (preservation signal vs. query signal), and the absence of an oracle all represent substantive differences. The strongest response is to own the QBC lineage explicitly, position DWIC as a principled adaptation of committee disagreement from the active learning paradigm to the synthetic retraining paradigm, and clearly articulate what the adaptation requires and what new guarantees or insights it provides.

agentId: a0427c3968321eebf (use SendMessage with to: 'a0427c3968321eebf' to continue this agent)
&lt;usage>total_tokens: 50794
tool_uses: 49
duration_ms: 343939&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a226bab4-a430-441a-9534-8d0286e19b54",
  "isSidechain": false,
  "promptId": "ae35a659-7407-4079-9c58-2bf4f6ffeb73",
  "type": "user",
  "uuid": "4142b497-4356-42c6-b431-7dd2d27ff949",
  "toolUseResult": {
    "status": "completed",
    "prompt": "A research proposal about \"Disagreement-Weighted Iterative Curation (DWIC)\" — using multi-verifier disagreement to preserve tail data in synthetic retraining — was criticized for not acknowledging its connection to Query-by-Committee (QBC) active learning. The reviewer said \"DWIC is essentially QBC applied to synthetic data curation with a tail-preservation framing.\"\n\nPlease research:\n\n1. Search for \"query by committee active learning\" - find the seminal papers (Seung, Opper, Sompolinsky 1992; Freund et al. 1997)\n2. Search for \"query by committee synthetic data\" and \"active learning data curation LLM\"\n3. Search for \"committee disagreement data selection language models 2024 2025\"\n4. Read key papers to understand:\n   - The classical QBC framework and its theoretical properties\n   - How QBC relates to selecting samples at the decision boundary vs. the tail\n   - Key differences between QBC (selecting what to LABEL next) vs. DWIC (selecting what to RETAIN/UPWEIGHT in retraining)\n   - Any recent work applying QBC-like ideas to LLM training data curation\n   - What specifically DWIC adds beyond standard QBC\n\nThe goal is to properly position DWIC relative to this intellectual ancestry while clearly articulating what is novel. Report findings in detail.",
    "agentId": "a0427c3968321eebf",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have a comprehensive understanding of the research landscape. Here is my detailed report:\n\n---\n\n## Research Report: Positioning DWIC Relative to Query-by-Committee (QBC) Active Learning\n\n### 1. The Classical QBC Framework\n\n**Seminal Papers:**\n\n- **Seung, Opper, & Sompolinsky (1992)**, [\"Query by Committee\"](https://dl.acm.org/doi/10.1145/130385.130417), Proceedings of the Fifth Annual ACM Workshop on Computational Learning Theory, pp. 287-294. This paper introduced the QBC algorithm: a committee of learners is trained on the same dataset, and the next query is chosen according to the principle of **maximal disagreement**. The key theoretical result is that QBC achieves asymptotically finite information gain per query, leading to generalization error that decreases **exponentially** with the number of examples -- in contrast to random sampling, which yields zero information gain and only inverse power-law error decrease.\n\n- **Freund, Seung, Shamir, & Tishby (1997)**, [\"Selective Sampling Using the Query by Committee Algorithm\"](https://link.springer.com/article/10.1023/A:1007330508534), Machine Learning 28(2-3), pp. 133-168. This paper extended QBC to the **selective sampling** (stream-based) setting: given an infinite stream of unlabeled examples, the algorithm decides which to send to an oracle for labeling. The key result: if a two-member committee achieves information gain with positive lower bound, prediction error decreases exponentially with the number of queries.\n\n**Core QBC Mechanism:**\n- A committee of models is drawn from the **version space** (the set of hypotheses consistent with current labeled data)\n- Each committee member votes on the label of each candidate\n- The candidate with **maximum disagreement** (measured via vote entropy, consensus entropy, or KL divergence) is selected for labeling\n- The goal is to **minimize the version space** as rapidly as possible by querying the most informative samples\n- This process concentrates queries on samples near **decision boundaries** -- where committee members disagree most\n\n### 2. What QBC Selects: Decision Boundaries, Not Tails\n\nThis is a critical distinction. QBC fundamentally selects samples that lie near the **decision boundary** between competing hypotheses. As noted in [Burr Settles' Active Learning Literature Survey](https://burrsettles.com/pub/settles.activelearning.pdf), uncertainty-based methods including QBC have a well-known limitation: they are \"prone to querying outliers\" near the classification boundary, and the most uncertain instance \"is not 'representative' of other instances in the distribution, so knowing its label is unlikely to improve the accuracy of the data as a whole.\" This has led to complementary approaches like **density-weighted methods** that combine uncertainty with representativeness.\n\nIn other words, QBC is designed to **resolve ambiguity at the boundary** -- it targets the samples that are most confusing to the current hypothesis set. It does NOT specifically target tail/rare examples unless those happen to coincide with the decision boundary. In many real distributions, tail examples may actually fall far from any decision boundary and would be **ignored** by standard QBC.\n\n### 3. The Key Paradigm Difference: \"What to Label\" vs. \"What to Retain\"\n\nThis is the most fundamental distinction between QBC and DWIC:\n\n- **QBC (Active Learning)**: Operates in a setting where you have a large pool of **unlabeled** data and a limited labeling budget. The question is: \"Which samples should I send to an oracle for annotation?\" The goal is **efficient label acquisition**. Selected samples get labeled and added to the training set.\n\n- **DWIC (Data Curation for Retraining)**: Operates in a setting where you have a large corpus of **already-generated synthetic data** (or a mix of real + synthetic). The question is: \"Which samples should I retain or upweight in the next round of training?\" The goal is **preventing distribution collapse** in iterative retraining. Selected samples are retained/upweighted rather than labeled.\n\nResearch from [CVPR 2025 (Active Data Curation)](https://arxiv.org/abs/2411.18674) explicitly notes this paradigm shift: active data curation reframes selection as \"implicit distillation\" rather than traditional active learning, and the authors show that techniques from active learning \"do not trivially extend\" to data curation settings.\n\n### 4. The Model Collapse Problem DWIC Addresses\n\nThe [Shumailov et al. (2024) Nature paper](https://pubmed.ncbi.nlm.nih.gov/39048682/) established that iterative training on synthetic data causes **model collapse** -- specifically, \"tails of the original content distribution disappear.\" The mechanism: finite sampling from a model underrepresents tail regions, the next model trained on this data generates even fewer tail samples, and errors compound across generations. Early-stage collapse manifests as **tail disappearance**; late-stage collapse converges to a shrunken, low-variance distribution.\n\nThis is the specific problem DWIC targets: using multi-verifier disagreement as a signal to **preserve tail data** that would otherwise be lost in iterative synthetic retraining loops.\n\n### 5. Recent Related Work at the Intersection\n\nSeveral 2024-2025 works operate in the space between QBC and DWIC:\n\n- **\"Curated Synthetic Data Doesn't Have to Collapse\"** ([arXiv:2605.07724](https://arxiv.org/abs/2605.07724), 2025): Shows that using **pluralistic/multiple reward functions** during data curation prevents mode collapse. When different reward functions disagree on what to favor, the resulting distribution converges to a stable mixture maintaining support over all high-reward regions. The parallel to DWIC is direct: disagreement between evaluators preserves diversity.\n\n- **\"Escaping Model Collapse via Synthetic Data Verification\"** ([arXiv:2510.16657](https://arxiv.org/abs/2510.16657)): Analyzes iterative retraining with an external verifier that filters synthetic data. Uses a single verifier (not a committee), provides theoretical conditions under which verification prevents collapse. Does not address tail preservation specifically.\n\n- **Multi-Agent Verification (MAV)** ([arXiv:2502.20379](https://arxiv.org/abs/2502.20379)): Uses multiple verifiers at inference time (not training-time curation), treating disagreement between verifiers as a feature that provides robustness. Operates at test time only, not for training data selection.\n\n- **Superfiltering** ([ACL 2024](https://aclanthology.org/2024.acl-long.769/)): Uses Instruction-Following Difficulty (IFD) scores to filter training data, showing strong rank correlation between weak and strong models. This is a single-model filtering approach, not committee-based.\n\n- **QAQ** ([arXiv:2603.12165](https://arxiv.org/pdf/2603.12165)): Uses the \"cognitive gap\" between strong and weak models as a selection signal for synthetic code instructions. Retains samples where models disagree (valid but challenging). This is perhaps the closest existing work to a QBC-like approach applied to synthetic data curation.\n\n- **Multi-Actor Collaborative Data Selection** ([ACL 2025](https://aclanthology.org/2025.acl-long.466/)): Uses multiple independent scoring actors (quality, domain, topic) with a console that dynamically integrates their signals. However, it aggregates via weighted consensus rather than leveraging disagreement as the primary signal, and does not address tail preservation.\n\n- **ACID/ACED** ([CVPR 2025](https://arxiv.org/abs/2411.18674)): Active data curation using a reference model's loss vs. student model's loss as a selection criterion. Explicitly notes this is NOT disagreement-based -- it measures the gap between reference and student rather than committee disagreement.\n\n### 6. What DWIC Adds Beyond Standard QBC\n\nThe reviewer's claim that \"DWIC is essentially QBC applied to synthetic data curation with a tail-preservation framing\" captures the intellectual ancestry but undersells several important distinctions:\n\n**A. Inverted Selection Logic**\n- QBC selects high-disagreement samples **for labeling** (to efficiently reduce the version space)\n- DWIC uses disagreement to **retain/upweight** samples in retraining (to prevent distributional collapse)\n- This is not a trivial reframing. In QBC, high-disagreement samples need labels because they are at the decision boundary. In DWIC, high-disagreement samples need retention because they represent distributional regions at risk of being lost.\n\n**B. Different Objective Function**\n- QBC optimizes for **label efficiency** -- minimize the number of queries needed for good classification\n- DWIC optimizes for **distributional fidelity** -- preserve the full distribution (especially tails) across iterative retraining rounds\n- QBC's exponential error reduction guarantee is about classification error at the decision boundary, not about preserving the shape of the overall data distribution.\n\n**C. The Tail-Preservation Insight**\n- QBC focuses on the decision boundary -- the region of maximum classifier ambiguity\n- DWIC's insight is that verifier disagreement can serve as a proxy for tail/rare data -- regions where different verifiers have learned different representations because the data is sparse\n- This is a genuinely different use of disagreement: not \"these samples are hard to classify\" but rather \"these samples are underrepresented and at risk of disappearing\"\n\n**D. Iterative Retraining Context**\n- QBC operates in a single learning loop (label, retrain, query, repeat)\n- DWIC operates in a **generative retraining loop** where the data itself is synthetic and the risk is compound distributional drift across generations\n- The theoretical concerns are fundamentally different: QBC worries about sample efficiency for learning; DWIC worries about model collapse from recursive self-training\n\n**E. No Oracle Assumption**\n- QBC assumes access to an oracle that provides ground-truth labels for queried samples\n- DWIC has no oracle -- the signal comes entirely from inter-verifier disagreement. The verifiers themselves are imperfect and their disagreement is the only supervision signal for curation.\n\n### 7. Recommended Positioning\n\nThe honest and strongest positioning acknowledges QBC as clear intellectual ancestry while articulating the genuine novelty:\n\n1. **Acknowledge**: DWIC shares QBC's core mechanism -- using committee disagreement as an information signal for data selection. The lineage from Seung et al. (1992) and Freund et al. (1997) should be explicitly cited.\n\n2. **Distinguish the problem setting**: QBC is an active learning algorithm for efficient label acquisition. DWIC repurposes the committee disagreement signal for a fundamentally different problem: preventing distributional collapse in iterative synthetic retraining. This is akin to how attention mechanisms originated in one domain and were repurposed for another -- the mechanism is shared, but the problem formulation is novel.\n\n3. **Highlight the inversion**: In QBC, disagreement identifies samples that need external information (labels). In DWIC, disagreement identifies samples that contain information at risk of being lost. QBC adds information to the system; DWIC preserves information already in the system.\n\n4. **Emphasize the tail connection**: QBC's theoretical analysis focuses on decision boundary regions and version space reduction. DWIC's contribution is connecting disagreement to tail preservation -- arguing that verifier disagreement is a proxy for distributional sparsity, not just classifier uncertainty. This is supported by the model collapse literature showing that tails are the first casualty of iterative retraining (Shumailov et al., 2024).\n\n5. **Cite the emerging intermediate literature**: The \"Curated Synthetic Data Doesn't Have to Collapse\" paper (2605.07724) provides theoretical support that pluralistic/disagreeing evaluators preserve distributional diversity. The QAQ framework shows cognitive-gap disagreement as a practical selection signal for synthetic data. These works occupy the space between classical QBC and DWIC without fully instantiating DWIC's specific proposal.\n\n### Summary\n\nThe reviewer is right that QBC is the clear ancestor and must be acknowledged prominently. But the claim that DWIC is \"essentially QBC\" oversimplifies in important ways: the problem setting (curation vs. labeling), the objective (distributional preservation vs. label efficiency), the theoretical concerns (model collapse vs. version space reduction), the role of disagreement (preservation signal vs. query signal), and the absence of an oracle all represent substantive differences. The strongest response is to own the QBC lineage explicitly, position DWIC as a principled adaptation of committee disagreement from the active learning paradigm to the synthetic retraining paradigm, and clearly articulate what the adaptation requires and what new guarantees or insights it provides."
      }
    ],
    "totalDurationMs": 343939,
    "totalTokens": 50794,
    "totalToolUseCount": 49,
    "usage": {
      "input_tokens": 902,
      "cache_creation_input_tokens": 2746,
      "cache_read_input_tokens": 44138,
      "output_tokens": 3008,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2746
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 902,
          "output_tokens": 3008,
          "cache_read_input_tokens": 44138,
          "cache_creation_input_tokens": 2746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2746,
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
      "otherToolCount": 49
    }
  },
  "sourceToolAssistantUUID": "a226bab4-a430-441a-9534-8d0286e19b54",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-19T09:30:40.252Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive research from all five agents. Let me synthesize the findings and produce a major revision of the research proposal.

Key takeaways from the research:

### 1. PROF Paper (2509.03403)
- PROF uses PRM+ORM **agreement** to filter data - keeping samples where PRM and ORM agree, discarding disagreement
- This is the **inverse** of DWIC's approach
- PROF was withdrawn from peer review
- Key positioning: PROF discards high-disagreement samples as noise; DWIC argues they contain information
- PROF only uses 2 verifiers in a fixed hierarchy (ORM as ground truth)


### 2. Behavioral Entanglement (2604.07650)
- LLM verifiers share correlated biases from pretraining, but this only applies to LLM-to-LLM pairs. A symbolic checker breaks this entanglement entirely since it has no shared pretraining with neural verifiers. Using ORM and PRM from different model families would further mitigate this concern.
### 3. Disagreement-Tail Hypothesis
- The reviewers are right that there's no direct theoretical link between disagreement and tail data, though disagreement does capture epistemic uncertainty.
- The problem is that disagreement signals both tail data and noise equally, and RLHF typically treats it as unreliability to filter out. Active learning research shows query-by-committee is biased toward outliers and noise, but ERD demonstrates you can regularize disagreement to focus on OOD detection instead.
- This means the original hypothesis needs substantial reworking.

### 4. QBC Connection
- Query-by-committee targets decision boundaries rather than tails, and while DWIC inverts the selection logic by retaining disagreement for retraining instead of labeling, I should acknowledge QBC as the intellectual foundation here.

### 5. Recent Literature
- Cross-model disagreement validates disagreement as a correctness signal, and PMDC uses maximum disagreement for RM evaluation. "Hard Examples Are All You Need" shows mixed-outcome examples generate the strongest GRPO learning signal—this is crucial evidence. LASeR uses multi-RM selection via bandits as a competing approach, while "From Accuracy to Robustness" reveals rule-based and model-based verifiers fail in complementary ways, and VHG combines dual symbolic and neural verifiers.

Looking at all this research, the core claim that disagreement identifies tail data is too simplistic and unsupported. I need to pivot: instead of framing disagreement as a tail-data detector, I should reposition it as identifying samples with maximum learning signal, which aligns with the evidence from "Hard Examples Are All You Need" and the GRPO findings.

The symbolic checker becomes essential for decomposing useful disagreement from noise—when it confirms correctness but neural verifiers disagree, that's epistemic uncertainty in a verified sample, whereas neural agreement with symbolic disagreement likely reflects format sensitivity. Rather than claiming disagreement preserves tails, I should frame this as diversity-preserving informativeness, since the model collapse literature shows tails vanish first and disagreement samples tend to be harder and more diverse.

PROF should be the primary baseline, positioning DWIC as its complement—where PROF discards disagreement, DWIC preserves it. I also need to address entanglement by requiring ORM and PRM from different model families, using the symbolic checker as the decorrelation anchor, and acknowledge that DWIC adapts committee disagreement principles from query-by-committee.

I'm planning a pilot experiment to characterize what actually lives in disagreement regions, softening the language around verifier ceilings and widening versus breaking, updating the venue list, and adding an alpha ablation plan. The core hypothesis should shift: multi-verifier disagreement identifies samples with high learning signal density—mixed outcomes, non-trivial reasoning patterns, edge cases—that get systematically removed during iterative synthetic retraining because single-verifier filtering eliminates them.

In domains with ground-truth verifiers like math and code, disagreement between neural verifiers on symbolically-correct samples reveals diverse solution strategies that a single verifier would discard, while disagreement on incorrect samples exposes interesting failure modes where neural verifiers get fooled. The pilot phase directly addresses reviewer concerns by characterizing disagreement patterns on MATH-500 with existing verifiers, categorizing samples by agreement type, and measuring whether high-disagreement samples are harder problems, rarer solution strategies, noisy, or adversarial. Then the revised method uses a structured approach to curate synthetic data based on these disagreement patterns. that hypothesis was too strong. The symbolic checker acts as a ground truth anchor for math and code, which is essential for separating signal from noise in disagreement. Research on hard examples and PRM-ORM agreement shows that mixed outcomes have the strongest learning signal, but only when we use the symbolic checker to distinguish genuine difficulty from noise. So instead of upweighting all disagreement, I should use the anchor to decompose it meaningfully. I'm going to revise the DWIC method to keep the name but substantially change the approach: use a panel of K≥3 verifiers where at least one is a symbolic anchor with near-perfect precision.

For each solution, I'm categorizing disagreement into four cases based on what the anchor verifier says—if it confirms correctness while neural verifiers disagree, that's high-value disagreement worth strong upweighting; if it rejects while neural verifiers think it's good, that's potential reward hacking to filter out; if both agree it's correct, that's baseline consensus; and if both reject it, discard it entirely. The key is that the symbolic checker decomposes disagreement into epistemic uncertainty on verified-correct solutions versus noise or errors. Then I'm applying a weighting scheme that balances baseline weight with the disagreement signal.

This directly addresses the reviewer concerns—I now have a mechanism to distinguish useful from noisy disagreement, PROF's filtering becomes a special case, the symbolic checker breaks the entanglement problem by using different model families, and I'm adding anchor decomposition that QTC doesn't have.

For the pilot, I'm planning to take MATH-500 problems, generate 256 solutions per problem from Qwen3-8B, score everything with all three verifiers, categorize by agreement pattern, and then analyze the results.

For symbolically-verified-correct solutions, I'll measure strategy diversity through solution clustering, check for problem difficulty correlation, and look at the neural verifier confidence distribution. For high-disagreement cases that are still symbolically correct, I want to see if they're using rare strategies, coming from harder problems, or containing novel reasoning patterns. This pilot is computationally feasible at around 50 H100-hours and directly tests whether my hypothesis holds.

Now I'm updating the resource estimates and timeline, and reconsidering the venue strategy—removing ARR May 2026 since that's too late, keeping AAAI 2027 and ICLR 2027 as both are feasible, and considering NeurIPS 2027 as well.

I'm recognizing this is a major revision rather than a minor one. The core hypothesis is being substantially reframed, the method gets anchor decomposition as a structural change, I'm adding a pilot study phase, and there are significant new baselines and positioning—though the overall direction around multi-verifier disagreement for curation stays intact. Now I need to write out the complete revised proposal, being careful to address each reviewer concern directly.

For the title, I'm cycling through options to find something that captures the anchor decomposition and disagreement signal more precisely. I'm settling on something cleaner that emphasizes how disagreement becomes an informativeness signal for iterative curation. I should also reconsider the "tail preservation" framing since the reviewers had concerns about that angle.

The stronger argument is that disagreement signals informativeness by preventing distributional collapse during retraining. The connection to tails is defensible through the chain: model collapse manifests as tail disappearance, single-verifier filtering accelerates this loss, and verifier-anchored disagreement identifies diverse samples that resist consensus. By preserving these samples, I maintain distributional breadth. This is more principled than claiming disagreement directly equals tail preservation.

Now I'm ready to draft the full proposal with this reframing in place, shifting the core problem from "disagreement ≈ tail" to "can anchor-decomposed verifier disagreement serve as a principled informativeness signal for preventing collapse?"

I'm planning concrete methodological updates: adding a two-week pilot phase to generate multiple solutions per problem, introducing anchor decomposition to structure disagreement categories, specifying the alpha ablation plan, and adding PROF and LASeR as baselines. I'll also expand the related work to include behavioral entanglement and other recent papers, soften claims about the verifier ceiling theorem, and adjust the timeline and compute estimates accordingly. MATH-500 from Qwen3-8B
- Score with SymPy (anchor), Skywork-Reward-8B (ORM), VersaPRM (PRM) 
- Categorize into agreement quadrants
- Measure: (a) problem difficulty distribution per quadrant, (b) solution strategy diversity per quadrant, (c) proportion of noise/format errors per quadrant
- Hypothesis validation: symbolically-correct + neurally-disagreed samples should show higher strategy diversity and concentrate on harder problems compared to symbolically-correct + neurally-agreed samples

Phase 1 (Method, 6-8 weeks):
- Anchor-decomposed DWIC uses a symbolic checker to establish ground truth, then decomposes neural disagreement based on whether the anchor confirms correctness: anchor-verified correct samples with high neural disagreement get upweighted as "diverse correct," anchor-verified correct with low disagreement stay at baseline, and anchor-incorrect samples are discarded. The weighting formula only upweights disagreement when the symbolic checker confirms, directly filtering out noise while preserving useful disagreement on verified samples.
- Ablation studies will test β values from 0 to 10 and vary the number of neural verifiers from 2 to 5, using verifiers from different families like Skywork-ORM, Qwen-PRM, and InternLM-PRM.
- The core insight reframes the original claim: on anchor-verified samples, neural disagreement signals diverse solution strategies that single-verifier filtering would discard, and keeping these samples prevents the distributional collapse that Shumailov et al. documented.
- I'll measure this through solution strategy coverage entropy, hardest-decile accuracy, Pass@k ratios, and distribution divergence across rounds—all operationally concrete and testable in the pilot study.
- Sticking with the DWIC name rather than renaming it to reflect the anchor decomposition, since that's more of an implementation refinement than a fundamental shift.

Now I'm ready to write out the full JSON specification for the method.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4142b497-4356-42c6-b431-7dd2d27ff949",
  "isSidechain": false,
  "requestId": "req_011CbBh57YCYgD3SQU16KtPU",
  "type": "assistant",
  "uuid": "95174b69-8d27-4af9-9ae6-c912154c2082",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0111e6DV2RadLnwYgWqeEx1Q",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4652,
      "cache_creation_input_tokens": 14906,
      "cache_read_input_tokens": 17712,
      "output_tokens": 10387,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14906,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4652,
          "output_tokens": 10387,
          "cache_read_input_tokens": 17712,
          "cache_creation_input_tokens": 14906,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14906
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

_source line 31 · 2026-05-19T09:32:49.478Z_

Now I have comprehensive research from all five agents. Let me synthesize the findings before producing the revised proposal.

## Research Synthesis

**Key findings that reshape the proposal:**

1. **PROF (2509.03403)**: Uses PRM-ORM **agreement** to filter training data — the exact inverse of DWIC. Keeps samples where process and outcome agree, discards disagreement as noise. Achieves ~2% accuracy gains over vanilla GRPO. Was withdrawn from peer review. Must be a primary baseline.

2. **Behavioral Entanglement (2604.07650)**: LLM verifiers DO share correlated biases from pretraining. BUT the paper only studies LLM-to-LLM entanglement — a symbolic checker has zero shared pretraining and categorically different failure modes. Defense: the symbolic checker is the genuine decorrelation anchor; ORM+PRM provide weaker but non-zero additional diversity (especially if from different model families).

3. **The "disagreement ≈ tail" hypothesis is indeed unsubstantiated**: No direct theoretical result exists. Disagreement captures epistemic uncertainty, which is high for BOTH tail data AND noise. The RLHF literature actually treats disagreement as unreliability and filters/penalizes it. The active learning literature explicitly warns QBC is biased toward outliers and noise. **This requires a major reframing.**

4. **Critical supporting evidence** from "Hard Examples Are All You Need" (2508.14094): Mixed-outcome samples (where the model sometimes succeeds, sometimes fails — analogous to verifier disagreement) carry maximum GRPO learning signal. The hardest 10% yields 47% improvement; easy examples yield near-zero. This provides a different but defensible justification.

5. **QBC heritage**: Must be explicitly acknowledged. Key differences: QBC selects for labeling vs. DWIC retains for retraining; QBC targets decision boundaries vs. DWIC targets distributional preservation; DWIC has no oracle.

6. **New competitors**: LASeR (multi-RM via bandits, NeurIPS 2025), PMDC (max-disagreement for RM evaluation), VHG (dual symbolic+neural verifiers), difficulty-targeted data selection (NeurIPS 2025).

**The core revision strategy**: The original hypothesis ("disagreement ≈ tail data") must be replaced with an **anchor-decomposed** framework. The symbolic checker serves as a ground-truth anchor that decomposes raw disagreement into useful signal (neural disagreement on symbolically-verified samples = diverse strategies) vs. noise (neural disagreement on unverifiable samples). This directly addresses the "disagreement could be noise" concern.

Now producing the complete revised proposal:

```json
{
  "change_type": "major",
  "title": "Anchor-Decomposed Verifier Disagreement as an Informativeness Signal for Iterative Synthetic Data Curation",
  "core_problem": "Can we decompose multi-verifier disagreement into useful vs. noisy components using a ground-truth anchor verifier, and use the useful component as a principled signal for preserving distributional diversity during iterative synthetic retraining?",
  "opportunity": "Yi et al. (2025) showed that a single verifier's biases bound achievable performance in iterative synthetic retraining — we refer to this as the 'verifier ceiling' effect (our framing, not their terminology). Falahati et al. (2026) proved theoretically that pluralistic preferences prevent distributional collapse, but no one has operationalized multi-verifier disagreement as a practical data curation mechanism. PROF (Ye et al., 2025) demonstrated that PRM-ORM agreement is a useful curation signal, but it discards disagreement samples entirely — treating them as noise. Meanwhile, 'Hard Examples Are All You Need' (2025) showed that samples with mixed outcomes (where the model sometimes succeeds, sometimes fails) carry maximum GRPO learning signal, with the hardest 10% yielding 47% improvement vs. near-zero for easy examples. This suggests that the high-disagreement samples PROF discards may contain precisely the high-learning-signal data needed to push performance boundaries. The key insight we propose: raw verifier disagreement is an omnibus signal mixing useful diversity with noise, but a ground-truth anchor verifier (symbolic checker) can decompose it — neural disagreement on anchor-verified-correct samples specifically indicates diverse solution strategies, not noise.",
  "landscape": "Current approaches to verified synthetic data curation fall into three categories: (1) Single-verifier filtering (Yi et al. 2025; Feng et al. ICLR 2025), which is subject to the verifier's own biases. (2) Multi-verifier agreement-based filtering: PROF (Ye et al., arXiv 2509.03403) uses PRM-ORM consistency to keep 'clean' samples where process quality and outcome correctness agree, discarding disagreement; CoVerRL (2026) and RL Tango (NeurIPS 2025) co-evolve generator-verifier pairs but use single verifiers per round. (3) Multi-reward selection: LASeR (Nguyen et al., NeurIPS 2025) uses multi-armed bandits to select the best RM per instance from a pool, but does not use disagreement itself as a signal. QAQ (March 2026) uses strong-vs-weak 'cognitive gap' for code instruction selection but operates with only two models in a non-iterative setting. In the broader verification landscape, Kuai et al. (arXiv 2604.07650) demonstrated 'behavioral entanglement' — LLM-based verifiers share correlated biases from shared pretraining — but their analysis is restricted to LLM-to-LLM panels and does not cover heterogeneous panels including symbolic verifiers, which have categorically different failure modes (Guo et al., arXiv 2505.22203 show rule-based verifiers suffer false negatives from format sensitivity while model-based verifiers suffer false positives from reward hacking — structurally complementary errors). PMDC (arXiv 2601.16987) uses maximum reward-model disagreement for RM evaluation but not for training data curation. The theoretical connection between committee disagreement and data selection has deep roots in query-by-committee (QBC) active learning (Seung et al. 1992; Freund et al. 1997), which selects maximally-disagreed samples for labeling to minimize version space. However, QBC targets decision-boundary samples for label efficiency — not distributional preservation — and the active learning literature explicitly warns that disagreement conflates informative uncertainty with noise (density-weighted methods were developed to mitigate this). The key gap we address: no work decomposes multi-verifier disagreement using a ground-truth anchor to separate diversity-indicating disagreement from noise, and no work uses this decomposed signal for iterative synthetic data curation to prevent distributional collapse.",
  "inspired_by": "Three converging insights: (1) PROF shows PRM-ORM agreement is a useful curation signal but discards disagreement entirely — we hypothesize this throws away high-value data. (2) 'Hard Examples Are All You Need' empirically demonstrates that mixed-outcome samples carry maximum GRPO learning signal — and verifier disagreement is a proxy for mixed outcomes. (3) The behavioral entanglement literature shows LLM-only verifier panels have correlated biases, but heterogeneous panels (neural + symbolic) have structurally complementary failure modes — the symbolic checker can serve as a decomposition anchor that separates useful from noisy disagreement.",
  "approach": "We propose Disagreement-Weighted Iterative Curation (DWIC) with a key methodological innovation: **anchor-decomposed disagreement**. Rather than treating raw verifier disagreement as a direct proxy for tail data (a claim the literature does not support — disagreement captures epistemic uncertainty generally, including noise and ambiguity), we use a ground-truth anchor verifier to decompose disagreement into interpretable categories.\n\n**Phase 0: Pilot Characterization Study (2 weeks, ~50 H100-hours).** Before full-scale experiments, we conduct a pilot to empirically validate the core hypothesis. Generate 256 candidate solutions per problem on MATH-500 from Qwen3-8B. Score each with three verifiers: SymPy symbolic checker (anchor), Skywork-Reward-8B (ORM, Qwen-family), and Math-Shepherd-PRM (Mistral-family, chosen for cross-family decorrelation per behavioral entanglement concerns). Categorize all samples into four quadrants by anchor status × neural agreement: (Q1) anchor-correct + neural-agree, (Q2) anchor-correct + neural-disagree, (Q3) anchor-incorrect + neural-agree, (Q4) anchor-incorrect + neural-disagree. For each quadrant, measure: (a) problem difficulty distribution, (b) solution strategy diversity via clustering of proof/solution approaches, (c) proportion of format errors vs. genuine reasoning variation, (d) whether Q2 samples disproportionately contain rare/novel solution strategies compared to Q1. The pilot validates or refutes our hypothesis that anchor-decomposed neural disagreement correlates with strategy diversity. If Q2 shows no enrichment for diverse strategies relative to Q1, we will reconsider the approach before committing to full-scale experiments.\n\n**Phase 1: Anchor-Decomposed DWIC (8 iterative rounds).** Assemble a panel of K≥3 structurally diverse verifiers with at least one symbolic anchor and ≥2 neural verifiers from different model families (to mitigate behavioral entanglement). At each round, generate N=256 candidate solutions per problem from the current policy (Qwen3-8B). The anchor verifier establishes correctness ground truth; neural verifier disagreement is computed only on anchor-verified samples:\n\n- **Anchor-correct + high neural disagreement** ('diverse correct'): upweight with factor 1 + β · d_neural(x)\n- **Anchor-correct + low neural disagreement** ('consensus correct'): baseline weight 1.0\n- **Anchor-incorrect** (any neural status): discard (standard verified filtering)\n- **Anchor-indeterminate** (timeout/format issues): use neural majority vote with conservative weight γ < 1.0\n\nHere d_neural(x) = normalized disagreement across neural verifiers (variance of normalized scores), β controls upweighting strength, and γ controls the trust in neural-only verification. This formulation ensures disagreement-based upweighting is applied ONLY to samples whose correctness is anchor-verified, directly addressing the concern that disagreement may indicate noise rather than useful diversity.\n\n**Ablation grid for β:** {0, 0.5, 1, 2, 5} — where β=0 recovers standard anchor-verified filtering (a strong baseline). **Ablation for K (neural verifiers):** {2, 3, 5} using combinations from Skywork-ORM (Qwen), Math-Shepherd-PRM (Mistral), InternLM2-Reward (InternLM), and Eurus-RM (CodeLlama) to ensure cross-family diversity. **Ablation for γ:** {0, 0.3, 0.5, 0.7}.\n\n**Evaluation:** Run 8 iterative retraining rounds on MATH-500, AIME 2024, and LiveCodeBench. Measure: (1) downstream accuracy (Pass@1), (2) distributional health via Pass@k/Pass@1 ratio (diversity of correct solutions), solution-strategy coverage entropy, and hardest-decile accuracy, (3) round-over-round collapse metrics (KL divergence from round-1 distribution). Compare against: single-verifier SymPy filtering, PROF (PRM-ORM agreement filtering), LASeR (bandit-based RM selection), CoVerRL (co-evolved verifiers), RL Tango, DPH-RL (f-divergence regularization), uniform sampling, and β=0 ablation (anchor-verified filtering without disagreement upweighting).\n\n**Connection to theory:** Falahati et al. (2026) prove that pluralistic preferences converge to a weighted Nash bargaining solution maintaining distributional support. Our anchor-decomposed disagreement operationalizes this: neural disagreement on verified-correct samples reflects pluralistic evaluative perspectives, and upweighting these samples preserves the distributional breadth that single-verifier filtering erodes. This is complementary to, not a replacement for, the classical QBC insight (Seung et al. 1992) that committee disagreement identifies informative samples — our contribution is the anchor decomposition that separates informative from noisy disagreement, and the application to iterative synthetic retraining rather than active label acquisition.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "800-1100 H100-hours (pilot ~50h, 3 verifier setups ~150h, 8 retraining rounds ~256h, generation ~100h, ablations over β/K/γ ~250h, PROF/LASeR baseline reproduction ~100h)",
      "timeline": "14-18 weeks with 2 researchers (2 weeks pilot + 12-16 weeks main experiments)",
      "estimated_gpu_cost": "$2,000-$2,750 at ~$2.50/H100-hr"
    },
    "human_in_loop": {
      "gpu_hours": "800-1100 H100-hours (same GPU workload; Claude accelerates code, analysis, and paper drafting)",
      "timeline": "10-13 weeks with 1-2 researchers",
      "claude_api_cost": "$400-600 (experiment scripting, pilot analysis, ablation notebooks, paper drafting via Sonnet 4.6)",
      "estimated_gpu_cost": "$2,000-$2,750"
    },
    "auto_research": {
      "gpu_hours": "1400-1800 H100-hours (broader sweeps over β, K, γ, neural verifier family combinations, disagreement metrics; automated pilot analysis)",
      "timeline": "6-8 weeks",
      "claude_api_cost": "$900-1,400 (orchestration, code generation, iterative analysis, paper writing via Sonnet 4.6 + Opus 4.7 for theory sections)",
      "estimated_gpu_cost": "$3,500-$4,500",
      "speed_bottleneck": "GPU cluster queue time for sequential retraining rounds (~32h wall-clock per 8-round configuration on 8xH100); pilot study is a prerequisite gate for Phase 1"
    }
  },
  "target_venues": [
    "AAAI 2027 (full paper deadline: July 28, 2026 — feasible with pilot complete by mid-June)",
    "ICLR 2027 (estimated deadline: ~October 2026 — primary target with full results)",
    "NeurIPS 2027 (estimated deadline: ~May 2027 — fallback with comprehensive ablations)"
  ],
  "level": "top-tier",
  "key_references": [
    "Escaping Model Collapse via Synthetic Data Verification (Yi et al., ICLR 2026 DATA-FM Workshop) — single-verifier ceiling effect",
    "Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification (Feng et al., ICLR 2025) — verified iterative retraining",
    "Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences (Falahati et al., arXiv 2605.07724, 2026) — pluralistic preferences theory",
    "Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training [PROF] (Ye et al., arXiv 2509.03403, 2025) — PRM-ORM agreement-based data curation (primary baseline)",
    "How Independent are Large Language Models? Behavioral Entanglement and Reweighting Verifier Ensembles (Kuai et al., arXiv 2604.07650, 2026) — verifier correlation from shared pretraining",
    "Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking (Eisenstein et al., ICML 2024) — RM ensemble disagreement under distribution shift",
    "From Accuracy to Robustness: Rule- and Model-based Verifiers in Mathematical Reasoning (Guo et al., arXiv 2505.22203, 2025) — complementary failure modes of verifier types",
    "Hard Examples Are All You Need: Maximizing GRPO Post-Training Under Annotation Budgets (arXiv 2508.14094, 2025) — mixed-outcome samples carry maximum learning signal",
    "LASeR: Learning to Adaptively Select Reward Models with Multi-Armed Bandits (Nguyen et al., NeurIPS 2025) — bandit-based multi-RM selection",
    "Query by Committee (Seung, Opper, & Sompolinsky, COLT 1992) — foundational committee disagreement for data selection",
    "Selective Sampling Using the Query by Committee Algorithm (Freund et al., Machine Learning 1997) — QBC theoretical analysis",
    "Synthetic Eggs in Many Baskets: Impact of Synthetic Data Diversity on LLM Fine-Tuning (Schaffelder & Gatt, ACL Findings 2026) — multi-source diversity mitigates collapse",
    "CoVerRL: Breaking the Consensus Trap via Generator-Verifier Co-Evolution (arXiv 2026) — co-evolved verifiers",
    "RL Tango: Reinforcing Generator and Verifier Together (Zha et al., NeurIPS 2025) — co-training generator-verifier",
    "The Choice of Divergence: Mitigating Diversity Collapse in RLVR [DPH-RL] (arXiv 2025) — f-divergence for diversity",
    "Evaluating Reward Model Generalization via Pairwise Maximum Discrepancy Competition [PMDC] (arXiv 2601.16987, 2026) — max-disagreement for RM evaluation",
    "Cross-Model Disagreement as a Label-Free Correctness Signal (arXiv 2603.25450, 2026) — disagreement as reliable signal",
    "QAQ: Bidirectional Semantic Coherence for Selecting High-Quality Synthetic Code Instructions (arXiv 2026) — two-model cognitive gap for code data selection",
    "Verification Limits Code LLM Training (Gureja et al., arXiv 2025) — verifier limitations in code",
    "Weaver: Shrinking the Generation-Verification Gap with Weak Verifiers (Saad-Falcon et al., NeurIPS 2025) — combining weak verifiers",
    "The Curse of Recursion: Training on Generated Data Makes Models Forget (Shumailov et al., Nature 2024) — model collapse and tail disappearance",
    "Improving Data Efficiency for LLM RL Fine-tuning Through Difficulty-Targeted Online Data Selection (NeurIPS 2025) — difficulty-based curation alternative",
    "Verifier-Backed Hard Problem Generation (Lai et al., arXiv 2605.06660, 2026) — dual symbolic+neural verification"
  ],
  "description": "We propose Disagreement-Weighted Iterative Curation (DWIC) with anchor-decomposed disagreement, a method that uses a ground-truth symbolic verifier as an anchor to decompose multi-verifier disagreement into useful vs. noisy components for iterative synthetic data curation. The key insight addresses a fundamental limitation of raw disagreement: ensemble disagreement is an omnibus signal capturing epistemic uncertainty from BOTH informative diversity and uninformative noise (a concern well-established in the QBC/active-learning literature). Our anchor decomposition resolves this: a panel of K≥3 structurally diverse verifiers — including a symbolic checker (SymPy/test-execution) as the anchor and ≥2 neural verifiers (ORM, PRM) from different model families to mitigate behavioral entanglement (Kuai et al. 2026) — scores each synthetically generated candidate. Neural disagreement is only used as an upweighting signal on anchor-verified-correct samples, where it indicates diverse solution strategies rather than noise. This directly complements PROF (Ye et al. 2025), which uses PRM-ORM agreement to filter noise but discards the high-disagreement samples that 'Hard Examples Are All You Need' (2025) shows carry maximum GRPO learning signal. We first conduct a pilot characterization study on MATH-500 to empirically validate that anchor-decomposed neural disagreement correlates with solution strategy diversity (not just noise), then run 8 iterative retraining rounds with Qwen3-8B, evaluating both downstream accuracy and distributional health (Pass@k ratio, strategy-coverage entropy, hardest-decile accuracy) against PROF, LASeR, CoVerRL, RL Tango, DPH-RL, and single-verifier baselines on MATH-500, AIME 2024, and LiveCodeBench.",
  "project_name": "disagree_tail_curate",
  "source": "web_research",
  "revision_notes": {
    "issue_1_disagreement_tail_hypothesis": "MAJOR REFRAMING. The original claim 'disagreement ≈ tail data' was correctly identified as unsubstantiated. Research confirms no direct theoretical result links ensemble disagreement to distribution tails — disagreement is an omnibus epistemic uncertainty signal also elevated for noise, ambiguity, and adversarial inputs. We introduce 'anchor-decomposed disagreement': the symbolic checker serves as a ground-truth anchor that decomposes raw disagreement into (a) 'diverse correct' samples (neural disagreement on symbolically-verified solutions — indicating strategy diversity, not noise) and (b) discardable noise. Additionally, we cite 'Hard Examples Are All You Need' (2508.14094) showing mixed-outcome samples carry maximum GRPO learning signal, providing empirical justification. A mandatory pilot study on MATH-500 will validate the hypothesis before full-scale experiments.",
    "issue_2_PROF_baseline": "ADDRESSED. PROF (Ye et al., arXiv 2509.03403) added as a primary baseline and extensively discussed. PROF uses PRM-ORM agreement to retain 'clean' samples and discards disagreement — the exact inverse of DWIC's signal. We position DWIC as complementary: PROF's filtered-out samples (correct answer but low PRM, or incorrect answer but high PRM) may contain the diverse, high-learning-signal data that DWIC aims to preserve via anchor-decomposed upweighting.",
    "issue_3_behavioral_entanglement": "ADDRESSED. Kuai et al. (arXiv 2604.07650) extensively discussed. Three mitigations: (1) The symbolic checker has zero shared pretraining and categorically different failure modes (format-sensitivity false negatives vs. neural hallucination false positives, per Guo et al. 2505.22203) — the entanglement framework literally does not apply to it. (2) Neural verifiers are drawn from different model families (e.g., Qwen-based ORM + Mistral-based PRM) to minimize cross-family entanglement. (3) We no longer claim 'three independent signals' but rather 'two partially correlated neural signals plus one categorically independent non-neural anchor.'",
    "issue_4_venue_realism": "ADDRESSED. Removed EMNLP 2026 and AACL-IJCNLP 2026 via ARR May cycle (6 days away — infeasible). Retained AAAI 2027 (July 28, 2026) and ICLR 2027 (~October 2026). Added NeurIPS 2027 (~May 2027) as fallback.",
    "issue_5_QBC_ancestry": "ADDRESSED. Query-by-committee (Seung et al. 1992, Freund et al. 1997) explicitly cited as intellectual ancestry. Key distinctions articulated: (1) QBC selects samples for labeling (oracle-dependent) vs. DWIC retains/upweights for retraining (no oracle); (2) QBC targets decision-boundary samples for label efficiency vs. DWIC targets distributional preservation against iterative collapse; (3) QBC's theoretical guarantees concern version-space reduction, not tail preservation; (4) DWIC adds anchor decomposition to address QBC's known bias toward noise/outliers — a limitation the active learning literature explicitly warns about.",
    "issue_6_overclaiming": "ADDRESSED. Removed 'verifier ceiling theorem' — now described as the 'verifier ceiling effect (our framing, not their terminology).' Removed 'widening vs. breaking' language attributed to Falahati et al. All theoretical framings clearly labeled as our interpretations where applicable.",
    "issue_7_alpha_hyperparameter": "ADDRESSED. The original underspecified formula α + (1-α)·d(x) is replaced by a more principled anchor-decomposed formulation: w(x) = 1 + β·d_neural(x)·I[anchor_correct(x)], which only applies disagreement upweighting to anchor-verified samples. Explicit ablation grid: β ∈ {0, 0.5, 1, 2, 5}, K (neural verifiers) ∈ {2, 3, 5}, γ (anchor-indeterminate weight) ∈ {0, 0.3, 0.5, 0.7}. β=0 recovers standard verified filtering as a built-in baseline."
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95174b69-8d27-4af9-9ae6-c912154c2082",
  "isSidechain": false,
  "requestId": "req_011CbBh57YCYgD3SQU16KtPU",
  "type": "assistant",
  "uuid": "3d4f191e-6153-41b8-96d8-1c34ae26dc5d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0111e6DV2RadLnwYgWqeEx1Q",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4652,
      "cache_creation_input_tokens": 14906,
      "cache_read_input_tokens": 17712,
      "output_tokens": 10387,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14906,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4652,
          "output_tokens": 10387,
          "cache_read_input_tokens": 17712,
          "cache_creation_input_tokens": 14906,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14906
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

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"Verifier Disagreement as Tail-Preservation Signal in Synthetic Data Cu…",
  "leafUuid": "3d4f191e-6153-41b8-96d8-1c34ae26dc5d",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise verifier disagreement tail-preservation hypothesis",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"Verifier Disagreement as Tail-Preservation Signal in Synthetic Data Cu…",
  "leafUuid": "3d4f191e-6153-41b8-96d8-1c34ae26dc5d",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise verifier disagreement tail-preservation hypothesis",
  "sessionId": "593b0787-5a72-44d5-85e8-706f2a81fa97"
}
```

---
