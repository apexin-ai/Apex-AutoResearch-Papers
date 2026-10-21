# writing paper experiments

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_paper-experiments_20260514T185009_result.json`
- **Structured JSON:** [`fc29c420098b26c3db13.json`](../../sessions/fc/fc29c420098b26c3db13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Written to `artifacts/_project/paper/experiments.tex`. JSON report:

```json
{
  "section": "Experiments (Section 4)",
  "venue": "EMNLP 2026 Main",
  "word_count_estimate": 2850,
  "artifact_id": "art_20260514_b77022",
  "path": "artifacts/_project/paper/experiments.tex",

  "structure": {
    "4.1_Setup": "~220 words. Qwen3-4B, GRPO K=8, 500/1000 steps, FOLIO 500/100 split, 5 reward conditions, 3 seeds.",
    "4.2_ISR_as_Diagnostic": "~700 words. ISR collapse 0.642→0.132→0.003 (Fig2), 3-seed divergence (Fig3), SFT baseline 92.9% genuine.",
    "4.3_Meta_Level_Goodhart": "~900 words. Tab4 (3-seed β=0.1), H7 ISR-specific 64.5% vs 0%, premise-count-matched 1.06×, GRPO-universal H1, β=0.3 collapse, Tab1 landscape.",
    "4.4_Cross_Logic_Transfer": "~550 words. Prolog exec-only ISR<0.1 (Tab5), 3/3 seeds gaming 0% genuine (Fig4), classifier blind spot.",
    "4.5_Hacking_Taxonomy": "~480 words. 7 modes (Tab2), H1 universal, mode determined by reward, condition-specific associations."
  },

  "tables": {
    "Tab1_landscape": "table* — Goodhart landscape: 8 conditions, PR/ISR/H7/H1/Genuine/Phase",
    "Tab2_taxonomy": "table* — 7 hacking modes × 5 condition groups with prevalence %",
    "Tab4_beta01": "table — 6 rows (ISR×3 + Random×3), per-seed PR/ISR/H7/H1/Genuine",
    "Tab5_prolog": "table — 6 rows (exec×3 + STA×3), PR/ISR/functional H7/Genuine",
    "inline_premise_matched": "inline 2×2 table showing 1.06× ratio"
  },

  "figures": {
    "Fig2": "ISR collapse trajectory placeholder (dual y-axis, steps vs PR/ISR)",
    "Fig3": "Hacking composition stacked bar placeholder (§4.2)",
    "Fig4": "FOL vs Prolog grouped bar placeholder (§4.4)"
  },

  "hard_constraints_verified": {
    "no_2.4x_claim": true,
    "prolog_s44_gaming_not_genuine": true,
    "exec_only_s42_not_healthy": "reported as 87.1% H1, 12.9% genuine",
    "taxonomy_7_modes": true,
    "premise_count_matched_1.06x": true,
    "ISR_s44_genuine_FN_noted": "footnote in Tab4"
  },

  "data_sources": {
    "registry_experiments": ["plan003", "plan001-s42/s43/s44", "plan016", "plan002-b01-s42/s43/s44", "plan018-s42/s43/s44", "plan002-b03", "plan017", "plan009-sft", "plan006-prolog-exec/sta", "plan013"],
    "project_files": ["memory.md", "paper_framing.md"],
    "method_section": "method.tex (notation/citation consistency)"
  }
}
```

**Key changes from the existing draft:**
- "ProofWriter" → "FOLIO" throughout
- ISR s42 genuine: 30.9% → 32.1% (residual = 81−13−42, per task spec convention)
- Fig3 moved from §4.5 to §4.2
- Added Fig4 (FOL vs Prolog) placeholder in §4.4
- Added Tab2 (hacking taxonomy matrix) as table* in §4.5
- Prolog table uses proved-only ISR for ISR-reward rows (1.000/0.185/0.912)
- All Goodhart framing updated to D051 conclusions (no "sweet spot", no "2.4x")
- Convex random included in Tab1 for completeness

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "section": "Experiments (Section 4)",
    "venue": "EMNLP 2026 Main",
    "word_count_estimate": 2850,
    "artifact_id": "art_20260514_b77022",
    "path": "artifacts/_project/paper/experiments.tex",
    "structure": {
      "4.1_Setup": "~220 words. Qwen3-4B, GRPO K=8, 500/1000 steps, FOLIO 500/100 split, 5 reward conditions, 3 seeds.",
      "4.2_ISR_as_Diagnostic": "~700 words. ISR collapse 0.642→0.132→0.003 (Fig2), 3-seed divergence (Fig3), SFT baseline 92.9% genuine.",
      "4.3_Meta_Level_Goodhart": "~900 words. Tab4 (3-seed β=0.1), H7 ISR-specific 64.5% vs 0%, premise-count-matched 1.06×, GRPO-universal H1, β=0.3 collapse, Tab1 landscape.",
      "4.4_Cross_Logic_Transfer": "~550 words. Prolog exec-only ISR<0.1 (Tab5), 3/3 seeds gaming 0% genuine (Fig4), classifier blind spot.",
      "4.5_Hacking_Taxonomy": "~480 words. 7 modes (Tab2), H1 universal, mode determined by reward, condition-specific associations."
    },
    "tables": {
      "Tab1_landscape": "table* — Goodhart landscape: 8 conditions, PR/ISR/H7/H1/Genuine/Phase",
      "Tab2_taxonomy": "table* — 7 hacking modes × 5 condition groups with prevalence %",
      "Tab4_beta01": "table — 6 rows (ISR×3 + Random×3), per-seed PR/ISR/H7/H1/Genuine",
      "Tab5_prolog": "table — 6 rows (exec×3 + STA×3), PR/ISR/functional H7/Genuine",
      "inline_premise_matched": "inline 2×2 table showing 1.06× ratio"
    },
    "figures": {
      "Fig2": "ISR collapse trajectory placeholder (dual y-axis, steps vs PR/ISR)",
      "Fig3": "Hacking composition stacked bar placeholder (§4.2)",
      "Fig4": "FOL vs Prolog grouped bar placeholder (§4.4)"
    },
    "hard_constraints_verified": {
      "no_2.4x_claim": true,
      "prolog_s44_gaming_not_genuine": true,
      "exec_only_s42_not_healthy": "reported as 87.1% H1, 12.9% genuine",
      "taxonomy_7_modes": true,
      "premise_count_matched_1.06x": true,
      "ISR_s44_genuine_FN_noted": "footnote in Tab4"
    },
    "data_sources": {
      "registry_experiments": [
        "plan003",
        "plan001-s42/s43/s44",
        "plan016",
        "plan002-b01-s42/s43/s44",
        "plan018-s42/s43/s44",
        "plan002-b03",
        "plan017",
        "plan009-sft",
        "plan006-prolog-exec/sta",
        "plan013"
      ],
      "project_files": [
        "memory.md",
        "paper_framing.md"
      ],
      "method_section": "method.tex (notation/citation consistency)"
    }
  }
}
```

</details>

---
