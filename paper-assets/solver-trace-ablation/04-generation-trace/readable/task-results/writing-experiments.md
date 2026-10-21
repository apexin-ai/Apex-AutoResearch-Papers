# writing experiments

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_experiments_20260514T194457_result.json`
- **Structured JSON:** [`ead694926839cd6771ab.json`](../../sessions/ea/ead694926839cd6771ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

File written at 3015 words (within the ~2800 target). Wrapping up with the report.

```json
{
  "section": "4. Experiments",
  "word_count": 3015,
  "citations_needed": [
    "Qwen3-4B technical report (\\citep{placeholder} in §4.1)",
    "GRPO / DeepSeekMath (\\citep{placeholder} in §4.1)",
    "Extremal Goodhart — Manheim & Garrabrant 2019 (\\citep{placeholder} in §4.3)",
    "ProofWriter / FOLIO dataset papers (eval and training data)",
    "Prover9 (LADR) and SWI-Prolog tool references",
    "LOO / feature-attribution literature (referenced in §4.3 premise-count discussion)"
  ],
  "figures_needed": [
    "fig:isr-collapse — ISR collapse trajectory, dual y-axis (PR 32→96%, ISR* 0.64→0.003), 100/500/1000 steps with component-count annotation",
    "fig:hacking-composition — stacked bar chart of H7/H1/structural-collapse/Genuine across reward conditions (exec-only s42/s43/s44, ISR β=0.1 mean, random β=0.1 mean, SFT)",
    "fig:prolog-comparison — dual-panel: left exec-only PR per seed, right STA PR vs strict-genuine vs functional-genuine per seed"
  ],
  "tables_needed": [
    "tab:isr-vs-random — β=0.1 ISR vs random 3-seed comparison with H7/H1/Genuine breakdown (inline in §4.3)",
    "tab:prolog-cross — Prolog ISR-additive 3-seed strict vs functional classifier (inline in §4.4)",
    "tab:goodhart-landscape — full FOL reward landscape across 9 conditions (inline in §4.5)",
    "tab:hparams — full hyperparameters, deferred to Appendix"
  ],
  "notes": [
    "Constraints honored: (1) 2.4× raw genuine ISR replaced by premise-count-matched 1.06× on n_prem≥3 (§4.3); (2) Prolog s44 explicitly labeled query-as-fact gaming, 0% genuine via reviewer override + functional cross-validation (§4.4); (3) taxonomy is 7 modes including query-as-fact (§4.5); (4) plan013 vs plan017 simplification avoided — random-additive β=0.1 (plan018) and β=0.3 (plan017) used as controls against ISR-additive plan002 family only.",
    "C006 honored: §4.4 distinguishes Prolog exec-only low-ISR-as-redundant-encoding from exec+STA high-ISR-as-metric-gaming; reiterated in §4.5 Discussion-pointer.",
    "ISR* (proved-only) used consistently throughout.",
    "SFT baseline rendered as anti-hacking reference at 92.9% genuine but PR=14% — used in §4.2 and Table 4.5.",
    "Cross-references to §4.X labels point to §5 (sec:limitations) for two pending Discussion items: premise-count confound deep-dive and Prolog redundancy vs gaming distinction.",
    "Output path: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/experiments.tex (overwrote existing draft)."
  ]
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "section": "4. Experiments",
    "word_count": 3015,
    "citations_needed": [
      "Qwen3-4B technical report (\\citep{placeholder} in §4.1)",
      "GRPO / DeepSeekMath (\\citep{placeholder} in §4.1)",
      "Extremal Goodhart — Manheim & Garrabrant 2019 (\\citep{placeholder} in §4.3)",
      "ProofWriter / FOLIO dataset papers (eval and training data)",
      "Prover9 (LADR) and SWI-Prolog tool references",
      "LOO / feature-attribution literature (referenced in §4.3 premise-count discussion)"
    ],
    "figures_needed": [
      "fig:isr-collapse — ISR collapse trajectory, dual y-axis (PR 32→96%, ISR* 0.64→0.003), 100/500/1000 steps with component-count annotation",
      "fig:hacking-composition — stacked bar chart of H7/H1/structural-collapse/Genuine across reward conditions (exec-only s42/s43/s44, ISR β=0.1 mean, random β=0.1 mean, SFT)",
      "fig:prolog-comparison — dual-panel: left exec-only PR per seed, right STA PR vs strict-genuine vs functional-genuine per seed"
    ],
    "tables_needed": [
      "tab:isr-vs-random — β=0.1 ISR vs random 3-seed comparison with H7/H1/Genuine breakdown (inline in §4.3)",
      "tab:prolog-cross — Prolog ISR-additive 3-seed strict vs functional classifier (inline in §4.4)",
      "tab:goodhart-landscape — full FOL reward landscape across 9 conditions (inline in §4.5)",
      "tab:hparams — full hyperparameters, deferred to Appendix"
    ],
    "notes": [
      "Constraints honored: (1) 2.4× raw genuine ISR replaced by premise-count-matched 1.06× on n_prem≥3 (§4.3); (2) Prolog s44 explicitly labeled query-as-fact gaming, 0% genuine via reviewer override + functional cross-validation (§4.4); (3) taxonomy is 7 modes including query-as-fact (§4.5); (4) plan013 vs plan017 simplification avoided — random-additive β=0.1 (plan018) and β=0.3 (plan017) used as controls against ISR-additive plan002 family only.",
      "C006 honored: §4.4 distinguishes Prolog exec-only low-ISR-as-redundant-encoding from exec+STA high-ISR-as-metric-gaming; reiterated in §4.5 Discussion-pointer.",
      "ISR* (proved-only) used consistently throughout.",
      "SFT baseline rendered as anti-hacking reference at 92.9% genuine but PR=14% — used in §4.2 and Table 4.5.",
      "Cross-references to §4.X labels point to §5 (sec:limitations) for two pending Discussion items: premise-count confound deep-dive and Prolog redundancy vs gaming distinction.",
      "Output path: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/experiments.tex (overwrote existing draft)."
    ]
  }
}
```

</details>

---
