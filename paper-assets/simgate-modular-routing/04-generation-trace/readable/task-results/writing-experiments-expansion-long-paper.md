# writing experiments expansion long paper

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_experiments-expansion-long-paper_20260516T190419_result.json`
- **Structured JSON:** [`a2402bb39c40bbe03cea.json`](../../sessions/a2/a2402bb39c40bbe03cea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```json
{
  "task": "Expand Experiments section to ~3 pages",
  "files_modified": [
    "docs/paper/experiments.tex",
    "docs/paper/discussion.tex"
  ],
  "files_not_modified": [
    "docs/paper/method.tex",
    "docs/paper/introduction.tex"
  ],
  "structure_changes": {
    "experiments.tex": {
      "old": ["§4.1 Death Avoidance Decomposition", "§4.2 Baselines", "§4.3 Router Training as Diagnostic"],
      "new": [
        "§4.1 Death Avoidance Decomposition (+SCI paragraph, +Bootstrap CI paragraph)",
        "§4.2 Multi-Model Validation (new, Llama replication from old §4.3 last line)",
        "§4.3 Cross-Domain Negative Contrast: MATH (new, migrated from discussion.tex)",
        "§4.4 Baselines (unchanged, renumbered)",
        "§4.5 Router Training as Diagnostic Probe (trimmed Llama sentence, renumbered)"
      ]
    },
    "discussion.tex": {
      "removed": "MATH content from Cross-environment evidence paragraph",
      "kept": ["Cross-environment evidence (ALFWorld only)", "Penalty sensitivity", "Implications for router design", "Framework applicability", "Modality heterogeneity"],
      "added_ref": "\\S\\ref{sec:math-contrast} back-reference to new experiments section"
    }
  },
  "new_labels": {
    "sec:cross-model": "§4.2 Multi-Model Validation",
    "sec:math-contrast": "§4.3 Cross-Domain Negative Contrast: MATH"
  },
  "content_added": {
    "SCI_analysis": "Gini=0.2147, top-1/2/3 CR=14.3/27.5/39.8%, 10/11 tasks DAF=100%, find-non-living-thing exception",
    "bootstrap_CI": "B=10000, aggregate DAF CI [81.6%, 98.8%], 10/11 per-task Δ>0, chemistry-mix crosses zero",
    "multi_model": "Llama-3.1-8B-Instruct, 7 tasks, N=70, int_preferred=0, death rates 34.3% vs 0%, mechanism verification framing",
    "MATH_contrast": "N=300, Level 4-5, 81.0% vs 76.7% (+4.3pp, p=0.079), label inversion 30:17, Level 5 > Level 4, negative control framing"
  },
  "constraints_respected": {
    "no_ALFWorld_DAF_numbers": true,
    "MATH_directional_trend_wording": true,
    "no_method_tex_modification": true,
    "no_introduction_tex_modification": true,
    "no_fabricated_numbers": true
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "task": "Expand Experiments section to ~3 pages",
    "files_modified": [
      "docs/paper/experiments.tex",
      "docs/paper/discussion.tex"
    ],
    "files_not_modified": [
      "docs/paper/method.tex",
      "docs/paper/introduction.tex"
    ],
    "structure_changes": {
      "experiments.tex": {
        "old": [
          "§4.1 Death Avoidance Decomposition",
          "§4.2 Baselines",
          "§4.3 Router Training as Diagnostic"
        ],
        "new": [
          "§4.1 Death Avoidance Decomposition (+SCI paragraph, +Bootstrap CI paragraph)",
          "§4.2 Multi-Model Validation (new, Llama replication from old §4.3 last line)",
          "§4.3 Cross-Domain Negative Contrast: MATH (new, migrated from discussion.tex)",
          "§4.4 Baselines (unchanged, renumbered)",
          "§4.5 Router Training as Diagnostic Probe (trimmed Llama sentence, renumbered)"
        ]
      },
      "discussion.tex": {
        "removed": "MATH content from Cross-environment evidence paragraph",
        "kept": [
          "Cross-environment evidence (ALFWorld only)",
          "Penalty sensitivity",
          "Implications for router design",
          "Framework applicability",
          "Modality heterogeneity"
        ],
        "added_ref": "\\S\\ref{sec:math-contrast} back-reference to new experiments section"
      }
    },
    "new_labels": {
      "sec:cross-model": "§4.2 Multi-Model Validation",
      "sec:math-contrast": "§4.3 Cross-Domain Negative Contrast: MATH"
    },
    "content_added": {
      "SCI_analysis": "Gini=0.2147, top-1/2/3 CR=14.3/27.5/39.8%, 10/11 tasks DAF=100%, find-non-living-thing exception",
      "bootstrap_CI": "B=10000, aggregate DAF CI [81.6%, 98.8%], 10/11 per-task Δ>0, chemistry-mix crosses zero",
      "multi_model": "Llama-3.1-8B-Instruct, 7 tasks, N=70, int_preferred=0, death rates 34.3% vs 0%, mechanism verification framing",
      "MATH_contrast": "N=300, Level 4-5, 81.0% vs 76.7% (+4.3pp, p=0.079), label inversion 30:17, Level 5 > Level 4, negative control framing"
    },
    "constraints_respected": {
      "no_ALFWorld_DAF_numbers": true,
      "MATH_directional_trend_wording": true,
      "no_method_tex_modification": true,
      "no_introduction_tex_modification": true,
      "no_fabricated_numbers": true
    }
  }
}
```

</details>

---
