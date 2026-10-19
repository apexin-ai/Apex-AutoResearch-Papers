# deploy m008 fix and deploy 18228

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_m008-fix-and-deploy-18228_20260517T133303_result.json`
- **Structured JSON:** [`b993b638f083bc3b53f1.json`](../../sessions/b9/b993b638f083bc3b53f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**第 1 部分总结:**
- 3 个 ALIVE 进程已注册 registry (RUNNING) + cron 已存在
- 1 个 DEAD (`eval-obs-only-object-norm003-seed43`, PID 621127 on bjb1-18228) — 确认 batch7 误杀，已标记 DONE/failed

**第 2 部分总结:**
- bjb1-18228 全部 4 张 GPU 已部署：
  - cuda:0 → `eval-perdof-object-norm02-seed45-r2` (PID 634438)
  - cuda:1 → `eval-obs-only-object-norm005-seed43-r3` (PID 633649)
  - cuda:2 → `eval-obs-only-object-norm02-k5-seed42` (PID 633736)
  - cuda:3 → `eval-obs-only-object-norm02-k20-seed42` (PID 636713)
- nvidia-smi 验证 4 个进程均在正确 GPU 上运行
- 清理了前 Worker 遗留的 2 个残留 tmux session + 4 个 zombie GPU 进程

---
