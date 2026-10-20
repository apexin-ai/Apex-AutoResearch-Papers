# paper introduction draft

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_introduction-draft_20260514T080546_result.json`
- **Structured JSON:** [`5931364cf3ef452027ab.json`](../../sessions/59/5931364cf3ef452027ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Introduction drafted and saved to `artifacts/_project/paper/introduction.tex`.

Structure:
1. **Opening** — KV cache pressure + two compression axes + compound sparsity problem
2. **Gap** — prior work treats interaction as phase-invariant; problematic for reasoning models with heterogeneous generation
3. **Finding** — severity gradient under importance eviction, monotonically increasing with sparsity; specific numbers from DeepSeek (median diff 0.39→14.59, Cohen's d 0.44→0.80) + Qwen replication (~1/5 magnitude); random eviction 4/4 FAIL as control
4. **Mechanism** — entropy-discrimination collapse (one paragraph, pointers to §6)
5. **Contributions** — 3 items: phase–strategy interaction, monotonic dose-response + cross-model replication, mechanism
6. **Roadmap** — section pointers

Calibration notes:
- No "consistently" — reports "two models" and "50-problem subset" without overgeneralizing
- Uses median difference + Cohen's d (not ratio metrics, per D033)
- Bonferroni p<0.005 (per D032), not the deprecated p<0.0001
- Frames as "emergent phase-strategy interaction" (per D015 constraint)
- Does not claim importance is broken; frames as phase-dependent discriminability degradation
- Random control explicitly described as null result (4/4 FAIL)
- Qwen s015 non-significance not highlighted in intro (appropriate — details in Results)
- Cross-model claim scoped to "Qwen2 architecture family," not cross-architecture

---
