# analysis d213 6pair s42 conversion

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d213_6pair_s42_conversion_20260524T003745_result.json`
- **Structured JSON:** [`c151aceb330c8842cda1.json`](../../sessions/c1/c151aceb330c8842cda1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D213 完成。汇总表：

| exp_id | T | α | PermG_fwd | PermG_rev | Robust_K3 |
|--------|---|------|-----------|-----------|-----------|
| scale_14b_t10_a045_s42_fp32 | 10 | 0.45 | 0/6 | 0/6 | 0/6 |
| scale_14b_t10_a050_s42_fp32 | 10 | 0.50 | 4/6 | 0/6 | 3/6 |
| scale_14b_t10_a060_s42_fp32 | 10 | 0.60 | 4/6 | 0/6 | 3/6 |
| scale_14b_t10_a075_s42_fp32 | 10 | 0.75 | 5/6 | 0/6 | 5/6 |
| scale_14b_t15_a045_s42_fp32 | 15 | 0.45 | 3/6 | 0/6 | 4/6 |
| scale_14b_t15_a050_s42_fp32 | 15 | 0.50 | 3/6 | 0/6 | 2/6 |
| scale_14b_t15_a060_s42_fp32 | 15 | 0.60 | 6/6 | 0/6 | 6/6 |
| scale_14b_t15_a075_s42_fp32 | 15 | 0.75 | 6/6 | 0/6 | 6/6 |

数据分布在两台服务器：6 个在 17855 (`results/analysis/D102_14b_*_6pair.json`)，2 个在 19828 (`t10_a050_s42`, `t15_a075_s42`)。所有 PermG_rev = 0/6，方向性一致。合并 JSON 已注册为 artifact `D213_14b_s42_6pair_combined`。

---
