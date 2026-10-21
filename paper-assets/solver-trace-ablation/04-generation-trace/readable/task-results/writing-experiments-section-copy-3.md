# writing experiments section

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_experiments-section_20260514T185002_result.json`
- **Structured JSON:** [`c85b481744f732b49c3f.json`](../../sessions/c8/c85b481744f732b49c3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```json
{
  "section": "experiments",
  "word_count": {
    "with_markup": 2158,
    "text_only_approx": 1734,
    "budget": 2800
  },
  "citations_needed": [
    "deepseekmath (GRPO)",
    "proofwriter (data)",
    "manheim-goodhart-taxonomy (Goodhart taxonomy)",
    "karwowski-goodhart-rl (Goodhart in RL)"
  ],
  "figures_needed": [
    {
      "id": "fig2_isr_collapse",
      "type": "dual-axis line plot",
      "data": "plan003 (100 steps), plan001-s42-r2 (500 steps), plan016 (1000 steps)",
      "status": "placeholder"
    },
    {
      "id": "fig3_hacking_composition",
      "type": "stacked bar chart",
      "data": "exec-only s42, ISR β=0.1 s42/s43/s44, random β=0.1 3-seed mean, SFT",
      "status": "placeholder"
    }
  ],
  "tables_needed": [
    {
      "id": "tab1_goodhart_landscape",
      "caption": "Goodhart landscape across reward conditions",
      "rows": 6,
      "status": "inline"
    },
    {
      "id": "tab4_beta01_3seed",
      "caption": "ISR vs Random β=0.1 3-seed comparison",
      "rows": 6,
      "status": "inline"
    },
    {
      "id": "tab5_prolog_crosslogic",
      "caption": "Cross-logic transfer (FOL + Prolog)",
      "rows": 9,
      "status": "inline"
    }
  ],
  "notes": [
    "Tab2 (hacking taxonomy detail) folded into §4.5 enumerated list + Fig 3 — saves table float",
    "7 hacking modes listed per Director correction (query-as-fact = mode 7)",
    "Prolog s44 Reviewer correction applied: 0% genuine, query-as-fact gaming",
    "Premise-count-matched 1.06x analysis included; 2.4x language removed",
    "C006 ISR semantic distinction (redundant coding vs metric gaming) addressed in §4.4",
    "Random β=0.1 s43 data missing (was RUNNING) — 3-seed mean uses all 3 seeds per Director data override",
    "~640 words of budget remaining — can expand if reviewer anticipation paragraphs needed"
  ]
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "section": "experiments",
    "word_count": {
      "with_markup": 2158,
      "text_only_approx": 1734,
      "budget": 2800
    },
    "citations_needed": [
      "deepseekmath (GRPO)",
      "proofwriter (data)",
      "manheim-goodhart-taxonomy (Goodhart taxonomy)",
      "karwowski-goodhart-rl (Goodhart in RL)"
    ],
    "figures_needed": [
      {
        "id": "fig2_isr_collapse",
        "type": "dual-axis line plot",
        "data": "plan003 (100 steps), plan001-s42-r2 (500 steps), plan016 (1000 steps)",
        "status": "placeholder"
      },
      {
        "id": "fig3_hacking_composition",
        "type": "stacked bar chart",
        "data": "exec-only s42, ISR β=0.1 s42/s43/s44, random β=0.1 3-seed mean, SFT",
        "status": "placeholder"
      }
    ],
    "tables_needed": [
      {
        "id": "tab1_goodhart_landscape",
        "caption": "Goodhart landscape across reward conditions",
        "rows": 6,
        "status": "inline"
      },
      {
        "id": "tab4_beta01_3seed",
        "caption": "ISR vs Random β=0.1 3-seed comparison",
        "rows": 6,
        "status": "inline"
      },
      {
        "id": "tab5_prolog_crosslogic",
        "caption": "Cross-logic transfer (FOL + Prolog)",
        "rows": 9,
        "status": "inline"
      }
    ],
    "notes": [
      "Tab2 (hacking taxonomy detail) folded into §4.5 enumerated list + Fig 3 — saves table float",
      "7 hacking modes listed per Director correction (query-as-fact = mode 7)",
      "Prolog s44 Reviewer correction applied: 0% genuine, query-as-fact gaming",
      "Premise-count-matched 1.06x analysis included; 2.4x language removed",
      "C006 ISR semantic distinction (redundant coding vs metric gaming) addressed in §4.4",
      "Random β=0.1 s43 data missing (was RUNNING) — 3-seed mean uses all 3 seeds per Director data override",
      "~640 words of budget remaining — can expand if reviewer anticipation paragraphs needed"
    ]
  }
}
```

</details>

---
