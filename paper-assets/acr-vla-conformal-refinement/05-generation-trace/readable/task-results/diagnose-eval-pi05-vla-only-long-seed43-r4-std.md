# diagnose eval pi05 vla only long seed43 r4 std

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-pi05-vla-only-long-seed43-r4-std_20260522T165418_result.json`
- **Structured JSON:** [`ef58239e949e0ea16a05.json`](../../sessions/ef/ef58239e949e0ea16a05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**`eval-pi05-vla-only-long-seed43-r4-std` 从未实际运行。** 这是一个孤立的 registry 条目。

具体发现：

1. **服务器上不存在任何带 `-std` 后缀的文件**：`find /root/ -name "*seed43*r4*std*"` 返回空。

2. **存在一个名字相近但不同的已完成实验**：`eval-pi05-vla-only-long-seed43-r4`（无 `-std`），日志在 `/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-long-seed43-r4.log`。该实验**成功完成**，EXIT_CODE=0，整体成功率 **95.5% (191/200)**，结果保存在 `logs/eval_long_vla_only_seed43_r4.json`。

3. **无相关残留进程**。

4. **失败原因**：`-std` 变体在 registry 中被创建（PREPARING 状态）但从未被提交执行。cron 回调监控了一个不存在的进程，自然报告 "Process exited without valid W&B metrics"。

**建议操作**：将 registry 中 `eval-pi05-vla-only-long-seed43-r4-std` 标记为 CANCELLED 或删除。无需重跑——无 `-std` 版本已成功完成。

---
