# writing paper method

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_paper-method_20260514T184910_result.json`
- **Structured JSON:** [`622df3b75a446f7097e1.json`](../../sessions/62/622df3b75a446f7097e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Method section drafted and registered. Output report:

```json
{
  "section": "Method (Section 3)",
  "word_count": 1010,
  "file": "artifacts/_project/paper/method.tex",
  "citations_needed": [
    "mccune2010prover9 (Prover9)",
    "folio (FOLIO dataset)",
    "deepseekmath (GRPO)",
    "demillo1978 (mutation testing origin)",
    "jia-harman-survey (mutation testing survey)",
    "shapley-lime (feature attribution — placeholder, split into specific Shapley/LIME cites)"
  ],
  "figures_needed": [
    "fig:sta_overview (STA protocol overview, referenced in §3.3)"
  ],
  "tables_needed": [],
  "algorithms": [
    "Algorithm 1: Solver Trace Ablation (STA) — requires algorithmic package"
  ],
  "notes": [
    "Word count ~1010, under the 1200 budget — leaves room for reviewer-requested expansions",
    "Hacking taxonomy lists all 7 modes (H1, H7, H3, tautological collapse, repetition collapse, contradiction explosion, query-as-fact gaming); writing_plan said 6 but actual count is 7 per task spec",
    "Premise count bias discussed in §3.4 as explicit paragraph — critical for Claim 2 interpretation",
    "Convex formulation mentioned as discarded with rationale (penalty effect), not as active condition",
    "ISR explicitly scoped as syntactic necessity, not semantic faithfulness — preempts reviewer concern",
    "LaTeX needs: algorithm2e or algorithmic package, amsmath for equations",
    "\\cite{shapley-lime} is a placeholder — split into actual Shapley (1953) and LIME (Ribeiro et al. 2016) citations"
  ]
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "section": "Method (Section 3)",
    "word_count": 1010,
    "file": "artifacts/_project/paper/method.tex",
    "citations_needed": [
      "mccune2010prover9 (Prover9)",
      "folio (FOLIO dataset)",
      "deepseekmath (GRPO)",
      "demillo1978 (mutation testing origin)",
      "jia-harman-survey (mutation testing survey)",
      "shapley-lime (feature attribution — placeholder, split into specific Shapley/LIME cites)"
    ],
    "figures_needed": [
      "fig:sta_overview (STA protocol overview, referenced in §3.3)"
    ],
    "tables_needed": [],
    "algorithms": [
      "Algorithm 1: Solver Trace Ablation (STA) — requires algorithmic package"
    ],
    "notes": [
      "Word count ~1010, under the 1200 budget — leaves room for reviewer-requested expansions",
      "Hacking taxonomy lists all 7 modes (H1, H7, H3, tautological collapse, repetition collapse, contradiction explosion, query-as-fact gaming); writing_plan said 6 but actual count is 7 per task spec",
      "Premise count bias discussed in §3.4 as explicit paragraph — critical for Claim 2 interpretation",
      "Convex formulation mentioned as discarded with rationale (penalty effect), not as active condition",
      "ISR explicitly scoped as syntactic necessity, not semantic faithfulness — preempts reviewer concern",
      "LaTeX needs: algorithm2e or algorithmic package, amsmath for equations",
      "\\cite{shapley-lime} is a placeholder — split into actual Shapley (1953) and LIME (Ribeiro et al. 2016) citations"
    ]
  }
}
```

</details>

---
