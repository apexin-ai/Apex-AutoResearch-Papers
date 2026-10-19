# monitor starcoder s43 eval1500 v2

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_starcoder-s43-eval1500-v2_20260515T015608_result.json`
- **Structured JSON:** [`af2fc3726bbd38b11f1d.json`](../../sessions/af/af2fc3726bbd38b11f1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**eval@1500 仍在计算中**，尚未出结果。

当前状态：
- 训练已到 step 1500（epoch 2），日志最后更新 09:52:10
- eval 已计算约 9 分钟，进程存活（PID 519805，CPU 95%），GPU 1 利用率 100%
- 日志尚无 eval@1500 输出

已知结果回顾：
| eval | val_loss | R@1 | 备注 |
|------|----------|-----|------|
| @500 | 0.5279 (best) | 0.4708 | |
| @1000 | 0.5430 | 0.4780 (best R@1) | patience 1/2 |
| @1500 | ? | ? | 计算中 |

**预期**：如果 val_loss > 0.5279 → patience 2/2 → early stop。Best checkpoint 路径：
- `best_by_val_loss`: `/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s43/best_by_val_loss`
- `best_by_recall_at_1`: `/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s43/best_by_recall_at_1`

需要稍后再查一次日志才能拿到 eval@1500 的具体数值。

---
