# Experiment Progress Snapshot — 2026-05-27 18:20 UTC

## Summary
- **12 experiments** tracked across 4 servers
- **2 completed** , **1 crashed** , **9 running**

## Progress Table

| exp_id | server:GPU | progress | ETA (UTC) | note |
|--------|-----------|------|-----------|------|
| eval_openvla_l2norm_k085_object_seed42 | westd-27271:GPU1 | T10/10 Ep10/50 | ~18:35 | almost done |
| eval_openvla_random_k095_long_seed42_v2 | westd-38929:GPU0 | T5/10 start | ~23:15 | Long suite OV, ~1.0 eps/min |
| eval_openvla_l2norm_k095_long_seed42 | westd-38929:GPU1 | T9/10 Ep20/50 | ~19:55 | cliff curve key |
| eval_openvla_l2norm_k075_long_seed42_v2 | westd-38929:GPU2 | T8/10 Ep10/50 | ~21:35 | cliff curve key |
| eval_openvla_attn_k095_long_seed42 | westd-38929:GPU3 | T9/10 Ep30/50 | ~19:45 | cliff curve key |
| eval_pi05_random_k09_long_seed42_strict_v2 | westd-41074:GPU0 | T3/10 Ep10/50 | ~20:20 | cumul SR=32% (T0-T2), tracking k=0.9 anomaly |
| eval_pi05_random_k05_long_seed42_strict_w41_v2 | westd-41074:GPU1 | T3/10 Ep40/50 | ~19:50 | normal |
| eval_pi05_random_k095_long_seed42_strict | westd-41074:GPU2 | DONE | — | SR=60.6%, EXIT_CODE=0 |
| eval_pi05_l2norm_k085_long_seed42_strict_w41 | westd-41074:GPU3 | CRASHED | — | Network unreachable loading tokenizer, needs HF_HUB_OFFLINE=1 restart |
| eval_pi05_random_k07_long_seed42_strict_v2 | cqa1-33015:GPU0 | T4/10 Ep20/50 | ~20:45 | ~27min/task |
| eval_pi05_random_k05_long_seed42_strict | cqa1-33015:GPU1 | T3/10 Ep30/50 | ~21:05 | ~27min/task |
| eval_pi05_l2norm_k085_long_seed42_strict | cqa1-33015:GPU2 | T6/10 Ep20/50 | ~19:30 | SR 89.7% through T0-T5, excellent |
| eval_openvla_attn_k05_goal_seed42_v3 | cqa1-33015:GPU3 | DONE | — | SR=42.8% (214/500), Goal Attn k=0.5 gap filled |

## Key Observations

### Completed
1. **pi05_random_k095_long** (westd-41074:GPU2): SR=60.6%
2. **openvla_attn_k05_goal_v3** (cqa1-33015:GPU3): SR=42.8%, last Goal suite gap filled

### Needs Action
3. **pi05_l2norm_k085_long_w41** (westd-41074:GPU3): crashed on startup — `httpx.ConnectError: [Errno 101] Network is unreachable` loading `google/paligemma-3b-pt-224` tokenizer. **Needs HF_HUB_OFFLINE=1 + cached tokenizer to restart.**

### Watch Items
4. **pi05_random_k09** (westd-41074:GPU0): first 3 tasks cumulative SR=32.0% (48/150), consistent with previously observed k=0.9 ~32% anomaly — reproducing
5. **openvla_random_k095_long** (westd-38929:GPU0): latest ETA ~23:15 UTC, slowest experiment but still well before deadline (05-28 08:00 UTC)
6. **pi05_l2norm_k085** (cqa1-33015:GPU2): SR=89.7% through 6 tasks, outstanding performance

### ETA Distribution
- 18:35 UTC: l2norm_k085_object (westd-27271)
- 19:30-20:00 UTC: 4 experiments finish (l2norm_k095_long, attn_k095_long, l2norm_k085_cqa1, random_k05_w41)
- 20:20-21:05 UTC: 3 experiments finish (random_k09, random_k07, random_k05_cqa1)
- 21:35 UTC: l2norm_k075_long (westd-38929)
- 23:15 UTC: random_k095_long_v2 (westd-38929) — last to finish
- All before deadline 05-28 08:00 UTC
