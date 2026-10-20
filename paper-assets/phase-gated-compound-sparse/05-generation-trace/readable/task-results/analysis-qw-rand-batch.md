# analysis qw rand batch

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qw_rand_batch_20260514T082557_result.json`
- **Structured JSON:** [`4479e07061f9a263ccbe.json`](../../sessions/44/4479e07061f9a263ccbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验全部确认：DONE + conclusion=success + checkpoint_path 已设置 + metrics 非空。

**汇总：**

| 实验 | Median II (high/mid/low) | Median CI 重叠 | Verdict |
|------|--------------------------|---------------|---------|
| bf16_qw_rand_s015 | 0.14 / 0.22 / 0.19 | 完全重叠 | FAIL |
| bf16_qw_rand_s020 | 0.49 / 0.77 / 0.61 | 完全重叠 | FAIL |
| bf16_qw_rand_s025 | 1.60 / 2.22 / 2.26 | 完全重叠 | FAIL |

三个 Qwen random masking 负对照均为 FAIL（预期），与 DeepSeek random 系列结论一致：random masking 不产生 phase-dependent interaction pattern。Registry 已全部更新完毕。

---
