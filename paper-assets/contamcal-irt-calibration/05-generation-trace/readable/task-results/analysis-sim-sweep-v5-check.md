# analysis sim sweep v5 check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sim-sweep-v5-check_20260515T044642_result.json`
- **Structured JSON:** [`73bd38f5f447ae2e293c.json`](../../sessions/73/73bd38f5f447ae2e293c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程仍在运行（PID 652931，已跑 4h19m），最近文件更新在 04:36（~25 分钟前），仍在活跃产出。

**进度：102/120 seeds 完成**

| AUC | Done | OK | Fail | 成功率 |
|-----|------|----|------|--------|
| 0.55 | 30/30 | 27 | 3 | 90% |
| 0.65 | 17/30 | 0 | 17 | **0%** |
| 0.80 | 29/30 | 29 | 0 | 100% |
| 0.90 | 26/30 | 16 | 10 | 62% |

**剩余 18 seeds**：auc0.65×13, auc0.8×1, auc0.9×4

**失败原因**：全部 30 个失败都是 `[Errno 122] Disk quota exceeded`，不是模型收敛问题。auc0.65 的 17 个 fail 和 auc0.9_n100 的 10 个 fail 以及 auc0.55_n100 的 3 个 fail 都是磁盘配额错误。当前磁盘实际有 50GB 空闲，可能是 Stan 临时文件触发了某个配额限制（inode 或 tmpdir），而非真正的空间不足。

如果配额问题已解决（进程在继续正常产出），剩余 18 seeds 可能会正常完成。但 auc0.65 之前的 17 个 fail 不会自动重跑，完成后需要 `--resume` 重试这些失败的 seeds。

---
