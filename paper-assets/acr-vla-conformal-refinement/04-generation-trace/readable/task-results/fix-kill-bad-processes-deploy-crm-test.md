# fix kill bad processes deploy crm test

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill-bad-processes-deploy-crm-test_20260522T162924_result.json`
- **Structured JSON:** [`4f147a6798b2ca882801.json`](../../sessions/4f/4f147a6798b2ca882801.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

### Kill 确认
- **bjb2-28827**: PID 314354, 326502, 326643 (native precompute) — **已 kill**，tmux sessions precompute-spatial-fixed / precompute-goal-fixed 已清理
- **bjb1-32546**: PID 448061 (cuda:5 未注册 CRM 训练) — **已 kill**，cuda:5 已释放 (2 MiB)

### Wrapper Precompute 进度 (bjb2-28827)
| Suite | 进度 | 速率 | ETA |
|-------|------|------|-----|
| object | 18000/28950 (62%) | 15.0 samples/s | ~12 min |
| spatial | 18500/24133 (77%) | 14.5 samples/s | ~6.5 min |
| goal | 18500/24752 (75%) | 15.0 samples/s | ~7 min |

**spatial 和 goal 约 7 分钟完成，object 约 12 分钟完成。**

### CRM 测试训练
**暂时无法启动** — bjb1-32546 上不存在 `crm_cache_smolvla_k10/` 目录，需等 bjb2-28827 precompute 全部完成后 rsync 过去。预计 ~12 分钟后数据就绪，之后可 rsync + 启动训练。

需要我等数据跑完后自动执行 rsync + 部署训练吗？

---
