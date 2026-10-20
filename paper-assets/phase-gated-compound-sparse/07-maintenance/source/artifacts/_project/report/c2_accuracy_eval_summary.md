# C2 Accuracy Evaluation Summary — MATH-500 (n=50)

## Server Files
All results stored on westd-22162 at `/root/autodl-tmp/pacs/analysis_output/`:
- `accuracy_eval_ds_dense_n50.json` — DS dense baseline (extracted from ds_s015 dense section)
- `accuracy_eval_ds_s015.json` — DS s015 (dense + sparse)
- `accuracy_eval_ds_s030.json` — DS s030 (sparse only)
- `accuracy_eval_qw_s015.json` — QW s015 (dense + sparse)
- `accuracy_eval_qw_s030.json` — QW s030 (sparse only)
- `accuracy_eval_spike.json` — DS spike s025 (n=10, dense + sparse)

## Summary Table (n=50)

| Condition      | Dense Acc | Sparse Acc | Delta   | null_rate | trunc_rate | wrong_rate |
|----------------|-----------|------------|---------|-----------|------------|------------|
| DS dense       | 52% (26/50) | —       | —       | 46%       | 56%        | 2%         |
| DS s015        | 52%       | 34% (17/50)| -18pp  | 50%       | 52%        | 16%        |
| DS s030        | 52%       | 10% (5/50) | -42pp  | 64%       | 66%        | 26%        |
| QW dense       | 32% (16/50) | —       | —       | 10%       | 10%        | 58%        |
| QW s015        | 32%       | 32% (16/50)| 0pp    | 10%       | 8%         | 58%        |
| QW s030        | 32%       | 14% (7/50) | -18pp  | 20%       | 6%         | 66%        |

## Failure Mode Breakdown

### DeepSeek (thinking model, long CoT)
- Dense already truncates 56% of problems at max_new_tokens=2048
- **Wrong answer** rate increases from 2% → 16% → 26% as sparsity rises
- **Null answers** are almost entirely truncation-driven (trunc+null overlap is near-perfect)
- Extract failures (null but not truncated) are rare: 0 (dense), 1 (s015), 2 (s030)

### Qwen (non-thinking model, short generations)
- Dense truncation rate is only 10% — generations are much shorter
- **Wrong answer** is the dominant failure mode: 58% dense → 58% s015 → 66% s030
- Null answer rate is low even under sparsity (10% → 10% → 20%)
- QW s015 has zero accuracy degradation vs dense — sparsity is effectively invisible

## DS s030 Chinese Generation
- **20/50 problems (40%)** in DS s030 sparse condition have Chinese-language reasoning
- DS s015 sparse: only 2/50 (4%) have Chinese
- DS dense: 0/50 (0%) have Chinese
- Confirms: high sparsity (30%) triggers language switching in DeepSeek

## DS Spike s025 (n=10, early test)
- Dense: 40% (4/10), Sparse: 10% (1/10), Delta: -30pp
- Small sample, directionally consistent with n=50 results

## Key Takeaways
1. **DS is more sensitive to sparsity than QW** — DS loses 42pp at s030 vs QW losing 18pp
2. **Different failure modes**: DS fails via truncation (CoT too long), QW fails via wrong answers
3. **QW s015 is lossless** — 0pp degradation, compound sparsity at 15% is free for Qwen
4. **Language switching is a DS-specific pathology** at high sparsity (40% of problems at s030)
5. **DS dense 2048-token budget is insufficient** — 56% truncation means the dense baseline itself is constrained
