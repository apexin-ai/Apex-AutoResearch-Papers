# check precompute status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_precompute-status_20260521T164051_result.json`
- **Structured JSON:** [`7e1f4ed73866c8dcf19d.json`](../../sessions/7e/7e1f4ed73866c8dcf19d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/precompute_status_check.md`（save_project_file 不允许该文件名，已改用直接写入 artifacts 目录）。

**关键结论**:
- **16/17 shard 在跑**, 0 完成, 无 merged 输出文件
- **最慢路径**: bjb2-40593 obj s0 (3.35s/sample, ETA ~2.5h) + bjb2-28827 spatial (~2.5h)
- **🚨 pipeline-auto 远程探测逻辑坏了**: SSH 检测三台远程服务器都返回 0 进程（实际有 16 个）, 只有 local=4 (spatial shard6 进程树)。spatial shard6 是进度最快的 (ETA 1.6h), 它一完, total=0 会**触发早 merge**, 而对象/空间其他 shard 还没好。必须先修复
- **失败迁移情况**: 6 个 -r2 attempt 在 bjb1-18228 上被 SIGTERM（s7/s8/s9）和 bjb1-32546 上被 SIGTERM（s5/s6），但 s5/s7/s8/s9 都已通过 -fix 进程在 bjb1-32546 重启，s6-r2 在原机继续；bjb2-40593 s0 经历 OOM + SIGHUP 后用 nohup 重启，活在 `/root/precompute_pi05_shard0.log`（不在 ~/runs/ 目录）
- **rsync 滞后**: bjb1-32546 (源) 255 partials vs bjb1-18228 (目标) 217 partials，差 ~38 个

---
