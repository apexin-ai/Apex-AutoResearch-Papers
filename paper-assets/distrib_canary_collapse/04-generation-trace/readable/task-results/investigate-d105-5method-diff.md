# investigate d105 5method diff

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_d105_5method_diff_20260519T162829_result.json`
- **Structured JSON:** [`c0a04cc6b9a6250653af.json`](../../sessions/c0/c0a04cc6b9a6250653af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存并注册。核心发现：

**K≥4 差异根因：`d102_rerun_8pair.py` 的 leadlag consensus 对 naive_xcorr 的方向过滤器符号反转。** `peak_lag > 0` 在 method_ablation.py 的 lag 约定下 = downstream 领先 canary（错误方向）。6/8 pair 的 canary 领先证据（peak_lag=-1）被错误排除，2/8 pair 的 downstream 领先证据反而被计入。

**论文应使用 `unified_5method.json`**（K≥4=8/8），不含方向 bug，有完整 FDR 三级显著性。

Task 3 收尾：
- (a) "Rev 3/8" claim 在当前 registry 102 条记录中不存在，无需操作
- (b) `scale_14b_a100_s42_fp32` 不存在；14B s42 的 `5method_summary.txt` 确认用旧 →ppl 数据，但 `unified_5method.json` 已有正确 D102 数据，无需重生成

---
