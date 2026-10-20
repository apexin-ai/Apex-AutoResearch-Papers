# analysis v6 random s030 r3

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v6_random_s030_r3_20260514T061854_result.json`
- **Structured JSON:** [`b00957e6ed24d68bb202.json`](../../sessions/b0/b00957e6ed24d68bb202.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## v6_random_s030_r3 结果

**状态：** 完成，EXIT_CODE=0，Verdict=**PASS**

### Interaction Index (s=0.30, random masking)

| Phase | Mean | Median | Winsorized Mean | 95% CI | Skewness | Outliers |
|-------|------|--------|-----------------|--------|----------|----------|
| high_sparsity | **+9.2364** | 4.0237 | 11.7140 | [+2.51, +15.07] | -5.76 | 9 |
| mid_sparsity | **-230.7604** | 2.4272 | 6.5105 | [-659.62, -3.94] | -13.08 | 1 |
| low_sparsity | **-7.4119** | 4.7350 | 9.9636 | [-41.63, +15.06] | -14.60 | 4 |

### Perplexity (s=0.30)

| Phase | Dense | Attn-only | KV-only | Both |
|-------|-------|-----------|---------|------|
| high | 1.169 | 24.29 | 6.86 | 39.18 |
| mid | 1.227 | 382.65 | 7.38 | 27.44 |
| low | 1.228 | 94.88 | 9.88 | 88.94 |

### Phase Stats
- high: 21,086 tokens / 387 segments
- mid: 13,306 tokens / 191 segments
- low: 27,748 tokens / 397 segments

### Pass/Fail Tests
- **CI overlap test:** PASS — high vs mid CI non-overlapping
- **Sign reversal test:** PASS — high II>0, mid II<0
- **Overall:** PASS

### 注意点
- mid_sparsity 的 mean (-230.76) 被极端 outlier 严重拉偏，winsorized_mean (6.51) 和 median (2.43) 均为正值，说明是少数 problem 的极端负值造成
- low_sparsity 同理：mean=-7.41 但 median=4.74, winsorized_mean=9.96
- per_problem_ii 中 problem 42 (number_theory/427) 的 ii_mid=null（0 个 mid segments）
- 50 problems 全部处理完成

### 输出文件
- `/root/autodl-tmp/pacs/profiling_output_v6_random_s030_r3/profiling_results.json` (1.9MB)

---

关于消息末尾的 `allocate_and_submit` 调用（bf16_ds_rand_s015）：我没有 `allocate_and_submit` 工具。如需启动该实验，请提供可用的执行方式。

---
