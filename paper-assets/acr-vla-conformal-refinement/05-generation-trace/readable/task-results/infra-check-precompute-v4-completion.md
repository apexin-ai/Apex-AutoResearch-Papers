# infra check precompute v4 completion

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-precompute-v4-completion_20260513T200703_result.json`
- **Structured JSON:** [`77bc57d3a34ddf8424b2.json`](../../sessions/77/77bc57d3a34ddf8424b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### Precompute-v4 状态
| Shard | 进程 | spatial | object | Merge |
|-------|------|---------|--------|-------|
| shard0 | 已退出 | 完成 | 完成 (4857/4857) | 跳过（shard2未完成） |
| shard1 | 已退出 | 完成 | 完成 (4857/4857) | 跳过（shard0未完成） |
| shard2 | 已退出 | 完成 | 完成 (4856/4856) | **触发 merge 成功** |

### Cache 完整性
- **spatial**: manifest ✓, 12167 samples, 3 merged files齐全
- **object**: manifest ✓, 14570 samples, merge 由 shard2 完成

### CRM 训练已启动
- **exp_id**: `crm-train-v1`
- **PID**: 78520 (实际 python 进程)
- **GPU**: cuda:1, 546 MiB
- **数据**: 26737 samples (spatial 12167 + object 14570), K=10
- **模型**: CRM 337,438 参数
- **进度**: epoch 1 batch 100/752, loss=0.0195（正常下降中）
- **配置**: 50 epochs, batch_size=32, lr=1e-3

---
