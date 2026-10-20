# paper tex recovery A appendix

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_tex_recovery_A_appendix_20260523T051344_result.json`
- **Structured JSON:** [`918e54cb44b69eb89e58.json`](../../sessions/91/918e54cb44b69eb89e58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Zero warnings. All 9 missing sections restored:

| Section | Label | Content |
|---------|-------|---------|
| Representation Analysis | `app:representation` | PR/Fisher/Weight table for 7 variants |
| Layerwise Analysis | `app:layerwise` | PR/Fisher across layers 0-12 with figure |
| Discriminative Subspace Probe | `app:discriminative_probe` | Top-k SVD probe table (3/768 dims sufficient) |
| SVD Necessity Ablation | `app:svd_necessity` | Remove-top-3 vs remove-random-3 ablation |
| Topic Failure Analysis | `app:topic_failure` | Per-turn Fisher table showing why topic DAPT fails |
| OASST2 Adaptation | `app:oasst2` | OASST2 benign adaptation curve |
| Dual-OOD Detection | `app:dual_ood` | Estimated dual-OOD F1 under 5 benign conditions |
| Confidence Analysis | `app:confidence` | ToxicChat high-confidence FP analysis |
| Truncation Analysis | `app:truncated` | Full vs last-turn-only F1 comparison |

File: 693 → 935 lines. PDF: 25 pages, zero undefined references/warnings. Also fixed two broken cross-references (`tab:benign_curve` → `tab:wildchat_fpr`, `sec:benign` → `sec:benign_shift`).

---
