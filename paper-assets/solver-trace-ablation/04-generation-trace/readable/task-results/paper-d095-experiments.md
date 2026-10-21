# paper d095 experiments

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d095-experiments_20260515T195541_result.json`
- **Structured JSON:** [`fc542013ad72488332b6.json`](../../sessions/fc/fc542013ad72488332b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits are consistent. Let me verify the key data points against D095:

**Table 1 verification:**
- ISR β=0.1: H7=71% (163/231=70.6%→71), H1=18% (42/231=18.2%→18), N-H=6% (14/231=6.06%→6) ✓
- Random β=0.1: PR=87±8, ISR*=0.117±.04, H7=14% (36/262=13.7%→14), H1=71% (187/262=71.4%→71), N-H=10% (25/262=9.5%→10) ✓
- §-footnote for Random H7 seed dependency ✓

**§4.3 verification:**
- Fisher p=1.3×10⁻³⁹, OR=15.05 ✓
- Random H7 per-seed: 38.3% s43, 0% s42/s44 ✓
- H1 updated to 71% (from 81%) ✓
- PR updated to 87±8 (from 85±6) ✓
- Genuine rate: 6.1% vs 9.5%, Fisher p=0.182, n.s. ✓
- Wilson CI: ISR [3.6%, 9.9%], Random [6.5%, 13.7%] ✓
- Removed "significantly lower" claim, "conservative correction" sentence, and "crowd out genuine proofs" ✓

**§4.4 verification:**
- H7: "70.6% vs 13.7%, Fisher p=1.3×10⁻³⁹" ✓
- H7a: "64.5%, 149/231" ✓
- H7b: "6.1%, 14/231" ✓
- Table 2: H1=71, H7=14, H8=8, N-H=10 for Random; H7=71, N-H=6 for ISR ✓

**Narrative A compliance:**
1. No "H7 is ISR-specific" or "zero under random" ✓
2. "H7a is GRPO-general, seed-dependent; ISR amplifies it ~5x" ✓
3. Per-seed and pooled reported ✓
4. Random H7 single-seed source marked with §-footnote ✓
5. Genuine rate difference reported as n.s. (p=0.182) ✓
6. Correct framing: ISR makes H7 "near-deterministic" vs stochastic ✓

All 10 edits applied across 4 sections. Data matches D095 FINAL values exactly.

---
