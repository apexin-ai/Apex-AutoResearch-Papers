# diagnose mvp1 baseline std remaining

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mvp1_baseline_std_remaining_20260516T025156_result.json`
- **Structured JSON:** [`eb3fa9a22308dc1e47a9.json`](../../sessions/eb/eb3fa9a22308dc1e47a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态无法从 DONE 回退到 RUNNING。notes 已更新。

## 诊断结果

**进程仍在运行**，cron 再次误报（第4次）。这是已知问题：eval 脚本按 suite 顺序执行，父 PID 变化触发 cron 误判。

**已完成 suite 的 Success Rate：**

| Suite | SR | 详情 |
|-------|-----|------|
| libero_spatial | **66.0%** | 330/500 (10 tasks × 50 eps) |
| libero_object | **67.8%** | 339/500 (10 tasks × 50 eps) |
| libero_goal | **76.4%** | 382/500 (10 tasks × 50 eps) |
| libero_10 | **进行中** | task_0 已跑完 10 eps，无 eval_info.json |

**Registry 状态：** cron 已自动标记 status=DONE, conclusion=failed，但无法回退到 RUNNING（状态机限制）。notes 已更新记录实际情况。

**建议：** 保留 cron 等 libero_10 跑完后再最终判定。libero_10 有 10 tasks × 50 eps，当前进度约 2%，预计还需数小时。

---
