# audit failed experiments misdiagnosis

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_failed-experiments-misdiagnosis_20260520T112559_result.json`
- **Structured JSON:** [`dc0838573513b17f3983.json`](../../sessions/dc/dc0838573513b17f3983.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部更新完成。汇总：

```
实验ID                              | 服务器       | JSON存在? | 完整? | SR   | 结论    | 操作
------------------------------------|-------------|----------|-------|------|---------|---------------------------
eval-obs-only-object-norm003-seed44 | bjb2-28827  | ✅       | ✅    | 0.15 | success | 已清理 failure_reason（原已标 success）
eval-adaptive-k-spatial-p50-seed43  | bjb1-32546  | ✅       | ✅    | 0.33 | success | ✅ 误判修正：failed→success，添加 metrics
eval-adaptive-k-spatial-p50-seed44  | bjb2-28827  | ✅       | ✅    | 0.33 | success | ✅ 误判修正：failed→success，添加 metrics
eval-vla-only-spatial-seed48        | —           | ❌       | —     | —    | —       | Registry 中未找到此实验，所有服务器无 JSON
eval-vla-only-object-seed49         | bjb2-28827  | ❌       | —     | —    | killed  | 确认真实失败（无 JSON，conclusion=killed）
eval-vla-only-goal-seed48-r2        | bjb1-32546  | ❌       | —     | —    | failed  | 确认真实失败（ValueError: --checkpoint required）
```

**误判修正 2 个**：adaptive-k-spatial-p50 的 seed43/seed44 都是 EXIT_CODE=2（提交命令路径 `evaluate.py` vs `src/evaluate.py` 错误），但实际上已有另一个进程完成了评估并写出了完整 JSON。两个 seed 的 SR 均为 0.33，与对应 r2 重跑版本一致。

**eval-vla-only-spatial-seed48**：在 bjb2-28827、bjb2-40593、bjb1-18228 上均未找到对应的 JSON 或 log 文件，registry 中也没有此实验条目，可能从未实际提交过。

---
