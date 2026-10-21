## Variant-Level Aggregation Results (n=48, AND rule)

Script: /home/sonny/exec-sim-repair-verifier/aggregate_variant_level.py
JSON: /home/sonny/exec-sim-repair-verifier/artifacts/variant_level_aggregation.json

| Model | Form | Seed | Per-test Acc (n=9784) | Variant Acc (n=48) |
|---|---|---|---|---|
| DeepSeek-6.7B TRAJ s42 | TRAJ | 42 | N/A | 81.25% |
| DeepSeek-6.7B TRAJ s123 | TRAJ | 123 | N/A | 75.00% |
| Qwen3-8B CLS s42 | CLS | 42 | 84.48% | 72.92% |
| Qwen3-8B CLS s123 | CLS | 123 | 85.60% | 81.25% |
| Qwen3-4B CLS s42 | CLS | 42 | 76.92% | 68.75% |
| DeepSeek CLS s123 (seq8192) | CLS | 123 | 74.93% | 56.25% |
| DeepSeek CLS s123 (seq2048) | CLS | 123 | 82.62% | 72.92% |
| Qwen3-8B CWM s42 | CWM | 42 | 65.17% | 52.08% |
| DeepSeek CWM s123 | CWM | 123 | N/A | 47.92%* |
| DeepSeek CWM s42 | CWM | 42 | N/A | 47.92%* |

Majority baseline: 54.17% (variant) vs 72.96% (per-test)
*incomplete predictions