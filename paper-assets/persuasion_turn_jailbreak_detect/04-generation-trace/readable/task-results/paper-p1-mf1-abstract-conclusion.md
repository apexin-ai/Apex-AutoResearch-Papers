# paper p1 mf1 abstract conclusion

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_p1-mf1-abstract-conclusion_20260523T115020_result.json`
- **Structured JSON:** [`cef711812efda80239d2.json`](../../sessions/ce/cef711812efda80239d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both files updated. Summary:

**Abstract** (168 words, ≤200 limit):
- Dual-pillar structure: synthetic findings ("On synthetic data, ...") + ToxicChat reversal ("On human-authored single-turn data (ToxicChat), ...")
- Added "(attack-side OOD, IID benign upper bound)" qualifier
- "benefits substantially from domain adaptation at base model scale" replaces "requires domain adaptation"
- "at base scale (125M--184M parameters)" qualifier added
- Key numbers kept: F1=0.97–1.0 vs 0.26–0.31, F1=0.504, F1 0.837 vs 0.596, FPR 58–68%→0–1.5%, 24.3×
- ToxicChat reversal promoted to main finding

**Conclusion** (4 paragraphs replacing 1 sentence):
1. Synthetic data findings: classification DAPT recovers OOD, template robust (|d|≤0.14), mixed-LLM degrades, benign FPR fix, 24.3× speedup
2. ToxicChat reversal: MLM 0.837 vs 0.596 (24.1pp), condition-specific
3. Boundaries: 355M counterproductive (AA=1.000 vs 0.946), length sensitivity
4. Methodological contribution: reusable 4-axis ablation framework

Discussion/Limitations/Ethics unchanged.

---
