# paper seed level fill

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_seed_level_fill_20260523T053412_result.json`
- **Structured JSON:** [`ea735eec84e605b9d51f.json`](../../sessions/ea/ea735eec84e605b9d51f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No "Placeholder" strings remain, and the seed-level table (lines 924-928) has no "--" placeholders. The remaining "--" markers elsewhere are legitimate (FITD insufficient conversation length, etc.).

Table filled. Per-seed F1 values for `tab:seed_level`:

| Variant | DD s42 | DD s123 | DD s456 | AA s42 | AA s123 | AA s456 |
|---------|--------|---------|---------|--------|---------|---------|
| 9-class | 1.000 | 1.000 | .990 | .990 | .935 | .990 |
| Binary | 1.000 | 1.000 | 1.000 | .981 | .990 | 1.000 |
| Scrambled | .990 | 1.000 | 1.000 | .891 | .990 | .971 |
| MLM-only | 1.000 | .990 | .751 | .971 | .925 | .784 |
| Vanilla | .285 | .305 | .348 | .258 | .258 | .258 |

Values sourced from registry experiments (plan_002, plan_017_mlm_control, exp2, vanilla_multiseed_dd_ood) and corroborated against a previously-filled version found in the session transcript. The LaTeX compilation error ("Counter too large") is pre-existing and unrelated to this change.

---
