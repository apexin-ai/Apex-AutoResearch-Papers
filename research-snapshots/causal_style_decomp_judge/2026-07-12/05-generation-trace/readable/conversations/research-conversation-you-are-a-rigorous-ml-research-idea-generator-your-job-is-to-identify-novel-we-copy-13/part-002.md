# Research conversation: You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing — Part 2 of 2

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-you-are-a-rigorous-ml-research-idea-generator-your-job-is-to-identify-novel-we-copy-13.md) · [Structured JSON](../../../sessions/79/79e92d6b6ff1f4e08678.json)

## Round 1

### Assistant

_source line 254 · 2026-05-29T11:54:17.222Z_

<details><summary>Logged reasoning block</summary>

```text
This KG-as-reward-model paper is interesting but targets the medical domain and uses KGs for RL reward shaping, not for data synthesis/coverage. It's a related approach but different enough.

OK, I now have a very thorough picture. Let me compile my final analysis.

Summary of competitive landscape based on my searches:

**Papers that use skill graphs for math:**
- MASS (ICML 2025): Skill co-occurrence graph for data SELECTION efficiency. 46K skills, 1.18M edges. Does NOT target composition.
- Skill-Aware Data Selection (Jan 2026): Hierarchical skill tree for ATOMIC skill targeting in distillation.


- STAT (NeurIPS 2025): Tracks atomic skill gaps and synthesizes single-skill problems.

**Papers that target compositional generalization:**
- STEPS (Jan 2026): Uses skill taxonomy and structural entropy for compositional data synthesis, but focuses on instruction-following rather than math.
- Agentic Proposing (Feb 2026): Applies difficulty-adaptive skill composition without coverage-based approaches.
- MindLoom (May 2026): Explores thought mode composition but lacks coverage-based or DAG-structured design.
- Chang et al. (ICLR 2026) and Redhardt (NeurIPS 2025): Both address coverage principles, though Chang et al. only measures coverage without proposing construction methods.
- Zhao & Kaur (NeurIPS 2024): Demonstrates k→k+1 transfer but only for language skills.

**Papers that do math data synthesis:**
- KPDDS (AAAI 2025): Key-point driven synthesis without compositional targeting.
- MathFusion (ACL 2025): Problem fusion lacking coverage guidance.
- MathMixup (Jan 2026): Difficulty-controllable synthesis with curriculum but no compositional coverage.
- RV-Syn (Apr 2025): Structured function library with computational graphs for general math, not compositional.
- Arrows of Math (CIKM 2025): Addresses diversity, complexity, and correctness without compositional frontier.

**Benchmarks for compositional math:**
- OMEGA (NeurIPS 2025): Contains 40 templates.

OMEGA spans 6 domains with 2-skill compositions, and reinforcement learning fails on the compositional axis. MathTrap diagnoses compositional deficiency through trap problems, while AgentCoMa shows roughly 30% performance drop when combining commonsense and math skills.

The real gap is that no one has integrated skill dependency structure from math templates with compositional frontier identification and targeted synthesis of under-covered compositions to overcome the compositional ceiling. This combination is genuinely novel—zero papers directly address it—making it a strong candidate for AAAI 2027.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0db5d59-4f16-4be1-ae47-6e7270266606",
  "isSidechain": false,
  "requestId": "req_011CbWpDHTs1bKW37wyArYC8",
  "type": "assistant",
  "uuid": "c9ddc7d2-44f6-4f1b-bd0d-42f3e852681c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "7647c642-258e-4d28-8a6f-8e19098b0cdb",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118qmwTEUMG8MiF3iYmhQNM",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 83596,
      "output_tokens": 3139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 709,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3139,
          "cache_read_input_tokens": 83596,
          "cache_creation_input_tokens": 709,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 709
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

_source line 255 · 2026-05-29T11:55:03.158Z_

I now have a comprehensive understanding of the landscape. Let me compile my final analysis.

---

## Research Summary

After conducting **18+ targeted searches** across arXiv, OpenReview, GitHub, conference proceedings, and survey papers, and **reading 12+ papers in depth** via WebFetch, here is my assessment:

### Key Findings from Deep Research

**1. The gap is verified and open.** No published work combines skill dependency DAGs with compositional frontier identification for mathematical training data synthesis. Specifically:
- **MASS** (ICML 2025) uses skill graphs for data *selection efficiency* (confirmed: 46K skills, 1.18M edges, targeting 50-70% data reduction), explicitly **not** compositional generalization
- **STEPS** (Jan 2026) provides the information-theoretic framework but validates only on instruction-following (WildBench, AlpacaEval), **not** mathematical reasoning
- **STAT** (NeurIPS 2025) targets *atomic* skill gaps — its STAT-Syn explicitly **decomposes** multi-skill problems into single-skill ones (opposite of our approach)
- **Agentic Proposing** (Feb 2026) uses *difficulty*-adaptive selection (proficiency-inverse sampling), **not** coverage-based selection; no skill graph structure
- **MindLoom** (May 2026) composes "thought modes" iteratively, **not** via DAG-structured skill dependencies; no OMEGA evaluation
- **Chang et al.** (ICLR 2026) formalizes the coverage principle but explicitly states their framework "will motivate future research on targeted data augmentation strategies to maximize k-coverage" — no construction method provided

**2. OMEGA's compositional axis remains unsolved.** All existing OMEGA results use RL or prompting. RL gives limited compositional gains "only when training composition was semantically similar to evaluation." No published method has applied targeted data interventions to OMEGA's compositional axis.

**3. AAAI 2026 deadline has passed** (was Aug 1, 2025). **AAAI 2027** (deadline July 28, 2026) is the nearest viable top venue — 8 weeks from today.

**4. Critical baseline concern validated.** The make-or-break experiment is: does frontier-guided selection outperform random k-composition selection? STEPS shows structured selection outperforms random on instruction-following (+4.6 WB-Score over random baselines), providing precedent, but the math domain requires its own validation.

```json
[
  {
    "title": "Skill-DAG-Guided Frontier Synthesis for Mathematical Compositional Generalization",
    "core_problem": "Current LLMs exhibit a persistent compositional ceiling in mathematical reasoning — OMEGA (NeurIPS 2025) shows that RL fine-tuning fails to improve compositional performance (combining distinct skills like GCD + polynomial factoring) even when it substantially improves exploratory generalization (+38pp avg). The question is: can systematically identifying and filling compositional coverage gaps in training data — via skill dependency DAGs and information-theoretic selection — break this ceiling where scaling, RL, and curriculum learning all fail?",
    "opportunity": "Three independent threads have converged to make this tractable now: (1) OMEGA provides both the programmatic skill-composition structure (40 template generators encoding prerequisite relationships) and the controlled evaluation infrastructure (symbolic verification) needed to isolate compositional gains; (2) MASS (ICML 2025) proves skill graphs work for math data operations (46K skills, 1.18M edges, 50-70% efficiency gains), but uses them only for scoring existing data — repurposing the adjacency matrix to find MISSING compositions (zero/low co-occurrence tuples that are DAG-connected) is the unexploited move; (3) Redhardt et al. (NeurIPS 2025 Spotlight) and Chang et al. (ICLR 2026) independently establish that coverage of the compositional task space is the theoretical prerequisite for generalization, but Chang et al. explicitly call for 'future research on targeted data augmentation strategies to maximize k-coverage' — no such method exists for mathematical reasoning.",
    "landscape": "The state of the art divides cleanly into coverage-agnostic synthesis methods that ignore compositional structure, and coverage-aware methods that haven't been applied to math. STAT (NeurIPS 2025) identifies atomic skill gaps and synthesizes single-skill remediation problems — it explicitly decomposes multi-skill problems into single-skill ones, the opposite of compositional training. Agentic Proposing (Feb 2026) achieves 91.6% AIME25 via difficulty-adaptive skill composition with proficiency-inverse sampling, but optimizes for difficulty at the model frontier, not for under-covered compositions in the training distribution. MathFusion (ACL 2025) fuses math problems via sequential/parallel/conditional strategies (+18.0pp), but without skill-graph guidance or coverage targeting. STEPS (Jan 2026) provides the closest methodological framework — marginal structural information maximization over hierarchical skill taxonomies — but validates only on instruction-following benchmarks (WildBench, AlpacaEval, MT-Bench), not mathematical compositional generalization. MindLoom (May 2026) composes 'thought modes' with scarcity reward for diversity but uses iterative sequential application, not DAG-structured skill dependencies, and does not evaluate on OMEGA. The OMEGA benchmark itself (NeurIPS 2025) demonstrates the compositional ceiling across 2-skill compositions (S_A, S_B) but all intervention results use RL (GRPO on 1K problems), with gains limited to semantically similar training-evaluation compositions. No published method has been evaluated on OMEGA's compositional axis with targeted data synthesis interventions.",
    "inspired_by": "Field guide gap #1 (no published method uses skill dependency DAGs to fill compositional frontier gaps in math training data), gap #3 (no method distinguishes difficulty-targeting from coverage-targeting), gap #4 (practical methods to achieve Redhardt et al.'s formal coverage conditions do not exist), untried combination #1 (OMEGA templates as programmatic skill DAG source + STEPS' marginal structural information maximization + frontier-targeted synthesis), and innovation patterns 'Graph/Hierarchy as Selection Principle' + 'Information-Theoretic Selection over Heuristic Sampling' + 'Benchmark-Reveals-Gap-Then-Method-Fills-It'"
  }
]
```

**Venue recommendation:** Since AAAI 2026's deadline has long passed (Aug 2025), target **AAAI 2027** (Montréal, Feb 16-23, 2027; abstract deadline July 21, 2026; full paper deadline July 28, 2026). The ML track is appropriate for this work combining structured data design, skill graphs, and information-theoretic selection for compositional generalization.

Sources:
- [OMEGA: Can LLMs Reason Outside the Box in Math? (NeurIPS 2025)](https://openreview.net/forum?id=gBxpAKxg22)
- [MASS: Mathematical Data Selection via Skill Graphs (ICML 2025)](https://arxiv.org/abs/2503.14917)
- [STEPS: Skill Taxonomy Guided Data Synthesis (Jan 2026)](https://arxiv.org/abs/2601.03676)
- [Scaling Can Lead to Compositional Generalization (NeurIPS 2025 Spotlight)](https://arxiv.org/abs/2507.07207)
- [Can Models Learn Skill Composition from Examples? (NeurIPS 2024)](https://arxiv.org/abs/2409.19808)
- [Characterizing Pattern Matching and Its Limits (ICLR 2026)](https://arxiv.org/abs/2505.20278)
- [STAT: Skill-Targeted Adaptive Training (NeurIPS 2025)](https://arxiv.org/abs/2510.10023)
- [Agentic Proposing: Compositional Skill Synthesis (Feb 2026)](https://arxiv.org/abs/2602.03279)
- [MathFusion: Instruction Fusion (ACL 2025)](https://arxiv.org/abs/2503.16212)
- [MindLoom: Thought Mode Composition (May 2026)](https://arxiv.org/html/2605.21630)
- [MathTrap: Compositional Deficiency (EMNLP 2024)](https://arxiv.org/abs/2405.06680)
- [AgentCoMa: Compositional Benchmark (2025)](https://arxiv.org/abs/2508.19988)
- [Skill-Aware Data Selection (Jan 2026)](https://arxiv.org/abs/2601.10109)
- [KPDDS: Key-Point-Driven Data Synthesis (AAAI 2025)](https://arxiv.org/abs/2403.02333)
- [RV-Syn: Structured Function Library (2025)](https://arxiv.org/abs/2504.20426)
- [How Does RL Post-training Induce Skill Composition? (Dec 2025)](https://arxiv.org/abs/2512.01775)
- [MathMixup: Difficulty-Controllable Synthesis (Jan 2026)](https://arxiv.org/abs/2601.17006)
- [Graph-of-Skills: Dependency-Aware Retrieval (Apr 2026)](https://arxiv.org/abs/2604.05333)
- [DAG-Math: Graph-Guided Mathematical Reasoning (2025)](https://arxiv.org/abs/2510.19842)
- [AAAI-27 Call for Papers](https://aaai.org/conference/aaai/aaai-27/)
- [Mathematical Reasoning in LLMs: Survey (2026)](https://arxiv.org/abs/2605.19723)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9ddc7d2-44f6-4f1b-bd0d-42f3e852681c",
  "isSidechain": false,
  "requestId": "req_011CbWpDHTs1bKW37wyArYC8",
  "type": "assistant",
  "uuid": "ede0d1e2-ac69-4f2d-8dfd-03742f95ae7c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "7647c642-258e-4d28-8a6f-8e19098b0cdb",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118qmwTEUMG8MiF3iYmhQNM",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 83596,
      "output_tokens": 3139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 709,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3139,
          "cache_read_input_tokens": 83596,
          "cache_creation_input_tokens": 709,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 709
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

_source line 256_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-29 (UTC).** Use this when reasoni…",
  "leafUuid": "ede0d1e2-ac69-4f2d-8dfd-03742f95ae7c",
  "sessionId": "7647c642-258e-4d28-8a6f-8e19098b0cdb"
}
```

---


### Runtime record

_source line 257_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate compositional math training data via skill DAGs",
  "sessionId": "7647c642-258e-4d28-8a6f-8e19098b0cdb"
}
```

---
