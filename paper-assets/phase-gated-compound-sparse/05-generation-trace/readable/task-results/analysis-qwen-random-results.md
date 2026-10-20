# analysis qwen random results

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen_random_results_20260514T082541_result.json`
- **Structured JSON:** [`dd1ee99c38eb1338e74c.json`](../../sessions/dd/dd1ee99c38eb1338e74c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 全部更新完成。汇总：

| exp_id | sparsity | median (high→mid→low) | median_diff | pass_fail | n_problems |
|--------|----------|----------------------|-------------|-----------|------------|
| bf16_qw_rand_s015 | 0.15 | 0.138 → 0.219 → 0.188 | **+0.050** | **FAIL** (sign_reversal + ci_overlap) | 50 |
| bf16_qw_rand_s020 | 0.20 | 0.485 → 0.767 → 0.614 | **+0.129** | **FAIL** (sign_reversal + ci_overlap) | 50 |
| bf16_qw_rand_s025 | 0.25 | 1.604 → 2.222 → 2.264 | **+0.660** | **FAIL** (ci_overlap, no sign reversal) | 50 |

符合预期：random masking 在 Qwen2.5-7B-Instruct 上全部 FAIL。

- s015/s020 存在 sign reversal（mid > low，违反单调递增），且 CI 重叠严重
- s025 的 median 碰巧单调递增，但各 phase CI 大幅重叠，无统计显著性
- median_difference 均为小正值（0.05~0.66），远小于 importance-based masking 实验中的差异
- 与 DeepSeek random 实验结果一致：random masking 不产生有意义的 phase 间单调效应

---
