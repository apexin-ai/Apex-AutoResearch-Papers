# Exp 3: 70B Few-NERD Count Curves Status

**Server:** westd-24295 | **Session:** exp3_70b | **Checked:** 2026-05-17 19:04 UTC

## Status: RUNNING

## Configuration
- Model: llama-3.1-70b-instruct-fp8 (TP=2, vLLM v0.21.0)
- Dataset: Few-NERD (1000 test samples)
- Count levels: [2, 6, 12, 22, 44, 66] x 25 batches = 150 total
- Started: 2026-05-17 18:24

## Progress: 66/150 batches (44%)

| Count Level | Batches Done | Status |
|-------------|-------------|--------|
| count_12 | 25/25 | Done |
| count_2 | 25/25 | Done |
| count_22 | 16/25 | In progress |
| count_44 | 0/25 | Pending |
| count_6 | 0/25 | Pending |
| count_66 | 0/25 | Pending |

## Timing
- count_12: ~36s/batch avg
- count_2: ~27s/batch avg
- count_22: ~41s/batch avg
- Elapsed: ~40 min for 66 batches
- ETA remaining: ~50-60 min (est. completion ~19:55-20:05 UTC)

## GPU Status
| GPU | Memory Used | Memory Total | Utilization |
|-----|------------|-------------|-------------|
| 0 | 91,399 MiB | 97,887 MiB | 100% |
| 1 | 91,399 MiB | 97,887 MiB | 100% |

## Notes
- No errors observed
- HF_HUB_OFFLINE=1 in effect
- Results file not yet written (will be generated after all 150 batches complete)
