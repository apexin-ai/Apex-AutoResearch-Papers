# code permutation test median fix

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_permutation-test-median-fix_20260514T065914_result.json`
- **Structured JSON:** [`6e9e5e056bb21784d153.json`](../../sessions/6e/6e9e5e056bb21784d153.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**修改了 3 个文件，commit `1b4f61a`：**

1. **`interaction_index.py`** — `bootstrap_interaction_index` 现在同时 bootstrap mean 和 median，返回 dict 包含 `median_ci_low`/`median_ci_high`

2. **`run_profiling.py`** — 5 处改动：
   - `evaluate_pass_fail`：CI overlap 和 sign reversal 检测改用 median CI（向后兼容 `.get()` 回退）
   - bootstrap caller：适配新 dict 返回值
   - `ii_out`：输出包含 `median_ci_low`/`median_ci_high`
   - EPS guard：`ppl_d > 1e-10`
   - Print summary：显示 median CI

3. **`metrics.py`**（先前未提交）：NaN/Inf CE loss 过滤

**验证结果：** v6_random_s030_r3 verdict 从 PASS → FAIL。三个 phase 的 median II 均为正值（high=2.50, mid=2.59, low=4.04），无 sign reversal，符合 random masking 无 phase 区分的预期。

---
