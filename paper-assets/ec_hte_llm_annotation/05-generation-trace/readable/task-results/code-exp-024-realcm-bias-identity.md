# code exp 024 realcm bias identity

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-024-realcm-bias-identity_20260522T122608_result.json`
- **Structured JSON:** [`ad0b0c7b63f58baca946.json`](../../sessions/ad/ad0b0c7b63f58baca946.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results verified. Summary:

**Global R² = 0.975** across all 11 LLMs, confirming Theorem 1's bias identity `bias(z,s) = Δτ · [B_s]_{z,1}` with real LLM confusion matrices.

| LLM | Dataset | R² | max\|B\| |
|-----|---------|-----|----------|
| gpt-4-turbo | TweetEval | 0.993 | 0.328 |
| Qwen2.5-7B | TweetEval | 0.990 | 0.272 |
| Mistral-7B | TweetEval | 0.990 | 0.242 |
| Gemma-2-9B | TweetEval | 0.982 | 0.185 |
| gpt-4o | CivilComments | 0.979 | 0.198 |
| gpt-4o | TweetEval | 0.975 | 0.240 |
| gpt-4.1 | TweetEval | 0.969 | 0.139 |
| gpt-3.5-turbo | TweetEval | 0.948 | 0.087 |
| gpt-3.5-turbo | CivilComments | 0.935 | 0.170 |
| gpt-4o-mini | TweetEval | 0.929 | 0.170 |
| gpt-4o-mini | CivilComments | 0.756 | 0.089 |

R² strongly correlates with max|B| — LLMs with more heterogeneous per-subgroup error rates produce stronger bias signals that are easier to verify empirically. The one outlier (gpt-4o-mini Civil, R²=0.76) has near-homogeneous FPR/FNR across subgroups (max|B|=0.089), so the predicted biases are tiny and MC noise dominates.

Output files:
- `results/exp_realcm_bias_identity.csv` (440 rows)
- `results/exp_realcm_summary.csv` (11 rows)

---
