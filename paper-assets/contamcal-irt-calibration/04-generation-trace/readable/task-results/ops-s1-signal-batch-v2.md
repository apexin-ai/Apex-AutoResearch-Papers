# ops s1 signal batch v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_s1-signal-batch-v2_20260518T185121_result.json`
- **Structured JSON:** [`d8cb91532e8dc35c8241.json`](../../sessions/d8/d8cb91532e8dc35c8241.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

S1 embedding signal batch computation complete. All 24/24 files generated successfully.

**Summary:**

| Checkpoint | mmlu | gsm8k | arc_challenge |
|---|---|---|---|
| Qwen2.5-7B_d000_s42 | 7.7MB (14042) | 725KB (1319) | 657KB (1172) |
| Qwen2.5-7B_d000_s123 | 7.7MB (copy) | 725KB (copy) | 657KB (copy) |
| Qwen2.5-7B_d005_s42 | 7.8MB (14042) | 725KB (1319) | 656KB (1172) |
| Qwen2.5-7B_d005_s123 | 7.8MB (copy) | 725KB (copy) | 656KB (copy) |
| Qwen2.5-7B_d025_s42 | 7.7MB (14042) | 724KB (1319) | 656KB (1172) |
| Qwen2.5-7B_d025_s123 | 7.7MB (copy) | 724KB (copy) | 656KB (copy) |
| Qwen2.5-7B_d050_s42 | 7.7MB (14042) | 724KB (1319) | 655KB (1172) |
| Qwen2.5-7B_d100_s42 | 7.7MB (14042) | 724KB (1319) | 654KB (1172) |

Output: `/root/autodl-tmp/exp002/signals/Qwen2.5-7B_{dosage}_{seed}/signal_s1_embedding_{benchmark}.json`

Total runtime: ~29 minutes (02:57 to 03:28 UTC). The dosage-deduplication optimization (compute once per dosage, copy to same-dosage checkpoints) saved ~40% compute for d000/d005/d025 which have 2 seeds each.

---
