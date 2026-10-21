# code check scoring ablation v2 logs

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check_scoring_ablation_v2_logs_20260517T090931_result.json`
- **Structured JSON:** [`5976d8fffc8299b2039e.json`](../../sessions/59/5976d8fffc8299b2039e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### scoring_ablation_batch_v2 (cuda:0) — **PARTIAL FAILURE**

该 session 的 cron 日志**只运行了 magnitude**（不是 gradient）：
1. **magnitude prune** — 完成，18.99% sparsity
2. **magnitude eval** — 在 60/200 时被 Terminated（acc=0.0000）
3. magnitude SFT/post-SFT — 未执行

日志只有 107 行，无 gradient 记录。tmux session 仍存在但进程已结束。

### gradient（单独运行，非 batch_v2）— **PARTIAL FAILURE**

| 步骤 | 状态 | 结果 |
|------|------|------|
| prune | ✅ 完成 | 保存到 pruned_gradient_20 (12G) |
| eval post-prune | ✅ 完成 | **accuracy = 0.255 (25.5%)** |
| SFT | ❌ 失败 | step 935/1870 (50%) 磁盘满 |
| eval post-SFT | ❌ 未执行 | — |

### random (scoring_ablation_random, cuda:1) — **IN PROGRESS**

- prune 完成 (20.04% sparsity)
- eval post-prune 进行中：**26/200 (13%)**，速度 ~20-50s/it

### cka_only — 未发现独立 session/日志

### 关键问题：**数据盘 100% 满**

```
/dev/md0  250G  250G  1.2M  100%  /root/autodl-tmp
```

磁盘上有大量旧模型目录（共约 180G+ pruned/sft 文件）。gradient SFT 因此失败，random 后续 SFT 也必然会失败。需要清理空间后重跑 gradient SFT 和 magnitude 全流程。

---
