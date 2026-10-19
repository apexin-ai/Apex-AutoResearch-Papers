# diagnose eval adaptive unc head seed42 fail

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-adaptive-unc-head-seed42-fail_20260520T193923_result.json`
- **Structured JSON:** [`2ef3827d9fac131fb964.json`](../../sessions/2e/2ef3827d9fac131fb964.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

memory.md 已有大量同类 false positive 记录。adaptive_unc_head 的情况完全匹配已知模式（eval 无 sentinel/W&B），无需新增条目。

补充 seed44 的结果到诊断结论。

## 最终诊断

**根因：监控 false positive（已知模式）。** 与 memory.md 第一条失败模式记录完全一致——eval 脚本不写 sentinel 也不上报 W&B，进程正常退出后 cron 5 次检测无标记 → 自动标记 failed。

**三个 seed 全部正常完成：**
- seed42: 14.0%, seed43: 11.0%, seed44: 11.0%
- 所有 seed 的 `mean_l2=0.0000, avg_k=1.0` → uncertainty head 实质未执行任何修正（K=1 无候选比较，correction 为零）
- `fast_path ≈ 12%` → 88% step 的 uncertainty 超阈值但无修正能力

**不是代码 bug、OOM、环境问题。** 是监控 infra 的已知缺陷 + 方法本身无效（与 D090 NO-GO 判定一致）。

同服务器 `eval-obs-only-object-norm003-seed43`（SR=14.0%）和 `eval-obs-only-object-norm02-seed43-r3`（运行中/已完成）同样正常，非系统性故障。

---
