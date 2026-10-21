# ops check act256v2 alive

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-act256v2-alive_20260525T172248_result.json`
- **Structured JSON:** [`2c52bcf391fedba3f292.json`](../../sessions/2c/2c52bcf391fedba3f292.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**exp-act-256-v2 已死，被外部 kill。**

| 项目 | 详情 |
|------|------|
| 死因 | 外部 kill（日志无 error/OOM/exception） |
| 停止位置 | step 690/8000，01:09 UTC |
| 最新 checkpoint | checkpoint-500（完好） |
| Loss 趋势 | 收敛良好：sft 0.64 → 0.0085 |
| 模式 | v1 在 step 200 被 kill，v2 在 step 690 被 kill，同一台机器同一块卡 |

Registry 已更新为 DONE/killed。

**需要你决定**：是否立即重跑 v3？如果重跑，建议：
1. 从 checkpoint-500 resume（省 ~56 分钟）
2. 考虑用 cuda:1 而非 cuda:0，排除是否有其他 worker/cron 在抢 cuda:0

---
