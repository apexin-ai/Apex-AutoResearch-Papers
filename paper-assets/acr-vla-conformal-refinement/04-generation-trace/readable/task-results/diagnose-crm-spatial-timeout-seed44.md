# diagnose crm spatial timeout seed44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_crm-spatial-timeout-seed44_20260522T132355_result.json`
- **Structured JSON:** [`806888d0faa089c48b1b.json`](../../sessions/80/806888d0faa089c48b1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/diagnose_crm_spatial_timeout.md`。核心结论：

**失败原因：纯超时，无任何 error 或 hang。** 每个 episode 耗时 ~310 秒，200 episodes 需要 ~17.2 小时，但 timeout 仅 ~12 小时。

**完成进度：**
- Seed 42: 7/10 tasks (140/200 eps), 部分平均 90.0%
- Seed 43: 7/10 tasks (140/200 eps), 部分平均 85.7%
- Seed 44: 6.5/10 tasks (130/200 eps), 部分平均 82.3%
- 缺失 task 7/8/9，无 JSON 输出文件（进程被杀前未写入）

**特别发现：** `on_ramekin` task 跨三个 seed 平均仅 41.7%，远低于其他 task 的 93%+。

**建议：** 将 timeout 增至 20h (72000s) 重跑。不要改 n_action_steps=10，那会使运行时间变成 ~85h。

---
